#!/usr/bin/env python3
"""Second bit-packed relation-semigroup checker of ECA image period lifts."""
from collections import Counter,deque

I=sum(1 << (5*i) for i in range(4))

def bit_comp(a,b):
    ans=0
    for i in range(4):
        successors=(a >> (4*i)) & 15
        row=0
        for k in range(4):
            if successors & (1<<k):
                row |= (b>>(4*k))&15
        ans|=row<<(4*i)
    return ans

def rel(rule,symbol):
    ans=0
    for i in range(4):
        for jbit in range(2):
            target=2*(i&1)+jbit
            if (rule>>(2*i+jbit))&1 == symbol:
                ans|=1<<(4*i+target)
    return ans

def accepts_period(relation,k):
    v=I
    for _ in range(k):v=bit_comp(v,relation)
    return bool(v&I)

def classify(rule):
    a,b=rel(rule,0),rel(rule,1)
    seen={I}
    queue=deque([I])
    while queue:
        z=queue.popleft()
        for t in (a,b):
            w=bit_comp(z,t)
            if w not in seen:
                seen.add(w)
                queue.append(w)
    periodic=[z for z in seen if any(accepts_period(z,k) for k in range(1,5))]
    return next(m for m in range(1,13) if all(accepts_period(z,m) for z in periodic))

def main():
    cs=[classify(r) for r in range(256)]
    assert Counter(cs)==Counter({1:156,2:82,4:6,6:12})
    assert [i for i,m in enumerate(cs) if m==4]==[90,94,122,133,161,165]
    assert [i for i,m in enumerate(cs) if m==6]==[22,30,86,104,106,120,135,149,151,169,225,233]
    print('VERIFY_BITS_OK',dict(sorted(Counter(cs).items())))

if __name__ == '__main__':
    main()
