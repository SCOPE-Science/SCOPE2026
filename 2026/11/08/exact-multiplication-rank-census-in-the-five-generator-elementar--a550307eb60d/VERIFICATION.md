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
The complete mathematical argument is in `RESULT.md`. Execute `python3 check.py` with Python 3; no external packages are required. The output must match `check_output.txt` byte-for-byte apart from any platform newline convention. This checker constructs squarefree-basis multiplication matrices and performs ordinary elimination in characteristic two. It exhausts both canonical quadratic high-degree families (each containing \(2^{16}\) possibilities), the \(2^{10}\) homogeneous quadratic forms, the \(2^{10}-1\) nonzero cubic forms, every nonzero homogeneous quartic and quintic form, and the \(64\) corrections of each canonical cubic. It also checks \(160\) deterministic quadratic samples over the extension field \(\mathbb F_4\), and verifies that the symbolic count totals are \(q^{32}\) for \(q\in\{2,4,8\}\).

Expected terminal marker: `ALL_DIRECT_MULTIPLICATION_RANK_CHECKS_OK`. Exhaustion refers only to the explicitly enumerated finite cases; in particular it is **not** an exhaustive enumeration of all \(2^{32}\) algebra elements, and it cannot substitute for the arbitrary-field proof. The full rank support and formulas are established using the separately written normal forms and counting argument, not by extrapolating these tests.
