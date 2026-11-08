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

# Verification details
Run `python3 verify.py` with a standard Python 3 interpreter in the directory containing this document. The program needs no external packages. The full expected output is provided in `verify_output.txt`.

The graph, exact face predicate, edge ordering, and boundary orientations are all generated in the verifier. Two independent enumerations find 272 perfect matchings. An exhaustive independent check of 41,025 graph matchings, using completion on unmatched vertices, agrees with the 30,561-face complex generated from the perfect matchings. The forward and reverse acyclic matchings are each checked by a complete directed topological sort of the Hasse graph, with 150,720 incidences.

Forward matching: 15,173 matched pairs; 124 critical three-cells and 91 critical four-cells. Its exact integer Morse boundary is \(124\times91\), has 70 unit invariant factors, and no remaining nonzero block. Reverse matching: 15,154 matched pairs; 134 critical three-cells, 110 critical four-cells, nine critical five-cells, with exact boundary ranks 80 and nine and vanishing boundary composition. Full original simplicial mod-two boundaries are reduced independently to confirm Betti ranks \(54\) in dimension three and \(21\) in dimension four, with all other reduced ranks zero.

The completed topological claim uses discrete Morse theory and the fact that maps from \(S^3\) to a wedge of three-spheres are completely classified by their degree vectors. This supplies the homotopy conclusion from the unit Smith factors; mod-two checks by themselves would not prove torsion-freeness or the homotopy type.

Limits: Exhaustion is specific to the finite graph defined here. No argument about higher-dimensional hypercubes, an integral symmetry character, or an independent external audit is included.
