"""GF(2) polynomial check of the affine Rule 105 temporal-three resonance."""
import json

def deg(a): return a.bit_length()-1

def rem(a,b):
    while a and deg(a)>=deg(b):a ^= b << (deg(a)-deg(b))
    return a

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return a

def division(a,b):
    q=0
    while a and deg(a)>=deg(b):
        shift=deg(a)-deg(b);q ^= 1<<shift;a ^= b<<shift
    return q,a

# P(s) = (s+1)^2(1+s+s^2+s^3+s^4) over GF(2).
P = (1<<6) ^ (1<<5) ^ (1<<1) ^ 1
H = (1<<2)^1    # (s+1)^2
rows=[]
for n in range(1,241):
    modulus=(1<<n)|1
    allones=(1<<n)-1
    g=gcd(P,modulus)
    gh=gcd(H,modulus)
    solvable=(rem(allones,g)==0)
    fixed_solvable=(rem(allones,gh)==0)
    p3_count=(1<<deg(g)) if solvable else 0
    p1_count=(1<<deg(gh)) if fixed_solvable else 0
    t3=(p3_count-p1_count)//3
    assert p3_count>=p1_count and (p3_count-p1_count)%3==0
    assert p1_count==(4 if n%4==0 else 0)
    assert t3==(20 if n%20==0 else 0)
    if n<=40: rows.append([n,p1_count,p3_count,t3])
print(json.dumps({'tested_lengths':240,'rule':105,'fixed_configs':'4 iff 4 divides n, otherwise 0','primitive_three_orbits':'20 iff 20 divides n, otherwise 0','first_40':[row for row in rows if row[3]>0 or row[0] in (1,4,5,10,12,16,19,21,24,28,36,40)]},separators=(',',':')))
