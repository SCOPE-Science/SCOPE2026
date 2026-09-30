# CORRECT slice: pairs (x in C0, y in C1) with x*y = z^{-1} (so (x,y,z) satisfies xyz=1). Contains our triple.
import json, itertools
N=12
def compose(a,b): return [b[a[i]] for i in range(len(a))]
def inv(a):
    b=[0]*len(a)
    for i,v in enumerate(a): b[v]=i
    return b
def ctype(p):
    s=[False]*N; t=[]
    for i in range(N):
        if not s[i]:
            j=i;c=[]
            while not s[j]: s[j]=True;c.append(j);j=p[j]
            if len(c)>1: t.append(len(c))
    t=sorted(t,reverse=True); t+=[1]*(N-sum(t)); return tuple(sorted(t,reverse=True))
d=json.load(open("triple.json"))
z=d["vinf"]; zi=inv(z)
pairs=[]
pts=list(range(N))
for q4 in itertools.combinations(pts,4):
    q4s=set(q4); rest=[p for p in pts if p not in q4s]
    m=min(q4); others=[p for p in q4 if p!=m]
    for a,b,c in itertools.permutations(others):
        for q2 in itertools.combinations(rest,2):
            xinv=list(range(N))
            xinv[a]=m; xinv[b]=a; xinv[c]=b; xinv[m]=c
            xinv[q2[0]]=q2[1]; xinv[q2[1]]=q2[0]
            y=[zi[xinv[i]] for i in range(N)]
            if ctype(y)==(5,4,3):
                x=list(range(N))
                x[m]=a; x[a]=b; x[b]=c; x[c]=m
                x[q2[0]]=q2[1]; x[q2[1]]=q2[0]
                pairs.append([x,y])
print("npairs:",len(pairs))
# our triple present?
ox,oy=d["v0"],d["v1"]
print("our pair present:", [ox,oy] in pairs)
# C(z)-orbits (centralizer fixes z hence zinv too)
seen=[False]*N; cycs=[]
for i in range(N):
    if not seen[i]:
        j=i;c=[]
        while not seen[j]: seen[j]=True;c.append(j);j=z[j]
        if len(c)>1: cycs.append(c)
def cyc_perm(c):
    p=list(range(N))
    for i in range(len(c)): p[c[i]]=c[(i+1)%len(c)]
    return p
gens=[cyc_perm(c) for c in cycs]
els={tuple(range(N))}; stack=[list(range(N))]
while stack:
    h=stack.pop()
    for g in gens:
        for k in (compose(h,g),compose(h,inv(g))):
            t=tuple(k)
            if t not in els: els.add(t); stack.append(k)
els=[list(e) for e in els]
def conj(p,g): return compose(compose(inv(g),p),g)
Tp=[(tuple(x),tuple(y)) for (x,y) in pairs]
key_of={p:i for i,p in enumerate(Tp)}
assign=[-1]*len(Tp); norb=0; reps=[]
for i in range(len(Tp)):
    if assign[i]>=0: continue
    assign[i]=norb; stack=[i]
    while stack:
        j=stack.pop()
        x,y=Tp[j]
        for g in els:
            k=key_of.get((tuple(conj(list(x),g)),tuple(conj(list(y),g))))
            if k is not None and assign[k]<0:
                assign[k]=norb; stack.append(k)
    reps.append([list(Tp[i][0]),list(Tp[i][1])]); norb+=1
def trans(x,y):
    xi,yi=inv(list(x)),inv(list(y))
    seen=[False]*N; st=[0]; seen[0]=True
    while st:
        i=st.pop()
        for nb in (x[i],y[i],xi[i],yi[i]):
            if not seen[nb]: seen[nb]=True; st.append(nb)
    return all(seen)
flags=[trans(x,y) for (x,y) in reps]
print("nclasses:",norb,"transitive:",sum(flags))
our_idx=key_of[(tuple(ox),tuple(oy))]
print("our class:",assign[our_idx])
json.dump({"pairs":pairs,"assign":assign,"reps":reps,"trans":flags,"our_idx":our_idx,"our_class":assign[our_idx]},
          open("nielsen_correct.json","w"))
print("wrote nielsen_correct.json")
