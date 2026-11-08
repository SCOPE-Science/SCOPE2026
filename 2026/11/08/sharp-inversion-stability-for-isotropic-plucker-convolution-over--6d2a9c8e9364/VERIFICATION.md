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

# Verification and reproducibility

The finite tests use only the explicit formulas and objects in `RESULT.md` and are not substitutes for the all-field mathematical proof.

From the containing directory, run `python CHECK_PRIME.py` with Python 3 and NumPy installed. The code generates nonzero isotropic decomposable bivectors from ordered vector pairs, computes Fourier transforms directly, constructs every alternating-frequency pencil in three small cases, evaluates its modular ranks, and asserts agreement with the derived exact integer multipliers. Complete comparisons cover \(64\), \(729\), and \(32768\) Fourier frequencies respectively in the binary four-dimensional, ternary four-dimensional, and binary six-dimensional settings. It also directly checks \(27\) frequencies in symplectic dimension six over \(\mathbb F_3\), including the nilpotent-Jordan minimum witness.

Run `python CHECK_GF4.py` using Python 3 (no third-party packages required). It implements the extension field \(\mathbb F_4\), enumerates the isotropic Plücker cone, and compares \(50\) directly evaluated trace-character sums with independent alternating-matrix-pencil rank formulas. This supplies a finite check beyond prime fields.

Observed successful terminal markers: `PASS p= 2 n= 4`, `PASS p= 3 n= 4`, `PASS p= 2 n= 6`, `PASS_BIG p= 3 n= 6`, and `GF4_ISOTROPIC_BIVECTOR_PASS support=255 checks=50`. The theorem begins in symplectic dimension six; four-dimensional tests check conventions only. The dimension-six ternary and four-dimensional extension-field checks sample frequencies rather than enumerate all of them. No numerical experiment is asserted to prove all dimensions or all field orders.

Scientific proof critical steps checked: exact \(\mathrm{SL}_2(\mathbb F_q)\) wedge-presentation multiplicity, subtraction of dependent pairs, alternating-form rank parity, integer spectral lattice, inequality for the least spectral endpoint, and Jordan-pencil attainment. The literature check compared direct and stronger potentially covering statements. The present status is self-review only; independent mathematical validation is not performed.
