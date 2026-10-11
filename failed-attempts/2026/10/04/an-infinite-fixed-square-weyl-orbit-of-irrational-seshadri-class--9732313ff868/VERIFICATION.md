---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Fresh lattice calculation verifies \(L^2=20\), \(L\cdot\delta=4\), \(L\cdot\alpha=0\), and the standard Kac translation formula \(T_\alpha^m(L)=L+4m\alpha+4m^2\delta\), yielding the displayed coefficients and strictly increasing plane degrees. Totaro's inspected Cremona-general-position machinery realizes each finite Weyl word by an isomorphism between the corresponding smooth blow-ups; pulling back Laface--Ugaglia Theorem 2 therefore preserves ampleness and the Seshadri constant. Countably intersecting the source configuration loci and the pulled-back very-general point loci gives one fixed very general surface and one common point for all \(m\). Primitivity is preserved by lattice automorphisms.

## originality

FAIL

The final infinite-orbit statement is mechanically implied by two inspected prior ingredients. Laface--Ugaglia Theorem 2 proves that the seed class \(L\) is ample on a very general nine-point blow-up and has \(\varepsilon(L;x)=2\sqrt5\) at a very general point. Totaro explicitly recalls that standard Cremona transformations and point permutations realize the affine Weyl action on the marked Picard lattice, that on smooth projective surfaces the resulting pseudo-isomorphisms are isomorphisms, and that very general point configurations are Cremona general. Applying these isomorphisms to any countable sequence of Weyl translates preserves ampleness and Seshadri constants; intersecting the countably many very-general loci yields one common very general surface and one common very general point. The displayed coefficient formula is then the routine Kac-translation calculation. Under the required implication standard, this is a corollary of prior results rather than an original scientific claim.

## value

FAIL

Once the seed theorem and standard affine-Weyl/Cremona transport are in hand, the infinite family, fixed square, common very general surface, and common point follow by a routine symmetry orbit plus a countable-intersection argument; the remaining coefficient formula is elementary lattice arithmetic. Under the shared value bar this is a useful observation but not an independently motivated mathematical gap beyond its prior ingredients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
