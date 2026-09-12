# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Circle dipole STLC with doubled spectrum
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1249
- **Disposition:** AUDIT_1_REJECT
- **Domain:** quantum control, bilinear Schrodinger
- **Method:** return method with degenerate Fourier analysis, quadratic and cubic Lie brackets

## Problem

Prove or disprove that the system i∂tψ(t,θ)=-∂θθψ(t,θ)+u(t)cosθψ(t,θ) on the circle S1=R/(2πZ) with periodic boundary conditions, state ψ(t) in the unit sphere of L2(S1,C), single real scalar control u in L∞((0,T),R), is small-time locally exactly controllable around the constant ground-state orbit Φ0(t)=(2π)^{-1/2}e^{-i0t}: there exist constants T*>0, C>0, q≥0, s=3, δ>0 such that for every T in (0,T*] and every ψf in H3(S1,C)∩S with ‖ψf-Φ0(T)‖H3<δ there exists u with ‖u‖L∞(0,T)≤C·T^{-q} steering ψ(0)=(2π)^{-1/2} exactly to ψ(T)=ψf. A complete answer either constructs such C,q,T*,δ and steering controls via a Lie-bracket return-method trajectory handling the doubly degenerate Fourier spectrum, or rigorously proves no such quadruple exists by exhibiting a conserved-quantity, resonance, or quadratic/cubic drift obstruction valid for all bounded small-time controls.

## Attempted claim

Prove or disprove that the system i∂tψ(t,θ)=-∂θθψ(t,θ)+u(t)cosθψ(t,θ) on the circle S1=R/(2πZ) with periodic boundary conditions, state ψ(t) in the unit sphere of L2(S1,C), single real scalar control u in L∞((0,T),R), is small-time locally exactly controllable around the constant ground-state orbit Φ0(t)=(2π)^{-1/2}e^{-i0t}: there exist constants T*>0, C>0, q≥0, s=3, δ>0 such that for every T in (0,T*] and every ψf in H3(S1,C)∩S with ‖ψf-Φ0(T)‖H3<δ there exists u with ‖u‖L∞(0,T)≤C·T^{-q} steering ψ(0)=(2π)^{-1/2} exactly to ψ(T)=ψf. A complete answer either constructs such C,q,T*,δ and steering controls via a Lie-bracket return-method trajectory handling the doubly degenerate Fourier spectrum, or rigorously proves no such quadruple exists by exhibiting a conserved-quantity, resonance, or quadratic/cubic drift obstruction valid for all bounded small-time controls.

## Research outcome

Disproved circle-dipole STLC: parity (evenness) is conserved by cos control, so non-even H3-nearby targets are unreachable at any time.

## Why this attempt failed

Failed axes: originality.

originality: REVISED AFTER TERMINAL CHECK: decisive prior found. Boscain-Caponigro-Chambrion-Sigalotti arXiv:1101.4313v4 (verified in full) studies the same S1 system i psi_t=(-d^2+u1 cos+u2 sin)psi and explicitly records that fixing one control to zero leaves a single-cos system that is not controllable by parity: cos does not couple odd with even wave functions. Section 8 formalizes H=H^alpha_e(+)H^alpha_o with cos/sin bases and Lemma 8.1 preserving even/odd L2 norms under the restricted single-direction control, i.e. the same even-subspace invariant from the constant ground state. That globally (approximately) non-controllable parity obstruction substantively implies the submitted H3-local STLC failure; the normalized sine family psi_{f,eps} at H3-distance O(eps) with odd-part eps/sqrt(1+eps^2)>0 is then a routine corollary/repackaging of the known stronger fact, not a new boundary. Originality therefore FAILS.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: This disproof targets exact reachability in the full H3-intersect-sphere neighborhood; it leaves open controllability restricted to the even subspace E, and does not analyze linearized, quadratic/cubic Lie-bracket, return-method, or large-time questions. Well-posedness/unitarity for the bounded cos perturbation is invoked via standard Dyson/monotone theory rather than re-proved from scratch.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
