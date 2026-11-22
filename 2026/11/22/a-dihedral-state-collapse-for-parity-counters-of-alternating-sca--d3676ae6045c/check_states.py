"""Independent prefix-vector orbit, congruence, and Moore minimization checks."""
from collections import deque
from math import comb

def transition(v,bit):
    w=v.copy()
    for j in range(len(v),0,-1):
        if (j-1)%2==bit:w[j-1]^=(v[j-2] if j>1 else 1)
    return w

def orbit(k):
    zero=(0,)*k; seen={zero};todo=deque([zero]); edges={}
    while todo:
        s=todo.popleft(); y=[]
        for b in (0,1):
            t=tuple(transition(list(s),b));y.append(t)
            if t not in seen:seen.add(t);todo.append(t)
        edges[s]=tuple(y)
    return seen,edges

def binary_lucas(n,k):
    return int((n&k)==k)

def main():
    state_checks=0; pair_checks=0; literal_min=0
    for k in range(1,91):
        L=1<<k.bit_length()
        # independently build all prefix-count vectors through transition closure
        S,E=orbit(k)
        assert len(S)==L,('orbit size',k,len(S),L)
        # finite state identity: each state encodes a unique cyclic index
        state=[]
        for t in range(L):
            v=tuple(binary_lucas((t+j//2)%L,j) for j in range(1,k+1))
            state.append(v)
        assert len(set(state))==L and set(state)==S
        for t,v in enumerate(state):
            assert E[v]==(state[(-t-1)%L],state[(-t)%L])
            state_checks+=1
        # The k-th coordinate has exact cyclic period L, checked directly.
        outputs=[v[-1] for v in state]
        for d in range(1,L):
            if L%d==0:
                assert any(outputs[t]!=outputs[(t+d)%L] for t in range(L))
                pair_checks+=1
        # Independent deterministic Moore partition refinement over all reachable states
        labels={v:int(v[-1]) for v in S}
        for _ in range(k+5):
            sig={v:(labels[v],labels[E[v][0]],labels[E[v][1]]) for v in S}
            palette={val:i for i,val in enumerate(sorted(set(sig.values())))}
            nxt={v:palette[sig[v]] for v in S}
            if len(set(nxt.values()))==len(set(labels.values())):
                labels=nxt;break
            labels=nxt
        assert len(set(labels.values()))==L,(k,len(set(labels.values())),L)
        literal_min+=L
    print(f'state_orbit_and_minimization PASS k=1..90 transitions={2*state_checks} period_checks={pair_checks} minimized_states_total={literal_min}')
if __name__=='__main__':main()
