# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A superpotential-value witness separating a Vianna-type monotone torus from Clifford in monotone dP2
- **Round:** 2026-09-07-first-light-01
- **Lane:** 368
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Symplectic Topology
- **Method:** Lagrangian Floer cohomology with Landau-Ginzburg superpotential wall-crossing and almost-toric mutation invariance

## Problem

Is a specified Vianna-type monotone mutation fibre L_mut in the monotone del Pezzo surface dP2 (CP2 blown up at 2 points; dP3 as fallback) Hamiltonian isotopic to the standard Clifford torus L_Cliff? Attack via the Landau-Ginzburg disk superpotential: compute the mutation-period superpotential truncation for L_mut and test whether its Newton polytope / critical-value set differs from that of L_Cliff, yielding a Floer-theoretic isotopy obstruction.

## Attempted claim

The explicitly specified one-step Vianna-type mutation fibre L_mut in monotone dP2 is not Hamiltonian isotopic to the Clifford torus L_Cliff: its Landau-Ginzburg disk superpotential W(L_mut) has a Newton polytope (equivalently, a critical-value set detectable with a suitable rank-one local system) distinct from W(L_Cliff), so Lagrangian Floer cohomology with that local system distinguishes the two tori.

## Research outcome

Fallback-grade CLAIMED result per admission fallback (a)+(c): a transferable one-wall LG mutation-invariance lemma plus exactly computed truncated superpotentials for the monotone dP2 (primary) and dP3 Clifford fibres, with one new certified Maslov-2 coefficient (2 at class (1,1)) and a proved Newton-polytope vertex-count separation (5v4 dP2; 6v5 dP3), all replayed by a stdlib verifier (VERIFY_OK). Geometric isotopy consequence stated only conditionally on cited wall-crossing theorems.

## Why this attempt failed

Failed axes: originality, value.

originality: No substantive delta over Pascaleff-Tonkonog 1711.03209 (plus Cho-Oh/Vianna). The 'transferable one-wall lemma' W0=C0+y(1+x)+y^-1(1+x^-1) -> W1=C0+y~(1+x)^2+1/(x y~) is the direct special case of PT Theorem 1.2 / Theorem 4.8 / Theorem 4.20 general wall-crossing (WL'=mu_[dD]^perp WL) for del Pezzo mutation configurations. The toric inputs W0 are the standard Cho-Oh Hori-Vafa sums; for Bl2 the draft's W0 is GL-equivalent to PT Table 1 Bl2 potential (1+x+y)(1+1/(xy))-1 (checked: supports {(1,0),(0,1),(-1,0),(0,-1),(-1,-1)} vs {(1,0),(1,1),(0,1),(-1,-1),(0,-1)} mapped by GL matrices found by brute force), so the input was published. The output W1 follows by one substitution plus (1+x)^2=1+2x+x^2 and an elementary hull count. PT already proves the stronger geometric statement the topic calls open: Corollary 4.28 proves every monotone del Pezzo including Bl2 (=dP2, two-point blow-up) contains infinitely many pairwise non-Hamiltonian-isotopic monotone tori, using Theorem 4.25 (all Table 1 potentials realised) plus wall-crossing; Vianna 1602.03356's exclusion of Bl1/Bl2 is thus closed by PT 2018. A verbatim-printed '5 vs 4' for this one wall was not found, but a 3-line instantiation of a published general formula plus binomial theorem is a mere parameter substitution, not a new claim; failed-search/timestamp does not establish priority. value: Even taken as fallback-grade exact datum, the record is a textbook instantiation with no independent retrieval need. Given PT's general mutation formula and the toric W0, any researcher can produce W1, coefficient 2, and 5-vs-4 / 6-vs-5 hull counts in minutes; it is mechanically implied, failing the 'not known or mechanically implied' test for narrow exact invariants. Geometrically, PT Corollary 4.28 already separates infinitely many tori in Bl2/dP2, so a conditional one-step Clifford-vs-mutant vertex-count distinction adds no rigidity-boundary movement, no demonstrated mirror-matching/displaceability use, and no general criterion. This is exactly the excluded category: mere parameter substitution of a general wall-crossing formula plus binomial/hull exercise, with VERIFY_OK certification alone not rescuing it. Narrowness per se is not the reason; lack of non-mechanical content and downstream need is.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Algebraic-combinatorial certificate only: proves the lemma, the exact mutated potentials, coefficient 2, and polytope inequivalence. Does not re-prove cited analytic inputs (Cho-Oh divisor potential; Pascaleff-Tonkonog wall-crossing; existence/monotonicity of the mutated ATF fibre; FOOO isotopy invariance).', 'No explicit ATBD nodal-trade diagram with coordinates is constructed; the target fibre is specified intrinsically as the one-step monotone mutation across the wall 1+x in direction (0,1…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
