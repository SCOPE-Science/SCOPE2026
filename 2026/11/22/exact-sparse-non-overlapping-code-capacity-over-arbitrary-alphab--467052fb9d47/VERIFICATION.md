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

# Verification of the exact sparse capacity theorem

The mathematical certificate is the self-contained four-step proof in `RESULT.md`. The only nontrivial upper-bound point is the equal-zero-gap overlap: for \(u=0^i a0^m b0^{m-i}\) and \(v=0^j c0^m d0^{m-j}\), if \(a=d\), then the proper prefix of \(u\) and the proper suffix of \(v\) of length \(m+i-j+1\) both equal \(0^i a0^{m-j}\). This forces disjoint initial/terminal marker-color sets. The matching construction uses all longer-initial-gap necklaces and a balanced color bipartition at equal gaps; the direct prefix/suffix reasoning covers every case.

Run `python checker.py` in a directory containing this file and `checker.py`. It prints the direct construction-verification count for 91 cases (alphabet sizes 2–7, word lengths 2–14), including 438,536 ordered word-pair comparisons. The optional command `python checker.py --milp` requires NumPy and SciPy, enumerates the **entire** weight-two candidate set, constructs all proper-prefix/suffix conflicts and all self-overlap exclusions, and solves 20 small exact binary integer programs (alphabet sizes 2–5, lengths 2–6) with zero relative mixed-integer optimality gap. All 20 match the formula. This optimization is a finite check, not the infinite proof.

No unbounded computational claim, proof-assistant certification, independent expert review, or verification of all possible equivalent prior literature is asserted. Arithmetic and source scope in the theorem remain as stated in `RESULT.md`.
