#!/usr/bin/env python3
"""Check finite instances of a general interval-count theorem for binary blocks.

The proof is symbolic; this tests independent direct-string and bit-window
implementations on all words and all needed summation ranges through length 10.
"""
def direct_count(v, h, t):
    word = format(v, f"0{h}b")
    digits = format(t, "b")
    return sum(digits[i:i + h] == word for i in range(len(digits) - h + 1))

def window_count(v, h, t):
    mask = (1 << h) - 1
    count = 0
    while t:
        count += ((t & mask) == v)
        t >>= 1
    return count

def check():
    total = 0
    for h in range(3, 11):
        H = 1 << h
        for v in range(H//2 + 1, H - 1):
            m, n = v + 1, H + v + 1
            running = 0
            vals = {}
            for t in range(m + n):
                a, b = direct_count(v, h, t), window_count(v, h, t)
                assert a == b, (h, v, t, a, b)
                running += a
                if t + 1 in (m, n, m + n):
                    vals[t + 1] = running
            assert (vals[m], vals[n], running) == (1, 4, 4), (h, v, vals, running)
            total += 1
    print(f"Checked {total} strict-interior patterns, lengths 3..10")
    print("PASS all nonextremal words of lengths 3..10")

if __name__ == "__main__":
    check()
