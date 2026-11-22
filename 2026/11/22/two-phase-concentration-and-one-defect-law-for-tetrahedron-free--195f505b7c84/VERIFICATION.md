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

# Reproducibility and limits

The standalone \`hypergraph_link_verify.py\` (standard-library Python) tests the new claim through three independent finite methods: the explicit shore polynomial, inclusion-exclusion on forbidden ternary triples and exhaustive link-edge enumeration. The exact rational count and decomposition are checked for \(n=1,2,3,4\), with exhaustive link-bit enumeration through \(n=3\). The code also compares finite ratios at \(n=8,12,20,40,60,100\). The recorded output is in \`verification_output.txt\`.

These checks cover only the displayed finite cases. The unrestricted exact formula and conditional asymptotics rest on the written combinatorial counting argument and explicit remainder inequality, not any numerical extrapolation. Independent audit has not been performed; no independent certification is claimed.
