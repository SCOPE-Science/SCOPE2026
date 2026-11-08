#!/usr/bin/env python3
"""Direct first-order AST semantics for bounded-variable witness sentences.
All quantification nodes bind a VARIABLE NAME, which is restored on scope exit;
this tests the required local variable recycling rather than adding names.
"""
from itertools import product
from check_necklaces import mkgraph,rot_min


def atom(op,*args):return (op,*args)
def conj(*args):return ('and',args)
def negate(x):return ('not',x)
def exists(v,p):return ('exists',v,p)
def forall(v,p):return ('forall',v,p)
def disj(*args):return ('or',args)

def evaluate(node,graph,env):
    op=node[0]
    if op=='eq':return env[node[1]]==env[node[2]]
    if op=='E':return bool(graph[env[node[1]]][env[node[2]]])
    if op=='not':return not evaluate(node[1],graph,env)
    if op=='and':return all(evaluate(p,graph,env) for p in node[1])
    if op=='or':return any(evaluate(p,graph,env) for p in node[1])
    if op in ('exists','forall'):
        name=node[1]; sub=node[2]; old=env[name]
        values=[]
        for v in range(len(graph)):
            env[name]=v
            values.append(evaluate(sub,graph,env))
            if op=='exists' and values[-1]:break
            if op=='forall' and not values[-1]:break
        env[name]=old
        return (any(values) if op=='exists' else all(values))
    raise ValueError(node)

def twin(x,y,k):
    z=next(v for v in range(k) if v not in (x,y))
    return forall(z,conj(disj(negate(atom('E',x,z)),atom('E',y,z)),
                         disj(negate(atom('E',y,z)),atom('E',x,z))))

def at_least(k,j,current):
    if j==1:return atom('eq',current,current)
    others=[v for v in range(k) if v!=current][:j-1]
    witnesses=[current]+others
    conds=[atom('not',atom('eq',witnesses[i],witnesses[jj]))
           for i in range(j) for jj in range(i+1,j)]
    conds += [twin(current,v,k) for v in others]
    f=conj(*conds)
    for name in reversed(others):f=exists(name,f)
    return f

def color_formula(k,c,current):
    q=at_least(k,c,current)
    return conj(q,negate(at_least(k,c+1,current))) if c<k else q

def cycle_word_formula(k,word):
    assert len(word)>=3 and k>=3
    L=len(word)
    # L successive nodes with labels 0,1,2,1,2,...; last arc returns to 0.
    names=[0]+[1+(i-1)%2 for i in range(1,L)]
    tail=atom('E',names[-1],0)
    for i in reversed(range(1,L)):
        tail=exists(names[i],conj(color_formula(k,word[i],names[i]),
                                  atom('E',names[i-1],names[i]),tail))
    return exists(0,conj(color_formula(k,word[0],0),tail))

def main():
    n_formula=0; n_color=0
    for k in (3,4):
        for sizes in ((1,1,1),(2,1,1),(3,1,1),(1,2,3),(2,2,2),
                      (1,1,1,1),(2,1,1,1),(1,2,2,1),(1,1,1,1,1)):
            _,E=mkgraph(sizes);actual=tuple(min(v,k) for v in sizes)
            # Directly assess the generated unary formulas for every vertex.
            for x in range(len(E)):
                for t in range(1,k+1):
                    got=evaluate(color_formula(k,t,0),E,[x]+[0]*(k-1))
                    expected=(actual[ next(i for i in range(len(sizes)) if x < sum(sizes[:i+1]))]==t)
                    assert got==expected,(k,sizes,x,t,got,expected)
                    n_color+=1
            trials=[actual,actual[1:]+actual[:1],actual[-1:]+actual[:-1],
                    tuple(1 if x!=1 else 2 for x in actual),
                    tuple(k for x in actual)]
            # String types of a different quotient length have separate length tests.
            for trial in trials:
                got=evaluate(cycle_word_formula(k,trial),E,[-1]*k)
                expected=rot_min(tuple(trial))==rot_min(actual)
                assert got==expected,(k,sizes,trial,got,expected)
                n_formula+=1
    print('Direct recursively-scoped variable-name formula checks: {}'.format(n_formula))
    print('Direct unary local fiber-color evaluations: {}'.format(n_color))
    print('formula syntax and semantics checks PASS')
if __name__=='__main__':main()
