---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For tau(0)=001,tau(1)=110, writing +1 for zero and -1 for one gives W_(k+1)=W_k W_k (-W_k), with total weight one and exact prefix extrema M_k=k+1 and m_k=min(0,2-k). Every length-n<=3^k factor crosses at most one two-supertile boundary, so direct partial-prefix differences constrain its signed sum to [-2k-1,2k+1]. Fixed parity thus gives at most 2k+2 distinct Parikh vectors. The adjacent aligned block U_k overline(U_k), which occurs since 01 occurs in the underlying word, realizes signed weight -(2k+1) by choosing prefix maximizing P_k; complement closure of the factor language realizes +(2k+1). Sliding windows interpolate all intermediate counts, proving exact rho(3^k)=2k+2 and max for n<=3^k, hence global logarithmic envelope and limsup=2. Direct construction from the substitution independently confirmed counts at k=0..6; these finite checks do not replace the exact supertile argument.

## originality

PASS

Best-of-knowledge original within the precise domain and invariant, based on actual relevant mathematical comparisons; source access limitations and priority risks are retained.

## value

PASS

This natural base-three binary digit-parity fixed point provides a sharp and quantitatively exact logarithmic Abelian-complexity envelope with a precisely attained scale subsequence. It resolves a motivated special morphism parameter within a broader automatic-complexity problem, and the simple supertile proof can serve as a structural benchmark for morphic discrepancy. No general all-n exact sequence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
