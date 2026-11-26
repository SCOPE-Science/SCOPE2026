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

Cancellation reduces the event to R(P)V=VR(Y) on d+4 independent symbols. At d=1,2,3 the solution families respectively have one, two and one free letters. At d>=4 the first d equations force V to be a periodic continuation of R(P), and the last four equations require its terminal block Y to satisfy Y=R(Y). Rotation bijects R(P) with Y, leaving q^2 choices. There are n-3-d pairs at each feasible displacement; the geometric tail and binary coefficient 11/64 follow. This is a pair count, not a distinct-descendant count. A separately written direct output enumeration (/workspace/branches/a06182c6-5100-4174-a77e-4f6b2e8785f1/rc4_independent_check.py) matched the probabilities for q=2, d=1..8 and q=4, d=1..5, plus the binary pair means for n=4..9. This is bounded corroboration only; the submitted checker was inspected, not executed.

## originality

FAIL

The numerical probabilities are not quoted in the sources, but the entire collision spectrum is mechanically implied by Lenz et al.'s exact all-length, all-displacement conditions for the conjugate palindromic operation. Zabokritskiy's coordinate involution preserves both sites and the uniform word law. In the palindromic variables, specializing Lenz equations (10a–c) to block length four identifies every letter for d=1 or 3, and gives the two classes in a b b a a b for d=2. Equations (11a–c) respectively force the initial repeat block, its four-periodic continuation and reversal symmetry of the rotated terminal block, leaving two free letters for every d>=4. Division by q^(d+4) and summation over displacements supply the whole expectation, without a new structural lemma. This is demonstrable prior coverage by implication, not an inference from titles or search unavailability.

## value

FAIL

Pair collisions are a meaningful second factorial moment of output multiplicities, and nonlocal collisions distinguish this length from length two. As submitted, however, all new-looking numbers are the direct free-class counts of the already characterized event and a routine expectation. No genuinely new residual invariant or complete multiplicity result is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
