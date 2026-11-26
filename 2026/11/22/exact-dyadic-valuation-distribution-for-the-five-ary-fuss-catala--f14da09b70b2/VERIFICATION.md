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

The odd denominator leaves the binomial valuation unchanged; Legendre or Kummer gives 2s₂(n)−s₂(5n), exactly the outgoing carries of n+4n. The two previous input bits and one incoming carry are sufficient; zero padding drains the two delayed bits and any remaining carry. The independently constructed eight-state matrix gives det(I−zM)=D and initial-state Cramer numerator (1−uz)(1+z+(2−u)z²+z³), proving the formal identity for every L including 0. As another check, the state generating functions for 001/100 and 011/110 coincide, q101=u q010 and (1−uz)q111=u²(1−z)q000; elimination gives the same rational function. The first derivative at u=1 decomposes as z/(1−2z)²−1/(1−2z)+(1/(1−z)+(1+z)/(1+z²))/2, yielding the claimed exact mean. At u=1 the denominator factors as (1−2z)(1−z⁴) and the numerator does not cancel the pole at 1/2. For F(λ,u)=λ⁵D(1/λ,u), the derivatives (Fλ,Fu,Fλλ,Fλu,Fuu) at (2,1) are (15,−15,64,−34,−20), hence λ′=1 and λ″=8/5. The log moment generating function has linear-in-L part L log(λ(e^t)/2), with first two derivatives 1/2 and 21/20; the analytic amplitude contributes O(1), and the other poles give a uniform exponentially small error near t=0. Taylor expansion at imaginary arguments of order L^−1/2 gives the asserted weak Gaussian limit. Independent histograms and means agree through L=20 (2,097,151 index instances across blocks), with direct binomial quotient checks for 0≤n<128. The finite checks alone say nothing about a convergence rate or translated intervals.

## originality

PASS

The supported distinct contribution is the full fixed-five dyadic valuation distribution and its exact mean and Gaussian fluctuation constant. The two lowest shells have direct published coverage; the valuation-one record is dated the same day, which does not establish priority. No disclosure of the full all-shell law, or stronger result specializing to it with the stated parameters, was established in the sources inspected.

## value

PASS

For the classical full five-ary tree counts, and equivalently the natural binary self-addition n+4n, the bivariate generating function evaluates every divisibility stratum on every dyadic block. Positive strata above one and the fluctuation constant 21/20 carry real information beyond the published low-shell results. Counting every shell and controlling typical fluctuations are distinct useful tasks; the contribution is not the routine use of Kummer's theorem or transfer matrices by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
