# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Newly certified hyperbolic period-7 saddle of the classical Henon map with explicit Krawczyk box, cone margin, and persistence interval
- **Round:** 2026-09-07-first-light-01
- **Lane:** 11
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Dynamical Systems
- **Method:** rigorous interval-arithmetic enclosure with continuation and topological horseshoe verification

## Problem

Fix H_{a,b}(x,y)=(1-a*x^2+y,b*x) with b=0.3. Exhibit and rigorously certify ONE period-7 saddle orbit at a=1.4 (minimal period exactly 7) by interval-Krawczyk boxes B_0..B_6 in phase space plus cone-condition hyperbolicity and a-continuation: boxes pairwise disjoint, widths <=1e-09, Krawczyk strict inclusion with margin logged, interval monodromy eigenvalues off unit circle with explicit cone (Q,lambda,margin), and uniform certification over a-parameter interval A=[1.4-d,1.4+d] with d>=2.5e-05 (target >=5e-05). Success predicate is fully numerical and auditor-checkable from the interval log.

## Attempted claim

There exists a minimal-period-7 saddle orbit {p_0..p_6} of H_{1.4,0.3} with p_i in explicit boxes B_i of width <=1e-09 (pairwise disjoint, logged), certified by strict Krawczyk inclusion K([B]) subset interior([B]) for F(z)=(H(z0)-z1,...,H(z6)-z0); interval monodromy M=D(H^7)([B_0]) encloses eigenvalues with |lambda_u|>1>|lambda_s| (saddle, off unit circle) witnessed by explicit cone Q,lambda>1 with interval positivity margin >0; and the same itinerary persists over parameter interval A=[1.4-d,1.4+d] with d>=2.5e-05 (target 5e-05) by uniform Krawczyk inclusion at b=0.3.

## Research outcome

First bit-reproducible interval certificate for a minimal-period-7 Hénon saddle (P7-A) at classical (1.4,0.3): 1e-09 point boxes with strict Krawczyk inclusion (margin 5e-10, q 4.3e-09), disjointness gap 0.119, monodromy trace 35.7426/det -2.19e-04 giving lambda_u~35.74/lambda_s~-6e-06, diagonal cone Q=diag(1,-1/5) lambda=10 with Sylvester margins >900, and uniform persistence over a in [1.39995,1.40005] (d=5e-05, 2x target) with wider 1e-03 tubes (margin 4.5e-04). Narrow-box persistence limit quantified at d~5.48e-10, proving same-box persistence to 2.5e-05 impossible and justifying two-level boxes. Verifier is pure-Python stdlib, 0.04s, 60-record JSONL + SHA256.

## Why this attempt failed

Failed axes: value.

value: Even though correct and new, result is not independently worth finding later: textbook restatement + single enumeration + tiny unmotivated gain. (i) Textbook method: 14-dim Krawczyk/interval-Newton for Henon periodic orbits with trace/det eigenvalue bounds and diagonal-cone Sylvester check is canonical validated-numerics exercise (Tucker/Wilczak/Zgliczynski tutorials; CAPD/INTLAB routinely certify such strongly hyperbolic orbits in minutes). No methodological innovation; huge margins (q 4e-09, cone >900, eigenvalue gaps 34.7/0.99999) show orbit is far from bifurcation and easy. (ii) Mere enumeration: one orbit P7-A among many numerically known Henon cycles, no classification, no fixed symbolic partition (itinerary means cyclic box order only), no counting or optimality. First-box-for-this-itinerary is weak firstness — any tabulated numerical cycle can be boxed routinely. (iii) Tiny unmotivated persistence: d=5e-05 (relative 3.5e-05) with 1e-03 wide tubes, threshold 2.5e-05 arbitrary audit target not tied to any bifurcation or entropy milestone; narrow 1e-09 boxes provably persist only to ~5.48e-10, so advertised narrow boxes are non-robust points, persistence requires 1000x wider tubes. Standard hyperbolic persistence via IFT guarantees some interval; quantifying 5e-05 adds no insight. (iv) Motivated reuse not delivered: draft cites entropy/bifurcation certification and transverse homoclinic forcing positive entropy, but explicitly disclaims any entropy theorem; single saddle without homoclinic/transversality gives no entropy lower bound, no bifurcation-diagram certificate demonstrated, future reuse speculative. Widths/margins are audit criteria, not contributions (draft admits). Therefore falls under reject categories: textbook restatement, mere parameter substitution (classical 1.4,0.3 instance), tiny unmotivated gain, unexplained enumeration even if correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: One orbit only, no classification; persistence uses wider tubes (1e-03) not same 1e-09 boxes — narrow-box max d~5.48e-10 bisected exactly, so same-box 2.5e-05 persistence is disproved by sensitivity (~1.53d); cone is monodromy Lyapunov (per-step same-Q provably fails near x=0); eigenvalue bounds via interval tr/det (sound overestimation); CPython IEEE-754 round-trip assumed; entropy/bifurcation reuse is motivation, not claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
