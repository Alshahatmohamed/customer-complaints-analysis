
import pandas as pd
df = pd.read_excel('shipping_complaints_dataset.xlsx')
print(df.head())
  

#step 2 : Preliminary Data Checking


#Public information about columns and Data types
print("\n---column information ---")
print(df.info())
# Statistical description for digital Data
print("\n--- statistical desciption ---")
print(df.describe())
# Checking for missing Data
print("\n---Number of missing values in each column ---")
print(df.isnull().sum())



# step 3 : Data cleaning 


print("\n---Checking for missing values ---")
print(df.isnull().sum())

# remove rows with any missing values (if needed)
df_cleaned =df.dropna()
 
print("\n---Checking for Duplicates ---")
print(f"Number of duplicate rows: {df_cleaned.duplicated().sum()}")

# remove duplicate rows 
df_cleaned =df_cleaned.drop_duplicates()

print("\n---Cleaned Date Preview ---")
print(df_cleaned.head())


# Step 4: save cleaned Data
# Save to new Excel file 
df_cleaned.to_excel("cleaned_shipping_complaints_dataset.xlsx",  index=False )
print("cleaned Data have neen saved to 'cleaned_shipping_complaints_dataset.xlsx'")
