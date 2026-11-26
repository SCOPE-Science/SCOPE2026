---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The two complexes of neighborhoods centered on a single shore intersect in exactly the graph (including every vertex); each unique apex collapses relative to its nonempty simplex base by pairing apex faces with and without a chosen base vertex. The remaining complex is the dual of Ind(C_n) since a complement must contain an adjacent pair. The full 2-skeleton follows from ceil(n/2)>3. Integral Alexander duality and the cycle independence formula put free reduced homology in just one degree r=n-3-dim(Ind(C_n))>=3 (r=2k-2,2k-1,2k-1 in the stated cases). Hurewicz and homological Whitehead give a wedge in that degree. The bipartite overlap is connected by the common-neighbor argument and its cycle rank is n(n-2)-2n+1. Maps from a connected graph to either simply connected shore are nullhomotopic, and the cofibrant union is the corresponding homotopy pushout, with reduced suspension of the graph as third summand. Independently generated closed-neighborhood faces and reduced their binary boundary matrices for n=7,8,9, obtaining nonzero reduced Betti entries {2:22,3:2}, {2:33,3:2}, {2:46,4:4}; this checks examples only, not integral homotopy. The packaged checks/verify.py and its recorded output are supplementary evidence, not a substitute for the argument.

## originality

FAIL

The earlier published two-factor-complement result explicitly gives the *unsuspended* wedge and covers the entire frozen theorem by taking just one forbidden cycle. This is a scientific overlap, not a negative inference from failed access to a full text. The published statement contains the hypotheses, dimension and multiplicities needed for exact specialization.

## value

FAIL

A complete integral wedge classification for this graph family would be useful as a new result, but the frozen claim supplies only the one-cycle substitution in the already published two-factor wedge law. No distinct invariant, useful new range, equivariance result, or independent substantive advance is established. It can serve as an exposition or worked example, not as a standalone new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
