"""Independent integer DP and small-word enumeration for a pinned cycle."""
from itertools import product
from collections import defaultdict

def local_dp(L):
    total=good=0
    for first in range(3):
        dp={(first,first%3):1}
        for _ in range(1,L):
            nx=defaultdict(int)
            for (prev,residue),ways in dp.items():
                for diff in range(3):
                    if prev==2 or diff==1:
                        nx[(diff,(residue+diff)%3)]+=ways
            dp=nx
        for (last,residue),ways in dp.items():
            if residue==0:
                total+=ways
                if first==1 or last==2:good+=ways
    return total,good

def local_naive(L):
    b=a=0
    for word in product(range(3),repeat=L-1):
        colors=(0,)+word
        if all((colors[(i-1)%L]==(colors[i]+1)%3 or
                colors[(i+1)%L]==(colors[i]+1)%3)
               for i in range(1,L)):
            b+=1
            if colors[1]==1 or colors[-1]==1:a+=1
    return b,a

for L in range(3,101):
    observed=local_dp(L)
    expected=(2*(L//3)+1,2 if L%3==0 else 0)
    assert observed==expected,(L,observed,expected)
    if L<=11:assert local_naive(L)==expected,(L,local_naive(L),expected)
    if L<=12: print('PASS cycle length',L,'(total,support)=',observed)
print('PASS lengths_3_through_100=98; direct_pinned_color_enumeration_lengths_3_through_11=9')
