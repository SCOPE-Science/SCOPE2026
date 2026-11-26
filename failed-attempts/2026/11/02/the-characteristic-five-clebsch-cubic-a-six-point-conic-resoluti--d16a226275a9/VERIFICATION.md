---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Equal coordinate squares and the sum-of-signs condition force a unique singularity P. In the chosen coordinates the cubic really is 3(sQ+D) before scalar division, and Q has nonsingular matrix I+J. On each of a+b=0, a+c=0, b+c=0 the conic cuts two distinct F5-points, with all six pairwise distinct; the listed points meet Bézout's bound and exhaust the six F5-points of Q. The inverse graph of projection is the blowup of the reduced complete intersection (Q,D): the resolved inverse takes the local ratio [-D:Q] for the homogeneous coordinates [s:t] on the direction line, and maps [s:t] to [s:t(a,b,c)]. The contraction is an isomorphism away from P, where the direction recovers the graph point; only the strict transform of Q maps to P, and its square is -2. For the automorphism upper bound, any automorphism lifts to the minimal resolution and preserves its unique exceptional conic E. It therefore preserves the plane line class H=-K_Y-E, descends via its complete system to a projectivity preserving the six centers, and the induced plane action is faithful because the blowup is birational. The stabilizer of the six points preserves their unique conic and acts faithfully on it; on P^1 it is contained in PGL2(F5) by the uniqueness of a projectivity with three prescribed images. Coordinate S5 realizes all 120 distinct permutations on these directions: they are the cosets of the order-20 normalizer of a Sylow-five subgroup and the action has trivial core. Thus it attains the bound and all automorphisms descend over F5. Each split blowup adds q points, and contracting the split conic subtracts q, yielding the stated zeta function of X. An independent check on the identical model enumerated 120 direction permutations and counts 56 and 776; it does not supply the geometric upper bound.

## originality

FAIL

The earlier exact catalogue result already proves the same split resolution, zeta function and six-point coordinate action. It expressly does not assert the full surface automorphism group, but supplies both divisor-class formulas from which that group follows formally: the plane blowdown is intrinsic via H=-K_Y-E. Hence even the narrower full-group assertion is a routine consequence of the earlier classified model and action, not an unresolved invariant. No reliance on same-day priority or on an inaccessible paper.

## value

FAIL

The full automorphism group of this natural singular reduction is a reasonable invariant to ask for, and the proof correctly distinguishes the group from the evident subgroup. But the already known marked resolution and its divisor classes recover the blowdown canonically, so the requested upper bound is a routine stabilizer calculation. The other packaged invariants were directly proved earlier. There is no surviving nonroutine exact invariant or new structural argument in the frozen Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
