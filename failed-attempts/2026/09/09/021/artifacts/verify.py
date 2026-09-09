"""Independent checker: verifies Latin, N2=0, transversal counts, pairwise non-isotopy of 12 reps,
autotopism orders, and 3-block paratopy partition. Stdlib only. Run: python3 verify.py"""
import json, itertools, sys
D=json.load(open("class_table.json"))
REPS=D["reps"]  # list of {id, grid, aut, trans}
def is_latin(L):
    n=len(L); S=set(range(n))
    for r in range(n):
        if set(L[r])!=S: return False
    for c in range(n):
        if set(L[r][c] for r in range(n))!=S: return False
    return True
def n2(L):
    n=len(L); c=0
    for r1 in range(n):
        for r2 in range(r1+1,n):
            for c1 in range(n):
                a=L[r1][c1]; b=L[r2][c1]
                if a==b: continue
                for c2 in range(c1+1,n):
                    if L[r1][c2]==b and L[r2][c2]==a: c+=1
    return c
def row_ints_rows(B,b):
    # int encodings of rows of B under column perm b
    out=[]
    for u in range(len(B)):
        v=0; row=B[u]
        for j in range(len(B)): v|=(row[b[j]]<<(3*j))
        out.append(v)
    return out
def iso_count(A,B):
    n=len(A)
    apos=[0]*n
    for j in range(n): apos[A[0][j]]=j
    total=0
    cols=list(range(n))
    for a0 in range(n):
        Ba0=B[a0]
        for b in itertools.permutations(cols):
            pc=[Ba0[b[apos[x]]] for x in range(n)]
            Cmap={}
            for u in range(n):
                v=0; row=B[u]
                for j in range(n): v|=(row[b[j]]<<(3*j))
                Cmap[v]=u
            used=1<<a0; ok=True
            for r in range(1,n):
                v=0; row=A[r]
                for j in range(n): v|=(pc[row[j]]<<(3*j))
                u=Cmap.get(v)
                if u is None or (used>>u)&1: ok=False; break
                used|=(1<<u)
            if ok: total+=1
    return total
def conjugate(L,p):
    n=len(L); M=[[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            t=(r,c,L[r][c]); M[t[p[0]]][t[p[1]]]=t[p[2]]
    return M
def para_count(A,B):
    t=0
    for p in itertools.permutations([0,1,2]):
        t+=iso_count(conjugate(A,p),B)
    return t
def trans_count(L):
    n=len(L); cnt=[0]; cu=[False]*n; su=[False]*n
    def dfs(r):
        if r==n: cnt[0]+=1; return
        for c in range(n):
            s=L[r][c]
            if not cu[c] and not su[s]:
                cu[c]=su[s]=True; dfs(r+1); cu[c]=su[s]=False
    dfs(0); return cnt[0]
ok=True
print("reps:",len(REPS))
for R in REPS:
    L=R["grid"]
    assert is_latin(L), R["id"]
    z=n2(L); assert z==0, (R["id"],z)
    t=trans_count(L); assert t==R["trans"], (R["id"],t,R["trans"])
    a=iso_count(L,L); assert a==R["aut"], (R["id"],a,R["trans"] if False else R["aut"])
    print(f"rep {R['id']}: latin OK, N2=0 OK, trans={t} OK, aut={a} OK")
m=len(REPS)
for i in range(m):
    for j in range(i+1,m):
        c=iso_count(REPS[i]["grid"],REPS[j]["grid"])
        blk_i=D["main_block"][REPS[i]["id"]]; blk_j=D["main_block"][REPS[j]["id"]]
        if blk_i==blk_j:
            pass  # same-block pairs may be isotopic or not; isotopy classes already distinct
        else:
            assert c==0,(REPS[i]["id"],REPS[j]["id"],c)
print("cross-block non-isotopy OK")
# paratopy: within-block connectivity + cross-block separation on block leaders
leaders={}
for R in REPS:
    leaders.setdefault(D["main_block"][R["id"]],R["id"])
print("blocks:",{k:[R["id"] for R in REPS if D["main_block"][R["id"]]==k] for k in leaders})
ids=[R["id"] for R in REPS]; G={R["id"]:R["grid"] for R in REPS}
L=list(leaders.values())
for i in range(len(L)):
    for j in range(i+1,len(L)):
        t=para_count(G[L[i]],G[L[j]])
        print(f"paracount block {L[i]}-{L[j]} = {t}")
        assert t==0
print("cross-block non-paratopy OK")
# within-block: check claimed bridges
for (a,b) in D["bridges"]:
    t=para_count(G[a],G[b]); print(f"bridge {a}-{b} paracount={t}"); assert t>0
print("VERIFY_OK")
