import pytest

from morse import decode


test_cases = [
    ('... --- ...', 'SOS'),
    ('.---- ..--- ...-- ....-', '1234'),
    ('.-- .... --- ..--..', 'WHO?')
]


@pytest.mark.parametrize(
    'morse_message, decoded_message',
    test_cases, ids=['SOS', '1234', 'WHO?']
)
def test_decode(morse_message, decoded_message):
    assert decode(morse_message) == decoded_message
