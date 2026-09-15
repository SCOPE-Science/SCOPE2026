# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** MacWilliams-Delsarte binomial bound for binary linear codes with prescribed dual distance beyond the unrestricted-code range
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20382
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Coding Theory
- **Method:** MacWilliams identities and linear-programming bound analysis

## Problem

Let {C_n} be binary linear [n,k_n] codes with k_n/n -> R in (0,1) and dual distance d^perp_n/n -> delta^perp > 0, and let A^{(n)}_w be the Hamming weight distribution of C_n. Let xi_ABL(R,delta^perp) be the Ashikhmin-Barg-Litsyn binomiality threshold (Corollaries 2-3 of arXiv/doi:10.1109/18.915662, improving Krasikov-Litsyn doi:10.1023/A:1008206125050): for every unrestricted binary code of rate R and dual distance delta^perp n, A^{(n)}_w <= 2^{k_n-n} binomial(n,w)(1+o(1)) uniformly for w/n in [xi_ABL(R,delta^perp),1/2] as n -> infinity. Using the full binary MacWilliams identities relating {A^{(n)}_w} to the dual distribution {A^{perp(n)}_j} -- in particular A^perp_j=0 for 1 <= j < d^perp_n and A^perp integral/nonnegative as the weight distribution of the linear dual -- decide, via Delsarte linear-programming feasible-polynomial (Krawtchouk) analysis, whether there exists an open set of (R,delta^perp) and epsilon(R,delta^perp)>0 such that every binary linear family above satisfies the same binomial upper bound on the strictly larger interval [xi_ABL(R,delta^perp)-epsilon,1/2], and otherwise establish Delsarte-MacWilliams LP-optimality of xi_ABL for binary linear codes (no feasible Krawtchouk certificate extends it).

## Attempted claim

Let {C_n} be binary linear [n,k_n] codes with k_n/n -> R in (0,1) and dual distance d^perp_n/n -> delta^perp > 0, and let A^{(n)}_w be the Hamming weight distribution of C_n. Let xi_ABL(R,delta^perp) be the Ashikhmin-Barg-Litsyn binomiality threshold (Corollaries 2-3 of arXiv/doi:10.1109/18.915662, improving Krasikov-Litsyn doi:10.1023/A:1008206125050): for every unrestricted binary code of rate R and dual distance delta^perp n, A^{(n)}_w <= 2^{k_n-n} binomial(n,w)(1+o(1)) uniformly for w/n in [xi_ABL(R,delta^perp),1/2] as n -> infinity. Using the full binary MacWilliams identities relating {A^{(n)}_w} to the dual distribution {A^{perp(n)}_j} -- in particular A^perp_j=0 for 1 <= j < d^perp_n and A^perp integral/nonnegative as the weight distribution of the linear dual -- decide, via Delsarte linear-programming feasible-polynomial (Krawtchouk) analysis, whether there exists an open set of (R,delta^perp) and epsilon(R,delta^perp)>0 such that every binary linear family above satisfies the same binomial upper bound on the strictly larger interval [xi_ABL(R,delta^perp)-epsilon,1/2], and otherwise establish Delsarte-MacWilliams LP-optimality of xi_ABL for binary linear codes (no feasible Krawtchouk certificate extends it).

## Research outcome

Proved local real-LP primal-duality barrier: at BCH localizations (15,7,4) and (31,15,7), exact Delsarte-MacWilliams primal maxima exceed the binomial value by 11-46x at weights strictly below the binding xi1 branch (xi2=0 shown by scan), so no real-LP Krawtchouk certificate proves the binomial bound there.

## Why this attempt failed

Failed axes: value.

value: The headline is three tiny-n point evaluations (n=15,31; w=2,4,5) showing the real-LP relaxation exceeds the binomial value below the xi1 branch. The admitted target asked for an asymptotic open set epsilon-extension ruling or Delsarte-MacWilliams LP-optimality of xi_ABL; the draft explicitly claims neither and retreats to finite-n localizations. Fixed small-weight LP slack where binomial<1 is a cheap small-instance mismatch and arbitrary finite slice under the shared standard: it does not resolve the asymptotic question, provides no general criterion, census, benchmark, or downstream use, and the precise numbers 5.63636/22.2762/29.4919 were not motivated before computation as a recognized needed fact. Correctness plus novelty do not create value.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Real-LP certificates only; no claim about integrality-using certificates, true extremal weight distributions, or violating codes. Integrality remarks are labeled heuristic without degree accounting and unused by the theorem. ABL free-parameter optimality is noted as unproved in the source ('we leave this fact without proof'); no family- or global LP-optimality is claimed. Result is local to the two finite-n BCH localizations; no open set, epsilon-extension ruling, or asymptotic family is claime…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
