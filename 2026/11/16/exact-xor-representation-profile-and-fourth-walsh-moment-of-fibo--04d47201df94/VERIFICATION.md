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

# Verification

`CHECK.py` uses only Python's standard library. Running `python3 CHECK.py` completes exact checks of all ordered XOR representations for every \(n\) from \(1\) through \(13\), comparing each of the \(2^n\) output coordinates with the run formula. It verifies that the counts sum to the square of the Fibonacci-cube vertex count, that no difference is absent, and the precise extrema with the upper equality restriction.

For \(1\le n\le12\), an independent integer Walsh–Hadamard transform of the vertex indicator checks both second and fourth moments. The integer transfer matrix is checked by direct multiplication against its characteristic polynomial, and the recurrence against its generated values through \(n=18\). The energy sequence starts \(1,8,21,89,296,1105,3897\) (with the \(n=0\) convention). Output terminates in `FIBONACCI_XOR_PROFILE_AND_FOURTH_MOMENT_PASS` when all assertions succeed.

The symbolic proof in `RESULT.md` covers all \(n\ge1\). Finite checks cannot alone prove that universal statement. Full-text priority checking is bounded by source access; the 1997 transform article remained abstract-only, and the scalar energy numbers are previously indexed as OEIS A264238.
