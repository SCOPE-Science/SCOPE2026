---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed the law for the stated lifetime indegree with multiplicities. An independent geometric lag G with p_h=(1−q)q^(h−1) at source n gives the growing model upon conditioning on G≤n. Keep G if valid and otherwise independently resample from the conditional law. The disagreement probability is q^n per parent draw, so a union bound over n≥k+1 gives m q^(k+1)/(1−q). In fact source k+1 cannot affect the block, so the bound need not be optimal. In the stationary comparison block, subtraction of the deterministic internal-source total mL leaves incoming minus outgoing boundary flux. Disjoint source choices make the two fluxes independent. The outgoing crossing probability at source t=1,…,L is q^(t−1); from source L+s the probability of landing inside is q^(s−1)(1−q^L). Matching the outgoing count to the infinite Bernoulli series adds a tail of mean m q^L/(1−q); monotone coupling of the incoming count to an independent series costs the same union bound. The series are almost surely finite, and their difference thus gives the advertised uniform TV upper bound including k=0 and L=1. The h=0 Bernoulli group is deterministic and cancels from the difference, leaving the modulus-square product and variance 2m q/(1−q²). A symmetric integer-valued law with this positive variance is not Gaussian. The stationary single-target variance is m times the sum of p_h(1−p_h); at lag d≥1 the covariance is −m times the sum of p_h p_(h+d), since one choice at a shared source cannot hit both targets. These sums are absolutely convergent. Substituting the resulting γ gives the incremental L-block variance γ(0)+2Σ_(d=1)^(L−1)γ(d)=2m q^L/(1+q), yielding the stated exact variance on summation. The Fourier series is m(1−|φ_G|²), where φ_G is geometric; this yields the displayed rational spectrum and quadratic zero. Stationary bounded variance and the uniformly square-integrable number of coupled lag disagreements also imply tightness of the finite-start excess. The stated data from checker.py are source-reported only; the code was read, not run. No finite check certifies the infinite bounds, and the exact covariance, spectrum and block variance here refer to the stationary field.

## originality

PASS

Pass for the explicit, quantitative two-boundary total-variation law for finite-start lifetime indegrees, including its evaluated difference distribution. Stationary bounded number variance and the structure-factor mechanism are covered in broader perturbed-lattice work; the displayed spectrum is its evaluated geometric specialization. The established bulk mechanism, geometric-lag coupling and same-model results are credited rather than counted as standalone originality. No inspected statement implies the finite-start TV law with its two explicit errors and evaluated distribution.

## value

PASS

Lifetime indegree sums might suggest additive fluctuations from random single-vertex counts. The exact edge balance identifies instead two finite, asymptotically independent fluxes; the law explains what replaces a bulk central limit theorem and gives a quantitative error separated into distance-from-start and block-length effects. This goes beyond a qualitative hyperuniformity statement or a spectral example: it identifies the limiting mass law for the original growth model and controls its approximation uniformly in block placement and length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
