---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The conic compactification T=P_{P3}(Sym²U) is 8-dimensional; the degree-4 part of (ell,Q)² has rank 10+4+1−1=14, yielding P_T(E) of dimension 21. Outside the conic the linear system is base-point free; Bertini gives generic smoothness away and irreducibility, so the unique positive-dimensional singular component is the conic and the incidence map is generically degree one. The K-theory resolution gives s(E)=(1−2h−k)/[(1−2h)^10(1−h−k)^4(1−2k)]. Independently reconstructed top relevant coefficients 579040,139412,22992,1981; base pushforward gives 579040−4·139412+6·22992−4·1981=151420. Source verifier also derives the same number by 24-point torus localization; geometry relies on Bertini and rank argument, not its numerical output.

## originality

PASS

Best-of-knowledge originality: the explicit statement is not implied by inspected stronger sources; limitations and plausible overlap recorded.

## value

PASS

An exact degree for a natural 21-dimensional nonnormal-quartic family gives a 21-general-point enumerative count and a reusable incidence/Segre calculation, not a textbook substitution of a known line count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
