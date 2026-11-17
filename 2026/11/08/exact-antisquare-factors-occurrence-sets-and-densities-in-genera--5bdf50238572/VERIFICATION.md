---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS — A length-2k antisquare contains k ones. The valuation-parity word has ones only at i≡b−1 mod b, so separation immediately excludes k≥2 at b≥4 and k≥3 at b=3. At b=3,k=2, the only candidate is 1001 at i=3q+2, with even ν_3(q+1),ν_3(q+2). At b=2 every even-index symbol is 0; k ones force alternating words and parity of complementary halves requires odd k, while four consecutive odd positions contain one forced 0, leaving k=1 or3. The exceptional length-six factors occur exactly when ν_2(q+2) is positive even. Transition 10/01 positions are odd-valuation tests ν_b(i+1),ν_b(i+2); floor-series H_b and E count all starts at each finite N and geometric sums give densities 1/(b+1),1/6,1/12, with logarithmic floor errors. Independent direct enumeration for bases 2,3,4,5,7 over starts i<400 and orders k≤23 exactly matched all factor supports and prefix counts, including base2 133+133 transitions and 33+33 length-six starts, base3 100+100 transitions and 67 occurrences of 1001. Proof, not test horizon, establishes infinite completeness.

## originality

PASS

PASS — The final combined result is all-base antisquare support together with every exact starting-position set, finite cutoff formula and limiting density for valuation-parity period-doubling words. Currie (2023) studies classical base-two forbidden factors and partly covers base-two support; Baranwal et al. (2023) classify minimal antisquares generally, which is not an arithmetic enumeration of these automatic-word occurrences. Their substantive theorems do not imply the claimed all-base exact valuation census from title matching alone. The known support case is credited, and quantitative refinement is distinct.

## value

PASS

PASS — This is a complete, naturally motivated factor-language and frequency theorem for a standard arithmetic automatic-word family. Every possible antisquare has an exact index description and finite-prefix count, not just finite experimental support or a generic automaton algorithm. Base-dependent sharp transitions and all orders give mathematical structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
