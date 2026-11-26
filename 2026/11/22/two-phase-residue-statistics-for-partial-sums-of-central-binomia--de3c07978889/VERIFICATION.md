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

For base-five doubling, the least digit ≥3 produces a Lucas zero (no earlier carry), and otherwise the digit factors are (1,2,1,0,0). Summing complete five-term blocks and the final partial block gives (u,a)↦(−u+c_d a,w_d a) with c=(0,1,3,4,4); leading zeroes preserve (0,1). On independent uniform digits, the first digit 3 or 4 kills the second coordinate forever, and Y_r=(−1)^r S(n) is then constant as depth advances. The coupling error is at most the survival probability (3/5)^r, uniformly in each residue. For an independent distribution check, affine equivariance of the digit rules makes the limiting signed value from initial (u,a≠0) equal in law to u+aZ with Z the limit from (0,1). Conditioning on the first digit gives two chances in five of Z=1, and otherwise the push-forwards of Z by z↦−z, −1−2z, −3−z, each with weight 1/5. This map contracts differences of laws by at most 3/5, and (1,8,2,1,2)/14 satisfies its five equations exactly. Sign reflection at odd depth gives (1,2,1,2,8)/14. Multiplying the coupling error by 5^r proves the bound for counts, and opposite parity limits differ in all four nonzero coordinates. Independently checked all 20 published certificate equations, the five-state equations, all seven finite histograms and the exact integer binomial sum histogram at depth four via python3 /workspace/branches/reproduce_3_4_5.py. The supplied checker and recorded output were read, not executed; the finite tests do not replace the coupling. The frozen theorem makes no claim at residue zero for arbitrary cutoffs.

## originality

PASS

Lucas products, endpoint congruences and finite-state methods are established. The substantiated distinct claim is the evaluated pair of running-sum laws at the two parity subsequences, with the pointwise error and failure of the four densities. None of the compared statements gives this evaluated law.

## value

PASS

The summatory central-binomial sequence is a natural arithmetic object. Prime-power endpoints and the single-coefficient distribution do not determine whether its residue classes among indices have densities via known endpoint laws. The distinct even/odd histograms and a uniform finite-depth error quantify a concrete obstruction for every nonzero residue; the absorption argument identifies its source. This is more than obtaining digit recurrences or small tables and does not presume wider-modulus generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
