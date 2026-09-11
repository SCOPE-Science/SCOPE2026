import itertools
H=0.375
# pairing list (0-indexed) from earlier enumeration
pairs=[
[(0,1),(2,3),(4,5)],
[(0,1),(2,4),(3,5)],
[(0,1),(2,5),(3,4)],
[(0,2),(1,3),(4,5)],
[(0,2),(1,4),(3,5)],
[(0,2),(1,5),(3,4)],
[(0,3),(1,2),(4,5)],
[(0,3),(1,4),(2,5)],
[(0,3),(1,5),(2,4)],
[(0,4),(1,2),(3,5)],
[(0,4),(1,3),(2,5)],
[(0,4),(1,5),(2,3)],
[(0,5),(1,2),(3,4)],
[(0,5),(1,3),(2,4)],
[(0,5),(1,4),(2,3)],
]
# MC means from run (idx order above)
mc=[0.038115,0.006357,-0.014825,0.007278,-0.000628,0.001767,-0.014555,-0.000188,-0.000260,0.001840,-0.000321,0.000936,-0.005232,-0.000686,0.002359]
def compat(w,P):
    for (i,j) in P:
        if w[i]!=w[j]: return False
    return True
e6sq=0.0
for w in itertools.product([0,1],repeat=6):
    s=sum(v for v,P in zip(mc,pairs) if compat(w,P))
    e6sq+=s*s
    if abs(s)>0.005:
        print(w, round(s,6), sum(1 for P in pairs if compat(w,P)))
import math
e6=math.sqrt(e6sq)
print("e6_est",e6)
print("f3=e6*6^.75",e6*(6**0.75))
# level4
A=0.158852453398871; B=-0.0625; C=0.028647546601129
e4sq=0
for w in itertools.product([0,1],repeat=4):
    P4=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
    V=[A,C,B]
    s=sum(v for v,P in zip(V,P4) if all(w[i]==w[j] for (i,j) in P))
    e6sq2=s*s
    e4sq+=e6sq2
e4=math.sqrt(e4sq)
print("e4",e4,"f2",e4*(2**0.75),"f1",math.sqrt(2)/2)
