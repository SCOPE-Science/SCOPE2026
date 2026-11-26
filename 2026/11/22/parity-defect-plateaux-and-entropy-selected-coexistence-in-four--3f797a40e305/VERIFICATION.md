---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For k favored rim spins and t favored apices, the forced bond cost is at least max(0,2k-n)+tk. The k-breakpoints are 0, floor(n/2), ceil(n/2), n; for 0<x<=2 the mixed or all-favored apex lines at the positive breakpoints cost t(k-x) more than the nonfavored-apex line, and k=0 cannot beat -x floor(n/2) since floor(n/2)>=3. For 2<=x<=n the line n(1-x) bounds all competing lines by their endpoint gaps, with only k=n at x=n; that is a three-sector apex tie, and the greatest slope in magnitude takes over beyond n. The rim equality patterns have no extraneous nonfavored bond costs when counted as proper colorings after excluding the apex colors. On the odd rim at x=1, the two boundary k-sectors add, while at x=2 all independent nonfavored rim sets contribute 3*2^|R|+6. The cyclic independence transfer eigenvalues give both terms of D_n; near activity 2 the top eigenvalue gives density 1/3 for R and variance O(n), so the limiting favored fraction is 2/3. At x=0 proper colorings are counted by whether apices coincide; x=n gives 4^2 apex choices. No unsupported finite-temperature inference is needed.

## originality

PASS

The strongest inspected comparators establish overlapping wheel mechanisms or solve other Potts models. They do not cover the full finite-exchange four-color two-nonadjacent-apex family, the odd-rim J crossing or the activity-2 entropy selection.

## value

PASS

This completes a natural graph-family classification and separates three phenomena quantitatively: a parity defect creates an extra field interval, local freedom at coexistence produces a third macroscopic favored density, and the final saturation threshold scales with apex degree. Knowing the full labeled degeneracy matters to uniform ground-state sampling; the energy envelope alone cannot predict the 2/3 density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
