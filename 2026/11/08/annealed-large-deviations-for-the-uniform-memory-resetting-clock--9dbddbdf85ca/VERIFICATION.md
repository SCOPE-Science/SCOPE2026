---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For a rate-r Poisson reset process with unit deterministic drift and U uniform over the complete elapsed physical history, rescaling z=rt and Y_z=rQ_(z/r) gives a rate-one process on 0<=Y_z<=z. Conditioning on the next infinitesimal interval yields F_s'(z)=(s-1)F_s(z)+z^-1 int_0^z F_s(u)du, F_s(0)=1 and F_s'(0)=s. Differentiation produces zF_s''(z)+[1+(1-s)z]F_s'(z)-sF_s(z)=0. The unique analytic-at-zero solution for s!=1 is M(-s/(1-s),1,-(1-s)z), matching all exact series coefficients. Negative-argument Kummer asymptotics for each fixed real s<1 give F_s(z)~[(1-s)z]^[s/(1-s)]/Gamma(1/(1-s)), so the limiting log-mgf / log z is s/(1-s). For s>1 no-reset paths yield F_s(z)>=exp((s-1)z), and for s=1 monotonicity in s and an unbounded limit as s up-to-1 force Lambda(1)=+infinity. The resulting Lambda is proper, lsc, finite/differentiable on (-infinity,1), and steep at s=1; exponential tightness follows from any fixed s in (0,1) and nonnegativity. Gartner-Ellis gives the LDP for positive y; the lower bound on every open neighborhood containing 0 follows by approximation from positive y, while the closed-set upper bound follows from exponential tightness. Its exact good Legendre rate is (sqrt(y)-1)^2 for y>=0, infinity otherwise. Differentiating the generator at s=0 gives m=gamma+log z+E1(z), and locally uniform Kummer asymptotics in complex s near 0 give second cumulant 2log z+2gamma-2-pi^2/6+o(1) and Gaussian characteristic-function convergence. The proof does not claim a state-space LDP, quenched annealed equality, rates for different reset distributions or memory kernels, or a speed other than log z.

## originality

PASS

Best-of-knowledge priority attaches to the complete annealed logarithmic-speed LDP for the unwrapped uniform-Poisson operational clock, in particular its positive/zero boundary and both rare-time tails, not to the exact Kummer transform, mean scaling, model or general Gartner-Ellis argument. The 2017 diffusion paper already supplies the same Kummer family with Brownian Fourier symbol Dk^2; the 2026 quantum source explicitly supplies the same unwrapped recursion and energy-basis Kummer solution, with typical log-scale behavior. The 2019 tree paper treats CLTs and local limits for monkey walks. The 2023 Boci-Mailler theorem establishes only a quenched LDP for relocated Markov-process positions and Remark 1.5 explicitly says its annealed upper bound is not proved. The exact characteristic transform plus known hypergeometric asymptotics is a close, fairly direct route to the claimed specialized LDP; this raises a meaningful priority/independent-contribution risk, but in the inspected primary statements the complete annealed rate theorem is not stated or delivered. Searches of semantically similar published mathematical results, primary and scholarly indexing found no earlier explicit full annealed clock theorem. Negative searches do not prove novelty.

## value

PASS

An operational time with uniform historical resetting is a natural observable in the established preferential-relocation/quantum-memory protocol. The new explicit rate I(y)=(sqrt(y)-1)^2 for both short and long relative elapsed times gives rare-event probabilities of polynomial order in physical time, not captured by the known typical log-time law or a marginal Brownian-position CLT. The annealed/quenched distinction is a concrete open gap highlighted by Boci-Mailler Remark 1.5; resolving the annealed problem for this exact exponential-run specialization is useful even without a general kernel theorem. The exact mean, variance correction and CLT quantify typical uncertainty and tie rare tails to fluctuations. The value is a bounded natural special-case theorem rather than a new general large-deviation method; routine Kummer and Gartner-Ellis tools do not alone supply its scope and boundary analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
