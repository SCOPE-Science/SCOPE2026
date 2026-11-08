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

# Verification record

Run `python verify_noisy_star.py` with Python 3 and no third-party packages. The program builds each finite noisy-star Markov generator from the clock definition, solves its stationary equations using exact rational Gaussian elimination, compares both factorial-moment sequences and each reconstructed joint probability with an independent finite-state distribution, and checks beta-limit moment identities through degree 16. Actual run: `PASS: 2550 total exact rational assertions, including all-order moments and full joint-law inversion on 30 finite chains.` Parameter families include zero and nonzero hub imitation rates, varying leaf and redraw rates, and star sizes 2, 3, 4, 6 and 8.

The source proof independently establishes all-degree stationary identities, strictly positive recurrence denominators, exact inversion and weak convergence. Finite tests neither enumerate all \(k\) nor independently certify historical originality. The beta law is also an application of established two-state switching-limit theory; the finite complete stationary recursion is the primary result.
