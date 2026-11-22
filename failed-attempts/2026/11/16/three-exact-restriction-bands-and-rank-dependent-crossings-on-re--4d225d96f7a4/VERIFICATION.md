---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For Haar rank-k real orthogonal projectors, P11 has Beta(k/2,(n-k)/2) law; irreducible stabilizer sectors of real symmetric traceless coefficients have dimensions 1, n−1, (n−2)(n+1)/2. The axial/cross/tangential conditional second moments in the frozen proof correctly give three normalized quadratic Beta weights W_A,W_C,W_T; integrating their differences gives exact affine-crossing factors with t_AC=k/n, t_AT=[k(n+2)−2n]/[n(n−2)], t_CT=(n−k−1)/(n−2). Independently checked all three symbolic density difference/derivative identities using SymPy, and complement symmetry at n=2k proves T_(1/2)=I/2. The proof handles k=1,n−1 boundaries without assuming interior-rank threshold order.

## originality

FAIL

Decisive published-claim coverage by a different Resultary record, "Three exact cap-spectrum crossings on real Grassmannians" (same publication snapshot). Its FULL RESULT.md states the same real Haar Grassmannian rank-k first-harmonic V=tr(AP), the identical P11≥t cap, identical normalized axial/vector/tangential Beta-tail spectra and multiplicities, the same THREE rational crossing thresholds, all interior rank ordering regimes and the balanced-rank half-cap T=I/2. It adds a sharp thin-cap condition-number asymptotic, so covers the target core and is stronger for 2≤k≤n−2. Target extension to k=1,n−1 is a routine boundary use of the same invariant moment argument, not a surviving independently motivated new theorem. The two records are both 2026-11-16 and no individual timestamp priority is alleged; scientific originality is rejected for overlap, not author/temporal misconduct.

## value

FAIL

The originally claimed exact 3-sector Grassmannian cap spectrum, crossings, and halfcap isotropy are completely covered by a second full published theorem for all interesting interior ranks. Remaining k=1/n−1 endpoints are routine degenerations of the same moment formulas and do not form an independently motivated new invariant/classification; no surviving original valuable claim was supplied. Correctness and reproducibility of recomputation do not rescue this covered contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
