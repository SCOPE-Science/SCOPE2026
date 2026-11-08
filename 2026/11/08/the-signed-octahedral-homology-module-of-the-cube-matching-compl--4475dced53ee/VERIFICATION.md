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

The self-contained `verify.py` was executed with Python 3. It constructs the twelve cube edges, all 107 nonempty matching faces, and 252 face-poset covers. It generates 51 matched Hasse pairs, confirms the five exact critical faces, and topologically sorts the directed Hasse graph to establish acyclicity. Thus the homology-concentration premise is a complete finite certificate, not a numerical guess.

The program independently checks all forty-eight affine automorphisms and 4,560 signed boundary identities, computes their reduced Lefschetz numbers, and compares these with the characters of the signed-coordinate exterior square and flip-parity line. The identity character equals four; Fourier multiplicities on the eight-element translation group are exactly those of the three weight-two characters and the weight-three character, with no trivial character.

`verification_output.txt` records the complete emitted summary and begins with `CUBE_MATCHING_OCTAHEDRAL_REPRESENTATION_PASS`. The mathematical proof also invokes standard theorems of discrete Morse theory, rational character theory, and characteristic-zero finite-group averaging; these theorems are not proved from scratch in the verifier. Verification does not establish originality or constitute an independent audit. The known nonequivariant wedge decomposition is not treated as new.
