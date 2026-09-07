"""Method B: Lehmer/factorial-code enumeration with independent decoder + table checker.
Table built via pairwise-comparison ranks (distinct construction from Method C).
Stdlib only.
"""
import itertools, time

S4 = list(itertools.permutations([1,2,3,4]))
PID = {p:i for i,p in enumerate(S4)}
# Build lookup table TAB[idx] = pattern id, via comparison-count ranks
TAB = [-1]*10000
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                if a==b or a==c or a==d or b==c or b==d or c==d:
                    continue
                ra = 1+(a>b)+(a>c)+(a>d)
                rb = 1+(b>a)+(b>c)+(b>d)
                rc = 1+(c>a)+(c>b)+(c>d)
                rd = 1+(d>a)+(d>b)+(d>c)
                TAB[a*1000+b*100+c*10+d] = PID[(ra,rb,rc,rd)]

def decode_lehmer(code, n):
    # code: list length n with 0<=code[i]<n-i ; rem sorted ascending
    rem = list(range(1, n+1))
    out = [0]*n
    for i in range(n):
        out[i] = rem.pop(code[i])
    return tuple(out)

def iter_lehmer_codes(n):
    # odometer over factorial number system, lex order on code tuple
    if n==0:
        yield []
        return
    bounds = [n-i for i in range(n)]
    code = [0]*n
    while True:
        yield tuple(code)
        # increment
        k = n-1
        while k>=0:
            code[k]+=1
            if code[k]<bounds[k]:
                break
            code[k]=0
            k-=1
        if k<0:
            return

def count_pair_B(p1, p2, nmax=9):
    id1, id2 = PID[p1], PID[p2]
    counts = []
    for n in range(0, nmax+1):
        if n<4:
            import math
            counts.append(math.factorial(n))
            continue
        quads = list(itertools.combinations(range(n),4))
        T = TAB
        c = 0
        for code in iter_lehmer_codes(n):
            pi = decode_lehmer(code, n)
            hit=False
            for (i,j,k,l) in quads:
                pid = T[pi[i]*1000+pi[j]*100+pi[k]*10+pi[l]]
                if pid==id1 or pid==id2:
                    hit=True; break
            if not hit:
                c+=1
        counts.append(c)
    return counts

if __name__=="__main__":
    t0=time.time()
    print(count_pair_B((1,3,4,2),(2,1,4,3),8), f"{time.time()-t0:.2f}s")
