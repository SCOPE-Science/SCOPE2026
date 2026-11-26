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

Reflecting the odd ideal-indicator coordinates sends x_odd>=x_even on each cover to y_odd+y_even<=1, giving the full-dimensional path stable-set polytope. Two independent-set words that differ on several components admit component swaps with the same midpoint, so are not adjacent. For a single difference interval, common zeros are fixed by nonnegativity, common ones by a tight equality to an adjacent common zero, and alternating entries on the interval by tight neighbor sums leaving one parameter. A flippable interval hitting a cluster of k ones may take any ordered pair of its one positions as endpoints, or use its available flanking zeros, giving k(k+1)/2+k(a+b)+ab choices. Intervals not hitting a one consist of single zeros not adjacent to a one. Subtracting the disjoint augmented cluster spans and adding the cluster contributions gives n+sum binom(t_i,2) with t_i=k_i+a_i+b_i-1. A zero correction permits only isolated endpoint ones; for n>=3 all four indicated words exist. For c nonempty clusters, augmented spans have lengths at least 2t_i-1, so if T=sum t_i then T-c+1<=(n-c+2)/2. Merging A,B>=1 loses (A-1)(B-1) in the binomial sum. Thus equality for odd n needs one cluster; its span fills the path with a=b=1. Even n also excludes c>=3. If c=2 at equality each span must be length 2t_i-1, forcing a_i=b_i=1 for both, so t_i>=2 and merging is strict. The remaining single even cluster has t_i=n/2, filling the path for a+b=1 or leaving exactly one endpoint outside its span for a+b=2. These give the two plus two displayed even words. The all-zero word has degree n, and the path Fibonacci recurrence yields the asserted simple-vertex fraction.

## originality

PASS

The evaluated cluster formula and full classification of simple and maximizing vertices are distinguishable from the known adjacency criterion, connected-block edge census, and an earlier incidence formula that gives the degree of the empty ideal (already yielding the even maximum value at one vertex). Neither computing that one degree nor knowing the average or an algorithm for individual incidences states the sharp upper bound and exhausts the equality cases. The pass concerns the evaluated structural classification only.

## value

PASS

The same Fibonacci-sized family has only four simple vertices but vertices of quadratic degree, versus the known linear average. The explicit cluster correction and parity-rigid equality classification explain this spread and allow individual degrees to be read off without enumerating neighbors. This is more than calculating the degree of a known highly symmetric vertex or recomputing a global count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
