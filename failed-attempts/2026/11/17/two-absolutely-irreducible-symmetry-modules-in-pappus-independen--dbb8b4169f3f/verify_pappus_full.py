"""Exact finite verification of the Pappus independence-homology character.

Python 3 standard library only. Run in the directory containing character_classes.tsv.
The signed chain trace and the orbit-cycle trace are calculated separately.
"""
from collections import Counter
from pathlib import Path
import argparse

N = 18
EDGES = [
(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),(3,4),(3,10),
(4,5),(4,15),(5,6),(6,7),(6,11),(7,8),(7,14),(8,9),(9,10),
(9,16),(10,11),(11,12),(12,13),(12,17),(13,14),(14,15),
(15,16),(16,17)]
# This graph also has the LCF representation [5,7,-7,7,-7,-5]^3.

def graph_data():
    adj = [set() for _ in range(N)]
    for a,b in EDGES:
        assert a != b and b not in adj[a]
        adj[a].add(b)
        adj[b].add(a)
    assert len(EDGES)==27 and {len(s) for s in adj}=={3}
    return adj, [sum(1 << j for j in s) for s in adj]

def is_independent(mask, nb):
    t=mask
    while t:
        bit=t&-t
        i=bit.bit_length()-1
        if nb[i]&mask:
            return False
        t-=bit
    return True

def automorphisms(adj):
    mapping = {}
    used = set()
    result=[]
    def backtrack():
        if len(mapping) == N:
            result.append(tuple(mapping[i] for i in range(N)))
            return
        unmapped = [i for i in range(N) if i not in mapping]
        x=max(unmapped,key=lambda i:sum((j in mapping) for j in adj[i]))
        for y in range(N):
            if y in used:
                continue
            if all((u in adj[x])==(mapping[u] in adj[y]) for u in mapping):
                mapping[x]=y
                used.add(y)
                backtrack()
                used.remove(y)
                del mapping[x]
    backtrack()
    result=sorted(result)
    assert len(result)==216==len(set(result))
    assert all(all((j in adj[i])==(g[j] in adj[g[i]]) for i in range(N) for j in range(N)) for g in result)
    return result

def gf2_rank(columns):
    pivots={}
    for v in columns:
        while v:
            k=v.bit_length()-1
            if k not in pivots:
                pivots[k]=v
                break
            v^=pivots[k]
    return len(pivots)

def homology_mod2(face_groups):
    boundary_rank={}
    for d in range(1,len(face_groups)):
        lower={m:i for i,m in enumerate(face_groups[d-1])}
        cols=[]
        for m in face_groups[d]:
            s=m
            col=0
            while s:
                a=s&-s
                col^=1<<lower[m^a]
                s-=a
            cols.append(col)
        boundary_rank[d]=gf2_rank(cols)
    betti=[len(x)-boundary_rank.get(d,0)-boundary_rank.get(d+1,0) for d,x in enumerate(face_groups)]
    assert betti==[1,0,0,0,10,0,0,0,0]
    return boundary_rank,betti

def inverse(g):
    v=[0]*N
    for i,j in enumerate(g):v[j]=i
    return tuple(v)

def compose(a,b):
    return tuple(a[b[i]] for i in range(N))

def vertex_cycles(g):
    unseen=set(range(N));cycles=[]
    while unseen:
        i=min(unseen); x=i; cyc=[]
        while x in unseen:
            unseen.remove(x);cyc.append(x);x=g[x]
        cycles.append(tuple(cyc))
    return cycles

def signed_chain_trace(g,groups):
    total=-1   # subtract the invariant H_0 line
    for d,faces in enumerate(groups):
        for mask in faces:
            a=[i for i in range(N) if mask&(1<<i)]
            b=[g[i] for i in a]
            if set(a)!=set(b):continue
            inv=sum(b[i]>b[j] for i in range(len(b)) for j in range(i+1,len(b)))
            total+=(-1)**(d+inv)
    return total

def cycle_subset_trace(g,face_set):
    cycles=vertex_cycles(g)
    eligible=[]
    for cyc in cycles:
        mask=sum(1<<x for x in cyc)
        if mask in face_set:
            eligible.append(mask)
    ans=-1
    for selection in range(1,1<<len(eligible)):
        mask=0
        ncyc=0
        for i,piece in enumerate(eligible):
            if selection&(1<<i):mask|=piece;ncyc+=1
        if mask in face_set:
            ans+=(-1)**(ncyc+1)
    return ans

def subgroup_generated(generators,table):
    H={0};front=[0]
    while front:
        a=front.pop()
        for b in generators:
            v=table[a][b]
            if v not in H:
                H.add(v);front.append(v)
    return H

def derived_subgroup(sub,table,invs):
    comm=set()
    for a in sub:
        for b in sub:
            comm.add(table[table[table[a][b]][invs[a]]][invs[b]])
    return subgroup_generated(comm,table)

def permutation_order(g):
    from math import lcm
    out=1
    for c in vertex_cycles(g):out=lcm(out,len(c))
    return out

def character_classes(group,table,invs,chi):
    unseen=set(range(len(group)));cls=[]
    while unseen:
        a=min(unseen)
        orbit=set(table[table[b][a]][invs[b]] for b in range(len(group)))
        assert orbit<=unseen
        assert len({chi[i] for i in orbit})==1
        cls.append(sorted(orbit));unseen-=orbit
    rows=[]
    for j,c in enumerate(cls,1):
        a=c[0];g=group[a]
        lengths=sorted(len(x) for x in vertex_cycles(g))
        rows.append((j,len(c),permutation_order(g),'.'.join(map(str,lengths)),chi[a],','.join(map(str,g))))
    assert len(rows)==13 and sum(r[1] for r in rows)==216
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--write-table',action='store_true')
    args=ap.parse_args()
    adj,nb=graph_data()
    faces=[m for m in range(1,1<<N) if is_independent(m,nb)]
    groups=[[m for m in faces if m.bit_count()==d+1] for d in range(9)]
    fvector=[len(x) for x in groups]
    assert fvector==[18,126,438,801,756,348,90,18,2]
    assert len(faces)==2597
    B,betti=homology_mod2(groups)
    reduced_euler=sum((-1)**d*f for d,f in enumerate(fvector))-1
    assert reduced_euler==10
    # Universal coefficients bound rational Betti numbers by mod-two Betti numbers.
    # Reduced Euler characteristic therefore forces rational H_4 dimension 10.
    group=automorphisms(adj);ids={g:i for i,g in enumerate(group)}
    assert group[0]==tuple(range(N))
    face_set=set(faces)
    chi=[signed_chain_trace(g,groups) for g in group]
    crosscheck=[cycle_subset_trace(g,face_set) for g in group]
    assert chi==crosscheck
    assert chi[0]==10
    table=[[ids[compose(a,b)] for b in group] for a in group]
    inverses=[ids[inverse(g)] for g in group]
    assert all(table[i][inverses[i]]==0 and table[inverses[i]][i]==0 for i in range(len(group)))
    classes=character_classes(group,table,inverses,chi)
    head='class\tsize\torder\tvertex_cycle_lengths\tchi_H4\trepresentative_images_0_to_17'
    text=head+'\n'+'\n'.join('\t'.join(map(str,row)) for row in classes)+'\n'
    table_path=Path(__file__).with_name('character_classes.tsv')
    if args.write_table:
        table_path.write_text(text,encoding='utf-8')
    assert table_path.read_text(encoding='utf-8')==text
    assert sum(chi)==0
    assert sum(c*c for c in chi)==432
    # These equations say there are precisely two different irreducible complex
    # constituents, each with multiplicity one.
    D1=derived_subgroup(set(range(len(group))),table,inverses)
    D2=derived_subgroup(D1,table,inverses)
    Z=derived_subgroup(D2,table,inverses)
    D4=derived_subgroup(Z,table,inverses)
    assert tuple(map(len,(D1,D2,Z,D4)))==(54,27,3,1)
    assert Z=={0,129,179}
    assert all(chi[i]==1 for i in Z if i!=0)
    # The projector (1+z+z^2)/3 has rank (10+1+1)/3=4.
    rank_fixed=sum(chi[i] for i in Z)//3
    assert rank_fixed==4
    rank_other=chi[0]-rank_fixed
    assert rank_other==6
    # Because Z is characteristic and the full complex character norm is two,
    # both nonzero Z-isotypic summands are absolutely irreducible.
    bp=[v for v in range(len(group)) if group[v][0]%2==0]
    # The LCF vertex labels have even/odd graph bipartition.
    assert all((u%2)!=(v%2) for u,v in EDGES)
    assert len(bp)==108 and sum(chi[i] for i in bp)==0
    r=tuple((i+6)%N for i in range(N))
    assert r in ids and chi[ids[r]]==-2
    print('PAPPUS_FULL_CHARACTER_EXACT_PASS')
    print('vertices=18 edges=27 automorphisms=216 classes=13')
    print('faces=2597 f_vector='+str(fvector))
    print('mod2_boundary_ranks='+str([B[d] for d in range(1,9)]))
    print('mod2_betti='+str(betti)+' rational_reduced_betti_degree_4=10')
    print('character_histogram='+str(sorted(Counter(chi).items())))
    print('character_sum=0 character_square_sum=432')
    print('derived_series_orders=216,54,27,3,1')
    print('normal_order3_fixed_dimensions=4,6 both_absolutely_irreducible=yes')
    print('full_group_invariants=0 bipartition_preserving_invariants=0')
    print('period_six_translation_trace=-2')
    print('character_table_exact_match=yes signed_vs_cycle_trace_216_match=yes')

if __name__=='__main__':main()
