---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

I enumerated perfect matchings independently by permutations between the checkerboard bipartition sides, computed all static traces and solved depth feasibility by the exact two-fibre splitting condition. The five triples were (1,0,0), (2,1,1), (3,1,1), (5,2,2), (8,2,3); all eight leaf witnesses and all thirteen edge frequencies in the L5 certificate agreed. The unique 4-of-8 coordinate is V3; shattering a triple would require three such coordinates. The cardinality bound excludes four online rounds, and the explicit tree reaches three. Each chain bridge has an even side and is the only edge crossing that cut, so is forbidden in any perfect matching. The class is exactly the independent tuple of block matchings, with constant-zero bridge queries. Static shattering is blockwise and adds, and tree concatenation gives 3s rounds, the maximum permitted by the 8^s concepts. The graph conditions follow by laying ladders side by side with bridges between corners and taking compatible bipartitions. Replay: python3 /workspace/reproduce_2.py <frozen certificate.json>, output /workspace/reproduce_2.txt. The arbitrary-s proof does not rely on any finite enumeration of amplifier graphs.

## originality

FAIL

Demonstrable equivalent coverage in a distinct indexed record: Resultary 94247ccc912f proves the exact L5 physical-edge dimensions (2,3), and the exact 8^s, 2s, 3s bridge-chain separation on the same restrictive graph class. It uses upper-right to lower-left connectors rather than upper-right to upper-left; both sets of connectors are identically zero queries by the same even-cut argument, yielding identical incidence concept systems up to coordinate relabeling. This is a coverage finding, not a claim that the other authors or record preceded this one. What remains distinct in presentation is the elementary n<5 baseline and the horizontal-only contrast, not a substantial uncovered result that would justify passing or a repair.

## value

PASS

The principal mathematical question is worthwhile: distinguishing physical edge-query online dimension from static rank at the first possible short ladder, and locating the mechanism in extra rung tests, gives a useful sharp example. The linear separation in connected restrictive graphs is more informative than an arbitrary dimension table; bridge exclusion also explains its limitation to graphs not required to be matching-covered. This scientific significance is of the theorem itself and does not make its equivalent indexed coverage original. The isolated elementary short-ladder baseline is not a viable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
