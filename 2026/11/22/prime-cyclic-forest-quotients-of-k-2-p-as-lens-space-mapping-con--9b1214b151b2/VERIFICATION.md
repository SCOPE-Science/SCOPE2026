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

# Reproduction and boundaries

Run `python3 verify.py` using Python 3.10 or newer. The script uses only the standard library and constructs its own face sets and cellular boundary matrices; it does not load precomputed matrices, logs, or remote files. `verification_output.txt` is the actual saved output of this command.

For \(p=3\) and \(p=5\), the script enumerates all \(4^p\) possible selections of the two incident hub edges per leaf and independently checks the cycle criterion by union-find. It constructs the quotient of the barycentric cross-polytope boundary using actual orbits of strict face flags, checks that all integer boundary compositions vanish, and calculates chain ranks and Betti numbers over \(\mathbb F_p\) and \(\mathbb F_{101}\). The quotient-base vectors agree with \(\Sigma L_p\). The proof in RESULT.md supplies the general Fourier decomposition, the degree-\(p\) attaching map and the integral lens cellular boundaries. Neither finite field experiment alone would establish integral torsion or a uniform theorem.

The certificate does not check every prime, and it does not calculate the complete nonabelian homotopy groups or possible hidden cohomology operations. The mathematical claim rests on the explicit mapping-cone homeomorphism and the standard lens-space CW calculation. Independent mathematical audit has not been performed.
