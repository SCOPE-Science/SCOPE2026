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
# Verification

A fully enumerative diagnostic is supplied as `CHECK.py`; execute `python CHECK.py`. Its finite checks compute \(\operatorname{Cov}(D_i,I)\) and \(\operatorname{Cov}(M,I)\) as fractions from independent uniform word enumeration, not from the proof formula. Its assertions cover 161 positive count vectors through length eight with up to four letters, and compare all positional, aggregate and mean identities, including symmetry; 2,356 exact assertions plus the additional explicit-size tests are reported.

The infinite statement requires the mathematical argument, which consists of an exact adjacent-swap bijection, inversion-complement reversal, and a complete three-position sign count. Those steps are written in `RESULT.md`, including equal-letter cases. The classifier for size six is proved by a multiplicity-gap inequality rather than a finite search. Direct enumeration is diagnostic only.

Self-review only; no independent audit has been performed.
