from collections import Counter

TOP = 'TOP'
BOT = frozenset()


def analyze(W):
    def q(j): return (0,j)
    def r(j): return (1,j)
    L0=frozenset(q(j) for j in range(W))
    L1=frozenset(r(j) for j in range(W))

    def leq(p,s):
        i,l=p; j,m=s
        return p==s or i>=j+2 or (i==j+1 and m != l+1)

    def comp_down_nonempty(D):
        D=set(D); assert D
        jmin=min(i for i,_ in D)
        out=set()
        for i in range(jmin+2):
            for l in range(W):
                p=(i,l)
                if not any(leq(p,d) for d in D): out.add(p)
        return frozenset(out)

    def meet(a,b):
        if a==TOP: return b
        if b==TOP: return a
        return frozenset(set(a)&set(b))

    def join(a,b):
        if a==TOP or b==TOP: return TOP
        return frozenset(set(a)|set(b))

    def impl(a,b):
        if b==TOP: return TOP
        if a==TOP: return b
        D=set(a)-set(b)
        if not D: return TOP
        return comp_down_nonempty(D)

    def closure(gen):
        E={BOT,TOP,gen}
        changed=True
        while changed:
            changed=False
            old=tuple(E)
            for a in old:
                for b in old:
                    for z in (meet(a,b),join(a,b),impl(a,b)):
                        if z not in E:
                            E.add(z); changed=True
        return E

    # All nonempty rank-0 upsets.
    rank0=[]
    for mask in range(1,1<<W):
        rank0.append(frozenset(q(j) for j in range(W) if mask>>j & 1))

    # All rank-1 upsets.  For a nonempty T subset L1, upward closure forces
    # all of L0 except that a singleton r_l (l<W-1) may omit q_{l+1}.
    rank1=[]
    for mask in range(1,1<<W):
        T=frozenset(r(j) for j in range(W) if mask>>j & 1)
        full=frozenset(set(L0)|set(T))
        rank1.append(full)
        if mask & (mask-1)==0:
            l=(mask.bit_length()-1)
            if l < W-1:
                rank1.append(frozenset((set(L0)-{q(l+1)})|set(T)))
    assert len(rank1)==(1<<W)+W-2

    c0=Counter(len(closure(U)) for U in rank0)
    c1=Counter(len(closure(U)) for U in rank1)
    expected0=Counter({3:1,5:(1<<W)-W-1,9:W-1})
    expected1=Counter({3:(1<<W)-1,5:W-1})
    assert c0==expected0, (W,c0,expected0)
    assert c1==expected1, (W,c1,expected1)

    expected9={frozenset(L0-{q(j)}) for j in range(1,W)}
    actual9={U for U in rank0 if len(closure(U))==9}
    assert actual9==expected9

    expected5_rank1={frozenset((L0-{q(j)})|{r(j-1)}) for j in range(1,W)}
    actual5_rank1={U for U in rank1 if len(closure(U))==5}
    assert actual5_rank1==expected5_rank1

    # Check each maximal nine-element closure is really closed under all
    # operations, not merely that the iterative closure happened to have size 9.
    binary_checks=0
    for a in actual9:
        E=closure(a)
        assert len(E)==9
        for x in E:
            for y in E:
                assert meet(x,y) in E; binary_checks += 1
                assert join(x,y) in E; binary_checks += 1
                assert impl(x,y) in E; binary_checks += 1

    # Structural deep-level lemma: for all tested levels, every point at i>=2
    # lies below every maximal point.  The proof is immediate from i>=0+2.
    deep_checks=0
    for i in range(2,15):
        for l in range(W):
            for m in range(W):
                assert leq((i,l),q(m)); deep_checks += 1

    assert len(closure(BOT))==2
    assert len(closure(TOP))==2
    assert ((1<<W)-W-1)+(W-1)==(1<<W)-2
    return len(rank0)+len(rank1)+binary_checks+deep_checks+5


checks=0
# These are n=1,2,3, i.e. widths 2^n+1 = 3,5,9.
for W in (3,5,9):
    checks += analyze(W)

# Symbolic arithmetic identities for further widths.  This does not replace
# the proof; it guards the displayed multiplicity formulas against transcription
# errors for a broad range of W.
for n in range(1,20):
    W=(1<<n)+1
    rank0_5=(1<<W)-W-1
    rank1_5=W-1
    assert rank0_5+rank1_5==(1<<W)-2; checks += 1
    assert W-1==(1<<n); checks += 1

print(f'VERIFY_OK {checks} exact assertions')
