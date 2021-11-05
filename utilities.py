def parse_italian_price(string: str) -> float:
    string = string.replace(",", ".").replace("€", "").strip()
    return float(string)
