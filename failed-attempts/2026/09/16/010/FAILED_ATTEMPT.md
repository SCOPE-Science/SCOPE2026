# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp Li-Yau equality rigidity on noncollapsed RCD(0,N) spaces
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20447
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** Metric Geometry
- **Method:** optimal-transport and heat-flow analysis

## Problem

Let (X,d,H^N) be a noncollapsed RCD(0,N) space with integer N>=3 and let u>0 be a locally weak solution of the heat equation on X x (0,T) in the sense of Zhang-Zhu. If equality holds in the sharp global Li-Yau estimate (ln u)_t - |grad ln u|^2 + N/(2t) = 0 at some point (x0,t0), does it follow that X is an N-metric-measure cone over an RCD(N-2,N-1) space with pole at the vertex, and in particular that if the pole is N-regular then X is isomorphic to R^N and u is a constant multiple of the heat kernel?

## Attempted claim

Let (X,d,H^N) be a noncollapsed RCD(0,N) space with integer N>=3 and let u>0 be a locally weak solution of the heat equation on X x (0,T) in the sense of Zhang-Zhu. If equality holds in the sharp global Li-Yau estimate (ln u)_t - |grad ln u|^2 + N/(2t) = 0 at some point (x0,t0), does it follow that X is an N-metric-measure cone over an RCD(N-2,N-1) space with pole at the vertex, and in particular that if the pole is N-regular then X is isomorphic to R^N and u is a constant multiple of the heat kernel?

## Research outcome

Repaired submission: restored Lemma 2 with exact theorem numbers (bounded drift, singular-x0 continuity, backward propagation), proved r=d(o,.) and volume ratio for De Philippis-Gigli, verified Ketterer diam/measure hypotheses and pole t-independence, completed Widder moments/covariance/uniqueness; one-point Li-Yau equality forces metric cone (RCD(N-2,N-1) link), Euclidean heat kernel at regular pole.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET proof has essential gaps. Lemma 2 propagation from Q(x0,t0)=0 to Q=0 on Xx(0,t0] invokes Sturm Harnack for solutions while Q is only a continuous supersolution with L_inf drift and unverified H1/domain membership for ZZ16 Thm4.4 and GR17 Thm2.8; slice-freezing ignores dtQ term. Bochner (3) needs g=Lf in H1 cap L_inf, not shown; alpha=1 extension of ZZ16 Lem5.7 unverified. Hessian-to-distance r=d(o,.) and volume ratio (9) assume Laplacian has no singular part and coarea/cutoff integration without proof. Pole t-independence is false from Hessian alone (translated |x-a|^2/2 on R^N share Hessian g); no E=0 computation fixes ot. Euclidean Widder moment bound uses t'<t dominance backwards (narrower cannot dominate wider+quadratic); fixable with later time. Artifact check passes (agree 3.8e-7) but covers only finite mixtures.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Uses assumed continuous representative of E; weak Bochner/maximum/cone theorems invoked as cited results with exact numbers (ZZ16, GR17, DPG16, Ket15, Sturm/Marola-Masson); computed check covers finite Gaussian mixtures with general Widder measure handled analytically; no claim for t>t0 or classifying u on non-Euclidean cones.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
