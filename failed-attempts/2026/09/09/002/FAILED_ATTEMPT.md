# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Skeletal cut-locus dichotomy for symmetric disphenoids with blooming edge-net witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 262
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Geometry
- **Method:** source-unfolding cut-locus computation with skeleton-incidence and blooming edge-net certification

## Problem

Decide the skeletal-cut-locus dichotomy over the symmetric disphenoid family D_t with congruent (1,1,t) faces: for which t in (0,2) does there exist a source point x with cut locus C(x) contained in the 1-skeleton, with exact tree type and blooming edge-net certificate where it exists and a proved obstruction where it does not; deliver the threshold plus both certificates replayed from committed unfoldings.

## Attempted claim

Over D_t, t in (0,2): an exact skeletal-cut-locus dichotomy with threshold interval T* such that for t on one side there exists an explicit source point x with C(x) subset Sk(D_t) of stated tree type whose source unfolding is a certified blooming edge-net, and for t on the other side no source point has skeletal cut locus, proved by an explicit combinatorial obstruction; all trees and containments replayed from committed source unfoldings.

## Research outcome

Proved an exact skeleton-edge cut point u*=(-13+sqrt(1429))/45 on the regular disphenoid D_1 for the face-centroid source, with exact tie of two unfold paths and stdlib replay certificate; the full skeletal dichotomy was not closed and is explicitly not claimed.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Replay of the committed scripts succeeds (cert_exact.py SELF-TEST OK; edge_bisect.py EDGE-BISECT CERT OK with quadA=u^2-8u/15+17/36, quadB=u^2/4-29u/30+169/180, diff=(3/4,13/30,-7/15), D=1429/900, u*~0.55115 in (11/20,14/25), endpoint order flip A<B to B<A). However two independent fatal defects make the stated theorem about D_1 false: (1) Wrong model geometry. cert_exact.py ref_face() places the face triangle at (0,0),(1,0),(0,1/2) with comment claiming equilateral (1/2,sqrt3/2). Edge lengths are 1, 0.5, sqrt(1.25)~1.118, not 1,1,1. The S3 sqrt(3) engine is never used for the base triangle (y=S3(1/2,0) instead of S3(0,1/2)). Layout check confirms: F1->F3 apex at (2/5,-4/5) instead of correct equilateral (1.5,-0.866). Source bary(1/3,1/3,1/3) maps to (1/3,1/6)~(0.333,0.167) instead of correct centroid (0.5,sqrt3/6~0.289). So proven quadratics/root describe a right-triangle-faced tetrahedron-like surface, not regular D_1. (2) False global minimality / not a cut point. Source face F0=(0,1,2) and target face F3=(1,2,3) share edge (1,2); target y(u) lies ON that shared edge. The true shortest path from interior source to y is the direct in-face segment in F0, squared length (u-1/2)^2+1/12 ~0.0858 at u=11/20 (0.0859 at u*), vs claimed qA~0.4814, qB~0.4828. Independent check: valid_and_dist strict=False for seq (0,3) returns 73/2880~0.0253 in code coordinates (also strictly shortest), while strict=True returns None because t=1 on the boundary is rejected by the strict interior-crossing filter. true_dists strict enumeration therefore omits the true minimizer and reports only the two longer detours. The DRAFT step 3 claim 'exactly two valid paths exist ... Hence at both endpoints the global minimizer is one of A,B' is false; the loose enumeration shows 3 paths with (0,3) first. At u* the two detours tie at ~0.48-0.69 (depending on correct vs code geometry) but are both strictly longer than the direct segment, so y(u*) does not have two distinct globally-shortest geodesics and is not in C(x). Continuity between three checked rationals also does not rule out a third path becoming valid inside the bracket, but the direct-path counterexample alone defeats the cut-point conclusion. What is proved is only a tie of two non-minimizing unfold paths in the wrong geometry; what is experimental (float scans of face-interior cut loci, vertex-grid gaps) is correctly labeled as such and not claimed. value: Strongest self-contained headline judged separately from the unfinished dichotomy survey, which the DRAFT honestly disclaims ('no full skeletal witness, no skeletal-free interval, no threshold dichotomy; admitted full dichotomy and fallback pair NOT closed'). The remaining headline is: one interior point where C(x) meets one skeleton edge for one source (face centroid) on D_1. This is not a skeletal witness C(x) subset Sk (which requires containing the entire cut locus; DRAFT notes evidence the centroid's locus also meets face interiors, so centroid is…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Narrow partial theorem only: one edge cut-point for one source at t=1. Does NOT prove C(x) subset Sk (full skeletal witness), no skeletal-free interval, no threshold dichotomy; full admitted claim and fallback pair not closed. Strict interior-crossing validity filter; vertex-grazing paths excluded (all crossings here strictly interior with margin). Minimality at u* via continuity between exactly-checked brackets plus exhaustive DFS sequence list.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
