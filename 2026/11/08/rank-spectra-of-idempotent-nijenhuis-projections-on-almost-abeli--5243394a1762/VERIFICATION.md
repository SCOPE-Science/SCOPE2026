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

# Verification protocol and observed evidence
The proof in `RESULT.md` is symbolic and valid for arbitrary finite fields and matrix sizes in the stated domain. `check.py` performs a second, exhaustive calculation for seven small prime-field examples, taking the original Lie bracket and Nijenhuis torsion equation as input. It enumerates all matrices of the linear operator and tests the identity on every basis pair; bilinearity makes that an exhaustive condition on all vector pairs. It separately enumerates invariant subspaces and disjoint pairs and computes the theorem's right-hand side. Its comparisons do not assume the subalgebra classification.

To reproduce: `python check.py`; standard Python 3 only, no additional packages. The recorded output is embedded as `check_output.txt`. The run finished with the exact marker `ALMOST_ABELIAN_NIJENHUIS_DIRECT_TORSION_OK`.

Observed rank counts, in ranks \(0\) through \(m+1\):

- Scalar, \(m=2\), \(q=2\): \((1,28,28,1)\).
- One Jordan block, \(m=2\), \(q=2\): \((1,12,12,1)\).
- Irreducible action, \(m=2\), \(q=2\): \((1,4,4,1)\).
- Split squarefree, \(m=2\), \(q=3\): \((1,63,63,1)\).
- Scalar, \(m=3\), \(q=2\): \((1,120,560,120,1)\).
- One Jordan block, \(m=3\), \(q=2\): \((1,24,32,24,1)\).
- Irreducible action, \(m=3\), \(q=2\): \((1,8,0,8,1)\).

A second checker `check_f4.py`, run with `python check_f4.py`, represents the genuine extension field \(\mathbb F_4\) as \(\mathbb F_2[u]/(u^2+u+1)\), and directly exhausts the original idempotency and Nijenhuis equations. Its four rank spectra for \(m=2\) are scalar \((1,336,336,1)\), Jordan \((1,80,80,1)\), irreducible \((1,16,16,1)\), and distinct split \((1,144,144,1)\). Its output is in `check_f4_output.txt`, ending in `ALMOST_ABELIAN_NIJENHUIS_GF4_EXTENSION_OK`.

Limits: these finite computations cannot establish the arbitrary-dimension theorem, which instead depends on the separate direct-sum and incidence proof. The prime-field checker uses modular arithmetic, while the separate extension-field checker uses polynomial-reduction arithmetic; neither computes automorphism orbits or scheme structures, and neither performs an independent mathematical audit.
