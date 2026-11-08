#!/usr/bin/env python3
"""Independent exhaustive direct CCA/GHM orbit checks on small circular ladders."""
from itertools import product

def delta(a,b):return ((b-a+1)%3)-1

def graph(n):
    E=set()
    for r in (0,1):
        for j in range(n):
            a=r*n+j;b=r*n+(j+1)%n
            E.add(tuple(sorted((a,b))))
    for j in range(n):E.add((j,j+n))
    N=[set() for _ in range(2*n)]
    for a,b in E:N[a].add(b);N[b].add(a)
    return N

def data(c,n):
    curl=[]
    for i in range(n):
        j=(i+1)%n
        curl.append(delta(c[i],c[j])+delta(c[j],c[n+j])+delta(c[n+j],c[n+i])+delta(c[n+i],c[i]))
    top=sum(delta(c[i],c[(i+1)%n]) for i in range(n))
    return all(x==0 for x in curl),top

def rates(c,N):
    def calc(model):
        seen={}; seq=[];state=c
        while state not in seen:
            seen[state]=len(seq);seq.append(state)
            if model=='CCA':
                state=tuple((s+1)%3 if any(state[j]==(s+1)%3 for j in N[i]) else s for i,s in enumerate(state))
            else:
                state=tuple((s+1)%3 if s in (1,2) or (s==0 and any(state[j]==1 for j in N[i])) else 0 for i,s in enumerate(state))
        cyc=seq[seen[state]:]
        increments=[]
        for k,s in enumerate(cyc):
            t=cyc[(k+1)%len(cyc)]
            if model=='CCA': increments.append(sum(t[j] == (s[j]+1)%3 for j in range(len(s))))
            else:increments.append(sum(s[j]==0 and t[j]==1 for j in range(len(s))))
        return sum(increments),len(cyc)*len(c)
    return calc('CCA'),calc('GHM')

def run():
    for n in (3,4,5):
        neighbors=graph(n);size=0; flat=0;wind=0
        for c in product(range(3),repeat=2*n):
            isflat,h=data(c,n)
            if not isflat:continue
            flat+=1
            (ac,dc),(ag,dg)=rates(c,neighbors)
            assert ac*n==abs(h)*dc,('CCA',n,c,h,ac,dc)
            assert ag*3*n==abs(h)*dg,('GHM',n,c,h,ag,dg)
            if h:wind+=1
            size+=1
        print(f'n={n} checked_flat={flat} with_winding={wind}')
    print('DYNAMICS_OK')

if __name__=='__main__':run()
