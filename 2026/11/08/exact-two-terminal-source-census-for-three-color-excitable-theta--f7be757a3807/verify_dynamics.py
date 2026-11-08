"""Direct synchronous Greenberg--Hastings iteration, no firing-pattern shortcuts."""
from itertools import product
from collections import Counter

def graph(Ls,trees=()):
    adj=[set(),set()]
    for L in Ls:
        path=[0]+list(range(len(adj),len(adj)+L-1))+[1]
        adj.extend(set() for _ in range(L-1))
        for a,b in zip(path,path[1:]):adj[a].add(b);adj[b].add(a)
    for parent in trees:
        u=len(adj);adj.append(set([parent]));adj[parent].add(u)
    return adj

def step(x,adj):
    return tuple((s+1)%3 if s else int(any(x[w]==1 for w in adj[v])) for v,s in enumerate(x))

def pred(Ls):
    def cnt(L,d):
        return sum((L-2*a)%3==d for a in range(L+1))+sum((L-1-2*a)%3==d for a in range(L))
    out=0
    for d in range(3):
        cc=[cnt(L,d) for L in Ls]
        pp=[int(L%3==d) for L in Ls]
        mm=[int((-L)%3==d) for L in Ls]
        def mul(seq):
            a=1
            for v in seq:a*=v
            return a
        out+=3*(mul(cc)-mul([c-p for c,p in zip(cc,pp)])-mul([c-m for c,m in zip(cc,mm)])+mul([c-p-m for c,p,m in zip(cc,pp,mm)]))
    return out

if __name__=='__main__':
    cases=0;checks=0
    for Ls in product(range(2,6),repeat=3):
        a=graph(Ls)
        if len(a)>10:continue
        count=0;fix=0
        for x in product(range(3),repeat=len(a)):
            y=step(x,a); z=step(y,a); w=step(z,a)
            count+=int(w==x and y!=x)
            fix+=int(y==x)
        assert count==pred(Ls),(Ls,count,pred(Ls))
        assert fix==1,(Ls,fix)
        checks+=3**len(a);cases+=1
    print('direct_dynamic_cases=',cases,'states_iterated=',checks)
    for Ls,trees in [((3,3,3),(0,)),((2,4,2),(2,3)),((3,3,3),(2,8,9)),((3,4,5),(2,))]:
        a=graph(Ls,trees)
        if len(a)>12:continue
        count=0
        for x in product(range(3),repeat=len(a)):
            y=step(x,a)
            if step(step(y,a),a)==x and y!=x:count+=1
        assert count==pred(Ls),(Ls,trees,count,pred(Ls))
        print('tree_case=',Ls,trees,'primitive_three=',count)
