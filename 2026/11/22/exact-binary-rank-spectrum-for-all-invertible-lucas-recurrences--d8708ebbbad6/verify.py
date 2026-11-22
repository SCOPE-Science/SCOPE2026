"""Exact modular-rank census via direct recurrence; no external dependencies."""
from collections import Counter

def observed(a):
    m=1<<a
    counts=Counter()
    for P in range(m):
        for Q in range(1,m,2):
            x,y=0,1
            for n in range(1,3*m+2):
                x,y=y,(P*y-Q*x)%m
                if x==0:
                    counts[n]+=1
                    break
            else:
                raise AssertionError((a,P,Q,'no zero'))
    return counts

def predicted(a):
    c=Counter()
    c[2]=1<<(a-1)
    for j in range(2,a+1):
        c[1<<j]=1<<(a+j-3)
    if a==1:
        c[3]=1
    elif a==2:
        c[3]=2
        c[6]=2
    else:
        c[3]=1<<(a-1)
        c[6]=3*(1<<(a-1))
        for j in range(2,a-1):
            c[3*(1<<j)]=1<<(a+j-1)
    return c

def main():
    checked=0
    for a in range(1,9):
        got,expected=observed(a),predicted(a)
        assert got==expected,(a,got,expected)
        assert sum(got.values())==1<<(2*a-1)
        checked+=1<<(2*a-1)
    print(f'VERIFY_OK moduli=8 parameter_pairs={checked}')
if __name__=='__main__':main()
