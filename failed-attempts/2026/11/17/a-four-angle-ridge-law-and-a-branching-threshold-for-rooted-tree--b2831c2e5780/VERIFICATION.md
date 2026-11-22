---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The canonical order polytope has exactly root-lower, leaf-upper, and n-1 cover facets, total n+L. All facet pairs except the L-U upper-leaf/own-cover pairs with branching parent meet in codimension two; for an excluded pair the equalities force the parent and every sibling to one. Normal dot products for root/leaf boundaries, adjacent covers, and sibling covers give pi/4 at d_root+U, pi/3 at n-1-d_root, 2pi/3 at W=sum binom(d_v,2), and pi/2 at binom(n+L-1,2)-W. The number of ridges R=binom(n+L,2)-L+U matches the sum. The sharp equivalence of right-angle fraction tending to one and maximum child degree Delta=o(n) follows from W<=Delta(n-1)/2 and W>=binom(Delta,2), with R=Theta(n^2). A checker covers all rooted free trees n=2..9 (748 root placements) by actual vertex-affine ranks; the general proof is independent of enumeration. Boundary n=2 works.

## originality

FAIL

A published more general theorem, Four-angle ridge spectra and crossed-cover obstructions for all Euclidean order polytopes (Resultary, November 17, 2026), was materially read and proves the exact four-angle multiplicity distribution for EVERY finite poset. Specializing its augmented-cover graph to rooted trees gives F=n+L; no crossed covers; disallowed boundary two-edge chains precisely the L-U branching-parent leaf pairs; T_boundary=d_root+U; T_interior=n-1-d_root; same-source internal covers W. Hence all four proposed angle counts and ridge count are direct special cases, even though wording/parameters differ. Its general W count plus elementary quadratic bounds yields Delta=o(n) iff right-angle concentration. The exact publication ordering within November 17 is unknown; mathematical coverage, not unsupported timing, determines the rejection. The older Ahmad-Fourier-Joswig face-partition theorem also covers combinatorial ridge incidence, though not the metric data alone.

## value

FAIL

Rooted-tree order polytopes and their ridge geometry are natural, but this package offers only an elementary specialization of the already available all-poset exact metric classification plus the immediate bound Delta=o(n) iff W=o(n²). There is no separate structural invariant, extremum, counterexample or non-routine consequence outside that general theorem. Correctness and a finite checker do not establish independent incremental mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
