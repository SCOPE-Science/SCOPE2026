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

Run `python3 verify.py` in the same directory; no external packages or stored certificates are required. The program enumerates the complete \(2^{16}\) face-candidate universe, builds every simplicial boundary and computes binary ranks, then iterates through all \(384\) automorphisms and checks two independently implemented trace calculations against the stated character. It checks all sixteen translation Fourier averages, inner product, and six exact subgroup averages. The expected output is in `verification_output.txt`, with final sentinel `Q4_INDEPENDENCE_B4_CHARACTER_PASS`.

The binary rank proof determines rational homology concentration by rank comparison and Euler characteristic. The character is determined from signed Lefschetz traces, and its irreducible decomposition follows from translation weight spaces and the \(S_4\) action. Neither a finite experiment beyond this exact finite domain nor a general theorem for larger cubes is claimed.
