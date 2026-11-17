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

Conditioning on the first uniformly ordered vertex proves star law I_m∈{1,m} with probabilities 1/(m+1),m/(m+1). For the private pendant extension, first hub gives size 2, first new leaf reduces to K_{1,m−1} with one extra selected, first attachment leaf gives m, and any other old leaf leaves an edge plus isolated leaves, also m. Consequently P(I_m^+=2)=(m+1)/(m(m+2)), P(I_m^+=m)=1−this. Direct exact fraction subtraction gives a strict positive upper-tail difference at 2 and strict negative difference −1/[m(m+1)(m+2)] at m while mean increases (m²+m+2)/[m(m+1)(m+2)], for each integer m≥3. The only connected graphs on 1..3 vertices K1,K2,P3,K3 and their possible pendant attachments are exhausted, showing sharp minimum original order four. Independent rational first-vertex recursion corroborated m=3..8; finite enumeration is not used as all-m proof.

## originality

PASS

The natural stochastic-order crossing for a single pendant extension (despite an increasing mean) and the smallest connected-original size were not covered by the inspected closest random-greedy MIS literature or relevant published records. Krivelevich et al develop local-limit laws and expected-size monotonicity/edge deletion phenomena, not this exact opposing upper-tail family. Results on random-greedy edge matching concern a distinct greedy object and can have opposite monotonicity. This is a best-of-knowledge finite-structural originality judgment.

## value

PASS

This is a sharp minimal counterexample to a natural stochastic-monotonicity intuition under graph augmentation. A complete two-point distribution and opposite upper-tail inequalities are more informative than an expected-size increase; the minimal four-vertex connected obstruction supplies a reusable boundary case for greedy graph algorithms, despite being elementary and finite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
