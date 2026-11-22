"""Standalone exhaustive associativity and Veronese-condition checks in F_2, F_4.
Run with: python3 verify.py
"""
from itertools import product


def field_mul(x, y, q):
    if q == 2:
        return x & y
    out = 0
    for i in range(2):
        for j in range(2):
            if ((x >> i) & 1) and ((y >> j) & 1):
                out ^= (1 << (i + j))
    if out & 8:  # alpha^3 = 1 from alpha^2 = alpha + 1
        out ^= 0b1011
    if out & 4:
        out ^= 0b111
    return out


def check(q):
    mul = [[field_mul(x,y,q) for y in range(q)] for x in range(q)]
    # Pack extension-field coordinates with bitwise XOR as vector addition.
    b = 1 if q == 2 else 2
    mask = (1 << b)-1
    unpack = [(i & mask,(i >> b)&mask,(i >> (2*b))&mask) for i in range(1<<(3*b))]
    smul = [[sum(mul[s][v[j]] << (b*j) for j in range(3)) for v in unpack] for s in range(q)]
    size=1<<(3*b)
    def eprod(i,t,a,B,c):
        x,y,z=unpack[t]
        if i==0:return smul[y][c] ^ smul[z][B]
        if i==1:return smul[x][c] ^ smul[z][a]
        return smul[x][B] ^ smul[y][a]
    def rank1_symmetric(a,B,c):
        aa=unpack[a];bb=unpack[B];cc=unpack[c]
        M=[[aa[0],bb[0],cc[0]],[aa[1],bb[1],cc[1]],[aa[2],bb[2],cc[2]]]
        if M[0][1]!=M[1][0] or M[0][2]!=M[2][0] or M[1][2]!=M[2][1]:return False
        for i in range(3):
            for k in range(i+1,3):
                for j in range(3):
                    for l in range(j+1,3):
                        if mul[M[i][j]][M[k][l]] ^ mul[M[i][l]][M[k][j]]:return False
        return True
    associated=condition=disagree=0
    for a in range(size):
      for B in range(size):
       for c in range(size):
        # Necessary and sufficient associativity constraints for all 27 basis triples.
        z=(eprod(0,c,a,B,c)==0 and eprod(1,c,a,B,c)==0 and
           eprod(0,B,a,B,c)==0 and eprod(2,B,a,B,c)==0 and
           eprod(1,a,a,B,c)==0 and eprod(2,a,a,B,c)==0)
        if z:
          u=eprod(0,a,a,B,c)
          z=(u==eprod(1,B,a,B,c)==eprod(2,c,a,B,c))
        v=rank1_symmetric(a,B,c)
        associated+=bool(z)
        condition+=bool(v)
        disagree+=bool(z!=v)
    assert associated==condition==q**3 and disagree==0, (q,associated,condition,disagree)
    print('EXHAUSTIVE_OK',f'q={q}',f'tables={size**3}',f'associative={associated}',f'Veronese={condition}',f'mismatch={disagree}')

if __name__=='__main__':
    for q in (2,4):check(q)
