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

For connected noncomplete SRG with mu>0, the standard adjacency identity gives L(tI+A)=QI-mu J, with t=k-lambda+mu and Q=v mu. Thus the star-edge transfer-current kernel at root u is K=[tI+A(H_u)+(t-2)J]/Q, whose eigenvalues are 1 and (t+theta_j)/Q for j>=2. The determinantal UST edge law yields the exact rooted-degree PGF z product_j(1+(t+theta_j)(z-1)/Q); all Bernoulli factors nonzero since the entire star can occur in a spanning tree. Therefore fixed parameters allow recovering the neighborhood adjacency spectrum. The first two spectral power sums are fixed; trace A(H)^3=6 times neighborhood triangle count yields third factorial cumulant difference 12 Delta triangles/Q^3. The rook/Shri local graphs K3 disjoint K3 versus C6 give the stated exact PGFs, difference z(z-1)^3(5z+27)^2/2^23, third difference 3/4096. Independent exact polynomial factorization checked and original verifier’s weighted matrix-tree code was read.

## originality

PASS

General transfer-current determinants, Rapoport’s explicit UST degree distributions and Pozrikidis’s general spanning-tree degree generation are prior work and are not claimed new. Their accessible results do not state a fixed-SRG parameter-class local-neighborhood spectral inversion or the exact rook/Shrikhande third-cumulant separation. A fully inspected Resultary complete-multipartite UST root-degree inversion is for a substantially different graph class. Given the direct structural application of standard methods, priority remains qualified; no exact stronger theorem was identified.

## value

PASS

Recovering the entire local-neighborhood adjacency spectrum from one UST root-degree law is a natural inverse-graph invariant within an important spectral class. The rook and Shrikhande graphs give a sharp explicit distinction beyond identical global spectra and identical first two moments; the third factorial cumulant encodes local triangles. This is useful exact information rather than just a trivial evaluation of a general known formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
