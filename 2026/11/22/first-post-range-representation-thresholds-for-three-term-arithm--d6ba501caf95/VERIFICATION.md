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

The total length u=x+y+z and offset v=y+2z recover x,y from z, whose allowed interval is [max(0,v−u),floor(v/2)]. For N=as+dt all possibilities are (u,v)=(s−dℓ,t+aℓ) with ℓ≥0 since t∈[0,a−1]. At s=a+d+k, k=−1,0 and k=1 only for even a and odd t, ℓ≥2 would require 2d+t≤2, impossible. For ℓ=1 the upper branch a+2k−t of the minimum applies because k≤t; when k=−1,t=a−1 it is −1 and the formula correctly returns zero. The ℓ=0 contribution is 1+floor(t/2). The two floors give p+1 at the claimed threshold and p one period earlier, including the smallest a. Monotonicity under adjoining a proves both the first-crossing claim and absence of later gaps. The maximum is at t=a−1 even in the parity-jump case, where that index is odd. Subtracting a gives the greatest gap; summing (M_t−(dt mod a))/a gives the genus including zero. Independent replay using the exact increment R(n)−R(n−a) from representations with x=0 (via a linear congruence, not the uploaded DP) confirmed 708 coprime pairs and 27576 threshold residues, their immediate predecessor counts, and both global invariants.

## originality

PASS

The supported advance is the full explicit first-post-range Apéry classification for all coprime steps d≥3 and the resulting invariants. Results for d=1 and the known earlier p-range do not give that classification. Best-of-knowledge decision with a material thesis access risk.

## value

PASS

This is the first level excluded by a precisely bounded published result that poses the higher-threshold problem. It answers that first case for an infinite variable-step family, not an isolated example, and gives the complete residuewise crossing rule useful for membership queries as well as both global invariants. The parity effect identifies why the threshold is not generally a uniform one-layer shift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
