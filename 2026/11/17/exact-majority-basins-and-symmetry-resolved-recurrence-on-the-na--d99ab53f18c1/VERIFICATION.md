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

# Verification

The package includes complete source code and captured outputs. Reproduce from its extracted working directory using:

```sh
g++ -std=c++17 -O3 nauru_direct.cpp -o nauru_direct
./nauru_direct > nauru_direct_output.txt
python3 nauru_cayley.py > nauru_cayley_output.json
```

The first program constructs the generalized Petersen adjacency independently and checks all \(2^{24}\) labelled configurations directly. Its `t=` rows refine first periodic entry by ultimate least period. The second program reconstructs the same graph using its ordered-injective-triple Cayley representation, computes both twelve-bit maps over all 4,096 states, enumerates all 494-by-494 shore-fixed pairs, their exact basin products, and all group-and-time symmetry classes. It uses only the Python standard library.

Cross-checks from the recorded outputs: 494 fixed configurations, 243,542 primitive-two phases, initial 244,036 periodic configurations, sharp first-entry time five with 584,640 states entering then, and total 16,777,216 states. The Cayley certificate separately computes 121,771 temporal two-cycles, the basin totals 979,268 and 15,797,948, group order 144 and 17/1,147 symmetry classes.

Limit: These checks are exhaustive because the object has exactly 24 binary vertices; they do not establish any theorem on an unbounded graph family. Scientific evidence is computational with a fully specified finite algorithm, supported by the factorization in the proof, not an external independent certification.
