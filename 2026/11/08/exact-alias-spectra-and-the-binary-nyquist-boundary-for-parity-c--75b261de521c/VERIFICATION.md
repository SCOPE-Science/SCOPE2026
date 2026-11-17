---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Finite-abelian character orthogonality on C=ker(sum:A^n->A) makes R*R a disjoint union of all-ones Gram blocks indexed by diagonal-character cosets. Orbit block length equals number of character symbols with multiplicity >=s=n-r. The block eigenvalue is t, hence j=1..min(q,floor(n/s)); multinomial exponential-generating function counts their multiplicities after dividing by q. Distance n between distinct diagonal-alias words gives injectivity iff 2r<n. Minimum maximal q-symbol occupancy ceil(n/q) gives surjectivity iff r>=n-ceil(n/q). Both yield binary odd middle unitarity; balanced two-symbol occupancy yields (q-1)/2 binom(n,n/2) kernel dimension at first alias. Independent finite direct enumerations for q=2..5, n=2..6 and all radii corroborate the unlimited character argument.

## originality

PASS

Character annihilators and diagonal coset aliases are classical, not claimed new. The exact occupancy-level squared singular spectrum, its complete multinomial multiplicities, boundary radius rank criteria and odd-binary unitary phase for this deterministic Fourier mask are not supplied by the inspected prior random-matrix or Hamming-sphere results. Best-of-knowledge qualified by possible stronger code-coset enumerator analogues.

## value

PASS

Single checksum sampling is a basic natural experimental design and coding observation constraint, while low-degree Fourier support represents interaction order. Full singular multiplicities, exact rank and kernel, sharp identifiability/onto thresholds and the exceptional binary unitary case are information beyond the trivial annihilator identity and may be used directly to design or diagnose finite sampling schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
