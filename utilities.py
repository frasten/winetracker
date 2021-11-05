def parseItaPrice(string: str) -> float:
    string = string.replace(",", ".").replace("€", "").strip()
    return float(string)
