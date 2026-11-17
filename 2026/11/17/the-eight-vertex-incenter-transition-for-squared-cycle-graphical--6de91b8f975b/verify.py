"""Exact cut census and high-precision incenter checks for squared-cycle zonotopes.

The theorem for all orders is proved analytically in RESULT.md. This script checks
finite instances independently, without treating a finite test as a general proof.
"""
from decimal import Decimal, localcontext
from itertools import combinations
from math import comb


def edges(n):
    return tuple((i, (i + step) % n) for i in range(n) for step in (1, 2))


def cut(n, mask, ed):
    return sum(((mask >> a) ^ (mask >> b)) & 1 for a, b in ed)


def active_cut_masks(n):
    ed = edges(n)
    best_num, best_den, best = None, None, []
    for mask in range(1, (1 << n) - 1):
        s = mask.bit_count()
        b = cut(n, mask, ed)
        num, den = b*b, s*(n-s)   # same ordering as squared normalized cut ratio
        if best_num is None or num*best_den < best_num*den:
            best_num, best_den, best = num, den, [mask]
        elif num*best_den == best_num*den:
            best.append(mask)
    return best


def predicted_active(n):
    if n <= 7:
        return {sum(1 << j for j in range(n) if j != i) for i in range(n)} | {1 << i for i in range(n)}
    m = n // 2
    sizes = (m,) if n % 2 == 0 else (m, m + 1)
    return {sum(1 << ((i + t) % n) for t in range(s))
            for i in range(n) for s in sizes}


def rank(vectors, n):
    # Rational elimination is unnecessary: multiply centered indicators by n
    a = [[n * ((mask >> j) & 1) - mask.bit_count()
          for j in range(n)] for mask in vectors]
    from fractions import Fraction
    a = [[Fraction(z) for z in row] for row in a]
    k = 0
    for j in range(n):
        p = next((i for i in range(k, len(a)) if a[i][j] != 0), None)
        if p is None:
            continue
        a[k], a[p] = a[p], a[k]
        t = a[k][j]
        a[k] = [x/t for x in a[k]]
        for i in range(k+1, len(a)):
            if a[i][j] != 0:
                t = a[i][j]
                a[i] = [x-t*y for x,y in zip(a[i], a[k])]
        k += 1
    return k


def extreme_signs(m):
    if m % 2 == 0:
        for plus in combinations(range(m), m//2):
            p = set(plus)
            yield tuple(1 if i in p else -1 for i in range(m))
    else:
        for zero in range(m):
            inds = [i for i in range(m) if i != zero]
            for plus in combinations(inds, (m-1)//2):
                p = set(plus)
                yield tuple(0 if i == zero else (1 if i in p else -1)
                            for i in range(m))


def check_centers(n):
    m = n//2
    with localcontext() as ctx:
        ctx.prec = 65
        D = Decimal
        rho = D(3)*(D(n)/D(m*m)).sqrt()
        beta = D(3)*(D(1) - (D(1)-D(1)/(D(m)*D(m))).sqrt())
        gamma = D(2) - D(3)*D(n-1).sqrt()/D(m)
        b = min(beta,gamma)
        ss = list(extreme_signs(m))
        ed = edges(n)
        # For a fixed subset the maximal center displacement over all predicted
        # center-polytope vertices is an integer multiple of the scale b.
        comparisons=0
        for mask in range(1, (1<<n)-1):
            s=mask.bit_count()
            w=cut(n, mask, ed)
            rhs=D(w)/2-rho*(D(s*(n-s))/D(n)).sqrt()
            counts = [((mask>>i)&1)+((mask>>(i+m))&1) for i in range(m)]
            v = max(abs(sum(u*c for u,c in zip(signs,counts))) for signs in ss)
            assert D(v)*b <= rhs + D('1e-54'), (n, mask, v, rhs, b)
            comparisons += 1
        # Every index bound must be necessary, not just sufficient.
        assert b > 0
        if m==4:
            assert gamma < beta
        else:
            assert beta < gamma
        return comparisons, len(ss), str(b)


def main():
    total=0
    for n in range(6, 17):
        active=set(active_cut_masks(n))
        predicted=predicted_active(n)
        assert active==predicted, (n,len(active),len(predicted),list(active^predicted)[:8])
        r=rank(active,n)
        expected = n-1 if n%2 or n<8 else n//2
        assert r==expected,(n,r,expected)
        total += (1<<n)-2
        print('cut census',n,'active',len(active),'rank',r,'incenter dimension',n-1-r)
    total_c=0
    for n in (8,10,12,14):
        c,v,b=check_centers(n)
        total_c += c
        print('all predicted center vertices valid',n,'vertices',v,'scale',b,'cuts',c)
    print('VERIFIED squared-cycle graphical zonotopes cuts',total,'center constraint masks',total_c)

if __name__=='__main__':
    main()
