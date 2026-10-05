def calculate_summary(data):
    total_income = 0
    total_expense = 0
    categories = {}

    for t in data["transactions"]:
        amt = t["amount"]
        if t["type"] == "income":
            total_income += amt
        elif t["type"] == "expense":
            total_expense += amt
            cat = t.get("category", "Lain-lain")
            categories[cat] = categories.get(cat, 0) + amt

    net_balance = total_income - total_expense
    
    total_flow = total_income + total_expense
    income_pct = (total_income / total_flow * 100) if total_flow > 0 else 0
    expense_pct = (total_expense / total_flow * 100) if total_flow > 0 else 0

    burn_rate = (total_expense / total_income * 100) if total_income > 0 else (100.0 if total_expense > 0 else 0)

    if burn_rate <= 50:
        status = "AMAT HEMAT"
        color = "green"
    elif burn_rate <= 80:
        status = "WASPADA"
        color = "yellow"
    else:
        status = "BOROS BANGET!"
        color = "bold red"

    category_percentages = {}
    if total_expense > 0:
        for cat, amt in categories.items():
            category_percentages[cat] = (amt / total_expense) * 100

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance,
        "income_pct": income_pct,
        "expense_pct": expense_pct,
        "burn_rate": burn_rate,
        "status": status,
        "color": color,
        "category_percentages": category_percentages
    }