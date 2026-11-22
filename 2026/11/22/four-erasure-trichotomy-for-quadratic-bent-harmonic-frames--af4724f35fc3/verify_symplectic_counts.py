"""Independent exact symplectic-triple census of all 4-point masks."""
from itertools import combinations
from collections import Counter
from math import comb

def B(x,y,m):
    return sum((((x>>(2*j))&1)*((y>>(2*j+1))&1) + ((x>>(2*j+1))&1)*((y>>(2*j))&1)) for j in range(m))%2

def census(m):
    v=1<<(2*m)
    cnt=Counter()
    for t in combinations(range(v),4):
        x,u,vv,w=t
        u^=x;vv^=x;w^=x
        signs=(B(u,vv,m),B(u,w,m),B(vv,w,m))
        cls='positive' if signs==(1,1,1) else ('negative' if signs==(0,0,0) else 'mixed')
        cnt[cls]+=1
    V=1<<(2*m)
    expect={
        'positive':V**3*(V-1)//192,
        'mixed':V**2*(V-4)*(V-1)//32,
        'negative':V*(V-12)*(V-4)*(V-1)//192,
    }
    assert cnt==expect,(cnt,expect)
    assert sum(cnt.values())==comb(V,4)
    print('symplectic m=',m,'v=',V,'counts=',dict(sorted(cnt.items())))

if __name__=='__main__':
    census(2)
    census(3)
