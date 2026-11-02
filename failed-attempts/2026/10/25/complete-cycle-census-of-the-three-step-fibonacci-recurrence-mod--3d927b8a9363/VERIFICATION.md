---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For the exact all-ones three-step map A, independent integer arithmetic yields (A^13-I)/3 integral with determinant 106, so A modulo 3 has order 13 and lifts by a unit perturbation at every 3-adic depth. Irreducibility of x³-x²-x−1 in F3 implies all nonzero vectors modulo 3 have period 13. For every valuation stratum k-t, repeated cubing shows primitive period exactly 13·3^(t−1), with 26·3^(3t−3) states and 2·9^(t−1) cycles. Direct independent complete state census modulo 3,9,27 examined 20439 states and matched all orbit counts. This correctness result is nevertheless nonoriginal because of Klaška 2008.

## originality

FAIL

Prior full-text coverage is decisive: Klaška (2008) Theorem 3.10 establishes the period 3^(t-1)h(3) for EVERY nonzero initial triple mod 3 in the irreducible case; Lemma 2.2 extends to every valuation. h(3)=13 and h(9)=39 follow from the audited small matrix certificate. Dividing the 26*3^(3t-3) states in each valuation stratum by their known common period yields exactly 2*9^(t-1) cycles. The entire claim, including all multiplicities and sum, is thus a direct elementary corollary, not merely an OEIS match.

## value

PASS

The full natural all-state period spectrum and orbit multiplicities for Tribonacci modulo 3^k form a mathematically interpretable and reproducible exact invariant, rather than arbitrary initial values. However its mathematical contribution as NEW knowledge is eliminated by the 2008 stronger theorem; independent value is not used as a novelty substitute.

The dated certificate retains the supplied scientific assessment, sources and limitations.
