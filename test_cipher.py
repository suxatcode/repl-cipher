import cipher
import pytest


@pytest.mark.parametrize("name, alphabet, plaintext, expected", [
    [
        "simple translation",
        [
            "ABC",
            "BAC",
        ],
        "AAACB",
        "BBBCA",
    ],
    [
        "character not specified in alphabet should be ignored",
        [
            "ABC",
            "BAC",
        ],
        "AAACBF",
        "BBBCAF",
    ],
])
def test_cipher_2(name, alphabet, plaintext, expected):
    assert cipher.cipher(alphabet, plaintext), expected
