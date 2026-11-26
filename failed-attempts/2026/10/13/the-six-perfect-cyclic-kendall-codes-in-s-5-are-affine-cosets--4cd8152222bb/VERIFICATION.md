---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With permutations viewed as functions from positions to symbols and T the identity plus the five cyclic position transpositions, B(g)=gT has size six. A perfect code is an exact cover by these balls and has 20 centers. Branching on one uncovered vertex exhausts every compatible ball that could cover it, discarding only intersections with a chosen ball. An independently written enumeration generated the 120 tuples, made the five position swaps including (4,0), and recursively chose an uncovered point of least compatible degree. It yielded 254 nodes and exactly six covers of size 20. Direct construction of all left cosets of the order-20 affine subgroup gave exactly the same sets, with disjoint balls and full coverage. The stabilizer under left multiplication of A is A, since gA=A is equivalent to g∈A. Frozen verification/verify.py was inspected but not executed. The result is limited to degree five, radius one, and the cyclic position-swap metric.

## originality

FAIL

The exact classification is already covered by distinct indexed Resultary record 7b31d21a4b95: same graph, radius, labeled count and six affine left cosets; the orbit and stabilizer are automatic from that statement. The earlier Buzaglo–Etzion paper instead supplies the affine example only in the passages inspected. This is a finding of demonstrable equivalent coverage in the available record, not a finding that that indexed result has historical priority. The distinct records have different proof organizations and catalogue dates, which alone do not establish the order of the discoveries.

## value

FAIL

As a first result the natural finite equality classification would resolve the first cyclic instance of the original question. As reviewed, it is an alternative exhaustive replay of an already covered classification; the unnormalized search supplies no distinct structural or algorithmic gain, and the orbit and stabilizer add no mathematical content to the established coset description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
