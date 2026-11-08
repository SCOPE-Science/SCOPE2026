#!/usr/bin/env python3
"""Exact residue checks for the rank-four balancing prime and power sums."""
MOD=17
max_exp=96
max_length=400
B=[0,1]
for _ in range(2,16):
    B.append((6*B[-1]-B[-2])%MOD)
assert B[:9]==[0,1,6,1,0,16,11,16,0]
assert pow(6,8,17)==16 and pow(6,16,17)==1
checked=0
for exponent in range(1,max_exp+1):
    word=[pow(B[i],exponent,MOD) for i in range(8)]
    for length in range(1,max_length+1):
        # The gcd of all integer windows is divisible by 17 iff every residue window vanishes.
        direct=all(sum(word[(start+j)%8] for j in range(length))%17==0 for start in range(8))
        if exponent%2:
            predicted=(length%8==0)
        else:
            predicted=(length%4==0 and ((length//4)%17==0 or exponent%16==10))
        assert direct==predicted,(exponent,length,direct,predicted)
        checked+=1
print(f'CHECK_OK: {checked} exponent-length cases, 8 cyclic starts per case; exact modular recurrence and phase law.')
