---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Reconstructed L=2^d-W as the count of removed simplex-corner representatives, indexed by binary vertices. For two losses, deficit sum >= Hamming distance, while each deficit sum <a<1; hence Hamming distance=1. Three pairwise adjacent binary vertices cannot exist, so L<=2 for every d. Each of d 2^{d-1} cube edges has coincidence volume 2h^d/d! where h=(a-1/2)_+, so p2=2^d h^d/(d-1)!; E[L]=2^d a^d/d!, p1=E[L]-2p2 and p0=1-p1-p2. Integer Fourier coefficients of W equal those of the polytope and Parseval yields Var(L)=E[L]+2p2-E[L]^2. Differentiating the nonanalytic term 2^{d+1}h^d/(d-1)! produces jump 2^{d+1}d at order d. Positive-measure support arguments and h->1/2 supremum checked. Independently sampled 20,000 uniform torus points at (d,a)=(3,.2),(3,.75),(4,.75),(5,.95); all removals <=2 and frequencies near analytic masses. This Monte Carlo does not establish the universal theorem; the graph/simplex proof does.

## originality

PASS

Best-of-knowledge PASS after separate formulation/implication comparisons, published-result search, and bounded primary-literature inspection; not a certification of absolute historical priority. No identified prior theorem yields the exact three-level law across all d>=3 by direct specialization; mathematical reduction and distinct necessary inputs were checked. Priority remains bounded.

## value

PASS

An all-dimensional overlap obstruction remains exactly two despite exponentially many cube representatives. It gives a complete, nontrivial lattice covering multiplicity law and sharp nonanalytic Fourier-energy order, a motivated invariant for a canonical corner-truncated body; the planar d=2 result does not imply these general-dimensional facts. Finite mesh cases were not treated as a novelty or value certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
