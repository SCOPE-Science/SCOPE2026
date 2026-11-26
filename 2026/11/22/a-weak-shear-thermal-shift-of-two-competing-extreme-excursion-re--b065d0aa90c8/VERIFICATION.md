---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Gaussian inversion with the exponential renewal age gives the exact scaled kernel and the finite thermal subtraction in proof step 2. The limiting derivative factors into two quadratics, giving two nondegenerate minimum branches separated by a maximum near the crossing. The crossing and sign can be checked without trusting rounded bracket values: set P=ab and S=a+b. The branch equations give (b-a)/S=P/3, and their stationary costs are 2a-3/a+3/a³ and 2b+3/b+3/b³. The gap divided by S is 2P(P²-3)/(3(9-P²)), with 0<P<3. At equality P=sqrt(3), giving a_c²=2sqrt(3)-3, b_c²=2sqrt(3)+3, q_c²=8sqrt(3), and L=2. The short-age term in the c bracket is (1-a_c²)²/a_c^5 > sqrt(2) because a_c²<1/2. The long-age term is (1+b_c²)²/b_c^5 ≤16/(9sqrt(3)) for b_c≥sqrt(3). Thus the sign is strictly positive. Uniform endpoint coercivity localizes all potential global minima to a compact interval; C² convergence there preserves the two nondegenerate candidates and the action gap excludes the remainder. The implicit function theorem and envelope differentiation give the unique local crossing and the coefficient to O(eta^{-4}); a separate bisection gives q_c≈3.7224194364 and c≈6.4474195909. At fixed eta, Laplace localization of the regular conditional density gives relative weights g/sqrt(F_ss); the singular-looking origin factor is controlled by F≥constant/s there and the large-age tail by F≥s. Replay via RESULT.md proof steps 1–5. VERIFICATION.md and checker.py were inspected, not executed. The result is local in q and for sufficiently large eta; it takes R to infinity at fixed eta before the separate expansion in eta.

## originality

PASS

The same-model Gaussian kernel and the pure-random-acceleration limiting action are known and are not considered original. The checked sources do not give the distinct retained-noise weak-shear coexistence boundary, its positive eta^{-2} displacement or the corresponding two-well age law. Fixed-shear results and the marginal-on-displacement unique-age saddle do not eliminate a two-saddle competition at a jointly conditioned rare transverse endpoint. This is a bounded statement-level assessment, not a priority certification.

## value

PASS

The two minimizers represent genuinely different histories leading to the same observed endpoint. The result shows where one history replaces the other and how even weak longitudinal thermal noise moves their equality boundary, a prediction lost in the pure-acceleration reduction. Obtaining normalized conditional weights distinguishes actual coexistence from merely finding two stationary points of an action.

The dated certificate retains the supplied scientific assessment, sources and limitations.
