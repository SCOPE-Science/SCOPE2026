"""Independent full-label simulator for deterministic majority on two cliques joined by one edge."""
import math

def update(bits, m, n):
    z=list(bits)
    for i in range(m+n):
        if i<m:
            near=sum(bits[j] for j in range(m) if j!=i)
            if i==0: near+=bits[m]
            degree=(m-1)+(i==0)
        else:
            near=sum(bits[j] for j in range(m,m+n) if j!=i)
            if i==m: near+=bits[0]
            degree=(n-1)+(i==m)
        if 2*near>degree: z[i]=1
        elif 2*near<degree: z[i]=0
    return tuple(z)

def check(m,n):
    hits={}; per_counts={1:0,2:0}; maxent=0; periods=set(); cycles=set()
    for k in range(1<<(m+n)):
        s=tuple((k>>j)&1 for j in range(m+n)); seen={};route=[]; p=s
        while p not in seen:
            seen[p]=len(route);route.append(p);p=update(p,m,n)
            if len(route)>7:raise AssertionError(('long',m,n,k))
        t=seen[p]; period=len(route)-t
        if period not in (1,2):raise AssertionError((m,n,k,period))
        per_counts[period]+=1; maxent=max(maxent,t);periods.add(period)
        if t==0:cycles.add(tuple(sorted(route)))
        hits[(t,period)]=hits.get((t,period),0)+1
    want=2*math.comb(m-1,m//2)*math.comb(n-1,n//2) if m%2==0 and n%2==0 else 0
    assert per_counts[2]==want and hits.get((0,2),0)==want,(m,n,per_counts,hits,want)
    assert maxent==({(1,1):2,(0,0):4}.get((m%2,n%2),5)),(m,n,maxent)
    assert len([c for c in cycles if len(c)==1])==4
    assert len([c for c in cycles if len(c)==2])==want//2
    return maxent,per_counts[2],len(cycles),len(hits)

if __name__=='__main__':
    inspected=0
    for m in range(3,9):
        for n in range(m,9):
            r=check(m,n)
            inspected+=1<<(m+n)
            print(f'{m},{n}: max_entry={r[0]} period2_states={r[1]} cycles={r[2]} transient_classes={r[3]}')
    print('PASS exhaustive labelled configurations:',inspected)
