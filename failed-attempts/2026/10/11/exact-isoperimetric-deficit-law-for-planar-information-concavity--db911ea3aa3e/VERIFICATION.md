---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The domain is each planar convex body with nonempty interior, any r>0 and 0<=t0<t1<=1, 0<lambda<1. Classical Steiner gives A_t=(1−t)^2A+rt(1−t)P+pi r²t² and P_t=(1−t)P+2pi rt>0. D=P²−4pi A is nonnegative and vanishes only for disks. Directly P_t²−4pi A_t=(1−t)²D; hence I_t=P_t/(4pi)−D(1−t)²/(4pi P_t). Exact symbolic differentiation and a separate finite Jensen numerator identity reproduce respectively I_t''=−2pi r²D/P_t³ and the claimed finite gap. The formula extends to t=1 because P_t stays positive, and strict concavity for every nondisk follows from D>0. The actual repository verify.py was reconstructed byte-for-byte (Git blob SHA 296dc...) and executed with VERIFY_OK; an independent SymPy derivation verified all three polynomial identities. No finite experiment substitutes for the general proof.

## originality

FAIL

The advertised exact law does not solve an additional geometric or analytic determination beyond the classical all-parameter planar Steiner polynomial and perimeter formula. Zhang–Zhou (2017), Eq. (1)-(2), prints both A(s)=A+Ps+pi s^2 and the discriminant D=P^2−4pi A; Richter–Saorín Gómez (2022), Eq. (2.2)-(2.4), gives the general parallel-body volume and perimeter polynomial. Setting s=rt/(1−t) and using homogeneity gives I_t=P_t/(4pi)−D(1−t)^2/(4pi P_t). Differentiating this elementary rational identity twice yields I_t''=−2pi r^2D/P_t^3. Its three-point Jensen identity follows by elementary common-denominator arithmetic from the same explicit input; the disk equality case is also classical. The exact output was not found verbatim in the searched literature, which is NOT represented as a claim that a paper printed it. The decisive coverage is mathematical implication by a textbook rational calculation, not matching wording. The inaccessible 2003/2026 full texts remain documented risks but are not the reason for rejection.

## value

FAIL

The area-to-perimeter profile and isoperimetric deficit are canonical, but the complete claimed result is only the second derivative and Jensen difference of a known quadratic-over-linear Steiner expression. Its proof requires no new convex-geometric estimate, motivated unknown invariant, hard structural lemma or nonroutine boundary analysis: write the classical exact A_t and P_t, divide, and simplify. The sign, strictness and equality family are exactly the standard isoperimetric inequality. Merely replacing a known qualitative statement by an immediately determined rational identity supplies no independent mathematical obstacle resolved, and no structural consequence beyond the already tabulated polynomial data. This is a useful illustrative identity, not a distinct contribution under the stated bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
