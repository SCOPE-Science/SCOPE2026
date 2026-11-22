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

# Scientific verification

The proof uses an exact Poisson Laplace functional for the infinite-line one-point survival law, a radius-\(\lceil(\log n)^2\rceil\) coupling of wheel and line, and independent outward-ray bounds for locally dependent pairs. The two local-dependence sums vanish and determine the Gumbel and Poisson limits without invoking an unverified infinite simulation. The vanishing-rate escape boundary uses a first-moment bound only.

`verify_wheel.py` constructs the finite continuous-time Markov SI generator on 6-, 8- and 10-rim wheels, with no external packages. It evaluates the transient distribution by uniformization and checks twelve independent numerical references for site survival at four combinations of rate and time. The program was run successfully on the new standalone file.

These finite checks do not prove infinite-size limit, novelty, or independent scientific validity. There is no claim about moments of the limit or a general theorem for other networks.
