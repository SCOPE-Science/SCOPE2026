"""Independent microscopic state enumeration for mixed-threshold 3-state excitation."""
from itertools import product
from collections import Counter
from math import factorial
from verify_profiles import count_by_first_entry

def advance(state,m):
    left=state[:m];right=state[m:]
    excited_left=left.count(1);excited_right=right.count(1)
    return tuple(((2 if c==1 else 0) if c else (1 if excited_right>=1 else 0)) for c in left) + tuple(
        ((2 if c==1 else 0) if c else (1 if excited_left>=2 else 0)) for c in right)

def first_repeat(state,m):
    prior={}
    for t in range(14):
        if state in prior:return prior[state],t-prior[state]
        prior[state]=t
        state=advance(state,m)
    raise AssertionError('late recurrence')

def large_onto(m):
    return sum(factorial(m)//(factorial(i)*factorial(j)*factorial(m-i-j))
               for i in range(2,m+1) for j in range(2,m-i+1) if m-i-j>=2)

def split_large(m):
    return sum(factorial(m)//(factorial(i)*factorial(m-i)) for i in range(2,m-1))

def run():
    total=0
    for m,n in [(1,1),(1,4),(2,2),(3,2),(3,3),(4,2),(4,3),(5,3),(6,3),(6,4)]:
        h=Counter(first_repeat(s,m) for s in product(range(3), repeat=m+n))
        total+=3**(m+n)
        assert sum(h.values())==3**(m+n)
        assert h==count_by_first_entry(m,n), (m,n,'full transient-period mismatch')
        assert max(t for t,p in h)<=5
        assert all(p in [1,3,4] for t,p in h)
        assert h[(0,1)]==1
        assert h[(0,3)]==large_onto(m)*(3**n-3*(2**n)+3)
        assert h[(0,4)]==2*split_large(m)*(2**n-2)
        assert (max(t for t,p in h)==5)==(m>=3 and n>=2)
        print(m,n,'period3_states',h[(0,3)],'period4_states',h[(0,4)],'max_entry',max(t for t,p in h))
    print('TOTAL_MICROSTATES',total)
    print('PASS')

if __name__=='__main__':run()
