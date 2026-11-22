from itertools import product

def allowed(w):
    p=[i for i,a in enumerate(w) if a=='1']
    return all((b-a-1)%2==0 for a,b in zip(p,p[1:]))
def cyclic(w):
    p=[i for i,a in enumerate(w) if a=='1']
    return not p or (allowed(w) and ((len(w)-p[-1]+p[0]-1)%2==0))
def eta(w):
    for k in range(1,len(w)+2):
        for prefix in ([w[:k]] if k<=len(w) else [w+'0',w+'1']):
            if all(w[j]==prefix[j%k] for j in range(len(w))) and cyclic(prefix):return k
    return None

def all_comps(n,L):
    if n<0:return
    if n==0:
        yield ()
    else:
        for j in range(L):
            for t in all_comps(n-(2*j+1),L):yield (j,)+t

num=0
for L in range(2,6):
    for extra in range(0,14):
        for js in all_comps(extra,L):
            w='11'+'0'*(2*L)+'1'+''.join('0'*(2*j)+'1' for j in js)+'0010'
            assert len(w)==2*L+7+extra
            assert allowed(w) and eta(w)==len(w)+1,(L,extra,js,w,eta(w))
            num+=1
print('exact marker checks',num)
for n in range(2,15):
    p=[s for t in product('01',repeat=n) if allowed(s:=''.join(t))]
    q=sum(eta(w)==n+1 for w in p)
    assert max(map(eta,p))==n+1
    print(n,len(p),q)
