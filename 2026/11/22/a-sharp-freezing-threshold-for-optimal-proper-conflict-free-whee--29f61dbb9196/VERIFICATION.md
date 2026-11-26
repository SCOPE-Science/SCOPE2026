---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The hub colour is absent from the rim, so the rim vertices automatically have a neighbourhood witness; the hub needs a colour used exactly once on the rim. Three named colours do not suffice (an odd rim is not 2-colourable and a properly 2-coloured even rim has two equally sized parts of size at least two). Giving one rim site its own colour and alternating two others off it proves that four suffice. For n≥5 at most one rim colour is a singleton, since n−2 occurrences of a third colour exceed the rim independence number. Thus the fixed-hub states consist of a chosen singleton site and colour, and one of two alternating orders. There are 6n per hub. A non-singleton can only move to the singleton colour away from its neighbours, and must leave another singleton behind; a singleton move would leave no witness. This freezes every state for n≥7. For n=5, encoding the state by the singleton site p and the cyclically ordered tuple (singleton, next colour, following colour), one allowed move advances p by 1 and rotates the tuple by one, and the other is its inverse. Each orbit has length lcm(5,3)=15; the 30 states per hub give two cycles. For n=6 the thrice-used colour stays fixed, and a move advances p by 2 or −2 and swaps the other colour roles; the orbit has length lcm(3,2)=6. This yields six cycles per hub. At n=3 every assignment is frozen by properness, and at n=4 two singleton colours and one opposite repeated pair give 12 states per hub; changing a singleton destroys both witnesses. The hub itself cannot move. Independent direct enumeration of all four-palette assignments for 3≤n≤7 confirmed state counts 24,48,120,144,168 and the component sizes and degrees. Replay: python3 /workspace/review-evidence/2/exhaustive_check.py 3 4 5 6 7. The frozen verify.py and VERIFICATION.md were inspected, not executed. Finite enumeration is not the all-n proof.

## originality

PASS

The all-order optimal PCF transition classification is distinct from scalar PCF chromatic-number results and from wheel state or seed counts. Credit the known universal-hub PCF mechanism and ordinary 3-colouring where it coincides: the pentagonal fixed-hub case is exactly ordinary three-colour reconfiguration of C5 and is not in itself a new PCF mechanism. The six-cycle components at n=6 and universal freezing for n≥7 are where preservation of the singleton imposes additional structure.

## value

PASS

The connected-component structure, not just a count of states or the known optimum, answers when two optimal wheel colourings can be joined without losing a conflict-free witness. It identifies the exact mobile heaps of states at the two exceptional lengths and a permanent freezing boundary. This is a natural full-family reconfiguration benchmark with precise invariants, restricted to named colours and elementary moves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
