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

# Verification of the finite phase portrait

The graph uses two staggered five-rings and their poles as specified in `RESULT.md`; both verification programs have their own graph constructors. It has 12 vertices, 30 undirected edges and five neighbors per vertex.

Run the following exact computations from a clean directory containing the two source files:

```sh
python3 check_majority.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_majority.cpp -o verify_majority
./verify_majority
```

The Python program enumerates all 4096 configurations, exhaustively constructs 120 adjacency-preserving automorphisms, checks the dynamics commutes with each automorphism for every state, and computes the seven geometric two-cycle orbits. The C++ program independently evaluates the threshold by ten three-neighbor conjunctions, tests the first periodic entrance time of every state, and reproduces every stated basin count. `checks_output.txt` contains the observed output. The graph's standard identity was cross-checked against an independent built-in icosahedral graph constructor, but neither main checker imports external packages or requires this identity test to run.

Critical assertions include the exact first-entry histogram, exactly 14 fixed states, exactly 156 primitive two-cycles, 12 isolated cap basins, both consensus basins of size 1586, the 2/4/6/14 basin distribution of two-cycles, and sharp entrance time five with 240 attaining configurations. The witness integer 87 follows the trajectory 87, 47, 23, 41, 16, 0. Direct finite enumeration establishes these assertions only for this stated graph and rule. No finite experiment is used to infer a claim for all graphs.
