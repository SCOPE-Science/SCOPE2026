---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The P3/P4 meet-row reduction and P1/P2 constrain top, bottom, and each atom row. P5 gives exactly a_i->u_i<=u_i and a_i->w<=w. The disjoint bottom cases w=0, w=atom, w=1 yield respectively m+1, m(m+1), and four-colored terminal-or-arrow functional digraph types; the first two sum (m+1)^2. For permutation cycle length d the equivariant choice is four terminal colors plus Fix(sigma^d)-1 other vertex targets, hence 3+sum_{e|d}e c_e; Burnside gives the stated partition sum. Rooted-tree decoration of sinks and directed cycles gives A(z) and C(z). Splitting out d=1 gives a (1-T(z))^{-1} factor; Otter T(z)=1-b sqrt(1-z/rho)+... yields coefficient K rho^{-m}m^{-1/2}. Independent exact Burnside evaluation gives U_2..U_10=(24,66,186,533,1562,4592,13532,39778,116724). These finite values do not prove asymptotics.

## originality

PASS

PASS, best-of-knowledge. The Oct 18 and Oct 26 height-two preconditional classifications already give labeled operation counts. They do not count orbits under atom permutations, identify the four-terminal functional-map isomorphism structure, or derive the Otter-type square-root pole. The entire Oct 26 earlier proof was compared. Standard Pólya/Otter and generic unlabelled functional-digraph theory are credited as methods, not novelty. No stronger published original calculation of this lattice-specific quotient was found; priority risk from unindexed equivalence remains.

## value

PASS

PASS. Isomorphism classes are the natural intrinsic objects for finite algebra classifications, unlike raw labeled operation counts. The complete Burnside spectrum, canonical functional-digraph model and sharp asymptotic characterize how many inequivalent logical algebra structures occur as the atom count grows. The change from ordinary rooted-tree m^{-3/2} to a square-root pole m^{-1/2} is mathematically structural, independently useful for enumeration and comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
