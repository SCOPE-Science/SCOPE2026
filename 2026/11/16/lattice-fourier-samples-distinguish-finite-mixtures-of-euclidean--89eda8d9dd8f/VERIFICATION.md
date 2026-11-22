---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Fourier coefficients on the dual lattice equal (up to fundamental-cell volume) Fourier coefficients of the locally finite lattice-periodized compactly supported mixture; all vanishing means periodization zero a.e. Fix any one sphere boundary S_j. Only finitely many lattice translates of the finite family intersect a compact tubular neighborhood of S_j. If none is identical in parameter class, each other sphere intersects S_j in at most a proper codimension-one subsphere, so d>=2 provides an open patch of S_j free of all other boundaries. The alleged zero periodization has a jump exactly a_j across that patch, forcing a_j=0. For d=1, the distribution derivative on R/sZ is the summed signed endpoint delta measure. Vanishing derivative gives an a.e. constant; the integral over one cell is sum 2a_jr_j, so these two independent conditions are necessary and sufficient. A length-s interval shifted by a nonlattice amount supplies sharp aliasing. Independently computed a planar six-disk 81-frequency matrix with rank 6 and minimum singular 0.2968204, and checked interval periodization; such finite checks do not establish all-lattice uniqueness.

## originality

PASS

Periodization and unique singular interface patches are known geometric techniques, and Asipchuk–Robins characterize when two ordinary set indicators have equal lattice Fourier samples via equidecomposability. Their results do not establish complex linear independence of an arbitrary many weighted, arbitrarily overlapping balls or the exact 1D weighted mixture kernel. Bounded primary comparisons and Resultary returned no direct covering assertion; older inverse-interface uniqueness equivalences remain risk.

## value

PASS

The finite-ball mixture inverse problem is natural in lattice tomography and Fourier shape inference. The exact no-alias result despite arbitrary overlap and complex cancellation, plus a necessary-and-sufficient dimension-one obstruction, is a meaningful complete classification of a natural dictionary rather than a fitted one-off example. It identifies precise information loss under periodization without claiming finite noisy recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
