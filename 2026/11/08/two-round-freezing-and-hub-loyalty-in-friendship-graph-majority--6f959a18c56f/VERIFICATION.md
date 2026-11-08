---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification and boundaries

Use Python 3 with the standard library only; no additional packages or external data are needed. Execute `python3 verify_direct.py` and `python3 verify_counts.py` from this directory.

The adjacency-based program tests every binary configuration of the labelled friendship graphs with \(1\le k\le8\), a total of 174,760 initial configurations. It runs three synchronous updates and checks that the second state is fixed; it independently counts first fixed-entry times, final hub reversals and unanimous outcomes. `direct_output.txt` contains the observed equalities and the terminating marker `EXHAUSTIVE_OK`.

The separate weighted edge-type enumerator checks the exact population identities for every \(1\le k\le100\), comparing independent multinomial category sums with the binomial-tail formulas. It also evaluates asymptotic leading-term ratios at \(k=100,101,200,201\). `count_output.txt` contains its results and the terminating marker `ORBIT_COUNT_OK`.

The finite-range checks are evidence of correct implementation and boundary behavior, not a proof for all graph sizes. The all-size mathematical proof is in `RESULT.md`, including the crucial fixed-edge lemma, the hub tie case, exact combinatorial counting and the asymptotic tail argument. No external or independent scientific audit was performed.
