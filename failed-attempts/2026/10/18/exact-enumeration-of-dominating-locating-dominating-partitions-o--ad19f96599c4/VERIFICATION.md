---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Both domination conditions forbid 000 and 111. For n>=5 two distinct vertices share at most one neighbor, so a repeated nonempty L-signature must consist of the sole central one in a cyclic 00100; the converse holds. In C3 only partitions with a single D vertex work; in C4 the four rotations of 0011 work and both alternating words fail by a two-neighbor collision. For the cyclic language, paired zero and one runs have length 1 or 2, and a singleton one-run cannot sit between two length-2 zero-runs. With k zero-runs, a labelled word has k choices for its distinguished run, while a linear list of k run pairs can be placed at n absolute starts. Comparing these marked objects yields n/k times the transfer trace, even for periodic words. The determinant and exceptional coefficients give the claimed OGF. Its factor 1-z-z^3-z^5 has a simple unique smallest-modulus zero rho by the equality condition of the triangle inequality; the log derivative contributes rho^(-n) with unit amplitude. Positive counts for every n also follow by composing lengths 2 and 3 from zero-runs of length one, except that n=4 needs its separate graph witness.

## originality

FAIL

A distinct size-marked catalogue result explicitly covers the same one-sided class and forbidden patterns for n>=5. Its t=1 specialization gives the complete stable-range scalar OGF and hence its asymptotic. The underlying scalar sequence is also indexed as OEIS A001636 apart from the short-cycle corrections. The stronger catalogue record's date is later than the frozen source path; exact mathematical coverage does not establish historical priority or dependence.

## value

FAIL

A mixed-partition counting interpretation is intrinsically natural, but the full weighted version with the same local characterization is already available in the checked catalogue. The residual C3/C4 adjustments and pole simplification do not amount to a separate contribution. No distinct surviving repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
