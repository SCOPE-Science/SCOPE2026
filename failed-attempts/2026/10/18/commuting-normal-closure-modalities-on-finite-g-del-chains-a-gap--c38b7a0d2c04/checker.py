from itertools import combinations

def ceiling(F,n):
    return tuple(min(y for y in F if y>=x) for x in range(n))

def prediction(F,H,n):
    C=sorted(set(F)&set(H))
    return all(not ((set(F)-set(C))&set(range(a+1,b))) or
               not ((set(H)-set(C))&set(range(a+1,b)))
               for a,b in zip(C,C[1:]))

def compositions(t):
    if t==0: yield ()
    for d in range(1,t+1):
        for tail in compositions(t-d): yield (d,)+tail

for n in range(2,10):
    subsets=[]
    for mask in range(1<<(n-2)):
        F=(0,)+tuple(i+1 for i in range(n-2) if (mask>>i)&1)+(n-1,)
        subsets.append((F,ceiling(F,n)))
    actual=0
    for F,f in subsets:
        for H,g in subsets:
            commutes=all(f[g[i]]==g[f[i]] for i in range(n))
            assert commutes==prediction(F,H,n),(n,F,H)
            actual+=commutes
    predicted=sum(__import__('functools').reduce(lambda p,d:p*(2**d-1),c,1) for c in compositions(n-1))
    assert actual==predicted,(n,actual,predicted)
    print(n,actual)
print('TWO_S4_CHAIN_COMMUTATION_OK')
