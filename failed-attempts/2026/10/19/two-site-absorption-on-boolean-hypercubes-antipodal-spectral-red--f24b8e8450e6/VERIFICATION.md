---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Walsh characters give d+1 distinct energy levels since J>0. The space spanned level by level by projections of the two sink vectors reduces both H and the loss operator; its orthogonal complement evolves unitarily. An eigenvector in the bright space with real effective energy would have zero amplitude at both sinks by taking imaginary parts and using strict positivity of the losses. It would then belong to a single H eigenspace and be orthogonal to both sink projections in that eigenspace, a contradiction. Dissipativity excludes positive imaginary energy and in finite dimension all bright Jordan blocks decay. For a nonantipodal pair and an interior Walsh weight k, choose one index in the support of s and one outside; keep a fixed k−1 subset of the remaining d−2 indices and exchange the two chosen indices. This produces opposite parities of overlap with s, so the signed count has strict modulus less than C_k and the interior Gram ranks are two. The extreme ranks are one. For antipodes the vectors are collinear in every level with sign (−1)^k. The Gram inverse with entries 2^(-d)(C_k,K_k(h)) and sink overlaps 2^(-d)(K_k(w),K_k(z)) gives the displayed localized probabilities, including 2/2^d from the extreme levels in the nonantipodal case. The normalized projection trace gives both dimension-five and general averages. Numerical evolution in the bundled script was inspected but not executed; the decay claim rests on the reducing subspaces and spectral argument.

## originality

FAIL

A distinct earlier-dated Resultary result states the same two-sink hypercube rank dichotomy and an equivalent complete sitewise law with identical model assumptions up to time and loss-rate conventions. The overlap is exact and stronger than the separate later rank-and-average result. It establishes indexed coverage, without deciding historical priority outside the catalogue or provenance of either derivation.

## value

PASS

The mathematical content identifies a natural trap placement where adding a loss site does not increase the absorbable space, while every other distinct placement gives the same dimension increase and a calculable localized efficiency. This is useful model information beyond generic bright/dark terminology, but the exact indexed match means the frozen package adds no distinct result on this point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
