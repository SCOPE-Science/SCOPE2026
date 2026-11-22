#!/usr/bin/env python3
"""Reconstruct and check an exact finite homotopy certificate for a square cylinder."""
import itertools
import collections
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent

def mask(xs):
    return sum(1 << x for x in xs)

def unmask(n):
    return tuple(i for i in range(20) if n & (1 << i))

def graph():
    # Three open rows, four cyclic columns: the Cartesian graph P_3 square C_4.
    h = {tuple(sorted((4*r+c, 4*r+(c+1)%4))) for r in range(3) for c in range(4)}
    v = {tuple(sorted((4*r+c, 4*(r+1)+c))) for r in range(2) for c in range(4)}
    return sorted(h | v)

def enumerate_matchings(edges):
    nbrs = [[] for _ in range(12)]
    for idx, (a,b) in enumerate(edges):
        nbrs[a].append((b,idx)); nbrs[b].append((a,idx))
    def walk(unmatched, selected):
        if not unmatched:
            yield tuple(sorted(selected));return
        v = min(unmatched)
        for w,i in nbrs[v]:
            if w in unmatched:
                yield from walk(unmatched-{v,w}, selected+[i])
    return set(walk(set(range(12)),[]))

def enumerate_brute(edges):
    expected = (1 << 12)-1
    out = set()
    for candidate in itertools.combinations(range(20),6):
        used=0
        for idx in candidate:
            a,b=edges[idx]
            val=(1 << a)|(1 << b)
            if used & val: break
            used |= val
        else:
            if used==expected:out.add(candidate)
    return out

def make_faces(facets):
    out=set()
    for f in facets:
        for k in range(1,len(f)+1):
            out.update(itertools.combinations(f,k))
    return out

def find_pairs(faces):
    cofaces=collections.Counter();unique={}
    for face in faces:
        if len(face)<2:continue
        for sub in itertools.combinations(face,len(face)-1):
            if sub in faces:
                cofaces[sub]+=1;unique[sub]=face
    return cofaces,unique

def produce_collapses(faces):
    faces=set(faces); steps=[]
    while True:
        counts,coface=find_pairs(faces)
        eligible=[(len(s),s,coface[s]) for s,c in counts.items() if c==1]
        if not eligible:break
        _,s,f=max(eligible)
        steps.append([mask(s),mask(f)])
        faces.remove(s);faces.remove(f)
    return steps,faces

def apply_collapses(initial,steps):
    faces=set(initial)
    for i,(s0,f0) in enumerate(steps):
        s=unmask(s0);f=unmask(f0)
        assert len(f)==len(s)+1 and set(s)<set(f), ('not codimension one',i)
        assert s in faces and f in faces, ('missing face',i)
        counts,unique=find_pairs(faces)
        assert counts.get(s,0)==1 and unique[s]==f, ('not free',i)
        faces.remove(s);faces.remove(f)
    counts,_=find_pairs(faces)
    assert not any(c==1 for c in counts.values()), 'claimed complete collapse is incomplete'
    return faces

def spanning_tree(edges,verts):
    root=min(verts); seen={root}; queue=[root]; tree=[]
    for u in queue:
        for a,b in edges:
            if u!=a and u!=b:continue
            w=b if u==a else a
            if w not in seen:
                seen.add(w);queue.append(w);tree.append((a,b))
    assert seen==set(verts)
    return tree

def presentation(faces,tree):
    edges=sorted(f for f in faces if len(f)==2)
    triangles=sorted(f for f in faces if len(f)==3)
    index={e:i+1 for i,e in enumerate(e for e in edges if e not in set(tree))}
    words={mask(t):[] for t in triangles}
    for triangle in triangles:
        a,b,c=triangle
        for x,y in [(a,b),(b,c),(c,a)]:
            e=tuple(sorted((x,y)))
            if e in index: words[mask(triangle)].append(index[e] if x<y else -index[e])
    return index,words

def produce_kills(words,index):
    words={k:list(v) for k,v in words.items()};kills=[]
    while any(words.values()):
        options=sorted((k,v[0]) for k,v in words.items() if len(v)==1)
        if not options:raise AssertionError('cannot eliminate all circle generators')
        face,letter=options[0];kills.append([face,abs(letter)])
        del words[face]
        for key,word in words.items():
            words[key]=[x for x in word if abs(x)!=abs(letter)]
    assert len(kills)==len(index), (len(kills),len(index))
    return kills,words

def apply_kills(words,index,kills):
    words={k:list(v) for k,v in words.items()}
    alive=set(index.values())
    for i,(face,g) in enumerate(kills):
        assert face in words, ('missing relator',i)
        assert len(words[face])==1 and abs(words[face][0])==g, ('not primitive single generator',i)
        assert g in alive, ('generator already eliminated',i)
        del words[face];alive.remove(g)
        for key,word in words.items():
            words[key]=[x for x in word if abs(x)!=g]
    assert not alive and len(words)==11 and all(not w for w in words.values())
    return len(words)

def modular_rank(columns,p):
    pivot={};rank=0
    for col in columns:
        v=dict((k,int(x)%p) for k,x in col.items() if x%p)
        while v:
            k=min(v)
            if k not in pivot:
                inv=pow(v[k],-1,p)
                pivot[k]={j:(t*inv)%p for j,t in v.items()}
                rank+=1;break
            fac=v[k];d=pivot[k]
            for j,t in d.items():
                value=(v.get(j,0)-fac*t)%p
                if value:v[j]=value
                elif j in v:del v[j]
    return rank

def verify(certificate):
    edges=graph()
    assert len(edges)==20
    facets=enumerate_matchings(edges)
    assert facets==enumerate_brute(edges) and len(facets)==32
    initial=make_faces(facets)
    assert len(initial)==1196
    fvec=[sum(len(f)==n for f in initial) for n in range(1,7)]
    assert fvec==[20,142,392,418,192,32],fvec
    steps=certificate['collapses']
    assert len(steps)==526
    final=apply_collapses(initial,steps)
    assert [sum(len(f)==n for f in final) for n in range(1,4)]==[18,66,60]
    assert all(len(f)<=3 for f in final)
    verts=[f[0] for f in final if len(f)==1]
    one=sorted(f for f in final if len(f)==2)
    tree=spanning_tree(one,verts)
    assert len(tree)==17
    assert [[a,b] for a,b in tree]==certificate['tree_edges']
    gen,relators=presentation(final,tree)
    assert len(gen)==49 and len(relators)==60
    two_cell_left=apply_kills(relators,gen,certificate['relator_kills'])
    assert len(certificate['relator_kills'])==49
    for p in [2,3,5,7]:
        rows={f:i for i,f in enumerate(one)}
        cols=[]
        for t in sorted(f for f in final if len(f)==3):
            col={}
            for i in range(3):
                s=t[:i]+t[i+1:]
                col[rows[s]]=1 if i%2==0 else -1
            cols.append(col)
        assert modular_rank(cols,p)==49, ('modular rank',p)
    assert 18-66+60==1+two_cell_left==12
    assert sum((-1)**(len(f)-1) for f in initial)==12
    print('GRAPH vertices=12 edges=20; FACETS=32 (two independent enumerations)')
    print('F_VECTOR',fvec,'NONEMPTY_FACES',len(initial))
    print('FREE_FACE_COLLAPSES',len(steps),'RESIDUAL_F_VECTOR',[18,66,60])
    print('BFS_TREE_EDGES',len(tree),'NON_TREE_GENERATORS',len(gen),'TRIANGLE_RELATORS',len(relators))
    print('SINGLE_LETTER_RELATOR_ELIMINATIONS',len(certificate['relator_kills']))
    print('FINAL_2_CELLS',two_cell_left,'H2_RANK',two_cell_left,'PI1_TRIVIAL',True)
    print('MODULAR_BOUNDARY_RANKS',[(p,49) for p in [2,3,5,7]])
    print('HOMOTOPY_TYPE_WEDGE_11_S2_CERTIFIED')

if __name__ == '__main__':
    facets=enumerate_matchings(graph());initial=make_faces(facets)
    if len(sys.argv)>1 and sys.argv[1]=='--make-certificate':
        pairs,final=produce_collapses(initial)
        vert=[f[0] for f in final if len(f)==1]
        one=sorted(f for f in final if len(f)==2)
        tree=spanning_tree(one,vert)
        index,relators=presentation(final,tree)
        kills,_=produce_kills(relators,index)
        doc={'collapses':pairs,'tree_edges':[list(x) for x in tree],'relator_kills':kills}
        (ROOT/'certificate.json').write_text(json.dumps(doc,separators=(',',':'))+'\n',encoding='utf-8')
    verify(json.loads((ROOT/'certificate.json').read_text(encoding='utf-8')))
