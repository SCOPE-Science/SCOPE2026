#!/usr/bin/env python3
"""Finite checks of Feres angular transition graph and twisted Fourier contraction."""
import math, numpy as np

def u(beta,t):return (1+math.tan(beta)*math.cos(t)/math.sin(t))/2

def prob(alpha,t):
    pi=math.pi
    if 0<=t<alpha:p1=1.
    elif alpha<=t<pi-3*alpha:p1=u(alpha,t)
    elif pi-3*alpha<=t<pi-2*alpha:p1=2*math.cos(2*alpha)*u(2*alpha,t)
    else:p1=0.
    if 0<=t<pi-3*alpha:p2=0.
    elif pi-3*alpha<=t<pi-2*alpha:p2=u(alpha,t)-2*math.cos(2*alpha)*u(2*alpha,t)
    elif pi-2*alpha<=t<pi-alpha:p2=u(alpha,t)
    else:p2=0.
    if 0<=t<2*alpha:p3=0.
    elif 2*alpha<=t<3*alpha:p3=2*math.cos(2*alpha)*u(2*alpha,-t)
    elif 3*alpha<=t<pi-alpha:p3=u(alpha,-t)
    else:p3=1.
    if 0<=t<alpha:p4=0.
    elif alpha<=t<2*alpha:p4=u(alpha,-t)
    elif 2*alpha<=t<3*alpha:p4=u(alpha,-t)-2*math.cos(2*alpha)*u(2*alpha,-t)
    else:p4=0.
    return [p1,p2,p3,p4]

def f(alpha,t):return [t+2*alpha,-t+2*math.pi-4*alpha,t-2*alpha,-t+4*alpha]

def check(n,ratio):
    alpha=math.pi/n; theta=alpha*ratio
    A=[theta+2*j*alpha for j in range(n) if theta+2*j*alpha<math.pi]
    B=[-theta+2*j*alpha for j in range(1,n) if 0<-theta+2*j*alpha<math.pi]
    states=A+B
    assert len(states)==n, (n,len(states))
    P=np.zeros((n,n))
    for i,t in enumerate(states):
        for p,tp in zip(prob(alpha,t),f(alpha,t)):
            if p>1e-11:
                j=min(range(n),key=lambda x:abs(states[x]-tp))
                assert abs(states[j]-tp)<1e-11,(n,i,tp,states)
                P[i,j]+=p
    assert np.max(abs(np.sum(P,axis=1)-1))<1e-11
    pi0=np.sin(states);pi0/=sum(pi0)
    assert np.max(abs(pi0@P-pi0))<1e-11
    assert np.max(abs(pi0[:,None]*P-P.T*pi0[None,:]))<1e-11
    for k in (1,2,3,4):
        K=P*np.exp(2j*k*np.array(states))[None,:]
        r=max(abs(np.linalg.eigvals(K)))
        assert r<1-1e-8,(n,k,r)
    graph={i:{j for j in range(n) if P[i,j]>1e-11} for i in range(n)}
    assert all(i in graph[j] for i in graph for j in graph[i])
    degrees=sorted(len(s) for s in graph.values())
    assert degrees==[1,1]+[2]*(n-4)+[3,3],(n,degrees)
    # Extract unique undirected cycle by pruning the two degree-1 leaves.
    left=set(range(n))
    while True:
        leaves=[i for i in left if len(graph[i]&left)<=1]
        if not leaves:break
        for i in leaves:left.remove(i)
    assert len(left)==n-2
    print(n, 'states',n,'graph cycle',len(left),'angular period',math.gcd(2,n-2),'max4 Fourier radii', [round(max(abs(np.linalg.eigvals(P*np.exp(2j*k*np.array(states))[None,:]))),8) for k in range(1,5)])
for n in range(7,17):check(n,math.sqrt(2)/3)
print('All finite tests pass; tests are not infinite proofs.')
