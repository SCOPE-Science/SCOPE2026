# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** GHPUL scaling limit of the full critical face-percolation loop ensemble on quadrangulations to CLE_6
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20378
- **Disposition:** NO_RESULT
- **Domain:** Probability Theory
- **Method:** SLE coupling and peeling exploration analysis

## Problem

Let (Q_n,e_n) be a free Boltzmann quadrangulation with simple boundary of perimeter l_n^L+l_n^R (even), with c^{-1}n^{-1/2}l_n^{L,R} -> l^{L,R}>0 for c=2^{3/2}/3, decorated by critical (p=3/4) face percolation theta_n with l_n^L-white/l_n^R-black boundary conditions. Equip Q_n with the rescaled graph metric d_n=c^{-1/2}n^{-1/4}d_graph, the rescaled degree measure mu_n, the rescaled boundary path xi_n, and the chordal percolation exploration path eta_n with time rescaling s n^{3/4}, exactly as in Gwynne-Miller Theorem 1.2. Let Gamma_n be the full collection of face-percolation interface loops on Q_n obtained by iterating the chordal peeling exploration inside the complementary bubbles (the discrete analogue of the branching-SLE_6 construction of CLE_6). Let (H,d,mu,xi) be the free Boltzmann Brownian disk of perimeter l^L+l^R. Prove, unconditionally and asymptotically as n->infinity, that (Q_n,d_n,mu_n,xi_n,Gamma_n) => (H,d,mu,xi,Gamma) in law in the Gromov-Hausdorff-Prokhorov-uniform-loop (GHPUL) topology, where Gamma is an independent CLE_6 on H, jointly with the GHPU convergence (Q_n,d_n,mu_n,xi_n,eta_n) => (H,d,mu,xi,eta) to chordal SLE_6.

## Attempted claim

Let (Q_n,e_n) be a free Boltzmann quadrangulation with simple boundary of perimeter l_n^L+l_n^R (even), with c^{-1}n^{-1/2}l_n^{L,R} -> l^{L,R}>0 for c=2^{3/2}/3, decorated by critical (p=3/4) face percolation theta_n with l_n^L-white/l_n^R-black boundary conditions. Equip Q_n with the rescaled graph metric d_n=c^{-1/2}n^{-1/4}d_graph, the rescaled degree measure mu_n, the rescaled boundary path xi_n, and the chordal percolation exploration path eta_n with time rescaling s n^{3/4}, exactly as in Gwynne-Miller Theorem 1.2. Let Gamma_n be the full collection of face-percolation interface loops on Q_n obtained by iterating the chordal peeling exploration inside the complementary bubbles (the discrete analogue of the branching-SLE_6 construction of CLE_6). Let (H,d,mu,xi) be the free Boltzmann Brownian disk of perimeter l^L+l^R. Prove, unconditionally and asymptotically as n->infinity, that (Q_n,d_n,mu_n,xi_n,Gamma_n) => (H,d,mu,xi,Gamma) in law in the Gromov-Hausdorff-Prokhorov-uniform-loop (GHPUL) topology, where Gamma is an independent CLE_6 on H, jointly with the GHPU convergence (Q_n,d_n,mu_n,xi_n,eta_n) => (H,d,mu,xi,eta) to chordal SLE_6.

## Research outcome

Target blocked and cleanly exited: GHPUL convergence of the full critical face-percolation loop ensemble to CLE6 cannot be closed from Gwynne-Miller Theorem 1.2 alone, because complementary peeling bubbles are generically monochromatic, microscopic bubbles have infinite variation, and the required uniform stability and loop-tightness inputs are missing. No emergent finding met the independent-value bar.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The GHPUL full-loop-ensemble target could not be closed in-lane: monochromatic peeling bubbles fall outside the dichromatic Gwynne-Miller Theorem 1.2 input, the only summation-based small-bubble shortcut diverges like 1/eps per the bounded recovery test, and uniform loop-level tightness plus CLE6 identification inputs are absent. Working notes and recovery-test scripts are preserved in output/WORKLOG.md and output/artifacts/.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The GHPUL full-loop-ensemble target could not be closed in-lane: monochromatic peeling bubbles fall outside the dichromatic Gwynne-Miller Theorem 1.2 input, the only summation-based small-bubble shortcut diverges like 1/eps per the bounded recovery test, and uniform loop-level tightness plus CLE6 identification inputs are absent. Working notes and recovery-test scripts are preserved in output/WORKLOG.md and output/artifacts/.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
