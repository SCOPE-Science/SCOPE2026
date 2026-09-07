#!/usr/bin/env python3
"""Independent replay verifier for isotopy-stratified transversal census.
Reads ONLY squares.csv, transversals.csv, partial.csv from same directory.
Checks (stdlib only):
 1. Every matrix in squares.csv is Latin (rows/cols are perms of 0..n-1).
 2. Every witness in transversals.csv has n cells, distinct rows/cols/syms, symbols match matrix.
 3. Every witness in partial.csv has tau cells, distinct rows/cols/syms, symbols match matrix.
 4. Independently recounts N for each DISTINCT matrix named in transversals/partial
    via itertools.permutations (algorithmically independent of census DFS) and
    checks claimed N/tau (tau==n iff N>0; transversal-free tau==n-1).
Usage: python3 verifier.py [--dir DIR]
Exit 0 on success, nonzero with message on failure.
"""
import csv, os, sys, itertools, argparse

def parse_matrix(s, n):
    rows = s.split("|")
    assert len(rows)==n, f"expected {n} rows got {len(rows)}"
    M=[]
    for r in rows:
        vals=[int(x) for x in r.strip().split()]
        assert len(vals)==n, f"row len {len(vals)} != {n}"
        M.append(vals)
    return M

def parse_cells(s):
    s=s.strip()
    if not s: return []
    cells=[]
    for tok in s.split(";"):
        a,b,c=tok.split(",")
        cells.append((int(a),int(b),int(c)))
    return cells

def is_latin(M):
    n=len(M); tgt=set(range(n))
    for i in range(n):
        if set(M[i])!=tgt: return False
    for j in range(n):
        if set(M[i][j] for i in range(n))!=tgt: return False
    return True

def check_transversal(M, cells):
    n=len(M)
    if len(cells)!=n: return False, f"len {len(cells)} != n {n}"
    rs=[r for r,_,_ in cells]; cs=[c for _,c,_ in cells]; ss=[s for _,_,s in cells]
    if len(set(rs))!=n: return False, "rows not distinct"
    if len(set(cs))!=n: return False, "cols not distinct"
    if len(set(ss))!=n: return False, "syms not distinct"
    if set(rs)!=set(range(n)) or set(cs)!=set(range(n)) or set(ss)!=set(range(n)):
        return False, "not covering 0..n-1"
    for (r,c,s) in cells:
        if not (0<=r<n and 0<=c<n and 0<=s<n): return False, "out of range"
        if M[r][c]!=s: return False, f"cell {(r,c,s)} mismatches M={M[r][c]}"
    return True, "ok"

def check_partial(M, cells, tau):
    n=len(M)
    if len(cells)!=tau: return False, f"len {len(cells)} != tau {tau}"
    rs=[r for r,_,_ in cells]; cs=[c for _,c,_ in cells]; ss=[s for _,_,s in cells]
    if len(set(rs))!=len(rs): return False, "rows not distinct"
    if len(set(cs))!=len(cs): return False, "cols not distinct"
    if len(set(ss))!=len(ss): return False, "syms not distinct"
    for (r,c,s) in cells:
        if not (0<=r<n and 0<=c<n and 0<=s<n): return False, "out of range"
        if M[r][c]!=s: return False, f"cell {(r,c,s)} mismatches M={M[r][c]}"
    return True, "ok"

def count_N_perm(M):
    n=len(M); cnt=0
    for perm in itertools.permutations(range(n)):
        if len({M[r][perm[r]] for r in range(n)})==n:
            cnt+=1
    return cnt

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--dir",default=os.path.dirname(os.path.abspath(__file__)))
    a=ap.parse_args(); d=a.dir
    sq_path=os.path.join(d,"squares.csv"); tr_path=os.path.join(d,"transversals.csv"); pa_path=os.path.join(d,"partial.csv")
    for p in [sq_path,tr_path,pa_path]:
        assert os.path.exists(p), f"missing {p}"
    # load squares: map sq_id/rep_id -> (n, matrix). squares.csv has all 186 with rep_id column.
    mats={}  # id -> (n,M)
    rep_of={}
    n_trans=0
    with open(sq_path) as f:
        r=csv.DictReader(f)
        assert set(r.fieldnames)>= {"sq_id","stratum","n","rep_id","matrix"}, f"bad header {r.fieldnames}"
        for row in r:
            n=int(row["n"]); M=parse_matrix(row["matrix"],n)
            if not is_latin(M):
                print(f"FAIL: {row['sq_id']} not Latin"); return 1
            mats[row["sq_id"]]=(n,M); rep_of[row["sq_id"]]=row["rep_id"]
            # also index rep_id matrix (base rows equal rep matrix)
            if row["rep_id"] not in mats:
                mats[row["rep_id"]]=(n,M)
            n_trans+=1
    print(f"squares.csv: {n_trans} Latin squares verified.")
    # transversals
    ntr=0
    with open(tr_path) as f:
        r=csv.DictReader(f)
        for row in r:
            rep=row["rep_id"]; n=int(row["n"]); N=int(row["N"]); tau=int(row["tau"])
            assert rep in mats, f"unknown rep {rep}"
            nn,M=mats[rep]
            assert nn==n, f"n mismatch {rep}"
            cells=parse_cells(row["witness"])
            ok,msg=check_transversal(M,cells)
            if not ok:
                print(f"FAIL transversal {rep}: {msg}"); return 1
            # independent recount
            N2=count_N_perm(M)
            if N2!=N:
                print(f"FAIL transversal {rep}: claimed N={N} recount={N2}"); return 1
            if tau!=n:
                print(f"FAIL transversal {rep}: tau {tau} != n {n} despite N>0"); return 1
            if N<=0:
                print(f"FAIL transversal {rep}: N<=0 but listed as transversal"); return 1
            print(f"transversal {rep}: n={n} N={N} recount={N2} witness OK.")
            ntr+=1
    # partials (transversal-free)
    npa=0
    with open(pa_path) as f:
        r=csv.DictReader(f)
        for row in r:
            rep=row["rep_id"]; n=int(row["n"]); tau=int(row["tau"]); N=int(row["N"])
            assert rep in mats, f"unknown rep {rep}"
            nn,M=mats[rep]
            assert nn==n
            cells=parse_cells(row["witness"])
            ok,msg=check_partial(M,cells,tau)
            if not ok:
                print(f"FAIL partial {rep}: {msg}"); return 1
            N2=count_N_perm(M)
            if N2!=0 or N!=0:
                print(f"FAIL partial {rep}: expected N=0 got claimed {N} recount {N2}"); return 1
            if tau!=n-1:
                print(f"FAIL partial {rep}: transversal-free tau={tau} expected n-1={n-1}"); return 1
            print(f"partial {rep}: n={n} tau={tau} N=0 recount=0 witness OK (maximal: n-1 with no full transversal).")
            npa+=1
    print(f"ALL CHECKS PASSED: {n_trans} squares Latin, {ntr} transversal witnesses, {npa} partial witnesses, independent N recounts match.")
    return 0

if __name__=="__main__":
    sys.exit(main())
