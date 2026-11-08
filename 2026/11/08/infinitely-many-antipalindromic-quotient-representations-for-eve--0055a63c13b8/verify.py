#!/usr/bin/env python3
"""Exact integer checks of explicit binary antipalindrome quotient identities."""

def value(blocks, base):
    out = 0
    for block in blocks:
        assert 0 <= block < base
        out = out * base + block
    return out


def rc(block, width):
    bits = f'{block:0{width}b}'
    return int(''.join('1' if d == '0' else '0' for d in bits[::-1]), 2)


def is_antipalindrome(n):
    bits = bin(n)[2:]
    return bits[0] == '1' and len(bits) % 2 == 0 and all(bits[i] != bits[-1-i] for i in range(len(bits)))


def check_one(r, t):
    width = 2*r
    Q = 1 << width
    b = Q - 3*(1 << (r-1))
    c = b - Q//2 + 1
    x, y = c-1, b+1
    Bblocks = [b] + [x]*t + [c] + [y]*t + [b]
    Ablocks = [b-1, Q//2] + [0]*(t-1) + [1, Q//2-1] + [Q-1]*(t-1) + [Q-2, Q-b]
    B = value(Bblocks, Q)
    A = value(Ablocks, Q)
    assert 0 < x < c < b < y < Q, (r, t, b, c, x, y)
    assert len(Bblocks) == 2*t+3
    assert len(Ablocks) == 2*t+4
    assert B*(Q-1) == A, (r,t)
    assert rc(b, width) == b and rc(c, width) == c and rc(x,width)==y
    assert rc(b-1,width) == Q-b
    assert rc(Q//2,width) == Q-2
    assert rc(0,width)==Q-1 and rc(1,width)==Q//2-1
    assert is_antipalindrome(B) and is_antipalindrome(A), (r,t)
    assert B.bit_length() == width*(2*t+3)
    assert A.bit_length() == width*(2*t+4)
    return A,B


def main():
    for r in range(2,31):
        Bprev = None
        for t in range(1,21):
            A,B = check_one(r,t)
            if Bprev is not None: assert B > Bprev
            Bprev = B
    print('PASS: 580 exact quotient identities, 580 antipalindrome pairs, and 580 length checks (2<=r<=30, 1<=t<=20).')
    for r,t in [(2,1),(2,2),(3,1),(4,1)]:
        A,B = check_one(r,t)
        print(f'Example r={r}, t={t}: N={4**r-1}, A={A}, B={B}, A/B={A//B}, binary lengths=({A.bit_length()},{B.bit_length()}).')
    print('Finite checks are not the infinite proof; the block identities prove every r>=2 and t>=1.')

if __name__ == '__main__':
    main()
