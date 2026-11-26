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

Verified the external floor-difference and least-period theorem in its applicable coprime scope, and independently reconstructed its mechanism. Towers eventually stabilize modulo each fixed integer by induction using CRT, exponent reduction modulo phi for unit prime-power components, and growing exponents for nonunits. For odd p dividing r, successive exponent differences eventually are multiples of ord_p(a), giving a per-height increment v_p(a^(p−1)−1) by LTE. For 2 the differences are even and the increment is v_2(a²−1)−1. Thus the eventual minimum of the normalized affine valuation lines uses the least slope (and the least intercept among ties). The floor-difference word for slope u/d has period d and any period k requires k·u/d integral by its average, so d is least. For odd p the unit roots of X^(p−1)−1 lift uniquely from the p−1 roots mod p; for 2 the larger of v_2(a±1) is c_2(a), giving two reduced classes mod 2^k for k≥2. Independence by CRT gives the difference of tails for each t; prime bases have the same weights on every fixed reduced residue event by PNT in arithmetic progressions. Both local integer thresholds for t>1 are at least 2, so raising t by one multiplies the minimum's mass by 1/r, with the special 2-adic endpoint Q_2(2)=1 included. Separate (0,1] and sum chains from (1,2]; shifting preserves denominators. The event λ>J is itself determined by a finite modulus and has limiting frequency tending to zero in both populations, justifying the countable union and normalization. Each eligible d≥2 has a positive atom at 1+1/d using a prime whose exponent is divisible by d, and d=1 has a positive atom at 2. Negative or zero slopes are not relevant, and squarefree radices give only period 1. The independent command python3 /workspace/branches/tetration_replay.py counted actual unit valuations over all 4096 and 41472 reduced classes for 64 and 144, respectively, and reproduced both exact example vectors after the proved tail summation. This is not an enumeration of infinite towers or a proof by experiment. Frozen checker read, not executed.

## originality

PASS

Substantial inputs, including the exact period criterion, attainable periods, CRT local tails, aggregate density and prime-relative aggregate result, are prior. The verified distinct result is the period-by-period finite distribution, with the same prime-relative vector. The October manuscript explicitly poses the period-resolved question; the checked revision states aggregate, not period-resolved formulas.

## value

PASS

The classification answers a precisely posed quantitative question in the source literature. It resolves unequal weights among periods that have the same status in the set of attainable periods, works for arbitrary mixed radices, and converts an infinite atomic sum to finitely many exact rational operations. This is appreciably more useful than restating the aggregate nonconstant proportion or computing a few finite samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
