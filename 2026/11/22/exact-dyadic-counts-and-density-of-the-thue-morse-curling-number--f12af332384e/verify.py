#!/usr/bin/env python3
"""Independent finite checks of the stated Thue--Morse curling-number theorem.
No finite check is used as a substitute for the all-index proof.
"""

def direct(n, word):
    length = n + 1
    return 2 if any(word[length-2*p:length-p] == word[length-p:length]
                    for p in range(1, length//2 + 1)) else 1

def main():
    limit = 1 << 20
    t = bytes(i.bit_count() & 1 for i in range(limit))
    present = bytearray(limit)
    # Pansiot-Brlek finite-square decomposition gives an exact all-index recursion.
    for n in range(limit):
        if n & 1:
            present[n] = present[n // 2]
        elif n >= 2:
            m = n // 2
            small = t[m] != t[m - 1]
            length_six = m >= 3 and t[m-3:m+1] in (
                b'\x00\x00\x01\x01', b'\x01\x01\x00\x00')
            assert not (small and length_six), (n, m)
            present[n] = int(small or length_six)
    for n in range(2048):
        assert 1 + present[n] == direct(n, t), ('independent square-suffix check', n)
    print('PASS independent all-period square-suffix checks for every prefix length 1..2048')
    observed = [1] + [1 + present[i] for i in range(31)]
    reference = [int(ch) for ch in '11121122121221221222122222122122']
    assert observed == reference, ('published 2007 first 32 entries', observed, reference)
    print('PASS first 32 published curling-transform entries, including historical initial term')
    c = 0
    q = 0
    j = 0
    for n in range(limit):
        c += int(not present[n])
        q += int(n >= 1 and t[n] == t[n-1])
        j += int(n >= 3 and t[n-3:n+1] in (b"\x00\x00\x01\x01", b"\x01\x01\x00\x00"))
        if n + 1 >= 4 and (n + 1) & n == 0:
            r = (n + 1).bit_length() - 1
            expected = ((1 << r) + 9*r - 4 - (r & 1)) // 6
            assert 6*c == (1 << r) + 9*r - 4 - (r & 1), (r,c,expected)
            assert 3*q == (1<<r) - (1 if r%2 == 0 else 2), ("adjacent-pair count",r,q)
            s = r-2
            qprev = ((1<<s) - (1 if s%2 == 0 else 2))//3
            assert j == 2*qprev, ("fourgram count",r,j,qprev)
            print(f'r={r:2d}; N={1<<r:7d}; ones={c:7d}; exact={expected:7d}; PASS')
    print('PASS dyadic exact counts and both intermediate factor-count lemmas r=2..20')
    print('PASS sample proportion at N=1048576:',f'{c/limit:.12f}', 'target=0.166666666667')

if __name__ == '__main__':
    main()
