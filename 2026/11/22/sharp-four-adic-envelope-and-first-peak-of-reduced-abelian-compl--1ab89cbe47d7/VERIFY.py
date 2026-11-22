"""Independent finite checks for a sharp reduced-Abelian envelope of Thue--Morse.
Requires only Python 3. No external dependencies.
"""
from itertools import groupby

def extrema(N):
    lo=[0]*(N+1); hi=[0]*(N+1)
    if N>=2: hi[2]=1
    for L in range(3,N+1):
        a=L//2
        lo[L]=L-1-hi[a+1]
        hi[L]=L-1-(lo[a] if L%2==0 else lo[a+1])
    return lo,hi

def reduced_count(a,b):
    return sum(2 if j%2==0 else 1 for j in range(a,b+1))

MAX=4**9
lo,hi=extrema(MAX)
for m in range(2,10):
    bound=4**m
    expected=(3*(m+2)+1)//2
    vals=[reduced_count(lo[n],hi[n]) for n in range(1,bound+1)]
    q=(2*bound+4)//3
    first=q+(2 if m%2 else 0)
    observed=max(vals)
    first_actual=vals.index(observed)+1
    assert observed==expected, (m,observed,expected)
    assert first_actual==first, (m,first_actual,first)
    assert hi[q]-lo[q]==m+1
    assert reduced_count(lo[first],hi[first])==expected
    print(f'power-four m={m}, bound={bound}, max={observed}, first={first}')

# Independent prefix-based extrema (no extrema recurrence) and direct Parikh count.
T=''.join(str(n.bit_count()%2) for n in range(1<<15))
changes=[int(T[j]!=T[j+1]) for j in range(len(T)-1)]
prefix=[0]
for x in changes: prefix.append(prefix[-1]+x)
for L in range(1,513):
    alts=[prefix[i+L-1]-prefix[i] for i in range(len(T)-L+1)]
    direct_min,direct_max=min(alts),max(alts)
    assert (direct_min,direct_max)==(lo[L],hi[L]),(L,(direct_min,direct_max),(lo[L],hi[L]))
    # The Thue-Morse factor language is complement-closed, so this interval
    # determines the reduced Parikh-vector count independently.
    if L<=64:
        # Explicitly enumerate reductions of all windows, distinct Parikh vectors.
        classes=set()
        for i in range(len(T)-L+1):
            a=alts[i]
            first=int(T[i])
            zeros=(a+2)//2 if first==0 else (a+1)//2
            ones=a+1-zeros
            classes.add((zeros,ones))
        assert len(classes)==reduced_count(lo[L],hi[L]),(L,len(classes))
print('Independent factor-window extrema verified for all lengths 1..512.')
print('Direct reduced-Parikh class counts verified for all lengths 1..64.')
