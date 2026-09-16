import itertools
from flipsearch import check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

def cycle(n):
    return [frozenset((i,(i+1)%n)) for i in range(n)]

def join_facets(A,na,B,nb):
    return [frozenset(Fa|{v+na for v in Fb}) for Fa in A for Fb in B]

def facet_list_to_ids(facets):
    mp={}; nx=[0]
    def g(v):
        if v not in mp: mp[v]=nx[0]; nx[0]+=1
        return mp[v]
    out=[frozenset(g(v) for v in F) for F in facets]
    return out,nx[0],mp

# Family 1: join of even cycles C6*C6 (d=4, n=12): 3-sphere? join of spheres. Balanced (2+2 colors).
A=cycle(6); B=cycle(6)
J=join_facets(A,0,B,6)
J,n,mp=facet_list_to_ids(J)
colors=[None]*n
for v,i in mp.items(): colors[i]= (v%6)%2 if v<6 else 2+(v%6)%2
print('join C6*C6: nfacets',len(J),'valid',check_valid(J,4,colors))
beta=strand_of_facets(J,n)
print('strand',beta)
print('excess',[b-formula(4,3,i) for i,b in enumerate(beta)])
print()
# Family 2: suspension of balanced 2-sphere with 9 verts? Build minimal balanced 2-sphere: octahedron boundary (6 verts, colors 0,1,2 pairs) then... simpler: use cross-polytope boundary d=3 (octahedron, n=6), suspend with 2 apices (color 3) x? Suspension of S^2 over 2 apices gives S^3 with n=8 (k=2 case): strand should be [0,4,...].
oct_=[frozenset(p) for p in itertools.product([0,1],[2,3],[4,5])]
S=[F|{6} for F in oct_]+[F|{7} for F in oct_]
S,n2,mp2=facet_list_to_ids(S)
col2=[None]*n2
for v,i in mp2.items(): col2[i]= 0 if v in (0,1) else (1 if v in (2,3) else (2 if v in (4,5) else 3))
print('susp(octa): valid',check_valid(S,4,col2),'strand',strand_of_facets(S,n2))
print()
# Family 3: join C4 x octahedron boundary? d = 2+3 = 5, n = 4+6=10 (k=2): still k=2.
# Family 4: join C8 * C8 (d=4, n=16, k=4): compare vs formula k=4.
A8=cycle(8); B8=cycle(8)
J2=join_facets(A8,0,B8,8)
J2,n3,mp3=facet_list_to_ids(J2)
col3=[None]*n3
for v,i in mp3.items(): col3[i]=(v%8)%2 if v<8 else 2+(v%8)%2
print('join C8*C8: nfacets',len(J2),'valid',check_valid(J2,4,col3))
beta2=strand_of_facets(J2,n3)
print('strand',beta2)
print('formula k=4:',[formula(4,4,i) for i in range(n3+1)])
print('excess',[b-formula(4,4,i) for i,b in enumerate(beta2)])
