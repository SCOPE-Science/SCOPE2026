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

Theorem A of Takahasi–Yamamoto is the coding input; the counted objects are unrestricted finite blocks in the closed Dyck coding, not realized or periodic trajectories. Independently, a nonzero-reduction word decomposes uniquely at its unmatched brackets: all unmatched closers precede all unmatched openers, and the gaps are balanced typed Dyck words. A matched pair cannot straddle an unmatched bracket. With C=1+Mt²C² for one balanced gap, summing all numbers of unmatched closers and openers gives C/(1−MtC)². For q=tC this is the claimed OGF, using (1−q)(1−Mq)=(1+Mq²)(1−(M+1)t). For a check of the pole calculation put z=(M+1)t and r=Mq; then z=(M+1)r/(M+r²) and (1−z)²F=(M−r)²/[M(M+r²)]. At z=1 the analytic branch has r=1 and dr/dz=(M+1)/(M−1); the value and negative z-derivative of (1−z)²F there are (M−1)²/[M(M+1)] and 4/(M+1). The double-pole coefficients thus give the stated slope and constant (M+1)/M. The radical is holomorphic in |z|<(M+1)/(2sqrt(M)); r=1 forces z=1, with no other poles. Subtracting the principal part and taking a Cauchy radius 1/ϑ gives exactly the normalized remainder for fixed M≥2. Lagrange extraction gives A_{n,M}=(n+1)^{-1}∑_{k≡n mod 2, 0≤k≤n}(k+1)² M^((n+k)/2) binom(n+1,(n−k)/2); an independent integer evaluation for M=2 and n=0,…,9 matches the table. The entropy refinement follows by expanding the logarithm for large n, not at n=0. The frozen verifiers were inspected, not executed.

## originality

FAIL

A distinct Resultary record, 95f659142ec7 (2026/11/2), states the same unrestricted Dyck-language generating function for every alphabet size in scope and the same two-term asymptotic with a sharper error. The dimension-three wording does not give a different count once the previously established coding theorem is applied, and the logarithmic refinement is immediate from the shared coefficients. The failure is material equivalent coverage without an established distinct mathematical contribution, not a claim that the later-dated catalogue entry predates this frozen record or that historical priority has been settled.

## value

PASS

As a mathematical theorem, exact word complexity for this canonical nonsofic coding is a useful invariant. The linear factor and constant reveal finite-length behavior invisible to the known exponential entropy, across every M≥2 and all interior geometric parameters. The mathematical significance of that theorem is separate from its equivalent coverage in a distinct record; the dimension-three restatement and the entropy expansion are not separate advances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
