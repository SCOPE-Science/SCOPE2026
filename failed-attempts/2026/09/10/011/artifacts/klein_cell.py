"""Fix Klein 21-line / 49-point cell numerically over Q(zeta7) embedded in C.
Construct G_K = PSL(2,7) 3-dim rep from Bauer et al. Sec 2.2, orbit the
fixed line of involution i, cluster pairwise intersections into 49 points,
verify 21 quadruple + 28 triple, replay Prop 3.1 upper-bound counts.
Stdlib + numpy only.
"""
import numpy as np

z = np.exp(2j*np.pi/7)
g = np.diag([z**4, z**2, z**1])
h = np.array([[0,1,0],[0,0,1],[1,0,0]], dtype=complex)
s = (2*z**4+2*z**2+2*z+1)/7
M = np.array([[z-z**6, z**2-z**5, z**4-z**3],
              [z**2-z**5, z**4-z**3, z-z**6],
              [z**4-z**3, z-z**6, z**2-z**5]], dtype=complex)
i = s*M
print("det g,h,i:", np.linalg.det(g), np.linalg.det(h), np.linalg.det(i))
print("i^2 ~ I?", np.max(np.abs(i@i-np.eye(3))))
print("s^2 =", s**2, " (-7 expected)")

# generate projective group: normalize by scalar (det^(1/3)) — just close under mult up to scale
def pkey(A):
    # canonical projective key: scale so max abs entry =1 with phase fixed
    B = A/np.max(np.abs(A))
    # fix phase: first max entry real positive
    idx = np.argmax(np.abs(B))
    B = B/np.exp(1j*np.angle(B.flat[idx]))
    return tuple(np.round(B.flatten(),6))

gens=[g,h,i]
elts={pkey(np.eye(3)):np.eye(3)}
frontier=[np.eye(3)]
while frontier:
    A=frontier.pop()
    for G in gens+( [np.linalg.inv(g) for g in gens] ):
        B=A@G
        k=pkey(B)
        if k not in elts:
            elts[k]=B
            frontier.append(B)
print("group size (projective):", len(elts))
Gs=list(elts.values())

# fixed line of i: -1 eigenspace (2-dim) -> line in P2; normal = +1 eigenvector (point)
w,v=np.linalg.eig(i)
print("eigvals i:", w)
# +1 eigenvector -> quadruple point p; line L: orthogonal to... fixed pointwise line = span of -1 eigenvectors = plane perp to +1 covector.
# In P2 with action v -> A v, fixed line pointwise: set of v with A v = -v (projectively = +v since -1 scalar... careful).
# Projectively i has order 2: points with i v ~ v. +1 eigvec: isolated fixed point. -1 eigvecs: every point in that plane fixed (since i v = -v ~ v).
# So line L = plane spanned by the two -1 eigvecs. Its homogeneous line coords = left +1 eigenvector (row).
# Compute left eigenvectors:
wl,vl=np.linalg.eig(i.T)
for k in range(3):
    print(k, wl[k], vl[:,k])
# find +1:
jplus=[k for k in range(3) if abs(wl[k]-1)<1e-6][0]
line0 = vl[:,jplus]  # line coefficients (l.x=0 fixed plane)
print("line0 coeffs:", line0)

# orbit of line under G: line coeffs transform as l -> l A^{-1} (since (Ax).(l A^{-1})=...)
lines=[]
seen=set()
for A in Gs:
    l = np.linalg.inv(A).T @ line0
    l = l/np.linalg.norm(l)
    # identify up to scale
    # canonical: make first-largest entry real positive
    idx=np.argmax(np.abs(l)); l=l/np.exp(1j*np.angle(l[idx]))
    key=tuple(np.round(l,5))
    # dedupe up to sign/phase already fixed; but l ~ -l same line: enforce by doubling key check
    key2=tuple(np.round(-l,5))
    if key not in seen and key2 not in seen:
        seen.add(key); lines.append(l)
print("num lines:", len(lines))
assert len(lines)==21, "expected 21 lines"

# pairwise intersections
pts=[]
for a in range(21):
    for b in range(a+1,21):
        p=np.cross(lines[a],lines[b])
        if np.linalg.norm(p)<1e-10: continue
        p=p/np.linalg.norm(p)
        pts.append(p)
print("pairs:", len(pts))  # 210
# cluster projectively (p ~ phase*p and p ~ -p etc: distance = 1-|<p,q>|)
clusters=[]
for p in pts:
    found=False
    for c in clusters:
        if abs(abs(np.vdot(c[0],p))-1)<1e-4:
            c.append(p); found=True; break
    if not found:
        clusters.append([p])
print("num clusters (singular points):", len(clusters))
sizes=sorted([len(c) for c in clusters])
# multiplicity m of point = number of lines through it; pairs = C(m,2)
from collections import Counter
print(Counter(sizes))
# map pair-count -> m: 6 pairs = quadruple (C4,2=6), 3 pairs = triple
n4=sum(1 for c in clusters if len(c)==6)
n3=sum(1 for c in clusters if len(c)==3)
print("quadruple:",n4,"triple:",n3,"total:",n4+n3)
# check each line contains how many of each
def nearest(p):
    best=None;bd=9
    for j,c in enumerate(clusters):
        d=1-abs(np.vdot(c[0],p))
        if d<bd: bd=d;best=j
    return best,bd
for a in range(3):
    cnt4=cnt3=0
    for b in range(21):
        if b==a: continue
        p=np.cross(lines[a],lines[b]); p=p/np.linalg.norm(p)
        j,d=nearest(p)
        assert d<1e-4
        m=6 if len(clusters[j])==6 else 3
        # count distinct points on line a
    # distinct:
    seenpts=set()
    for b in range(21):
        if b==a: continue
        p=np.cross(lines[a],lines[b]); p=p/np.linalg.norm(p)
        j,d=nearest(p); seenpts.add(j)
    c4=sum(1 for j in seenpts if len(clusters[j])==6)
    c3=sum(1 for j in seenpts if len(clusters[j])==3)
    print(f"line {a}: {c4} quad + {c3} triple = {c4+c3} pts")

# Prop 3.1 dimension check
import math
def C2(n): return n*(n-1)//2 if n>=2 else 0
for k in [1,2,7,16]:
    d=28*k+2
    v=C2(d+2)-21*C2(2*k+1)-28*C2(5*k+1)
    print(f"k={k} d={d} virt dim={v} (paper: {7*k+6})")
    assert v==7*k+6
# upper bound ratio
print("upper bound (91k+2)/(14k) ->", 91/14)
# Lemma 3.3 floor check
for k in [16/7,7]:
    print(k, (91*k+24)/(14*k+4))
# D intersections
def dotD(d,m4,m3): return 28*d-42*m4-140*m3
for name,dd,a,b in [("A",21,4,3),("C1",18,4,0),("C2",42,0,8),("C3",144,4,27)]:
    B2=dd*dd-21*a*a-28*b*b
    print(name, "D.B=",dotD(dd,a,b), "B2=",B2)
print("KLEIN_CELL_OK")
