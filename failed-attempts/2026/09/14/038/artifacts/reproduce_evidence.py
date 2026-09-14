# Write a single reproducible evidence script + run log capturing ALL target numbers deterministically.
import cypari2, datetime
pari = cypari2.Pari()
pari.allocatemem(600_000_000)
log = []
log.append("PARI " + str(pari("version()"))[:200])
def run(c):
    try:
        r = str(pari(c))
    except Exception as e:
        r = "ERR " + str(e)[:300]
    log.append(">>> " + c + "\n" + r[:4000])
cmds = [
 "mf=mfinit([42,2],1); mfdim(mf)",
 "mf=mfinit([42,2],1); B=mfbasis(mf); mfcoefs(B[5],20)",
 "mf=mfinit([42,2],1); [mfheckemat(mf,2)[5,5], mfheckemat(mf,3)[5,5], mfheckemat(mf,7)[5,5]]",
 "mf=mfinit([42,2],1); W2=mfatkininit(mf,2); W2[2][5,5]",
 "mf=mfinit([42,2],1); W3=mfatkininit(mf,3); W3[2][5,5]",
 "mf=mfinit([42,2],1); W7=mfatkininit(mf,7); W7[2][5,5]",
 "E=ellinit([1,1,1,-4,5]); ellglobalred(E)",
 "E=ellinit([1,1,1,-4,5]); ellrootno(E)",
 "E=ellinit([1,1,1,-4,5]); ellanalyticrank(E)",
 "E=ellinit([1,1,1,-4,5]); ellrank(E)",
 "E=ellinit([1,1,1,-4,5]); elltors(E)",
 "E=ellinit([1,1,1,-4,5]); ellmoddegree(E)",
 "E=ellinit([1,1,1,-4,5]); ED=ellinit(elltwist(E,-19)); ellglobalred(ED)",
 "E=ellinit([1,1,1,-4,5]); ED=ellinit(elltwist(E,-19)); ellrootno(ED)",
 "E=ellinit([1,1,1,-4,5]); ED=ellinit(elltwist(E,-19)); ellanalyticrank(ED)",
 "E=ellinit([1,1,1,-4,5]); ED=ellinit(elltwist(E,-19)); ellrank(ED)",
 "E=ellinit([1,1,1,-4,5]); ED=ellinit(elltwist(E,-19)); elltors(ED)",
 "E=ellinit([1,1,1,-4,5]); ED=ellinit(elltwist(E,-19)); [ellheegner(ED), ellheight(ED,ellheegner(ED))]",
 "E=ellinit([1,1,1,-4,5]); ED=ellinit(elltwist(E,-19)); ellisdivisible(ED,ellheegner(ED),2)",
 "default(realbitprecision, 128); mf=mfinit([42,2],1); B=mfbasis(mf); F=B[5]; L=lfunmf(mf,F); LK=lfuntwist(L,-19); [lfun(L,1), lfun(LK,1), lfun(LK,1,1), lfun(LK,1,2)]",
 "K=bnfinit(x^2+19); K.disc",
 "idealfactor(nfinit(x^2+19),2); idealfactor(nfinit(x^2+19),3); idealfactor(nfinit(x^2+19),7)",
 "qfbclassno(-19)",
]
for c in cmds:
    run(c)
open("output/artifacts/evidence_log.txt","w").write("\n\n".join(log) + "\n")
print("wrote evidence_log with", len(cmds), "commands")
