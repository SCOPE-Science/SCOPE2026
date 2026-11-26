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

Burnside's basis theorem identifies generation with spanning G/Φ(G); when n=1 a nonzero alternating pairing forces the two images to span, and when n≥2 two images cannot span. The class-two commutator is bilinear and alternating (also for p=2); its radical is zero by the definition of the center. Each projective point therefore has an independent fiber of p(p−1) elements, with complete adjacency precisely across nonorthogonal points. Counting nonzeros outside one hyperplane, and then outside two distinct hyperplanes, and dividing by p−1 gives k=p^{2n−1} and the common-neighbor count c=p^{2n−2}(p−1). Thus A²=(k−c)I+cJ on the entire base space, giving eigenvalues ±p^{n−1} on the all-ones orthogonal complement, with multiplicities from dimension and trace. The full matrix A⊗J_{p(p−1)} scales those eigenvalues and adds the stated zeros. Positive k and c imply distance at most two, attained by distinct same-fiber vertices. Nondegenerate alternating forms are isometric at fixed p,n, and D/R=p^n recovers p,n by the stated formula for n≥2. The rank-one spectrum is entirely zero, with p³−p vertices. The packaged finite checker was inspected and is supplementary; the proof is uniform in p,n.

## originality

FAIL

A distinct Resultary record already constructs the identical projective independent-fiber model of the extraspecial noncommuting graph, including type-independence. For n≥2 the nongeneration condition is automatic. All displayed numerical invariants and reconstruction follow by standard symplectic incidence counts and adjacency-matrix rules, not by a new structural result. The n=1 exception follows from the fact that all proper subgroups have order at most p² and are abelian.

## value

FAIL

The isomorphism type and spectrum are natural invariants, but the exact graph and its type-blindness are already supplied by the projective-fiber model. The spectral list and parameter recovery are mechanically implied by that model's standard incidence and blow-up calculation, and the small-rank case is a direct generation/abelian-subgroup check. Neither is a substantive surviving standalone advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
