import pytest
from foo.advanced_volume import calculate_advanced_volume

def test_calculate_advanced_volume():
    # Test normal cases with default precision
    assert calculate_advanced_volume(1) == 4.18879
    assert calculate_advanced_volume(0) == 0
    assert calculate_advanced_volume(2.5) == 65.44985

    # Test normal cases with specified precision
    assert calculate_advanced_volume(1, precision=3) == 4.189
    assert calculate_advanced_volume(2.5, precision=4) == 65.4498

    # Test negative radius case
    with pytest.raises(ValueError):
        calculate_advanced_volume(-1)

    # Test large radius case with precision
    assert calculate_advanced_volume(1000, precision=2) == 4188790204.79
