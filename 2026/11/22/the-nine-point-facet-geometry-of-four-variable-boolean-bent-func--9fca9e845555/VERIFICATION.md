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

# Reproducible mathematical checks

Run `python3 verify_quadratic.py` in the directory containing `nine_trace_witnesses.json`. It builds all rank-four binary alternating forms, generates the 896 candidate Boolean functions, checks the weight distribution, full proper-subset covering counts, affine-orbit transitivity of the 4480 nine-point facets, all 512 traces on the representative nine-set, and the seven- and eight-point obstruction descriptions. Success prints `QUADRATIC_BENT_FACE_CERTIFICATE_PASS`.

Compile `verify_walsh.cpp` with `c++ -O2 -std=c++17 verify_walsh.cpp -o verify_walsh`, then run `./verify_walsh`. It independently enumerates 65536 Boolean truth tables and uses the exact fast Walsh–Hadamard transform, not the polar-rank formula. It verifies all 65536 query supports against the complete bent truth-table class and the proper ten-block criterion. Success prints `INDEPENDENT_WALSH_TRACE_ENUMERATION_PASS`.

The witness JSON specifies the 512 binary trace labels on points \(\{0,1,2,4,5,6,8,9,10\}\), with a corresponding 16-bit truth-table mask for each label. The Python verifier decodes and checks every label. No external packages are required, and no probabilistic test is substituted for an exhaustive one.

The finite calculation proves nothing about Boolean bent classes in six or more variables. Exactness of this finite result remains subject to independent audit beyond these two checked implementations.
