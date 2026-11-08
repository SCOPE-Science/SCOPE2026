"""Reproduce the exact Schlaefli-graph Ising ground-state census.

Requires only Python 3 and a C++17 compiler. The two C++ programs enumerate
all 2^27 spin assignments by different recurrences. No external graph files.
"""
import itertools
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
VERT = [('E',i) for i in range(6)] + [('L',i,j) for i,j in itertools.combinations(range(6),2)] + [('C',i) for i in range(6)]

def intersect(a,b):
    if {'E':0,'L':1,'C':2}[a[0]] > {'E':0,'L':1,'C':2}[b[0]]: a,b=b,a
    if a[0]==b[0] and a[0] in ('E','C'): return False
    if a[0]=='E' and b[0]=='L': return a[1] in b[1:]
    if a[0]=='E' and b[0]=='C': return a[1]!=b[1]
    if a[0]==b[0]=='L': return not (set(a[1:]) & set(b[1:]))
    if a[0]=='L' and b[0]=='C': return b[1] in a[1:]
    raise AssertionError((a,b))

A = [[int(i!=j and not intersect(VERT[i], VERT[j])) for j in range(27)] for i in range(27)]
assert all(sum(A[i])==16 for i in range(27))
assert sum(map(sum,A))//2==216
assert all(sum(A[i][v]*A[v][j] for v in range(27))==(10 if A[i][j] else 8)
           for i in range(27) for j in range(i+1,27))
# A 9-coloring certificate by cocliques; every outside vertex sees two members.
PARTITION=[(0,6,22),(1,11,23),(3,8,21),(4,18,24),(5,20,25),
           (2,17,26),(7,13,19),(9,14,15),(10,12,16)]
assert sorted(v for block in PARTITION for v in block)==list(range(27))
for i,T in enumerate(PARTITION):
    assert all(A[x][y]==0 for x,y in itertools.combinations(T,2))
    for j,U in enumerate(PARTITION):
        if i!=j:
            assert all(sum(A[x][y] for y in U)==2 for x in T)

expected = [
 (0,1),(16,27),(32,135),(48,45),(60,2160),(72,6750),
 (84,1080),(92,42120),(100,86400),(108,8400),(112,247860),
 (116,351216),(120,22968),(120,495720),(120,495720),(120,22968),
 (116,351216),(112,247860),(108,8400),(100,86400),(92,42120),
 (84,1080),(72,6750),(60,2160),(48,45),(32,135),(16,27),(0,1)
]
# The spectral bound is 2/3*k*(27-k); evenness rounds down to an even cut.
assert all(cut==2*(k*(27-k)//3) for k,(cut,mul) in enumerate(expected))
# The explicit partial color-class construction attains every bound.
for k,(cut,mul) in enumerate(expected):
    m,r=divmod(k,3)
    chosen=[v for T in PARTITION[:m] for v in T] + list(PARTITION[m][:r] if m<9 else ())
    computed=sum(A[u][v] for u in chosen for v in range(27) if v not in chosen)
    assert computed==cut

with tempfile.TemporaryDirectory(prefix='finite-ising-') as td:
    answers=[]
    for stem in ('verify_gray','verify_dp'):
        exe=pathlib.Path(td)/stem
        subprocess.run(['c++','-O3','-std=c++17',str(ROOT/(stem+'.cpp')),'-o',str(exe)],check=True)
        p=subprocess.run([str(exe)],check=True,capture_output=True,text=True)
        values=[tuple(map(int,line.split())) for line in p.stdout.splitlines()]
        assert len(values)==28
        assert values==[(k,c,m) for k,(c,m) in enumerate(expected)]
        answers.append(values)
    assert answers[0]==answers[1]

counts=[m for c,m in expected]
assert counts[12]+counts[13]+counts[14]+counts[15]==1037376
assert sum(counts[9:13])==630444
assert sum(counts[6:10])==138000
assert sum(counts[3:7])==10035
assert sum(counts[0:4])==208
assert [counts[k] for k in (12,9,6,3,0)]==[22968,8400,1080,45,1]
print('VERIFIED: 134217728 spin states; both exhaustive methods agree; all analytical profile/degeneracies verified.')
