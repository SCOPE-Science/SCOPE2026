#!/usr/bin/env python3
"""Finite arithmetic checks for a theorem on hiccup complement discrepancy.

The unbounded conclusions rely on the written induction, not finite tests.
"""

def words(k, H):
    w = '0'
    out = []
    for _ in range(H + 1):
        out.append(w)
        w = w*k + '1'
    return out

def prefix_extrema(w, k):
    d = 0; lo = hi = 0; position = 0
    for i, c in enumerate(w, 1):
        d += 1 if c == '0' else -(k-1)
        if d > hi:
            hi, position = d, i
        lo = min(lo, d)
    return d, lo, hi, position

def direct_word(k, x, N):
    # Construct the values up to N directly from the original hiccup rule.
    g = x
    seen = bytearray(N+1)
    if g <= N:
        seen[g] = 1
    j = 2
    while g < N:
        g += (1 if (j <= N and seen[j]) else k+1)
        if g <= N:
            seen[g] = 1
        j += 1
    return ''.join('1' if seen[i] else '0' for i in range(1, N+1))

def check(k, x, H=5):
    q=x-2
    delta=q-k+1
    ww=words(k,H)
    word='0'+''.join(w*q+'1' for w in ww)
    if len(word)>160000:
        H-=1
        ww=words(k,H)
        word='0'+''.join(w*q+'1' for w in ww)
    assert direct_word(k,x,len(word))==word,(k,x,'sequence mismatch')
    value=1; start=1
    for h,w in enumerate(ww):
        L=len(w)
        total, lo, hi, pos=prefix_extrema(w,k)
        assert total==1 and lo==0 and hi==1+(k-1)*h
        u=1+(k-1)*sum(len(w2) for w2 in ww[:h])
        assert pos==u
        assert value==1+h*delta
        stage=w*q+'1'
        d=value
        trace=[d]
        for c in stage:
            d+=1 if c=='0' else -(k-1)
            trace.append(d)
        assert d==1+(h+1)*delta
        assert max(trace)==q+1+h*q,(k,x,h,max(trace),q+1+h*q)
        assert min(trace)==min(1+h*delta,1+(h+1)*delta)
        assert trace[(q-1)*L+u]==q+1+h*q
        start+=len(stage)
        value=d
    return len(word)

def main():
    ncases=0
    total=0
    for k in range(2,6):
        for x in range(3,9):
            total+=check(k,x, H=5)
            ncases+=1
    print(f'VERIFY_OK cases={ncases} positions={total}')
if __name__=='__main__':
    main()
