"""Independent finite checks for the crown-graph dissociation homotopy and symmetry theorem.
Runs using Python standard library only; not a substitute for the general topological proof.
"""
from itertools import combinations, permutations
from math import comb

def choose(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0

def enumerate_faces(n):
    A=[i for i in range(n)]
    B=[n+i for i in range(n)]
    edges=[(i,n+j) for i in range(n) for j in range(n) if i!=j]
    nei=[0]*(2*n)
    for x,y in edges:nei[x]|=1<<y;nei[y]|=1<<x
    f1=set(); f2=set()
    for mask in range(1,1<<(2*n)):
        # Direct induced maximum degree test.
        ok1=all((mask&nei[v]).bit_count()<=1 for v in range(2*n) if mask>>v&1)
        if ok1:f1.add(mask)
        ai=[i for i in range(n) if mask>>i&1]
        bj=[j for j in range(n) if mask>>(j+n)&1]
        # Completely separate facet-containment test.
        ok2=(not ai or not bj) or (len(ai)<=2 and len(bj)<=2 and
            any(set(ai).issubset({i,j}) and set(bj).issubset({i,j}) for i,j in combinations(range(n),2)))
        if ok2:f2.add(mask)
    assert f1==f2,(n,len(f1^f2))
    return f1

def sign_for_face(mask,mapping,n):
    v=[j for j in range(2*n) if mask>>j&1]
    w=[mapping[j] for j in v]
    if set(w)!=set(v):return 0
    return -1 if sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))%2 else 1

def lefschetz_reduced(faces,mapping,n):
    return sum((-1)**(s.bit_count()-1)*sign_for_face(s,mapping,n) for s in faces)-1

def rank_mod2(rows):
    piv={}
    for z in rows:
        while z:
            j=z.bit_length()-1
            if j in piv:z ^= piv[j]
            else:piv[j]=z;break
    return len(piv)

def mod2_betti(n,faces):
    fs={}
    for s in faces:fs.setdefault(s.bit_count()-1,[]).append(s)
    ranks={}
    for k in range(1,max(fs)+1):
        ind={s:j for j,s in enumerate(fs[k-1])}
        cols=[sum(1<<ind[s^(1<<v)] for v in range(2*n) if s>>v&1) for s in fs[k]]
        ranks[k]=rank_mod2(cols)
    return [len(fs[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0) for k in range(max(fs)+1)]

for n in range(3,7):
    faces=enumerate_faces(n)
    f=[sum(1 for s in faces if s.bit_count()==k) for k in range(1,max(n,4)+1)]
    formula=[]
    for k in range(1,max(n,4)+1):
        val=2*choose(n,k)
        if k==2:val+=n*n
        if k==3:val+=4*choose(n,2)
        if k==4:val+=choose(n,2)
        formula.append(val)
    assert f==formula,(n,f,formula)
    betti=mod2_betti(n,faces)
    assert betti==[0,0,choose(n-1,2)]+[0]*(len(betti)-3),(n,betti)
    count=0
    for perm in permutations(range(n)):
        fixed=sum(perm[i]==i for i in range(n))
        two=sum(perm[perm[i]]==i and perm[i]!=i for i in range(n))//2
        expected=((fixed-1)*(fixed-2)//2)-two
        for swap in (0,1):
            mapping=[(n if swap else 0)+perm[i] for i in range(n)]+[perm[i] if swap else n+perm[i] for i in range(n)]
            actual=lefschetz_reduced(faces,mapping,n)
            assert actual==(-expected if swap else expected),(n,perm,swap,actual,expected)
            count+=1
    print('n=',n,'faces=',sum(f),'face_vector=',f,'mod2_reduced_Betti=',betti,'group_elements_checked=',count)
print('ALL_CHECKS_PASS')
