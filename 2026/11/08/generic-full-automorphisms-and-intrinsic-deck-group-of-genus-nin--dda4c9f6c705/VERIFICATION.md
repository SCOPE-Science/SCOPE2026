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

Five parameters avoiding branch values yield twenty simple roots of the hyperelliptic polynomial and genus9. The explicit maps (t,y)->(t,-y),(-t,-y),(1/t,-y/t^10) preserve the model, commute and produce eight automorphisms; fixed-point computations single out exactly three free involutions once full Aut has order8. For a=(2,3,4,5,6), reduction modulo 719 gives exactly the twenty listed rational branch points. Independent full 20*19*18=6840 projectivity image-triple enumeration yields only t,-t,1/t,-1/t on the roots. Since every branch root is rational, this exhausts geometric stabilizers as well. Hyperelliptic lifting bounds geometric special-fiber Aut by 8. In char0, Hurwitz |Aut|<=672<719 excludes the 719-primary kernel of good-reduction specialization, forcing exactly eight at the rational point. Automorphism-size upper-semicontinuity gives exact eight on a Zariski-open dense parameter set. The free involution subgroup is intrinsic, yielding unique genus3 quotient. This extrapolation uses a legitimate geometric specialization theorem, not just the finite-field experiment.

## originality

PASS

Borówka–Ortega classify hyperelliptic Klein covers and show injectivity of a Prym map; their older paper provides the same quartic-factor curve and involutions. Those foundational constructions are prior work and not claimed new. The surviving contribution is proof of generic exact full automorphism group of the entire five-parameter type-I.1 family and intrinsic recovery of the top-curve free Klein subgroup; these do not follow from Prym map injectivity. Genus9 polarized-abelian-surface subfamily differs from full parameter family. Best-of-knowledge historical risk from unread specialized source and broader classical automorphism theory.

## value

PASS

Generic automorphism group and uniqueness of an unramified quotient are natural moduli invariants, with direct interpretation of the forgetful morphism. The complete finite-field branch-stabilizer certificate provides a concrete robust method for generically minimizing the group, not merely computing one example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
