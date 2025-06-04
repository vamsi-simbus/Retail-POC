def rename_column(col_name):
    return col_name.strip().replace(" ", "_") \
                          .replace("%", "") \
                          .replace("(", "") \
                          .replace(")", "") \
                          .replace("$", "") \
                          .replace("-", "_")
