"""Bounded fallback attempts for lane-619 preset fallback:
Hom(O(E),E)=0 for mu-stable E of class v=(2,H,2), h0>=6.
F1 slope | F2 h0-bound analysis | F3 exact-sequence forcing (off-by-one)
| F4 Serre-construction counterexample feasibility count.
"""
print("== F1 slopes ==")
print("mu(O(E)) = E.H = 5 < 7 = H^2/2 = mu(E): nonzero maps allowed. FAILED route.")

print("== F2 h0(I_Z(H-E)) <= 4 ? ==")
print("chi(O(H-E)) = (H-E)^2/2+2 =", (14-10+0)/2+2)
print("(E-H).H = -9 <0 so h0(O(E-H))=0 (H ample).")
print("Hence h0(O(H-E)) >= chi = 4, and h0(O(H-E)) = 4 + h1(O(H-E)).")
print("Upper bound <=4 needs h1(O(H-E))=0.")
print("(H-E)^2 = 4 >0 and H-E effective (h0>=4) => H-E big (Zariski: P^2>0).")
print("But Kawamata-Viehweg needs NEF+big; nefness of H-E unproven from hypotheses")
print("(needs negative-curve classification vs BN-generality: unbounded). BLOCKED.")

print("== F3 exact-sequence forcing, granting <=4 hypothetically ==")
print("Nonzero φ:O(E)->E injective (ker torsion in line bundle => 0);")
print("coker = I_Z(H-E), len Z = c2 - E.(H-E) = 7-5 = 2.")
print("0->O(E)->E->I_Z(H-E)->0 gives h0(E) <= h0(O(E)) + h0(I_Z) = 2+4 = 6.")
print("h0>=6 compatible via equality (h0(E)=6, h0(I_Z)=4). OFF-BY-ONE:")
print("the criterion's own <=4 route cannot contradict h0>=6.")
print("Closing needs <=3, i.e. |H-E| base-point-free, i.e. Reider + Picard control: absent.")
print("Also Clifford check: excess shape gives gamma=7-2*(6/2-1)=3 = Cliff_1 (genus 8 BN-general);")
print("no Clifford contradiction either. BLOCKED with proof of insufficiency.")

print("== F4 counterexample-triple (Serre construction) feasibility ==")
print("Ext^1(I_Z(H-E),O(E)): chi=-<b,a>=-3; hom=H0(O(2E-H))=0 (H-deg -4);")
print("so ext^1 >= 3, PExt dim >= 2: extensions exist as sheaves.")
print("Need: Z in Bs|H-E| (base locus UNKNOWN from hypotheses) + mu-stability check")
print("(needs Picard knowledge: rule out D with D.H>=7 injecting) + h0(E)=6.")
print("No explicit BN-general genus-8 K3 equations available; excess existence is the open")
print("problem itself. INFEASIBLE in bounded time. BLOCKED.")
print("ALL FALLBACK CHECKS DONE")
