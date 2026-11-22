---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For a rooted complete binary tree, the signed independent-set sum pair (F_h,E_h) satisfies E_h=F_{h-1,L}F_{h-1,R}, F_h=E_h+(-1)^r E_{h-1,L}E_{h-1,R}, initialized at height0 by (2,1),(0,1). Mod2 every character has the parity of the unsigned independent-set total; q_h mod2 follows q_{h-1}+q_{h-2}, periodic 0,1,1 at heights 0,1,2, giving lower gaps 2,1,1. Explicit all-descendant-equal state cycle (0,1)->(1,0)->(1,1)->(0,1) produces multiplier1 in the nonzero residues, zero at height multiples of3; switching its final root sign produces 2, proving sharp gap all h. At h=3, complete height2 signed-state ratio table totals 128 and contains 120 occurrences of ratio1 and one each 25/9 and 9/25; zero criterion needs pair product+1 at root sign-1, giving 120²+2=14402 zeros, and no root sign+1 cancellations. Character group size 32768, rank18366, nonzero gap2, unsigned count2306, Parseval sum 75563008. Independent integer state recurrence replicated entire ratio table and nullity. Fourier character diagonalization gives Moore–Penrose inverse norm reciprocal gap.

## originality

PASS

Bounded semantic Resultary search plus primary-literature comparison finds no earlier theorem dominating the precise full stated claim. Explicit equivalences and narrower covered portions are identified. This is best-of-knowledge, not a guarantee of global novelty. The previously known ingredients and different domains of related results are not claimed new.

## value

PASS

Exact pseudoinverse stability at every tree height plus a complete first genuinely singular character classification answers natural deconvolution questions not fixed by homogeneous independence-polynomial parity. The two exceptional reciprocal ratios make the finite h=3 classification mathematically structural rather than an arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
