def f_int(x): return x**6 - 3*x**5 + x**4 + 3*x**2 - x + 1
def count_affine(p):
    sq = set((t*t) % p for t in range(p))
    n=0; pts=[]
    for x in range(p):
        v = f_int(x) % p
        if v in sq:
            # count roots
            c = sum(1 for t in range(p) if (t*t)%p==v)
            n += c
            if c>0: pts.append((x,c))
    return n, pts
for p in [13,17,31,7,11,3]:
    n,pts = count_affine(p)
    print(f"p={p} affine=#{n} total_proj(assuming 2 inf)={n+2} detail={pts}")
