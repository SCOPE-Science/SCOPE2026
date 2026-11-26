---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The radical products land in Kw, which the radical annihilates; this gives associativity and the local radical with J²=Kw. The nondegenerate commutator form on the a,b quotient gives the stated center. A noncentral radical element with a nonzero a or b coefficient has a nonzero central product with a suitable c_i; an element with nonzero scalar part has one with w, and the remaining nonzero elements are central. Any unital K-linear isomorphism induces L on J/(Z∩J) and sends w to (det L)w′ by the commutator, while squaring forces Q′(Lv)=(det L)Q(v). Conversely, this identity fixes the action on the central quotient by the perfect pairing; the correction to the V×V product is alternating and imposes one nonzero linear equation on the four central correction coordinates. Thus each admissible L has q³ choices of correction and q² choices for each of the two independent w′ offsets, giving q⁷ actual invertible lifts. Isotropy is equivalent to Tr(αβ)=0: if α=0 it is immediate, and otherwise the line search reduces to u²+u+αβ=0. The two nonsingular binary forms are isometric within each type, with determinant-one isometries in the displayed polar normalization. The split similitudes preserve or swap the two zero lines; the anisotropic norm similitudes are multiplication by a nonzero extension element followed by identity or conjugation. This gives the two stated orders. Counting trace-zero products gives q(q+1)/2 pairs, and each zero of Q gives q³ square-zero radical elements. Tr(1)=m modulo 2 verifies the parity of scalar extension; direct substitution verifies the displayed F₄ map. The published-size q=4 count 294912 for both binary models is consistent because they are both split over F₄; a trace-one F₄ model instead has count 491520. The independent bounded replay checked trace classes for all ordered parameter pairs over F₂ and F₄ and the q³ correction count for 12 and 360 admissible quotient maps respectively, not all full algebra maps; see /workspace/branches/5d3ca7bf-3f6b-4ed8-a5a8-901320f9b893/replay.py, replay_GF2.txt and replay_GF4.txt. The frozen checker and stdout were inspected, not rerun.

## originality

PASS

The model and exact binary classification, including the 24-versus-8 square-zero contrast, are prior. The classical binary quadratic-form classification and similitude counts are likewise not claimed. The supported distinct result is the ring-level uniform lift count and exact K-linear automorphism arithmetic over all finite binary extensions; the other counts and scalar-descent contrast are consequences in this ring family.

## value

PASS

The family comes from the minimal binary centrally essential examples, so scalar extension and K-linear symmetry are natural invariants. The theorem counts the whole automorphism group, including the nontrivial q⁷ factor that is invisible in the quadratic quotient, and explains exactly when the two minimal examples coalesce after base change. This is a useful structural invariant and not a finite replay of the binary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
