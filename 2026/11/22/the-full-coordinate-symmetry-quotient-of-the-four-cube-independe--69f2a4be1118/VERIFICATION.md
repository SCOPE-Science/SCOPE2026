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
# Verification instructions

Compile and regenerate the complete finite collapse certificate:

```sh
g++ -std=c++17 -O2 compute_q4_orbit.cpp -o compute_q4_orbit
./compute_q4_orbit q4_orbit_certificate.txt
```

Or directly replay the supplied certificate without compiling:

```sh
python3 verify_q4_orbit.py q4_orbit_certificate.txt
```

The Python 3 standard-library verifier independently reconstructs the cube's adjacency relation, all independent faces, the full affine symmetry group of order \(384\), the orbit of every chain, the face incidences and the dynamic free-face conditions for all \(3360\) collapse pairs. The complete dictionary of distinct flags has cardinality \(2,199,938\), also certified by an independent ordered-Bell formula. Expected final output:

`VERIFY_OK_Q4_INDEPENDENCE_FULL_ORBIT_COLLAPSIBLE faces=742 flags=2199938 group=384 cells=6721 collapses=3360 remaining_vertex=0`

The certificate consists of \(6721\) explicit orbit-cell representatives and \(3360\) ordered collapse pairs. Every index is checked against the same data actually supplied. The assertion is finite and exact. No independent third-party scientific audit is claimed, and no general conclusion for higher cube dimensions is certified.
