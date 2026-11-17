"""Independent Boolean neighborhood and word-boundary certificate.
Run: python3 checks/symbolic.py
"""

def local(l,c,r):
    return (57 >> (4*l + 2*c + r))&1

for l in range(2):
    for c in range(2):
        for r in range(2):
            assert (local(l,c,r)==c)==(l==0 and r==1)
print('Rule-57 hold/toggle condition: PASS')

# After one all-changing sweep, interior two-cycle consistency is
# x_{i+2}=1-x_i. Its boundaries must satisfy x_{n-1}=x_1,
# x_{n-2}=x_0. Check these purely algebraic constraints for 3..256.
for n in range(3,257):
    solutions=[]
    for a in (0,1):
        for b in (0,1):
            x=[(a,b,1-a,1-b)[i%4] for i in range(n)]
            if x[-1]==x[1] and x[-2]==x[0]:solutions.append((a,b))
    assert len(solutions)==(4 if n%4==2 else 0), (n,solutions)
print('Two-cycle boundary congruences n=3..256: PASS')
print('ALL SYMBOLIC CHECKS PASSED')
