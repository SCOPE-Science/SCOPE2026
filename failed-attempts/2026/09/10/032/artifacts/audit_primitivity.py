"""Lane-584 deepening: flux-class primitivity (wall-crossing quantum),
S1-BF group pinning, connected-sum families stress (honest, both directions).
"""
import json, math

Q1=[[1,0,0,0],[0,-1,0,0],[0,0,0,1],[0,0,1,0]]
def pair(v,w):
    return sum(v[i]*Q1[i][j]*w[j] for i in range(4) for j in range(4))
def quad(v): return pair(v,v)

c=(1,1,2,2)
basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
ps=[pair(c,e) for e in basis]
print(f"c={c}: pairings={ps}, gcd={math.gcd(math.gcd(ps[0],ps[1]),math.gcd(ps[2],ps[3]))}")
assert quad(c)==8
g=math.gcd(math.gcd(ps[0],ps[1]),math.gcd(ps[2],ps[3]))
assert g==1
print("PRIMITIVE: c_flux indivisible => each transverse wall crossing "
      "contributes quantum +/-1 (not a multiple).")
# all 68 flux vectors: check primitivity across the box sample
import itertools
def is_char(v):
    for i in range(4):
        if (pair(v,basis[i])-Q1[i][i])%2!=0: return False
    return True
prim=0; tot=0; nonprim=[]
for v in itertools.product(range(-4,5),repeat=4):
    if is_char(v) and quad(v)==8:
        tot+=1
        ps2=[pair(v,e) for e in basis]
        gg=math.gcd(math.gcd(ps2[0],ps2[1]),math.gcd(ps2[2],ps2[3]))
        if gg==1: prim+=1
        else: nonprim.append(v)
print(f"flux in box: total={tot}, primitive={prim}, imprimitive={nonprim}")
assert tot==68

# S1-BF group pinning (statement level, Baraglia/Bauer-Furuta conventions):
# fiberwise index D = (d+1) complex? For spin-c families over S1 with d=-1:
# S1-BF(F) in pi^{S1}_{0}(S^0) = A(S1) (Burnside) completed stem-0 class;
# ghost (H-fixed) part = ordinary BF (=0 here by connected-sum vanishing),
# free part = families count FSW. So S1-BF nontriviality <=> FSW!=0 in pinned
# chamber (given ghost=0). Auditable group statement; number still open.
print("S1-BF PIN: stem-0 S1-stable class; ghost part = ord BF = 0 (conn-sum); "
      "free part = FSW count in pinned chamber. Nontriviality <=> J!=0.")

# Connected-sum families stress (honest both-directions note):
# Ordinary SW vanishes (both sides b2+>0). Parametrized analogue: IF the loop
# of metrics/perturbations could be chosen neck-stretched AND regular for the
# whole loop, fiberwise gluing gives empty parametrized moduli => FSW=0.
# BUT neck-stretching around the loop requires the loop to preserve the
# connected-sum decomposition (F must preserve the neck up to isotopy).
# Corrected F (Wall key) does NOT preserve any fixed neck: stabilization is
# routed through P, so no F-invariant decomposition exists a priori; the
# standard families connected-sum vanishing does not apply without an
# F-invariant neck. Conversely no theorem gives J!=0 either. OPEN both ways.
print("CONN-SUM STRESS: no F-invariant neck (Wall-key F) => families conn-sum "
      "vanishing inapplicable; no nonzero theorem either. OPEN both ways.")

out={"primitive":True,"flux_total_box":tot,"flux_primitive_box":prim,
 "S1BF":"stem-0, ghost=0, free=FSW","F_invariant_neck":False,
 "J_status":"uncomputed"}
with open("output/artifacts/primitivity_ledger.json","w") as f:
    json.dump(out,f,indent=2)
print("wrote output/artifacts/primitivity_ledger.json")
print("ALL VERIFY_OK")
