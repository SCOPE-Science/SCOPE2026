# Self-review

## Correctness — PASS

The probability-Hermite generating function and Mehler diagonal give an exact finite sum-of-squares coefficient identity, independent of convergence. The coefficients are all nonnegative when \(0\le\gamma\le1\), and the constant-square coefficient has the proved positive central-binomial lower bound. The sharpness argument deals separately with negative \(\gamma\) and \(\gamma>1\); for the latter, an alternating series ratio tends to \(\gamma/(\gamma+1)\) after rigorous geometric-tail domination. The 528 exact-rational/symbolic checks in `verify_hermite.py` replay, but the analytical proof is the infinite certificate.

## Originality — PASS, qualified

Karvonen and Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, Sect. 2.4, explicitly state the relevant all-degree Hermite positivity as unproved; their approximate weight formula is credited. Their exact full-kernel weights are distinct. Karvonen, Kanagawa and Särkkä's other positivity theorems require different node hypotheses; the 2015 Gaussian-process sigma-point work provides earlier context without this sign proof. Searches of corresponding Hermite, Mehler, Laguerre and kernel-quadrature aliases, relevant published mathematical finding records, and accessible prior local claims have not produced an implication covering the SOS and sharp \([0,1]\) boundary. An equivalent classical identity under different notation is a material residual priority risk, not disproved by search.

## Value — PASS

The result proves a specific previously conjectured all-degree numerical-quadrature weight property, including a reusable nonnegative sum-of-squares certificate and an exact parameter-range boundary. This addresses an explicit question in a recognized integration construction; it is not a routine numerical table. The exact Gaussian-kernel-system weights, convergence rates, and floating-point accuracy remain unproved.

Self-review: passed. Independent audit: not yet performed.
