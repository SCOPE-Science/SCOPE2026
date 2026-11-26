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

Each tenth-root power has coefficients in {−1,0,1} in the basis 1,X,X²,X³ after cyclotomic reduction. A k-minor therefore has coefficient magnitudes ≤k!≤120. Evaluation at all four primitive tenth roots modulo 401 tests exact zero: a polynomial of degree ≤3 vanishing at four distinct points is zero in the field, and each integral coefficient is smaller in magnitude than 401. This equivalence for each minor makes the maximum of the four modular ranks the complex rank. A separate exact implementation verified the roots and replayed all 63,504 ordered row/column pairs, reproducing (0,0,0,240,6640,56624) for ranks zero through five, the nine displayed affine profiles on every orbit member, and zero mismatches of the rank-three criterion. Row affines act by column relabeling and nonzero column scalings, so the orbit weighting is legitimate. With parity-coset rows the entire fifth-order Fourier matrix appears with columns repeated according to residues modulo five, so rank is the number of occupied residues, giving the pattern (2,2,1,0,0). Choosing the three occupied classes, the singleton class and its representative gives 60 choices; either parity gives 120, and transposing gives a disjoint 120. The exact enumeration proves the converse. The frozen C++ programs and both saved JSON outputs were inspected, not executed.

## originality

PASS

The supported distinct contribution is the complete central order-ten incidence table, with the rank-three equivalence and the orbit profiles. A same-day result includes a general lower bound implying rank at least three here; that part alone is already covered in substance, irrespective of priority. Same-order full-spark classification says which rows always achieve rank five but does not enumerate the singular restrictions or partition their defects. Neighboring-order complete tables do not cover order ten.

## value

PASS

Order ten is motivated by the early failure of the Fourier full-spark residue criterion; size five is the central, square sampling problem at that order, not an arbitrary chosen slice. The nine exact profiles distinguish full recovery from one or two undetermined directions and show which row choices concentrate each failure. In particular the rank-three equivalence explains the worst loss by a parity/mod-five configuration, a useful benchmark for sampling or exact Fourier-minor work beyond knowing which rows are full spark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
