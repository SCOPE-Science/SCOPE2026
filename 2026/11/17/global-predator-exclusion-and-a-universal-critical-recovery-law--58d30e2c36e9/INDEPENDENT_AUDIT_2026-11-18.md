# Independent mathematical audit

## correctness

PASS

Correctness PASS. For 0<s<1, w, alpha, theta>0 and 0<x0<=1, y0>0, G(x)=(x-s)(1-x)/(x+w) satisfies G(x)<1-x on (0,1), so the prey strip remains invariant; g=x exp(G) has 1+xG'>0. Predator exponent is at most beta/(1+alpha)-theta and at equality equals -theta(1-x)/(1+alpha*x). A hypothetical positive predator limit at equality forces x->1 then strictly negative prey log-drift, contradiction. The asymptotically autonomous monotone prey map has liminf/limsup fixed among 0,s,1; lower barriers and the x<=s one-way region force one limit. For x->1 set u=1-x,v=y; the local recurrence u_next=(1-a)u+bv+O((u+v)^2), log(v_next/v)=-ku+O(u^2), with a=(1-s)/(1+w), b=1/(1+alpha), k=theta/(1+alpha). The ratio u/v is bounded by a contracting affine inequality then tends to b/a; reciprocal v increments tend to k*b/a, yielding the two asserted n-scaled amplitudes. f_eta(t)>t gives a nonempty open recovery wedge, and above-threshold explicit (x*,y*) is positive for small delta. Numerically checked three critical examples at n=200000 and exactly differentiated G; no finite sampling is offered as proof.

## originality

PASS

Originality PASS, best of knowledge. Patra–Maitra introduced precisely this exponential Holling-II strong double-Allee map and derived local equilibria/Neimark–Sacker analysis; its accessible 2024 preprint and the 2026 journal abstract do not establish every-orbit extinction at beta_c, prey-limit trichotomy, or the exact pair of critical amplitudes. Other critical predator papers found by Resultary concern altered prey/predator equations and hence do not imply these map-specific constants. The 2026 subscription journal full text could not be inspected because authorized Oxford retrieval returned vpn_disconnected; priority remains bounded and uncertain, not rejected solely for access.

## value

PASS

Value PASS. A globally sharp invasion/exclusion boundary with all-orbit prey endpoint classification and universal critical constants, conditional on an explicitly nonempty recovery basin, is a substantive qualitative and quantitative result for a named ecological difference equation. The critical 1/n amplitudes require nonlinear coupling analysis and are not a routine equilibrium linearization; an above-threshold existence witness sharpens the biological boundary without claiming stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
