def calculate_delivery_cost(distance: int, size: str, fragile: bool, workload: str) -> int:
    total_cost: int = 0

    if distance > 30:
        total_cost += 300
    elif distance > 10:
        total_cost += 200
    elif distance > 2:
        total_cost += 100
    else:
        total_cost += 50

    if size == "small":
        total_cost += 100
    elif size == "big":
        total_cost += 200
    else:
        raise ValueError("Введен неверный размер габаритов груза. Допустимые значения: small, big")

    if fragile and distance > 30:
        raise Exception("Хрупкие грузы нельзя возить на расстояние более 30 км")
    elif fragile:
        total_cost += 300

    if workload == "very high":
        total_cost *= 1.6
    elif workload == "high":
        total_cost *= 1.4
    elif workload == "increased":
        total_cost *= 1.2
    elif workload not in ["very high", "high", "increased", "normal"]:
        raise ValueError(
            "Введена неверная загруженнось службы доставки. Допустимые значения: very high, high, increased, normal")

    return int(max(total_cost, 400))


print(calculate_delivery_cost(40, "small", fragile=False, workload="normal"))