---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For row minimum r_j (n for the empty row), an upset pair with p<q fails exactly at rows satisfying p<=r_j<q; for p>=q there are no failures. The output is the upset immediately after the last failing row, or the full chain if none fail. Adjacent pairs recover each last index, and each row can be last for at most one label. A partial injection is realized by its prescribed arrows (f(p),p); those arrows are forced in every realization, proving unique minimum size, including the empty domain. In a prescribed row there are 2^(n-1-p) supersets with minimum p; all other rows independently choose the empty set or a minimum whose prescribed final row is strictly later. This yields the full fibre product. Counting partial injections and using rigidity of the finite Heyting chain gives the stated labeled operation and isomorphism counts. The frozen scripts and finite verification notes were inspected, not executed; the symbolic proof covers every n>=1.

## originality

FAIL

A distinct indexed Resultary record gives the same unrestricted chain classification and exact realization fibres, and states that the canonical relation is inclusion-least. The failed originality finding is about demonstrated equivalent coverage in the checked corpus, not a claim of publication priority or of dependence. The separate persistence theorem, known rook counts, and de Groot–Litak normalization are relevant but are not the decisive overlap.

## value

PASS

The mathematical result (apart from originality) solves a natural fixed-carrier representation problem. It recovers a canonical minimal frame from only adjacent operation values and quantifies exactly how many raw frames represent every operation, including loss of row and arrow information. These are useful structural statements beyond evaluating a familiar binomial sum. They do not leave a distinct uncovered remainder under this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
