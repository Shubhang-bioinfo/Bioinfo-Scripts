import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

print("Setup Complete ")

ngs_filepath = "" ### Enter the .csv file path
data = pd.read_csv(ngs_filepath, index_col= "Year",parse_dates=True)
print(f"{data}\n")

df = pd.read_csv("") ### Enter the .csv file path
# Convert 'Year' to year-only integers
df['Year'] = pd.to_datetime(df['Year']).dt.year
# Reshape from wide to long
df_long = pd.melt(df, id_vars=['Year'],var_name='Omic_Type',value_name='Publications')
print(f"{df_long}")

plt.figure(figsize=(12, 8))
sns.kdeplot(data=df_long, x='Year', weights='Publications', hue='Omic_Type', fill=True, alpha=0.4)
plt.title("Relative Density of Omics Publications (2020–2025): Evidence of Multi-Omics Underrepresentation", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Density of Publications", fontsize=12)
plt.xlim(2020, 2025)  # Limit to your actual data range
plt.xticks(range(2020, 2026))  # Tighter year ticks for clarity
sns.set_style("whitegrid")
plt.show()

plt.figure(figsize=(12,6))
plt.title("Annual Omics Publications with Total Counts Annotated", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Publications", fontsize=12)
plt.xticks(range(2020, 2026))
sns.set_style("whitegrid")
sns.lineplot(data=data)
plt.show()

df = pd.read_csv("") ### Enter the .csv file path
df['Year'] = pd.to_datetime(df['Year']).dt.year
# Reshape to Long Format
df_long = pd.melt(df, id_vars=['Year'],var_name='Omic_Type',value_name='Publications')
# Calculate Total Publications per Omic Type
totals = df_long.groupby("Omic_Type")["Publications"].sum()
# KDE Plot
plt.figure(figsize=(15, 10))
sns.kdeplot(data=df_long, x='Year', weights='Publications', hue='Omic_Type', fill=True, alpha=0.4)
plt.title("Relative Density of Omics Publications (2020–2025): Evidence of Multi-Omics Underrepresentation", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Density of Publications", fontsize=12)
plt.xlim(2020, 2025)
plt.xticks(range(2020, 2026))
sns.set_style("white")
# Add Total Publications as Text Box Inside Plot
text = "\n".join([f"{omic}: {total}" for omic, total in totals.items()])
plt.text(2025.1, 0.02, text, fontsize=10, va='top', ha='left')
plt.show()

# Load Data
df = pd.read_csv("") ### Enter the .csv file path
df['Year'] = pd.to_datetime(df['Year']).dt.year

# Reshape to Long Format
df_long = pd.melt(df, id_vars=['Year'],var_name='Omic_Type',value_name='Publications')

# Scatter Plot for Multiple Omic Types
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df_long, x='Year', y='Publications', hue='Omic_Type', s=150, alpha=0.8, edgecolor='black')
plt.title("Scatter Plot of Omics Publications (2020–2025)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Publications", fontsize=12)
plt.xticks(range(2020, 2026))
sns.set_style("whitegrid")
plt.legend(title="Omic Type")
plt.tight_layout()
plt.show() 
