---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof reduces binary 2-binomial signatures at a fixed weight to the scattered \(01\)-count. The successive rotations change this count by \(-k\) or \(n-k\). After scaling by \(d=\gcd(n,k)\), the resulting walk has increments \(+a,-b\) with coprime \(a,b\). Distinct residues modulo \(a+b\) give the lower bound; existence of a balanced cyclic window yields an inductive upper bound; direct height-set counting provides an extremizer.

To reproduce finite checks, run \`python3 verify.py\` with Python 3.8+ and no nonstandard dependencies. The code independently computes all scattered pattern counts up to length two for all rotations of all 8,166 nonconstant binary words of lengths 2 through 12. It checks exact minima and maxima for every nontrivial weight, the characterization of every minimum equality case, and both extremal constructions. The local run produced \`VERIFY_OK\`.

Finite enumeration does not certify the infinite-range claim. That claim is justified by the complete induction and arithmetic arguments in RESULT.md. The verification has not been independently audited.
