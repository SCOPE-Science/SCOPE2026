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

From the package directory run `python3 verify.py`. The verifier reconstructs all twenty face triples via two cyclic pentagonal rings and uses standard-library `fractions.Fraction` for every probability and Laplace-transform comparison. It requires no network access, external data, or third-party packages.

Two computational derivations are compared: a memoized recurrence over 202 reachable twelve-bit occupied masks and a direct enumeration of all ordered successful face histories. A separate face-propagation procedure verifies all 120 icosahedral automorphisms and the three terminal-pattern orbits. It checks the \(10,60,1\) terminal pattern multiplicities, complete per-pattern rational probabilities, conditional local transition multiplicities for every first face, and the total jamming-time Laplace transform at six exact rational arguments. The first two exact moments are checked from explicit pathwise exponential waiting-time moments.

The finite proof uses the displayed face construction and transition table in RESULT.md. The verifier is an exact exhaustive check of the fixed twelve-site model, not a Monte Carlo estimate and not an infinite-family argument. It does not assess historical priority or provide an independent scientific audit.
