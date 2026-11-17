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

# Verification of the signed shuffle basis and coinvariants

The theorem is established by the integral Künneth isomorphism and the exact signed orbit–stabilizer calculation in `RESULT.md`. The following finite checks are an independently executable consistency test, not a replacement for the all-parameter proof.

Run `python VERIFY.py` using only the Python standard library. It constructs every signed shuffle representative for dimension one through four and degrees zero through four, evaluates the actual magnitude boundary on each chain, and compares the entire coefficient dictionary under each adjacent coordinate swap and a bit flip. These tests examine chains rather than just homology dimensions.

Run `python VERIFY.py --smith` with SymPy installed to additionally construct the integer matrix of all relations from coordinate flips and adjacent coordinate transpositions and compute its Smith normal form at five specified dimension/degree pairs. It must agree exactly with `VERIFY_EXPECTED.txt` and yield only unit and two invariant factors. The checks were executed from the included source, and the recorded output is included. The finite cases covered are exactly those printed by the program, not all values of the parameters.

For the general result the critical logical checks are: natural Künneth is an integral isomorphism (no Tor terms for the Cartesian powers of \(K_2\)); the sign of a block permutation is its weighted inversion parity; translations have no signs; a stabilizer of a weak composition has a negative element precisely when an odd part repeats; one orbit then imposes just \(2x=0\); and distinct composition orbits contribute direct summands. These observations prove all quantifiers and the unbounded-rank corollary without appealing to computer enumeration.

Independent mathematical audit: not performed.
