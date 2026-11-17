---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

On H(d,q) for d≥1,q≥3 the one-particle Fourier energy d(q−1)−q wt(u) gives bosonic total-momentum p and pair-energy t sectors. All symmetric momentum pairs in a nonempty (p,t) sector have a common nonzero coincidence Fourier character; thus exactly one bright vector per sector. Momentum p of weight w=0 permits d+1 even energy indices, and w≥1 permits each integer t in [w,2d], crucially using q≥3. Summation gives bright rank q^(d−1)((d+1)q+d)−d and dark dimension N(N+1)/2 minus that rank, including d=1 boundary. Localized capture follows by Fourier-orthogonal sector projection and root-of-unity sums Σ_{a≠0}|1+ζ^a|²=2(q−2), yielding stated finite rational coefficient sum. Independent numerical full bosonic spectral decompositions at (d,q)=(2,3),(2,4) gave dark ranks 14,82 and exact capture 13/18,1/2 and 11/24,2/9. Empty sectors correctly omitted, rates arbitrary positive. Tests corroborate only finite d,q.

## originality

PASS

PASS best-of-knowledge: all-q nonbinary two-boson coincidence-loss rank and local capture differ materially from the q=2 hypercube classification (its energy support has parity gaps) and from one-particle Hamming absorption. Bernard–Crampé–Vinet (2021/2023) work on the same graph H(d,q) but for free fermionic ground-state entanglement; it supplies adjacency diagonalization but has no bosonic all-site collision detector or loss law. Published related collision results on other networks do not dominate the q≥3 Hamming parameters. An unindexed general association-scheme two-body absorption result could entail this law, retained as risk.

## value

PASS

An exact all-dimensional dark-subspace classification and distance-resolved capture distribution for q-ary Hamming networks is a natural extension from Boolean hypercubes, but q≥3 produces a qualitatively different contiguous energy support, not parameter substitution. Explicit rational capture at all Hamming separations and arbitrary positive local loss rates provide precise physically relevant transport invariants. Complete H(2,q) specializations serve as meaningful boundary checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
