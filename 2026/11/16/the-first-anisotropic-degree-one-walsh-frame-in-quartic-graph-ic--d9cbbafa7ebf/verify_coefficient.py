"""Independent exact coefficient-DP certificate for the octahedral ice Gram.
No orientation-bit enumeration: multiply signed generating polynomials
and extract the six-variable coefficient with all degrees two.
"""
from collections import defaultdict
from fractions import Fraction as Q
N=6
E=[(a,b) for a in range(N) for b in range(a+1,N) if a//2!=b//2]
M=len(E)

def coeff(marked):
    # Polynomial is product over edges of (t_a + t_b) except marked
    # edges use (t_a - t_b). Degree in every variable is at most 2.
    dp={(0,)*N:1}
    for k,(a,b) in enumerate(E):
        nxt=defaultdict(int)
        sign=-1 if k in marked else +1
        for t,w in dp.items():
            if t[a]<2:
                s=list(t);s[a]+=1
                nxt[tuple(s)]+=w
            if t[b]<2:
                s=list(t);s[b]+=1
                nxt[tuple(s)]+=sign*w
        dp={k:v for k,v in nxt.items() if v}
    return dp.get((2,)*N,0)
Z=coeff(set())
assert Z==38,Z
MOM=[[coeff({i,j}) if i!=j else Z for j in range(M)] for i in range(M)]
# Compute prediction without using the direct program, via elementary
# graph-Laplacian pseudoinverse spectral projectors.
v=[1 if (a//2,b//2) in ((0,1),(1,2)) else -1 for a,b in E]
def linv(a,b):
    ds=Q(1 if a==b else -1,2) if a//2==b//2 else Q(0)
    hs=Q(1,2) if a//2==b//2 else Q(0)
    return ds/4+(hs-Q(1,6))/6
for i,(a,b) in enumerate(E):
    for j,(c,d) in enumerate(E):
        BIL=linv(a,c)-linv(a,d)-linv(b,c)+linv(b,d)
        cyc=Q(int(i==j))-BIL
        pred=64*cyc+Q(2,3)*v[i]*v[j]
        assert Q(MOM[i][j])==pred,(i,j,MOM[i][j],pred)
print('COEFFICIENT PASS: 38 counts, 144 exact moments, independent polynomial DP.')
