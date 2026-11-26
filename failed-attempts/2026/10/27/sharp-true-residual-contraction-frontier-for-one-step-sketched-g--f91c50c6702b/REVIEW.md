# Independent mathematical audit

## correctness

PASS

In the residual plane let v=Ar/‖Ar‖ and write r/‖r‖=cv+sw. For Gram diagonal entry a and off-diagonal d in this basis the normal equation leaves s(w−(d/a)v), after normalization. If s=0 the residual is eliminated. The embedding gives (a−1)²+d²≤ε², and (1−ε²)d²≤ε²a² since the difference in the relaxed scalar inequality is (a−(1−ε²))². Equality is feasible: the displayed M± has trace 2 and eigenvalues 1±ε, hence a real square root. The SPD moment bound ‖Ar‖²≤(L+μ)〈r,Ar〉−μL for unit r follows spectrally; minimizing the lower bound on c² gives c≥2√(μL)/(μ+L) with equality at the stated endpoint-eigenvector mixture. This proves sharpness over the admissible class (not for each fixed matrix or for d=1). Combining produces the exact factor, with one-step elimination when κ=1. For κ>1 the uniform strict condition is exactly ε<c_*=2√κ/(κ+1); at ε=c_* the negative extremal off-diagonal has d/a=−c_*/s, forcing t=0. The same sketch also meets all larger budgets; reusing it is admissible on the unchanged plane and stagnates. Below threshold the bound iterates for adaptive admissible sketches. The exact-rational support checker was inspected, not run; its bounded tests are corroborative only.

## originality

FAIL

A distinct Resultary record gives the same exact attained one-step residual frontier under the same squared-norm embedding, including its universal nonexpansion threshold and strict growth above it. Strict contraction is q<1. The negative off-diagonal choice in the same sharp Gram construction forces zero update at the frontier; the earlier record's printed norm-equality example need not itself use that choice. The difference in presentation supplies no separate mathematical novelty.

## value

FAIL

The sharp true-residual frontier is a useful method benchmark in isolation, but the exact factor and boundary regime are already covered. The only apparent additional claim, zero-update stagnation rather than equality of norms, requires just the opposite sign of the same extremal off-diagonal. The remaining restart estimate is a direct iteration and does not supply an uncovered valuable exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
