"""Independent suffix-neighbor test of binary five-run MUS formula; Python 3 only."""
from itertools import product
from collections import Counter
from random import Random


def via_suffix_array(w):
    n=len(w)
    positions=sorted(range(n),key=lambda i:w[i:])
    def lcp(i,j):
        h=0
        while i+h<n and j+h<n and w[i+h]==w[j+h]: h+=1
        return h
    result=set()
    for k,p in enumerate(positions):
        L=1+max(lcp(p,positions[k-1]) if k else 0,
                lcp(p,positions[k+1]) if k+1<n else 0)
        if L>n-p: continue
        v=w[p:p+L]
        suffix=v[1:]
        if L==1 or sum(w[t:t+len(suffix)]==suffix for t in range(n-len(suffix)+1))>=2:
            result.add(v)
    return result


def candidate_list(a,b,c,d,e):
    z=[]
    M=max(a,c,e)
    unique=(a==M)+(c==M)+(e==M)==1
    if unique: z.append('0'*M)
    if b!=d: z.append('1'*max(b,d))
    t=min(a,c)+1
    if a!=c and not(unique and M==t):z.append('0'*t+'1')
    t=min(c,e)+1
    if c!=e and not(unique and M==t):z.append('1'+'0'*t)
    r=min(b,d)
    if max(b,d)-r>=2:
        z.append('0'+'1'*(r+1));z.append('1'*(r+1)+'0')
    if b!=d:z.append('0'+'1'*r+'0')
    if c<=a and c<=e:z.append('1'+'0'*c+'1')
    return set(z)

h=Counter(); checked=0
for a,b,c,d,e in product(range(1,8),repeat=5):
    w='0'*a+'1'*b+'0'*c+'1'*d+'0'*e
    got=via_suffix_array(w); want=candidate_list(a,b,c,d,e)
    assert got==want,(a,b,c,d,e,got^want)
    checked+=1;h[len(got)]+=1
print('independent_suffix_array_complete_tuples',checked)
print('independent_mus_histogram',dict(sorted(h.items())))
rng=Random(260504826)
for j in range(180):
    a,b,c,d,e=[rng.randrange(1,90) for _ in range(5)]
    w='0'*a+'1'*b+'0'*c+'1'*d+'0'*e
    assert via_suffix_array(w)==candidate_list(a,b,c,d,e),(a,b,c,d,e)
print('random_long_parameter_tuples',180)
for length in range(5,17):
    for a in range(1,length):
        for b in range(1,length):
            for c in range(1,length):
                for d in range(1,length):
                    e=length-a-b-c-d
                    if e<=0:continue
                    count=len(candidate_list(a,b,c,d,e))
                    assert count<=8
                    if length<=9: assert count<8
print('no_eight_shorter_than_length_10',True)
w='0010111000'
assert len(via_suffix_array(w))==8
assert via_suffix_array(w)=={'000','111','001','011','110','100','010','101'}
print('first_eight_example',w)
print('first_eight_mus',sorted(via_suffix_array(w)))
print('status PASS')
