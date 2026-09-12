# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Two-term free-energy expansion for the two-periodic Aztec diamond
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1241
- **Disposition:** AUDIT_2_REJECT
- **Domain:** dimer free energy / partition function asymptotics
- **Method:** Kasteleyn-Pfaffian asymptotics and steepest descent with surface tension

## Problem

Let Z_n(a) be the dimer partition function (weighted sum over domino tilings, equal up to sign by a linear combination of four Kasteleyn Pfaffians) of the order-n Aztec diamond with fixed 2-periodic weights (1,a), 0<a<1 fixed. Prove or disprove that (1/n^2)*log Z_n(a) = F0(a) + F1(a)/n + o(1/n) as n->infinity, where F0(a) is the explicit surface-tension integral (Ronkin-type functional of the 2-periodic spectral curve integrated over the rescaled diamond) and F1(a) is an explicit boundary constant determined by the arctic-curve and frozen-region data, with both constants given in closed form in terms of a. A complete answer is a rigorous derivation of this two-term expansion with identified F0,F1 via Kasteleyn-Pfaffian asymptotics and steepest descent, or a rigorous disproof showing no such expansion holds (e.g. a different second-order coefficient, oscillation, or logarithmic correction).

## Attempted claim

Let Z_n(a) be the dimer partition function (weighted sum over domino tilings, equal up to sign by a linear combination of four Kasteleyn Pfaffians) of the order-n Aztec diamond with fixed 2-periodic weights (1,a), 0<a<1 fixed. Prove or disprove that (1/n^2)*log Z_n(a) = F0(a) + F1(a)/n + o(1/n) as n->infinity, where F0(a) is the explicit surface-tension integral (Ronkin-type functional of the 2-periodic spectral curve integrated over the rescaled diamond) and F1(a) is an explicit boundary constant determined by the arctic-curve and frozen-region data, with both constants given in closed form in terms of a. A complete answer is a rigorous derivation of this two-term expansion with identified F0,F1 via Kasteleyn-Pfaffian asymptotics and steepest descent, or a rigorous disproof showing no such expansion holds (e.g. a different second-order coefficient, oscillation, or logarithmic correction).

## Research outcome

Repaired submission: corrected Lemma 2/(star) to cross-face Delta p^2+q^2, general-m local shuffle proofs with counting and surgery accounting, symbolic T^2 closure plus homogeneity justification, and explicit scoping of F0/F1 to closed-form constants with the a=1 check; all verification scripts retained.

## Why this attempt failed

Failed axes: originality.

originality: TERMINAL UPDATE: the paid final check returned a decisive prior that substantively covers the headline. Robert-Ruelle, GUE-corners process in two-periodic Aztec diamonds (arXiv:2509.14071, v1 17 Sep 2025, v2 1 Sep 2026), Proposition 3.2 / equation (3.26), states exactly Zn=(2ab)^{floor((n+1)^2/4)}(a^2+b^2)^{floor(n^2/4)} times (1 if n!=1 mod 4, a/b if n=1 mod 4) for the two-periodic Aztec diamond with face weights a,b, and notes it was already computed via the octahedron recurrence (Di Francesco-Soto-Garrido 2014, ref [24]) and lambda-determinants (ref [29]). The primary source was verified in full (HTML v2, Sections 3.1-3.2, eqs. (3.24)-(3.26) plus GGI-slide corroboration). Under the specialization b=1 this formula is algebraically and numerically identical to the submitted closed form: auditor verified zero difference (to ~1e-15) for n=0..15, with F0=(1/4)ln(2a(1+a^2)) and F1=(1/2)ln(2a) matching as the n^2 and n coefficients and the C_{n mod 4} pattern (including the n=1 mod 4 a/b factor matching C_1=F1-F0+ln a) coinciding. The weight conventions coincide up to the stated specialization (checkerboard face weights (a,b) vs (1,a) with b=1; both give face-uniform edge weights and identical partition numbers, confirmed by determinant agreement). Hence the submitted exact finite-n identity, and therefore its F0/F1/K_n/C_r consequences, is a strict special case (b=1) of a broader prior theorem published before this audit, and is substantively implied without needing the submitted wording. A new domino-shuffle proof does not make the known formula a new mathematical claim under the shared STANDARD. Originality therefore FAILS; correctness and value are unchanged per the terminal-gate rule.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: F0 is not separately derived as the Ronkin surface-tension integral nor F1 as the arctic-curve boundary constant; the theorem is explicitly scoped to closed-form free-energy constants (a=1 EKLP check included). The shuffle face-regrouping local analysis is supplemented by computational face-census/isomorphism verification on small sizes.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
