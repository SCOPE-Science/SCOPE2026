"""Method C: naive brute over itertools.permutations with sorted-based checker.
Table built via sorted()+list.index (distinct from Method B's comparison construction).
Stdlib only.
"""
import itertools, time

S4L = list(itertools.permutations([1,2,3,4]))
P2I = {p:i for i,p in enumerate(S4L)}
# table via sorted rank
TABC = [-1]*10000
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                if len((a,b,c,d))!=len({a,b,c,d}):
                    continue
                s = sorted([a,b,c,d])
                r = (s.index(a)+1, s.index(b)+1, s.index(c)+1, s.index(d)+1)
                TABC[a*1000+b*100+c*10+d] = P2I[r]

def count_pair_C(p1, p2, nmax=9):
    j1, j2 = P2I[p1], P2I[p2]
    out=[]
    for n in range(0, nmax+1):
        if n<4:
            import math
            out.append(math.factorial(n))
            continue
        quads = list(itertools.combinations(range(n),4))
        T = TABC
        total=0
        for pi in itertools.permutations(range(1,n+1)):
            found=False
            for (i,j,k,l) in quads:
                q = T[pi[i]*1000+pi[j]*100+pi[k]*10+pi[l]]
                if q==j1 or q==j2:
                    found=True; break
            if not found:
                total+=1
        out.append(total)
    return out

if __name__=="__main__":
    t0=time.time()
    print(count_pair_C((1,3,4,2),(2,1,4,3),8), f"{time.time()-t0:.2f}s")
