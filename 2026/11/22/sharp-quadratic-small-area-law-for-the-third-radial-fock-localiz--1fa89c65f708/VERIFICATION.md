---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The coordinate t=pi|z|^2 converts area to length and radiality diagonalizes the localization operator with weights f_j=e^(-t)t^j/j!. The j>=3 peaks decrease, with maximum 9/(2e^3)<c, so above that times s the ordered third eigenvalue is the minimum of L_0,L_1,L_2. The dual h=cf_0+(1-c)f_2 attains c only at 0 and tau; this follows from the signs of h' around the two roots 2-tau and tau. To justify strictness for the supremum (not just individual masks), set g=c-h. Its tail limit is positive and its zero set has measure zero, so for each fixed s choose eta>0 with |{g<eta}|<s/2. Every mask then has integral_E g>=eta s/2, and combining this with the high-mode cutoff gives M_3(s)<cs. In the two-band construction the central piece loses p^2 s^2/2 in L_0, L_2 has no central term at that order, and the annulus has no first-moment term about tau. The adjustment p_s=p+p^2 s/[2(1-A+B)] balances both to cs-cp^2s^2/2+O(s^3), while L_1/s tends to 2c/tau>c. Conversely the dual deficit of near maximizers gives two-point concentration and the L_2 mass fixes the central fraction p. Since g(t)/t tends to c at zero, bathtub rearrangement forces at least cp^2s^2/2+o(s^2) loss. For F near zero of measure m, moving the missing length d=|F triangle [0,m]|/2 to the right of m costs at least d^2 in first moment. Saturation of the coefficient, followed by taking the small neighborhood smaller and using o(s) mass in the intervening fixed annulus, yields the scaled central-disk assertion. Independent high-precision values tau=1.59362426004004009, c=0.24460180302352822, p=0.05197452634475800 give the stated coefficient.

## originality

PASS

The dual peak certificate, leading slope, two-radius split, disk-plus-ring geometry and weak concentration are prior. The supported distinct contribution is the sharp second-order deficit for the ordered third radial eigenvalue, with a balancing adjustment and central filling at the rescaled area level. This is not merely the m=2 substitution of the prior first-order two-mode theorem.

## value

PASS

The prior third-eigenvalue example demonstrates only that an annulus loses. This gives a sharp accuracy benchmark for the optimized ordered eigenvalue and explains why weak two-radius concentration is insufficient for comparably accurate masks: a nonzero fraction must nearly fill the central disk on its natural area scale. The positive correction comes from a boundary first-moment constraint and has matching explicit masks; it is not merely extra numerical precision in a known constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
