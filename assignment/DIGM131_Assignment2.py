# Cube Stats
rows = 7
cols = 4
spacing = 2

# Cube Organizer
base_width = 1.0
tower_height = base_width 
roof_offset = tower_height

def create_grid_pattern(rows, cols, spacing):
    """Creates a grid of cubes."""
    # Loop for creating rows
    for i in range(rows):
        # Loop for creating cols
        for j in range(cols):
            
            # The Cubes get different shapes depending on its position on the grid
            cube = cmds.polyCube(w=base_width, h=tower_height + i - j, d=base_width, name=f"Cuh_{i}_{j}")[0]
            
            # Postioner for the Cubes
            cmds.xform(cube, translation=(i * spacing, 0, j * spacing))

# Function Runner
create_grid_pattern(rows=10, cols=10, spacing=1.5)