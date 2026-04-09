ground_size = 20
cmds.polyCube(w=ground_size, h=0.1, d=ground_size, name="ground")

building_height = 4
building_width = 1.5
cmds.polyCube(w=building_width, h=building_height,
 d=building_width, name="building_01")
cmds.move(3, building_height / 2.0, 2, "building_01")

building_height = 3
building_width = 3
cmds.polySphere(r=0.5,name="building_02")
cmds.move(0, building_height / 2.0, 3, "building_02")

building_height = 4
building_width = 2.5
cmds.polyCube(w=building_width, h=building_height,
 d=building_width, name="building_03")
cmds.move(6, building_height / 2.0, 6, "building_03")

building_height = 4
building_width = 2.5
cmds.polySphere(r=2,name="building_04")
cmds.move(2, building_height / 2.0, 5, "building_04")

building_height = 2
building_width = 4
cmds.polyCube(w=building_width, h=building_height,
 d=building_width, name="building_05")
cmds.move-(3, building_height / -2.0, 2, "building_05")