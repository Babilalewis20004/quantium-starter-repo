import pandas as pd
import glob

# Step 1: Get all CSV files in the data folder
csv_files = glob.glob("*.csv") 
print("CSV files found:", csv_files)

# Step 2: Load and process each CSV
processed_dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Keep only Pink Morsels
    df = df[df['product'] == 'pink morsel']
    
    # Calculate Sales
    df['Sales'] = df['quantity'] * df['price']
    
    # Keep only relevant columns and rename
    df = df[['Sales', 'date', 'region']]
    df.rename(columns={'date': 'Date', 'region': 'Region'}, inplace=True)
    
    processed_dfs.append(df)

# Step 3: Combine all processed data into a single DataFrame
final_df = pd.concat(processed_dfs, ignore_index=True)

# Step 4: Save the final output CSV
final_df.to_csv('formatted_sales.csv', index=False)

print("Formatted CSV saved as 'formatted_sales.csv'")
