import itertools,collections,math,sys,random,time

def get_complex(m):
    verts=[(i,j) for i in range(m) for j in range(i+1,m) if (j-i)%m not in (1,m-1)]
    V=len(verts)
    intersect=[[bool(set(verts[i])&set(verts[j])) for j in range(V)] for i in range(V)]
    faces=[(i,) for i in range(V)]
    for k in range(V):
        faces.extend([f+(k,) for f in faces[:] if f[-1]<k and all(intersect[i][k] for i in f)])
    faces=sorted(set(faces),key=lambda f:(len(f),f))
    fidx={f:i for i,f in enumerate(faces)}
    groups=[]
    for a in range(m):
        for sign in (1,-1):
            perm=[verts.index(tuple(sorted(((a+sign*i)%m,(a+sign*j)%m)))) for i,j in verts]
            groups.append(perm)
    fmap=[{fi:fidx[tuple(sorted(perm[x] for x in f))] for fi,f in enumerate(faces)} for perm in groups]
    return verts,faces,fmap

def flags_and_quotient(m,which='dihedral'):
    verts,faces,fmap=get_complex(m)
    if which=='cyclic': fmap=fmap[::2] # group list alternating orientation
    children=collections.defaultdict(list)
    for i,f in enumerate(faces):
        for s in range(len(f)-1):
            pass
        if len(f)>1:
            for sub in itertools.combinations(f,len(f)-1):children[faces.index(sub)].append(i)
    # by recursive extending chains using only inclusions by one size? flags may jump ranks!
    # all strict chains can jump. easier building for each face all subfaces arbitrary
    subfaces=[[] for _ in faces]
    F={f:i for i,f in enumerate(faces)}
    for i,f in enumerate(faces):
        for r in range(1,len(f)):
            subfaces[i].extend(F[t] for t in itertools.combinations(f,r))
    chaincache={}
    def ending(i):
        if i not in chaincache:
            chaincache[i]=[(i,)]+[ch+(i,) for j in subfaces[i] for ch in ending(j)]
        return chaincache[i]
    flags=sorted(set(ch for i in range(len(faces)) for ch in ending(i)),key=lambda t:(len(t),t))
    keys={}
    for fl in flags:
        key=min(tuple(mp[x] for x in fl) for mp in fmap)
        keys[key]=None
    orb=sorted(keys,key=lambda t:(len(t),t))
    C={o:i for i,o in enumerate(orb)}
    dimensions=collections.Counter(len(f)-1 for f in orb)
    boundary={}
    for j,fl in enumerate(orb):
        if len(fl)>1:
            b=collections.Counter()
            for r in range(len(fl)):
                newfl=fl[:r]+fl[r+1:]
                target=min(tuple(mp[x] for x in newfl) for mp in fmap)
                b[C[target]]+=(-1)**r
            boundary[j]={i:v for i,v in b.items() if v}
    return verts,faces,orb,boundary,dimensions

def collapse(orb,boundary):
    active=set(range(len(orb)))
    higher=collections.defaultdict(set)
    for j,b in boundary.items():
        for i,v in b.items(): higher[i].add(j)
    matches=[]
    while 1:
        candidates=[]
        for i,ups in higher.items():
            if i not in active:continue
            cur=[j for j in ups if j in active]
            if len(cur)==1 and abs(boundary[cur[0]].get(i,0))==1:
                candidates.append((len(orb[i]),i,cur[0]))
        if not candidates: break
        _,i,j=min(candidates, key=lambda a:(-a[0],a[1]))
        assert i in active and j in active
        active.remove(i);active.remove(j);matches.append((i,j))
    return active,matches

