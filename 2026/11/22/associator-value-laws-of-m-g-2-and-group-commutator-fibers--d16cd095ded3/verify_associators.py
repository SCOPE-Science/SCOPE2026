from itertools import product, permutations
from collections import Counter

def groups():
    # Symmetric groups S_3 and S_4, dihedral D_8 and D_10
    for n in (3,4):
        E=list(permutations(range(n))); idx={p:i for i,p in enumerate(E)}; one=idx[tuple(range(n))]
        mul=[[idx[tuple(x[y[i]] for i in range(n))] for y in E] for x in E]
        yield 'S_'+str(n),mul,one
    for n in (4,5):
        E=list(product(range(n),range(2))); idx={p:i for i,p in enumerate(E)}; one=idx[(0,0)]
        mul=[[idx[((a+(-1)**b*c)%n,(b+d)%2)] for c,d in E] for a,b in E]
        yield 'D_'+str(2*n),mul,one

def check(nm,mul,one):
    z=len(mul);inv=[next(b for b in range(z) if mul[a][b]==one and mul[b][a]==one) for a in range(z)]
    def cm(a,b):
        # (x u^e) (y u^f), return (base,bit)
        x,e=a;y,f=b
        if not e and not f: return mul[x][y],0
        if not e and f: return mul[y][x],1
        if e and not f:return mul[x][inv[y]],1
        return mul[inv[y]][x],0
    def assoc(a,b,c):
        left=cm(cm(a,b),c);right=cm(a,cm(b,c))
        assert left[1]==right[1]
        if left[1]==0:return mul[inv[left[0]]][right[0]]
        return mul[inv[right[0]]][left[0]]
    C=Counter(mul[mul[inv[a]][inv[b]]][mul[a][b]] for a in range(z) for b in range(z))
    A=Counter(assoc(a,b,c) for a in product(range(z),range(2)) for b in product(range(z),range(2)) for c in product(range(z),range(2)))
    assert all(A[w] == (z**3 if w==one else 0) +7*z*C[w] for w in range(z)),(nm,A,C)
    print(nm,'order',z,'assoc total',sum(A.values()),'associator support',sorted(w for w in A if A[w]>0),'zero_associator',A[one], 'commutator_fiber_values',sorted(set(C.values())))
for nm,mul,one in groups():check(nm,mul,one)

# Independently verify odd-dihedral closed form for every individual rotation.
for n in (3,5):
    elems=list(__import__("itertools").product(range(n),range(2)))
    ix={p:i for i,p in enumerate(elems)}
    mult=[[ix[((a+(-1)**b*c)%n,(b+d)%2)] for c,d in elems] for a,b in elems]
    one=ix[(0,0)]
    inv=[next(j for j in range(2*n) if mult[i][j]==one and mult[j][i]==one) for i in range(2*n)]
    from collections import Counter
    C=Counter(mult[mult[inv[a]][inv[b]]][mult[a][b]] for a in range(2*n) for b in range(2*n))
    assert C[one]==n*n+3*n
    for j in range(1,n): assert C[ix[(j,0)]]==3*n
    for j in range(n): assert C[ix[(j,1)]]==0
print("CHEIN_ASSOCIATOR_FIBERS_VERIFIED")
