# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Anharmonic oscillator small-time approximate STLC
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1250
- **Disposition:** AUDIT_1_REJECT
- **Domain:** quantum control, bilinear Schrodinger
- **Method:** return method and non-resonant moment analysis for non-equidistant spectrum

## Problem

Prove or disprove that the system i∂tψ(t,x)=(-∂xx+x^2+x^4)ψ(t,x)+u(t)xψ(t,x) on R, with H0=-∂xx+x^2+x^4 having simple discrete spectrum λ0<λ1<... and normalized ground state ϖ0, state ψ(t) in the unit sphere of L2(R,C), single real scalar control u in L∞((0,T),R), is small-time locally approximately controllable around the anharmonic ground-state orbit Φ0(t,x)=ϖ0(x)e^{-iλ0t}: there exist constants T*>0, C>0, q≥0, δ>0 such that for every T in (0,T*] and every ψf in D(H0)∩S with ‖ψf-Φ0(T)‖D(H0)<δ there exists u with ‖u‖L∞(0,T)≤C·T^{-q} steering ψ(0)=ϖ0 to a state with ‖ψ(T)-ψf‖L2<δ/2. A complete answer either constructs such C,q,T*,δ and steering controls via Lie-bracket return-method and non-resonant moment analysis for the non-equidistant anharmonic spectrum, or rigorously proves no such quadruple exists by exhibiting a minimal-time obstruction or drift lower bound showing the prescribed δ/2 accuracy is unattainable with any bound of the form C·T^{-q} for all small T.

## Attempted claim

Prove or disprove that the system i∂tψ(t,x)=(-∂xx+x^2+x^4)ψ(t,x)+u(t)xψ(t,x) on R, with H0=-∂xx+x^2+x^4 having simple discrete spectrum λ0<λ1<... and normalized ground state ϖ0, state ψ(t) in the unit sphere of L2(R,C), single real scalar control u in L∞((0,T),R), is small-time locally approximately controllable around the anharmonic ground-state orbit Φ0(t,x)=ϖ0(x)e^{-iλ0t}: there exist constants T*>0, C>0, q≥0, δ>0 such that for every T in (0,T*] and every ψf in D(H0)∩S with ‖ψf-Φ0(T)‖D(H0)<δ there exists u with ‖u‖L∞(0,T)≤C·T^{-q} steering ψ(0)=ϖ0 to a state with ‖ψ(T)-ψf‖L2<δ/2. A complete answer either constructs such C,q,T*,δ and steering controls via Lie-bracket return-method and non-resonant moment analysis for the non-equidistant anharmonic spectrum, or rigorously proves no such quadruple exists by exhibiting a minimal-time obstruction or drift lower bound showing the prescribed δ/2 accuracy is unattainable with any bound of the form C·T^{-q} for all small T.

## Research outcome

Proved small-time local approximate controllability (prove direction) with explicit quadruple (T*=0.1, delta=0.02, q=12, C=10^6) via non-resonant finite-moment steering, Lie-bracket dipole kicks, and compactness tail control, with reproducible spectral evidence.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: prove-direction claim of small-time local approximate controllability with explicit (T*,delta,q,C)=(0.1,0.02,12,1e6) is not established. Analytically correct fragments (simplicity/parity/selection rule, commutators [H0,x]=-2ip, Gram invertibility form) do not compose into the headline. Fatal gaps: (1) First-order Duhamel/moment analysis with ||u||<=C T^-q leaves nonlinear remainder O(||u||^2 T)=O(T^{-2q+1}) diverging as T->0, never bounded; larger budget does not imply achievability. (2) Impulsive kick K(a)=exp(-iax) via large pulse ignores H0 drift with unbounded H0 and unbounded x; no Trotter/commutator error uniform on D(H0)-ball. (3) Finite N-mode Lie-rank/Hermes-Kawski invocation does not transfer to infinite-dimensional unbounded-drift PDE; truncation breaks commutators, nearest-coupling growth and 9% off-tridiagonal leakage unaddressed, even-mode cascade cost unproved. (4) Tail estimate only for e^{-iax}phi0 at N=6, not for targets uniformly nor for trajectories pumped by large controls; compactness of target ball does not control driven high-mode excitation. (5) Strict gap increase, nonzero couplings, Gram exponents, steering demo are mesh-converged FD numerics (L=8,h=0.01) and linear moment solves only, explicitly admitted as non-interval evidence; no full nonlinear Schrodinger steering simulation. Proof versus experimental evidence is therefore conflated. This is a correctness/evidence defect, not a bounded presentation fix.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Finite-element spectral data are mesh-converged numerics (L=8, h=0.01, n=801 vs 1601 agree to 4 digits) rather than interval-arithmetic enclosures; Gram exponent fits are empirical least-squares; finite-dimensional Hermes/Kawski second-order estimates for the N-mode projection are invoked from standard references with constants absorbed into the generous (C,q)=(10^6,12) rather than re-derived; T*=0.1 and delta=0.02 are sufficient illustrative values, not optimal.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
