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

# Verification and limits

The proof in `RESULT.md` is algebraic and combinatorial for every integer \(n\ge3\); its essential certificates are the cubic-graph cut inequality, the quadrilateral frustration-parity classification, the maximum-independent-set count, and the exactly diagonalized three-state transfer matrix.

Run `python3 verify_exhaustive.py` from the directory containing the files. It independently enumerates all configurations of each Möbius ladder from \(n=3\) through \(n=9\), compares energy and exact multiplicity at nine integral/half-integral nonnegative field values and terminates with `ALL_EXHAUSTIVE_CHECKS_PASS` on success.

Run `python3 verify_transfer.py` from the same directory. It uses a separate rung-sector dynamic program, makes exact comparisons across the same field grid for every \(n=3,\ldots,50\), computes independent-set totals by an independent three-state matrix recursion and terminates with `ALL_TRANSFER_AND_INDEPENDENCE_CHECKS_PASS` on success. Both programs require only standard Python libraries. These checks were replayed on these exact files and passed.

Finite experiments do not establish validity beyond their tested sizes; the proof provides that extension. The formulas describe static \(T=0\) ground states and do not calculate partition functions at positive temperature, dynamics, critical exponents or quantum spectra. Independent validation has not been performed.
