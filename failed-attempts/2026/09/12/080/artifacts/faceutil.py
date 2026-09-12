def faces(rotA, rotB):
    na = len(rotA); nb = len(rotB)
    posA = [ {b:i for i,b in enumerate(rotA[a])} for a in range(na)]
    posB = [ {a:i for i,a in enumerate(rotB[b])} for b in range(nb)]
    visited = set()
    flist=[]
    for a in range(na):
        for b in range(nb):
            for direction in [0,1]:
                if direction==0:
                    u, v = ('A',a), ('B',b)
                else:
                    u, v = ('B',b), ('A',a)
                if (u,v) in visited: continue
                cur_u, cur_v = u, v
                cyc=[]
                while True:
                    visited.add((cur_u,cur_v))
                    cyc.append((cur_u,cur_v))
                    if cur_v[0]=='A':
                        a2 = cur_v[1]; b2 = cur_u[1]
                        idx = posA[a2][b2]
                        w = rotA[a2][(idx+1)%len(rotA[a2])]
                        nxt_u, nxt_v = cur_v, ('B',w)
                    else:
                        b2 = cur_v[1]; a2 = cur_u[1]
                        idx = posB[b2][a2]
                        w = rotB[b2][(idx+1)%len(rotB[b2])]
                        nxt_u, nxt_v = cur_v, ('A',w)
                    cur_u, cur_v = nxt_u, nxt_v
                    if (cur_u,cur_v)==(u,v):
                        break
                    if len(cyc)>100:
                        break
                flist.append(cyc)
    return flist

def face_lens(rotA, rotB):
    return sorted(len(f) for f in faces(rotA, rotB))

def is_quadrangulation(rotA, rotB):
    fl = faces(rotA, rotB)
    return len(fl)==16 and all(len(f)==4 for f in fl)

def genus(rotA, rotB):
    na=len(rotA); nb=len(rotB); E=na*nb
    F=len(faces(rotA,rotB)); V=na+nb
    return (2-V+E-F)//2
