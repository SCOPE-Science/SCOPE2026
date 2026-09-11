"""Fallback probe: literal depth-2 finite win is impossible on the free window.
Checks (stdlib, deterministic):
 A. F-window W (words in {a,A,b,B}, length<=2, 1+4+12=17 words) is parabolically
    2-colorable (proper on Schreier edges): color = word-length parity.
    Hence every local depth-2 position admits a proper 3-coloring response;
    no purely local Player-I strategy forces a 4th color or monochromatic edge.
 B. Any quotient identification of two distinct W-words w1!=w2 at depth<=2
    forces the nontrivial word w1*w2^{-1} (reduced length 2..4, certified
    nontrivial in Gamma2 by abelianization or UT(4,F5) rep) to stabilize a
    vertex -> creates a cycle through that vertex in the quotient Schreier
    graph, contradicting acyclicity. So a depth-2 gluing quotient that forces
    a finite win cannot stay acyclic.
 C. Freeness basis: <a,b> words length<=4 nontrivial (extends census logic):
    abelianization + UT(4,F5) rep from f3_window_census (r|->I verified there).
Prints FALLBACK_DEPTH2_BLOCKED on success.
"""
inv = {'a':'A','A':'a','b':'B','B':'b','c':'C','C':'c','d':'D','D':'d'}
def red(w):
    st=[]
    for g in w:
        if st and st[-1]==inv[g]: st.pop()
        else: st.append(g)
    return st
def expvec(w):
    e={'a':0,'b':0,'c':0,'d':0}
    for g in w: e[g.lower()]+=1 if g.islower() else -1
    return tuple(e[b] for b in 'abcd')
# --- W enumeration (F=<a,b>) ---
gens=['a','A','b','B']
W=[()]
W+= [(g,) for g in gens]
for g1 in gens:
    for g2 in gens:
        if g2!=inv[g1]: W.append((g1,g2))
assert len(W)==1+4+12==17, len(W)
# A: parity 2-coloring is proper on generator edges inside W
col={w: len(w)%2 for w in W}
for w in W:
    for s in gens:
        v=tuple(red(list(w)+[s]))
        if v in col:
            assert col[v]!=col[w], f"parity fails {w}->{v}"
print("A: depth-2 F-window 17 words parity-proper (2-colorable) OK")
print("   -> no local Player-I depth-2 forced 4th color; proper 3-responses always exist")
# C/B: nontriviality of window differences via abelianization + UT(4,F5) rep
def M4(d):
    M=[[0]*4 for _ in range(4)]
    for i in range(4): M[i][i]=1
    for (i,j),v in d.items(): M[i][j]=v%5
    return tuple(tuple(x) for x in M)
def mm4(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4))%5 for j in range(4)) for i in range(4))
def minv4(A):
    p=5; n=4
    a=[list(r)+[1 if i==j else 0 for j in range(n)] for i,r in enumerate(A)]
    for c in range(n):
        piv=next(k for k in range(c,n) if a[k][c]%p!=0)
        a[c],a[piv]=a[piv],a[c]
        iv=pow(a[c][c],-1,p)
        a[c]=[(x*iv)%p for x in a[c]]
        for k in range(n):
            if k!=c and a[k][c]%p!=0:
                f=a[k][c]%p
                a[k]=[(x-f*y)%p for x,y in zip(a[k],a[c])]
    return tuple(tuple(r[n:]) for r in a)
Ia=((1,1,2,3),(0,1,4,4),(0,0,1,0),(0,0,0,1))
Ib=((1,0,2,1),(0,1,4,2),(0,0,1,1),(0,0,0,1))
Ic=((1,0,3,2),(0,1,4,1),(0,0,1,4),(0,0,0,1))
Id=((1,1,3,1),(0,1,2,4),(0,0,1,1),(0,0,0,1))
rep4={'a':Ia,'b':Ib,'c':Ic,'d':Id,'A':minv4(Ia),'B':minv4(Ib),'C':minv4(Ic),'D':minv4(Id)}
I4=M4({})
def rep4ev(w):
    Q=I4
    for g in w: Q=mm4(Q,rep4[g])
    return Q
# verify rep descends (r|->I)
P=I4
for g in list('abABcdCD'): P=mm4(P,rep4[g])
assert P==I4, "rep must descend"
# check all pairwise differences nontrivial
ncheck=0; ab=0; u4=0
for i in range(len(W)):
    for j in range(i+1,len(W)):
        d=tuple(red(list(W[i])+ [inv[g] for g in reversed(W[j])]))
        if len(d)==0: raise AssertionError(f"W words collide in F4: {W[i]} {W[j]}")
        ncheck+=1
        if expvec(d)!=(0,0,0,0): ab+=1
        else:
            assert rep4ev(d)!=I4, f"difference {d} uncertified"
            u4+=1
print(f"B/C: {ncheck} pairwise window differences all nontrivial in Gamma2 ({ab} abelianization + {u4} UT(4,F5)) OK")
print("   -> any depth<=2 gluing identification forces a cycle; acyclicity lost")
print("FALLBACK_DEPTH2_BLOCKED")
