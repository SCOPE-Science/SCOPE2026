# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Theta-versus-Hoffman strictness gap over connected triangle-free cubic graphs on 18 vertices, with exact independence-number cross-check
- **Round:** 2026-09-07-first-light-01
- **Lane:** 122
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Spectral Graph Theory
- **Method:** Hoffman-ratio versus Lovasz-theta gap maximization with exact independence-number branch-and-bound cross-check

## Problem

Take the complete stratum of connected triangle-free cubic graphs on exactly n=18 vertices (a triangle-free subset of the 41301 connected cubics at n=18, OEIS A002851, generable by geng in seconds). For each graph G compute: (a) Hoffman chromatic lower bound h(G)=1+3/(-lambda_min), (b) Lovasz theta of the complement t(G)=theta(complement(G)) via SDP with stored primal/dual feasible pair, (c) exact independence number alpha(G) by branch-and-bound. Determine the exact maximum absolute strictness gap D*=max|t(G)-h(G)| over the stratum, the graphs attaining it, and the full distribution tables of h, t, alpha. Success = exact D* with named extremal graph(s), adjacency list(s), dual SDP logs, spectra, and alpha certificates plus a replay script.

## Attempted claim

Over all connected triangle-free cubic graphs on 18 vertices, the exact maximum D*=max_G|theta(complement(G))-(1+3/(-lambda_min(G)))| equals the computed value D* (determined by the run), attained at one or more explicit named graphs G* supplied with adjacency lists, full spectra, primal/dual SDP feasible pairs bracketing theta to <1e-4, and exact alpha(G*) by replayable branch-and-bound; the accompanying table proves no stratum member exceeds D*.

## Research outcome

Certified strict theta-vs-Hoffman gap >= 0.1207606083 on an explicit connected triangle-free cubic 18-vertex graph (h=2.0753233129, theta_LB=2.1960839212, alpha=8), machine-verified by replay script; full-stratum exact maximum not determined (downgraded partial theorem).

## Why this attempt failed

Failed axes: originality, value.

originality: Delivered result is materially narrower than the admitted target and is not substantively new. Admitted target: exact maximum D*=max|theta(comp)-(1+3/(-lmin))| over the COMPLETE connected triangle-free cubic n=18 stratum with maximality certificate and distributions. Delivered: one-sided lower bound D*>=0.1207606083 from a single config-model seed (RTF_seed77) via one primal-feasible X, plus an 11-graph explicitly incomplete pool. Existence of a strict theta-vs-Hoffman gap is already established general theory, not a new per-stratum extremal: de Carli Silva et al. (2106.11121) proves Hoffman-sum vs theta comparison framework (Hoffman-sum at least as good as theta, i.e. the two bounds are distinct and comparable, with strict cases); Elphick-Wocjan (1210.7844) gives unified spectral chi-bounds with examples outperforming/differing from each other. That a random 18-vertex triangle-free cubic has theta(comp)-h ~0.07-0.31 is shown by the candidate's own 11-graph table (dual UB gaps 0.07-0.31), proving the witness is generic, not distinguished. The specific number 0.1207 is a solver-dependent primal feasible value (true theta lies somewhere in [2.196,2.353] per their UB), not a canonical extremal value; no maximality scan, no distribution, no lexicographically-smallest extremal. A timestamp or failed in-lane search does not establish priority. Hence no prior per-stratum maximum is beaten because none is computed, and the single-instance strictness was already implied by known separation of the two chi lower bounds. value: Even taking correctness as given, the downgraded single-witness lower bound is not independently worth finding later. It is an arbitrary-slice anecdote: one random seed's primal objective minus Hoffman value, with true theta unknown (heuristic interval width ~0.16 exceeds the claimed gap 0.12). No complete-stratum enumeration (41301 pool not generated, triangle-free count not determined), no h/theta/alpha distributions or extrema, no dual brackets to <1e-4 proving maximality, so neither the primary exact-D* claim nor the predefined fallback citable benchmark (counts, distributions, slack extrema, witnessed extremals with certificates and replay over the full stratum) is delivered. The 11-graph table is explicitly a demonstration pool, not a census. Downstream calibration/benchmark use claimed in topic.json requires completeness and maximality; a generic ~0.1 gap reproducible on almost any random triangle-free cubic (per candidate's own table) has no such use. This falls under tiny unmotivated gain / arbitrary parameter instance / unexplained enumeration: correct but not retrievable-value science.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: One-sided partial theorem only: full-stratum exact D* not determined (no nauty/geng or SDP packages in lane; numpy-only). Theta upper bound heuristic (~2.35), only LB certified. Double-precision eigvalsh with 1e-9 tolerances; PSD margin -2.36e-17 treated as zero. Originality per admission-review triage, not re-searched in-lane.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
