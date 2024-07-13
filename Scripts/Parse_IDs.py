import xml.etree.ElementTree as ET

def extract_svg_path_ids(file_path):
    try:
        # Parse the SVG file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extracting ids from path elements
        # Adjusting for the namespace
        path_ids = [path.get('id') for path in root.findall('.//{http://www.w3.org/2000/svg}path') if path.get('id')]

        return path_ids
    except ET.ParseError as e:
        return f"Error parsing SVG file: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Use a raw string for the file path or replace single backslashes with double backslashes
    file_path = r'C:\\Users\\nbira\\Desktop\\Kamuin No Text.svg'  # Replace with your SVG file path
    ids = extract_svg_path_ids(file_path)

    if isinstance(ids, list):
        print("const infoText = {")
        for id in ids:
            formatted_name = id.replace('-', ' ').capitalize()
            print(f"    '{id}': '{formatted_name}',")
        print("};")
    else:
        print(ids)  # Print the error message

if __name__ == "__main__":
    main()
