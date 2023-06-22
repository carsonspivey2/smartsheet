def find_pcrid_column(columns):
    for column in columns:
        if column.title == 'PCR ID':
            return True
    return False
