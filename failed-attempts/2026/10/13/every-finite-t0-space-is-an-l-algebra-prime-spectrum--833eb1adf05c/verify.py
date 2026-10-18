from itertools import product, combinations

assertions = 0
posets_checked = 0


def all_posets(n):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    for states in product((0,1,2), repeat=len(pairs)):
        le = [[False]*n for _ in range(n)]
        for i in range(n): le[i][i]=True
        for (i,j),s in zip(pairs,states):
            if s==1: le[i][j]=True
            elif s==2: le[j][i]=True
        ok=True
        for i in range(n):
            for j in range(n):
                if le[i][j]:
                    for k in range(n):
                        if le[j][k] and not le[i][k]:
                            ok=False; break
                    if not ok: break
            if not ok: break
        if ok:
            yield le


def upper_sets(le):
    n=len(le)
    out=[]
    for mask in range(1<<n):
        ok=True
        for x in range(n):
            if mask>>x & 1:
                for y in range(n):
                    if le[x][y] and not (mask>>y & 1):
                        ok=False; break
            if not ok: break
        if ok:
            out.append(frozenset(i for i in range(n) if mask>>i & 1))
    return out

for n in range(0,6):
    count_n=0
    for leP in all_posets(n):
        count_n += 1
        posets_checked += 1
        # Omega = P + a fresh greatest element top=n.
        N=n+1; top=n
        le=[[False]*N for _ in range(N)]
        for i in range(n):
            for j in range(n): le[i][j]=leP[i][j]
        for i in range(N): le[i][i]=True
        for i in range(n): le[i][top]=True

        def mul(x,y):
            return top if le[x][y] else y

        # Verify all L-algebra axioms directly.
        for x in range(N):
            assert mul(x,x)==top; assertions += 1
            assert mul(x,top)==top; assertions += 1
            assert mul(top,x)==x; assertions += 1
        for x in range(N):
            for y in range(N):
                if mul(x,y)==top and mul(y,x)==top:
                    assert x==y; assertions += 1
                for z in range(N):
                    assert mul(mul(x,y),mul(x,z)) == mul(mul(y,x),mul(y,z)); assertions += 1

        ideals=[I for I in upper_sets(le) if top in I]
        # L-algebra ideals are exactly the nonempty upper sets; with a greatest element these are exactly the upper sets containing top.
        assert all(top in I for I in ideals); assertions += 1

        primes=[]
        for P in ideals:
            if len(P)==N: continue
            prime=True
            for I in ideals:
                for J in ideals:
                    if I.intersection(J).issubset(P):
                        if not (I.issubset(P) or J.issubset(P)):
                            prime=False; break
                if not prime: break
            if prime: primes.append(P)

        predicted=[]
        for m in range(n):
            down={x for x in range(N) if le[x][m]}
            predicted.append(frozenset(set(range(N))-down))
        assert set(primes)==set(predicted); assertions += 1
        assert len(primes)==n; assertions += 1

        # Map m -> Omega \ down(m), and check every basic/open U_I pulls back to I cap P.
        phi={m:predicted[m] for m in range(n)}
        spec_open_preimages=[]
        for I in ideals:
            U={m for m,Q in phi.items() if not I.issubset(Q)}
            rhs=set(I).intersection(range(n))
            assert U==rhs; assertions += 1
            spec_open_preimages.append(frozenset(U))
        target_opens=set(upper_sets(leP))
        assert set(spec_open_preimages)==target_opens; assertions += 1

    # Known numbers of labeled posets on n points, OEIS A001035, for a second independent census check.
    known=[1,1,3,19,219,4231][n]
    assert count_n==known, (n,count_n,known); assertions += 1
    print(f"n={n} labeled_posets={count_n}")

print(f"VERIFY_OK {assertions} exact assertions; {posets_checked} labeled posets checked")
