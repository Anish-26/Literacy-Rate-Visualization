import geopandas as gp
import pandas as pd
from shapely import wkt

# Load Source GeoJSON
print("Loading source GeoJSON...")
df_geo = gp.read_file(r"c:\Users\Anish\OneDrive\Desktop\minor\GEOJASON\indian_states_clean_final.geojson")
df_geo = df_geo.rename(columns={"state_name": "State Name"})
df_geo["State Name"] = df_geo["State Name"].str.upper()

# Explicitly map names to match CSV
name_map = {
    "DADRA AND NAGAR HAVELI AND DAMAN AND DIU": "DADRA AND NAGAR HAVELI",
    "JAMMU AND KASHMIR AND LADAKH": "JAMMU AND KASHMIR"
}
df_geo["State Name"] = df_geo["State Name"].replace(name_map)

# Load CSV
print("Loading CSV data...")
df_csv = pd.read_csv(r"c:\Users\Anish\OneDrive\Desktop\minor\DATA\Clean\clean_SDG4.csv")
df_csv["State Name"] = df_csv["State Name"].str.upper()

# Merge
print("Merging data...")
df_merged = pd.merge(df_csv, df_geo, on="State Name", how="inner")

print(f"Merged states count: {len(df_merged)}")
missing_csv = set(df_csv["State Name"]) - set(df_merged["State Name"])
if missing_csv:
    print(f"Still missing from CSV: {missing_csv}")
else:
    print("All CSV states successfully matched and included!")

# Save as actual GeoJSON
output_path = r"c:\Users\Anish\OneDrive\Desktop\minor\OUTPUT\Map_data_restored.geojson"
print(f"Saving to {output_path}...")
df_merged = gp.GeoDataFrame(df_merged, geometry='geometry')
df_merged.to_file(output_path, driver='GeoJSON')

print("Success! Restored map data created.")
