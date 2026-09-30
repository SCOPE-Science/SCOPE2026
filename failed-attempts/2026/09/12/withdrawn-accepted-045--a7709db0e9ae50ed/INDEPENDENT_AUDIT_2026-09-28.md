# Independent Audit — 2026/09/12/045

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `a4388fce90c777f9d11a20f372b2ca0f45ece62a`
- Disposition: **FAILED**

## Correctness

**PASS** — The negative deterministic-s0 conclusion is correct. For any fixed scale s, the record's Brownian-Gibbs tube argument gives positive probability that the geodesic location g(s) exceeds any prescribed finite level; choosing s*=min(s0,1/2) and using g(0)=0 then forces a positive-probability violation of the proposed one-sided modulus. Independently, the same fixed-scale positivity also follows from the stronger one-point large-deviation theorem below.

## Originality

**FAIL** — Spivak's 2025 Theorem 1.1 gives, for every fixed t in (0,1), an explicit asymptotic P(gamma(t)>=r)=exp(-c(t) r^3(1+o(1))) as r tends to infinity. In particular this probability is strictly positive for all sufficiently large r. For any finite M, choose such an r>M; then P(gamma(t)>M)>0. Thus the record's advertised stronger lemma ('per-scale full support' above every finite threshold) is an immediate monotonicity consequence of a published stronger fixed-time tail theorem, and the deterministic-s0 disproof is then a one-line specialization.

## Scientific value

**FAIL** — The target statement is worth clarifying, but after the 2025 one-point large-deviation result the record contributes no new structural theorem: its headline follows directly by evaluating one fixed time and comparing a finite threshold with the known positive upper tail. The separate Brownian-Gibbs proof is an alternative proof of a consequence already covered by stronger prior work.

## Sources

- One-point large deviations of the directed landscape geodesic (Daniel Spivak): https://arxiv.org/abs/2503.09486 — Theorem 1.1 gives an explicit positive fixed-time upper-tail asymptotic for gamma(t) as the spatial threshold tends to infinity.
- The directed landscape (Dauvergne, Ortmann, Virag): https://arxiv.org/abs/1812.00309 — Background construction, continuity and geodesic framework.

## Limitations

- This audit does not challenge the internal Brownian-Gibbs proof; the rejection is driven by prior coverage and resulting scientific value.
- The conclusion concerns the record's claimed independent finding, not whether the target statement itself is true or false.

GitHub was read only as evidence; no repository mutation was performed in this audit chat.
