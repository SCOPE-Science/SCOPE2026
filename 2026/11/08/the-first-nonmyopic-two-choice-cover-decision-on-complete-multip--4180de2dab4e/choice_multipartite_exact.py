"""Exact optimal two-offer cover-control checker for complete multipartite graphs.
All arithmetic is rational, including Bellman-system solves."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, combinations_with_replacement
from time import monotonic


def linear_solve(A,b):
    n=len(b); M=[[F(a) for a in row]+[F(rhs)] for row,rhs in zip(A,b)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if M[i][j]),None)
        if pivot is None: raise ArithmeticError('Improper policy: singular Bellman system')
        M[j],M[pivot]=M[pivot],M[j]
        fac=M[j][j]; M[j]=[v/fac for v in M[j]]
        for i in range(n):
            if i==j:continue
            fac=M[i][j]
            if fac:M[i]=[v-fac*w for v,w in zip(M[i],M[j])]
    return [M[i][-1] for i in range(n)]


def solve_sizes(sizes, first_counterexample_only=False):
    sizes=tuple(sizes); k=len(sizes); N=sum(sizes)
    dp={}; bad=[]; ncells=0; iterations=0
    states=sorted(product(*(range(q+1) for q in sizes)),key=sum,reverse=True)
    for x in states:
        if not any(x): continue
        active=tuple(i for i in range(k) if x[i])
        if x==sizes:
            dp[x]={i:F(0) for i in active};continue
        local=[]
        for i in active:
            opts=[]
            den=N-sizes[i]
            for j in range(k):
                if i==j:continue
                if x[j]: opts.append((j,True,F(x[j],den)))
                if x[j]<sizes[j]: opts.append((j,False,F(sizes[j]-x[j],den)))
            assert sum(t[2] for t in opts)==1
            events=[(a,b,a[2]*b[2]) for a in opts for b in opts]
            local.append((i,events))
        # Begin from a high finite upper bound to obtain a proper, productive policy.
        V={i:F(1000000) for i in active}
        for it in range(120):
            A=[[F(int(i==j)) for j in active] for i in active]
            bvec=[F(1) for i in active]
            for r,(i,ev) in enumerate(local):
                for a,b,w in ev:
                    options=[]
                    for j,visited,p in (a,b):
                        if visited:options.append((V[j],True,j))
                        else:
                            xx=tuple(x[t]+int(t==j) for t in range(k))
                            options.append((dp[xx][j],False,j))
                    val,vis,j=min(options, key=lambda z:(z[0],z[1],z[2]))
                    if vis:A[r][active.index(j)]-=w
                    else:bvec[r]+=w*val
            sol=linear_solve(A,bvec)
            W=dict(zip(active,sol))
            iterations+=1
            if W==V:break
            # Check whether new values satisfy the full optimal Bellman equation.
            is_optimal=True
            for i,ev in local:
                rhs=F(1)
                for a,b,w in ev:
                    vals=[]
                    for j,visited,p in (a,b):
                        if visited: vals.append(W[j])
                        else:
                            xx=tuple(x[t]+int(t==j) for t in range(k))
                            vals.append(dp[xx][j])
                    rhs+=w*min(vals)
                if rhs!=W[i]:is_optimal=False;break
            V=W
            if is_optimal:break
        else:raise ArithmeticError(('Policy iteration did not converge',sizes,x))
        for i,ev in local:
            rhs=F(1)
            for a,b,w in ev:
                vals=[]
                for j,visited,p in (a,b):
                    if visited:vals.append(V[j])
                    else:
                        xx=tuple(x[t]+int(t==j) for t in range(k))
                        vals.append(dp[xx][j])
                rhs+=w*min(vals)
                if a[1]!=b[1]:
                    val=[]
                    for j,visited,p in (a,b):
                        val.append((V[j] if visited else dp[tuple(x[t]+int(t==j) for t in range(k))][j],j,visited))
                    unvisited=next(z for z in val if not z[2])
                    visited=next(z for z in val if z[2])
                    if visited[0]<unvisited[0]:
                        bad.append(dict(sizes=sizes,x=x,current_part=i,unvisited_part=unvisited[1],visited_part=visited[1],unvisited_value=str(unvisited[0]),visited_value=str(visited[0]),gap=str(unvisited[0]-visited[0])))
            assert rhs==V[i],('not Bellman optimal',sizes,x,i)
            ncells+=1
        dp[x]=V
        if bad and first_counterexample_only:
            return bad[0],ncells,iterations,dp
    return bad,ncells,iterations,dp

if __name__=='__main__':
    t=monotonic(); cases=0;cells=0;iterations=0
    bad9=[];nine_cases=0;nine_cells=0
    # All isomorphism types of connected complete multipartite graphs on at
    # most nine vertices are precisely integer partitions with >=2 parts.
    for N in range(2,10):
        casesN=0
        for k in range(2,N+1):
            for sizes in combinations_with_replacement(range(1,N),k):
                if sum(sizes)!=N: continue
                bad,c,it,dp=solve_sizes(sizes)
                if N<9:
                    assert not bad, ('Unexpected earlier counterexample',sizes,bad[0])
                    cases+=1;cells+=c;iterations+=it
                else:
                    nine_cases+=1;nine_cells+=c
                    if bad:bad9.append((sizes,bad))
                casesN+=1
        print('order',N,'types',casesN,'complete',round(monotonic()-t,2),'seconds',flush=True)
    assert (cases,cells)==(58,7391),(cases,cells)
    assert (nine_cases,nine_cells)==(29,11956),(nine_cases,nine_cells)
    assert len(bad9)==1 and bad9[0][0]==(1,2,6),bad9
    exceptions={
       (tuple(z['x']),z['current_part'],z['unvisited_part'],z['visited_part'])
       for z in bad9[0][1]
    }
    assert exceptions=={
        ((0,1,1),2,0,1),((0,2,1),2,0,1),((0,2,2),2,0,1)
    }, exceptions
    witness=next(z for z in bad9[0][1] if tuple(z['x'])==(0,2,2))
    assert F(witness['unvisited_value'])==F(863502507888814,58892405629491)
    assert F(witness['visited_value'])==F(136185927932950168179443,9289655025356352195549)
    assert F(witness['gap'])==F(3210462360632365129,1327093575050907456507)
    print('PASS: 58 types through eight vertices; 7391 rational Bellman states')
    print('PASS: 29 types with nine vertices; only K_(1,2,6) has counterexamples')
    print('PASS: exactly three distinct bad decision-state types at order nine')
    print('PASS: exact witness values and strictly positive gap')
    print('elapsed_seconds',round(monotonic()-t,2),'policy_iterations_small',iterations)
