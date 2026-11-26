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

At a smooth point with p_i,p_j nonzero, the tangent direction with entries p_i/(a_i p_i^3) and -p_j/(a_j p_j^3) in positions i,j annihilates the tangent linear term. The quadratic term along it vanishes iff a_i p_i^3+a_j p_j^3=0. Three such pair equations are incompatible in characteristic unlike 2. With two nonzero coordinates, F(P)=0 gives that relation, and the full tangent quadratic vanishes (the other two coordinates do not enter it). Thus the triple-cut tangent criterion gives exactly the three distinct intersection points on each of the six lines, none a coordinate vertex; smoothness and characteristic unlike 3 ensure the expected transverse cuts. J is the reduced union of the lines and F is regular modulo J. For M=intersection (x_i,x_j)^2, monomial membership requires b_i+b_j>=2: either all coordinates occur, or one does not occur and the other three occur at least twice. Thus M=(Q,g_0^2,...,g_3^2) where g_i=Q/x_i. For a direct CM check, the 5-by-4 matrix with first row -g_i and diagonal x_i in the four other rows has maximal minors Q and ±g_i^2; its ideal has height two, so Hilbert–Burch applies. R/J is also CM by the ordinary rank-two uniform matroid theorem (or the syzygies x_i g_i=x_0 g_0). F avoids the line primes and is therefore regular modulo both J and M. This gives I=(F,J), saturated and locally reduced. With K=M+FJ+(F^2), one has (K:F)=I and (K,F)=(M,F). The multiplication-by-F exact sequence has one-dimensional CM outer terms; K is saturated. Locally Q belongs to the square of the point ideal, so K is exactly the ideal of the doubled projective points, including by descent from a splitting field. Counting monomial supports of size at most two gives H_{R/J}=(1+2t+3t^2)/(1-t)^2; for R/M add 4(t^3+t^4+t^5)/(1-t)^2 for support of size three with at least one exponent one. The exact sequence gives H_{R/K}=(1-t^3)(H_{R/M}+t^3 H_{R/J}), the claimed numerator, length 72, regularity 7, and the listed Hilbert function. Modulo Q the nine sextics are independent: F^2 has a pure sixth power, each Fg_i has a (4,1,1) term of the corresponding support, and each g_i^2 has its own (2,2,2) term. All six other J-products vanish modulo Q. This proves the minimal list and unique quartic. The attached jet code and recorded three-field interpolation results were inspected, not executed; they do not substitute for the all-field proof.

## originality

FAIL

The central symbolic-square identity is a direct instance of the earlier matroid-specialization theorem of Geramita–Harbourne–Migliore–Nagel, not just analogous to a star configuration or supported by Varbaro's CM lemma. Applying that theorem with one loop and inspecting monomial exponents yields the quartic defect immediately. The geometric identification is classical geometry with a direct tangent computation, and the remaining numerical invariants are forced by the specialized ideal; it is not asserted that the earlier theorem prints the Hilbert series in this notation.

## value

FAIL

Doubled-point interpolation on the diagonal cubic is geometrically natural, but here the novel-looking defect and quartic follow by a routine specialization of an existing theorem and elementary exponent checks. The Hilbert and generator data then follow by degree and monomial counts. The frozen claim adds no independent structural or exact invariant beyond that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
