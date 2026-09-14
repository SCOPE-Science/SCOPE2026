# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Full Sarnak–Xue density for random Cayley graphs of SL_2(F_p)
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20096
- **Disposition:** NO_RESULT
- **Domain:** Combinatorics
- **Method:** representation-theoretic spectral gap techniques

## Problem

Fix d≥2. For each prime p, let G_p=SL_2(F_p), choose uniformly a d-element set T_p⊂G_p\{1} with T_p∩T_p^{-1}=∅, put S_p=T_p∪T_p^{-1}, and let X_p=Cay(G_p,S_p). Set q=2d−1 and n_p=|G_p|. If μ_i are the normalized adjacency eigenvalues of X_p, counted with multiplicity, define ρ_i=2 when |μ_i|≤2√q/(q+1), and otherwise define ρ_i∈(2,∞] by |μ_i|=(q^{1/ρ_i}+q^{1−1/ρ_i})/(q+1). Is it true that for every fixed r>2 and ε>0 there is C_{d,r,ε} such that Pr[# {i:ρ_i≥r}≤C_{d,r,ε} n_p^{2/r+ε}]→1 as p→∞ through primes?

## Attempted claim

Fix d≥2. For each prime p, let G_p=SL_2(F_p), choose uniformly a d-element set T_p⊂G_p\{1} with T_p∩T_p^{-1}=∅, put S_p=T_p∪T_p^{-1}, and let X_p=Cay(G_p,S_p). Set q=2d−1 and n_p=|G_p|. If μ_i are the normalized adjacency eigenvalues of X_p, counted with multiplicity, define ρ_i=2 when |μ_i|≤2√q/(q+1), and otherwise define ρ_i∈(2,∞] by |μ_i|=(q^{1/ρ_i}+q^{1−1/ρ_i})/(q+1). Is it true that for every fixed r>2 and ε>0 there is C_{d,r,ε} such that Pr[# {i:ρ_i≥r}≤C_{d,r,ε} n_p^{2/r+ε}]→1 as p→∞ through primes?

## Research outcome

Target blocked: sharp Sarnak-Xue density 2/r+epsilon for random Cayley graphs of SL2(Fp) could not be rigorously established in-session. Adjacency moments give a strictly weaker exponent (computed); the non-backtracking route yields the right exponent algebraically but its uniformity lemmas remain unproved. Clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The sharp 2/r+epsilon density bound for random SL2(Fp) Cayley graphs was not proved: naive adjacency moments provably overshoot the exponent (verified gap), and the sharp non-backtracking route still lacks rigorous uniform word-map, proper-power, and Ihara-Bass transfer lemmas. Reproducible artifacts cover only exponent algebra and a tiny-prime (p=5) spectral illustration, not the missing analytic estimates.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The sharp 2/r+epsilon density bound for random SL2(Fp) Cayley graphs was not proved: naive adjacency moments provably overshoot the exponent (verified gap), and the sharp non-backtracking route still lacks rigorous uniform word-map, proper-power, and Ihara-Bass transfer lemmas. Reproducible artifacts cover only exponent algebra and a tiny-prime (p=5) spectral illustration, not the missing analytic estimates.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
