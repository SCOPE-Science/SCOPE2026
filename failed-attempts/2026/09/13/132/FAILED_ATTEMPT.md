# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Nontrivial resonance certificate for named nonlinear Anosov H_star
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1780
- **Disposition:** NO_RESULT
- **Domain:** hyperbolic dynamics
- **Method:** dynamical determinant periodic-orbit certificate and anisotropic spectrum

## Problem

Let A_d be the toral automorphism of T^3 induced by [[4,1,0],[1,1,1],[0,1,1]] (determinant -1, eigenvalue moduli approximately 4.330-analogue 0.128/1.798/4.330 family, one stable and two unstable directions) and R(x1,x2,x3) = (x1 + 0.02*sin(2*pi*(x2+x3)), x2 + 0.02*sin(2*pi*x3), x3) mod 1, triangular hence Lebesgue-preserving. Let H_star = A_d o R, real-analytic volume-preserving Anosov with dim E^s = 1, dim E^u = 2, nonlinear and distinct from any linear automorphism. Prove or disprove that the transfer operator (Q g)(x) = g(H_star^{-1}(x)) on an anisotropic space has a nontrivial Ruelle resonance lambda1 != 1 with |lambda1| >= 0.6, equivalently there exist explicit non-constant real-analytic observables phi,psi and c > 0 with |int phi*(psi o H_star^n) dm - int phi dm int psi dm| >= c*(0.6)^n for infinitely many n >= 0, certified by an explicit zero of the dynamical determinant from periodic data up to period 4. A complete answer exhibits the resonant mode and correlation lower bound with periodic-orbit certificate, or rigorously proves the disc {|lambda| >= 0.6} minus {1} is resonance-free for H_star, i.e. optimality/refutation with full determinant plus spectral enclosure proofs.

## Attempted claim

Let A_d be the toral automorphism of T^3 induced by [[4,1,0],[1,1,1],[0,1,1]] (determinant -1, eigenvalue moduli approximately 4.330-analogue 0.128/1.798/4.330 family, one stable and two unstable directions) and R(x1,x2,x3) = (x1 + 0.02*sin(2*pi*(x2+x3)), x2 + 0.02*sin(2*pi*x3), x3) mod 1, triangular hence Lebesgue-preserving. Let H_star = A_d o R, real-analytic volume-preserving Anosov with dim E^s = 1, dim E^u = 2, nonlinear and distinct from any linear automorphism. Prove or disprove that the transfer operator (Q g)(x) = g(H_star^{-1}(x)) on an anisotropic space has a nontrivial Ruelle resonance lambda1 != 1 with |lambda1| >= 0.6, equivalently there exist explicit non-constant real-analytic observables phi,psi and c > 0 with |int phi*(psi o H_star^n) dm - int phi dm int psi dm| >= c*(0.6)^n for infinitely many n >= 0, certified by an explicit zero of the dynamical determinant from periodic data up to period 4. A complete answer exhibits the resonant mode and correlation lower bound with periodic-orbit certificate, or rigorously proves the disc {|lambda| >= 0.6} minus {1} is resonance-free for H_star, i.e. optimality/refutation with full determinant plus spectral enclosure proofs.

## Research outcome

Target blocked: bounded probes (period 1-2 orbit weights ≈1, Fourier subdominant values ~1e-3, correlation decay ratio ~6e-5) suggest fast mixing but cannot certify either a ≥0.6 resonance or a resonance-free disc; clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certificate was produced in either direction: periodic-orbit data stop at periods 1-2, Fourier sections leak without spectral enclosure, and Monte Carlo decay covers only one observable pair. A complete answer still needs interval-certified period-≤4 orbits, Bessel-tail bounds, and a verified anisotropic resolvent estimate.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certificate was produced in either direction: periodic-orbit data stop at periods 1-2, Fourier sections leak without spectral enclosure, and Monte Carlo decay covers only one observable pair. A complete answer still needs interval-certified period-≤4 orbits, Bessel-tail bounds, and a verified anisotropic resolvent estimate.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
