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

# Reproducible verification

With Python 3 and only its standard library, run from the same directory:

```sh
python3 verify_relation.py
python3 verify_direct.py
```

The first program regenerates both Rule 110 adjacency matrices from the local truth table, enumerates exactly \(75\) reachable Boolean relations, verifies the rational denominator factorization and residue divisibility, and computes all \(75\) consecutive integer recurrence residues for \(n=11,\ldots,85\). These are a finite certificate for an infinite recurrence because the constructed integer transfer matrix has dimension \(75\) and Cayley–Hamilton applies. The code also checks the first \(18\) image-count coefficients.

The second program independently applies the Rule 110 local update by cyclic bit rotations to every binary input of each length \(1,\ldots,18\); it compares the number of distinct resulting indexed words against the coefficients. Brute force is confirmatory and is not used as the infinite proof.

The dominant-pole argument additionally uses exact discriminant \(-751\) and rational sign intervals for the quartic factor; the proof records these details, which can be checked by integer arithmetic.

These checks do not constitute independent verification of mathematical priority, nor do they extend to multistep predecessors or the infinite-limit dynamical system.
