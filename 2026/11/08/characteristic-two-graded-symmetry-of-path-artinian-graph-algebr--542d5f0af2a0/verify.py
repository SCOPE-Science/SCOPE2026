"""Independent finite enumeration of graded automorphisms of path Artinian algebras."""
from itertools import product


def field(q):
    if q == 4:
        def mul(a, b):
            out = 0
            for i in (0, 1):
                for j in (0, 1):
                    if ((a >> i) & 1) and ((b >> j) & 1):
                        out ^= (1 << (i+j))
            if out & 4: out ^= 7  # t^2=t+1 in GF(4)
            return out
        return lambda a,b: a^b, mul
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q


def count(n, q):
    add,mul = field(q)
    vals = [u for u in product(range(q), repeat=n) if any(u)]
    good_pairs = [(i,j) for i in range(n) for j in range(i+2,n)]
    def product_is_zero(v,w):
        return all(add(mul(v[i],w[j]),mul(v[j],w[i]))==0 for i,j in good_pairs)
    good = [v for v in vals if product_is_zero(v,v)]
    compat = {v:[w for w in good if product_is_zero(v,w)] for v in good}
    def rank(columns):
        m = [[columns[c][r] for c in range(len(columns))] for r in range(n)]
        pivots=0
        for col in range(len(columns)):
            found=next((r for r in range(pivots,n) if m[r][col]),None)
            if found is None: continue
            m[pivots],m[found]=m[found],m[pivots]
            inverse=next(a for a in range(1,q) if mul(a,m[pivots][col])==1)
            m[pivots]=[mul(inverse,x) for x in m[pivots]]
            for r in range(pivots+1,n):
                if m[r][col]:
                    scalar=m[r][col]
                    # subtraction == addition in char 2
                    m[r]=[add(x,mul(scalar,y)) if q in (2,4) else (x-mul(scalar,y))%q for x,y in zip(m[r],m[pivots])]
            pivots+=1
        return pivots
    total=0
    def rec(columns):
        nonlocal total
        if len(columns)==n:
            total+=1;return
        for v in (compat[columns[-1]] if columns else good):
            if rank(columns+[v])==len(columns)+1:
                rec(columns+[v])
    rec([])
    return total


def verify():
    tests = [(4,2),(5,2),(6,2),(4,3),(5,3),(4,4)]
    for n,q in tests:
        got=count(n,q)
        predicted=2*q**(4 if q%2==0 else 2)*(q-1)**n
        print(f"n={n} q={q} computed={got} expected={predicted}")
        assert got==predicted,(n,q,got,predicted)
    print('VERIFY_OK')

if __name__=='__main__': verify()
