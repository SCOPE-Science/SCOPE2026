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

## Reproduction

From a directory containing `checker.py`, run `python3 checker.py`. The test exits with an assertion failure if any comparison fails. A successful run prints the number of comparisons in four categories.

The checker directly recounts scattered index triples for words through length \(13\), compares all residues for moduli \(2\) through \(10\), breadth-first searches transition states for moduli \(2\) through \(23\), and confirms injectivity of the three-suffix output signature. An independent Moore output-partition-refinement algorithm minimizes the reachable machines for moduli \(2\) through \(10\). It also constructs positive-word realizations of the commutator transformations and verifies their witness action for moduli \(2\) through \(8\).

Replayed checks: 147447 direct word-count comparisons; 22 reachability moduli; 58751 unique output-signature states; 2685 group-generator and constructive-witness checks; 9 independent Moore minimizations. All passed. The all-modulus conclusion is supplied by the algebraic proof in `RESULT.md`, not by an extrapolation from the finite tests.

## Scientific limits

The claim concerns a residue-output Moore machine. It is not a claim about the minimum Boolean DFA for an individual target residue. Complete historical priority and independent mathematical validation have not been established.
