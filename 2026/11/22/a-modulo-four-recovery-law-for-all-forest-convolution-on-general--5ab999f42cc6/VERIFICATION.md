---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Every cycle uses two whole arms because each internal vertex has degree two; a spanning forest may have isolated vertices and may use zero or one whole arm. At a Walsh frequency, the total signed weight over an arm is 2^ell on a zero block and zero otherwise. Subtracting the full-arm sign s_i gives the proper-subset weights d_i=2^ell_i-1 on zero blocks and -s_i elsewhere. The zero/full-arm split gives exactly (1); factor all proper-subset weights to get the bracket 1-k+z+sum_{i in Z}1/d_i, proving (2)–(3) with its stated global sign. For z=0 the empty sum contributes nothing; for z>=1, d_i=-1 modulo four and the z-dependent terms cancel, giving (4), including its frequency-parity sign. Thus all k outside 1 mod 4 are universally invertible, while k=4t+1 with all ell=2 and z=3t gives an exact zero. Distinct zero-block sets partition the full 2^N characters and each has multiplicity product_{i notin Z} d_i. At k=5, z<=2 gives too small a reciprocal sum and z>=4 gives a positive left and a nonpositive right; z=3 forces three length-two arms. In the equal-length case the equation solves to z=(k-1)(2^L-1)/2^L, admissible and integral exactly at 2^L|(k-1). The Walsh basis diagonalizes unnormalized counting convolution, so the nullity computation is on the stated whole space. Independent replay (python3 /tmp/opencode/ordinal1-spectrum-check.py) uses DSU cycle detection on every edge subset and an integer Walsh transform, rather than classifying subsets by completed arms; it confirmed all 284,032 coefficients over the six cases and nullities 0,0,90,49,0,2268, including 49 for lengths (2,2,2,3,3). The deposited verifier uses the arm-partition test and agrees in finite scope; no finite experiment establishes the general criterion.

## originality

PASS

The forest enumerator, signed weight evaluations and Fourier diagonalization are prior machinery. Bounded comparison supports the specific modulo-four universal inversion boundary with a matching singular family, the Mersenne-reciprocal per-instance zero criterion and resulting rank/nullity, not a priority claim for enumerators or Fourier methods.

## value

PASS

On a natural entire series-parallel subfamily and all acyclic edge sets, the result identifies an exact universal obstruction, not just a finite spectrum or choice of frequency slice. It distinguishes, for every exceptional branch count, an explicit singular graph from the universal nonexceptional classes. The exact zero multiplicities determine how much data is lost for any given arm lengths, and the five-arm transition specifies when lengthening an arm removes all loss. No full unequal-length Diophantine classification or sharp surviving gap is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
