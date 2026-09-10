# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Twisted sum-product dichotomy for order-one definable sets in characteristic-zero Frobenius difference ultraproducts
- **Round:** 2026-09-07-first-light-01
- **Lane:** 529
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Mathematical Logic
- **Method:** geometric stability theory: ultraproduct transfer, group configuration, and distal regularity decomposition

## Problem

Transfer a twisted sum-product/expansion dichotomy to the characteristic-zero pseudofinite difference class (K,sigma)=prod_U (F_{p_n^{l_n}},Frob_{p_n}) with p_n->infinity: show that for a bounded-complexity difference-formula class, small twisted sum-product forces a group configuration over Fix(sigma) (subfield or 1-dim algebraic group coset), or isolate the definable obstruction where the transfer fails.

## Attempted claim

Let p_n be distinct primes ->infinity, l_n->infinity, K_n=(F_{p_n^{l_n}},sigma_n=Frob_{p_n}), (K,sigma)=prod_U K_n, and Phi_D the class of one-variable difference formulas of total degree <=D and sigma-order <=1. Then there exist eps(D)>0 and eta(D)>0 such that for U-almost-all n, every A_n subset K_n uniformly defined by Phi_D with |K_n|^delta<=|A_n|<=|K_n|^{1-delta} satisfies: either |A_n+A_n|+|A_n*sigma_n(A_n)|>=|A_n|^{1+eps(D)}, or A_n is eta-commensurable with a proper difference subfield or a coset of a one-dimensional Fix(sigma_n)-definable algebraic group (i.e. |A_n cap (c+G)|>=|A_n|^{1-eta} for some such c+G).

## Research outcome

Target general-D dichotomy not proved (stabilizer route blocked by SOP/TP2 wildness + ring-degree obstruction, documented). Fallback exact exponents not proved (no viable closing route). Claimed instead a proved emergent lemma: qf order<=1 definable sets are O(p_n) or co-O(p_n), hence eventually vacate any fixed intermediate window, forcing the quantified case; plus exact horn-necessity identities pinning the two-term growth shape. Replay VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: Fails independent-retrieval standard despite correctness and narrow novelty. (a)-(b) is a textbook restatement: injectivity (p>D) + Schwartz-Zippel degree bound + DNF union bound + elementary asymptotics B_n=O(p_n) vs q_n=p_n^{l_n}. DRAFT itself concedes ingredients standard. The Dp bound is mechanically implied by deg F(X,X^p) (exactly the 'trivial upper bound' noted in Hrushovski/Hils), and window vacuity is the finitary restatement of the known 0/1-dimensional phenomenon for one-variable qf sets (Zou integer-valued coarse dimension). It proves no growth exponents, no dichotomy, and by its own limitation says nothing about quantified formulas where the target/fallback live; it is a negative vacuity observation, not a reusable bridge lemma with growth-vs-structure content. (c) horn identities are immediate subgroup closures (norm-1 torus multiplicative subgroup, trace kernel additive subgroup, plus Galois invariance); certification of T.sig(T)=T and V+V=V does not establish formal horn-necessity for the exact target (T,V are order-(l-1) definable, not bounded order-1, and for fixed delta eventually |T|,|V|~q/p exceed q^{1-delta}, so not in-window; for l=2 they lie in the STRUCT horn). Narrow-datum rescue does not apply: the precise constants B_n=2^mDp and the equalities are mechanically implied by definitions/degree, not an unknown invariant a future researcher would need to retrieve; replay certifies but does not rescue textbook content per policy. Even if correct and new, this is a textbook/elementary packaging with no substantive result toward the admitted target or fallback.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Quantifier-free fragment only; no statement about existential/universal formulas where the target lives. No growth exponents; does not prove target or fallback (25/24, 11/12) dichotomy. Exhaustive checks are small-field Fp-slice illustrations; general-coefficient case rests on Lemma 2.1 proof (needs p>D).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
