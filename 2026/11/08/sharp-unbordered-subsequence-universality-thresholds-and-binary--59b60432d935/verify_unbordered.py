"""Direct finite diagnostics for the boundary classification of unbordered binary universal words."""
from itertools import product


def arch_index(w):
    count=0
    seen=0
    for b in w:
        seen|=1<<b
        if seen==3:
            count+=1
            seen=0
    return count

def is_unbordered(w):
    return all(w[:d]!=w[-d:] for d in range(1,len(w)))

def direct_universal(w,k):
    for t in product((0,1),repeat=k):
        i=0
        for a in w:
            if a==t[i]:
                i+=1
                if i==k: break
        if i!=k:return False
    return True

def good_c(c):
    # x=0 normalized. c is the list of first letters of paired arches.
    m=len(c)
    if c[-1]!=0:return False
    for j in range(1,m):
        # 1 <= j <= k-2 = m-1
        if c[m-j-1]==1 and c[m-j]==0 and c[m-j+1:]==c[:j-1]:
            return False
    return True

def encode(c,x=0):
    return (x,x,1-x)+sum(((a,1-a) for a in c),())

def predicted(k):
    if k==1:return {(0,1),(1,0)}
    words=set()
    for c in product((0,1),repeat=k-1):
        if not good_c(c):continue
        for x in (0,1):
            converted=tuple(a^x for a in c)
            w=encode(converted,x)
            words.add(w)
            words.add(w[::-1])
    return words


def execute():
    counts=[]
    n_test=0
    direct_test=0
    for k in range(1,10):
        pred=predicted(k)
        # Check every possible length-minimal word independently via arch, borders.
        length=2*k if k==1 else 2*k+1
        actual=set()
        for w in product((0,1),repeat=length):
            n_test+=1
            if arch_index(w)>=k and is_unbordered(w):actual.add(w)
            if k<=4:
                b=direct_universal(w,k)
                assert b==(arch_index(w)>=k),('direct mismatch',k,w)
                direct_test+=1
        assert pred==actual,(k,len(pred),len(actual),list(pred^actual)[:4])
        # Prove no shorter unbordered universal words for small cases independently.
        if k>=2:
            for w in product((0,1),repeat=2*k):
                n_test+=1
                assert not (arch_index(w)>=k and is_unbordered(w)),('too short',k,w)
        counts.append((k,length,len(actual)))
    # Beyond brute word enumeration, test normalized halfword criterion 2^12 cases.
    for k in range(2,15):
        pred=predicted(k)
        size=4*sum(good_c(c) for c in product((0,1),repeat=k-1))
        assert len(pred)==size,(k,len(pred),size)
        for w in pred:
            assert is_unbordered(w) and arch_index(w)>=k
    for q in range(3,9):
        for k in range(1,16):
            A=tuple(range(q))
            B=(0,)+tuple(range(2,q))+(1,)
            w=A*(k-1)+B
            assert len(w)==q*k
            assert all(w[:d]!=w[-d:] for d in range(1,len(w)))
            assert all(set(w[i*q:(i+1)*q])==set(range(q)) for i in range(k))
    print('PASS: q-ary constructions for q=3..8 and k=1..15')
    print('PASS: complete binary-word classification and minimality; words examined:',n_test)
    print('PASS: independent direct all-subsequence checks:',direct_test)
    print('PASS: normalized-code/reversal tests through k=14')
    print('COUNTS (k,min_length,count):',counts)

if __name__=='__main__':execute()
