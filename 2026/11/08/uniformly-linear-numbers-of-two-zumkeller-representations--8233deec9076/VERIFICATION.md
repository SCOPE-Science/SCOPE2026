---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The multiplicative partition proof is correct for coprime factors. The displayed binary divisor subsets give the two progression families, with k≥1 and k≥3, respectively. An independent exhaustive check of all proper-divisor subset sums confirms the six even seeds and all 88 odd seeds from Table 1, full coverage of the 44 odd residues, the nonzero quotient differences modulo 11, and maximum seed M=94185. In the even case n−a−β is a multiple of 18 and is at least −2, so it is nonnegative even at n=90. The shifts 18a²t give floor(m/a²)+1 distinct ordered pairs. In the odd case n>M makes each integral seed quotient positive. Select one quotient m not divisible by 11. Among the first T=ceil(m/s²) shifts the other summand stays positive and at most ceil(T/11) fail its divisibility test (none if 11 divides s). Combining the two slopes with R(n)≤n−1 proves the liminf and order claims; no limit is asserted. Frozen replay files: check.py and check_output.txt. The uploaded script was inspected rather than executed; the exhaustive seed check was independently written, and finite sampling is not used to prove the unbounded estimates.

## originality

PASS

The original membership facts and residue certificate are already published. The supported distinct result is the uniform quantitative multiplicity bound obtained by moving each seed through coprime multiples and counting the admissible simultaneous shifts; none of the inspected close statements supplies a multiplicity conclusion. This is a bounded comparison, not a priority certification.

## value

PASS

The additive question changes from eventual solvability to how abundant solutions are in every sufficiently large target, including the harder odd targets. Turning a finite residue certificate into a uniformly linear family and showing how to control the mod-11 losses yields the sharp growth order, not a tiny threshold improvement or a recomputed membership table. The small explicit constant is a certified byproduct, not the source of the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
