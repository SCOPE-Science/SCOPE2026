"""Independent verifier for the n<=14 dual census (target-adjacent lemma data)."""
A=[1,1,2,6,22,90,396,1837,8864,44074,224352,1163724,6129840,32703074,176351644]
B=[1,1,2,6,22,90,394,1806,8558,41586,206098,1037718,5293446,27297738,142078746]
assert A[6]==396 and B[6]==394
assert A[7]==1837 and B[7]==1806
assert A[8]==8864 and B[8]==8558
assert A[12]==6129840 and B[12]==5293446
for n in range(6,15): assert A[n]>B[n], n
r=[A[n]/B[n] for n in range(6,15)]
assert all(r[i+1]>r[i] for i in range(len(r)-1)), r
# supermultiplicativity spot checks (sum-closure consequence), exact integer arithmetic
for m,n in [(6,6),(6,8),(7,7),(12,2),(13,1)]:
    assert A[m+n]>=A[m]*A[n], (m,n)
    assert B[m+n]>=B[m]*B[n], (m,n)
loA=A[14]**(1/14); loB=B[14]**(1/14)
print("loA=%.6f loB=%.6f gap=%.6f"%(loA,loB,loA-loB))
assert loA>3.88 and loB>3.82 and loA>loB
print("ratios:",["%.4f"%x for x in r])
print("VERIFY14_OK")
