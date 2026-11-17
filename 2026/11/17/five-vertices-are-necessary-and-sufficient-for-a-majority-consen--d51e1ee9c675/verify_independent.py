"""Independent finite check of simultaneous consensus gain and statewise loss.
Requires only Python 3; exhaustive over all labelled simple graphs through five vertices.
The basin algorithm follows trajectories, not predecessor reachability.
"""
from itertools import permutations
from collections import Counter


def pairs(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def neighborhood(n, edge_list):
    a=[set() for _ in range(n)]
    for i,j in edge_list:
        a[i].add(j);a[j].add(i)
    return a


def connected(n, edge_list):
    nbr=neighborhood(n,edge_list)
    seen={0};front=[0]
    for x in front:
        for y in nbr[x]:
            if y not in seen:
                seen.add(y);front.append(y)
    return len(seen)==n


def basin(n, edge_list):
    nbr=neighborhood(n,edge_list)
    goal=(1<<n)-1
    out=set()
    for x in range(1<<n):
        cur=x; seen=set()
        while cur not in seen:
            if cur==0 or cur==goal:
                out.add(x);break
            seen.add(cur)
            y=0
            for v in range(n):
                ones=sum((cur>>u)&1 for u in nbr[v])
                if 2*ones>len(nbr[v]) or (2*ones==len(nbr[v]) and (cur>>v)&1):
                    y|=1<<v
            cur=y
    return out


def canonical_marked(n, eds, deleted):
    P=pairs(n); pos={e:i for i,e in enumerate(P)}
    minimum=None
    for perm in permutations(range(n)):
        edges2={tuple(sorted((perm[u],perm[v]))) for u,v in eds}
        deleted2=tuple(sorted((perm[deleted[0]],perm[deleted[1]])))
        mask=sum(1<<pos[e] for e in edges2)
        q=(mask,pos[deleted2])
        if minimum is None or q<minimum:
            minimum=q
    return minimum


def main():
    all_classes=Counter(); nrecords=Counter()
    for n in range(2,6):
        epairs=pairs(n)
        for mask in range(1<<len(epairs)):
            eds=[p for k,p in enumerate(epairs) if mask>>k&1]
            if not connected(n,eds):continue
            old=basin(n,eds)
            for e in eds:
                rest=[p for p in eds if p!=e]
                if not connected(n,rest):continue
                new=basin(n,rest)
                if len(new)>len(old) and old-new:
                    nrecords[n]+=1
                    key=canonical_marked(n,eds,e)
                    all_classes[key]+=1
    print('gain_and_loss_by_order:',dict(nrecords))
    print('marked_isomorphism_classes:',len(all_classes))
    for key,count in sorted(all_classes.items()):
        mask,k=key;n=5;epairs=pairs(n)
        e=epairs[k]; E=[p for j,p in enumerate(epairs) if mask>>j&1]
        old=basin(n,E);new=basin(n,[p for p in E if p!=e])
        print('class_key=',key,'count=',count,'edges=',E,'deleted=',e,
              'old=',len(old),'new=',len(new),'lost=',len(old-new),'gained=',len(new-old))
    assert dict(nrecords)=={5:240}
    assert len(all_classes)==2
    assert sorted(all_classes.values())==[120,120]
    assert sorted((len(basin(5,[p for j,p in enumerate(pairs(5)) if mask>>j&1])),
                   len(basin(5,[p for j,p in enumerate(pairs(5)) if mask>>j&1 and j!=k])))
                  for mask,k in all_classes)==[(22,24),(26,30)]
    print('PASS')

if __name__=='__main__':main()
