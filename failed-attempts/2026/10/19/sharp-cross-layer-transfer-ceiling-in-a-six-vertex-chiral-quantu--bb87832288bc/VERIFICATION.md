---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Fourier core eigenvalues are 0, +sqrt(3), -sqrt(3) in the stated gauge. Squaring each traceless shifted 2x2 sector gives (lambda^2+4)I/4. Exponentiation and summation with Fourier projector entries exp(2pi i s(k-j)/3)/3 give the stated cosine phase and kernel. The triangle bound yields amplitude (1+4/sqrt(7))/3. Independent sign flips in Q(sqrt(3),sqrt(7)) prove frequency independence, so the continuous torus orbit and every positive-time tail are dense; for each pair the two sines and shifted cosine can approach +1. Equality would require both sine magnitudes to be 1 and hence a rational ratio of their frequencies, impossible. The probability constant, its digits as written, and all nine singleton-pair quantifiers are correct. Independent direct matrix power series checked 36 amplitudes with maximum discrepancy 2.7e-14; this corroborates the kernel, not the infinite-time conclusion.

## originality

FAIL

The winning source is the prior rooted-product decomposition and frequency analysis for the very same core and leaf graph, not merely literature about similar routers. Its explicit cross-block projectors give the claimed kernel by substitution at m=1, and its established independent frequency basis then gives the ceiling by maximization over three free phases. The explicit decimal and nonattainment need not appear in the earlier paper for this direct consequence to be covered.

## value

FAIL

The channel is motivated by the router's asymmetric performance, and the number is useful as a benchmark. However the contribution as a narrow exact invariant is a mechanical evaluation of the already solved six-site spectral model using its already established frequency basis; it offers no further structural or performance result beyond those inputs. The benchmark does not meet the bar for an independently valuable new exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
