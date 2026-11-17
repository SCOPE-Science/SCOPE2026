---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Renewal on independent reset attempts gives M(b)=(1-H(b))/(rH(b)) with H=K_kappa*mu, kappa=sqrt(r/D). On the right tail of compactly supported mu, H=C exp(-kappa b), fixing kappa by log M slope. F(s)=integral(1+sM)^-1 db is continuous strictly decreasing from infinity to zero and equals 2/kappa only at physical s=r; then distributional Helmholtz inversion recovers arbitrary atomic/continuous mu and D=r/kappa^2. On an interval, annihilating the exponential-kernel convolution forces zero signed measure internally and two weighted external masses zero. Fourier multiplier 2kappa/(kappa^2+xi^2) makes smooth density oscillations decay at exact n^-2 while TV tends to epsilon/pi. Independent direct 1-vs-2-atom equivalence check confirms the local ambiguity example.

## originality

PASS

Best-of-knowledge novelty rests in simultaneous identification of unknown r, D and compactly supported reset law from one spatial target scan at fixed physical rate, exact two-moment partial-window fibers, and quantified n^-2 instability. Prior Méndez et al. derive the forward renewal law, and Abundo treats inverse first passage at fixed target/rate rather than full moving-target scan. Earlier two-target Resultary theorem varies rate and knows D, and starts at a fixed nonrandom initial site; it does not imply this triple inversion or local equivalence. Literature searches did not locate stronger coverage; absence of discovery is not definitive priority.

## value

PASS

Natural inverse problem: what can ideal spatial mean-first-passage observations reveal about reset rate, diffusivity and reset-source heterogeneity? The exact reconstruction and partial-data identifiability boundary matter for inverse stochastic processes; the sharp smooth counterexample explains fundamental ill-conditioning and precludes naive stable recovery. Not just restatement of known forward formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
