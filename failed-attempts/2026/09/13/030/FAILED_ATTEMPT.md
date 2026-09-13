# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Multiplicity-three flop functors and spherical cotwist
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1530
- **Disposition:** AUDIT_2_REJECT
- **Domain:** algebraic geometry, derived categories of threefolds
- **Method:** fibre-product Fourier-Mukai functors, null-category spherical functor

## Problem

Let f: X -> Y and f+: X+ -> Y be flopping contractions of quasi-projective Gorenstein Calabi-Yau threefolds with fibres of dimension at most one over an affine base Y with isolated canonical hypersurface singularity of multiplicity exactly 3 (hence outside the Bodzenta-Bondal multiplicity-two hypothesis), and let F = R(p+)_* L(p)^*: Perf(X) -> Perf(X+), F+ = R(p)_* L(p+)^*: Perf(X+) -> Perf(X) be the fibre-product Fourier-Mukai functors via W = X x_Y X+. Let A_f be the null category of f, let Psi: D -> Perf(X) be the Bodzenta-Bondal derived null-category spherical functor with cotwist kernel K_C in Perf(X x X) and cotwist C = FM_{K_C}. Settle by proof or rigorous disproof: are F and F+ mutually inverse equivalences on perfect complexes, and is F+ \circ F isomorphic to the inverse spherical cotwist C^{-1} as Fourier-Mukai functors on Perf(X)? A complete answer proves both the equivalence and the kernel identity K_{F+\circ F} \simeq K_C^{-1} in Perf(X x X), or gives a rigorous counterexample with an explicit perfect complex where equivalence or the cotwist identity fails.

## Attempted claim

Let f: X -> Y and f+: X+ -> Y be flopping contractions of quasi-projective Gorenstein Calabi-Yau threefolds with fibres of dimension at most one over an affine base Y with isolated canonical hypersurface singularity of multiplicity exactly 3 (hence outside the Bodzenta-Bondal multiplicity-two hypothesis), and let F = R(p+)_* L(p)^*: Perf(X) -> Perf(X+), F+ = R(p)_* L(p+)^*: Perf(X+) -> Perf(X) be the fibre-product Fourier-Mukai functors via W = X x_Y X+. Let A_f be the null category of f, let Psi: D -> Perf(X) be the Bodzenta-Bondal derived null-category spherical functor with cotwist kernel K_C in Perf(X x X) and cotwist C = FM_{K_C}. Settle by proof or rigorous disproof: are F and F+ mutually inverse equivalences on perfect complexes, and is F+ \circ F isomorphic to the inverse spherical cotwist C^{-1} as Fourier-Mukai functors on Perf(X)? A complete answer proves both the equivalence and the kernel identity K_{F+\circ F} \simeq K_C^{-1} in Perf(X x X), or gives a rigorous counterexample with an explicit perfect complex where equivalence or the cotwist identity fails.

## Research outcome

Proved the multiplicity-3 flop setup is impossible: a terminal crepant flop forces an isolated cDV multiplicity-2 base, so both target statements hold vacuously with no counterexample possible.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: TARGET hypothesis class is empty by standard Reid classification, so both 'equivalence' and 'kernel identity K_{F+oF}~=K_C^{-1}' hold only vacuously with no perfect complex, no kernel computation, and no extension of Bodzenta-Bondal. STANDARD requires Admission to rule out vacuity, type errors, tiny-instance mismatches and arbitrary parameter facts with both outcomes independently valuable; admitting mult-exactly-3 slice outside mult-2 hypothesis without checking Reid cDV-mult-2 was that mistake. Sharpness Fermat cubic strictly-canonical base is textbook. Vacuous truth over empty class plus standard-base existence does not advance recognized question, boundary, or downstream use; future researcher needs Reid itself, not this repackaging. Intrinsic empty-scope low value, not repairable by bounded addition.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The resolution is by impossibility (vacuous truth over an empty hypothesis class) rather than by extending the Bodzenta-Bondal equivalence and cotwist identity to singular or strictly canonical flops; it relies on Reid's Gorenstein terminal = isolated cDV classification and standard discrepancy calculus (Kollar-Mori) as cited background, and does not construct or classify flops of strictly canonical threefolds, for which the functors F, F+ and spherical functor Psi are not addressed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
