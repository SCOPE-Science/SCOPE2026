# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Hyperbolic typical-cell vertex-number distribution
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1263
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** hyperbolic stochastic geometry
- **Method:** Slivnyak-Mecke plus hyperbolic Delaunay circumdisk

## Problem

Let H^2 be the hyperbolic plane of curvature -1 with stationary Poisson-Voronoi tessellation of intensity lambda>0 and typical cell C_lambda defined by Palm calculus at the origin. Let N_lambda be its number of edges/vertices (N_lambda>=3). Determine, for every lambda>0 and every integer n>=3, an exact explicit integral representation p_n(lambda)=P(N_lambda=n), with stated integration domain, hyperbolic distance/volume factors, and empty circumdisk probability. A complete answer gives the kernel for all n and lambda, proves sum_{n>=3} p_n(lambda)=1 and finiteness of E[N_lambda], and evaluates the high-intensity limit.

## Attempted claim

Let H^2 be the hyperbolic plane of curvature -1 with stationary Poisson-Voronoi tessellation of intensity lambda>0 and typical cell C_lambda defined by Palm calculus at the origin. Let N_lambda be its number of edges/vertices (N_lambda>=3). Determine, for every lambda>0 and every integer n>=3, an exact explicit integral representation p_n(lambda)=P(N_lambda=n), with stated integration domain, hyperbolic distance/volume factors, and empty circumdisk probability. A complete answer gives the kernel for all n and lambda, proves sum_{n>=3} p_n(lambda)=1 and finiteness of E[N_lambda], and evaluates the high-intensity limit.

## Research outcome

Exact integral law for the hyperbolic Poisson-Voronoi typical-cell vertex count proved for all intensities and all n>=3 with repaired kernel including deterministic self-avoidance S, with normalisation, finite mean, Euclidean high-intensity limit, and re-run S=1 verification.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: draft proves the admitted exact integral law itself. The Slivnyak-Mecke counting kernel with gap H, finite-centre Ei, deterministic self-avoidance S and flower void exp(-lambda F) is correctly derived in both directions, cosine-rule threshold tanh(rho/2)<cos(pi/n), Klein linear solve, union-area functional and re-run symmetric S=1 margins all check out, and the high-intensity DCT domination is sound. However the finite-mean proof in Section 2 is logically reversed: P(x neighbour)=P(union_c A_c) >= P(A_m) for any fixed midpoint ball, so emptiness of B(m,rho/2) lower-bounds rather than upper-bounds the neighbour probability. Hence E[N]<=lambda-int void bound is invalid and E[N]<infty is asserted without valid proof, although the fact itself is true by published expected f-vector results. This essential-inference error fails correctness as written but is boundedly repairable.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The kernel is explicit up to the elementary Klein-coordinate bisector-intersection map, the union-area functional, and the deterministic self-avoidance indicator S; no further elementary closed form holds for general asymmetric configurations. Hyperbolic Delaunay existence, uniqueness and transversality are cited from standard theory. Numerics verify only the symmetric regular-flower sub-family (S=1 with positive margins) as a sanity check, not the full n-fold integral.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
