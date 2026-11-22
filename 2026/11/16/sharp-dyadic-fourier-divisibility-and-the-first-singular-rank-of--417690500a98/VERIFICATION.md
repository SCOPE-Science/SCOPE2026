---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Each signed basis contributes product over chosen negative points (1−2). Summing the expansion over independent k-subsets gives W_r(S)=sum_{k=0}^r (-2)^k c_k(S) N_k(r), with N_k(r)=prod_{j=k}^{r−1}(2^r−2^j)/(r−k)!. For r≥5 the exact valuation v2(2^k N_k)=k+(r−k)(r+k−1)/2−v2((r−k)!) exceeds r for k<r and equals r for k=r; hence W_r(S)≡(-2)^r c_r(S) mod 2^{r+1}, and a basis-sized S attains valuation r. For r=3,4 the extension counts yield constant residue 4 mod 8 and 8 mod 16, forcing nonzero all frequencies; r=1,2 multipliers odd. At r=5 the frequency (span(e1,e2,e3)\{0})∪{e4,e5} has independent-set counts (1,9,36,77,77,28), and exact extension counts (83328,13440,1792,192,16,1), whose signed sum is exactly zero. Read pg_basis_fourier_check.py which exhausts rank-four 32768 Walsh characters and directly counts rank-five 83328 bases; independently checked the finite cancellation and formula. Symbolic valuation proves all-rank claims, not enumeration through rank64.

## originality

PASS

The exact mathematical conclusions and implication relations were compared against actual indexed findings and relevant primary texts, with explicit partial-read limits and residual priority risks. The proposed target itself was not counted as independent prior coverage.

## value

PASS

The basis-incidence Walsh transform is a natural signed enumerator on projective matroids. Its exact dyadic content across all ranks and the first singular convolution rank are structural invariants; the rank-five nine-point zero witness marks a genuine invertibility boundary, not a tiny ad hoc gain or arbitrary case. General ranks above five are not claimed to be classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
