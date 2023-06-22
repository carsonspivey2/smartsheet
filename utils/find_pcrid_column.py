def find_prcid_column(columns):
    for column in columns:
        if column.get('title') == 'PCR ID':
            return True
    return False
