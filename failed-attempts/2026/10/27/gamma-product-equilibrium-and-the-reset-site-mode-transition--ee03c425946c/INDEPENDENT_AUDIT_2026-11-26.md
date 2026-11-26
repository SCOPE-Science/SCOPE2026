# Independent mathematical audit

## correctness

PASS

For the specified Brownian entrance, the clock is continuous, strictly increasing and unbounded (in d≥3 Brownian transience puts the path eventually outside any fixed ball), and the origin is polar after departure. With n=α+2 and Y=R^n/(κ n²), direct differentiation gives L_Y=y∂²_y+a∂_y, a=1+(d−2)/n. The time-change Itô argument extends from zero because r^n is C² there and the drift and quadratic variation after time change are a dt and 2Y dt for positive times. At fixed t and s≥0 the bounded backward-test martingale with value (1+s(t−v))^(−a) exp(−sY_v/[1+s(t−v)]) gives Y_t in law tG_a. Independent Poisson ages are Exp(λ); coupling at the next reset gives uniqueness. The product law follows by scaling the age, and both gamma integrals are finite exactly when q/n>−1 since a>1. Writing ν=a−1 and u=λr^n/(κ n²), the Bessel product density has f_U(0+)=Γ(ν)/Γ(a)=1/ν, giving the small-ball constant λ/[κ(d−2)n] and spatial density asymptotic λr^(n−d)/[κ(d−2)ω_d]. In the spatial mode calculation, (z^νK_ν)'=−z^νK_{ν−1}<0, settling n−d≤0. For n−d>0, ν∈(0,1); h=zK_{ν−1}/K_ν satisfies z h'=h²+2νh−z². Small-z asymptotics give h∼c z^(2ν) for c>0, hence h'>0 near zero by the Riccati equation; at infinity h=z+1/2−ν+O(1/z) gives h'→1 by the same equation. Every zero of h' would have h''=−2, precluding a return to positive derivative, so h increases strictly from zero to infinity. The spatial log slope n−d−(n/2)h has one zero above threshold, proving the unique maximizing radius, not a mode of the radius density. The frozen numerical script and recorded checks were inspected, not executed; they are not needed for these universal statements.

## originality

FAIL

Resultary 56391c757951 proves the same stationary spatial density and mode transition in a larger parameter range for the same entrance and reset convention. Its transient kernel is explicitly gamma after the frozen radial power transform, so mixing with the specified exponential age directly gives the two-gamma representation and exact moments. This is mathematical coverage, not a priority inference from catalog dates.

## value

FAIL

The sharp spatial-mode threshold is useful but already covered. The exact two-gamma sampler is practically convenient; it is obtained directly by a change of variables in the covered transient heat kernel followed by drawing the already specified exponential age. The moments and small-ball coefficient also follow directly, so the reviewed package does not supply a separate worthwhile mathematical increment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
