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

# Reproduction and proof boundaries

`check.py` is standalone and uses the Python standard library. From the directory containing the two files, run `python3 check.py`. Its output must equal the success lines in `check_output.txt` (ordering is deterministic). The script independently builds the normalized multiplication, constructs the derivation linear equations and computes their finite-field ranks, tests parameterized automorphisms by direct multiplication, exhausts all \(2^{16}\) four-by-four binary linear transformations in two dimension-four cases, and checks the existence or absence of predicted automorphisms over the dual-number rings for selected primes.

The central theorem is not a computational census: its field-independent and scheme-theoretic claims are proved algebraically in `RESULT.md`. The finite-field checks establish the listed finite cases only. The dual-number witnesses test tangent directions but do not independently prove the entire representing group scheme.

The first verified public archival precursor is arXiv:1208.1709 (8 August 2012); the ordinary automorphism gcd condition is already explicit in arXiv:1805.10285, Theorem 5.2, under characteristic-zero assumptions. That condition is not claimed as original. The characteristic-\(p\) group-scheme conclusion remains subject to external historical-priority review.
