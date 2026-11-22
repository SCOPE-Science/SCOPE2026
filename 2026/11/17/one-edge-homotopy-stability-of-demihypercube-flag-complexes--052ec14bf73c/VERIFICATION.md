---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Let A=Cl(H_n-e), K=Cl(H_n). The common-neighbor edge link L has two (n-3)-simplices joined by n-2 disjoint cross-edges, hence L≃ wedge^(n-3) S1; independently enumerated this link for every n=4..10. The pair (K,A) has H3(K,A)=Z^(n-3) and zero other reduced relative homology. Four-coordinate even-parity cross-polytope S3 cycles containing e induce a unimodular basis of this relative H3, so H3(K)->H3(K,A) is surjective integrally and H3(A) injects primitively with rank B_n-(n-3). The full K is simply connected by parity-Cayley generators and filled squares, and Van Kampen for K=A∪(e*L) with simply connected ΣL gives A simply connected. By Hurewicz and homological Whitehead, A is wedge of the stated number of S3. Exact B_n and link ranks for n4..10 independently computed; these do not substitute for the all-n proof.

## originality

PASS

Green determines integral topology of intact half-cube complexes; Bendersky et al study full cube Rips objects. The exact one-edge deletion relative link map and split integral inclusion for parity half-cube are additional, not implied by a one-vertex deletion result (loss C(n-1,3) rather than n-3). No exact duplicate edge-fault theorem identified.

## value

PASS

All-order robust edge-deletion theorem for an intrinsically natural Hamming/demihypercube flag complex, including a canonical primitive homology inclusion and explicit lost cross-polytope generators, is structurally meaningful and usable beyond computing a few Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
