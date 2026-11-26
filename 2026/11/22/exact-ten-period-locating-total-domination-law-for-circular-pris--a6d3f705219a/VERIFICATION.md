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

Total domination makes all selected-neighbor signatures nonempty. Equal signatures of two unselected vertices then share a neighbor, so their cyclic column distance is at most two. For n>=5 the five consecutive columns are distinct and contain every neighbor needed for each forward comparison; iterating checks every possible collision, including at the wrap. Overlap of four-symbol states gives exactly the column words on a closed length-n walk and charges each column's population once. I independently implemented strip signatures as bitset intersections and computed exact sparse distances backwards from every terminal state. This gave 729 transitions and 41,728 finite entries in each of T^8 and T^18; all 65,536 state pairs satisfy identical finiteness and a weight shift eight on the finite ones. Multiplying by T^(n-8) transports this exact identity to every n>=8; it is not a conjectured pattern from trace samples. Independent direct subset enumeration gave minima 3,4,4,6,6,7 at n=3..8, and exact traces at n=5..18 agree with the claimed formula, completing the residue induction. The baseline cubic bound also follows by counting edges across S and its complement: at most 2|S| such edges and at least 2(2n-|S|)-|S|, since at most |S| outsiders can have distinct singleton signatures. Replay: python3 /workspace/reviews/reproduce.py 3; /workspace/reviews/reproduce-output.txt. The frozen verifier was inspected, not executed.

## originality

PASS

The same-graph Theorem 5 settles the 0,2,4 mod 5 classes and the 2026/11/2 counterfamily settles 3 mod 5 for n>=8 (n=3 was already known). The verified distinction is the remainder of the global classification: the 1 mod 5 class splits into the sharp lower-bound class 1 mod 10 and the genuine exception 6 mod 10. Neither the published conjecture nor the earlier counterfamily implies this. The theorem agrees with the conjecture at 6 mod 10, including n=16, and disagrees at n=11; the older upper bounds remain valid.

## value

PASS

It closes a specific published conjecture on a natural regular graph family and identifies the exact parity-sensitive exception to the general cubic bound. A finite integer identity controls all cycle lengths; value rests on the all-order optimum and sharp exceptional class, not merely on enumerating small prisms or reproducing the older 3 mod 5 counterexamples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
