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

The source language, nucleotide involution, self-separation, cross-separation, exact GC count and homopolymer constraint are checked independently from codebook input. `verify.py` generates every eligible word at lengths two, four and six, and confirms that the corresponding conflict graphs have \(0\), \(40\) and \(344\) vertices, with \(468\) and \(7804\) edges at the latter two nonempty lengths.

For length four, exhaustive maximal-independent-set enumeration proves capacity \(4\) and exactly \(64\) maximal-size codebooks. For length six, two independently generated integer-optimization formulations each establish a branch-and-bound upper bound strictly less than \(28\) and attain \(27\), while `code6.txt` independently supplies the feasible \(27\)-set. `code8.txt` is a directly checked feasible \(136\)-word code, not a proof of eight-base optimality. Command: `python verify.py` with the pinned requirements.

The exact integer objective and incidence constraints have integral coefficients. A numerical optimization solver is used for the complete finite branch-and-bound; the verifier requires a certified bound within \(0.01\) of the exhibited integer value, leaving a full integer-unit separation from the excluded bound \(28\). This computation has not been replicated in a formal theorem prover or independently audited.
