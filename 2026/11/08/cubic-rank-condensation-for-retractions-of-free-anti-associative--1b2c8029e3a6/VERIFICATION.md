---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The anti-associative relation over char≠2 forces all length-four products to zero while preserving independent degree-one, degree-two and right-nested degree-three words. The actual RESULT.md constructs the free algebra V⊕V⊗²⊕V⊗³ with sign -(uv)w=u(vw), and arbitrary generator images determine homomorphisms. Any composition-idempotent e induces an idempotent P on V; choose basis U=image P,W=ker P and set g(u)=e(u),g(w)=w−e(w). This is identity mod the square, hence a filtered automorphism; e g=g P on generators, so e=gPg^-1, with image isomorphic F_r and rank d(r). The kernel G of automorphisms fixing V/J is the independent affine generator higher-degree shifts, of size q^{nB(n)}; commuting with P forces shifts in U to U-only words (B(r)) and those in W to words with W letters (B(n)−B(r)). Orbit-stabilizer yields q^{r(B(n)−B(r))+(n−r)B(r)} lifts per fixed P, times {n brack r}_q q^{r(n-r)} linear projections. Image orbit size is {n brack r}_q q^{r(B(n)−B(r))}, and fixed-image fibers q^{(n-r)d(r)}. Independent symbolic expansion reproduced quartic E_n=-2r^4+(n−2)r³+(n−2)r²+(n³+n²+2n)r, with uniformly bounded Gaussian correction. Its limit f(t)=t+t³−2t⁴ has unique strict interior maximizer alpha solving 8alpha³−3alpha²−1=0 and negative second derivative; for all sufficiently large n the integer ranks outside floor/ceil x_n lose order n² in log_q weight, giving the stated exponentially small leakage. Independent n=2,q=3 formula gives 4*3^13=6,377,292 rank-one endomorphisms, consistent with 3^12 per fixed degree-one projection and 3^3 per embedded image. These finite checks are not the proof of all n or asymptotic concentration.

## originality

PASS

Remm 2022/2024 complete primary paper explicitly determines the free anti-associative algebra and three homogeneous dimensions; it does not count composition-idempotent endomorphisms or images. Cerqua–Facchini 2023 full pre-Lie paper, §6, gives abstract retraction/semidirect correspondence in a different algebra variety, no q-Gaussian enumerator. The highly similar published Resultary class-two Lie census was read in full: its F_n=V⊕∧²V, ranks r+binom(r,2), and quadratic-large-deviation saddle are not the odd-char anti-associative cubic tensor algebra. The entire enumerator and quartic asymptotic are neither renaming nor numerical specialization. A general operadic projection formula might provide an alternative but no directly covering finite-field formula was located.

## value

PASS

Retractions classify genuine direct-factor algebra decompositions; the complete family-wide image orbit and fixed-fiber census over every odd finite field is a natural structural invariant of the free anti-associative variety. The new cubic graded layer changes the growth exponent from class-two analogues and yields an irrational rank-condensation fraction and two-integer window at exponential accuracy. This is motivated, mathematically nonroutine classification, not just a rebranding of q-linear projections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
