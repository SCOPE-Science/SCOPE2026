from itertools import combinations_with_replacement, permutations
from math import comb
from functools import lru_cache

checks = 0

def check(cond, msg='assertion failed'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

@lru_cache(None)
def stirling(n,k):
    if n == k == 0: return 1
    if n == 0 or k == 0: return 0
    return k*stirling(n-1,k) + stirling(n-1,k-1)

def partitions(seq):
    # canonical set partitions as tuples of tuples, blocks ordered by least element
    seq = tuple(seq)
    if not seq:
        yield ()
        return
    first = seq[0]
    for rest in partitions(seq[1:]):
        yield ((first,),) + rest
        for i in range(len(rest)):
            b = tuple(sorted((first,) + rest[i]))
            yield tuple(sorted(rest[:i] + (b,) + rest[i+1:], key=lambda x:x[0]))

def uniq_partitions(n):
    return set(partitions(tuple(range(n))))

def perms3(t):
    return set(permutations(t,3))

def cycle_orbits(k):
    # Universe e=-1 plus k diversity atoms 0..k-1; f=id, so Peircean cycles are S_3-orbits.
    U = (-1,) + tuple(range(k))
    unseen = set((a,b,c) for a in U for b in U for c in U)
    orbits=[]
    while unseen:
        t=next(iter(unseen))
        o=perms3(t)
        unseen -= o
        orbits.append(o)
    return orbits

def make_T(k, mask):
    e=-1
    T=set()
    U=(e,) + tuple(range(k))
    # Exactly the consistent identity cycles [a,e,a].
    for a in U:
        T |= perms3((a,e,a))
    free=list(combinations_with_replacement(range(k),3))
    for i,m in enumerate(free):
        if (mask>>i)&1:
            T |= perms3(m)
    return U,T,free

def check_axioms(U,T):
    e=-1
    # IP with f=id
    for a,b,c in list(T):
        check((a,c,b) in T)
        check((c,b,a) in T)
    # II
    for a in U:
        for b in U:
            check(((a,e,b) in T) == (a==b))

# Structural cycle check: all free cycles are exactly diversity multisets of size 3.
for k in range(0,6):
    obs=cycle_orbits(k)
    div=[o for o in obs if all(-1 not in t for t in o)]
    ident=[o for o in obs if any(-1 in t for t in o)]
    check(len(div)==comb(k+2,3), (k,len(div)))
    # Identity cycle consistency is completely forced by II.
    forced=0
    forbidden=0
    for o in ident:
        representative=next(iter(o))
        # all permutations have same multiset; allowed iff it is {a,a,e} for some a (including a=e)
        vals=sorted(representative)
        ok=(vals.count(-1)==1 and len(set(vals))==2) or (vals==[-1,-1,-1])
        if ok: forced += 1
        else: forbidden += 1
    check(forced==k+1)
    check(forced+forbidden==len(ident))

# Exhaustively instantiate every admissible free-cycle pattern through k=3 and check IP/II.
for k in range(0,4):
    q=comb(k+2,3)
    seen=set()
    for mask in range(1<<q):
        U,T,free=make_T(k,mask)
        check_axioms(U,T)
        frozen=frozenset(T)
        check(frozen not in seen)
        seen.add(frozen)
    check(len(seen)==2**q)

# Independent partition enumeration versus Stirling recursion.
for n in range(0,8):
    P=uniq_partitions(n)
    check(len(P)==sum(stirling(n,k) for k in range(n+1)))
    for k in range(n+1):
        check(sum(len(p)==k for p in P)==stirling(n,k))

# Type spectrum formula and its two-case derivation.
def type_count(n):
    return sum(stirling(n+1,k+1)*2**comb(k+2,3) for k in range(n+1))

def type_count_two_case(n):
    total=0
    for k in range(n+1):
        no_e=stirling(n,k)
        with_e=(k+1)*stirling(n,k+1)
        check(no_e+with_e==stirling(n+1,k+1))
        total += (no_e+with_e)*2**comb(k+2,3)
    return total

expected=[3,23,1135,1059247,34375535071,72058315739597647]
for n,v in enumerate(expected,1):
    check(type_count(n)==v,(n,type_count(n),v))
    check(type_count_two_case(n)==v)

# Injective ordered tuples: either all n entries are diversity atoms, or one coordinate is e.
def injective_count(n):
    return 2**comb(n+2,3) + n*2**comb(n+1,3)
expected_inj=[3,20,1072,1052672,34364981248,72057800196358144]
for n,v in enumerate(expected_inj,1):
    check(injective_count(n)==v)

# One-point extension over a finite substructure with d diversity atoms.
# The free cycles containing the new x are: xxx; a,xx (d choices); abx for multisets ab (C(d+1,2)).
for d in range(0,9):
    bits=1+d+comb(d+1,2)
    check(bits==comb(d+2,2))
    check(2**bits==2**comb(d+2,2))

# The leading k=n term dominates the full type count; verify the exact gap exponent to next term.
for n in range(1,20):
    check(comb(n+2,3)-comb(n+1,3)==comb(n+1,2))
    check(type_count(n) >= 2**comb(n+2,3))

print('TYPE_COUNTS', expected)
print('INJECTIVE_COUNTS', expected_inj)
print('VERIFY_OK', checks, 'exact assertions; all admissible FSIASe tables exhausted through 3 diversity atoms')
