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

The smooth general pencil gives a transverse codimension-two Plücker section, of complex dimension d=4n−4 and ambient class h². Below d, integral weak Lefschetz identifies the complementary degree 4n−6 with the ambient Schubert classes. The complements of (2n−3−j,j) in the 2×(2n−1) rectangle are (2n−1−j,2+j); adding two boxes to (2n−1−b,b) gives precisely the pairing binomial(2,b−j), with unavailable indices omitted. The vector (−1)^b(n−b) satisfies the resulting second-difference equation with v_n=0. Poincaré duality and the known torsion-free cohomology establish the integral relation R_n. Expanding h²q_j=q_{j+2}+2cq_j+c²q_{j−2} for j≥1 and q_{−1}=0 gives h²R_n=(n+1)h q_{2n}−q_{2n+1} by cancellation. A nonzero common zero of q_{2n}, R_n over a field would have c≠0 and then force two consecutive vanishing q's, contradicting q_0=1 by backwards recurrence. Thus the candidate has the same complete-intersection Hilbert function over Q and every residue field and is torsion-free in each degree. The top class c^{2n−2} integrates to 1 by Pieri, hence generates the candidate top degree as well; fieldwise Artinian Gorenstein duality relative to this class yields unimodular integral pairings. The tautological ring map has equal ranks by the additive result, and the determinant identity for each pair of complementary degrees forces integral isomorphisms, not merely rational ones. Substitution gives the n=2 relations, and the different primitive Plücker top powers are the stated Catalan numbers. Even without grading, the saturation index of the d-th power of the nilradical is the same Plücker degree, so the nonisomorphism also holds in that reading. No executable certificate is needed for these deductions.

## originality

FAIL

Already covered, not false: the earlier 84ed57af052d record gives the entire integral graded cohomology ring on the same tautological generators for all n≥2, and moreover its Chow ring. The displayed two-relation ideal follows mechanically over Z from that colon-ideal presentation. Put Q=q_{2n}, P=q_{2n+1}. Modulo h² one has Q≡(−c)^n and P≡(n+1)h(−c)^n (from the recurrence). Hence the polynomial R=((n+1)hQ−P)/h² is defined integrally; the Pieri recurrence identifies it with the displayed R_n. If h²f=AQ+BP, then h²(f+BR)=(A+(n+1)hB)Q. Since h does not divide Q, unique factorization implies Q divides f+BR. Conversely both Q and R belong to the colon ideal. This is precisely (Q,P):h²=(Q,R_n). Thus the sole candidate distinction, explicit generators of the same ideal, is a direct algebraic conversion. The identical middle matrix is already stated and the comparing Plücker powers depend only on the known degree of the two hyperplane sections in question.

## value

FAIL

The integral cup-product question itself is worthwhile, and explicit relations are convenient. But the same integral ring, middle pairing, and comparison are already accessible from the stronger prior exact-family presentation. The only remaining gain is writing that ideal using the immediately obtained numerator quotient and one gcd; no new cup product, invariant, or independently motivated consequence remains. There is no substantive repair to the claim as frozen.

The dated certificate retains the supplied scientific assessment, sources and limitations.
