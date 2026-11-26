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

Lucas identifies each row's support as a radix digit box. Independently, split a row n=a p^(r-1)+t into a+1 increasing copies of the support at t, shifted by successive multiples of p^(r-1). The within-copy gaps contribute A times the depth-(r-1) pooled histogram after summing over a; the a boundary gaps all equal p^(r-1)-t because each lower support begins at 0 and ends at t. Varying t covers each size 1 through p^(r-1) once and summing a gives B for each. Thus the depth-r histogram is A times the preceding one plus that flat contribution, starting from an empty depth-0 histogram. This verifies the full formula, including p=2, r=1 and the sharp cutoff. Row support sizes sum to A^r, and removing one endpoint per row counts A^r-p^r pairs; their lengths telescope to the row indices, proving the finite mean. The normalized limit is a probability law: it mixes the discrete uniforms on 1,...,p^i with weights (B/A)(p/A)^i, summing to one since A-p=B. The shell of p^i-p^(i-1) points gives the stated tail and a geometric s-moment term of order (p^(s+1)/A)^i, including divergence at equality. The moment claim concerns nonnegative orders. Independent direct binomial-coefficient enumeration agreed on six prime/depth cases; this is finite corroboration only, distinct from the supplied additive Pascal-row checker and its recorded CHECK_OK.

## originality

PASS

Best-of-current-evidence pass for the complete pooled nearest-neighbor spectrum, its specified limit and exact tail, not for Lucas support, its cardinality, or general Pascal self-similarity. The closest Pascal results count entries or optimize contiguous runs, while the nearest exact gap laws apply to other supports. The exact Pascal spacing statement was not established in the inspected comparisons.

## value

PASS

Within-row nearest-neighbor gaps distinguish a fractal's spacing from its support size and its longest surviving block. The exact finite spectrum for every prime and depth resolves every gap size under a natural pair-weighted ensemble; the exact normalized tail further explains why the limiting mean diverges even though every finite mean exists. The boundary-counting argument is elementary but the statistic and its heavy-tail cutoff are usable in studies of the Pascal support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
