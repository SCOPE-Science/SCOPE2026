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

# Reproduction and scientific limits

Run `python3 checker.py` in the same directory as this file, using a Python 3 interpreter and no external packages. For two through six S-alleles, the checker enumerates every simple heterozygote support of each cardinality up to the first feasible cardinality (or every cardinality if infeasible), verifying the exact minima and numbers of minimum-size supports, the three four-allele pollen-dominance supports, and the five-cycle characterization at five alleles. It also tests the general matching constructions on seven through sixty S-alleles. The included checker passed 12,494 deterministic assertions.

The global claims for all integer \(k\ge2\) are established analytically in `RESULT.md`, not by the finite search. The tests do not address population-genetic dynamics, mate frequencies, empirical dominance classification, or historical priority.
