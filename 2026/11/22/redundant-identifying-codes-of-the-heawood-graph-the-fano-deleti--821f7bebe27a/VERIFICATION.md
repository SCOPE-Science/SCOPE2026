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

# Verification of the redundant identifying-code census

The graph has fourteen vertices. The two included standalone checkers enumerate all \(2^{14}=16{,}384\) subsets, not a sample.

To run the Fano-incidence and orbit checker with Python 3:

```sh
python3 verify_fano.py
```

Expected first output line: `VERIFY_FANO_OK`. This reconstructs lines from cyclic residues, verifies the equivalent two-detector and pairwise-symmetric-difference tests, compares against the geometric deletion classification mask by mask, checks the full cardinality polynomial, tests extension of every admissible deletion to a four-set and constructs all 336 automorphisms to obtain two four-deletion orbits of sizes 14 and 84.

To run the structurally independent direct-failure checker with a C++17 compiler:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct
./verify_direct
```

Expected output: `VERIFY_DIRECT_OK counts=98,224,91,14,1 minimal=98`. This checker constructs incidence by binary-vector dot products in dimension three, removes each detector in turn, tests all fourteen closed-neighborhood signatures for nonemptiness and distinctness, and classifies inclusion-minimal detector sets.

Both procedures enumerate the full fixed graph. The geometric classification and the complete proof are in `RESULT.md`. Exhaustive finite computation does not imply analogous statements for larger projective planes; the output is not an independent scholarly audit or a historical-priority certificate.
