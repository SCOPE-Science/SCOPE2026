# PD toolkit: parse KnotAtlas PD (mixed "4251"/"5,12,6,13" tokens), Seifert circles.
# Convention: X[a,b,c,d], a=incoming under, cyclic order => strands a-c, b-d.
# Seifert (oriented) smoothing pairs in->out across strands: (a,d)&(b,c). Uniform.
from collections import defaultdict
PD820 = "X4251 X8493 X5,12,6,13 X13,16,14,1 X9,14,10,15 X15,10,16,11 X11,6,12,7 X2837"
def parse_pd(s):
    out=[]
    for tok in s.split('X'):
        tok=tok.strip()
        if not tok: continue
        if ',' in tok:
            nums=[int(x) for x in tok.split(',')]
        else:
            nums=[int(ch) for ch in tok.strip()]
        assert len(nums)==4, tok
        out.append(tuple(nums))
    return out
def seifert_circles(pd, pairing='ad_bc'):
    parent={}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(x,y):
        rx,ry=find(x),find(y)
        if rx!=ry: parent[rx]=ry
    for ci in range(len(pd)):
        for p in range(4):
            parent[(ci,p)]=(ci,p)
    pos=defaultdict(list)
    for ci,quad in enumerate(pd):
        for p,lbl in enumerate(quad):
            pos[lbl].append((ci,p))
    for lbl,occ in pos.items():
        assert len(occ)==2,(lbl,occ)
        union(occ[0],occ[1])
    for ci in range(len(pd)):
        if pairing=='ad_bc':
            union((ci,0),(ci,3)); union((ci,1),(ci,2))
        else:
            union((ci,0),(ci,1)); union((ci,2),(ci,3))
    return len(set(find(x) for x in parent))
if __name__=='__main__':
    pd=parse_pd(PD820)
    print("n=",len(pd))
    for p in ['ad_bc','ab_cd']:
        s=seifert_circles(pd,p)
        print(p,"s=",s,"cano_genus=",(2+len(pd)-s)/2)
