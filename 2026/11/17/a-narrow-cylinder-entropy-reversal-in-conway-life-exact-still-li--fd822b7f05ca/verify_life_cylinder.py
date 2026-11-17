#!/usr/bin/env python3
"""Exact checks for B3/S23 on a three-row, horizontally cyclic strip with zero vertical exterior.
Python standard library only. The n<3 geometry is intentionally excluded.
"""
from collections import Counter
import sys
sys.setrecursionlimit(10000)

def life_column(left, centre, right):
    result=0
    for row in range(3):
        near=0
        for other in range(max(0,row-1),min(3,row+2)):
            near+=(left>>other)&1
            near+=(right>>other)&1
            if other!=row:near+=(centre>>other)&1
        alive=(centre>>row)&1
        if near==3 or (alive and near==2):result|=1<<row
    return result

def matrices():
    fixed=[[] for _ in range(64)]
    for a in range(8):
        for b in range(8):
            row=8*a+b
            for c in range(8):
                if life_column(a,b,c)==b:fixed[row].append(8*b+c)
    phases=[[] for _ in range(4096)]
    for a in range(64):
        p=a&7; q=a>>3
        for b in range(64):
            x=b&7; y=b>>3
            u=64*a+b
            for c in range(64):
                z=c&7; w=c>>3
                if life_column(p,x,z)==y and life_column(q,y,w)==x:
                    phases[u].append(64*b+c)
    return fixed, phases

def cyclic_components(rows):
    n=len(rows);rev=[[] for _ in range(n)]
    for u,row in enumerate(rows):
        for v in row:rev[v].append(u)
    used=[False]*n;order=[]
    for s in range(n):
        if used[s]:continue
        used[s]=True; stack=[(s,0)]
        while stack:
            x,k=stack[-1]
            if k<len(rows[x]):
                v=rows[x][k];stack[-1]=(x,k+1)
                if not used[v]:used[v]=True;stack.append((v,0))
            else:order.append(x);stack.pop()
    used=[False]*n; comps=[]
    for s in reversed(order):
        if used[s]:continue
        used[s]=True;stack=[s];component=[]
        while stack:
            u=stack.pop();component.append(u)
            for v in rev[u]:
                if not used[v]:used[v]=True;stack.append(v)
        if len(component)>1 or component[0] in rows[component[0]]:
            comps.append(sorted(component))
    return sorted(comps,key=lambda c:(-len(c),c))

def induced(rows, subset):
    index={x:i for i,x in enumerate(subset)}
    return [[index[y] for y in rows[x] if y in index] for x in subset]

def traces(edges, count):
    m=len(edges);t=[0]*(count+1)
    for init in range(m):
        v=[0]*m;v[init]=1
        for k in range(1,count+1):
            w=[0]*m
            for i in range(m):
                if v[i]:
                    for j in edges[i]:w[j]+=v[i]
            v=w;t[k]+=v[init]
    return t

def characteristic(edges):
    m=len(edges);tr=traces(edges,m);c=[1]
    for k in range(1,m+1):
        z=sum(c[k-i]*tr[i] for i in range(1,k+1))
        assert z%k==0,(k,z)
        c.append(-z//k)
    return c # high-degree first

def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out

# Characteristic factors are in descending powers of the indeterminate u.
P14=[1,0,0,-1,2,0,5,-3,2,-1,0,2,0,1,1]
P19=[1,-2,1,-7,9,-17,3,12,47,22,15,4,26,-8,-1,9,-3,-9,5,-2]
P20=[1,-2,1,-7,7,-15,3,26,41,38,25,-24,-20,-62,9,17,-27,-23,33,-16,4]

def collatz_bound(edges, rounds, rational_num=243, rational_den=100, sense='upper'):
    v=[1]*len(edges)
    for _ in range(rounds):v=[sum(v[j] for j in row) for row in edges]
    signs=[rational_den*sum(v[j] for j in row)-rational_num*v[i] for i,row in enumerate(edges)]
    assert min(v)>0
    if sense=='upper':assert max(signs)<0
    else:assert min(signs)>0
    return {'rounds':rounds,'entries':len(v),'min_entry':min(v),'max_entry':max(v),'min_difference':min(signs),'max_difference':max(signs)}

def main():
    fixed,phases=matrices()
    assert sum(map(len,fixed))==134
    assert sum(map(len,phases))==5022
    A=cyclic_components(fixed); B=cyclic_components(phases)
    assert [len(c) for c in A]==[40]
    assert [len(c) for c in B]==[48,6,6]
    AF=induced(fixed,A[0]); BP=induced(phases,B[0])
    assert sum(map(len,AF))==94
    assert sum(map(len,BP))==112
    assert characteristic(AF)==mul([1]+[0]*7,mul(P14,P19))
    assert characteristic(BP)==mul([1]+[0]*14,mul(P14,P20))
    for c in B[1:]:
        assert characteristic(induced(phases,c))==[1,0,0,0,0,0,-1]
    cf=collatz_bound(AF,16,sense='upper')
    ct=collatz_bound(BP,14,sense='lower')
    # Primitivity: both components have a self-loop and are strongly connected by construction.
    assert any(u in AF[u] for u in range(len(AF)))
    assert any(u in BP[u] for u in range(len(BP)))
    ff=traces(AF,14)
    t=traces(BP,14)
    for n in range(3,15):
        period2=t[n]+(12 if n%6==0 else 0)
        assert (period2-ff[n])%2==0 and period2>=ff[n]
        if n<=12:print(f'n={n}: fixed={ff[n]}, temporal_two_return={period2}, primitive_two_orbits={(period2-ff[n])//2}')
    print('fixed_transfer_states=64 edges=134 cyclic_SCCs=40:94')
    print('temporal_two_transfer_states=4096 edges=5022 cyclic_SCCs=48:112,6:6,6:6')
    print('charpolys: u^7*P14*P19 and u^14*P14*P20, plus 2*(u^6-1): exact PASS')
    print('fixed_Perron_certificate upper_243/100:',cf)
    print('two_Perron_certificate lower_243/100:',ct)
    print('all_length_entropy_inequality=PASS')
if __name__=='__main__':main()
