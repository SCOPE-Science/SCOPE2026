---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

On Hermitian matrices, i[H,X] is skew with respect to real Hilbert–Schmidt pairing, so homogeneous response energy forces boundary diagonals and every off-diagonal zero; bond equations then force all diagonals zero, establishing invertibility. Diagonal equations yield conserved j and X_11=1/2−j/Γ, X_NN=−1/2+j/Γ. Pairing with X yields source Γ/2−j and dissipative energy 2Γ(1/2−j/Γ)^2+[γ(N−1)+Γ]j²/(2t²)+E; rearrangement gives j(1−j/j0)=E≥0. j=0 contradicts source boundary values and zero coherences. E=0 kills real nearest-neighbor and all longer coherences; real bond equations then force v_k−v_{k+1}=0. A directly constructed constant-potential response attains equality. Independently solved N=3, t=Γ=γ=1, v=(0,1,2): j=6/25,j0=2/7,E=24/625. Entire check code inspected; all-N proof is the dissipative identity, not finite tests.

## originality

PASS

PASS best-of-knowledge: Jacob et al. 2024 primary full article on exactly boundary-driven tilted XX chain reports exact n=2,3 currents and approximate tridiagonal construction for longer chains, not the arbitrary-N rigorous current ceiling at same dephasing, with exact nonnegative excess coherence certificate and equality iff constant onsite potential. Žnidarič–Horvat 2012 provides general covariance equations and disorder context; Žnidarič 2010 supplies clean-chain benchmark. Those premises alone do not make the specific sharp global energy identity a previously stated result, though their combination could be a prior implication specialist concern.

## value

PASS

An all-size sharp exclusion of tilt-enhanced current at fixed dephasing settles a natural nonperturbative transport comparison beyond short-chain formulas and uncontrolled coherence truncations. Its exact excess-coherence identity quantitatively identifies the obstruction and supplies equality characterization for every onsite profile; relates to noise-assisted transport without falsely asserting monotonicity in dephasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
