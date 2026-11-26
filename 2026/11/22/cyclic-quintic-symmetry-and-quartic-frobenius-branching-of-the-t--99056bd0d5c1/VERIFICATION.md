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

The exact published models are smooth genus-four canonical complete intersections. By the canonical action every ground-field automorphism extends uniquely to a rational projectivity preserving the unique containing quadric. Since the cubic part of the homogeneous ideal is spanned by F and linear multiples of Q, the displayed coefficient test is necessary and sufficient. I executed an independent exact enumerator, python3 /workspace/reproductions/curve_similitudes.py, not the supplied checker. It uses columns of similitudes rather than the Hermitian cosets: enumerate isotropic X,Y with B(X,Y)=lambda nonzero, normalize the first nonzero entry of X to 1, then choose Z,W in the polar orthogonal complement with Q(Z)=Q(W)=lambda and B(Z,W)=lambda B(e_z,e_w). These four column norms and all polar products specify Q(Tv)=lambda Q(v), and the nondegenerate polar form ensures invertibility. This covers every projective similitude once, in both characteristics. Exact cubic substitution and comparison modulo Q give 5 stabilizers out of 120 and 1440 projectivities respectively, equal to the five projective powers of the displayed matrices. The matrices themselves have order five; since Phi_5 is irreducible of degree four over both fields, any nontrivial such four-dimensional linear action has that separable characteristic polynomial. Riemann–Hurwitz for the prime-order tame action says 6=5(2g_0−2)+4r, forcing g_0=0 and r=4; a genus-zero curve over a finite field is P¹. The four projective eigenlines must therefore lie on the source curve, and arithmetic Frobenius permutes them transitively by ord_5(q)=4. Totally ramified fibers have distinct branch values, so there is one closed branch point of degree four. This proves only the full ground-field groups for the two marked models and their quotient behavior, not geometric automorphism groups. The uploaded script was inspected, not executed; smoothness and canonical model identification were checked against the cited original model results.

## originality

PASS

Prior work supplies the two isomorphism classes, model equations, and point-count/gonality tests, and a binary census supplies an equivalent orbit method. The additional established invariant is the full rational stabilizer of each marked model and its arithmetic branch type. No inspected prior table gives the stabilizer size or orbit length for the specific models, and the methods and lists of representatives alone do not give them without computing the relevant orbits. Riemann–Hurwitz and the Frobenius cycle are direct consequences once the group is known, not claimed as new techniques. Credit Castryck–Tuitman's earlier preprint example over F3; the frozen equations are those subsequently selected by Faber–Grantham, not the first construction of that isomorphism class.

## value

PASS

The two curves are all genus-four cases of gonality five over finite fields, making their full arithmetic automorphism groups natural exact invariants rather than arbitrary field cutoffs. Fullness matters for identifying the actual arithmetic quotient and tells a future user that both canonical extreme cases support the same tame quintic quotient and single quartic branch place. This is not a re-count of the known census or rational point totals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
