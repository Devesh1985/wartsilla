import pytest
from wartsila_int import calculate_soc

def test_calculate_soc():
    # Test cases based on expected SOC calculations
    assert calculate_soc(0.5, 0, 0.80) == 0.8  # No change in SOC
    assert round(calculate_soc(0.5, 50, 0.80), 2) == 0.52  # Discharging
    assert round(calculate_soc(0.5, -25, 0.52), 2) == 0.63  # Charging
    assert round(calculate_soc(0.5, -25, 0.63), 2) == 0.75  # Charging again