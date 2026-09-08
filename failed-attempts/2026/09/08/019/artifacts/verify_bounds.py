"""Verify the integer-arithmetic growth certificates (no enumeration needed)."""
a12 = 16115110
# Fekete lower bound: 3.986^12 < a12  <=>  3986^12 < a12 * 10^36
assert 3986**12 < a12 * (10**36), "lower-bound certificate failed"
assert not (3987**12 < a12 * (10**36)), "sharpness check unexpected"
# consistency: root < 4 since a12 < 4^12
assert a12 < 4**12
# Wilf-separation table entries
C = [1,1,2,6,23,102,496,2569,13934]
A = [1,1,2,6,22,87,352,1428,5768]
assert C[4] == 23 and A[4] == 22
print("bound certificates OK: 3.986^12 <", a12, "< 4^12")
