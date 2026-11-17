---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For identical unit utilities an EF full allocation necessarily partitions nq goods into bundles of q. Each mixed induced bundle is K_{j,q-j}; a radius-one dominating vertex exists precisely for j=1 or q-1, whereas any 1<=j<=q-1 is covered by one radius-two vertex or two radius-one vertices. Counting labeled class assignments yields N11=binom(n,t)a!b!/((q-1)!)^n for integer t=(a-n)/(q-2) in [0,n], and N12=N21=a!b![x^a](sum_{j=1}^{q-1}x^j/(j!(q-j)!))^n. For q=4,a=b=2n parity makes t=n/2; dividing coefficients reduces to the centered -1,0,1 walk with probabilities 2/7,3/7,2/7 and variance 4/7. Its span-one Fourier local CLT with the central binomial Stirling estimate gives ratio (4/sqrt7)(4/7)^n. These arguments cover q=3, arbitrary positive a,b, boundary t=0,n and even-subsequence restriction; direct n=3 K6,6 count 0 vs 29,700 corroborates finite case.

## originality

PASS

Existing compact-fair-division and star-partition work covers the model and bare arithmetic center feasibility. It does not, in the material inspected, provide this labeled factorial-coefficient census, equality of two different budgets, or the sharp (4/7)^n conditional fraction. The count is more than renaming the earlier existence criterion; this is best-of-knowledge originality, subject to older star-factor enumeration overlap.

## value

PASS

The first natural bundle size where strict-radius feasibility develops gaps is q=4. The exact distribution of all fair allocations under different compactness budgets measures scarcity rather than mere existence; an exponentially small tight-budget fraction has direct combinatorial and fair-allocation significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
