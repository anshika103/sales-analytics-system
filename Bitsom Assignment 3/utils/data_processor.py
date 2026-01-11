def clean_data(raw_records):
    """
    Cleans messy sales data according to project criteria.
    """
    valid_records = []
    total_parsed = len(raw_records)
    
    for record in raw_records:
        try:
            # 1. Validation: Missing CustomerID or Region or incorrect field count
            # record[6] is CustomerID, record[7] is Region
            if len(record) != 8 or not record[6] or not record[7]:
                continue

            # 2. Validation: TransactionID must start with 'T'
            if not record[0].startswith('T'):
                continue

            # 3. Clean numeric formatting (Remove commas from strings like '1,500')
            qty = int(record[4].replace(',', ''))
            price = float(record[5].replace(',', ''))

            # 4. Validation: Quantity and UnitPrice must be > 0
            if qty <= 0 or price <= 0:
                continue

            # 5. Clean Product Name: Remove commas (e.g., "Mouse,Wireless" -> "Mouse Wireless")
            product_name = record[3].replace(',', ' ')

            # If all checks pass, store the cleaned record
            valid_records.append({
                "TransactionID": record[0],
                "Date": record[1],
                "ProductID": record[2],
                "ProductName": product_name,
                "Quantity": qty,
                "UnitPrice": price,
                "CustomerID": record[6],
                "Region": record[7]
            })
            
        except (ValueError, IndexError):
            continue
            
    # Calculate counts for the required terminal output
    valid_count = len(valid_records)
    invalid_count = total_parsed - valid_count

    # MANDATORY OUTPUT: Your manager specifically asked for these print statements
    print(f"\nTotal records parsed: {total_parsed}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {valid_count}\n")
            
    return valid_records, invalid_count

def clean_data(raw_records):
    """
    Cleans messy sales data according to specific manager criteria.
    """
    valid_records = []
    total_parsed = len(raw_records)
    
    for record in raw_records:
        try:
            # 1. REMOVE: Check for correct field count (8 fields)
            if len(record) != 8:
                continue
                
            # 2. REMOVE: Missing CustomerID or Region
            if not record[6].strip() or not record[7].strip():
                continue

            # 3. REMOVE: TransactionID not starting with 'T'
            if not record[0].startswith('T'):
                continue

            # 4. CLEAN & KEEP: Remove commas from numeric strings
            # record[4] is Quantity, record[5] is UnitPrice
            qty_str = record[4].replace(',', '')
            price_str = record[5].replace(',', '')
            
            qty = int(qty_str)
            price = float(price_str)

            # 5. REMOVE: Quantity <= 0 or UnitPrice <= 0
            if qty <= 0 or price <= 0:
                continue

            # 6. CLEAN & KEEP: Remove commas from ProductName
            # record[3] is ProductName
            product_name = record[3].replace(',', ' ')

            # store the cleaned record
            valid_records.append({
                "TransactionID": record[0],
                "Date": record[1],
                "ProductID": record[2],
                "ProductName": product_name,
                "Quantity": qty,
                "UnitPrice": price,
                "CustomerID": record[6],
                "Region": record[7]
            })
            
        except (ValueError, IndexError):
            # Skip rows with malformed data that cause errors during conversion
            continue
            
    valid_count = len(valid_records)
    invalid_count = total_parsed - valid_count

    # REQUIRED PRINTOUT: This must appear exactly as requested
    print(f"Total records parsed: {total_parsed}")
    print(f"Invalid records removed: {invalid_count}")
    print(f"Valid records after cleaning: {valid_count}")
            
    return valid_records, invalid_count