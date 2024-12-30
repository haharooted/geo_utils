import json
import argparse

def load_geojson(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_geojson(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def deduplicate_geojson(geojson_data):
    # Using a set to track unique features
    seen_features = set()
    unique_features = []

    for feature in geojson_data['features']:
        # Convert the feature to a tuple to make it hashable
        feature_tuple = tuple(sorted(feature.items()))
        
        if feature_tuple not in seen_features:
            seen_features.add(feature_tuple)
            unique_features.append(feature)

    geojson_data['features'] = unique_features
    return geojson_data

def main():
    parser = argparse.ArgumentParser(description="Deduplicate features within a single GeoJSON file.")
    parser.add_argument("input_geojson", help="Path to the input GeoJSON file")
    parser.add_argument("output_geojson", help="Path to save the deduplicated GeoJSON file")
    
    args = parser.parse_args()
    
    # Load the input GeoJSON
    geojson_data = load_geojson(args.input_geojson)
    
    # Deduplicate features
    deduplicated_data = deduplicate_geojson(geojson_data)
    
    # Save the deduplicated GeoJSON
    save_geojson(deduplicated_data, args.output_geojson)
    
    print(f"Deduplicated GeoJSON saved to {args.output_geojson}")

if __name__ == "__main__":
    main()
