import pandas as pd
from pathlib import Path

CLEAN = Path("data/cleaned")

master_path = CLEAN / "pfand_2022_master.csv"
backup_path = CLEAN / "pfand_2022_master_FULL_backup.csv"

df = pd.read_csv(master_path)

# Backup original
df.to_csv(backup_path, index=False)
print("Backup saved:", backup_path)

# Dashboard scope only
keep = ["Glas", "Aluminium", "Kunststoff"]
df_fixed = df[df["material"].isin(keep)].copy()

# Convert numeric columns, coercing errors to NaN
for col in ["pfand_input_kt", "total_recycled_kt", "recycling_rate_pct"]:
    if col in df_fixed.columns:
        df_fixed[col] = pd.to_numeric(df_fixed[col], errors="coerce")

df_fixed.to_csv(master_path, index=False)
print("Fixed saved:", master_path)
print(df_fixed)
