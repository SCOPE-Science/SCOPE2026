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

For real n-vectors modulo constants the layer-cake/coarea identity represents arbitrary x by nested indicator cuts with exactly additive G_n(x), so the maximum over all cuts equals the quotient norm. The column values g_j=(n+2j−1)(H_n−H_{j−1})−2(n−j+1) follow from the lower-triangular Cesaro matrix; monotonic g_j is proved by D_j(n)=n+1−2j sum_{i=j}^n1/i≥0. Triangle bound reduces every k-cut to (sum_{j<=k}g_j)/[k(n−k)], and complement reduces to k<=n/2. The exact harmonic gap F(n,k)>0 comes from a strict positive difference for n>=2k and 17 rational base cases k=5..21 plus explicit log lower bounds for k>=22. Independent exact-rational enumeration of every nontrivial cut for 2<=n<=8 reproduced sharp values 1/2,2/3,29/36,37/40,103/100,118/105,2369/1960 and confirmed the harmonic anchors and n<100 gaps. e1 attains formula ((n+1)H_n−2n)/(n−1); monotonic increase and n=6 instability follow from its exact expression. Finite check alone is not an all-n proof; the harmonic estimates fill that gap.

## originality

PASS

The finite complete-pair Gini quotient norm is not the bv_p sequence norm or adjacent variation studied by Akhmedov–Başar; their Theorem 3.1 norm 1 includes constant vectors and uses successive differences, while this exact norm crosses 1 at n=6 and grows logarithmically. The separately published finite Cesaro residual I-C_n threshold is a different signed operator and its norm does not determine ||C_n||_G. Resultary matching semantic search primarily retrieved this finding and distinct averaging kernels, not an antecedent with the identical finite harmonic constant. This supports best-of-knowledge original exact Gini characterization, with possible historical unindexed forms still a risk.

## value

PASS

Complete-pair Gini dispersion is a natural measure of inequality/consensus distinct from adjacent-edge variation. The exact all-n norm formula, extremal one-coordinate signal, sharp onset n=6, and logarithmic instability quantify a meaningful norm incompatibility under a widely used averaging matrix. This is not a numeric slice or renaming of a standard l^p norm and may be needed to certify finite population disparity gains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
