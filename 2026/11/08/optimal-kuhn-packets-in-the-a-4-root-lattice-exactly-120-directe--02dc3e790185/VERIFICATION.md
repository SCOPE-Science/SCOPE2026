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
# Verification of the \(A_4\) packet theorem

**Analytic checks.** The zero-sum, integral-coordinate normalization is explicit. Root inequalities exactly determine the nearest-lattice-point cell because \(z_i^2\ge |z_i|\) for every integer coordinate. The only Voronoi vertices have two coordinate levels, giving the squared covering-radius maximum \(6/5\). Every directed path packet has binary-shift witnesses and a rational exact squared-radius formula. The converse uses the published common-packet implication from Xue [1], and the optimal-frame characterization uses an integral subset-sum diameter bound with no asymptotic or numerical step.

**Reproducible finite checks.** Run `python3 verify_a4.py`. The script enumerates 50 short vectors, tests 230300 unordered candidate frames, finds exactly 120 surviving independent frames, verifies that all are directed paths and lattice bases, and checks 2880 exact integer sphere identities. It emits the marker `A4_PACKET_EXACT_OK` on success. The empirical enumeration independently corroborates rather than replaces the proof.

**Boundaries.** The script does not certify the published general \(\mu\le\kappa\) theorem, historical priority, or any other lattice. These are respectively cited established theory, a literature-comparison question, and outside the claim. Independent audit: not performed.
