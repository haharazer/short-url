import redis
import random
from config import HOST

class UrlShorter:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)

    def gen_short_url(self, long_url):
        short_url = self.redis.get(long_url)
        if short_url:
            return HOST + '/u/' + short_url
        rand_id = random.randrange(1000000, 9999999)
        rand_str = base62_encode(rand_id)
        while self.redis.get(rand_str):
            rand_id = random.randrange(1000000, 9999999)
            rand_str = base62_encode(rand_id)
        self.redis.set(rand_str, long_url)
        self.redis.set(long_url, rand_str)
        return HOST + '/u/' + rand_str

    def get_long_url(self, code):
        return self.redis.get(code)


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num