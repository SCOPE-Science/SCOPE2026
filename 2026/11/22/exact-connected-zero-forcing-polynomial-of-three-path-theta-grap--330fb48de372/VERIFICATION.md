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

# Verification instructions

Run `python CODE/verify_theta.py` with Python 3.9 or later; the script has no external dependencies. It constructs each simple theta graph from edge-length triples, traverses the full power set of vertices, checks initial induced connectivity by a graph reachability algorithm, and separately executes simultaneous eligible zero-forcing moves to closure. A second implementation independently constructs the coefficients by direct integer polynomial convolution of the proposed formula.

The regression suite enumerates 68 triples \(2\le a\le b\le c\le8\) with \(a+b+c\le18\), visiting exactly 1,886,304 initial masks, of which 37 triples have repeated arm lengths. It verifies complete coefficient vectors, vanishing degrees below three, the universal degree-three coefficient six and the leading coefficient one; it exits with assertions if any case fails. When executed during preparation, it returned `VERIFY_OK`.

The unbounded-integer polynomial expansions are exact. The finite tests do not prove the theorem for all path lengths; the proof in `RESULT.md` is the exhaustive structural classification by the two terminal vertices. No independent mathematical audit is represented by this verification record.
