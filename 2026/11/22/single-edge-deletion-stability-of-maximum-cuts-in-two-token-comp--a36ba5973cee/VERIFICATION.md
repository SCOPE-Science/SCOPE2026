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

The red graph is on base labels and includes the possible red pair ab; its edge set describes token colors, not present base edges. Each intact token adjacency shares a unique base label v, so the cut score is the sum of r_v(n−1−r_v). Removing the base edge ab deletes only the (n−2) adjacencies {a,w}--{b,w}, losing exactly one per mismatched external label. Maximizing the local terms gives the two central degrees at even order and the single central degree at odd order; for n≡3 mod 4 an all-central degree sum is odd, forcing a loss of at least one and giving exactly the one-defect equality condition. Equality at M_n for the faulted graph forces zero mismatch. In the displayed constructions, a,b have degree 1+|S|, an S vertex has degree |S|+1−deg_D(s) plus its cross-degree, and a T vertex has degree |T|−1 plus its cross-degree. Substitution gives the required central values in all four residues (including just the unmatched T vertex one below center for n≡3); n=3,4 are checked separately. At n=5 the intact score is 20 minus a sum of squared degree deviations; loss one is impossible by parity. The score-20 red graphs are exactly the twelve 5-cycles and every one loses two when ab is deleted. All remaining faulted optima have squared loss two and no mismatch. For these, when both endpoint degrees are two the (t,s)=(0,2) case has three choices of the synchronized neighbor set, and the permitted red edges on the remaining triple are either one of the two edges from its non-neighbor to a neighbor, or both; (1,1) is the complement. The cases (1,0),(0,3) contribute one each. Thus there are 12+9+9+1+1=32 ordered optima. Independent enumeration at n=3,4,5,6 gives scores 2,8,18,36 and ordered multiplicities 2,2,32,56 and checks the optimizer predicates against actual cut scores. The all-order conclusion rests on the construction and bound, not the enumeration.

## originality

PASS

The universal deletion-stability theorem with optimizer classification is distinct as a whole in the inspected material. In particular, the odd orders n≥7 require a synchronized construction beyond the compared intact and split-graph results. Do not credit the intact value/degree mechanism, the even-order value, or the isolated n=5 value and multiplicity as distinct: the first two are prior results or immediate implications, and the distinct same-day split-graph record covers the last two at theorem/log level respectively. It does not classify the n=5 optimizers or supply the all-order statement. No chronology is inferred from a same-day date.

## value

PASS

A one-edge fault in a highly symmetric parent graph removes a whole matching in the token graph, and the persistence of the exact cut optimum is not merely monotonicity. The all-order synchronization criterion and explicit residue constructions explain when the intact upper bound survives, including the odd orders left open by previously known parity bounds. The five-cycle obstruction and complete exceptional optimizer description explain why that lone order fails, beyond the already tabulated exceptional number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
