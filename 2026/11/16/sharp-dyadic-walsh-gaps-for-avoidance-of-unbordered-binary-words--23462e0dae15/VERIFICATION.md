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

Unbordered w of length k has no overlapping occurrences; inclusion-exclusion over compatible length-k occurrence intervals J yields W(s)=sum_{J disjoint, supp(s) subset union(J)}(-1)^(|J|+<s,forced(J)>) 2^(n-k|J|). For n=qk+r every term divisible by 2^r. When s is one on all prefix qk positions, unique tiling J={1,1+k,...} gives ±2^r, even for q=0 (empty packing), proving sharp minimum and gcd. When r=0 the only maximal full tiling has odd residue, so all characters nonzero. When r=1, every maximum q-packing misses precisely one of holes 1,1+k,...,1+qk, giving W/2 mod2=(q+1)+sum s_(jk+1), balanced on half the characters, including n=1. Exact independent direct avoidance enumeration plus FWHT checked 216 complete spectra for all unbordered patterns k=2..5 and n=1..9. Finiteness is corroboration only; disjoint-packing argument proves all n,k.

## originality

PASS

Earlier special-pattern 001 theorem obtains its three-phase gap but not uniformity over every unbordered w of every length nor the affine first-valuation-layer parity law. Classical single-pattern avoidance inclusion-exclusion counts sequences, not signed characterwise spectral divisibility.

## value

PASS

A broad natural family of forbidden-factor subshifts receives exact integer Fourier recovery thresholds with a universal residue-class law and a 50% valuation-layer classification. It directly generalizes a motivated special case while exposing a structural role of nonoverlap beyond cardinality counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
