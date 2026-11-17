#!/usr/bin/env python3
"""Direct state-transition verification for closed-neighborhood minority on K_(n,n,n)."""
import networkx as nx

def transition(n, mask, v):
    group=v//n
    ones = sum((mask>>j)&1 for j in range(3*n) if j//n!=group)
    current=(mask>>v)&1
    opposite_count = ones if current==0 else 2*n-ones
    same_count=2*n-opposite_count
    # Closed neighborhood has one extra self-vote, so flip iff
    # neighbors of same colour >= n (tie at n flips).
    active = same_count >= n
    return mask ^ (1<<v) if active else mask

def cut(n, mask):
    counts=[sum((mask>>j)&1 for j in range(i*n,(i+1)*n)) for i in range(3)]
    return sum(n*(counts[i]+counts[j])-2*counts[i]*counts[j]
               for i,j in [(0,1),(0,2),(1,2)])

def run(n):
    vertices=range(1<<(3*n)); graph=nx.DiGraph();graph.add_nodes_from(vertices)
    for state in vertices:
        for v in range(3*n): graph.add_edge(state,transition(n,state,v))
    classes=[s for s in nx.strongly_connected_components(graph)
             if all(y in s for x in s for y in graph.successors(x))]
    expected=6*(2**n-1)
    assert len(classes)==1 and len(classes[0])==expected,(n,len(classes),[len(s) for s in classes],expected)
    recurrent=classes[0]
    assert all(cut(n,x)==2*n*n for x in recurrent)
    assert all((cut(n,x)==2*n*n)==(x in recurrent) for x in vertices)
    active=0
    for state in recurrent:
        for v in range(3*n):
            nxt=transition(n,state,v)
            if nxt!=state:
                assert transition(n,nxt,v)==state
                active+=1
    return n,len(recurrent),len(graph),graph.number_of_edges(),active

if __name__=='__main__':
    for n in (1,2,3,4):print(*run(n))
    print('PASS: recurrent class counts, max cuts, transition reversibility (n=1..4).')
