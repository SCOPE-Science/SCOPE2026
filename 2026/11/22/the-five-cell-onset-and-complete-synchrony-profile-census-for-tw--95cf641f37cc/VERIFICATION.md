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

The receiving-row adjacency convention gives 15 possible rows at five cells; all 15^5 labelled matrices are partitioned into simultaneous-relabelling orbits. Reality and simplicity force a fifth eigenvalue r real and distinct from 0 and 2. Trace gives r, and monic polynomial division by t(t-2)(t-r) gives integer c>0 in t²+c. The frozen Newton-sum filter is exact. I independently generated the orbits before filtering, with 6874 five-cell and 475 four-cell orbits in the full row-sum-two universe. I matched the first two nonleading characteristic coefficients by trace and 2x2 principal minors, and the remaining polynomial by exact determinant evaluations: at 0 and 1 for n=5 (also at 2 by row sums), and at 0 for n=4 (also at 2). This gives sufficient distinct roots for the difference of degree at most n-3. For four cells the candidate is t(t-2)(t²+c). A partition is robustly invariant iff input multiplicities agree blockwise: sufficiency uses identical own-state and identical unordered input values in each block, and necessity follows by taking input sum as the admissible function and varying the independent block coordinates. Enumerating all 52 or 15 partitions, using exact transitive closures, and comparing both full computed catalogues and their orbit metadata to the supplied JSON yields 191 weak classes (21960 labelled) and 56 strong, with histograms (2,12,59,40,59,4,15) and (2,6,22,16,8,1,1), respectively. The two canonical matrices agree with the Finding and have orbit size 120, are strongly connected, and have r=-1,c=1. At four cells all nine weak classes have b>0, and fewer than four cells cannot have four distinct required eigenvalues. Replay: python3 /workspace/reproduce_reviews.py 4.

## originality

PASS

The supported distinct contribution is the five-cell synchrony distribution and the existence and classification of the two synchrony-primitive classes, hence the sharp onset within valency two. The established four-cell exclusion and the spectral five-cell totals are not new. The identical indexed target is not a separate result. Direct comparison found no source which supplies the five-cell b(G) data or makes them a consequence of the spectral totals.

## value

PASS

The exact first two classes without a robust synchrony reduction answer the natural next-size question after the four-cell obstruction. The complete profile measures how much quotient structure survives across the whole first eligible size and distinguishes graphs with identical spectra and connectivity. The result is not valued for rerunning the known 191-class spectral count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
