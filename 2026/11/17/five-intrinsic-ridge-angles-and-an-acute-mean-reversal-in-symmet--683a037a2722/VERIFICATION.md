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

Proof constructs explicit strictly positive except two zero coordinate witnesses for each pair n>=4; for n=3 diagonal/incidence pair forces further vanishing and is not a ridge. The row-sum tangent projection P=I-R*(RR*)^-1 R with RR*=nI/2 + 11^T/2 gives norm-squared DD (n-1)^2/n², off D/(2n²), and five unnormalized projected products 1/n²,-(n-1)/n²,1/n²,-(n-2)/(2n²),1/n². Interior angle cosine is minus normalized product. Counts DD C(n,2), DOinc n(n-1), DOnon C(n,2)(n-2), OOshared n C(n-1,2), OOdisjoint 3C(n,4), except DOinc removed for n=3. Exact arcsin convexity yields mean angle sign for n>=4 and n=3 formula positive. OOdisjoint weight 1-O(1/n) and +2/n² angle, OOshared weight 4/n and -1/n angle, hence n² random limit 2, mean -2, n³variance 4. Independent numerical checks across n=3,4,5,10,100,1000 and inspected exact fraction inverse Gram code for n=3..7 support but cannot prove all n.

## originality

PASS

Brualdi-Cao classify symmetric stochastic matrix vertices and dimension, not pairwise Frobenius ridge dihedral angles. De Jong-Wulkenhaar compute volume of prescribed-diagonal slices rather than variable-diagonal ridge spectrum; only abstract was read for that source, so cannot claim a comprehensive noncoverage inspection. Resultary symmetric-edge/transportation angle calculations are different polytopes. No full same-object prior angle table located, qualified against unindexed sources.

## value

PASS

Complete intrinsic Frobenius ridge geometry of natural symmetric Birkhoff-like polytope, with sharp n=3 exception and rare acute ridges reversing the sign of an overwhelmingly obtuse angular law. The distinction between typical and mean angle matters for random ridge/metric curvature research; not merely facet counts or a negative tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
