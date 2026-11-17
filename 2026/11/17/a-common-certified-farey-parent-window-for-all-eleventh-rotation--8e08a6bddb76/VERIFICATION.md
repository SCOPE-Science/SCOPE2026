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
# Reproducibility and scope of the exact certificate

Run `python3 verify_eos.py` from a directory containing the embedded file. It uses no network and no third-party packages. Successful completion prints exactly five `CERT` lines (one per numerator \(k=1,\ldots,5\)) and the terminal marker `FIVE_FAREY_PARENT_CYCLES_AND_SINGER_BASINS_CERTIFIED`.

The certificate's fixed scaled-integer denominator is \(10^{55}\). Each interval arithmetic operation widens its endpoint by integer floor or ceiling division. The exponential evaluator first scales a nonnegative exponent into \([0,1/2]\), computes the degree-55 Taylor polynomial, and appends an upper error of \(10^{-55}\), valid because \(2(1/2)^{56}/56!<10^{-55}\). The exact enclosing interval is squared back up; negative exponents use the inverse. Disjoint phases and strict derivative enclosures are checked at each of five rational trapping boxes.

For each numerator, the checker brackets both nondegenerate critical points and proves eventual strict entry into the attracting phase boxes. Their recorded entrance bounds are \((61,104)\), \((162,48)\), \((43,117)\), \((49,214)\) and \((126,55)\). This is a finite computation whose completeness is restricted to the specifically stated rational boxes and finite capture trajectories; it is **not** an exhaustive state-space enumeration. Mathematical existence and uniqueness use the contraction theorem and the previously proved negative-Schwarzian critical-basin theorem, respectively.

The other five numerators are exact reflections. Robustness on a common open steepness interval follows from the finiteness and strictness of certified inequalities. No explicit interval width is certified. No independent mathematical audit has been performed.
