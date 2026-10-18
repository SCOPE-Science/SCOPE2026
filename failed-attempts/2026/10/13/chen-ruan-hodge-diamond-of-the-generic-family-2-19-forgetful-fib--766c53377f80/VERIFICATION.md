---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Zhao identifies the generic fiber with quotient by G=A[2]⋊{±1} (here direct product because translations are 2-torsion). Each nontrivial translation has no fixed points; (T,−1) fixes the sixteen points solving 2x=T, with a transitive free action of A[2] and residual stabilizer C2. Its derivative on tangent A is −I, age 1. There are 16 such distinct conjugacy elements, hence 16 one-point gerbe sectors with Hodge shift (1,1). Inversion kills odd-degree cohomology of the abelian surface and leaves untwisted (h00,h20,h11,h02,h22)=(1,1,4,1,1). Adding 16 gives h11=20, b0,b2,b4=(1,22,1), orbifold Euler 24. This is the standard global-quotient age formula and is correct under the general smooth over C assumption.

## originality

FAIL

FAIL: Zhao establishes not only K_V ≅ [A/(A[2]×{±1})] but the factorization A→A/A[2] ≅ A via multiplication-by-two. The free normal translation subgroup can be quotient out as stacks, yielding a canonical equivalence [A/(A[2]×{±1})] ≅ [(A/A[2])/{±1}] ≅ [A/{±1}]. The latter is precisely the classical orbifold Kummer surface with its well-known sixteen A1 order-two sectors and K3 Chen–Ruan Hodge profile. Fantechi–Göttsche global quotient fixed-point/age theorem and standard Kummer orbifold results already dominate the numerical computation by immediate application of Zhao’s equivalence. Merely relabeling this classic orbifold as Zhao’s K-moduli fiber does not supply a new uncovered invariant; no claim of source exact wording is needed for implication coverage.

## value

FAIL

FAIL: once Zhao has supplied the quotient-stack isomorphism and free A[2]-quotient equivalence, this is the textbook 16-sector Kummer orbifold Hodge calculation (untwisted h11=4 +16), already synonymous with the Kummer K3 profile. There is no new moduli-specific structural argument, unexpected boundary, new invariant, or additional ring calculation; it is a known-table recomputation under a renamed object, despite correctness and pedagogical usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
