# Settle F2 rank of ordered d1 exactly: sparse elimination over F2 on 24240x56040 (2 nnz/col) is cheap via union-find + cycle check.
# Left-null analysis above was muddled; do it carefully:
# A = incidence (rows 0-cells, cols 1-cells), each col has exactly one +1 and one -1 (over ZZ). Over F2, each col has two 1s (a loop? none: faces distinct? check loops: u!=v always since edge endpoints distinct, but f1,f2 as 0-cells could coincide? f1,f2 differ at position l (u vs v) => distinct. No loops.)
# rank_F2(A) = R - dim ker(A^T), ker(A^T) = {x in F2^R : x_a + x_b = 0 for every edge (a,b)} = {x constant on components} (since x_a=x_b). Connected => dim 1 => rank = R-1 = 24239. The odd-cycle subtlety I raised applies to a DIFFERENT matrix (unoriented incidence with one 1 per... ). For graph incidence with two 1s per column, left null = componentwise constants ALWAYS. So rank F2 = 24239 exactly. The union-find "bipartite" computation above is irrelevant to rank (it measures right-null structure). My printed formula line was wrong; correct: rank=24239.
# Verify no loops and connectivity already done (1 component). Also verify each column indeed has 2 distinct rows (no zero columns mod 2 from cancellation: +1/-1 at distinct rows => two 1s mod 2, fine).
print("rank d1 F2 = 24239 by left-null argument (connected, no loops).")
# Certify no loops:
import pickle, itertools
with open("mats.pkl","rb") as f:
    DM=pickle.load(f)
cells=DM["cells"]; edges=DM["edges"]
n=5
with open("collapse_state.pkl","rb") as f:
    S=pickle.load(f)
remaining=S["remaining"]
rem1=set(remaining[1])
nloops=0; ntot=0
for j in rem1:
    es,vs=cells[1][j]
    e=es[0]; u,v=edges[e]
    assert u!=v
    for l in range(n):
        for rest in itertools.permutations(vs):
            f1=[""]*n; f2=[""]*n
            ri=0
            for m in range(n):
                if m==l: continue
                f1[m]=rest[ri]; f2[m]=rest[ri]; ri+=1
            f1[l]=u; f2[l]=v
            ntot+=1
            if tuple(f1)==tuple(f2): nloops+=1
print("total cols",ntot,"loops",nloops)
