from fractions import Fraction

def substitute(s):return ''.join('0001' if c=='0' else '0111' for c in s)

def verify():
    word='0'
    for k in range(1,9):
        word=substitute(word)
        assert len(word)==4**k
        z,o=word.count('0'),word.count('1')
        assert z-o==2**k,(k,z,o)
        assert o==(4**k-2**k)//2
    # Language complexity from an 8-level prefix. This is a finite consistency test, not a proof.
    for n in [1,2,3,4,5,6,7,8,11,16,23,32,45,64,100,128,256]:
        p=len({word[i:i+n] for i in range(len(word)-n+1)})
        assert n+1 <=p <=16*n,(n,p)
    print('PASS: 8 exact substitution-count identities and 17 finite factor checks')
if __name__=='__main__':verify()
