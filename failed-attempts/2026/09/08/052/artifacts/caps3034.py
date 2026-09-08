"""AG(3,4) cap utilities: F4 arithmetic, points, lines, cap/completeness checks."""
import itertools
add = lambda a,b: a^b
_MUL = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
def mul(a,b): return _MUL[a][b]
def coords(p): return ((p>>4)&3,(p>>2)&3,p&3)
def pt(c): return (c[0]<<4)|(c[1]<<2)|c[2]
PTS = list(range(64))
def build_lines():
    dirs=[]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                if (a,b,c)==(0,0,0): continue
                first = a if a!=0 else (b if b!=0 else c)
                if first!=1: continue
                dirs.append((a,b,c))
    lines=set()
    for d in dirs:
        seen=set()
        for p in PTS:
            if p in seen: continue
            c=coords(p)
            L=tuple(sorted(pt((add(c[0],mul(t,d[0])),add(c[1],mul(t,d[1])),add(c[2],mul(t,d[2])))) for t in range(4)))
            lines.add(L)
            for q in L: seen.add(q)
    return sorted(lines)
LINES = build_lines()
# pair -> line index; point -> lines containing it
PAIR2LINE={}
PT2LINES={p:[] for p in PTS}
for i,L in enumerate(LINES):
    for a,b in itertools.combinations(sorted(L),2):
        PAIR2LINE[(a,b)]=i
    for q in L: PT2LINES[q].append(i)
def is_cap(S):
    S=set(S)
    for L in LINES:
        if len(S.intersection(L))>=3: return False
    return True
def secant_covered(S):
    S=set(S); cov=set()
    for L in LINES:
        n=sum(1 for q in L if q in S)
        if n==2:
            for q in L:
                if q not in S: cov.add(q)
    return cov
def uncovered(S):
    S=set(S); cov=secant_covered(S)
    return sorted(p for p in PTS if p not in S and p not in cov)
def is_complete(S):
    return is_cap(S) and not uncovered(S)
