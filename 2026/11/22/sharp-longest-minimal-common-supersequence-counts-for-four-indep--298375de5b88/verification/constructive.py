"""Independent gap-branch generation and direct deletion checks."""
from itertools import product,combinations
from math import comb

def sub(p,w):
    pos=0
    for c in w:
        if pos<len(p) and p[pos]==c:pos+=1
    return pos==len(p)

def valid(w,a,b,c,d):
    u='0'*a+'1'*b;v='1'*c+'0'*d
    return sub(u,w) and sub(v,w) and all(not(sub(u,w[:i]+w[i+1:]) and sub(v,w[:i]+w[i+1:])) for i in range(len(w)))

def parts(zeros,ones):
    # all words containing a specified number of zeros and ones
    for positions in combinations(range(zeros+ones),zeros):
        pos=set(positions)
        yield ''.join('0' if j in pos else '1' for j in range(zeros+ones))

def branch(a,b,c,d):
    out=set()
    n=a+b+c+d-1
    for x in range(a+d):
        for h in range(1,a+d-x):
            y=a+d-1-x-h
            if x+h<a or y+h<d:continue
            # complete canonical prefix and suffix one groups
            for pre in parts(x,c-1):
                for suf in parts(y,b-1):
                    w=pre+'1'+'0'*h+'1'+suf
                    # The central ones stand at the last member of first c
                    # and the first member of last b, respectively.
                    if len(w)==n and valid(w,a,b,c,d):out.add(w)
    return out

def formula(a,b,c,d):
    def B(a,b,c,d):
        if a==1:return comb(d+b-1,b)
        if d==1:return comb(a+c-1,c)
        return comb(a+c-2,c-1)*comb(d+b-2,b-1)
    return B(a,b,c,d)+B(c,d,a,b)

count=0;constructed=0
for a,b,c,d in product(range(1,6),repeat=4):
    zero=branch(a,b,c,d)
    # swap and complement the two input languages, preserving ordered inputs
    one={''.join('1' if j=='0' else '0' for j in w) for w in branch(c,d,a,b)}
    assert zero.isdisjoint(one),(a,b,c,d)
    assert len(zero|one)==formula(a,b,c,d),(a,b,c,d,len(zero),len(one))
    assert all(valid(w,a,b,c,d) for w in zero|one)
    count+=1;constructed+=len(zero)+len(one)
print('CONSTRUCTIVE_OK parameter_tuples=',count,'constructed_words=',constructed)
