from delivery_cost_calculator import calculate_delivery_cost
import pytest


class TestDeliveryCostCalculator:
    @pytest.mark.parametrize("distance, size, fragile, workload , expected", [
        (30, "big", False, "very high", 640),
        (10, "small", True, "increased", 600),
        (2, "big", False, "normal", 400),  # Кейс на минимальную сумму
        (40, "small", False, "normal", 400),
        (15, "small", True, "high", 840),
    ])
    def test_delivery_cost_calculations(self, distance, size, fragile, workload, expected):
        assert expected == calculate_delivery_cost(distance, size, fragile, workload)

    def test_fragile_exception_error(self):
        with pytest.raises(Exception):
            calculate_delivery_cost(distance=40, size="small", fragile=True, workload="normal")

    def test_size_value_error(self):
        with pytest.raises(ValueError):
            calculate_delivery_cost(distance=30, size="wrong size", fragile=True, workload="normal")

    def test_workload_value_error(self):
        with pytest.raises(ValueError):
            calculate_delivery_cost(distance=15, size="small", fragile=True, workload="wrong workload")