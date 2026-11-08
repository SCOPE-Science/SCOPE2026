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

# Computation and proof checks

The noncentral coordinate model is \(\mathbb F_q c\oplus\mathbb F_q^m\oplus\mathbb F_q^m\). The checker `verify.py` computes finite-field operations, tests commuting pairs through the two independent bracket equations, and separately groups ordered pairs of vectors by their exterior-product values. The direct and fiber paths are independent counting implementations. They reproduce the closed numerator and probability. Run `python3 verify.py` using Python 3 standard library only; the matching expected output is embedded in `verification_output.txt`.

Exact direct tests: \((q,m)=(2,2),(2,3),(2,4),(4,2)\), together examining 1,328,128 ordered noncentral pairs. Fiber tests: nine combinations over \(q=2,4,8\), together examining 337,488 ordered vector pairs. A further 66 exact integer/rational substitutions test nonnegativity and the equality of two expressions for the formula. The \(m=2\) tests are diagnostic only; the new claim begins at \(m=3\).

Critical symbolic steps reconstructed: the zero exterior fiber has \((q+1)q^m-q\) points; every nonzero decomposable fiber has \(q(q^2-1)\) points; the number of such fibers is \((q^m-1)(q^m-q)/(q(q^2-1))\). The hub split contributes \((q^2-1)q^m((q+1)q^m-q)\) solutions in the nonzero case. All central coordinates cancel from the ratio. These mathematical arguments, rather than experiments, prove the all-rank and all-even-field assertion.

Limits: the code does not enumerate all matrices over all finite fields, has no external theorem prover, and cannot establish historical novelty; there is no external independent audit.
