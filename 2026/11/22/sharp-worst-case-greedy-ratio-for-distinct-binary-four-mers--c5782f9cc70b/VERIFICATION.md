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

Independently reproduced the full finite classification with an exact de Bruijn-graph BFS for OPT (state: final triple, exact mask of factors seen, followed by minimization over supermasks), and a separately written head-to-tail matching recursion for all maximizing ordered Greedy ties. To justify the compression without relying on the retrieved literature, maintain pairwise substring-free current strings and a nonincreasing maximum overlap k, initially at most 3. Upon merging X to Y at overlap k, any overlap from XY to another Z exceeding k either comes wholly from Y, contradicting maximality, or contains all of Y in Z, contradicting substring-freeness; the incoming case is symmetric. If XY newly contains Z, the occurrence must start before Y starts and end after X ends, giving a larger X-to-Z overlap. The reverse containment would put X in Z. Thus the invariants hold after every merge, including ties; once zero is reached, all remaining merges save zero. The length of each positive overlap is determined by the end words. Reversal with merge directions reversed, and complementation, preserve both problems. All 65,535 nonempty masks entered the symmetry filter (16,959 representatives); exact cross-products give the unique best representative 1343, ratio 17/11, and labeled masks 1343, 5431, 60584, 64672. Independent literal-string recursion visited 418 states for mask 1343, confirmed the stated legal length-17 output is among the worst outputs, and verified the given length-11 optimum by the factor-window lower bound.

## originality

PASS

Pass is for the all-cardinality upper bound and absence of any other equality sets, not for the eight-word obstruction, the exhibited sharp instance, or endpoint compression by itself. Closest indexed companion claims overlap on the eight-word extremizers; no inspected statement imposes the necessary upper bound for larger input sizes. Same-day dating does not settle priority. Literature and companion-file access limits are material to the historical judgment, not to the independent census.

## value

PASS

Binary four-mers are a natural complete finite domain of distinct equal-length reads. The worst legal tie quantifier is an algorithmic guarantee, not a distributional observation. Settling every larger input size and isolating one exact equality orbit turns a known obstruction into a sharp guarantee for the domain. No claim is made about larger alphabets, longer words or random-tie performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
