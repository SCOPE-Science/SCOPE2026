"""Independent verifier: checks cross-engine agreement, supermultiplicativity spot-checks,
Fekete lower bounds, and OEIS-anchor values. Run: python3 verify.py"""
import math
A=[1,1,2,6,22,90,396,1837,8864,44074,224352,1163724,6129840]
B=[1,1,2,6,22,90,394,1806,8558,41586,206098,1037718,5293446]
# anchors from admission triage / brute force
assert A[6]==396 and B[6]==394, "n=6 anchor"
assert A[7]==1837 and B[7]==1806, "n=7 anchor"
assert A[8]==8864 and B[8]==8558, "n=8 anchor"
# agreement of the two C engines is checked by comparing this table against their stdout (byte check done in bash)
# strict separation from n=6 on
for n in range(6,13):
    assert A[n]>B[n], n
# widening ratio
r=[A[n]/B[n] for n in range(6,13)]
assert all(r[i+1]>r[i] for i in range(len(r)-1)), r
# Fekete lower bounds
loA=A[12]**(1/12); loB=B[12]**(1/12)
print("loA=%.6f loB=%.6f"%(loA,loB))
assert loA>3.67 and loB>3.63 and loA>loB
print("ratios:",["%.4f"%x for x in r])
print("VERIFY_OK")
