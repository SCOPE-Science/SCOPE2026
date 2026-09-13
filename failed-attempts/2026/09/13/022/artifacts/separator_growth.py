"""Separator-growth recurrence for minimal ehf-layered-wheels (audit artifact).

For fixed separator budget s, this script evaluates the recurrence bounding the
number of vertices that can detach from the giant component in G_l - S, |S|<=s:

  F(j*) = 0                     (highest S-free layer fully in giant component)
  F(j)  = (s+1)*(s + F(j-1) + 1)*B   for layers above j*

B = max box size (zones x specials+gaps), s+1 bounds #segments, s+F+1 bounds
max run of blocked vertices in the layer below. Only <=s layers sit above j*.
Giant component >= n - s - F_total; balancedness fails once n > 3*(s+F_total).
With n_l >= 3^l, this gives an explicit l defeating each s.
"""
B = 200
def max_detached(s):
    F = 0
    for _ in range(s):  # at most s layers above j*
        F = (s+1)*(s + F + 1)*B
    return F

print(f"{'s':>4} {'F(s)':>14} {'n needed':>14} {'l suffices':>10}")
for s in [1,2,3,5,10,28]:
    F = max_detached(s)
    need = 3*(s+F)
    import math
    l = max(0, math.ceil(math.log(need+1,3)))
    print(f"{s:>4} {F:>14} {need:>14} {l:>10}")
print()
print('E.g. s=28 (=9C+1 for C=3): any minimal ehf-layered-wheel with l>=%d onward'
      % max(0, __import__("math").ceil(__import__("math").log(3*(28+max_detached(28))+1,3))))
print('has omega=3 and no balanced separator of size <=28, defeating C=3.')
