import pandas as pd
import geopandas as gp

# Load CSV
csv_path = r"c:\Users\Anish\OneDrive\Desktop\minor\DATA\Clean\clean_SDG4.csv"
df_csv = pd.read_csv(csv_path)
csv_states = set(df_csv["State Name"].str.upper().unique())

# Load Source GeoJSON
geojson_path = r"c:\Users\Anish\OneDrive\Desktop\minor\GEOJASON\indian_states_clean_final.geojson"
gdf = gp.read_file(geojson_path)
geojson_states = set(gdf["state_name"].str.upper().unique())

print("CSV States:", len(csv_states))
print("GeoJSON States:", len(geojson_states))

print("\nStates in CSV but not in GeoJSON:")
print(csv_states - geojson_states)

print("\nStates in GeoJSON but not in CSV:")
print(geojson_states - csv_states)
