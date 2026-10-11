import itertools, math

def partitions(n, r, lo=1):
    if r == 0:
        if n == 0:
            yield ()
        return
    for x in range(lo, n+1):
        if n-x < x*(r-1):
            break
        for q in partitions(n-x, r-1, x):
            yield (x,) + q

def labels(parts):
    out=[]
    for i,a in enumerate(parts):
        out += [i]*a
    return out

def direct(vals, lab):
    n=len(lab)

    # Positive-labeled vertices must form an independent set.
    pos=[v for v,x in enumerate(vals) if x>0]
    for a in range(len(pos)):
        for b in range(a+1,len(pos)):
            if lab[pos[a]] != lab[pos[b]]:
                return False

    # Double Roman conditions.
    for v,x in enumerate(vals):
        if x==0:
            n3=sum(vals[u]==3 and lab[u]!=lab[v] for u in range(n))
            n2=sum(vals[u]==2 and lab[u]!=lab[v] for u in range(n))
            if not (n3>=1 or n2>=2):
                return False
        elif x==1:
            if not any(vals[u]>=2 and lab[u]!=lab[v] for u in range(n)):
                return False
    return True

def predicted(parts):
    N=sum(parts)
    coeff=[0]*(3*N+1)
    for ni in parts:
        # All vertices of the selected part have labels 2 or 3.
        for threes in range(ni+1):
            if ni==1 and threes==0:
                continue
            w=2*ni+threes
            coeff[w] += math.comb(ni,threes)
    return coeff

def min_formula(parts):
    m=min(parts)
    if m==1:
        return 3, sum(n==1 for n in parts)
    return 2*m, sum(n==m for n in parts)

types=0
functions=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=labels(parts)
            actual=[0]*(3*N+1)
            for vals in itertools.product(range(4), repeat=N):
                functions += 1
                if direct(vals,lab):
                    actual[sum(vals)] += 1
            pred=predicted(parts)
            assert actual==pred, (parts,actual,pred)
            mn=min(i for i,c in enumerate(actual) if c)
            assert (mn,actual[mn])==min_formula(parts), (parts,mn,actual[mn],min_formula(parts))
            types += 1

print("VERIFY_OK")
print("multipartite_types_checked =", types)
print("quaternary_labelings_checked =", functions)
print("orders = 2..9")
print("all-function classification matched")
print("all weight-enumerator coefficients matched")
print("minimum weight and minimum-function count matched")
