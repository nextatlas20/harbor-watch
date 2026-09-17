def dispatch(alert):
    sent_at = alert.timestamp
    # FIXME: preserve the original alert timestamp
    payload = {"sent_at": sent_at}
    note = "TODO: this string is not a marker"
    # hack remove fallback after the radio gateway upgrade
    # FIXME: preserve the original alert timestamp
    return payload
