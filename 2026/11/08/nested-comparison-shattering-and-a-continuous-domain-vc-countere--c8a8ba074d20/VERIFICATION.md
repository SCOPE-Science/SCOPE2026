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

On a fixed ordered axis, two nonnested comparison queries (a,b),(c,d) with a<=c and b<=d obey a preferred to b => c preferred to d by the no-valley property, so cannot be shattered. Strictly nested pairs can be deleted as consecutive endpoint blocks in independently chosen orders, leaving all comparisons outside the selected pairs identical: this produces a strong coordinate cube. Choosing 2k axis positions and pairing extremes gives exactly binom(n,2k) supports, hence VC=floor(n/2). The adaptive extreme-pair deletion tree has 2^(n-1) distinct consistent paths; the class has exactly that many strict orders, proving Ldim=n-1. A common peak at k+1/2 and explicit utility samples 8i±1 on nested pairs realize all 2^k continuous preference labels with strict monotonicity on each side; interpolation gives infinite VC for unrestricted qualitative continuous single-peaked utilities. Independent full pair-comparison trace enumeration confirmed the nested-support criterion for n<=5; finite checks support, not prove, the universal statement.

## originality

PASS

The source provides the complete labeled comparison-shattering complex, fixed-complement cubes, exact VC and Littlestone dimension on every fixed-axis single-peaked ranking domain, plus a concrete common-peak infinite VC counterexample for unrestricted continuous one-peaked preferences. Classical endpoint-deletion enumeration, sign representation and elicitation complexity do not state the full binary-pair shattering support classification. The Basu–Echenique 2020 paper does explicitly give finite VC as an illustrative claim for qualitative real single-peaked preferences, but the current explicit counterexample shows that illustration does not apply as written to unrestricted utilities; it does not impugn their separate main expected-utility results.

## value

PASS

Complete classification of shattered pair-comparison supports and strong cubes for a standard social-choice domain is a natural combinatorial invariant. The exact VC versus adaptive Ldim gap is meaningful for online preference learning, and the continuous common-peak construction identifies a sharp limitation of a widely cited qualitative finite-VC example. These are structural and conceptually motivated results, not a tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
