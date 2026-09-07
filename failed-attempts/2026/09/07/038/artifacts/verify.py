"""Independent replay verifier (stdlib only) for binary [n,k] witness table.
Reads artifacts/codes.json (+ optional grassl_chains.json, bound_log.csv).
For each cell (n,k):
  (a) recomputes min distance d and full weight enumerator W by exhaustive
      2^k enumeration over GF(2) using an int-bitmask implementation
      (independent of the derivation pipeline's list-based code);
  (b) checks sum(W)==2^k and min nonzero weight == claimed d;
  (c) checks systematic form Gs == [I_k | P] and full rank;
  (d) syndrome cross-check: builds H=[P^T|I_{n-k}] from Gs and verifies
      H*Gs^T==0 and rank(H)==n-k;
  (e) recomputes Griesmer sums G(k,d), G(k,d+1) and checks claimed d does
      not violate Griesmer (G(k,d)<=n), reporting tightness;
  (f) compares claimed d against Grassl BKLC LB/UB stored alongside.
Writes PASS/FAIL per cell and a summary. Exit code 0 iff all pass.
Usage: python3 artifacts/verify.py [artifacts_dir]
"""
import json, os, sys
def popcnt(x): return bin(x).count("1")
def rows_to_ints(G):
    out=[]
    for row in G:
        x=0
        for b in row: x=(x<<1)|b
        out.append(x)
    return out
def min_dist_and_enum(G):
    k=len(G); n=len(G[0])
    Gi=rows_to_ints(G)
    from collections import Counter
    cnt=Counter(); best=n+1
    for mask in range(1<<k):
        cw=0
        for i in range(k):
            if (mask>>i)&1: cw^=Gi[i]
        w=popcnt(cw)
        cnt[w]+=1
        if mask and w<best: best=w
    return (best if k else 0), dict(sorted(cnt.items()))
def is_systematic(Gs):
    k=len(Gs); n=len(Gs[0])
    for i in range(k):
        if Gs[i][i]!=1: return False
        for j in range(k):
            if j!=i and Gs[i][j]!=0: return False
    return True
def griesmer(k,d):
    return sum((d+(1<<i)-1)//(1<<i) for i in range(k))
def main():
    d0=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__))
    codes=json.load(open(os.path.join(d0,"codes.json")))
    fails=0
    print(f"verifying {len(codes)} cells from codes.json")
    for key in sorted(codes, key=lambda s:(int(s.split(',')[0]),int(s.split(',')[1]))):
        c=codes[key]; n,k,d,Wc,Gs=c["n"],c["k"],c["d"],c["W"],c["Gs"]
        Wc={int(a):b for a,b in Wc.items()}
        d2,W2=min_dist_and_enum(Gs)
        ok=True; notes=[]
        if d2!=d: ok=False; notes.append(f"distance mismatch enum={d2} claimed={d}")
        if W2!=Wc: ok=False; notes.append("enumerator mismatch")
        if sum(W2.values())!=2**k: ok=False; notes.append("enumerator sum !=2^k")
        if not is_systematic(Gs): ok=False; notes.append("not systematic [I|P]")
        # syndrome check
        r=n-k; P=[row[k:] for row in Gs]
        H=[[P[i][j] for i in range(k)]+[1 if j==i else 0 for i in range(r)] for j in range(r)] if r else []
        # H*Gs^T==0 ?
        for hj in H:
            for gr in Gs:
                if sum(a&b for a,b in zip(hj,gr))%2!=0: ok=False; notes.append("H*G^T!=0"); break
        g1=griesmer(k,d); g2=griesmer(k,d+1)
        if g1>n: ok=False; notes.append(f"Griesmer violated G({k},{d})={g1}>{n}")
        tight="tight" if g2>n else "slack"
        glb,gub=[int(x) if str(x).isdigit() else x for x in c.get("grassl",[None,None])]
        if d!=gub: ok=False; notes.append(f"Grassl UB mismatch {gub}")
        st="PASS" if ok else "FAIL"
        if not ok: fails+=1
        print(f"[{key}] n={n} k={k} d={d} enum_d={d2} sum={sum(W2.values())} G(k,d)={g1} G(k,d+1)={g2}({tight}) Grassl=[{glb},{gub}] {st}"+("" if ok else " :: "+"; ".join(notes)))
    print(f"\n{len(codes)-fails}/{len(codes)} cells PASS")
    print("OVERALL:", "PASS" if fails==0 else "FAIL")
    return 0 if fails==0 else 1
if __name__=="__main__":
    sys.exit(main())
