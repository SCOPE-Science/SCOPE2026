"""Exact stdlib-only verifier for lane-238 fallback witnesses. Usage: python3 verify.py"""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
def bareiss(A):
    n=len(A); B=[row[:] for row in A]; d=1; prev=1
    for k in range(n-1):
        if B[k][k]==0:
            piv=None
            for i in range(k+1,n):
                if B[i][k]!=0: B[k],B[i]=B[i],B[k]; d=-d; piv=i; break
            if piv is None: return 0
        for i in range(k+1,n):
            Bk=B[k]; Bi=B[i]
            for j in range(k+1,n):
                Bi[j]=(Bi[j]*Bk[k]-Bi[k]*Bk[j])//prev
            Bi[k]=0
        prev=B[k][k]
        if prev==0: return 0
    return d*B[n-1][n-1]
def load(p):
    rows=open(os.path.join(HERE,p)).read().split()
    return [[1 if c=='+' else -1 for c in r] for r in rows], rows
def gram(M):
    n=len(M); return [[sum(M[i][k]*M[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
def check(path, det_expected, thresh, thresh_name, strict=True):
    M,rows=load(path); n=len(M)
    assert all(len(r)==n and set(r)<=set('+-') for r in rows), "entries must be +-1 square"
    D=abs(bareiss(M))
    G=gram(M)
    assert all(G[i][i]==n for i in range(n)), "Gram diagonal must equal n"
    assert D==det_expected, f"determinant mismatch {D} != {det_expected}"
    if strict:
        assert D>thresh, f"threshold failed {D} <= {thresh}"
    else:
        assert D==thresh, f"replay mismatch {D} != {thresh}"
    rs=[sum(M[i]) for i in range(n)]
    off=max(abs(G[i][j]) for i in range(n) for j in range(n) if i!=j)
    print(f"{path}: n={n} D={D} > {thresh_name}={thresh} OK; excess={sum(rs)} max|Goff|={off}")
    return {"n":n,"D":D,"excess":sum(rs),"row_sums":rs,"max_offdiag":off}
R29=(2**28)*(7**12)*320; K29=(2**28)*(7**13)*43
D33=(2**32)*(8**14)*441; FK33=(2**32)*(8**15)*51
B29=(2**28)*(7**14)*math.sqrt(57)
out={}
out['posted_n29']=check('posted_n29.txt',R29,R29,"R29(replay)",strict=False)
out['W29']=check('W29.txt',R29,K29,"K29")
out['W29b']=check('W29b.txt',1166133779202284978176,K29,"K29")
out['posted_n33']=check('posted_n33.txt',D33,FK33,"FK33")
out['W33']=check('W33.txt',D33,FK33,"FK33")
out['W33b']=check('W33b.txt',7744681031906218150461440,FK33,"FK33")
out['ratios']={"R29/Barba29":R29/B29,"K29/Barba29":K29/B29,"R29/K29":R29/K29,
 "D33/FK33":D33/FK33,"W33b/FK33":7744681031906218150461440/FK33}
json.dump(out,open(os.path.join(HERE,'results.json'),'w'),indent=1)
print("ALL CHECKS PASSED")
