"""Independent direct semantics on the explicit all-depth path witnesses."""
def apply_delta(v):
    n=len(v)
    return [int(i==0 or i==n-1 or v[i-1]==v[i+1]) for i in range(n)]
for d in range(1,101):
    n=d+2
    zero=[0]*n
    defect=zero.copy();defect[-1]=1
    a,b=zero,defect
    for _ in range(d):
        a=apply_delta(a); b=apply_delta(b)
    assert a[1]==1 and b[1]==0,(d,a[1],b[1])
    # The two initial valuations agree on the whole radius-(d-1)
    # neighborhood of the pointed vertex 1.
    assert all(zero[j]==defect[j] for j in range(n) if abs(j-1)<d)
print('HIERARCHY_OK: d=1..100')
