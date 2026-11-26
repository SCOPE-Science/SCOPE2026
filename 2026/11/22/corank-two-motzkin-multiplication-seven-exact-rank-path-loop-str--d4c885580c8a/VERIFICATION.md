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

A side of a rank-(n−2) diagram has exactly two omitted vertices: they can be singletons for any pair, or a hook for an adjacent pair, because a hook enclosing a propagating vertex would violate planarity. The other vertices match in increasing order, so either outer side is free, with W_n choices each. For disjoint inner omitted sets all four omitted vertices carry a boundary connection, and any hook joins stubs on the same side, leaving rank n−4 and no floating component. The three ordered counts with zero, one, and two hooks are respectively C(n,2)C(n−2,2), 2(n−1)C(n−2,2), and (n−2)(n−3). With one common vertex the no-hook, one-hook, and two-hook cases give counts n(n−1)(n−2), 4(n−1)(n−2), and 2(n−2): the common vertex floats only without hooks, and two overlapping hooks give exactly one new opposite-boundary connection. With coinciding sets there are two isolated paths, one hooked path, or a two-edge loop, with counts C(n,2), 2(n−1), and n−1. This yields all seven coefficients after the free factor W_n². The disjoint case cannot occur at n=3, so omit its term. The loop event has exactly n−1 inner pairs out of W_n², consistent with the reported probability and total mass W_n⁴.

## originality

PASS

Pass the closed aggregate rank/path/loop distribution for arbitrary ordered corank-two Motzkin factors. The one-sided parametrization and individual-product weighting by middle components are prior. In particular Dolinka–East–Gray §5.2 defines the loop/path twist for partial Brauer diagrams and §5.3 explicitly restricts that same twist to the Motzkin subalgebra. Those formulas define terms in an aggregate but do not calculate the seven coefficients. Inspected nearby census results count other diagram classes or different fibers.

## value

PASS

The first rank class allowing both singleton omissions and hooks gives a natural product census that distinguishes loss of rank from the creation of floating paths and loops. The exact joint law, including the rank-preserving overlap of distinct hooks, is useful for random product calculations and evaluating rank-refined class sums in weighted multiplication. Those outcomes are not available from diagram-class dimensions alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
