"""Direct finite checks of the prime-window admissibility run spectrum."""
from math import prod, isqrt

def primes_below(n):
    sieve=[True]*n
    sieve[0]=sieve[1]=False
    for i in range(2,isqrt(n-1)+1):
        if sieve[i]:
            for j in range(i*i,n,i): sieve[j]=False
    return [i for i in range(2,n) if sieve[i]]

def local_primes(k):
    return [p for p in primes_below(2*k) if p>k]

def formula(k):
    ps=local_primes(k)
    assert ps
    gap=ps[0]-k
    a=lambda r:prod(max(0,p-k-r+1) for p in ps)
    freq=[a(r)-2*a(r+1)+a(r+2) for r in range(1,gap+1)]
    return ps,gap,freq,a(1)

def verify(k):
    ps,g,freq,eligible=formula(k)
    T=prod(ps)
    state=bytearray(T)
    # Directly test every integer of a period against the original k consecutive factors.
    for n in range(T):
        state[n]=int(all(all((n-i)%p for i in range(1,k+1)) for p in ps))
    assert sum(state)==eligible,(k,'onepoint')
    counts=[0]*(g+1)
    for n in range(T):
        if state[n] and not state[(n-1)%T]:
            length=1
            while state[(n+length)%T]: length+=1
            assert length<=g
            counts[length]+=1
    assert counts[1:]==freq,(k,counts[1:],freq)
    assert sum(r*counts[r] for r in range(1,g+1))==eligible
    assert all(state[n]==state[(n+T//p)%T] for n in range(T) for p in [] )
    for p in ps:
        assert any(state[n]!=state[(n+T//p)%T] for n in range(T)),(k,'period',p)
    return T,eligible,sum(counts)

def main():
    checked=[]
    for k in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20]:
        T,eligible,nruns=verify(k)
        checked.append((k,T,eligible,nruns))
    for k in range(2,2000):
        ps,g,freq,eligible=formula(k)
        assert all(v>=0 for v in freq)
        if len(ps)==1:
            assert freq==[0]*(g-1)+[1]
        else:
            assert all(v>0 for v in freq)
        assert sum(r*freq[r-1] for r in range(1,g+1))==eligible
    print('OK: direct all-residue verification for',len(checked),'parameter values')
    print('OK: direct period sharpness, exact run counts and first moment')
    print('OK: algebraic formula checks for 1998 parameter values')
    print('Examples (k,period,admissible endpoints,nonempty maximal runs):',checked[:8])

if __name__=='__main__':main()
