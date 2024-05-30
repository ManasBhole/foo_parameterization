import pytest
from foo.volume import calculate_volume

def test_calculate_volume():
    # Test normal cases
    assert calculate_volume(1) == 4.1887902047863905
    assert calculate_volume(0) == 0
    assert calculate_volume(2.5) == 65.44984694978735

    # Test negative radius case
    with pytest.raises(ValueError):
        calculate_volume(-1)

    # Test large radius case
    assert calculate_volume(1000) == 4188790204.7863903
