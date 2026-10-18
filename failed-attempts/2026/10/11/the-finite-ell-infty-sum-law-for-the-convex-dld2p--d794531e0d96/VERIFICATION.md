---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

FAIL

The stated pointwise equivalence for arbitrary finite ell-infinity products is not established by the proof. Its indispensable converse assumes that a non-Delta unit vector x has a **norm-one norming functional** f(x)=1 with ||I-f⊗x||<2; that purported characterization is false. Exact counterexample from Abrahamsen–Haller–Lima–Pirk, Proposition2.3: in real l1 take smooth x=(1/2,1/4,1/8,...). Its unique norm-one norming f=(1,1,...) obeys ||I-f⊗x||=2 (test e_n with n→infinity), although x is NOT a Delta-point: the nonnorming g=2e_1* satisfies g(x)=1 and ||I-g⊗x||=1<2. The correct Lemma2.1 requires testing all functionals g with g(x)=1, not just norm-one f. This invalidates the asserted Delta-coordinate equivalence and hence the converse convex-hull separation step based on it; indeed the 2026 primary paper flags Delta points in ell-infinity sums whose coordinates need not be Delta. The useful forward direction from one Delta-generating factor is plausible, but the claimed full iff statement has no verified replacement proof in the assigned package. This is a motivated, documented correctness gap; NOT a numerical timeout and NOT a claim that the final iff has been disproved as a standalone statement.

## originality

PASS

Existing primary 2020 theorem proves stability if BOTH factors have convex-DLD2P for any absolute norm. The 2026 source proves inheritance of convex-DLD2P by factors for all absolute norms EXCEPT ell-infinity and explicitly calls the ell-infinity case hard; it does not imply the asserted one-factor iff law. Published related infinite c0 convex generation is not the finite ell-infinity criterion. These comparisons are novelty evidence only, not correctness certification.

## value

PASS

An exact factor criterion for finite real ell-infinity sums would resolve the natural missing exception in recent absolute-sum inheritance theory. The claimed converse is substantial and the forward one-good-factor direction is mathematically motivated; the result is NOT accepted because its key nonstandard pointwise lemma is false, not because the problem lacks value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
