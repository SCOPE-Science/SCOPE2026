---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For n>=2 the source Corollary 4.1/Definition 4.2 gives primitive cone rays. The lower-unitriangular second-difference lattice automorphism sends rho_(n-j) to basis f_(j+1), old e_j to f_j−2f_(j+1)+f_(j+2), and u to −f_1+f_2. A one in the binary cone forces z_(i+1)=0; a zero forces a second-difference relation, with terminal z_(n+1)=0. Each interval between forced zeros contributes exactly one independent generator w with g*w=0; the all-zero word gives trivial quotient. Thus N/N_sigma=⊕Z/g and its finite Smith invariants agree with local toric Cl for full-dimensional simplicial cones. Maximizing the gap product means i_1=0 and an ordered composition of n; replacing 1 and >=5, and three 2s, derives standard 3/2 integer break. Counts are 1 for n=3a, a+1 for n=3a+2, and a(a+3)/2 for n=3a+1. Independent sympy Smith normal forms and determinants on all 508 cones of 2<=n<=8 confirmed every cyclic-factor profile, maximum and multiplicity. This is not a universal computational proof: the recurrence and integer-break argument is.

## originality

FAIL

The full fixed-point group spectrum is a direct special case of Arena–Song’s published §7 boundary-stratum quotient and stabilizer rule, together with its own primitive toric stack fan and the general inertia/class-group identification from Goldin et al. and toric divisor theory. The binary-gap code is exactly the ordered composition of bubble lengths; at each bubble’s unique torus-fixed point the nonzero highest elementary symmetric coordinate forces stabilizer μ_g. Its character group gives Z/g. Ordered integer compositions yield the claimed sharp maximum and counts by the standard integer-break argument; no genuinely original substantive remainder survived. Different naming and absence of verbatim formula do not avoid prior implication.

## value

PASS

Independently of priority, the coarse fixed-point local class-group spectrum, sharp largest cone multiplicity, and exact maximizing-orbit count are mathematically natural singularity invariants for a moduli-derived toric family, useful for selecting and comparing worst local singularities. The group type distinguishes, for example, Z/4 and (Z/2)^2 at n=4 even though their orders match. This intrinsic geometric use clears the natural-complete-classification value bar; it does not rescue originality because the classification is already implied by source results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
