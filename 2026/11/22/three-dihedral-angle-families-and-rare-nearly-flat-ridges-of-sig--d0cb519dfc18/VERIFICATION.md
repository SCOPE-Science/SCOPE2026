---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The known facet description is equivalent to row and column absolute sums at most one. Saturating same-support facets with h differing signs forces h coordinate zeros in addition to a row/column sum equality, so h≥2 is excluded. With h=1, filling the other n−1 entries uniformly gives exactly two tight facets for n≥3; at n=2 the unit entry forces a separate perpendicular equality. With different same-type supports the uniform fill has opposite sums 2/n<1 for n≥3. For n=2 both opposite sums must be one and the signs imposed by the two rows or columns fix an additional independent equality. Mixed-support sign disagreement forces the shared entry to vanish and a further row sign inequality to be tight independently; agreement admits a shared magnitude strictly between zero and one and a strictly positive distribution of the two remainders, so precisely those two facets are tight. A ridge has exactly two containing facets, as seen in a two-dimensional transverse section. Normal lengths are √n and the three inner products are 0, 1 and n−2. Counting distinct supports, matching shared signs, and Hamming-one edges of the sign cube gives the three multiplicities, including coincidence at n=3 and only the mixed class at n=2. Dividing by the total gives masses tending to 2/3, 1/3, 0; the rare mass is asymptotic to (2/3)2^(−n), so its contribution to the scaled mean is O(n2^(−n)). The small-angle formulas n arcsin(1/n)→1 and arccos(1−2/n)∼2/√n give both stated limits. Independently, exact integer affine ranks on every facet pair at n=2,3,4 gave normal-product histograms {1:32}, {0:384,1:360}, {0:3072,1:2048,2:256}. The proof, not the low-order replay, handles all n.

## originality

PASS

The hull, full facet model and general combinatorics of faces are prior work. The strongest same-object general result gives a dimension rule and the face lattice, but not an evaluation of codimension-two support types or a metric enumeration; the theorem on two-dimensional faces is not a ridge theorem for n≥3. The supported distinct claim is the explicit all-order classification in facet coordinates, the complete Frobenius angle histogram and its rare-class limit, not the exceptional n=2 shape or the general face machinery. No independent equivalent or dominating exact classification was verified.

## value

PASS

Ridges are the natural codimension at which this canonical realization has an ordinary dihedral angle. The exhaustive classification converts a general face model of a standard polytope into explicit metric data: no acute angles, a small excess at typical nonorthogonal ridges, and a separate exponentially rare almost-flat family. The exact family counts identify which faces cause the two scales; the contribution is not a small-n table or an arbitrary subsequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
