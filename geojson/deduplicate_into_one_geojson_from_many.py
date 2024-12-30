import json
import argparse
import os
from glob import glob
import logging

def load_geojson(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_geojson(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def deduplicate_geojsons_across_files(folder_path):
    # Using a set to track unique features across multiple files
    seen_features = set()
    unique_features = []
    
    geojson_files = glob(os.path.join(folder_path, "*.geojson"))
    logging.info(f"Found {len(geojson_files)} GeoJSON files in folder '{folder_path}'.")

    total_features = 0
    for idx, geojson_file in enumerate(geojson_files, 1):
        logging.info(f"Processing file {idx}/{len(geojson_files)}: {geojson_file}")
        try:
            geojson_data = load_geojson(geojson_file)
            features = geojson_data.get('features', [])
            logging.info(f"Found {len(features)} features in '{geojson_file}'.")
            total_features += len(features)
            for feature in features:
                # Convert the feature to a JSON string to make it hashable
                feature_str = json.dumps(feature, sort_keys=True)
                
                if feature_str not in seen_features:
                    seen_features.add(feature_str)
                    unique_features.append(feature)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON in '{geojson_file}': {e}")
        except Exception as e:
            logging.error(f"An error occurred while processing '{geojson_file}': {e}")

    logging.info(f"Total features processed: {total_features}")
    logging.info(f"Total unique features: {len(unique_features)}")

    return {
        "type": "FeatureCollection",
        "features": unique_features
    }

def main():
    parser = argparse.ArgumentParser(description="Deduplicate features across multiple GeoJSON files in a folder.")
    parser.add_argument("input_folder", help="Path to the folder containing GeoJSON files")
    parser.add_argument("output_geojson", help="Path to save the final deduplicated GeoJSON file")

    args = parser.parse_args()

    # Check if the input folder exists
    if not os.path.isdir(args.input_folder):
        logging.error(f"Input folder does not exist: {args.input_folder}")
        return

    # Deduplicate features across all GeoJSON files in the input folder
    deduplicated_data = deduplicate_geojsons_across_files(args.input_folder)

    # Save the deduplicated GeoJSON
    try:
        save_geojson(deduplicated_data, args.output_geojson)
        logging.info(f"Deduplicated GeoJSON saved to '{args.output_geojson}'.")
    except Exception as e:
        logging.error(f"Failed to save deduplicated GeoJSON: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
