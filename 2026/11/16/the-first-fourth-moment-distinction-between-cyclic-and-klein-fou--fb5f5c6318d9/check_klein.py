"""Exact integer Walsh checker for onto words over the four-element Boolean group.
Run: python check_klein.py [maximum_n]. Default maximum_n=8.
"""
import itertools
import sys

def run(max_n=8):
    assert 4 <= max_n <= 9
    for n in range(4, max_n+1):
        arr = [0] * (1 << (2*n))
        # Encode each four-symbol word in consecutive two-bit slots.
        for word in itertools.product(range(4), repeat=n):
            if len(set(word)) == 4:
                index = sum(symbol << (2*i) for i, symbol in enumerate(word))
                arr[index] = 1
        onto = sum(arr)
        size = len(arr)
        # Exact fast Walsh transform, not inclusion-exclusion.
        h = 1
        while h < size:
            for start in range(0, size, 2*h):
                for j in range(h):
                    a, b = arr[start+j], arr[start+j+h]
                    arr[start+j] = a+b
                    arr[start+j+h] = a-b
            h *= 2
        zeros_balanced=0
        for k in range(size):
            freq = [(k >> (2*i)) & 3 for i in range(n)]
            xor = 0
            for v in freq: xor ^= v
            expect_zero = xor != 0 or (n%2 == 1 and all(v != 0 for v in freq))
            if (arr[k] == 0) != expect_zero:
                raise AssertionError((n,k,freq,arr[k],expect_zero))
            if xor == 0 and arr[k] == 0: zeros_balanced += 1
        expected_extra = (3**n - 3)//4 if n%2 else 0
        assert zeros_balanced == expected_extra
        assert sum(v*v for v in arr) == (4**n) * onto
        assert arr[0] == onto == 4**n-4*3**n+6*2**n-4
        print(f'Klein n={n} onto={onto} rank={sum(v!=0 for v in arr)} extra={zeros_balanced}: PASS')

if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv)>1 else 8)
