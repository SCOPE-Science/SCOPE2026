"""Independent direct finite census of optimal list-four multiset codes."""
from itertools import combinations

def trace(v):
    s=0
    for i in range(3):
        if v[i]>=2:s|=1<<i
    if v[0] and v[1]:s|=1<<3
    if v[0] and v[2]:s|=1<<4
    if v[1] and v[2]:s|=1<<5
    return s

def admissible(masked):
    loads=[0]*6
    for mask in masked:
        for j in range(6):
            if mask&(1<<j):
                loads[j]+=1
                if loads[j]>4:return False
    return True

for n in (4,5):
    V=[(i,j,n-i-j) for i in range(n+1) for j in range(n+1-i)]
    t=[trace(v) for v in V]
    count=0
    for inds in combinations(range(len(V)),11):
        if admissible(t[i] for i in inds):count+=1
    expected=12*n-36
    assert count==expected,(n,count,expected)
    print('n=%d all_size_11_subsets=%d valid_11=%d'%(n,__import__('math').comb(len(V),11),count))
print('direct exhaustive census PASS')
