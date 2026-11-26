---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For r≥3, each co-singleton trace requires a divisor modulus at which the omitted point differs from all the others; some primary factor of the modulus already witnesses this, so each label needs a private prime. A prime cannot serve two labels: compare their witness levels at the smaller level using a third point and obtain contradictory congruences. Conversely, intersect the witness fibers for the omitted labels; for a nonempty trace the intersection is nonempty and is exactly a coset of the lcm modulus. The empty trace is provided by a singleton outside the support, since r≤ω(n)<n. The upper bound is attained when ω(n)≥3 by taking the individual unit vectors in CRT coordinates; pairs are shattered for all n≥3 using singletons, the whole group and an outside singleton. For n=1 no singleton support is shattered; for n=2 singletons are shattered but the full support cannot realize the empty trace. Locally, fix an outlier label and use the first digit k where it differs: choose q values for an anchor among the other coordinates, p^((a-k)(r-2)) for the remaining coordinates agreeing through k digits, and (p-1)p^(a-k) for the outlier agreeing through k-1 but not k. Summing gives q(p-1) times the sum of p^(b(r-1)) over b=0,...,a-1. This counts the same disjoint events as the frozen expression partitioned instead by the maximal common exponent of the non-outliers. By CRT, prescribed j labels all lacking a private prime give the stated product of q^r-jB_r. Inclusion–exclusion counts ordered tuples with all labels served; these tuples have no repeats, so division by r! is exact. At r=t each prime serves one distinct label, giving t! assignments that cancel the denominator, and squarefree factors then give nφ(n).

## originality

PASS

The verified distinct near matches count shattered supports on other concept families, not all cosets of the cyclic subgroup lattice. Classical intersection closure and CRT are not credited as new. The supported distinct claim is the exact cyclic shattering criterion together with the coefficientwise census from primary-coordinate outlier counts, not an assertion of priority for general box shattering.

## value

PASS

This counts all shattered supports of a canonical arithmetic concept class, not just the largest support size. The finite polynomial exposes the different roles of distinct primes and their exponents: the number of primes limits the rank, while exponents alter the number of witnesses at each rank. The private-label criterion explains the restriction and gives a direct test without enumerating all Boolean traces; the exact top coefficient and the boundary at n=1,2 give additional concrete information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
