# Self-review

## Correctness — PASS
The exact two-stage spherical-exponential formulas and the midpoint/double-extrapolation identities give closed one-step height maps. Symbolic sixth-order expansions, a uniform Taylor remainder, and an axisymmetry-induced scalar recurrence establish the global third-order coefficients and the fifth-order exceptional latitude. The standalone `verify.py` actually passed the stated algebraic and high-precision numerical checks. Numerical tests corroborate, rather than prove, the limits. The theorem concerns the height observable, not a higher global state order.

## Originality — PASS (qualified)
The 2026 source (Sect. 3.2) defines SRKRE\([1,2]\) and gives convergence/order analysis; the 2024 source (Sects. 3.1–3.5) defines STVDRK2 and discusses rigid rotation but not the two height-error coefficients, their sign boundary, sharp envelope or exceptional ring. Actual searches for SRKRE latitude drift, rigid-axis precession, spherical extrapolation and first integrals in mathematical research records found only distinct planar randomized rotations and unrelated spherical problems. Accessible historical claims of this slot had no matching height theorem. General geometric integration literature may have an equivalent modified-equation formulation, and that remains a priority risk; absence of search hits alone is not a uniqueness proof.

## Value — PASS
The axial height is a natural conserved first integral for the simplest non-geodesic sphere ODE. Its leading error is invisible to sphere-membership and ordinary state-order guarantees. The exact sign bifurcation and a latitude where one second-order method gains two further height orders distinguish two concrete algorithms and provide a diagnostic for preserving dynamics of spin/precession problems.

## Closest literature and scientific limits
- Lee–Leung (2026): spherical extrapolation definition and geometric/state-order guarantees, not a drift-sign theorem. https://link.springer.com/article/10.1007/s10915-026-03318-4
- Leung–Chau–Lee (2024): original SFE/STVDRK2 and rigid rotation as a test class, not the claimed comparative latitude asymptotics. https://link.springer.com/article/10.1007/s10915-024-02702-2
The claim is restricted to constant-speed rigid-axis rotation, sufficiently small h, and one fixed time horizon. Historical priority remains open to less obvious equivalent analyses.

Self-review: passed. Independent audit: not yet performed.
