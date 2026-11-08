"""Exact arithmetic checks for the specified polygonal-map survivor theorem.
All coordinates and segment inclusions use rational arithmetic; the
universal proof is in RESULT.md and is not replaced by these samples.
"""
from fractions import Fraction as Q
import sympy as sp

STATE = ('A', 'B', 'C', 'D', 'E', 'G', 'I', 'H')
ARROWS = {'A':('C',), 'B':('D',), 'C':('E',), 'D':('G',),
          'E':('G','I','H'), 'G':('A',), 'I':('B',), 'H':('C',)}
EXP = {'A':sp.sqrt(2),'B':sp.sqrt(2),'C':sp.sqrt(2),
       'D':sp.Integer(2),'E':sp.sqrt(2),'G':sp.sqrt(2),
       'I':sp.sqrt(2),'H':sp.Integer(2)}
M = sp.zeros(8)
for i,u in enumerate(STATE):
    for v in ARROWS[u]:
        M[i,STATE.index(v)]=1/EXP[u]
t = sp.symbols('t')
assert sp.factor(M.charpoly(t).as_expr()) == t*(16*t**7 - 4*t**4 - 4*t**3 - 1)/16

def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def between(x,p,q):
    if cross(sub(x,p), sub(q,p))!=0: return False
    return (min(p[0],q[0])<=x[0]<=max(p[0],q[0])
            and min(p[1],q[1])<=x[1]<=max(p[1],q[1]))
def F(p,b):
    x,y=p;return (abs(x)-y-1, x-abs(y)+b)

def points(b):
    return {
      'P1':(-b-2,-1),'P2':(b+2,-3),'P3':(b+4,2*b-1),'P4':(4-b,5),
      'S':(0,b+1),'X1':(0,-1),'X2':(0,b-1),'X3':(-b,1),
      'X4':(b-2,-1),'R':(b-2,2*b-3),
      'Y1':(b-1,0),'Y2':(b-2,2*b-1),
      'Z1':(-b-1,0),'Z2':(b,-1),'Z3':(b,2*b-1)
    }
CORE = {'A':('Z3','P3'),'B':('Y2','Z3'),'C':('X3','S'),
        'D':('Z1','P1'),'E':('P1','X1'),'G':('Z2','P2'),
        'I':('Y1','Z2'),'H':('Y1','X2')}
TRANS = {'T':('X3','Z1'),'U':('X1','Z2'),'V':('X2','Z3')}
# Every mapped core segment is exactly the contiguous concatenation
# of the indicated core and transient subsegments (or their subsegments).
PARTS = {
 'A':('C','AP4'),'B':('T','D'),'C':('E','CX4'),
 'D':('G',),'E':('G','I','H'),'G':('A',),'I':('B',),'H':('C','HY2')}

def segment_test(b):
    p=points(b)
    transient=dict(TRANS)
    transient['W']=('S','P4') if b<=3 else ('S','Y2')
    special={'AP4':('S','P4'), 'CX4':('X1','X4'), 'HY2':('S','Y2')}
    segments={**CORE,**transient,**special}
    for name,(u,v) in CORE.items():
        src=(p[u],p[v]); dst=(F(src[0],b),F(src[1],b))
        all_pts=[]
        for piece in PARTS[name]:
            a,c=segments[piece]
            assert between(p[a],*dst) and between(p[c],*dst),(b,name,piece,dst)
            all_pts += [p[a],p[c]]
        assert dst[0] in all_pts and dst[1] in all_pts,(b,name,dst)
        # Union length equals image length (collinear and no positive overlap).
        len_sq=lambda a,c:(a[0]-c[0])**2+(a[1]-c[1])**2
        dim=0 if dst[0][0]!=dst[1][0] else 1
        ivals=[]
        for piece in PARTS[name]:
            a,c=segments[piece]
            ivals.append((min(p[a][dim],p[c][dim]),max(p[a][dim],p[c][dim])))
        ivals.sort(); lo=min(dst[0][dim],dst[1][dim]);hi=max(dst[0][dim],dst[1][dim])
        assert ivals[0][0]==lo and ivals[-1][1]==hi,(b,name,ivals,dst)
        for u,v in zip(ivals,ivals[1:]):assert u[1]==v[0],(b,name,ivals)
        # all are single-affine-branch source segments; check midpoint
        assert F(((src[0][0]+src[1][0])/2,(src[0][1]+src[1][1])/2),b)==tuple((dst[0][i]+dst[1][i])/2 for i in (0,1)),(b,name)
    for s,t in [('P1','P2'),('P2','P3'),('P3','P4'),('P4','P1'),
                ('S','P1'),('X1','X2'),('X2','X3'),('X3','X4'),('X4','R'),('R','X3'),
                ('Y1','Y2'),('Y2','P1'),('Z1','Z2'),('Z2','Z3'),('Z3','X3')]:
        assert F(p[s],b)==p[t],(b,s,t)
    return True

for b in [Q(2),Q(9,4),Q(5,2),Q(11,4),Q(3),Q(13,4),Q(7,2),Q(15,4),Q(4)]:
    assert segment_test(b)
# The graph-directed similarity pressure equation at dimension d is
# 1 - 2*4**(-d) - 16**(-d) = 0. Let t=4**(-d).
u=sp.sqrt(2)-1
assert sp.simplify(1-2*u-u**2)==0
print('POLYGONAL_CORE_EXACT_BRANCH_AND_CHARPOLY_OK parameter_samples=9 states=8')
print('dimension=',sp.N(sp.log(1+sp.sqrt(2))/sp.log(4),15))
print('survival_root=',sp.nroots(16*t**7-4*t**4-4*t**3-1,maxsteps=200))
