"""Exact integer PSD certificate for 3.44*I +/- A (U=86/25), via fraction-free Bareiss LDL.

For M1 = U I - A (resp. M2 = U I + A) with U=86/25, scaled integer matrix
M' = 86 I -/+ 25 A has the same definiteness. Bareiss elimination keeps all
arithmetic in exact integers (no rounding); all 60 leading-principal-pivot
values are positive integers  =>  M' (hence M) is positive definite by
Sylvester's criterion  =>  all eigenvalues of A lie strictly inside (-U, U).

Runtime ~1-2 min (pure Python big-int elimination on 60x60). Prints VERIFY_OK.
"""
import csv, os
def load():
    p=os.path.join(os.path.dirname(__file__),"A_eps_star.csv")
    return [[int(x) for x in row] for row in csv.reader(open(p))]
def make(A,sgn):
    n=len(A)
    return [[(86-sgn*25*A[i][j]) if i==j else (-sgn*25*A[i][j]) for j in range(len(A))] for i in range(len(A))]
def bareiss_psd(M):
    n=len(M); B=[row[:] for row in M]; prev=1; pivs=[]
    for k in range(n):
        piv=B[k][k]; pivs.append(piv)
        if piv<=0: return False,k,piv,pivs
        if k==n-1: break
        for i in range(k+1,n):
            Bik=B[i][k]
            if Bik:
                Bi=B[i]; Bk=B[k]
                for j in range(k+1,n): Bi[j]=(Bi[j]*piv-Bik*Bk[j])//prev
            else:
                Bi=B[i]
                for j in range(k+1,n): Bi[j]=(Bi[j]*piv)//prev
        prev=piv
        for i in range(k+1,n): B[i][k]=0
    return True,None,None,pivs
def main():
    A=load(); n=len(A)
    assert n==60
    for sgn,name in [(1,"U-A"),(-1,"U+A")]:
        ok,k,piv,pivs=bareiss_psd(make(A,sgn))
        print(name,"PSD:",ok,"min_pivot:",min(pivs) if ok else f"FAIL@{k}={piv}")
        assert ok
    print("CERTIFY_UPPER_OK: 3.44I+/-A exact PSD => rho < 3.44")
main()
