"""Independent exact wave counts for three classical cubic incidence graphs.
Run: python3 levi_wave_verify.py
"""
from collections import defaultdict

def incidence_gp(n,k):
    # Vertices u_i=0..n-1, v_i=n..2n-1.
    edges=set()
    for i in range(n):
        for a,b in [(i,(i+1)%n),(n+i,n+(i+k)%n),(i,n+i)]:
            edges.add(tuple(sorted((a,b))))
    points=[i for i in range(n) if i%2==0]+[n+i for i in range(n) if i%2==1]
    lines=[i for i in range(n) if i%2==1]+[n+i for i in range(n) if i%2==0]
    pids={x:j for j,x in enumerate(points)}
    lids={x:j for j,x in enumerate(lines)}
    R=[[] for _ in range(n)]
    for a,b in edges:
        if a in pids:
            R[lids[b]].append(pids[a])
        else:
            R[lids[a]].append(pids[b])
    return tuple(tuple(sorted(r)) for r in R)

PAPPUS=((0,1,4),(1,2,5),(2,3,0),(3,4,7),(4,5,8),
        (5,6,3),(6,7,1),(7,8,2),(8,0,6))

def graph_data(R):
    m=len(R)
    assert all(len(set(r))==3 for r in R)
    assert sorted(j for r in R for j in r)==[i for i in range(m) for _ in range(3)]
    point_lines=[tuple(i for i, r in enumerate(R) if p in r) for p in range(m)]
    assert all(len(x)==3 for x in point_lines)
    return m,point_lines

def dfs_count(R):
    m,P=graph_data(R)
    count=0
    # Fix the colour of point zero to zero; multiply by 3 at the end.
    for z in range(3**(m-1)):
        p=[0];v=z
        for _ in range(m-1): p.append(v%3);v//=3
        eligible=[]
        for row in R:
            avail=[c for c in range(3) if any(p[j]==(c+1)%3 for j in row)]
            if not avail:break
            eligible.append(avail)
        if len(eligible)!=m:continue
        masks=[]
        for i,avail in enumerate(eligible):
            masks.append([sum(1<<j for j in R[i] if c==(p[j]+1)%3) for c in avail])
        def dfs(i,mask):
            if i==m:return int(mask==(1<<m)-1)
            return sum(dfs(i+1,mask|q) for q in masks[i])
        count+=dfs(0,0)
    return 3*count

def subset_dp_count(R):
    m,P=graph_data(R)
    allmask=(1<<m)-1
    answer=0
    for z in range(3**(m-1)):
        p=[0];v=z
        for _ in range(m-1):p.append(v%3);v//=3
        dp={0:1}
        for row in R:
            patterns=[]
            for c in range(3):
                if not any(p[j]==(c+1)%3 for j in row):continue
                patterns.append(sum(1<<j for j in row if c==(p[j]+1)%3))
            nd=defaultdict(int)
            for mask,nways in dp.items():
                for cover in patterns:nd[mask|cover]+=nways
            dp=nd
            if not dp:break
        answer+=dp.get(allmask,0)
    return 3*answer

def independent_direct_small(R):
    # Entire 3^(2m) state space for m<=4, with direct GHM update.
    m,P=graph_data(R)
    if m>4:return None
    nbr=[[] for _ in range(2*m)]
    for i,row in enumerate(R):
        for j in row:
            nbr[i].append(m+j);nbr[m+j].append(i)
    count=0
    for t in range(3**(2*m)):
        state=[];u=t
        for i in range(2*m):state.append(u%3);u//=3
        y=list(state)
        for _ in range(3):
            y=[(a+1)%3 if a else int(any(y[j]==1 for j in nbr[i])) for i,a in enumerate(y)]
        if y==state and any(state):
            z=list(state)
            z=[(a+1)%3 if a else int(any(z[j]==1 for j in nbr[i])) for i,a in enumerate(z)]
            if z!=state:count+=1
    return count

def main():
    cases=[('Mobius-Kantor',incidence_gp(8,3),54036),
           ('Pappus',PAPPUS,134478),
           ('Desargues',incidence_gp(10,3),645180)]
    for name,R,expected in cases:
        a=dfs_count(R)
        b=subset_dp_count(R)
        assert a==b==expected,(name,a,b,expected)
        print(f'{name}: {len(R)*2} vertices, periodic phase states {a}, primitive 3-orbits {a//3}; DFS and mask-DP agree')
    # Direct state-space cross-check on smallest bipartite cubic benchmark K3,3.
    k33=tuple((0,1,2) for _ in range(3))
    assert dfs_count(k33)==subset_dp_count(k33)==independent_direct_small(k33)==36
    print('K3,3: direct 729-state check agrees (36 phase states, 12 orbits)')
if __name__=='__main__':main()
