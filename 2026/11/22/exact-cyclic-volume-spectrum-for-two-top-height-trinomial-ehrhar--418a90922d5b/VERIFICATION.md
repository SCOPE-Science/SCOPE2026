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

# Verification of the exact cyclic-volume spectrum

Compile `cyclic_screen.cpp` using C++17, run `./cyclic_screen 60`, and require stderr output ending `SUMMARY 60 34219 2366 2352 14`. The fourteen printed pairs have group orders four, five, six, eight, or ten, and no other order survives. All 34,219 possible unordered high-element pairs for orders four through sixty are visited. Of these, 2,366 pass the faithful-character screen and 2,352 have a full-rank modular inconsistency certificate. Every exclusion is mathematically necessary for the target heights; a nonexcluded pair need not be realizable. The five included witness tuples are verified by `python3 witness_check.py` with exact integer heights.

The group-order cutoff sixty follows analytically from the average-height generation proof and the Euler-totient support restriction, independently of the finite checker. The second prime 1,000,000,009 gave the same fourteen survivors; the packaged source uses 1,000,000,007. The code proves rational-system impossibility by combining full column rank with inconsistency modulo a prime. It does not assert nonexistence merely because a numerical search failed.

The group-to-simplex correspondence is a cited mathematical theorem, and the witness replication argument multiplies all heights by the prescribed arbitrary exponent. No independent mathematical audit has been performed.
