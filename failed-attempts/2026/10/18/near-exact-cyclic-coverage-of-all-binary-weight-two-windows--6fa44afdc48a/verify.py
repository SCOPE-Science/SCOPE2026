"""Independent finite checks for sparse fixed-weight cyclic coverage.
This program verifies finite cases only; the uniform bounds use the written proof.
"""
from itertools import product

def gap_sequence(k):
    assert k >= 3
    g=[]
    for d in range(1,k//2+1):
        g.append(d)
        if d != k-d:
            g.append(k-d)
    g.append(k-1)
    return g

def host(k):
    return ''.join('1'+'0'*(d-1) for d in gap_sequence(k))

def spectrum(word,k):
    s=word+word[:k-1]
    return {s[i:i+k] for i in range(len(word)) if s[i:i+k].count('1')==2}

def required(k):
    return {'0'*i+'1'+'0'*(j-i-1)+'1'+'0'*(k-j-1) for i in range(k) for j in range(i+1,k)}

def brute(k, maxlength):
    target=required(k)
    for length in range(len(target),maxlength+1):
        for bits in product('01',repeat=length-1):
            s='0'+''.join(bits)
            if target <= spectrum(s,k):
                return length,s
    return None

def verify():
    for k in range(3,201):
        g=gap_sequence(k)
        assert sorted(g) == sorted(list(range(1,k))+[k-1])
        assert all(g[(i-1)%len(g)]>=k-d and g[(i+1)%len(g)]>=k-d
                   for i,d in enumerate(g))
        w=host(k)
        assert len(w)==k*(k+1)//2-1
        # Distinct target substrings, verified by direct extraction.
        assert len(spectrum(w,k))==k*(k-1)//2
        if k<=16:
            assert spectrum(w,k)==required(k)
    for k in (3,4,5):
        got=brute(k,len(host(k)))
        assert got is not None and got[0]==(3 if k==3 else len(host(k))), (k,got)
    print('VERIFY_OK; construction k=3..200; exhaustive minima k=3,4,5')
if __name__=='__main__': verify()
