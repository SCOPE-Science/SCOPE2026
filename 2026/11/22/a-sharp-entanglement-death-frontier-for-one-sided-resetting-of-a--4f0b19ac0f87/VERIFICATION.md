---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the full-space stationary-state argument. Writing the state entries as A,B,T,w,z as in RESULT.md, the reset transfers the two lower diagonal entries T to the corresponding upper positions and damps w,z. In the two parity blocks the off-diagonal equations are (r+4ih)w=iJ(A−T) and rz=iJ(B−T); both population balances use 2J Im(w)=2J Im(z)=rT. The proposed entries satisfy these identities and trace one. The two reordered block determinants are J²(r²+4J²+16h²)/(4Q²) and J²(r²+4J²)/(4Q²), hence faithfulness. The adjoint fixed-point dissipation identity then forces commutation with the local reset matrix units and their adjoints, so a fixed point must be I⊗G. Commutation with H requires [X,G]=[Z,G]=0 because J,h>0; this proves full-kernel uniqueness, not merely uniqueness within X-states. The standard spin-flip branches give |z|²−AT<0 and |w|²−BT=J²(16h²−4J²−r²)/(4Q²); equality is PPT/separable. Thus the normalized concurrence and the strictly positive-rate boundary are correct. The r=0 generator is excluded. The bundled checker and VERIFICATION.md were inspected but not executed; validation here is algebraic.

## originality

PASS

The closest matched one-sided classification uses an inequivalent reset axis. Full-system reset concurrence and general open-system methods do not give this stationary phase boundary. The positive-field, positive-rate classification survives the bounded comparison; this is not a priority assertion.

## value

PASS

The reset orientation is a physically and mathematically motivated distinction, not a parameter relabeling. The exact field threshold, rate threshold and equality case turn the contrast with stationary separability under aligned one-sided resetting into a usable quantitative classification. Full-space uniqueness rules out attributing the effect to a chosen initial parity sector.

The dated certificate retains the supplied scientific assessment, sources and limitations.
