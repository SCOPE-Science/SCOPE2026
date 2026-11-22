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

# Verification and its scope

The claims and assumptions in `RESULT.md` were reconstructed from the update rule rather than inferred from finite tables. The exact circular-window identity, uniqueness of the recurrent class-constant set, cyclic forbidden-run correspondence, closed-path interpretation of the transfer trace, exact phase-fiber multiplicities, and factorial-moment convergence are all proved there.

Run `python verify_direct.py` to exhaustively enumerate all labelled configurations for all pairs \(3\le n\le12\), \(2\le s<n\). It checks the computed first-periodic-entry times, all exact shell counts, and the positivity and count of the sharp last shell. For \(n\le10\), it also checks the precise recurrent phase-fiber counts \((2^m-1)^w\) against independently iterated states. The terminal output is `ALL_OK`.

Run `python verify_transfer.py` to compare an independent integer-matrix transfer implementation against direct circular-word enumeration for the 104 admissible \((m,t)\) pairs with \(2\le m\le14\), verify example populations and inspect numerical values of the Poisson-limit probability. The terminal output is `PASS`.

Both programs were executed successfully from the current complete package. These finite experiments are not substituted for the uniform-in-size proof. The stochastic limit is supported mathematically by the factorial-moment calculation, not asserted solely from its numerical convergence. No independent audit has been performed.
