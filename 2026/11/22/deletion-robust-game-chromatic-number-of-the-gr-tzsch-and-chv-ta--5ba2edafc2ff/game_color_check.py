#!/usr/bin/env python3
"""Finite exact vertex-colouring game checker, standard library only.
Runs independent recursion and canonical colour-name memoization.
"""
from functools import lru_cache

# Two explicit labelled graphs, no graph library or downloadable data.
GROTZSCH=((1,4,6,9),(0,2,5,7),(1,3,6,8),(2,4,7,9),
          (0,3,5,8),(1,4,10),(0,2,10),(1,3,10),(2,4,10),
          (0,3,10),(5,6,7,8,9))
CHVATAL=((1,4,6,9),(0,2,5,7),(1,3,6,8),(2,4,7,9),
         (0,3,5,8),(1,4,10,11),(0,2,10,11),(1,3,8,11),
         (2,4,7,10),(0,3,10,11),(5,6,8,9),(5,6,7,9))

def canonical(state):
    naming={};out=[]
    for c in state:
        if not c:out.append(0)
        else:
            if c not in naming:naming[c]=len(naming)+1
            out.append(naming[c])
    return tuple(out)

def without(g, omitted):
    vertices=[v for v in range(len(g)) if v!=omitted]
    new={v:i for i,v in enumerate(vertices)}
    return tuple(tuple(new[w] for w in g[v] if w!=omitted) for v in vertices)

def chromatic_possible(g, k):
    # Independent conventional backtracking, unrelated to minimax.
    order=sorted(range(len(g)),key=lambda v:-len(g[v]))
    state=[0]*len(g)
    def backtrack(t):
        if t==len(g):return True
        v=order[t];used={state[w] for w in g[v]}
        for c in range(1,k+1):
            if c not in used:
                state[v]=c
                if backtrack(t+1):return True
                state[v]=0
        return False
    return backtrack(0)

def game_alice_wins(g,k):
    # All complete legal histories, exact minmax, quotiented solely by
    # global permutations of the k color names.
    n=len(g)
    @lru_cache(maxsize=None)
    def solve(state):
        used=sum(c>0 for c in state)
        if used==n:return True
        moves=[]
        for v in range(n):
            if state[v]==0:
                prohibited={state[w] for w in g[v]}
                allowed=[c for c in range(1,k+1) if c not in prohibited]
                if not allowed:return False
                moves.extend((v,c) for c in allowed)
        if used%2==0:
            return any(solve(canonical(state[:v]+(c,)+state[v+1:]))
                       for v,c in moves)
        return all(solve(canonical(state[:v]+(c,)+state[v+1:]))
                   for v,c in moves)
    outcome=solve((0,)*n)
    return outcome,solve.cache_info().currsize

if __name__=='__main__':
    for name,g in [('Grotzsch',GROTZSCH),('Chvatal',CHVATAL)]:
        n=len(g)
        assert all(v not in g[v] and len(set(g[v]))==len(g[v]) for v in range(n))
        assert all(v in g[w] for v in range(n) for w in g[v])
        assert not chromatic_possible(g,3) and chromatic_possible(g,4)
        g4,states4=game_alice_wins(g,4)
        assert g4
        print(name,'n=',n,'m=',sum(len(v) for v in g)//2,'whole_chi=4','whole_game4=',g4,'states4=',states4)
        for omitted in range(n):
            h=without(g,omitted)
            assert not chromatic_possible(h,2)
            assert chromatic_possible(h,3)
            a3,n3=game_alice_wins(h,3)
            a4,n4=game_alice_wins(h,4)
            assert a3 is False and a4 is True
            print('delete=',omitted,'chi=3','game3=',int(a3),'game4=',int(a4),'states3=',n3,'states4=',n4)
    print('ALL CHECKS PASS')
