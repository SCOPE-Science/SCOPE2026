"""Exact-rational finite checks for a ternary pairwise-independent extremum."""
from fractions import Fraction as F
from itertools import product

N = 0

def check(statement, label):
    global N
    N += 1
    if not statement:
        raise AssertionError(label)

def latin_A(i, j):
    return (-i - j - 1) % 3

def latin_B(i, j):
    return (i - j - 1) % 3

def inspect(t):
    v = (F(0), F(1), t)
    d = t*t*(3-t)/6 if t <= 2 else t/3
    H = {(0,0):d,(0,1):-d/2,(0,2):-d/2,(1,1):d,(1,2):d,(2,2):t**3/3}
    def h(a,b): return H[tuple(sorted((a,b)))]
    total = (sum(H[i,j] for i in range(3) for j in range(i,3)) * 2
             - H[0,0] - H[1,1] - H[2,2]) / 3
    a = t*t/3; b = (t**3+2*t)/9
    check(total == (a if t <= 2 else b), (t, 'dual objective'))
    tight = set()
    for i,j,k in product(range(3), repeat=3):
        slack = h(i,j) + h(i,k) + h(j,k) - v[i]*v[j]*v[k]
        check(slack >= 0, (t,i,j,k,slack))
        if slack == 0: tight.add((i,j,k))
    for name,op,expected in [('A',latin_A,a),('B',latin_B,b)]:
        atoms = [(i,j,op(i,j)) for i,j in product(range(3),repeat=2)]
        for x,y in [(0,1),(0,2),(1,2)]:
            for u,w in product(range(3),repeat=2):
                check(sum(1 for q in atoms if q[x]==u and q[y]==w)==1,
                      (t,name,'two-way',x,y,u,w))
        val = sum(v[i]*v[j]*v[k] for i,j,k in atoms)/9
        check(val == expected,(t,name,'cost',val,expected))
        if (name=='A' and t<=2) or (name=='B' and t>=2):
            for atom in atoms:
                check(atom in tight,(t,name,'complementary slackness',atom))
    if t < 2:
        check(tight == {x for x in product(range(3),repeat=3)
                       if sorted(x) in ([0,0,1],[0,0,2],[0,1,1],[0,1,2],[1,2,2],[2,2,2])},
              (t,'A allowed patterns'))
    if t > 2:
        check(all(not (sum(x==2 for x in (i,j,k))==2) for i,j,k in tight),
              (t,'B no exactly-two-upper patterns'))

samples = [F(101,100),F(11,10),F(4,3),F(3,2),F(7,4),F(199,100),F(2),F(201,100),F(5,2),F(3),F(5),F(10)]
for t in samples: inspect(t)
print(f'PASS: {N} exact-rational conditions for {len(samples)} thresholds')
