assignments = []

    
#name of rows & columns
rows = 'ABCDEFGHI'
cols = '123456789'

#function wich will be used to get names of the boxes
def cross(A, B):
    return [a+b for a in A for b in B]

# Names of boxes
boxes = cross(rows, cols)
# create units 
rows_units = [cross(a, cols) for a in rows]
cols_units = [cross(rows, a) for a in cols]
squar_units = [cross(r, c) for r in ('ABC', 'DEF','GHI') for c in ('123', '456', '789')]

diagonal_units = []
diagonal_units.append(['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'])
diagonal_units.append(['I1', 'H2', 'G3', 'F4', 'E5', 'D6', 'C7', 'B8', 'A9'])
# all units
unitlist = rows_units+cols_units+squar_units+diagonal_units

#units and peers for each box
units = dict((b, [a for a in unitlist if b in a]) for b in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
    

#function to assign new values to dictionary 
def assign_value(values, box, value):
    
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy()) #save previous values
    return values

#Eliminating naked twins
def naked_twins(values):
    #Iterate over units and find all two-digit values then identify duplivates
    for unit in unitlist:
        two_digit = ([values[box] for box in unit if len(values[box]) ==2])
        dupes = ([x for n, x in enumerate(two_digit) if x in two_digit[:n]])
        #if more then 1 dupe in unit so iterate throught list of dupes
        for digit in dupes:
            for box in unit:
                #delete dupe values from other elements in unit (not from naked twins)
                if values[box] != digit:
                    for d in digit:
                        new_value = values[box].replace(d, '')
                        assign_value(values, box, new_value)
    return values



#Convert grid into a dict of {square: char} with '123456789' for empties.
def grid_values(grid):
    #check that in grid all 81 elements
    assert len(grid) == 81
    val = dict(zip(boxes, grid))
    
    for key, value in val.items():
        if value == '.':
            val[key] = '123456789'
    return val

#Display the values as a 2-D grid.
def display(values):
    
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# If a box has a value assigned delete this value from peers of the box 
def eliminate(values):
    # find assigned values 
    rep_items = [box for box in values.keys() if len(values[box]) == 1]
    #delete from peers
    for box in rep_items:
        digit = values[box]
        #assign new value for peer in values
        for peer in peers[box]:
            new_value = values[peer].replace(digit,'')
            assign_value(values, peer, new_value)
            
    return values

#Assign value to box if only value is possible only for one box
def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                assign_value(values, dplaces[0], digit)
    return values

#use constraint propagation, to do it combine eliminate, naked_twins and one_choice
def reduce_puzzle(values):
    stalled = False
    while not stalled:
        
        solved_values_before = len([box for box in values.keys() if len(values[box])== 1])
        #apply all techniques to values to solve sudoku
        values = eliminate(values)
        values = naked_twins(values)
        values = only_choice(values)
        
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        
        stalled = solved_values_before == solved_values_after
        
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values 

#Implementation of depth first search
def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values
    #find box with min lenght of value
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)    
    #try to solve sudoku using every value while not get right solution
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    
    #solve sudoku
    values = grid_values(grid)
    values = search(values)
    return values
    
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
