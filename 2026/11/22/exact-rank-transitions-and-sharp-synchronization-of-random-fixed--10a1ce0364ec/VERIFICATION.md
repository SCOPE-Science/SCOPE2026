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

A rank-r idempotent fixes exactly its r roots. Its uniform law is uniform over root sets B followed by independent uniform assignments of nonroots. For a fixed s-point current image, intersecting B gives a hypergeometric root count a; after choosing t-a fresh roots, inclusion–exclusion forces each to be hit while allowing hits to the a fixed roots. The count is valid at a=t and s=a as well, and sums to a stochastic row. Conjugation makes the conditional rank transition depend only on s, even conditioning on the whole preceding history, so the initial row r evolves by Q^(k-1). The full law is conjugation-invariant, hence each constant has mass Pr(rank=1)/n and the full-monoid variation distance to uniform constants is exactly Pr(rank>1), including k=1 and zero constant mass. Nested injection events give strict diagonal decrease: choose r roots containing s-1 specified points but not the added point (r<n), which can collide with one of those s-1; the event all s are roots gives positivity. Pair failure is 1/r times the probability not both are roots, yielding the stated lambda2. The transient chain has distinct positive diagonals. Its normalized right eigenvector at lambda2 satisfies the claimed recursion with positive terms at the preceding rank; the left eigenvector is the coordinate row for rank two. That projector gives the sharp amplitude and the remaining eigenvalues give the fixed-parameter error at lambda3. Rank two is exact and the n=4,r=3 example follows from Q_33=1/2 and Q_32=1/2. Independent bounded replay python3 -B /workspace/evidence/check_1.py builds idempotents by filtering all maps, exhausts ordered words through length three for the six pairs 3<=n<=5, and compares with a hit-count recursion and the inclusion–exclusion kernel. The all-parameter result uses the proof, not extrapolation. No prescribed nonconstant fibers or uniform growing-parameter asymptotics are claimed.

## originality

PASS

Best of inspected evidence for the general same-rank retraction model and its evaluated rank and constant-target laws. Credit the binary merger special case r=n−1 to the classical pair-coalescent/Moran-type mechanism; neither that case nor the general spectral projection principle is a distinct discovery. The general fixed-rank law includes several possible jumps when r>=3 and n−r>=2 and its retraction-specific positive leading coefficient is determined by the evaluated transition probabilities. The closest distinct same-day matrix and diagram laws do not induce this kernel. The bounded literature comparison is not a priority determination.

## value

PASS

Uniform fixed-rank retractions are a natural random multiplication model with forced fixed points and correlated mergers. The exact transition probabilities recover finite-time rank and constant-fiber statistics and determine the full-monoid synchronization distance. The leading coefficient distinguishes the precise asymptotic from just an exponential bound or an absorption assertion. Value lies beyond the corank-one binary case and is limited to fixed-parameter sharp asymptotics, not a cutoff or a solution for all product fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
