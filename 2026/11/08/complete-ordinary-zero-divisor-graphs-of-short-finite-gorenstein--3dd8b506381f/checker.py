"""Exact finite-field checks for the socle-polarity graph decomposition.
Run: python3 verify_gorenstein.py
No external packages required.  The graph is built from multiplication, not from the claimed decomposition.
"""
from collections import Counter, deque
from itertools import product
from math import comb

class GF:
    def __init__(self,q):
        self.q=q
        self.p={2:2,3:3,4:2,5:5,7:7,8:2}[q]
        self.modpoly={4:0b111,8:0b1011}.get(q)
    def add(self,a,b):
        return a^b if self.p==2 else (a+b)%self.p
    def mul(self,a,b):
        if self.q==2: return a*b
        if self.p !=2: return (a*b)%self.p
        ans=0
        x=a; y=b
        while y:
            if y&1: ans ^= x
            y>>=1; x<<=1
            if x & self.q: x ^= self.modpoly
        return ans
    def neg(self,a):return a if self.p==2 else (-a)%self.p


def run_case(q,kind):
    f=GF(q); add=f.add; mul=f.mul
    # B matrices: hyperbolic [[0,1],[1,0]], diagonal [[1,0],[0,d]]
    if kind=='split': M=(0,1,1,0)
    elif kind=='alternate': M=(0,1,1,0)
    elif kind=='nonalternate': M=(1,0,0,1)
    else:
        # choose d for anisotropic form a^2+d*b^2
        d=next(d for d in range(1,q) if all(add(mul(a,a),mul(d,mul(b,b)))!=0
                  for a,b in product(range(q),repeat=2) if (a,b)!=(0,0)))
        M=(1,0,0,d)
    a,b,c,d=M
    def B(x,y):
        X,Y=x; U,V=y
        return add(add(mul(a,mul(X,U)),mul(b,mul(X,V))),
                   add(mul(c,mul(Y,U)),mul(d,mul(Y,V))))
    # Each point is a nonzero element of the maximal ideal; multiplication has socle coefficient B.
    pts=[z for z in product(range(q),repeat=3) if z!=(0,0,0)]
    soc=[i for i,(x,y,z) in enumerate(pts) if (x,y)==(0,0)]
    nonsoc=[i for i,(x,y,z) in enumerate(pts) if (x,y)!=(0,0)]
    N=len(pts); assert N==q**3-1
    adj=[set() for _ in pts]
    for i in range(N):
        for j in range(i+1,N):
            if B(pts[i][:2],pts[j][:2])==0:
                adj[i].add(j);adj[j].add(i)
    # Independently compute isotropic projective lines.
    all_lines=set()
    isotropic=set()
    for x,y in product(range(q),repeat=2):
        if x==y==0:continue
        line=frozenset((mul(t,x),mul(t,y)) for t in range(1,q))
        all_lines.add(line)
        if B((x,y),(x,y))==0: isotropic.add(line)
    t=len(isotropic);s=q*(q-1); u=q-1; h=(q+1-t)//2
    assert len(all_lines)==q+1 and t+2*h==q+1
    if kind=='alternate':assert t==q+1
    if kind=='nonalternate':assert t==1
    if kind=='split':assert t==2
    if kind=='anisotropic':assert t==0
    assert len(soc)==u and all(len(adj[i])==N-1 for i in soc)
    remaining=set(nonsoc); component_sizes=[]; shapes=Counter()
    while remaining:
        start=next(iter(remaining)); C={start}; todo=[start]
        while todo:
            x=todo.pop()
            for y in (adj[x]&remaining)-C:
                C.add(y);todo.append(y)
        remaining-=C; component_sizes.append(len(C))
        degrees=Counter(len(adj[x]&C) for x in C)
        if len(C)==s and degrees=={s-1:s}:shapes['clique']+=1
        elif len(C)==2*s and degrees=={s:2*s}:shapes['complete_bipartite']+=1
        else:raise AssertionError((q,kind,len(C),degrees))
    assert shapes['clique']==t and shapes['complete_bipartite']==h
    E=sum(map(len,adj))//2
    target=comb(u,2)+u*((q+1)*s)+t*comb(s,2)+h*s*s
    assert E==target,(E,target)
    expected={N-1:u}
    if t: expected[q*q-2]=t*s
    if h: expected[q*q-1]=2*h*s
    assert Counter(map(len,adj))==Counter(expected)
    print(f'PASS field={q:<2} type={kind:<12} vertices={N:<4} edges={E:<7} iso_lines={t:<2} K_s={t:<2} K_s_s={h:<2}')
    return N

if __name__=='__main__':
    total=0
    for q in (2,4,8):
        for kind in ('alternate','nonalternate'):
            total+=run_case(q,kind)
    for q in (3,5,7):
        for kind in ('split','anisotropic'):
            total+=run_case(q,kind)
    print('VERIFY_OK configurations=12 total_graph_vertices=',total)

# Independent mixed-characteristic check: (Z/p^2Z)[t]/(t^2), m=(p,t), m^2=(pt).
# Its multiplication graph must coincide with the split symplectic model over F_p,
# although its characteristic differs from F_p[x,y]/(x^2,y^2).
def test_mixed_characteristic(p):
    residues=p*p
    elems=[(a,b) for a in range(residues) for b in range(residues) if (a%p==0 and b%p==0 and (a,b)!=(0,0)) or (a%p==0 and b%p!=0)]
    assert len(elems)==p**3-1
    def mult_zero(X,Y):
        a,b=X; c,d=Y
        return (a*c)%residues==0 and (a*d+b*c)%residues==0
    edges=sum(mult_zero(x,y) for i,x in enumerate(elems) for y in elems[i+1:])
    q=p;s=q*(q-1);u=q-1;t=(q+1 if q==2 else 2); h=(q+1-t)//2
    predicted=comb(u,2)+u*(q+1)*s+t*comb(s,2)+h*s*s
    assert edges==predicted,(p,edges,predicted)
    print('PASS mixed_characteristic',p,'vertices',len(elems),'edges',edges)

# Chromatic-polynomial identities (small binary graph) checked by direct vertex-color backtracking.
def test_coloring():
    for alternate in (True,False):
        q=2;s=2;u=1;t=3 if alternate else 1;h=(3-t)//2
        # Construct graph from the actual finite-field bilinear multiplication table.
        M=(0,1,1,0) if alternate else (1,0,0,1)
        pts=[a for a in product(range(q),repeat=3) if a!=(0,0,0)]
        def orth(a,b):
            x,y=a[:2];X,Y=b[:2];e,f,g,d=M
            return (e*x*X+f*x*Y+g*y*X+d*y*Y)%2==0
        edges=[(i,j) for i in range(len(pts)) for j in range(i+1,len(pts)) if orth(pts[i],pts[j])]
        # Backtracking over all proper assignments, not using structural formula.
        for colors in range(1,6):
            prior=[[] for _ in pts]
            for i,j in edges:prior[j].append(i)
            c=[-1]*len(pts)
            def rec(i):
                if i==len(pts):return 1
                ans=0
                used={c[j] for j in prior[i]}
                for col in range(colors):
                    if col not in used:
                        c[i]=col; ans+=rec(i+1)
                c[i]=-1
                return ans
            observed=rec(0)
            def fall(x,k):
                out=1
                for h in range(k):out*=x-h
                return out
            # Stirling second-kind S(2,1)=S(2,2)=1
            v=colors-u
            chrom_bi=fall(v,1)*(v-1)**s+fall(v,2)*(v-2)**s
            predicted=fall(colors,u)*(fall(v,s)**t)*(chrom_bi**h)
            assert observed==predicted,(alternate,colors,observed,predicted)
        print('PASS chromatic_polynomial q=2 type', 'alternate' if alternate else 'nonalternate')

if __name__=='__main__':
    test_mixed_characteristic(2)
    test_mixed_characteristic(3)
    test_coloring()
    print('VERIFY_ALL_OK')

# Characteristic-polynomial check, independently building the adjacency matrix and using
# the Faddeev–LeVerrier trace recurrence. No spectral data from the decomposition is used.
def check_spectrum(q,kind):
    f=GF(q)
    if kind in ('split','alternate'): M=(0,1,1,0)
    elif kind=='nonalternate':M=(1,0,0,1)
    else:
        d=next(d for d in range(1,q) if all(f.add(f.mul(a,a),f.mul(d,f.mul(b,b)))!=0
            for a,b in product(range(q),repeat=2) if a or b))
        M=(1,0,0,d)
    a,b,c,d=M
    def orth(x,y):
        X,Y=x[:2]; U,V=y[:2]
        return f.add(f.add(f.mul(a,f.mul(X,U)),f.mul(b,f.mul(X,V))),
                     f.add(f.mul(c,f.mul(Y,U)),f.mul(d,f.mul(Y,V))))==0
    pts=[v for v in product(range(q),repeat=3) if any(v)]
    n=len(pts)
    A=[[int(i!=j and orth(pts[i],pts[j])) for j in range(n)] for i in range(n)]
    I=[[int(i==j) for j in range(n)] for i in range(n)]
    B=[row[:] for row in I]
    coefficients=[1]
    for k in range(1,n+1):
        T=[[sum(A[i][h]*B[h][j] for h in range(n)) for j in range(n)] for i in range(n)]
        trace=sum(T[i][i] for i in range(n))
        assert trace%k==0
        ck=-trace//k
        coefficients.append(ck)
        for i in range(n):T[i][i]+=ck
        B=T
    def times(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]+=x*y
        return out
    def powlin(root,exp):
        p=[1]
        for _ in range(exp):p=times(p,[-root,1])
        return p
    u=q-1;s=q*(q-1)
    t=(q+1 if kind=='alternate' else 1 if kind=='nonalternate' else 2 if kind=='split' else 0)
    r=(q+1-t)//2
    p=[1]
    for root,exp in [(-1,u-1+t*(s-1)),(s-1,max(t-1,0)),(s,max(r-1,0)),(-s,r),(0,2*r*(s-1))]:
        p=times(p,powlin(root,exp))
    Q=[[u-1]]
    if t:
        for row in Q:row.append(t*s)
        Q.append([u,s-1])
    if r:
        for row in Q:row.append(2*r*s if len(Q)==1 else 0)
        if t:
            Q[0][-1]=2*r*s
            Q.append([u,0,s])
        else:Q.append([u,s])
    from itertools import permutations
    quotient=[0]
    size=len(Q)
    for perm in permutations(range(size)):
        inversions=sum(perm[i]>perm[j] for i in range(size) for j in range(i+1,size))
        term=[(-1)**inversions]
        for i,j in enumerate(perm):term=times(term,[(-Q[i][j]),int(i==j)])
        if len(quotient)<len(term):quotient += [0]*(len(term)-len(quotient))
        for i,x in enumerate(term):quotient[i]+=x
    p=times(p,quotient)
    assert p[::-1]==coefficients,(q,kind,p[::-1],coefficients)
    print('PASS spectral_polynomial field',q,'type',kind,'degree',n)

if __name__=='__main__':
    for q in (2,3):
        for kind in (('alternate','nonalternate') if q==2 else ('split','anisotropic')):
            check_spectrum(q,kind)
    print('VERIFY_COMPLETE_OK')
