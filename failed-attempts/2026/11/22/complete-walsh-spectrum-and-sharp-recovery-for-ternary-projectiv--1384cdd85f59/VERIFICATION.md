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

There are 286 triples minus 13·4 collinear triples, so 234 unordered bases; each point is in 54 and each pair in nine bases. Expanding the product of three Boolean signs gives the multiplier 234−108k+36·binom(k,2)−8·binom(k,3)+8t(S), where t(S) counts the collinear triples in the k-point subset. The expansion gives residue 2 modulo four, and complementing S changes the sign because bases have odd size. Independently I constructed the plane as the affine 3-by-3 grid with four directions at infinity, checked the unique line through each pair, removed each line's triples, and summed the signed basis contributions directly at every one of 8192 masks. This reproduces all k≤6 incidence shells, all 16 signed levels with their multiplicities, and the stated −2 witness in the frozen labeling. The trivial character gives 234 and the triangle inequality bounds all moduli by 234. The orthogonal Walsh basis gives rank 8192, inverse norm 1/2 and condition number 117 in counting convention. The integer matrix determinant is the product of all eigenvalues, all of exact valuation one, hence has valuation 8192.

## originality

FAIL

The spectrum is correct but already covered by a short implication from the distinct same-day Resultary result 17c865f9e680 for the exact same PG(2,3) line design. That result gives precisely 234 proper bicolorings with six points of color 1, none with five. Those two exact facts determine the missing five- and six-point incidence distributions using the first two line-intersection moments and elementary count identities. The smaller shells already follow from elementary incidences (the four-arc slice also has independent exact overlap). Hence all sixteen signed levels, their multiplicities, and the sharp recovery constants are covered, despite different terminology and no explicit spectral table in the bicoloring result. This is an implication judgment, not an inference of publication priority from same-day dating.

## value

FAIL

The convolution and its sharp gap are natural mathematical quantities. For this narrow finite result, however, the entire announced exact census and recovery data are mechanically recoverable from an existing exact bicoloring census by the displayed incidence identities. There is no demonstrated new invariant calculation left over, no broader result, and no substantive surviving claim to repair; an additional certificate or repackaging the covered data does not supply value under the finite-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
