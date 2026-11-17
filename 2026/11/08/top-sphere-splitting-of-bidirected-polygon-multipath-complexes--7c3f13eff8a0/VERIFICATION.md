---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For n≥6 the underlying cycle has n+1 vertices. A maximal n-arrow multipath is a coherent directed Hamilton path because any opposite-arrow pair makes a directed 2-cycle and a spanning path has uniform orientation. Thus the only top (n−1)-simplices are n+1 clockwise and n+1 anticlockwise faces; the disjoint top-chain boundary kernels are primitive Z-cycles of the two embedded boundaries ∂Δ^n. CCS Theorems 2.8,2.10 (read) yield ν=floor((n−1)/2)−1 connectivity and exactly H~_q=Z^r and H~_(n−1)=Z², where q=floor((n−1)/2)+[4|n], r=3 iff n≡3(mod4). If 4|n, H~_(ν+1)=0 and simply connected Hurewicz upgrades π_(ν+1)=0, giving (q−1)-connectivity. Hurewicz represents an integral basis of H_q by q-spheres, together with the two geometrically included top spheres; the resulting homology isomorphism of simply connected CW complexes is a homotopy equivalence by homological Whitehead. n=6 finite direct enumeration independently found 477 faces incl empty, mod2 H~_2 rank1 and H~_5 rank2. This finite check is corroboration, not the unbounded proof.

## originality

PASS

Best-of-knowledge PASS: the published integral groups and connectivity are inputs, not new. The two primitive top spherical classes and Hurewicz–Whitehead map establish the homotopy type that CCS Section 3 raises as an open question. The earlier published dihedral rational character uses these same top cycles but does not establish the integral wedge homotopy equivalence.

## value

PASS

A complete integral infinite-family homotopy type resolves an explicit open wedge question for the natural bidirected polygon multipath complexes. It is strictly more useful than Betti ranks because it determines higher homotopy information and realizes the top generators as actual embedded spheres; no equivariant splitting is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
