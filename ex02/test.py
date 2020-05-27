from vector import Vector

vector = Vector([0.0, 1.0, 2.0, 3.0])
vector2 = Vector(4)
vector3 = Vector((5, 9))

print(vector)
print(vector2)
print(vector3)

vector = vector + vector2
print(vector)
vector = vector2 * vector3
print(vector)
vector = vector3 / 2
print(vector)
