# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Punctured-torus Hitchin vs symmetrized-Fuchsian cuff domination
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1553
- **Disposition:** NO_RESULT
- **Domain:** higher Teichmuller theory
- **Method:** Fock-Goncharov monodromy weight matrices and positivity

## Problem

Let S be the once-punctured torus, with presentation pi1(S)=<a,b | [a,b] peripheral>. Consider the set R of conjugacy classes of positive (cusped Hitchin) representations rho: pi1(S)->PSL(3,R) with unipotent peripheral holonomy, parametrized by Fock-Goncharov positivity coordinates on a fixed ideal triangulation (two edge shears s1,s2 in R and one triangle invariant t>0, all edge cross-ratios and triple ratios >0). For loxodromic g let Hilbert length be H_rho(g)=log(|lambda1(rho(g))/lambda3(rho(g))|) with eigenvalues ordered by modulus, and Labourie cross-ratio defined from the associated Frenet flag map. Fix the intersecting cuff pair (a,b) with geometric intersection number one. Define the Fuchsian symmetrization rho_F of rho by setting t=1 and replacing each shear by its symmetrized absolute value per the standard 3-Fuchsian locus embedding, keeping the cusp unipotent. Decide the domination inequality: is H_rho(a) >= H_{rho_F}(a) AND H_rho(b) >= H_{rho_F}(b) for every rho in R, provable via Fock-Goncharov monodromy trace polynomials with positivity plus cross-ratio identities? Scope is all s1,s2 in R and all t>0. A complete answer is either a rigorous proof of both inequalities over all of R, or one explicit positive coordinate tuple (s1,s2,t) with rigorously computed flag matrices, eigenvalues and Hilbert lengths violating at least one of the two inequalities.

## Attempted claim

Let S be the once-punctured torus, with presentation pi1(S)=<a,b | [a,b] peripheral>. Consider the set R of conjugacy classes of positive (cusped Hitchin) representations rho: pi1(S)->PSL(3,R) with unipotent peripheral holonomy, parametrized by Fock-Goncharov positivity coordinates on a fixed ideal triangulation (two edge shears s1,s2 in R and one triangle invariant t>0, all edge cross-ratios and triple ratios >0). For loxodromic g let Hilbert length be H_rho(g)=log(|lambda1(rho(g))/lambda3(rho(g))|) with eigenvalues ordered by modulus, and Labourie cross-ratio defined from the associated Frenet flag map. Fix the intersecting cuff pair (a,b) with geometric intersection number one. Define the Fuchsian symmetrization rho_F of rho by setting t=1 and replacing each shear by its symmetrized absolute value per the standard 3-Fuchsian locus embedding, keeping the cusp unipotent. Decide the domination inequality: is H_rho(a) >= H_{rho_F}(a) AND H_rho(b) >= H_{rho_F}(b) for every rho in R, provable via Fock-Goncharov monodromy trace polynomials with positivity plus cross-ratio identities? Scope is all s1,s2 in R and all t>0. A complete answer is either a rigorous proof of both inequalities over all of R, or one explicit positive coordinate tuple (s1,s2,t) with rigorously computed flag matrices, eigenvalues and Hilbert lengths violating at least one of the two inequalities.

## Research outcome

Target blocked: universal Hilbert-domination over the cusped positive once-punctured torus locus was neither proved nor disproved. Attempted routes were (1) fixed-A linear intertwiner kernel analysis showing singular-only kernels, (2) generic-A determinant obstruction, and (3) Fock-Goncharov snake-matrix grid evaluation far from the unipotent locus; matching CLEAN_EXIT recorded in output/target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No unipotent-cusped positive point was solved: the snake-matrix grid gave commutator traces 131-2441 versus required 3, scipy was unavailable for the nonlinear cusp solve, and no rigorous eigenvalue or Hilbert-length certificate was produced. The linear intertwiner analysis is a negative scoping fact only. Any future attempt needs a custom certified nonlinear solver plus interval eigenvalue bounds.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No unipotent-cusped positive point was solved: the snake-matrix grid gave commutator traces 131-2441 versus required 3, scipy was unavailable for the nonlinear cusp solve, and no rigorous eigenvalue or Hilbert-length certificate was produced. The linear intertwiner analysis is a negative scoping fact only. Any future attempt needs a custom certified nonlinear solver plus interval eigenvalue bounds.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
