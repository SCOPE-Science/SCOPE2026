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

In the closed graph of intercept and mechanical coding, two different phases cannot give the same word: the translated coding intervals differ on an open arc, and irrational rotation visits it off the endpoints. The graph thus defines a continuous phase factor, even at split boundary codings, and a phase gap δ gives a positive symbolic separation η(δ) at every common iterate. For length N, the prefix sums at a nonsingular representative 0<t<1 are floor(t+jα) for 1≤j≤N; each jumps once at a distinct cut. Different complementary cells therefore have distinct words, and limits at a cut give adjacent words, not additional ones. Fixed precision requires only an O(1) extension of the N-step block, giving O(N) spanning growth and O(N^k) for ordered products and their two factors. For a lower bound, fix k disjoint positive-length arcs with pairwise phase gap δ. Equidistribution puts Θ(N) cut points in each arc, so each supports Ω(N) distinct length-N words at nonsingular intercepts. Choosing one per arc gives Ω(N^k) subsets. Two different choices disagree in some labeled word at a time before N; the corresponding point is then distance 1 from the same-label point in the other subset and at least η(δ) from every other label, giving fixed-scale Hausdorff separation. With k=1 there are no competing labels. For k≥2 all iterates remain in the compact invariant space of k-point sets with pairwise phase gaps at least δ, which cannot converge to a singleton or lower-cardinality stratum. Singleton collapse is a homeomorphism on this compact subspace onto its image, so its inverse preserves the fixed separation at another fixed scale. The full hyperspace contains every invariant layer and has infinite polynomial entropy. The finite layers and their suspensions have zero ordinary entropy by product and factor bounds. Replay path: checker.py and checker_output.txt lines 1–6, inspected not run. The single rational approximant 233/377 through length 60 and finite arc examples corroborate the coding construction, not equidistribution for every irrational slope, arbitrary k, or the collapse lower bound.

## originality

PASS

The standard Sturmian base exponent and ordered-product upper bound are not the distinct claims. The material lower bound is the full exponent after forgetting labels and then collapsing the singleton stratum in a minimal infinite system. The strongest published symmetric-product formula has hypotheses that fail here, and the strongest same-system catalogue result identifies the k=2 quotient but gives only ordinary entropy, not the polynomial exponent.

## value

PASS

Polynomial entropy detects an entire growth hierarchy hidden by ordinary entropy for a canonical minimal aperiodic example outside the finite-chain-recurrence and wandering-point hypotheses. The lower bound after the two different quotient operations is the meaningful part, and the phase separation argument explains exactly why observing only sets, even after collapsing singletons, does not erase the exponent here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
