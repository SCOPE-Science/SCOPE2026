---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With a nonzero hub, k zero rim sites force at least 2k−n zero-zero edges, and an odd wheel is not properly three-colorable. Thus U≥max(n mod 2,2k−n); for 0<x<2 its field-shifted bound is minimized uniquely at k=ceil(n/2), attained with strict alternation (even) or one forced zero-zero edge (odd). Equality leaves no hub-color rim site and yields exactly 4 or 2n labeled configurations. At x=2 equality requires no adjacent nonzero rim sites and no hub-color rim site; conversely every independent set of rim nonzeros realizes −n, giving 2L_n. For x>2 the nonzero-hub optimum is uniquely all-zero on the rim for each hub color. For a zero hub with k≥1 the exact edge cost is k+max(0,2k−n): place zeros optimally and alternate the two other colors in each remaining run. At k=0 the rim costs n mod 2. Minimizing these costs less x(k+1) and subtracting the nonzero-hub optimum gives, on successive field ranges (0,1], [1,2], [2,3], [3,∞), the differences (m−1)x, m−x, (m−1)x−m, n−x for n=2m, and (m−1)x, m−1, (m−1)(x−1), n−x for n=2m+1. The restrictions m≥3 even and m≥2 odd give strict positivity below n, and the zero-hub minimizer for x>3 is uniquely all zero. This gives exactly three states at n and one above, with no extra ground-state change at the internal hub-sector breakpoints 1 and 3. Fibonacci path counts give L_n=F_(n−1)+F_(n+1), the entropy density log φ at x=2, and the adjacent regime counts show the claimed density jump. Independently ran /workspace/branches/replay_2.py: integer transfer statistics by hub, last rim color, U and K for n=5..15; checked the full optimal statistics with multiplicities at 2,871 exact rational field points covering all positive intersections and one witness in each open field cell for those sizes. This is finite corroboration only; the analytic argument proves all n≥5. Uploaded code was inspected, not executed.

## originality

PASS

Wheel weighted proper-coloring formulas and general field Potts partition representations are known. The exact finite-coupling ground states in this claim include monochromatic edges, unlike proper colorings, and the strongest exact same-day wheel results use different spin interactions or optimize single-spin stability instead of global energy. The distinct supported claim is the full parity-sensitive finite-J ground-state diagram, including the threshold degeneracies and the exact Lucas correspondence.

## value

PASS

The wheel separates competition on a frustrated cycle from a hub with extensive degree. The theorem fully resolves both mechanisms and their degeneracies at all positive fields, yielding one fixed-field transition with genuine extensive entropy and a second size-dependent hub transition. This makes the hard-core independent-set structure at the first threshold an identifiable ground-state mechanism rather than an incidental enumeration; the odd cases also test behavior outside hard proper-coloring. No finite-temperature phase transition is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
