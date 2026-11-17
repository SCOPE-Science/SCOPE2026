---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS. In characteristic two D_f=f∂, D_f^2(x)=f f′, and even/odd coefficient decompositions lead to EO=0 and O²=0 in F_q[t]/(t^m) in both lengths. t-adic order of O and E controls permitted pairs and image rank; counting rank strata gives the displayed P_{m,q}, total q^m+floor(m/2)(q-1)q^{m-1}, maximal-rank homology count, and conditional uniform stratum index implies rank/m=>Uniform[1/2,1]. Actual verify.py constructs finite-field derivation matrices for small N. Independently algebraically matched P_{m,q} coefficients against the full prior 2026-10-25 closed formula for m=1..17 and q=2,4,8; finite checks are not the proof.

## originality

FAIL

FAIL. Earlier 2026-10-25 published parity-stable rank-variety theorem identifies the reduced rank-r loci in BOTH 2m and 2m+1 as the same varieties and gives the full identical rank polynomial, total and all homology ranks, for every characteristic-two field. The 2026-11-02 published square-zero derivation theorem independently supplies the same EVEN-length rank polynomial and Uniform[1/2,1] limit with stronger W1 O_q(1/m). Their conjunction directly implies every main numerical, parity and limit conclusion of this finding. The explicit pair-coordinate correspondence is only a presentation of the already proved parity-stability.

## value

FAIL

FAIL. Though the mathematics is correct and of natural interest, this submitted unchanged package recomputes a previously published exact rank table, parity equality and limit law. Its method adds no separately motivated unknown mathematical invariant or structural theorem beyond the earlier reduced rank-locus isomorphisms; reproducibility is not independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
