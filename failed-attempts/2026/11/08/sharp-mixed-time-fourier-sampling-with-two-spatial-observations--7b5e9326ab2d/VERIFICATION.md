---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Writing the Gram operator as I+P_T−Q_B, principal bases for the two rank-two subspaces split the difference into two blocks with trace zero and determinant −(1−σ²), where σ is the corresponding cross-Gram singular value. Orthogonal pairs give ±1, common directions give two zeros per coincident angle when counted with the complementary dimensions, and the balance is n−4 zeros; this includes the double 1 in the n=4 singular case. The two cross-Gram squared singular values are 2(1±|cos(πab/n)|)/n by the squared row lengths and the inner-product modulus. The smallest and largest frame eigenvalues sum to 2; singularity is ab≡0. The optimum selects the available residues closest to n/2, all attainable using a=1. For nonzero a of gcd d, ab=k has d solutions if d|k and none otherwise; excluding b=0 removes one only for k=0, and there are φ(n/d) choices of a. Multiplying by n² for origins and dividing by four for the two orderings of each unordered pair gives the two counts. Taylor expansion gives the stated second-order coefficients, and the eigenvalue ratio under a square root is the spectral condition number. Private replay: python3 /workspace/branches/check_fourier_spectrum.py (NumPy). It checked all eigenvalues for 501 difference pairs and independently enumerated unordered counts for n=4..12. The frozen checker builds full matrices but asserts only the two extreme eigenvalues and their sum; it was inspected, not executed. The finite checks, including the new checks of the entire multiset, supplement the proof.

## originality

FAIL

The earlier two-character harmonic-frame record e1e03f96b6f0 gives a stronger subset-dependent spectral formula in its Proof §1. Its two-erasure removed operator is, up to the factor 2/n, the Fourier cross-Gram square of the frozen problem. The classical projection-angle map therefore gives the full mixed spectrum from that exact prior spectral profile. Counting the singular placements is also an explicit specialization of its worst-mask count for size two or a repeated-phase count. The full optimum classification counts the same already known phase classes at nearest-antipodal rather than coincident/adjacent separation; this yields the remaining formulas mechanically. I did not find an earlier printed statement of the complete mixed-sampling theorem in this notation, and the distinct later four-erasure record is not prior art. The failure is for coverage by implication, not for identical titles or inaccessible sources.

## value

FAIL

The placement and conditioning problem is natural, and the formulas can be used as a sampling example. However the independently useful spectral datum is already available in the earlier subset profile via an exact known change of variables. The proposed remainder is the closest-to-antipodal two-phase selection, counting pairs with equal class capacities, and expanding its cosine formula; these do not constitute a separate nonmechanical result. No stronger independent sampling classification is established in the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
