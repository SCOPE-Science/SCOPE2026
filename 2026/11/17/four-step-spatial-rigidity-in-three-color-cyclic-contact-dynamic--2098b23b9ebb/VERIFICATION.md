---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

An F⁴-periodic site advances 0 or3 times, since each advance is +1 modulo3. An adjacent site changing three times would force an allegedly static site to change; connectedness gives either all static (three monochromatic states) or all change thrice. In active case a site trace is determined by initial color c∈Z3 and one of four hold times, 12 traces/site and 144/two-row column; an admissible 3-column transfer state uses original five-neighbor update, with 20,736 ordered-pair vertices. Inspecting verify_transfer.cpp and verify_masks.py shows complete candidate enumeration and independent SCC algorithms. Independently reimplemented transfer constraints gave 20,340 edges, 20,718 SCCs, exactly six directed simple 4-cycles. Every torus configuration corresponds bijectively to a closed transfer walk, so the cyclic graph classification proves all n, not just sampled widths. Source verifier identifies all 24 row-equal 2100 shifts/reversals/phase shifts; independently brute-executed original automaton for n=3..7 and found Fix(F⁴) counts [3,27,3,3,3].

## originality

PASS

Earlier two-dimensional cyclic automata develop defect/clock phenomenology and asymptotic excitation rates, but do not give the immediate F⁴ state census for the five-distinct-neighbor two-row Moore quotient. Closest indexed exact tori use different automata/thresholds or enumerate temporal three-cycles. Best-of-knowledge new precise recurrence theorem.

## value

PASS

An exact uniform population of temporal four-cycles and forced row equality across arbitrarily long strips is a natural all-circumference classification of the minimal nontrivial Moore-strip recurrence. The transfer proof rules out other oscillators, gives a concrete spatial rigidity mechanism, and exposes a sharp divisibility threshold; finite-state computation is exhaustive for this finite local transfer model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
