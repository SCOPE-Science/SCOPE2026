from collections import defaultdict

def language(k,n):
    M=n+2
    # states (m, t) m run length and t position in full generator, 0 <= t < (k+1)m
    states={(m,t) for m in range(1,M+1) for t in range((k+1)*m)}
    # map word to subset of states after emitting its letters
    start=frozenset(states)
    frontier={'':start}
    for _ in range(n):
        new={}
        for word,sub in frontier.items():
            for a in '01':
                nxt=set()
                for m,t in sub:
                    c='0' if t<m else '1'
                    if c!=a:continue
                    if t+1<(k+1)*m:nxt.add((m,t+1))
                    else:nxt.update((j,0) for j in range(1,M+1))
                if nxt:new[word+a]=frozenset(nxt)
        frontier=new
    return set(frontier)

def forb(k,n):
    out=set()
    for b in range(1,n):
        if b%k:out.add('0'+'1'*b+'0')
    for m in range(1,n):
        out.add('1'+'0'*m+'1'*(k*m+1))
        out.add('0'*(m+1)+'1'*(k*m)+'0')
    return {w for w in out if len(w)<=n}
for k in range(1,5):
 for n in range(1,13):
    lang=language(k,n)
    f=forb(k,n)
    lang2={format(x,'0%db'%n) for x in range(1<<n) if all(y not in format(x,'0%db'%n) for y in f)}
    if lang!=lang2:
       print('MISMATCH',k,n,len(lang),len(lang2),'false allowed',list(lang2-lang)[:10],'false forbid',list(lang-lang2)[:10]);exit(1)
 print('verified k',k,'1..12')
