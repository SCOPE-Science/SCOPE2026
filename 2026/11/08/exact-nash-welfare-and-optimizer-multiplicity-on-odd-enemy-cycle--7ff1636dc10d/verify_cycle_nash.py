"""Independent exhaustive check of unlabeled independent-set partitions of cycles."""

def verify(n):
    groups = []
    best = -1
    count = 0
    tested = 0
    def dfs(v):
        nonlocal best, count, tested
        if v == n:
            tested += 1
            product = 1
            for g in groups:
                size = len(g)
                if size == 1:
                    product = 0
                    break
                product *= (size-1)**size
            if product > best:
                best, count = product, 0
            if product == best:
                count += 1
            return
        for g in groups:
            if v - 1 not in g and (v != n-1 or 0 not in g):
                g.append(v)
                dfs(v+1)
                g.pop()
        groups.append([v])
        dfs(v+1)
        groups.pop()
    dfs(0)
    if n % 2 == 0:
        k=n//2
        assert (best,count)==((k-1)**n,1)
    elif n>=7:
        k=(n-1)//2
        assert (best,count)==((k-1)**k * (k-2)**(k-1), 2*n if k==3 else 2*n*(k-1))
    else:
        assert best == 0
    print(f"n={n} valid={tested} product={best} optimizers={count}")

for n in range(3,12):
    verify(n)
print("INDEPENDENT_EXACT_CHECK_OK")
