import os
import sys

# Add the current directory to sys.path to resolve 'utils' import issues
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.file_handler import load_raw_data
from utils.data_processor import clean_data
from utils.api_handler import get_product_info

def generate_report():
    # 1. Setup paths relative to this file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, 'data', 'sales_data.txt')
    output_folder = os.path.join(base_dir, 'output')
    output_path = os.path.join(output_folder, 'sales_summary.txt')

    print("--- Starting Sales Analytics System ---")

    # 2. Load the messy sales data
    raw_data = load_raw_data(input_file)
    if not raw_data:
        print(f"Error: Could not find or read data at {input_file}")
        return

    # 3. Process and Clean the data
    # This handles commas in numbers and invalid records
    valid_records, invalid_count = clean_data(raw_data)
    
    # 4. Perform Basic Analysis
    total_revenue = 0
    unique_products = set()
    
    for record in valid_records:
        total_revenue += (record['Quantity'] * record['UnitPrice'])
        unique_products.add(record['ProductID'])

    # 5. Build Report Content
    report_content = [
        "SALES DATA ANALYTICS REPORT",
        "="*30,
        f"Total Records in File: {len(raw_data)}",
        f"Valid Records Processed: {len(valid_records)}",
        f"Invalid Records Skipped: {invalid_count}",
        f"Total Revenue Calculated: {total_revenue:,.2f}",
        f"Unique Products Sold: {len(unique_products)}",
        "="*30,
        "\nData processing complete."
    ]

    # 6. Save the report to the output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    with open(output_path, 'w') as f:
        f.write("\n".join(report_content))

    print(f"Report successfully generated at: {output_path}")

if __name__ == "__main__":
    generate_report()