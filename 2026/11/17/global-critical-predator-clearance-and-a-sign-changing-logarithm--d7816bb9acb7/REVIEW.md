# Independent mathematical audit

## correctness

PASS

For a<=alpha*d, f(z)=(d+a z)e^{-alpha z} has f'(z)=e^{-alpha z}(a-alpha*d-alpha*a z)<0 when z>0. Positive u is protected by bounded z exp(-alpha z); v remains positive nonincreasing, u is logistic-upper-bounded and its positive overshoot above one has finite time integral. The compensated ratio z exp(-integral(u-1)_+) decreases, forcing z=v/u->0; lower logistic comparison then forces u->1. The exact reciprocal drift d(1-e^{-alpha z})/v->d alpha gives tv->1/(d alpha); the stable scalar ratio w/v=(1-u)/v->a. Exact H=(1-u)-a v equation gives H=O(v²), and independently expanded derivative of 1/v equals d alpha+d alpha(a-alpha/2)v+O(v²). Consequently v=1/(d alpha t)+O(log t/t²), allowing integration of the residual to finite C and the sign-changing logarithmic correction. SymPy exactly confirmed the displayed first two reciprocal-series terms. Global and infinite-time arguments are analytic, not evidence from the finite integration script.

## originality

PASS

The primary Blyuss–Kyrychko publications establish this exponential response and Lambert-W directional equilibria, but do not assert all-positive-seed global attraction at b=d under a<=alpha d or the exact reciprocal predator logarithmic clock. The published Lambert-fold result studies a fold with positive extinction ratio where (b+a z)e^{-alpha z}=d+1; for b=d and a<=alpha d, (d+a z)e^{-alpha z}<=d so that fold is algebraically impossible. Other critical predator-prey models have different response functions and are not equivalent.

## value

PASS

The full physical-time second asymptotic at a nonhyperbolic invasion boundary gives a finite renormalized clock with an explicit ecological sign crossover. The structural condition a<=alpha d also yields a motivated, global all-seed extinction domain instead of a local center-manifold heuristic. Such a signed log correction is a natural, nontrivial exact invariant of the same named ecological response.

The dated certificate retains the supplied scientific assessment, sources and limitations.
