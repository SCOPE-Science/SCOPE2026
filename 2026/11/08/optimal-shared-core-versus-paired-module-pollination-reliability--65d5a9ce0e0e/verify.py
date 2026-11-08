"""Independent finite checks for three-plant pollinator-loss reliability."""
from itertools import combinations

checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def hub(d, s):
    core = set(range(s))
    return tuple(frozenset(core | set(range(s+(d-s)*i,s+(d-s)*(i+1)))) for i in range(3))


def paired(d, s):
    common = set(range(2*s))
    p1 = set(range(2*s,d))
    p2 = set(range(d,2*d-2*s))
    p3 = set(range(2*d-2*s,3*d-2*s))
    return (frozenset(common|p1),frozenset(common|p2),frozenset(p3))


def robust_numerator(sets, a, b):
    m = len(set().union(*sets))
    d = len(sets[0])
    assert all(len(S) == d for S in sets)
    powers_a = [a**i for i in range(m+1)]
    powers_b = [b**i for i in range(m+1)]
    ans = powers_b[m] - 3 * powers_a[d]*powers_b[m-d] - powers_a[m]
    for i, j in combinations(range(3),2):
        u = len(sets[i]|sets[j])
        ans += powers_a[u]*powers_b[m-u]
    return ans


def brute_numerator(sets, a, b):
    m=len(set().union(*sets))
    total=0
    for mask in range(1<<m):
        surviving={i for i in range(m) if mask&(1<<i)}
        if all(surviving & S for S in sets):
            z=len(surviving)
            total += (b-a)**z * a**(m-z)
    return total


def signature(sets):
    a,b,c = sets
    t=len(a & b & c)
    pair=(len((a&b)-c), len((a&c)-b),len((b&c)-a))
    return t,tuple(sorted(pair))

for d,s in [(2,1),(3,1),(4,1),(4,2),(5,2)]:
    h=hub(d,s)
    p=paired(d,s)
    m=3*d-2*s
    check(len(set().union(*h)) == m,(d,s,'hub-union'))
    check(len(set().union(*p)) == m,(d,s,'paired-union'))
    check(signature(h) == (s,(0,0,0)),(d,s,'hub-sig'))
    check(signature(p) == (0,(0,0,2*s)),(d,s,'paired-sig'))
    for a,b in [(1,4),(1,2),(2,3),(3,4),(9,10)]:
        rh=robust_numerator(h,a,b)
        rp=robust_numerator(p,a,b)
        # Clearing denominators in q^(2d-2s)(1-q^s)(1-2q^s)
        prediction = a**(2*d-2*s) * b**(d-2*s) * (b**s-a**s) * (b**s-2*a**s)
        check((rp-rh) == prediction, (d,s,a,b,'factorization'))
        if m<=8:
            check(rh==brute_numerator(h,a,b),(d,s,a,b,'hub-brute'))
            check(rp==brute_numerator(p,a,b),(d,s,a,b,'pair-brute'))

for d,s in [(2,1),(3,1),(4,2)]:
    m=3*d-2*s
    subset_masks=[]
    for comb in combinations(range(m),d):
        subset_masks.append(sum(1<<k for k in comb))
    full=(1<<m)-1
    qs=[(1,4),(1,2),(3,4)]
    powers=[]
    for a,b in qs:
        vals=[a**e*b**(m-e) for e in range(m+1)]
        base=b**m-3*vals[d]-a**m
        powers.append((a,b,vals,base))
    winners=[set() for _ in qs]
    best=[None]*len(qs)
    num=0
    for x in subset_masks:
        for y in subset_masks:
            xy=x|y
            for z in subset_masks:
                if xy|z != full:
                    continue
                num+=1
                t=(x&y&z).bit_count()
                b12=((x&y)&~z).bit_count()
                b13=((x&z)&~y).bit_count()
                b23=((y&z)&~x).bit_count()
                sig=(t,tuple(sorted((b12,b13,b23))))
                unions=((x|y).bit_count(),(x|z).bit_count(),(y|z).bit_count())
                for ix,(a,b,vals,base) in enumerate(powers):
                    val=base+sum(vals[u] for u in unions)
                    if best[ix] is None or val>best[ix]:
                        best[ix]=val
                        winners[ix]={sig}
                    elif val==best[ix]:
                        winners[ix].add(sig)
    check(num>0,('enumerated',d,s))
    allowed_b={(0,(0,0,2*s))}
    allowed_h={(s,(0,0,0))}
    for ix,(a,b,vals,base) in enumerate(powers):
        sigs=allowed_b if a**s*2<b**s else allowed_h if a**s*2>b**s else allowed_b|allowed_h
        check(winners[ix] == sigs, (d,s,a,b,'winners',winners[ix],sigs))
    print('EXHAUSTIVE',f'd={d} s={s} m={m}',f'{num} labeled neighborhoods',f'optimizers {winners}')

print('PASS',checks,'exact assertions')
