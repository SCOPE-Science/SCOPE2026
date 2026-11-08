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

The theorem is proven for every integer \(n\ge4\) with chord-defined arc lengths \(a,b\ge2\). The proof's critical step is the two-front evolution on one chord arc, the blocking of the opposite arc until both endpoints are colored, and two-front completion of the other arc. The exact multiplicity list \(B_\ell(z)\) is a finite counting identity valid for every integer arc length. Nothing beyond this domain, such as multiple chords or different forcing rules, is claimed.

Run `python3 verification/check_python.py` from the directory containing the files. It builds the cyclic adjacency sets and applies all available legal forces at each round, independently of the theorem. It compares the resulting round counts to the formula for every chord placement on orders 4 through 50, and tests all nonconsecutive pairs at orders up to 12. This produced the message `PASS: all lengths n=4..50 ...`.

Run `g++ -std=c++17 -O2 verification/check_cpp.cpp -o propagation_check` followed by `./propagation_check`. Its independent unsigned-bit-mask representation checks all two-seed pairs for every chord placement on orders 4 through 22 and verifies the stated extrema, gapless spectrum, efficient-set counts, and cycle parity comparison. It produced `INDEPENDENT_CPP_PASS graphs=190 pairs=24795 n=4..22 all chord positions and all two-seed sets`.

The two finite checks are deliberately corroborative; neither is presented as proof of an infinite statement. Only the code sources are required, no unavailable binary or hidden data are dependencies. Independent scholarly audit has not been performed.
