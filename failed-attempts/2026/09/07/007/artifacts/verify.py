#!/usr/bin/env python3
"""Standalone brute-force verifier for RT(30,K4,6) witness.
Reads adjacency matrix (space-separated 0/1, 30x30) from given file.
Checks: symmetric, zero diag, K4-free (27405 quads), alpha<=5 (593775 6-sets).
Prints edge count, max degree, degree sequence.
"""
import itertools, sys

def load(path):
    M=[]
    with open(path) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            if " " in line:
                row=list(map(int,line.split()))
            else:
                row=list(map(int,list(line.strip())))
            M.append(row)
    assert len(M)==30 and all(len(r)==30 for r in M), f"bad shape {len(M)}"
    return M

def main(path):
    M=load(path)
    n=30
    for i in range(n):
        assert M[i][i]==0, "nonzero diag"
        for j in range(n):
            assert M[i][j]==M[j][i], "asymmetric"
            assert M[i][j] in (0,1)
    e=sum(sum(r) for r in M)//2
    degs=sorted([sum(r) for r in M],reverse=True)
    print(f"edges={e} maxdeg={degs[0]} mindeg={degs[-1]} degseq={degs}")
    # K4
    k4c=0
    for quad in itertools.combinations(range(n),4):
        a,b,c,d=quad
        if M[a][b] and M[a][c] and M[a][d] and M[b][c] and M[b][d] and M[c][d]:
            print(f"K4 FOUND {quad}"); return False
        k4c+=1
    print(f"K4 check passed ({k4c} quadruples)")
    # alpha
    ac=0
    for s in itertools.combinations(range(n),6):
        indep=True
        for ii in range(6):
            for jj in range(ii+1,6):
                if M[s[ii]][s[jj]]:
                    indep=False; break
            if not indep: break
        if indep:
            print(f"I6 FOUND {s}"); return False
        ac+=1
    print(f"alpha<=5 check passed ({ac} 6-sets)")
    print(f"VERIFIED: K4-free and alpha<=5, e={e}")
    return True

if __name__=="__main__":
    ok=main(sys.argv[1] if len(sys.argv)>1 else "output/artifacts/best_adj.txt")
    sys.exit(0 if ok else 1)
