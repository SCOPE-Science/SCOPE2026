---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible scientific verification

The two independent C++17 source programs implement the same explicitly defined fourteen-vertex nonincidence dynamics using different graph-construction and state representations. `verification/coheawood_a.cpp` enumerates the whole functional digraph and determines every cycle and basin by indegree peeling, while `verification/coheawood_b.cpp` evolves every excited/refractory bitmask directly until first rest. Both exhaustively classify exactly 4,782,969 states; their full standard output is embedded in the matching `.out` files. The histograms agree cell by cell: `(1,16383,803001,2393358,1107890,364518,90258,7560)` over first extinction times zero through seven. A separate Python implementation checks the Fano sharp witness and projective-plane nonincidence Gram matrix identities for orders two and four.

To replay, run `g++ -std=c++17 -O3 -o a verification/coheawood_a.cpp && ./a > a.out && cmp a.out verification/coheawood_a.out`, then the analogous steps for `coheawood_b.cpp`, then `python3 verification/verify_design.py > p.out && cmp p.out verification/verify_design.out`. Code and embedded expected outputs are executable and standalone; these checks concern finite cases only. The arbitrary-even-order conclusion relies instead on the complete analytic proof in `RESULT.md`, particularly the event-time Fourier obstruction and algebraic-integer argument.

Independent external mathematical validation is not performed. Historical priority is qualified by incomplete access to certain archival papers and possible unindexed earlier equivalent computations.
