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

Kummer reduces oddness to no carry in n+2n, precisely no adjacent 1 bits. Process the quadruple least-significant bit first: disjoint masks impose admissibility, and (old carry + a_bit+b_bit−c_bit−d_bit)/2 must be integral. The carry is bounded by 1 in modulus; at depth r it is the signed integer difference divided by 2^r, so zero terminal carry accepts exactly ordinary equality. As an independent finite certificate, permuting the two inputs on each side and exchanging sides yields the five orbit types empty, singleton, same-side pair, cross pair, and all four. In this order their outgoing multiplicity rows are (1,0,2,4,1), (1,0,1,2,0), (0,2,0,0,0), (1,0,0,1,0), (1,0,0,0,0), with starting empty and terminal selector (1,1,0,1,1). All these types are reachable and return to empty; its self-loop makes the transfer primitive. Its characteristic polynomial and initial vector products yield the stated denominator and numerator by Cayley–Hamilton, without extrapolating finite data. The root bracket and P'(t)>0 on t≥7/2 identify the Perron root (which is at least the positive root in the bracket); nonnegative nonzero endpoints give positive leading coefficient. Counting completions from the last prefix digit yields exactly phi^(-r) or phi^(-r-1) and consistent cylinder probabilities for weak convergence; the limiting law starts with the virtual preceding digit 0 and need not be the stationary initial distribution. The squared prefix-sum mass is comparable to E_r phi^(-4r). Real tails are bounded by 2/3 each, so each prefix sum splits between two adjacent cells; squared masses before and after splitting/combining are comparable by fixed factors. This gives the exact dyadic exponent and the adjacent-cell comparison also gives the distance exponent. A Lebesgue L² density would require the dyadic squared mass multiplied by 2^r to stay bounded, which contradicts lambda>phi^4/2. No singularity conclusion follows from this bound alone.

## originality

PASS

Bounded statement-level comparison supports the specific rational ordinary fibbinary energy and the exact real-convolution correlation dimension. Neither the already known support/parity and support size nor generic carry/finite-type machinery is credited as new. The literature assessment is not an exhaustive priority claim.

## value

PASS

The adjacent-11 binary shift is a standard dependent-digit model, and the odd-binomial support adds a natural arithmetic realization. Its support has dimension log(phi)/log(2)>1/2, so two summands have enough symbolic degrees of freedom that the sharp L² obstruction is not a support-dimension count. Ordinary sum collisions determine the precise rate of concentration under convolution; the exact growth exponent and D₂ quantify that rate and rule out an L² density in this canonical overlapping example. The rational energy also reports all finite dyadic scales, not an arbitrary finite window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
