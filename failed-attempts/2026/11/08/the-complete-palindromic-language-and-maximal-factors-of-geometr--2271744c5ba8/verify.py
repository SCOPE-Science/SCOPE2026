"""Direct finite factor census for sparse-power palindrome classification."""
from collections import defaultdict

def expected_words(base, maximum):
    out=defaultdict(set)
    for n in range(1,maximum+3):
        out[n].add(b'0'*n)
        if n%2:
            out[n].add(b'0'*(n//2)+b'1'+b'0'*(n//2))
    gap=base-1
    t=0
    while gap+1<=maximum+2:
        bound=1 if t==0 else (base-1)*base**(t-1)-1
        for pad in range(bound+1):
            word=b'0'*pad+b'1'+b'0'*(gap-1)+b'1'+b'0'*pad
            if len(word)>maximum+2:break
            out[len(word)].add(word)
        t+=1;gap*=base
    return out

def check(base,maximum=110,prefix_len=13000):
    word=bytearray(b'0'*prefix_len)
    x=1
    while x<prefix_len:
        word[x]=49;x*=base
    actual=defaultdict(set)
    for n in range(1,maximum+3):
        for i in range(prefix_len-n+1):
            z=word[i:i+n]
            if z==z[::-1]:actual[n].add(bytes(z))
    want=expected_words(base,maximum)
    for n in range(1,maximum+1):
        assert actual[n]==want[n],(base,n,actual[n]-want[n],want[n]-actual[n])
    max_actual={u for n in range(1,maximum+1) for u in actual[n] if all((a+u+a) not in actual[n+2] for a in (b'0',b'1'))}
    max_want=set()
    t=0;gap=base-1
    while gap+3<=maximum:
        pad=1 if t==0 else (base-1)*base**(t-1)-1
        u=b'0'*pad+b'1'+b'0'*(gap-1)+b'1'+b'0'*pad
        if len(u)<=maximum:max_want.add(u)
        t+=1;gap*=base
    assert max_actual==max_want,(base,[(len(u),u[:40]) for u in max_actual^max_want])
    return sum(len(actual[n]) for n in range(1,maximum+1)),len(max_want)

if __name__=='__main__':
    total=0
    for b in range(2,11):
        pal, maxpal=check(b)
        print('base',b,'distinct_palindromes_through_110',pal,'maximal_through_110',maxpal)
        total+=pal
    print('VERIFY_OK bases=2..10 lengths=1..110 palindromes_total=',total)
