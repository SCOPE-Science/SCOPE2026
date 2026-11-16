"""Independent exact Walsh and transfer checks for two-row order-ideal convolution."""
from collections import defaultdict, Counter
from math import comb

def direct_fourier(n):
    d = 1 << (2*n)
    arr = [0]*d
    for a in range(n+1):
        for b in range(a+1):
            mask = ((1<<a)-1) | (((1<<b)-1)<<n)
            arr[mask] = 1
    for block in [1<<j for j in range(2*n)]:
        for base in range(0,d,2*block):
            for k in range(base,base+block):
                x,y = arr[k],arr[k+block]
                arr[k],arr[k+block] = x+y,x-y
    return Counter(arr)

def transfer(n):
    states={(1,1):1}
    for _ in range(n):
        nx=defaultdict(int)
        for (p,w),mult in states.items():
            for delta in (-1,1):
                q=p+delta
                nx[q,w+q] += mult
                nx[q,w-q] += mult
        states=nx
    hist=Counter()
    for (_,w),v in states.items():
        hist[w]+=v
    return hist

def main():
    total=0
    for n in range(1,9):
        brute=direct_fourier(n)
        dyn=transfer(n)
        assert brute==dyn,(n,"spectra mismatch")
        assert sum(brute.values())==4**n
        assert max(abs(k) for k in brute)==comb(n+2,2)
        zeros=brute[0]
        assert (zeros==0)==(n%4 in (0,1)),(n,zeros)
        least=min(abs(k) for k in brute if k)
        assert least==(1 if n%4 in (0,1) else 2),(n,least)
        print(f'n={n} total_frequencies={4**n} zeros={zeros} minimum_nonzero={least}')
        total+=4**n
    for n in range(9,18):
        spec=transfer(n)
        least=min(abs(k) for k in spec if k)
        assert least==(1 if n%4 in (0,1) else 2)
        assert (spec[0]==0)==(n%4 in (0,1))
        assert sum(spec.values())==4**n
    print(f'TWO_ROW_ORDER_IDEAL_FOURIER_PASS total_direct_frequencies={total}')
if __name__=='__main__':main()
