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

# Verification of the six-profile distribution

`verify_all.py` uses only Python integer arithmetic. Its finite-state enumeration is algebraically proved equal to the inclusion-exclusion transfer formula in `RESULT.md`. Each of the sixty-four allowed-feature generating functions is a four-state matrix entry with numerator degree at most five and denominator degree at most four. Their sum has a common denominator of degree at most \(256\) and a numerator of degree at most \(257\). The six proposed rational functions have degrees at most \(16\) and \(13\) in numerator and denominator, respectively. Therefore each difference, after cross multiplication, has numerator degree at most \(272\). The program checks exact coefficient equality through degree \(279\), which proves all six rational identities, rather than merely testing sample lengths.

`independent_brute.py` constructs each length-\(n-1\) deletion descendant literally, computes all four pair frequencies from scratch, forms the set of distinct received profiles, and counts cardinalities for every source word with \(2\le n\le14\). It agrees with the exact matrix-based recurrence and checks the length-nine cutoff. Both scripts were executed from extracted contents of the final package; no scientific claim is based only on a prior-run log.

The result concerns a mathematical deletion-to-profile channel, not sequencing accuracy measured from experiments. The exact generating functions are proved using finite-algebraic certificates, whereas the independent direct enumeration is limited to fourteen symbols.
