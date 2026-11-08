"""Exact arithmetic checks for hyper-m-ary partition parity count theorem."""

def h_array(m,N):
    arr=[0]*N
    if N:arr[0]=1
    for n in range(1,N):
        q,r=divmod(n,m)
        arr[n]=(arr[q]+(arr[q-1] if q else 0)) if r==0 else arr[q]
    return arr

def via_recurrence(m,K):
    H=[1,m]
    for k in range(1,K):
        H.append((m-1)*H[-1]+2*H[-2]-1)
    return H[:K+1]

def via_three_states(m,K):
    # Counts of parity states (s(n),s(n+1)) for 0<=n<m**k.
    v=[1,0,0]
    out=[1]
    for k in range(1,K+1):
        x,y,z=v
        v=[x+z,y+z,(m-1)*x+y+(m-2)*z]
        out.append(v[1]+v[2]+1)
    return out

def main():
    checked=0
    for m in range(2,12):
        K=0
        while m**(K+1)<=175000:K+=1
        A=via_recurrence(m,K)
        B=via_three_states(m,K)
        assert A==B,(m,A,B)
        arr=h_array(m,m**K)
        for k in range(K+1):
            cnt=sum(v&1 for v in arr[:m**k])
            assert cnt==A[k],(m,k,cnt,A[k]);checked+=m**k
        for k in range(1,K+1):
            assert A[k]>=A[k-1]
    # independent generating-function coefficient checks (no floating-point)
    for m in range(2,20):
        H=via_recurrence(m,22)
        # denominator=(1-z)(1-(m-1)z-2z^2)=1-mz+(m-3)z^2+2z^3
        for k in range(22):
            rhs=H[k]-m*(H[k-1] if k>=1 else 0)+(m-3)*(H[k-2] if k>=2 else 0)+2*(H[k-3] if k>=3 else 0)
            assert rhs==(1 if k==0 else -2 if k==2 else 0),(m,k,rhs)
    # Known binary congruence comparison
    arr=h_array(2,65536)
    assert all((v&1)==int(i%3!=2) for i,v in enumerate(arr))
    print('VERIFY_OK', 'bases=2..11', 'recurrence+state+direct_checked_terms',checked, 'generating_function_bases=2..19','binary_residue_test=65536')

if __name__=='__main__':main()
