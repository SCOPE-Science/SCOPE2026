#!/usr/bin/env python3
"""Independent finite residue census for a pair of generalized-Fermat moduli.

Usage: python verify.py
Pure Python standard library, no external inputs. This is corroboration,
not a machine proof of the infinite theorem.
"""
from math import gcd

def min_residue(b, c, d):
    mod=(b**c+1)*(b**d+1)
    assert gcd(b,mod)==1
    vals=[]
    for n in range(1, 2*d+1):
        residue=(-pow(pow(b,n,mod),-1,mod)) % mod
        vals.append(residue or mod)
    return min(vals),vals

def main():
    tested=0
    for b in range(2, 22, 2):
        for c in range(1,7):
            for h in range(2,11,2):
                d=c*h
                if d>60: continue
                predicted=b**d+b**c+1
                least,residues=min_residue(b,c,d)
                assert least==predicted,(b,c,d,least,predicted)
                assert residues[d-c-1]==predicted,(b,c,d)
                assert ((predicted*pow(b,d-c,(b**c+1)*(b**d+1))+1)
                        %((b**c+1)*(b**d+1)))==0
                tested+=1
    # Separate direct k/n test for a bounded family rather than relying on
    # modular-inverse minimization alone.
    direct=0
    for b in (2,4,6,8):
        for c in (1,2,3):
            for h in (2,4):
                d=c*h
                predicted=b**d+b**c+1
                if d>9 or predicted>100_000:continue
                mod=(b**c+1)*(b**d+1)
                assert all((k*pow(b,n,mod)+1)%mod != 0
                           for k in range(1,predicted)
                           for n in range(1,2*d+1))
                assert (predicted*pow(b,d-c,mod)+1)%mod == 0
                direct+=1
    print(f'PASS: {tested} complete exponent-orbit checks; {direct} direct small-case censuses')

if __name__=='__main__':
    main()
