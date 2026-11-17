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

Horn closure monotonicity makes every explanation family order-convex in Boolean inclusion order. One omission witness per context in a minimal obstruction is distinct; any strict three-chain would violate the middle family order-convexity. A random maximal Boolean chain meets witnesses at most twice, and the 2-LYM/Sperner inequality bounds their cardinality by the two largest levels. For sharpness use all k and k+1 subsets, remove one per context, realize each order-convex family as upward closure intersection downward closure through finite exact context guards, g and integrity heads; the rules are acyclic. h=0 singleton and h=1 nonempty-family boundaries are handled, with first values 1,2,3,6,10,20,35.

## originality

PASS

The source Yang article states the general 2^h bound, qualitative unbounded obstruction rank, and order-convexity, but not the exact fixed-h two-Sperner Helly number with acyclic realization. Generalized Sperner/LYM upper bound is old and not credited; the specific application with matching Horn realizability yields a distinct exact resource classification.

## value

PASS

The exact maximum size of a minimal context obstruction as a function of the natural hypothesis budget h is a motivated combinatorial resource law. Sharp acyclic Horn realization shows the 2-Sperner bound is genuinely achievable rather than only a loose generic convexity estimate. No complexity or algorithmic generalization is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
