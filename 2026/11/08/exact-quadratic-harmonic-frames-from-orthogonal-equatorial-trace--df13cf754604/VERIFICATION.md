---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Represent H2 by complex symmetric trace-free d×d matrix A. Probability fourth moment yields ||f_A||²=2||A||_F²/[d(d+2)], while each coordinate equator has energy [2||A||²−4||row_i(A)||²+3|A_ii|²]/(d²−1). Averaging the k equators gives K[2k−4 selected-row mass/||A||²+3 selected-diagonal mass/||A||²], K=d(d+2)/[2k(d²−1)]. Off-diagonal pair (i,j) with s selected indices is eigenvector with factor 2(k−s), multiplicity binom(d−k,2),k(d−k),binom(k,2) for s=0,1,2. On diagonal trace-zero matrices the factor is 2k I−P_VP_I P_V, whose projection compression has eigenvalues 1 (k−1), 0 (m−1 when m>=2), m/d (one if m>0). Total multiplicity d(d+1)/2−1 and all d>=3,k=1..d boundaries check. For k<=2, x1x2 vanishes; for k>=3, minimum K(2k−4)>0. Largest factor 2k−1 (m=0), 2k−1/d (m=1) or 2k (m>=2), giving all stated ratios. Arbitrary positive equator weights give a selected pair eigenvalue d(d+2)(1−w_i−w_j)/(d²−1); largest pair mass exceeds 2/k unless weights uniform, proving unique maximin. Convexity λmax and concavity λmin under permutation averaging prove uniform minimizes ratio, without asserting uniqueness. Independently built 42 full generalized eigenvalue matrices d=3..9, 60 random weights, 102 bounded cases passed, max spectral error 1.78e−15. Finite checks do not establish all d; matrix derivation does.

## originality

PASS

Best-of-knowledge novelty PASS for the exact k-orthogonal continuous trace frame spectrum and weighted optimum, not for standard spherical fourth moments or the two-orthogonal-equator kernel. The same-day published two-oblique-equator theorem is closest but covers different measurement geometry. Full primary HTML inspections of Xiao-Zhuang, Quellmalz et al, Quellmalz 2020 and Michel-Plattner-Seibert found nonidentical operators. No indexed dominating result identified; not a proof of historical priority.

## value

PASS

A finite collection of continuous equator restrictions is a natural stable observation design for quadrupole fields. The theorem determines the exact universal minimum number of MUTUALLY ORTHOGONAL equators (three), all d,k spectral degeneracies, dimension-independent sqrt(3) sharp conditioning for three when d>=5, and uniqueness of the optimal lower-bound weights. The k=3 strict finite-trace recovery versus k=2 orthogonal nullspace is a meaningful geometry/measurement boundary, not an arbitrary slice or mere numerical repetition; complete optimizers and quantitative stability are useful for reconstruction and benchmarking. Does not claim optimality over nonorthogonal designs: two oblique traces already suffice in related prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
