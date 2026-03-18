import pandas as pd

def calculate_risk(row):
    score = 0

    if row['on_time_delivery_rate'] < 0.8:
        score += 1
    if row['defect_rate'] > 0.07:
        score += 1
    if row['lead_time_days'] > 10:
        score += 1
    if row['financial_risk_score'] > 0.5:
        score += 1

    if score >= 3:
        return "HIGH RISK"
    elif score == 2:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


df = pd.read_csv('../data/supplier_data.csv')
df['risk_level'] = df.apply(calculate_risk, axis=1)

print(df[['supplier_name', 'risk_level']])
