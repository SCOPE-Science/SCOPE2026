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

The standalone `gopel_verify.py` uses integer bit masks, no third-party packages, and all 720 permutations of six labels. It reproduces all eleven class spectra and each rational-node profile, checks the 16 node classes and all 15 isotropic subgroups, and independently reconstructs the Göpel family via 16 trope six-node incidence sets among all four-subsets. Successful output ends `GOPEL_FROBENIUS_720_PERMUTATIONS_VERIFIED_OK`.

For a manual check, a transposition fixes three perfect matchings, hence three maximal isotropic planes, and exactly four affine cosets on each, producing twelve rational tetrads. Of these, six contain four rational nodes and six contain none.

Finite enumeration proves the finite permutation reduction exactly, and the separate symplectic two-division argument proves the reduction is uniform over all odd-characteristic genus-two curves. The computations do not count actual curves of each branch type, imply rationality of Cremona automorphisms, verify historical priority exhaustively, or constitute independent validation.
