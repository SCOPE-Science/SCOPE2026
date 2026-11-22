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

The report proves the parameter-general theorem by explicit Boolean trace witnesses and a mod-two cocycle argument. The finite tests are independently executable consistency checks, not substitutes for the all-graph proof.

Run `python3 verify_field.py` using Python 3 standard libraries only. The code models the sixteen-vertex graph as the additive Cayley graph of \(\mathbb F_{16}\), where the generating set is the five nonzero cubes. It checks all strongly regular parameters, enumerates every support through four vertices, validates triple-type equivalences, computes binary boundary ranks, and detects the odd cocycle pairing.

Compile `g++ -O2 -std=c++17 verify_folded.cpp -o verify_folded`, then run `./verify_folded`. This independent implementation defines the same graph on even-parity five-bit words with Hamming-distance-four edges; it builds all supports from scratch and performs an independent binary boundary calculation. No stored adjacency list or face table is shared by the two implementations.

The observed outputs are in `verify_output.txt`. Both programs reproduce open f-vector \((1,16,80,160,0)\), closed f-vector \((1,16,120,320,0)\), boundary-two ranks \(65\) and \(104\), and reduced mod-two Betti pairs \((0,95)\) and \((1,216)\), respectively. The verified finite data refer to Clebsch only. General conclusions about Gewirtz and all other admissible strongly regular graphs rely on the proof, not a Gewirtz census. No independent external verification is asserted.
