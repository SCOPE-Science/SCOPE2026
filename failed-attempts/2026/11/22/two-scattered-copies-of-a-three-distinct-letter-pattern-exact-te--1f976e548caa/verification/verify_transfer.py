"""Exact transfer of capped subsequence counters against a rational GF recurrence."""
from collections import defaultdict

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def main():
    # Denominator (1-z)^3(1-2z)^2
    Q=multiply(multiply([1,-1],[1,-1]),[1,-1]); Q=multiply(Q,[1,-2]);Q=multiply(Q,[1,-2])
    N=[0,0,0,0,3,-1]
    expected=[]
    states={(0,0,0):1}
    for n in range(51):
        exact=sum(v for (x,y,c),v in states.items() if c==2)
        by_recurrence=(N[n] if n<len(N) else 0)-sum(Q[j]*expected[n-j] for j in range(1,min(n,len(Q)-1)+1))
        assert exact==by_recurrence,(n,exact,by_recurrence)
        expected.append(exact)
        nxt=defaultdict(int)
        for (x,y,c),count in states.items():
            nxt[(min(x+1,3),y,c)]+=count
            nxt[(x,min(y+x,3),c)]+=count
            if c+y<=2:nxt[(x,y,c+y)]+=count
        states=nxt
    print('Q=',Q)
    print('n=0..15',expected[:16]);print('n=50',expected[50]);print('TRANSFER_OK')
if __name__=='__main__':main()
