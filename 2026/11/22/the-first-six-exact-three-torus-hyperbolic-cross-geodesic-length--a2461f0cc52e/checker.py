"""Exact finite certificate: shortest three-torus hyperbolic-cross design geodesics.
No probabilistic tests; candidate ranges are proved complete by the stated norm cap.
"""
from itertools import product
from math import gcd, isqrt

# A hyperbolic-cross frequency is a triple of bounded integers whose
# product of max(1,absolute coordinate) is at most t.
def cross(t):
    return [(i,j,k) for i,j,k in product(range(-t,t+1), repeat=3)
            if max(1,abs(i))*max(1,abs(j))*max(1,abs(k))<=t
            and (i,j,k)!=(0,0,0)]

def run(t, norm2, target):
    frequencies=cross(t)
    assert len(frequencies)>0
    radius=isqrt(norm2)
    tested=0
    primitive=0
    survivors=[]
    witness_count=0
    for a in range(1,radius+1):
        for b in range(a,radius+1):
            for c in range(b,radius+1):
                if a*a+b*b+c*c>norm2:
                    continue
                tested+=1
                if gcd(a,b,c)!=1:
                    continue
                primitive+=1
                # A false candidate gets an explicit integer collision witness.
                w=next((m for m in frequencies if m[0]*a+m[1]*b+m[2]*c==0), None)
                if w is None:
                    survivors.append((a,b,c))
                else:
                    witness_count+=1
    assert survivors==[target], (t,survivors)
    assert sum(x*x for x in target)==norm2
    assert primitive==witness_count+len(survivors)
    return {'t':t,'cross_nonzero_size':len(frequencies),'norm2_min':norm2,
            'canonical_winner':target,'all_candidates_under_norm_cap':tested,
            'primitive_candidates':primitive,'rejected_with_integer_witness':witness_count,
            'survivors':survivors}

if __name__=='__main__':
    table={1:(21,(1,2,4)),2:(65,(2,5,6)),3:(101,(4,6,7)),
           4:(133,(4,6,9)),5:(133,(4,6,9)),6:(314,(7,11,12))}
    for t,(norm2,target) in table.items():
        print(run(t,norm2,target))
    print('EXHAUSTIVE FINITE CERTIFICATE PASSED')
