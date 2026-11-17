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
# Verification notes

Proof reconstruction: check \(b_k^k\le\prod_{j\le k}b_j\le\prod_{j\le k}a_j\) using decreasing order and weak log-majorization; take roots, including zero cases. The factorial bound \((k!)^{1/k}\ge(k+1)/e\) and telescoping \(\sum_{k\ge j}1/[k(k+1)]=1/j\) give the uniform summability. Dominated convergence and the simple \(p\)-power difference inequality finish the theorem. All restrictions \(T\in\mathcal S_p\), \(p>0\), \(0<t<1\) are necessary for the quoted inputs, and no inference about operator convergence is made.

`CHECK.py` is a standalone Python 3 standard-library diagnostic for finite arithmetic and finite weighted shifts. Execute from the directory containing `CHECK.py` with `python3 CHECK.py`; it prints its finite assertion total. It is not a formal certificate for the infinite theorem and supplies no independently reviewed claim. The paper arXiv:2611.07728v1 provides the nontrivial coordinatewise spectral-convergence input.
