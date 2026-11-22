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

Signed weighted matrix-tree identity makes W_n(s)=reduced Laplacian determinant. Odd n Cayley n^(n−2) odd gives nonvanishing; multivariate Prüfer identity at vertex signs x with sum 1 yields magnitude 1. Even n reduced Laplacian has all entries odd: row subtraction makes determinant divisible 2^(n−2). Balanced vertex signs sum 0 give zeros; negated signings are disjoint, yielding at least C(n,n/2) zeros. Flip the signs of a spanning tree H among vertices 2..n from balanced factor signing; reduced Laplacian becomes M−yy^T, where adj(M)=(product of −2x_ix_j over H)11^T and sum y_i=−1. Rank-one determinant identity yields |W|=2^(n−2). Fourier diagonalization yields stated exact (pseudo)inverse norms and condition numbers. Independent complete Walsh-Hadamard enumeration for n=3,4,5 gave gaps 1,4,1 and zeros 0,30,0, including uniform even divisibility for n=4. These finite checks corroborate but do not establish the universal integer proof.

## originality

PASS

Martin–Reiner's multivariate Cayley weighted spanning-tree identity already implies balanced-sign zeros and odd unit witness, which are correctly background rather than new. The nearby published *First Walsh cancellation threshold for complete-graph spanning trees* studies minimum negative-edge support of **zero** characters, not least nonzero magnitude across all characters. The published *Dyadic Fourier gaps for complete rooted arborescences* has the same numeric gap for signings of independent **directed** arcs, but directed Fourier characters are a strictly larger signing domain than undirected symmetric edge characters; directed attainment does not show an undirected attainment witness. Here independent 2^(n−2) matching on edge-symmetric signings and exact convolution (pseudo)inverse norms survive these comparisons.

## value

PASS

The smallest surviving character multiplier is a natural exact arithmetic conditioning invariant for counting convolution on all labelled K_n trees; complete parity dichotomy and explicit extremal edge signings give genuine structural information not fixed by the zero-support theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
