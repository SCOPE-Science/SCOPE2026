"""Standalone integer checks for the core-periphery hedonic-family theorem.
Pure Python 3 stdlib. Run python verify.py.
"""

def formulas(q):
    two = (q + 1) ** (2*q + 4)
    three = (2*q - 1) ** (2*q)
    mixed = (q + 1) ** (q + 2) * (q - 1) ** q
    return two, three, mixed


def count_optimal_from_reduced(q):
    products = []
    for a in range(q+1):
        for b in range(q+1):
            r = 2*q-a-b
            if r == 0:
                assert a == b == q
                val = (q+1)**(2*q+4)
            elif r == 1:
                val = 0
            else:
                val = (a+1)**(a+2)*(b+1)**(b+2)*(r-1)**r
            products.append((val,a,b))
    m = max(x[0] for x in products)
    return m, [(a,b) for val,a,b in products if val == m]


def brute_partitions(q):
    n=2*q+4
    ac={0,1}; bc={2,3}
    pa=set(range(4,4+q)); pb=set(range(4+q,4+2*q))
    def enemies(i,j):
        return (i in ac and j in bc|pb) or (j in ac and i in bc|pb) or (i in bc and j in pa) or (j in bc and i in pa)
    best=0; count=0; positive=0; examples=[]
    groups=[]
    def search(i):
        nonlocal best,count,positive,examples
        if i==n:
            count+=1
            prod=1
            for g in groups:
                if len(g)<2 or any(enemies(x,y) for ix,x in enumerate(g) for y in g[ix+1:]):
                    prod=0; break
                prod*= (len(g)-1)**len(g)
            if prod:
                positive+=1
            if prod>best:
                best=prod;examples=[tuple(tuple(g) for g in groups)]
            elif prod==best and prod>0:
                examples.append(tuple(tuple(g) for g in groups))
            return
        for g in groups:
            g.append(i);search(i+1);g.pop()
        groups.append([i]);search(i+1);groups.pop()
    search(0)
    return count,positive,best,examples

for q in range(2,81):
    two,three,mixed=formulas(q)
    assert mixed < two
    best, param = count_optimal_from_reduced(q)
    assert best == max(two,three)
    assert param == ([(q,q)] if q<=8 else [(0,0)]),(q,param)
    assert (three < two)==(q<=8)
    print('q=',q,'winner=',param,'best product digits=',len(str(best))) if q in (2,3,4,8,9,10,80) else None
for q in (2,3):
    partitions,positive,best,examples=brute_partitions(q)
    assert best==max(formulas(q)[:2])
    assert len(examples)==1,(q,len(examples))
    print('brute:',q,'players:',2*q+4,'partitions:',partitions,'positive:',positive,'best:',best,'optima:',len(examples))
print('PASS')
