"""Direct independent state-by-state validation of sequential self-inclusive parity on triangular windmills."""
from collections import Counter

def step(x,k):
    # bit 0 is hub; bit 2i+1,2i+2 are vertices of petal i.
    h=(x&1)
    for i in range(k):
        a=(x>>(2*i+1))&1; b=(x>>(2*i+2))&1
        h ^=a^b
    y=(x&~1)|h
    for i in range(k):
        aidx=2*i+1; bidx=aidx+1
        a=(y>>aidx)&1;b=(y>>bidx)&1
        y=(y&~(1<<aidx))|((a^b^h)<<aidx)
        a=(y>>aidx)&1
        y=(y&~(1<<bidx))|((b^a^h)<<bidx)
    return y

def expected(k):
    if k%2==0:
        counts={1:2,3:(1<<(2*k-1))-2,6:3*(1<<(2*k-1))}
    else:
        counts={1:2,2:2,3:(1<<(2*k-1))-2,4:4,6:(1<<(2*k-1))-2,12:(1<<(2*k))-4}
    return {p:c for p,c in counts.items() if c}

def main():
    for k in range(1,8):
        m=1<<(2*k+1)
        predicted=expected(k)
        freq=Counter()
        for x in range(m):
            v=step(x,k);t=1
            while v!=x and t<=12:
                v=step(v,k);t+=1
            assert v==x,(k,x,t)
            freq[t]+=1
        assert dict(freq)==predicted,(k,dict(freq),predicted)
        print('k=%d states=%d periods=%s PASS'%(k,m,sorted(freq.items())))
    print('DIRECT PASS')
if __name__=='__main__':main()
