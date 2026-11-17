---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For proper S in C_n, each induced component is a path with perfect matching iff its maximal one-run has even positive length. Every omitted gap of length <=3 is disjunctively dominated, and gap >=4 has a second unserved zero. Rooting at one of s selected-run starts yields exactly n/s times the positive composition coefficients. Independent exact enumerations of all labeled vertex subsets for n=3..14 using generic shortest-path domination and recursive perfect-matching tests matched every full polynomial coefficient. Formal logarithmic cycle construction then yields the claimed rational generating function. The deficit d=5k−n and s=k or k−1 gives the five-residue min-set formulas, and unique simple positive pole rho yields total P_n(1)~rho^(−n) with unit coefficient. Finite tests support but do not prove all n.

## originality

PASS

Henning, Pandey, Tripathi (2023) is the original primary source on this exact paired-disjunctive domination definition and determines minimum order 2 ceil(n/5) for cycles. Its publicly available abstract identifies minimum numbers and algorithms, not an all-cardinality labeled cycle polynomial or exact extremal multiplicities. Other Resultary paired domination polynomials concern different graph families or ordinary paired domination, a stronger neighborhood notion. Full 2023 paper was not obtainable via lawful open sources and institutional Oxford reports disconnected VPN, so no whole-paper noncoverage is claimed; this is a best-of-knowledge originality PASS with explicit material priority risk.

## value

PASS

All-size labeled subset census and five-residue optimal multiplicities refine a natural known graph-domination parameter and provide an independently useful exact enumerator and asymptotic growth, not a random arbitrary slice. Does not require a separate downstream theorem to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
