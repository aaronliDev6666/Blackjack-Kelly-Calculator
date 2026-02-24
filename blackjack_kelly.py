# blackjack_kelly.py
# Python 3 程序：点数检测 + A 灵活处理 + 基础胜率 + Hi-Lo 修正 + 凯利公式

def hi_lo_value(card):
    if card in ["2","3","4","5","6"]:
        return 1
    elif card in ["7","8","9"]:
        return 0
    elif card in ["10","j","q","k","a"]:
        return -1
    else:
        raise ValueError("无效牌面")

def hand_value(cards):
    """计算手牌点数，自动处理 A = 1 或 11"""
    values = []
    for c in cards:
        if c in ["j","q","k"]:
            values.append(10)
        elif c == "a":
            values.append(11)
        else:
            values.append(int(c))
    total = sum(values)
    ace_count = cards.count("a")
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def is_blackjack(cards):
    return len(cards) == 2 and (
        ("a" in cards) and any(c in ["10","j","q","k"] for c in cards)
    )

def base_win_rate(total):
    """根据点数设定基础胜率"""
    if total <= 16:
        return 0.50
    elif total == 17:
        return 0.52
    elif total == 18:
        return 0.54
    elif total == 19:
        return 0.56
    elif total == 20:
        return 0.58
    elif total == 21:
        return 0.99
    else:
        return 0.0

def kelly_fraction(p, b=1):
    q = 1 - p
    f = (b * p - q) / b
    return max(f, 0)

def main():
    print("=== Blackjack 凯利公式计算器 (基础胜率 + Hi-Lo 修正) ===")
    print("输入牌面 (如: a 10)，输入 'exit' 退出程序")
    while True:
        cards = input("请输入牌面: ").lower().split()
        if cards[0] == "exit":
            print("程序结束。")
            break

        total = hand_value(cards)

        if total > 21:
            # 爆牌
            p = 0.0
            b = 1
            f = 0.0
            half_f = 0.0
            print(f"点数: {total} → 爆牌！胜率 = 0%")
        elif total == 21:
            # Blackjack 特殊情况
            if is_blackjack(cards):
                p = 0.99
                b = 1.5
                print("检测到 Blackjack! 胜率 ≈ 100%")
            else:
                p = 0.99
                b = 1
                print("检测到 21 点! 胜率 ≈ 100%")
            f = kelly_fraction(p, b)
            half_f = f / 2
        else:
            # <21 用基础胜率 + Hi-Lo 修正
            running_count = sum(hi_lo_value(c) for c in cards)
            decks_remaining = 4
            true_count = running_count / decks_remaining
            edge = true_count * 0.005
            base_p = base_win_rate(total)
            p = min(base_p + edge, 0.99)  # 胜率不超过 99%
            b = 1
            f = kelly_fraction(p, b)
            half_f = f / 2
            print(f"点数: {total}")
            print(f"基础胜率: {base_p*100:.2f}%")
            print(f"Running Count: {running_count}, True Count: {true_count:.2f}")
            print(f"优势修正: {edge*100:.2f}% → 最终胜率: {p*100:.2f}%")

        print(f"凯利下注比例: {f*100:.2f}%")
        print(f"半凯利下注比例: {half_f*100:.2f}%")
        print("-" * 40)

if __name__ == "__main__":
    main()
