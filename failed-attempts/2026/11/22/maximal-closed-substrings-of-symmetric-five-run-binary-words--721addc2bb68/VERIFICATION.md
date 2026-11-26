---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a closed non-singleton the border occurring twice is its longest proper border: any longer border would put another occurrence of the shorter one before the suffix copy. If a one-letter right extension is closed, its longest border is exactly one longer: stripping the final letter gives an original border, and any border no longer than the original one would have an intermediate copy at the original suffix start. The left analogue follows by reversal. Thus the next-copy, maximal-LCE and predecessor conditions used in the proof characterize precisely the non-singleton MCSs. Within a run the candidates reduce to the whole run. Across runs, a shorter residual first prefix reaches only the first eligible repeated run, whereas a shorter second residual has an intervening copy in the first run. For equal residuals in runs 1 and 3, left maximality forces t=min(a,c); the matched prefix crosses the first transition at the same offset in both copies, ruling out an intermediate copy. Runs 1 and 5 add exactly c<t<=a, because otherwise the central run intervenes. Runs 3 and 5 give the mirror three-run class; equal residuals in runs 2 and 4 always have matching predecessors, leaving only the central class 1<=t<b. The family sizes give the two cases of K. Splitting into a=c+r or c=a+1+r gives the two independent geometric-series products. The length inequality and residue-class witnesses give the stated maximum, with the lone length-five case equal to six. The independent script /workspace/branches/independent-finite-checks.py checked both endpoint sets and the actual rational-series coefficients, plus extrema, on all 168 triples through length 18. This is supplemental to the argument, not a proof of all lengths.

## originality

FAIL

A distinct indexed five-run result, SCOPE-20261122-fd3768a38473, covers the complete endpoint and count theorems by the direct specialization d=b, e=a and explicitly gives the same lengthwise maximum. The displayed bivariate series is a mechanical sum of the specialized count, not an independent surviving theorem. This is demonstrated mathematical coverage; the shared publication day does not settle relative priority or provenance.

## value

FAIL

Exact MCS endpoints and sharp extremal counts are useful invariants for run-length encoded words, but this standalone claim supplies no additional substantive invariant beyond the complete five-parameter classification. The symmetry restriction is a substitution and the bivariate series is a routine geometric sum from the covered count. No distinct valuable remainder was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
