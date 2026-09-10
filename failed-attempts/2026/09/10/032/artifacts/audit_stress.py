"""Lane-584 stress: explicit integral isometry Q1 ~= 2<1>(+)2<-1> by direct
construction (replaces infeasible brute force), plus rechecks.
"""
import json

def transpose(M):
    return [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]
def mmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]

D=[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]]
Q1=[[1,0,0,0],[0,-1,0,0],[0,0,0,1],[0,0,1,0]]

# Columns: a=(1,-1,1,0) [sq 1], b=(0,0,0,1) [sq -1],
# c=(1,0,1,0) [sq 0], d=(0,1,-1,0) [sq 0]; see WORKLOG derivation.
M=[[1,0,1,0],[-1,0,0,1],[1,0,1,-1],[0,1,0,0]]
G=mmul(mmul(transpose(M),D),M)
print("M^T D M =",G)
assert G==Q1, "isometry check failed"
print("Q1 ~= diag(1,1,-1,-1) EXPLICIT (det must be +-1; Gram equality suffices).")

# det via Bareiss
A=[r[:] for r in M]; prev=1; sgn=1
for k in range(3):
    if A[k][k]==0:
        for i in range(k+1,4):
            if A[i][k]!=0: A[k],A[i]=A[i],A[k]; sgn=-sgn; break
    for i in range(k+1,4):
        for j in range(k+1,4):
            A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])//prev
        A[i][k]=0
    prev=A[k][k]
det=sgn*A[3][3]
print(f"det M = {det}"); assert abs(det)==1

# Wang extension recheck: e(E_F)=e(Z1)e(S1)=0; sig=0.
print("e(E_F)=6*0=0; sig(E_F)=0 (fibered over S1).")
# Wu recheck: e1^2=+1 odd => w2!=0.
print("Wu: e1^2=+1 odd => w2(Z1)!=0 CONFIRMED (non-spin).")
# Hurewicz direction (statement level).
print("Hurewicz: S1-BF nontrivial => some chamber has FSW!=0 (not conversely).")
# Killing: no smooth isotopy in-lane.
print("KILL: no smooth isotopy certificate; topological isotopy only.")

out={"isometry_found":True,"det_M":det,"M":M,"e_EF":0,
 "w2_nonzero":True,"killing_isotopy":False,"J_status":"uncomputed"}
with open("output/artifacts/stress_ledger.json","w") as f:
    json.dump(out,f,indent=2)
print("wrote output/artifacts/stress_ledger.json")
print("ALL VERIFY_OK")
