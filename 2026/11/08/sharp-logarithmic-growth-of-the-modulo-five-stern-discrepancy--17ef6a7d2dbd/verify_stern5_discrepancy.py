"""Exact finite certificate for the Stern sequence modulo-five prefix-discrepancy theorem.
Standard-library Python 3, no external data or dependencies.
"""

STATES = [(a,b) for a in range(5) for b in range(5) if a or b]
INDEX = {q:i for i,q in enumerate(STATES)}
ROOT = INDEX[(0,1)]
LEFT = [INDEX[(a,(a+b)%5)] for a,b in STATES]
RIGHT = [INDEX[((a+b)%5,b)] for a,b in STATES]
W = [int(a == 1)-int(a == 4) for a,b in STATES]

S = [W[:]]
LO = [[min(0,x) for x in W]]
HI = [[max(0,x) for x in W]]
for r in range(28):
    old_s, old_lo, old_hi = S[-1], LO[-1], HI[-1]
    S.append([old_s[LEFT[j]]+old_s[RIGHT[j]] for j in range(24)])
    LO.append([min(old_lo[LEFT[j]],old_s[LEFT[j]]+old_lo[RIGHT[j]]) for j in range(24)])
    HI.append([max(old_hi[LEFT[j]],old_s[LEFT[j]]+old_hi[RIGHT[j]]) for j in range(24)])

assert len(STATES) == 24
assert S[5] == S[1], "four-step full-sum identity (all states)"
assert S[28] == S[16], "twelve-step full-sum identity"
assert all(LO[28][j] == LO[16][j] - 4 for j in range(24))
assert all(HI[28][j] == HI[16][j] + 4 for j in range(24))

# Dynamic-programming extrema, computed in two independent ways.
# First direct recurrence from the individual Stern values for all N<=2^18.
N = 2**18
stern = [0]*(N+1)
stern[1] = 1
for n in range(2,N+1):
    stern[n] = stern[n//2] if n % 2 == 0 else stern[n//2] + stern[n//2 + 1]
partial = 0
min_seen = max_seen = 0
for n in range(N):
    partial += int(stern[n]%5 == 1)-int(stern[n]%5 == 4)
    level = (n+1).bit_length()-1
    if n+1 == 2**level:
        assert partial == S[level][ROOT]
    min_seen = min(min_seen,partial)
    max_seen = max(max_seen,partial)
    if n+1 == 2**level:
        assert min_seen == LO[level][ROOT]
        assert max_seen == HI[level][ROOT]
assert min_seen==LO[18][ROOT] and max_seen==HI[18][ROOT]

# Reconstruct an exact maximizer/minimizer at an exponential scale without searching it.
def extremal_prefix(level, state, maximize):
    if level == 0:
        return int((max if maximize else min)(0,W[state]) == W[state])
    A, B = LEFT[state], RIGHT[state]
    first = (HI if maximize else LO)[level-1][A]
    second = S[level-1][A] + (HI if maximize else LO)[level-1][B]
    if (first >= second) if maximize else (first <= second):
        return extremal_prefix(level-1,A,maximize)
    return 2**(level-1) + extremal_prefix(level-1,B,maximize)

def prefix_from_finite_sums(N,depth=28,state=ROOT):
    if depth==0:
        return W[state] if N else 0
    half=2**(depth-1)
    if N<=half: return prefix_from_finite_sums(N,depth-1,LEFT[state])
    return S[depth-1][LEFT[state]] + prefix_from_finite_sums(N-half,depth-1,RIGHT[state])

for r in [16,18,20,24,27,28]:
    for maximize in [False,True]:
        n=extremal_prefix(r,ROOT,maximize)
        val=prefix_from_finite_sums(n,depth=28)
        assert 0 <= n <= 2**r
        assert val == (HI if maximize else LO)[r][ROOT], (r,maximize,n,val)

# Independent direct enumeration to the first witnesses exceeding the historical sampled bounds.
max_n = extremal_prefix(24, ROOT, True)
min_n = extremal_prefix(24, ROOT, False)
sequence = bytearray(max_n + 1)
sequence[1] = 1
for t in range(2, max_n + 1):
    sequence[t] = sequence[t // 2] if t % 2 == 0 else (sequence[t // 2] + sequence[t // 2 + 1]) % 5
running, min_value, max_value = 0, None, None
for t in range(max_n):
    if t == min_n:
        min_value = running
    running += (sequence[t] == 1) - (sequence[t] == 4)
    if t + 1 == min_n:
        min_value = running
    if t + 1 == max_n:
        max_value = running
assert min_value == -6 and max_value == 12

print('VERIFY_OK states=24 initial_full_sum_period=4 at_r=1')
print('VECTOR_CERTIFICATE min(r+12)=min(r)-4 and max(r+12)=max(r)+4 for all r>=16')
print('DIRECT_STERN prefix_all_N_through=2^18 PASS')
print('TABLE r min max')
for r in range(28):
    print(r,LO[r][ROOT],HI[r][ROOT])
for maximize in [False,True]:
    n=extremal_prefix(24,ROOT,maximize)
    print('WITNESS r=24', 'MAX' if maximize else 'MIN', 'N=',n,'discrepancy=',prefix_from_finite_sums(n))
