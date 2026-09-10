# FALLBACK element (i), part 1 of 2: classical null-homotopy 2.eta = 0 in pi_*(S),
# recomputed from scratch via the classical Adams cobar over A_* (dual Steenrod).
# h0 = [xi1] (stem 0, filt 1) detects 2; h1 = [xi1^2] (stem 1, filt 1) detects eta.
# Claim: h0*h1 = 0 in Ext^{2,2} (stem 1) via cobar boundary d[x1|1] with x1=[xi1^2|xi1]+... -- verify by kernel rank.
# Work in A_* truncated: generators xi1(d1), xi2(d3), xi3(d7) + polynomial; coproduct standard Milnor.
from collections import defaultdict
# monomials xi1^a xi2^b xi3^c truncated a<8 (enough for degrees<=2)
mons=[(a,b,c) for a in range(8) for b in range(2) for c in range(2)]
def deg(m): return m[0]+3*m[1]+7*m[2]
def add(m1,m2): return (m1[0]+m2[0],m1[1]+m2[1],m1[2]+m2[2])
# psi(xi1)=x1@1+1@x1; psi(xi2)=x2@1+x1^2@x1+1@x2 (truncated, xi1^3 terms drop? keep exact to deg<=2)
def psi(m):
    a,b,c=m
    # psi(xi1)^a psi(xi2)^b psi(xi3)^c
    R={( (0,0,0),(0,0,0) ):1}
    def mul(P,Q):
        R2=defaultdict(int)
        for (a1,b1),v1 in P.items():
            for (a2,b2),v2 in Q.items():
                R2[(add(a1,a2),add(b1,b2))]^=v1&v2
        return {k:v for k,v in R2.items() if v}
    Px1={( ((1,0,0),(0,0,0)) ):1, ((0,0,0),(1,0,0)):1}
    Px2={( ((0,1,0),(0,0,0)) ):1, (((2,0,0),(1,0,0))):1, (((0,0,0),(0,1,0))):1}
    for _ in range(a): R=mul(R,Px1)
    for _ in range(b): R=mul(R,Px2)
    return R
# C^1 in degree 2: basis [m], deg(m)=2: xi1^2 only
B1=[m for m in mons if m!=(0,0,0) and deg(m)==2]
# C^2 in degree 2: pairs deg sum 2: [xi1|xi1] only
B2=[(m1,m2) for m1 in mons for m2 in mons if m1!=(0,0,0) and m2!=(0,0,0) and deg(m1)+deg(m2)==2]
print("C^1_2 basis:",B1," C^2_2 basis:",B2)
# d[m] = reduced coproduct terms
for m in B1:
    P=psi(m)
    red=[(x,y) for (x,y) in P if x!=(0,0,0) and y!=(0,0,0)]
    print(f"d[{m}] =",red)
# So d[xi1^2] = [xi1|xi1] (since psi(xi1^2)=(x1@1+1@x1)^2 = x1^2@1 + 1@x1^2 as cross terms cancel? check)
# If d[xi1^2]=0 then h0h1... use h0=[xi1], h1=[xi1^2]: product [xi1|xi1^2] in C^2_3? verify it's a boundary: d[xi1^3]=[xi1^2|xi1]+[xi1|xi1^2].
B1d3=[m for m in mons if m!=(0,0,0) and deg(m)==3]
print("C^1_3:",B1d3)
for m in B1d3:
    P=psi(m)
    red=[(x,y) for (x,y) in P if x!=(0,0,0) and y!=(0,0,0)]
    print(f"d[{m}] =",red)
print("CONCLUSION: h0*h1=[xi1|xi1^2]=d[xi1^3]+[xi1^2|xi1]; check whether [xi1^2|xi1] is itself a cycle/boundary -> h0h1=0 in Ext (classical relation).")
# verify [xi1^2|xi1] is a cycle: d2 = [d(xi1^2)|xi1]+[xi1^2|d(xi1)] = 0 since d(xi1)=d(xi1^2)=0 (primitive powers)
for m in [(2,0,0),(1,0,0)]:
    P=psi(m); red=[(x,y) for (x,y) in P if x!=(0,0,0) and y!=(0,0,0)]
    print(f"  prim check d[{m}] =",red)
