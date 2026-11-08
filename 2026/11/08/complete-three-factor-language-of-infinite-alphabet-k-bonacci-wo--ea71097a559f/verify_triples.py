"""Independent finite tests of the explicit three-factor classification."""
from itertools import product

def morphic_iterates(k,N):
    w=(0,)
    yield w
    for _ in range(N):
        new=[]
        for d in w:
            q,r=divmod(d,k)
            if r==k-1:new.append(d+1)
            else:new.extend((q*k,d+1))
        w=tuple(new)
        yield w

def block_iterates(k,N):
    words=[(0,)]
    for n in range(1,N+1):
        if n<k:
            w=tuple(v for j in range(n-1,-1,-1) for v in words[j])+(n,)
        else:
            w=tuple(v for j in range(n-1,n-k,-1) for v in words[j])+tuple(k+v for v in words[n-k])
        words.append(w)
    return words

def tau(j,k):
    assert j>=1
    return j-j%k if j%k else j-k+1

def first_patterns(k,N):
    items=[((0,1,0),2)]
    items.extend(((1,0,j),j) for j in range(2,k))
    for j in range(2,N):
        items.extend([((tau(j,k),j,0),j+1),((j,0,1),j+1)])
    for j in range(1,N):
        items.append(((tau(j,k),j,k),k+j-1))
        if j>=2:items.append(((j,k,k+1),k+j-1))
    return items

def predicted_factors(k,n,items):
    factors=set()
    for B,birth in items:
        for h in range(max(0,(n-birth)//k+1)):
            factors.add(tuple(x+h*k for x in B))
    return factors

def in_language(k,xyz):
    x,y,z=xyz
    q,r=divmod(z,k)
    if r==0:
        if x>=q*k and y>=q*k:
            a,b=x-q*k,y-q*k
            if (a,b)==(0,1):return True
            if b>=2 and a==tau(b,k):return True
        if q>=1 and x>=(q-1)*k and y>=(q-1)*k:
            a,b=x-(q-1)*k,y-(q-1)*k
            if b>=1 and a==tau(b,k):return True
        return False
    if r==1:
        if x>=q*k and y==q*k and x-q*k>=2:return True
        if q>=1 and x>=(q-1)*k and y==q*k and x-(q-1)*k>=2:return True
        return False
    return x==q*k+1 and y==q*k and 2<=r<k

cases=[(3,17),(4,15),(5,14),(6,13),(7,12),(8,11)]
num_iterates=num_three=num_membership=0
for k,N in cases:
    words1=list(morphic_iterates(k,N))
    words2=block_iterates(k,N)
    assert words1==words2
    items=first_patterns(k,N+1)
    for n,w in enumerate(words1):
        actual={tuple(w[i:i+3]) for i in range(len(w)-2)}
        predicted=predicted_factors(k,n,items)
        assert actual==predicted,(k,n,actual-predicted,predicted-actual)
        num_iterates+=1
        num_three+=len(actual)
    # Infinite-language membership: every triple with digits <=M must appear in W_(M+k).
    M={3:10,4:9,5:8,6:7,7:6,8:5}[k]
    w=block_iterates(k,M+k)[-1]
    observed={tuple(w[i:i+3]) for i in range(len(w)-2)}
    for xyz in product(range(M+1),repeat=3):
        assert in_language(k,xyz)==(xyz in observed),(k,M,xyz)
        num_membership+=1
    print(f'k={k}: through n={N}, length={len(words1[-1])}, triples={len(predicted_factors(k,N,items))}, M={M} tests OK')
print('PASS: word recurrences,',num_iterates,'finite languages,',num_three,'factor instances,',num_membership,'membership checks')
