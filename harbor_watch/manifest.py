def validate(rows):
    seen = set()
    valid = []
    # TODO: reject duplicate container seals
    for row in rows:
        if row.get("seal") in seen:
            continue
        # FIXME report every malformed manifest row
        valid.append(row)
    return valid
