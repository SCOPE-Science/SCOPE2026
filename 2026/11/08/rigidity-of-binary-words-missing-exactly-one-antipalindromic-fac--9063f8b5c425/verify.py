"""Independent finite checks of the stated antipalindromic first-stability theorem.
All infinite quantifiers are established by the accompanying proof, not by this script.
"""
from itertools import product

def a_count(w):
    found=set()
    for L in range(2,len(w)+1,2):
        for p in range(len(w)-L+1):
            u=w[p:p+L]
            if all(u[j]!=u[-1-j] for j in range(L//2)):
                found.add(u)
    return len(found)

def edge_count(w):
    edge=''.join('1' if w[i]==w[i+1] else '0' for i in range(len(w)-1))
    # Each antipal factor is encoded by its first symbol and an odd
    # palindromic edge factor whose middle entry is zero.
    return len({(w[p],edge[p:p+L-1])
               for L in range(2,len(w)+1,2)
               for p in range(len(w)-L+1)
               if edge[p:p+L-1]==edge[p:p+L-1][::-1]
               and edge[p+(L-2)//2]=='0'})

def period_word(m,period,phase=0):
    return ''.join(period[(phase+i)%len(period)] for i in range(m))

def candidates(n):
    assert n>=7
    A={period_word(n,'01',i) for i in range(2)}
    # Directly specify edge sequences. A binary word is recovered from
    # first bit and consecutive equality/non-equality edges.
    def decode(first, edges):
        out=first
        for e in edges:out+=out[-1] if e=='1' else str(1-int(out[-1]))
        return out
    B={decode(s,'1'+'0'*(n-2)) for s in '01'}
    C={decode(s,'0'*(n-2)+'1') for s in '01'}
    D={decode(s,'1'+'0'*(n-3)+'1') for s in '01'} if n%2==0 else set()
    P={period_word(n,'0011',i) for i in range(4)}
    return {'A':A,'B':B,'C':C,'D':D,'P':P}

def assert_edge_classes(n):
    classes=candidates(n)
    good=set().union(*classes.values())
    assert sum(map(len,classes.values()))==len(good)==(10 if n%2==0 else 10) + (2 if n%2==0 else 0)
    assert all(a_count(w)==n-1 for w in classes['A'])
    assert all(a_count(w)==n-2 for w in good-classes['A'])
    for typ,ss in classes.items():
        for w in ss:
            for b in '01':
                t=w+b
                new=a_count(t)-a_count(w)
                assert new in (0,1)
                predicted= (typ=='A' and b!=w[-1]) or (typ=='B' and b!=w[-1]) or (typ=='B' and n%2==1 and b==w[-1]) or (typ=='P' and t in candidates(n+1)['P'])
                assert (new==1)==predicted,(typ,n,w,b,new,predicted)
                assert (n-a_count(t)<=1)==(t in set().union(*candidates(n+1).values()))

count_words=0
for n in range(7,16):
    expected=set().union(*candidates(n).values())
    seen=set()
    for v in product('01',repeat=n):
        w=''.join(v); ac=a_count(w)
        assert ac==edge_count(w),(n,w,ac,edge_count(w))
        if ac>=n-2:seen.add(w)
        count_words+=1
    assert seen==expected,(n,len(seen),len(expected),sorted(seen^expected))
    assert_edge_classes(n)
for n in range(16,90):
    assert_edge_classes(n)
print(f'VERIFY_OK exhaustive_binary_words={count_words} n=7..15 template_extensions=n7..89')
