"""State-space enumeration of unmodified and self-feedback Paley automata."""
from collections import Counter

def run(p):
    residues={pow(j,2,p) for j in range(1,p)}
    adj=[[v for v in range(p) if (v-u)%p in residues] for u in range(p)]
    def next_state(bits,feedback):
        new=0
        for u,neighbors in enumerate(adj):
            parity=sum((bits>>v)&1 for v in neighbors)%2
            if feedback and u==0: parity^=bits&1
            new|=parity<<u
        return new
    total=1<<p
    observed=Counter(); base=Counter()
    for start in range(total):
        x=start; seq=[]; seen={}
        while x not in seen:
            seen[x]=len(seq);seq.append(x)
            x=next_state(x,True)
        t=seen[x]; per=len(seq)-t
        assert t==0, (p,start,t)
        observed[per]+=1
        x=start;seq=[];seen={}
        while x not in seen:
            seen[x]=len(seq);seq.append(x)
            x=next_state(x,False)
        t=seen[x];per=len(seq)-t
        base[(t,per)]+=1
    assert observed=={1:2,3:2**(p-2)-2,6:3*2**(p-2)},(p,observed)
    assert base=={(0,1):1,(0,3):2**(p-1)-1,(1,1):1,(1,3):2**(p-1)-1},(p,base)
    print(f'prime={p} state_count={total} modified={dict(observed)} unmodified={dict(base)}')

if __name__=='__main__':
    for p in [5,13]:run(p)
