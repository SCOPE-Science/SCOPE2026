"""Exact finite-certificate verifier for dyadic Abelian exponents in Rudin-Shapiro."""
from fractions import Fraction
from pathlib import Path
import json

MORPH={'a':'ab','b':'ac','c':'db','d':'dc'}
SIGN={'a':1,'b':1,'c':-1,'d':-1}

def sigma(w):
    return ''.join(MORPH[c] for c in w)

def factors(w, m):
    return {w[j:j+m] for j in range(len(w)-m+1)}

def factor_certificate():
    w='a'
    for _ in range(7):
        w=sigma(w)
    F=factors(w, 6)
    assert len(w)==128 and len(F)==40
    # Every length-6 factor of sigma(v) is inside sigma(u) for a length-6
    # factor u of v; this closure proves the infinite fixed-point language.
    closure=set()
    for v in F:
        closure.update(factors(sigma(v), 6))
    assert closure==F
    patterns={tuple(SIGN[x] for x in v) for v in F}
    assert len(patterns)==36
    return F, patterns

def block_sums_sign_pattern(x, parity, odd_k, second_half, z):
    # Normalized aligned block sums: if k is odd, even block index only;
    # if k is even, all aligned blocks have sum +/- H.
    # P/H and Q/H are (z,z) in first half, (z,T-z) in second half,
    # with T=1 for odd k and T=2 for even k.
    T=1 if odd_k else 2
    P=z
    Q=(T-z) if second_half else z
    e=4 if odd_k else 5
    out=[]
    for j in range(e):
        even_index=(parity+j)%2 == 0
        aligned=(x[j] if (even_index or not odd_k) else 0)
        cur, following=(P,Q) if even_index else (Q,P)
        out.append(aligned - cur*x[j] + following*x[j+1])
    return out

def has_common_linear_root(pattern, parity, odd_k, second_half):
    f0=block_sums_sign_pattern(pattern, parity, odd_k, second_half, 0)
    f1=block_sums_sign_pattern(pattern, parity, odd_k, second_half, 1)
    coeff=[]
    const=[]
    for j in range(1,len(f0)):
        const.append(f0[j]-f0[0])
        coeff.append(f1[j]-f1[0]-const[-1])
    roots={Fraction(-b,a) for a,b in zip(coeff,const) if a!=0}
    if any(a==0 and b!=0 for a,b in zip(coeff,const)):return False
    if len(roots)>1:return False
    # If all slopes and constants vanish, every value is a root.
    return True

def proof_certificate():
    F,patterns=factor_certificate()
    total=0
    for odd_k in [True,False]:
        for p in patterns:
            for parity in [0,1]:
                for second_half in [False,True]:
                    total+=1
                    assert not has_common_linear_root(p,parity,odd_k,second_half), (odd_k,p,parity,second_half)
    assert total == 288
    recorded=json.loads((Path(__file__).resolve().parent/'CERTIFICATE.json').read_text(encoding='utf8'))
    assert recorded['generation_depth']==7 and set(recorded['precursor_factors'])==F
    assert set(recorded['coded_sign_factors'])=={''.join('+' if a==1 else '-' for a in p) for p in patterns}
    assert len(recorded['mode_summary'])==4
    assert all(sum(z['contradiction_counts'].values())==72 and not z['contradiction_counts'].get('solution_possible') for z in recorded['mode_summary'])
    print('CERTIFICATE_OK', 'four_letter_factors',len(F), 'binary_factors',len(patterns),'linear_cases',total)

def rs(n):
    return 1-2*((n&(n>>1)).bit_count()&1)

def direct_checks():
    N=50000
    r=[rs(i) for i in range(N)]
    pref=[0]
    for x in r: pref.append(pref[-1]+x)
    count=0
    for k in range(10):
        L=1<<k
        e=4 if k%2==1 else 5
        for i in range(N-e*L):
            a=pref[i+L]-pref[i]
            assert any(pref[i+(j+1)*L]-pref[i+j*L] != a for j in range(1,e)), (k,i)
            count+=1
        if k%2==0:
            i=7*L
            a=pref[i+L]-pref[i]
            assert all(pref[i+(j+1)*L]-pref[i+j*L]==a for j in range(1,4))
        else:
            i=9*L+L//2
            a=pref[i+L]-pref[i]
            assert all(pref[i+(j+1)*L]-pref[i+j*L]==a for j in range(1,3))
    print('DIRECT_OK', 'positions_checked',count,'max_period',512)

if __name__=='__main__':
    proof_certificate()
    direct_checks()
    print('VERIFY_OK')
