# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Elliptic-wall emptiness for the excess locus h0>=6 in the rank-2 cell v=(2,H,2) on a BN-general genus-8 K3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 619
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Geometry
- **Method:** Bridgeland wall-crossing stability analysis with Mukai-lattice computation and Fourier-Mukai comparison

## Problem

Let (X,H) be a BN-general polarized K3 surface of genus 8 (H^2=14) carrying a maximal elliptic pencil E with E^2=0 and E.H=5. For Mukai vector v=(2,H,2) (v^2=6, dim M_H(v)=8, chi=4, c2=7), decide the excess Brill-Noether locus with h^0>=6 (expected BN dimension -4): prove the Bridgeland wall W induced by the elliptic spherical class a=(1,E,1) is actual and every object of class v with h^0>=6 is destabilized along W with factors a and b=v-a=(1,H-E,1), forcing h^0<=5 on the Gieseker-stable side, so no mu_H-stable BN bundle with h^0>=6 exists.

## Attempted claim

For BN-general polarized K3 (X,H) of genus 8 with maximal elliptic pencil E (E^2=0, E.H=5), the Gieseker moduli space M_H(v) with v=(2,H,2) contains no mu_H-stable bundle with h^0>=6: the elliptic Bridgeland wall W induced by a=(1,E,1) is a genuine wall for class v, every object of class v with h^0>=6 is strictly semistable along W with Jordan-Holder factors of classes a and b=(1,H-E,1), and the factor cohomology forces h^0<=5 for any Gieseker-stable object, certifying a sharp empty-chamber obstruction at expected BN dimension -4.

## Research outcome

Target blocked (slope 5<7 wrong way; chi(E(-E))=-1 no forcing; uniform fibre bound refuted by explicit elliptic h0=6 model; wall numerical but occupancy unproven; factor H0 sum 2+4=6). Preset fallback attempted on both horns and blocked: vanishing horn needs unproven h1(O(H-E))=0 and is proved off-by-one insufficient even if granted (2+4=6 compatible with h0>=6); counterexample horn reduces to the open excess-existence problem. No independently valuable original increment. CLEAN_EXIT with target_exit.json and replay scripts.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No access to explicit equations of a BN-general genus-8 K3 with maximal E.H=5 pencil; all checks are lattice/cohomology arithmetic plus one classical fibre model.', 'BN-generality used only via standard consequences (Picard control unavailable); negative-curve classification needed for |H-E| nefness/base-freeness was out of bounded scope.', 'Sigma-semistability occupancy at the numerical wall t0^2=1/7 not established; sheaf-level Ext^1>=3 does not supply it.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No access to explicit equations of a BN-general genus-8 K3 with maximal E.H=5 pencil; all checks are lattice/cohomology arithmetic plus one classical fibre model.', 'BN-generality used only via standard consequences (Picard control unavailable); negative-curve classification needed for |H-E| nefness/base-freeness was out of bounded scope.', 'Sigma-semistability occupancy at the numerical wall t0^2=1/7 not established; sheaf-level Ext^1>=3 does not supply it.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
