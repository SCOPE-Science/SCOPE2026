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

The block shift of an idempotent must be zero, so its local maps are identities or constants. At prescribed shift k a commuting local map intertwines the two local idempotents. The rank enumerators for source/target types II, IC, CI, CC are 2z(1+z), z, 2z, z(1+z), independently of constant values. The two mixed type populations coincide, both d_k, because the shift preserves the total number a of identity blocks. Multiplication gives 2^a z^m(1+z)^(m−2d_k). The coefficient of z^m in the sum is m2^a; the shifted powers have distinct degrees and thus recover the histogram. Unit conjugation rotates blocks and independently changes constant values, giving exactly the stated orbit count. Summing choices of constants leaves 2^m per binary type, and the two eigenvalues 2+z,z of the binary cycle transfer give the divisor expression for every m≥1, including the identity shift. At z=1 the latter shift contributes 8^m; for L≥2, (3^L+1)^(1/L)≤√10 by monotonicity of log(1+3^−L)/L, giving the stated bound. The rank excess at identity shift is exactly binomial by its normalized generating function, and the mass of the other shifts is R_m/(1+R_m), giving the TV inequality. A fresh point-map enumeration checked all idempotents and each prescribed shift through m=5, recovering total counts 8,104,960,8320,64000; the total coefficients were checked against the divisor expression via m+1 positive evaluations after factoring z^m. Difference-set enumeration through m=8 confirmed the three cutoffs 5,6,8, the ordered vectors and distinct orbit conditions. The m=6 example is a reflection, not a rotation; the m=8 example has size 5504 and is genuinely non-dihedral.

## originality

FAIL

The earlier exact partial-translation commutant calculation in Resultary d8e52ca92e37 covers the central rank counts by an explicit rank-preserving reduction. At fixed type A and marked shift k its commutation condition is exactly B⊆{i:w_i=w_(i+k)}, where B is the domain of the partial translation. In the frozen model take B to be the blocks where the local map has rank 2. For a fixed e and k, there are independently two choices at each identity TARGET block for each allowed B, one choice at the other target blocks: for an identity source and identity target the rank choice leaves two maps; for a constant source and identity target the map is constant with two possible values; for a constant target the rank and intertwining force the map. Thus every old choice of B lifts to exactly 2^a commuting maps, with rank increased from |B| to m+|B|. Summing constant values across e replaces 2^a by 2^m uniformly. The earlier polynomial P_(C_m)(z) counts every empty partial map only once per A, whereas the frozen count keeps its m shifts distinct. Consequently F_m(z)=2^m z^m[P_(C_m)(z)+(m−1)2^m]. This is exact equivalence after the known empty-map correction, not just a similar counting method or a shared numerical sample. The commute-probability and binomial TV estimates follow by the same transfer summands and their identity-shift mixture. The Z8 pair is also explicitly known. There may be distinct finite fingerprint cutoffs at 5 and 6, but those do not make the frozen central rank/transfer claim original. The FAIL is demonstrated published coverage of that claim, not an access failure or a mathematical error.

## value

FAIL

Rank and loss of conjugacy information are natural observables here. But the frozen result's principal exact invariant and infinite-family census amount to a fixed grade shift, multiplicity, and empty-map correction to a known commutant count. The probability normalization and mixing bound then follow directly; the prominent m=8 witness is a translation of a tabulated Z-related example. The remaining m=5 and m=6 cutoff differences correctly locate loss of information from forgetting shift indices or reflections, but as presented are small checks of the inherited difference pattern and do not establish independent scientific value of the combined result beyond that conversion. A separately posed finite classification or more general nontrivial fiber result would require its own assessment. No narrowed or repaired claim is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
