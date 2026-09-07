#!/usr/bin/env python3
"""P1: generating-tree DFS enumerator for Av(1234,1342) and Av(4231,4123).
Counts a_n for all n<=N in ONE traversal.
Node = avoider permutation of length k (values 0..k-1).
Children = k+1 extensions by last value v (renormalize prefix).
Incremental check: only quads (i<j<l<k) with new last element.
Lemma (exhaustively verified): quad (a,b,c,d) distinct is
  A-forbidden iff a==min AND (b<c<d OR d<b<c)
  B-forbidden iff a==max AND (b<c<d OR d<b<c)
"""
import sys, time, hashlib, json

def count_av(which, N, verbose=True):
    assert which in ('A','B')
    is_A = (which=='A')
    counts = [0]*(N+1)
    counts[0] = 1
    cur_level = [[]]
    for k in range(0, N):
        nxt = []
        t0=time.time()
        if is_A:
            for p in cur_level:
                for v in range(k+1):
                    if k==0:
                        nxt.append([v]); continue
                    q = [x+1 if x>=v else x for x in p]
                    q.append(v)
                    ok = True
                    if k>=3:
                        d = v
                        for i in range(k-2):
                            ai=q[i]
                            # quick: ai must be < d to possibly be min with d present?
                            # (need ai<d and ai<b,ai<c; check inside)
                            for j in range(i+1,k-1):
                                aj=q[j]
                                for l in range(j+1,k):
                                    a=ai; b=aj; c=q[l]
                                    if a<b and a<c and a<d:
                                        if b<c:
                                            if c<d:
                                                ok=False; break
                                            elif d<b:
                                                ok=False; break
                                if not ok: break
                            if not ok: break
                    if ok:
                        nxt.append(q)
        else:
            for p in cur_level:
                for v in range(k+1):
                    if k==0:
                        nxt.append([v]); continue
                    q = [x+1 if x>=v else x for x in p]
                    q.append(v)
                    ok = True
                    if k>=3:
                        d = v
                        for i in range(k-2):
                            ai=q[i]
                            for j in range(i+1,k-1):
                                aj=q[j]
                                for l in range(j+1,k):
                                    a=ai; b=aj; c=q[l]
                                    if a>b and a>c and a>d:
                                        if b<c:
                                            if c<d:
                                                ok=False; break
                                            elif d<b:
                                                ok=False; break
                                if not ok: break
                            if not ok: break
                    if ok:
                        nxt.append(q)
        counts[k+1]=len(nxt)
        if verbose:
            print(f"[{which}] n={k+1} count={len(nxt)} (level time {time.time()-t0:.2f}s)", flush=True)
        cur_level=nxt
        if not nxt:
            break
    return counts

if __name__=="__main__":
    which = sys.argv[1] if len(sys.argv)>1 else "A"
    N = int(sys.argv[2]) if len(sys.argv)>2 else 9
    t0=time.time()
    c=count_av(which,N)
    dt=time.time()-t0
    print(json.dumps({"class":which,"N":N,"counts":c,"seconds":round(dt,2)}))
    h=hashlib.sha256(json.dumps(c).encode()).hexdigest()[:16]
    print(f"checksum {h} total {dt:.1f}s", flush=True)
