---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The support function of the orthogonal free sum is max(||u||_1,||v||_1); its proper faces are precisely exclusive cube faces or mixed joins, with fixed-coordinate counts k,l. For an exclusive face, a normalized fixed-coordinate normal separates the face from its vertex complement by 1 (k=1) or 2/k (k>=2), attained by a face barycenter and either the origin in the other block or the barycenter of single-sign-flipped corners. For mixed faces, the normal equal to 1/k and 1/l on their fixed coordinates gives separation 2/max(k,l) in normal projection and distance 2/[max(k,l)sqrt(1/k+1/l)]; explicit convex combinations of a face barycenter and single-flip complementary vertices attain it. In k<=l sector its squared value is 4k/[l(k+l)], increasing in k and decreasing in l, so global minimizer is (k,l)=(1,q), with swapped (p,1) only if p=q. Exclusive faces are strictly larger. Counts 2p*2^q (or twice symmetric), diameter 2sqrt(q). Independently solved 38 finite-type convex-pair QPs for p,q=(2,2),(2,3),(3,4), obtaining maximum difference 2.4e-14; source checker additional cases. All-unbounded claims follow analytically, not from finite tests.

## originality

PASS

Known cube and cross-polytope face distances, including p=q=2, are credited. The full unbounded two-cube *free sum* face-rank spectrum does not follow from Peña–Wirth's Cartesian product rule, nor from general linear-map inequalities and universal upper bounds. Resultary searches for Hanner/free-sum aliases found the current result and different invariants, but no broad exact covering theorem. Provisional PASS with clearly delimited priority risk.

## value

PASS

A free sum of two cubes is a natural orthogonal Hanner polytope. The exact all-face Euclidean separation, full extremal-face classification, and the sharp q^{-3/2} normalized decay relative to a cube factor are meaningful sharp quantitative geometry, even without an algorithmic convergence theorem. This is distinct from a single low-dimensional instance or generic Cartesian product fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
