import consts

def get_body_cells(soldier_row, soldier_col):
    cells = []
    for r in range(consts.SOLDIER_BODY_ROWS):     # 3 שורות
        for c in range(consts.SOLDIER_COLS):       # 2 עמודות
            cells.append((soldier_row + r, soldier_col + c))
    return cells

def get_feet_cells(soldier_row, soldier_col):
    feet_row = soldier_row + consts.SOLDIER_BODY_ROWS   # השורה שאחרי הגוף
    cells = []
    for c in range(consts.SOLDIER_COLS):
        cells.append((feet_row, soldier_col + c))
    return cells

