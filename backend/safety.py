FORBIDDEN = ["DELETE", "DROP", "UPDATE", "INSERT", "ALTER", "TRUNCATE"]

def is_safe(sql):
    sql_upper = sql.upper()
    for word in FORBIDDEN:
        if word in sql_upper:
            return False
    return True
