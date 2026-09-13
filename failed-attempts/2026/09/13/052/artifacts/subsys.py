"""Decompose the orbit exact cover: segregate moved-point triples (fp=0, P^3) and mixed (fp=1).
Key structural lemma: moved-fixed pairs (f, m) are covered ONLY by mixed orbits (fp=1 triples
{ f, m1 in pair i, m2 in pair j }) or... wait, also by FIX rows? No: FIX rows cover (f, a) with a in pair i
only for the same pair. Let me recompute which rows cover which columns.
Columns: P2 = pair-orbits of moved-moved pairs; M1 = mixed pair-orbits (f, pair i) [27 of them];
U = use columns (9). FIX rows (f,i) cover M1[(f,i)] + U[i].
Mixed orbit {f, x in i, y in j}, i!=j: covers M1[(f,i)], M1[(f,j)]? NO — covers pairs (f,x),(f,y),(x,y):
pair-orbits are (f,i),(f,j), and moved pair-orbit (i,j-flavor). Yes two M1 columns + one P2 column.
P3 orbit {x in i, y in j, z in k}: covers three P2 columns.
So subsystem: FIX(27 rows, covering M1+U) + MIXED orbits (cover 2 M1 + 1 P2) + P3 (3 P2).
Count: M1 has 27 columns; each FIX covers 1, each MIXED covers 2. P3 covers 0.
Let m = #mixed orbits chosen, f9 = #fix rows = 9 (exactly one per use col... but could a use col be covered by nothing else? use cols only in FIX rows, so exactly 9 FIX rows).
M1 coverage: 9*1 + 2m = 27 -> m = 9. So exactly 9 mixed orbit-pairs.
Then P2 columns (72): covered by 9 mixed (1 each) + p P3 orbits (3 each): 9 + 3p = 72 -> p = 21.
Check: total orbits = 9 fix + 9 mixed + 21 P3 = 39 -> blocks = 10 fixed + ... wait fixed blocks: {18,19,20} + 9 FIX = 10; non-fixed blocks = 9*2 + 21*2 = 60; total 70. Correct!
So EVERY solution = distinguished triangle decomposition:
 (a) 9 FIX rows (transversal: pair i -> fixed point f(i)),
 (b) 9 mixed orbits forming an exact cover of remaining M1 pairs: i.e., on 9 pair-slots x 3 fix = 27 M1 cells minus 9 FIXED cells, the 9 mixed orbits each cover 2 cells in the same fix-row. So per fixed point f, the pairs assigned... this is a fixed-point-free... each mixed orbit is a domino within one fix-row. So per f-row with k FIX cells removed, remaining 9-k... must be even -> k odd? 9-k even -> k odd. So each fixed point gets an ODD number of pairs (1,3,5,7). Compositions of 9 into 3 odd parts!
 (c) 21 P3 orbits covering remaining P2 demand.
This gives a strong branching plan: enumerate f-assignments (3^9/6 ~ 3k, up to S3) then domino tilings (small), then P3 exact cover (72-9=63 cells... still big but reduced).
Actually better: joint search over M1+U subsystem first (FIX + mixed only, 36 cols, ~27+216 rows), enumerate ALL (M1,U) solutions — likely only thousands — then for each solve the P2/P3 residual (63 cols... hmm 72 P2 minus 9 covered = 63, /3 = 21 orbits from ~336 P3 rows). That's still a per-node exact cover but with tiny row set.
Let me first enumerate subsystem (b) fully and count.
"""
import time, sys
from itertools import combinations
def sig(x): return x^1 if x<18 else x
def is_fixed_pair(a,b):
    if a>b:a,b=b,a
    sa,sb=sig(a),sig(b)
    return (sa==a and sb==b) or (sa==b and sb==a)
def porb(a,b):
    if a>b:a,b=b,a
    c,d=sig(a),sig(b)
    if c>d:c,d=d,c
    return (a,b) if (a,b)<=(c,d) else (c,d)

# M1 columns: (f,i) for f in 0..2 (meaning 18+f), i in 0..8
def m1(f,i): return f*9+i
UOFF=27
def ucol(i): return UOFF+i
NCOL=36
# rows: FIX 27: [m1(f,i), ucol(i)]; MIXED orbits
rows=[]
# mixed orbit reps: {18+f, x in pair i (2 choices), y in pair j (2 choices)}, i<j; canonical min under sig
seen=set()
nmix=0
for f in range(3):
    F=18+f
    for i in range(9):
        for j in range(i+1,9):
            for x in (2*i,2*i+1):
                for y in (2*j,2*j+1):
                    t=tuple(sorted((F,x,y)))
                    st=tuple(sorted((sig(F),sig(x),sig(y))))
                    if st==t: print("weird fixed",t); continue
                    key=min(t,st)
                    if key in seen: continue
                    seen.add(key)
                    rows.append(([m1(f,i),m1(f,j)],('MIX',key)))
                    nmix+=1
for i in range(9):
    for f in range(3):
        rows.append(([m1(f,i),ucol(i)],('FIX',f,i)))
print("rows:",len(rows),"mixed:",nmix,"+27 fix")
# DLX-ish brute force with MRV in python (36 cols, 243 rows) — fine
col_rows=[[] for _ in range(NCOL)]
for ri,(cl,_) in enumerate(rows):
    for c in cl: col_rows[c].append(ri)
rowmask=[0]*len(rows)
for ri,(cl,_) in enumerate(rows):
    m=0
    for c in cl: m|=(1<<c)
    rowmask.append(m) if False else None
    rowmask[ri]=m
FULL=(1<<NCOL)-1
sys.setrecursionlimit(10000)
sols=[]
nodes=[0]
t0=time.time()
def dfs(rem,chosen):
    nodes[0]+=1
    if rem==0:
        sols.append(list(chosen)); return
    # MRV
    best=-1;bestn=99;besto=None
    r=rem
    while r:
        lsb=r&(-r); c=lsb.bit_length()-1; r^=lsb
        opts=[ri for ri in col_rows[c] if rowmask[ri]&~rem==0]
        if not opts: return
        if len(opts)<bestn: bestn=len(opts);best=c;besto=opts
        if bestn==1: break
    for ri in besto:
        chosen.append(ri)
        dfs(rem&~rowmask[ri],chosen)
        chosen.pop()
tlim=float(sys.argv[1]) if len(sys.argv)>1 else 30
dfs(FULL,[])
print(f"subsystem solutions: {len(sols)} nodes={nodes[0]} t={time.time()-t0:.2f}s")
from collections import Counter
c=Counter()
for s in sols:
    # type signature: per-fix count of FIX cells
    fx=tuple(sorted(sum(1 for ri in s if rows[ri][1][0]=='FIX' and rows[ri][1][1]==f) for f in range(3)))
    c[fx]+=1
print("FIX-per-row type distribution:",dict(c))
