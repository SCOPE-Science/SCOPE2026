#!/usr/bin/env python3
"""Exact checks for transitive-triangle-free one-point types on oriented paths.
No external modules are needed.
"""
from itertools import product

# 0: no edge; 1: new point -> old point; 2: old point -> new point
BLOCK_FORWARD={(1,1),(2,2),(2,1)}
BLOCK_BACKWARD={(1,1),(2,2),(1,2)}

def transfer(bits):
    v=(1,1,1)
    for direction in bits:
        s=sum(v)
        v=(s,v[0],v[0]+v[1]) if direction==0 else (s,v[0]+v[2],v[0])
    return sum(v)

def brute(bits):
    n=len(bits)+1
    ans=0
    for t in product((0,1,2),repeat=n):
        if all((t[i],t[i+1]) not in (BLOCK_FORWARD if d==0 else BLOCK_BACKWARD)
               for i,d in enumerate(bits)):
            ans+=1
    return ans

def from_switches(sw):
    bits=[0]
    for s in sw:bits.append(bits[-1]^s)
    return tuple(bits)

def verify():
    checks=0
    for n in range(1,9):
        for bits in product((0,1),repeat=n-1):
            assert transfer(bits)==brute(bits),(n,bits)
            checks+=1
    print('DIRECT_BRUTE_COMPARISONS',checks)
    # Verify switch-coordinate strict monotonicity, unique extrema and endpoint recurrence
    checks=0
    mn=[0,3,6,13]
    mx=[0,3,6,14]
    for n in range(4,25):
        mn.append(mn[-1]+2*mn[-2]+mn[-3])
        mx.append(2*mx[-1]+mx[-2]-mx[-3])
    for n in range(3,15):
        vals={sw:transfer(from_switches(sw)) for sw in product((0,1),repeat=n-2)}
        assert min(vals.values())==mn[n] and max(vals.values())==mx[n],n
        assert set(s for s,v in vals.items() if v==mn[n])=={(0,)*(n-2)}
        assert set(s for s,v in vals.items() if v==mx[n])=={(1,)*(n-2)}
        for s,actual in vals.items():
            for i in range(n-2):
                if s[i]==0:
                    t=s[:i]+(1,)+s[i+1:]
                    assert vals[t]>actual,(n,s,t,actual,vals[t])
                    checks+=1
    print('SWITCH_MONOTONICITY_COMPARISONS',checks)
    print('EXACT_ENDPOINT_COUNTS')
    for n in range(1,15):print(n,mn[n],mx[n])
    # verify strict cut-factor for all patterns through 11 vertices, including both bridge directions
    cuts=0
    for n in range(3,12):
        for sw in product((0,1),repeat=n-2):
            for j in range(n-2):
                if sw[j]!=0:continue
                bits=from_switches(sw)
                left_bits=bits[:j+1]
                right_bits=bits[j+2:]
                # prefix ending at vertex j+1, suffix beginning j+2
                left=(1,1,1)
                for d in left_bits:
                    s=sum(left)
                    left=(s,left[0],left[0]+left[1]) if d==0 else (s,left[0]+left[2],left[0])
                # suffix root counts by brute (independent from transfer)
                rp=rm=0
                for t in product((0,1,2),repeat=n-j-2):
                    if all((t[i],t[i+1]) not in (BLOCK_FORWARD if d==0 else BLOCK_BACKWARD) for i,d in enumerate(right_bits)):
                        rp+=(t[0]==1)
                        rm+=(t[0]==2)
                left_bias=(left[2]-left[1]) if bits[j]==0 else (left[1]-left[2])
                right_factor=rm if bits[j]==0 else rp
                altered=sw[:j]+(1,)+sw[j+1:]
                assert transfer(from_switches(altered))-transfer(bits)==left_bias*right_factor,(n,j,sw)
                assert left_bias>0 and right_factor>0
                cuts+=1
    print('CUT_FACTOR_COMPARISONS',cuts)
    print('ALL_CHECKS_PASS')
if __name__=='__main__':verify()
