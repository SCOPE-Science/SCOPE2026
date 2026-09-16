# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Prove Jensen's corrected billiards formula for second-generation p-canonical basis elements on the wall in affine type A2
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20473
- **Disposition:** NO_RESULT
- **Domain:** Representation Theory
- **Method:** Soergel bimodule categorification analysis

## Problem

Let G=SL_3 over an algebraically closed field of characteristic p>2, with affine Weyl group W, fW minimal W_f\W representatives, anti-spherical module AS_v with bases {n_x} and {^pn_x}, and x_0=id, x_1=s_0, x_2=s_0s_1, ... along one dominant-cone edge. Let eZ be the multiset from Lusztig-Williamson Steps 1-3 with Step 2 replaced by Jensen's corrected wall dynamics with geometric merge rule (type II/III), l=p, and define ^p zeta_0=n_{x_0} and for i>0, ^p zeta_i := n_{x_i} + sum_{(mu,n(v^k)) in eZ, n in {i,i-1,i-2}} phi(v^k) n_{x^s_mu} with phi as in LW18 section 6. Prove: (a) ^p zeta_i = ^pn_{x_i} for 0<=i<2p(p+1); (b) ^p zeta_i = ^pn^2_{x_i} for all i>=0 (Jensen arXiv:2105.04665 Conj. 3.1 correcting Lusztig-Williamson SIGMA 14 (2018) 015 Conj. 6.1).

## Attempted claim

Let G=SL_3 over an algebraically closed field of characteristic p>2, with affine Weyl group W, fW minimal W_f\W representatives, anti-spherical module AS_v with bases {n_x} and {^pn_x}, and x_0=id, x_1=s_0, x_2=s_0s_1, ... along one dominant-cone edge. Let eZ be the multiset from Lusztig-Williamson Steps 1-3 with Step 2 replaced by Jensen's corrected wall dynamics with geometric merge rule (type II/III), l=p, and define ^p zeta_0=n_{x_0} and for i>0, ^p zeta_i := n_{x_i} + sum_{(mu,n(v^k)) in eZ, n in {i,i-1,i-2}} phi(v^k) n_{x^s_mu} with phi as in LW18 section 6. Prove: (a) ^p zeta_i = ^pn_{x_i} for 0<=i<2p(p+1); (b) ^p zeta_i = ^pn^2_{x_i} for all i>=0 (Jensen arXiv:2105.04665 Conj. 3.1 correcting Lusztig-Williamson SIGMA 14 (2018) 015 Conj. 6.1).

## Research outcome

Target blocked: full proof of Jensen corrected billiards conjecture needs open representation theory; three concrete routes attempted with evidence, bounded simulator confirms only combinatorics, clean exit with no finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Proving Jensen Conjecture 3.1 needs a new representation-theoretic bridge from corrected billiard combinatorics to Soergel p-canonical bases plus control of higher generations; finite Magma data for l=3,5,7,11 and a combinatorial simulator cannot supply it, so no auditable partial result was reachable in-session.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Proving Jensen Conjecture 3.1 needs a new representation-theoretic bridge from corrected billiard combinatorics to Soergel p-canonical bases plus control of higher generations; finite Magma data for l=3,5,7,11 and a combinatorial simulator cannot supply it, so no auditable partial result was reachable in-session.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
