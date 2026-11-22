"""GF(2) matrix checker for a single self-input on a Paley graph."""
from collections import Counter

def rank(vectors):
    piv={}
    for x in vectors:
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x; break
            x^=piv[k]
    return len(piv)

def check(p):
    assert p%8==5 and all(p%i for i in range(2,int(p**0.5)+1))
    residues={j*j%p for j in range(1,p)}
    base=[sum(1<<j for j in range(p) if (j-i)%p in residues) for i in range(p)]
    edited=base[:]; edited[0]^=1
    def apply(M,vec):
        output=0
        for i,mask in enumerate(M):
            if (mask&vec).bit_count()%2: output|=1<<i
        return output
    vectors=[1<<i for i in range(p)]
    chain=[vectors]
    for _ in range(6):chain.append([apply(edited,v) for v in chain[-1]])
    assert chain[6]==vectors
    assert chain[3]!=vectors
    assert rank([a^b for a,b in zip(chain[3],chain[0])])==2
    assert rank([a^b for a,b in zip(chain[1],chain[0])])==p-1
    assert rank([a^b for a,b in zip(chain[2],chain[0])])==p-1
    assert rank([a^b for a,b in zip(chain[1],chain[0])])==p-1
    # A^4=A and rank(A)=p-1
    plain=base
    plain_ch=[vectors]
    for _ in range(4):plain_ch.append([apply(plain,v) for v in plain_ch[-1]])
    assert plain_ch[4]==plain_ch[1]
    assert rank(plain)==p-1
    print(f'prime={p} nodes={p} rank(B^3-I)=2 rank(B-I)={p-1} rank(B^2-I)={p-1} B^6=I true A^4=A true')

if __name__=='__main__':
    for prime in [5,13,29,37,53,61,101]:
        check(prime)
