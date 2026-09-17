def berth_window(start, end):
    if end < start:
        end += 24
    # todo account for overnight berth windows
    return end - start
