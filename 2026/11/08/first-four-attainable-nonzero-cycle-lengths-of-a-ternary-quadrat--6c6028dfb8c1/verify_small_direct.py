"""Independent direct ternary-word check for all periods n <= 11.
No assumptions from the binary-mask certificate are used.
"""
from itertools import product
EXPECTED = {(4,2):1,(4,3):1,(9,4):3,(9,6):3}
for n in range(1,12):
    for k in range(n):
        count = 0
        for word in product(range(3),repeat=n):
            if word[-1]!=0 or all(z==0 for z in word):
                continue
            if any(word[j]!=(word[(j-1)%n]+word[(j-k)%n]**2)%3
                   for j in range(n)):
                continue
            if any(all(word[j]==word[(j+d)%n] for j in range(n))
                   for d in range(1,n) if n%d==0):
                continue
            count += 1
        assert count==EXPECTED.get((n,k),0),(n,k,count)
print('INDEPENDENT_DIRECT_OK periods=1..11 all_lags exact_enumeration=yes')
