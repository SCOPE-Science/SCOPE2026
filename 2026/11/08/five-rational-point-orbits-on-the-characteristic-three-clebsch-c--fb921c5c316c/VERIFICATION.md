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

# Exact finite-field checks

Run `python3 verify_orbits.py` and `python3 verify_census.py` with both scripts in the same directory as this file. Only Python 3 standard-library modules are used. The exact field representation is \(\mathbb F_3[\iota]/(\iota^2+1)\), encoded as `a+3*b` where integers `a,b` are in `{0,1,2}`. Normalization divides by the first nonzero projective coordinate by seventh powering in the multiplicative group of order eight.

`verify_orbits.py` reconstructs the two projective line orbit prototypes, their 15 and 12 images under all 120 coordinate permutations, the five point orbits with size and stabilizer order, and all orbit-specific line-incidence counts. It checks the defining symmetric equations on every constructed line point and every orbit representative.

`verify_census.py` independently enumerates all \(9^4\) possible four-coordinate vectors in the trace hyperplane, normalizes the \(145\) surface points, enumerates every geometrically contained rational line by all pairs of rational points, and classifies point orbits and line multiplicities without using the first program's line prototypes.

Both programs completed successfully. Exhaustivity here means exhaustive over \(\mathbb F_9\): any rational point occurs among the four free coordinates, and any rational line contains two rational points, so is found among pair spans. The proof invokes a standard smooth-split cubic-surface formula and uses the independently checked line orbits to establish splitting. This is not a computational claim about fields other than \(\mathbb F_9\); there is no independent audit or external proof certification.
