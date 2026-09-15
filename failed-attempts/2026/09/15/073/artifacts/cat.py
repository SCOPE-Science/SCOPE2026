from fractions import Fraction
import itertools

def mons(nvars,deg):
    res=[]
    for e in itertools.product(range(deg+1),repeat=nvars):
        if sum(e)==deg: res.append(e)
    return sorted(res)

def poly_diff_coeffs(F, a):
    # F dict exp->Fraction; differentiate a times
    G=dict(F)
    for vi,ee in enumerate(a):
        for _ in range(ee):
            NG={}
            for e,c in G.items():
                if e[vi]>0:
                    ne=list(e); ne[vi]-=1; ne=tuple(ne)
                    NG[ne]=NG.get(ne,Fraction(0))+c*e[vi]
            G=NG
    return G

def rank_mat(M):
    # M list of lists of Fraction; gaussian elimination
    if not M or not M[0]: return 0
    R=[row[:] for row in M]
    m=len(R); n=len(R[0]); r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if R[i][c]!=0: piv=i; break
        if piv is None: continue
        R[r],R[piv]=R[piv],R[r]
        inv=R[r][c]
        # normalize not needed
        for i in range(m):
            if i!=r and R[i][c]!=0:
                f=R[i][c]/inv
                for j in range(c,n):
                    R[i][j]-=f*R[r][j]
        r+=1
        if r==m: break
    return r

def cat_rank(F,d,i):
    src=mons(4,i); tgt=mons(4,d-i)
    tindex={b:j for j,b in enumerate(tgt)}
    M=[]
    for a in src:
        G=poly_diff_coeffs(F,a)
        row=[Fraction(0)]*len(tgt)
        for e,c in G.items():
            if sum(e)==d-i and e in tindex:
                row[tindex[e]]=c
        M.append(row)
    return rank_mat(M)

def hvec(F,d):
    return [cat_rank(F,d,i) for i in range(d+1)]

def E(*e): return tuple(e)
# test generic compressed d=5
F=dict()
import random
random.seed(0)
# F = sum of 11 random 5th powers? generic rank 10 in middle. Let's just take Fermat + mixed
def pw(form, p):
    # form: dict exp deg1 -> coeff; compute form^p via expansion
    from collections import defaultdict
    cur={(0,0,0,0):Fraction(1)}
    for _ in range(p):
        nxt=defaultdict(Fraction)
        for e1,c1 in cur.items():
            for e2,c2 in form.items():
                ne=tuple(e1[k]+e2[k] for k in range(4))
                nxt[ne]+=c1*c2
        cur=dict(nxt)
    return cur
def lin(a,b,c,dd):
    return {(1,0,0,0):Fraction(a),(0,1,0,0):Fraction(b),(0,0,1,0):Fraction(c),(0,0,0,1):Fraction(dd)}
def add(*Fs):
    from collections import defaultdict
    r=defaultdict(Fraction)
    for F in Fs:
        for e,c in F.items(): r[e]+=c
    return dict(r)

F2=add(pw(lin(1,0,0,0),5),pw(lin(0,1,0,0),5),pw(lin(0,0,1,0),5),pw(lin(0,0,0,1),5),pw(lin(1,1,1,1),5),pw(lin(1,2,3,4),5))
print("F2 h",hvec(F2,5))
