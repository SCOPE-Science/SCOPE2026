---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Both least periods and the displayed histograms are correct. Integer recurrence and A^8=I+3B give six unit-lifting progressions per sequence, twice per residue class modulo 3, and force a least period of 8·3^(k−1) by the mod-3 state cycle and regular-branch injectivity. In each remaining branch the other coordinate divided by 3 runs bijectively modulo 3^(k−1). The norm identity and the sign modulo 3 choose the right square root. For U(z)=sqrt(1+λz²) with λ in 9Z_3, rationalizing U(z)−U(z′) shows it is divisible by 9(z−z′); the denominators 1+U and the sum of the two outer square roots are units. Thus the normalizing map is the identity plus a 9-contraction and permutes each finite quotient. The two critical classes are disjoint. Modulo 3^h an output of valuation 2j has two simple unit roots lifted with 3^j free choices, and zero has 3^floor(h/2) roots; every root gives three branch preimages. The cases k=1 and k=2, the zero square class and the half-Pell–Lucas normalization all agree. Independent norm-algebra enumeration from k=1 to 11 matched both complete histograms, the predicted square counts and least periods (1,417,168 scalar evaluations). Replay: python3 /workspace/branches/reproduce_frozen.py pell; log /workspace/branches/reproduction-pell.txt. This finite check does not prove unrestricted k.

## originality

FAIL

The obstruction is demonstrated prior implication, not an exact table hit or access failure. Lang–Lang's full orbit decomposition for q=2 modulo 3^k determines all Pell and associated Pell state pairs, and directly reduces the histogram to the elementary congruence count in claim_vs_prior_implication. The frozen account cites only the residue-completeness consequences of that paper and overlooks its stronger orbit result.

## value

FAIL

Exact multiplicities for this classical pair would be a useful refinement if independent of known coverage, but the frozen invariant is an elementary projection of the published complete state census. The alternative 3-adic derivation gives a correct exposition without a further mathematical gain beyond that corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
