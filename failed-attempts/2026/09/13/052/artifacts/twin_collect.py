import sys; sys.path.insert(0,'.'); import json as J, time
sys.setrecursionlimit(100000)
from itertools import combinations
from pipeline2 import expand, pasches_limit, switch, maybe_iso, sig, P3, pid
t0=time.time()
asg='000111222'
Fof=[int(c) for c in asg]
fixcell=[[0]*9 for _ in range(3)]
for i,f in enumerate(Fof): fixcell[f][i]=1
m1col={}; nc=72
for f in range(3):
    for i in range(9):
        if not fixcell[f][i]: m1col[(f,i)]=nc; nc+=1
rows=[]
for f in range(3):
    F=18+f
    for i in range(9):
        for j in range(i+1,9):
            if fixcell[f][i] or fixcell[f][j]: continue
            for x in (2*i,2*i+1):
                for y in (2*j,2*j+1):
                    t=tuple(sorted((F,x,y))); s=tuple(sorted((sig(F),sig(x),sig(y))))
                    if t>s: continue
                    rows.append(([pid(x,y),m1col[(f,i)],m1col[(f,j)]],('MIX',t)))
for t in P3:
    rows.append(([pid(t[0],t[1]),pid(t[0],t[2]),pid(t[1],t[2])],('P3',t)))
col_rows=[[] for _ in range(nc)]
for ri,(cl,_) in enumerate(rows):
    for c in cl: col_rows[c].append(ri)
rowmask=[]
for cl,_ in rows:
    m=0
    for c in cl: m|=(1<<c)
    rowmask.append(m)
FULL=(1<<nc)-1
best=[]
nsys=[0]
def dfs(rem,chosen):
    if nsys[0]>=250: return True
    if rem==0:
        nsys[0]+=1
        mix=[rows[ri][1][1] for ri in chosen if rows[ri][1][0]=='MIX']
        p3=[rows[ri][1][1] for ri in chosen if rows[ri][1][0]=='P3']
        B=expand(Fof,mix,p3)
        n=len(pasches_limit(B,100))
        best.append((n,mix,p3))
        return False
    r=rem; bn=10**9; bo=None
    while r:
        lsb=r&(-r); c=lsb.bit_length()-1; r^=lsb
        opts=[ri for ri in col_rows[c] if rowmask[ri]&~rem==0]
        if not opts: return False
        if len(opts)<bn: bn=len(opts); bo=opts
        if bn<=1: break
    for ri in bo:
        chosen.append(ri)
        if dfs(rem&~rowmask[ri],chosen): return True
        chosen.pop()
    return False
dfs(FULL,[])
best.sort(key=lambda z:z[0])
print('systems:',nsys[0],'t=',round(time.time()-t0,1))
print('lowest pasch counts:',[b[0] for b in best[:8]])
J.dump([{'n':n,'mix':[list(t) for t in m],'p3':[list(t) for t in p]} for n,m,p in best[:6]], open('minsys.json','w'))
print('saved minsys.json')
