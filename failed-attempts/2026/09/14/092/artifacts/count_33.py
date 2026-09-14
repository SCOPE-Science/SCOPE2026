"""Verify the 33-obstruction count decomposition in Conjecture 1.3 (BOSW).

Decomposition per topic statement:
  Group A: F7, F7-, F7=, H7, M(K4)+e, W^3+e, Lambda_3, Q6+e, P6+e, U3,7
           "and their duals"
  Group B: the six matroids in Delta*(U2,7)
  Group C: AG(2,3)\\e, its dual, its Delta-Y variant (3 matroids)
  Group D: P8, P8-, P8=, TQ8 (4 matroids)
Total claimed: 33.
"""
groupA_named = ["F7", "F7-", "F7=", "H7", "M(K4)+e", "W^3+e",
                "Lambda_3", "Q6+e", "P6+e", "U3,7"]
# Each of the 10 has a distinct dual counted separately (none listed is self-dual
# per the conjecture statement's phrasing "and their duals").
groupA = len(groupA_named) * 2
groupB = 6
groupC = 3
groupD = 4
total = groupA + groupB + groupC + groupD
print(f"Group A: 10 named x2 (duals) = {groupA}")
print(f"Group B: Delta*(U2,7) = {groupB}")
print(f"Group C: AG(2,3)\\e family = {groupC}")
print(f"Group D: P8 family + TQ8 = {groupD}")
print(f"Total = {total}")
assert total == 33, total
print("OK: decomposition sums to 33")
