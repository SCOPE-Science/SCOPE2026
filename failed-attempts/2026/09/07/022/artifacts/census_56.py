#!/usr/bin/env python3
"""Generic generating-tree census for all 56 symmetry-distinct (4,4) pairs.
Uses canonical reps from symmetry_lemma (lex-min orbit rep), generic rank-code check.
Outputs equivalence blocks by sequence to n=10 (or N).
"""
import itertools, time, json, hashlib, sys

def build_group():
    def rev(q): return q[::-1]
    def comp(q,n=4): return tuple(n-1-x for x in q)
    def inv(q):
        r=[0]*len(q)
        for i,v in enumerate(q): r[v]=i
        return tuple(r)
    gens=[rev,comp,inv]
    perms=list(itertools.permutations(range(4)))
    def table(f): return tuple(f(p) for p in perms)
    tables={table(lambda q:q)}; flist=[lambda q:q]; queue=[lambda q:q]
    while queue:
        f=queue.pop()
        for g in gens:
            h=lambda q,f=f,g=g: g(f(q))
            t=table(h)
            if t not in tables:
                tables.add(t); flist.append(h); queue.append(h)
    return flist

G=build_group()
perms=list(itertools.permutations(range(4)))
# canonical distinct pairs
seen=set(); reps=[]
for i,a in enumerate(perms):
    for b in perms[i+1:]:
        if (a,b) in seen: continue
        orb=set()
        for g in G:
            x,y=g(a),g(b)
            if x>y: x,y=y,x
            orb.add((x,y))
        seen|=orb
        # lex-min rep
        reps.append(min(orb))
reps=sorted(reps)
print(f"canonical reps: {len(reps)}", flush=True)
assert len(reps)==56

def rankcode(a,b,c,d):
    # rank tuple packed as r0+4*r1+16*r2+64*r3 using comparisons (no sort)
    r0=(a>b)+(a>c)+(a>d)
    r1=(b>a)+(b>c)+(b>d)
    r2=(c>a)+(c>b)+(c>d)
    r3=(d>a)+(d>b)+(d>c)
    return r0+4*r1+16*r2+64*r3

def code_of(p):
    a,b,c,d=p
    # p is perm of 0..3, rank tuple is p itself (since values are ranks)
    return p[0]+4*p[1]+16*p[2]+64*p[3]

def count_pair(forb_codes, N):
    # forb: set of 2 ints
    counts=[0]*(N+1); counts[0]=1
    cur=[[]]
    for k in range(0,N):
        nxt=[]
        for p in cur:
            for v in range(k+1):
                if k==0:
                    nxt.append([v]); continue
                q=[x+1 if x>=v else x for x in p]
                q.append(v)
                ok=True
                if k>=3:
                    for i in range(k-2):
                        for j in range(i+1,k-1):
                            for l in range(j+1,k):
                                if rankcode(q[i],q[j],q[l],v) in forb_codes:
                                    ok=False; break
                            if not ok: break
                        if not ok: break
                if ok: nxt.append(q)
        counts[k+1]=len(nxt)
        cur=nxt
    return counts

if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 10
    t0=time.time()
    seqs={}
    for idx,(a,b) in enumerate(reps):
        fc={code_of(a),code_of(b)}
        c=count_pair(fc,N)
        key=tuple(c)
        seqs.setdefault(key,[]).append((a,b))
        print(f"{idx+1:02d}/56 pair {a} {b} -> {c[1:]}", flush=True)
    print(f"distinct sequences: {len(seqs)} in {time.time()-t0:.1f}s", flush=True)
    # block size distribution
    sizes=sorted([len(v) for v in seqs.values()],reverse=True)
    print("block sizes:",sizes)
    # find A and B blocks
    for key,members in seqs.items():
        s=list(key)
        if s[1:10]==[1,2,6,22,89,380,1678,7584,34875] or s[1:10]==[1,2,6,22,89,380,1677,7566,34676]:
            print("TARGET",s,members)
    # save
    out={"N":N,"n_distinct":len(seqs),
         "blocks":[{"counts":list(k),"size":len(v),"members":[list(m) for m in v]} for k,v in sorted(seqs.items(),key=lambda x:-len(x[1]))]}
    print(json.dumps({"N":N,"distinct":len(seqs),"block_sizes":sizes}))
    h=hashlib.sha256(json.dumps(out,sort_keys=True).encode()).hexdigest()[:16]
    print("checksum",h)
    with open("output/artifacts/census_56.json","w") as f:
        json.dump(out,f,indent=1)
    print("wrote output/artifacts/census_56.json")
