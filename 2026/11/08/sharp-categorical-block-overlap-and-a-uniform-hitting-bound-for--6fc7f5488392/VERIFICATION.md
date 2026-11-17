---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The weighted induction over two depth-n categorical stochastic trees is valid for arbitrary nonnegative starting masses: the overlap is a jointly concave sum of minima in the first-symbol laws, minimized at extreme categorical laws. Coincident peaks yield F_n(s,t)>=F_{n+1}(s,t) by marginalization and differing peaks yield the extremal two-law product F_{n+1}. The oldest-symbol construction attains the lower bound for states (1,...,1) and (2,...,2), proving minimax sharpness. The multinomial formula, Hellinger square-root tilt and lazy symmetric span-one local CLT with dominated summation give the exact constant coth(t/2)/sqrt(4*pi*u). Neutral symbols imply strict decline for q>=3. The deviation-matrix identity plus oscillation contraction yields the normalized hitting bound, sufficient (not necessary) for uniform hitting times when a<theta. Independently verified exact rational overlap and attained minimax q=3,4 and d=1,2,3; this finite computation is not a universal proof.

## originality

PASS

The nearest Skórski 2026 paper gives binary minimax and general-alphabet conditional hitting estimates; its full appendix was inaccessible in this run, so possible stronger q-ary implication is retained as an explicit originality risk. Accessible Makur–Singh establishes general Doeblin contraction principles, not the exact q-ary product overlap law. The separate q>=3 minimax formula and sharp lazy-walk constant appear not directly established by checked material, best-of-knowledge PASS subject to Skórski full-text comparison.

## value

PASS

A sharp q-ary finite-memory block-coupling invariant and its exact asymptotic constant naturally extend binary theory and sharpen dimension-uniform hitting-time regimes. The explicit fixed-parameter sufficient threshold is valuable without claiming necessity for real hitting times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
