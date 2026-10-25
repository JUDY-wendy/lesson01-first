"""Compound interest calculator for lesson 01."""

from __future__ import annotations


def calculate(principal: float, annual_rate: float, years: int, compounds_per_year: int = 1) -> tuple[float, float, float]:
    """Return (compound total, simple total, difference)."""
    if principal <= 0:
        raise ValueError("本金必须大于 0")
    if annual_rate < 0:
        raise ValueError("利率不能为负")
    if years <= 0:
        raise ValueError("年限必须大于 0")
    if compounds_per_year <= 0:
        raise ValueError("复利频率必须大于 0")
    compound = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)
    simple = principal * (1 + annual_rate * years)
    return compound, simple, compound - simple


def read_number(prompt: str, integer: bool = False) -> float | int:
    while True:
        try:
            value = int(input(prompt)) if integer else float(input(prompt))
            if integer and value <= 0:
                raise ValueError
            if not integer and value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("请输入大于 0 的有效数值。")


def main() -> None:
    principal = read_number("请输入本金（元）：")
    while True:
        try:
            rate = float(input("请输入年利率（例如 0.05 表示 5%）："))
            if rate < 0:
                print("利率不能为负，请重新输入。")
                continue
            break
        except ValueError:
            print("请输入有效利率。")
    years = read_number("请输入年限（年）：", integer=True)
    rows = []
    for n in (1, 12):
        compound, simple, difference = calculate(principal, rate, years, n)
        rows.append(("年复利" if n == 1 else "月复利", compound, simple, difference))
    print("\n方式     复利终值（元）  单利终值（元）  差额（元）")
    print("-" * 55)
    for name, compound, simple, difference in rows:
        print(f"{name:<6} {compound:>14,.2f} {simple:>14,.2f} {difference:>12,.2f}")


if __name__ == "__main__":
    main()
