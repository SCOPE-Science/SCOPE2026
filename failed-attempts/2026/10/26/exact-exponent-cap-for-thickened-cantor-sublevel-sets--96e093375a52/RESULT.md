# Exact exponent cap for thickened Cantor sublevel sets

## Finding

Let \(C\subset[0,1]\) be the middle-third Cantor set and let \(\mu\) be its standard \((1/2,1/2)\) self-similar probability measure. Put \(s=\log 2/\log 3\). For an integer \(m\ge1\), a real number \(\varepsilon>0\), and \(0<\delta<1\), define

\[
F_{m,\varepsilon}(\delta)=\mu\!\left(\left(\{x\in\mathbb R:|x|^m<\delta\}\right)^{(\delta^\varepsilon)}\right),
\]

where \(A^{(r)}=\{x\in\mathbb R:\operatorname{dist}(x,A)<r\}\) is the open Euclidean \(r\)-neighbourhood. There are constants \(c,C,\delta_0>0\), depending at most on \(m,\varepsilon\), such that for every \(0<\delta<\delta_0\),

\[
c\,\delta^{s\min\{\varepsilon,1/m\}}\le F_{m,\varepsilon}(\delta)\le C\,\delta^{s\min\{\varepsilon,1/m\}}.
\]

Consequently, the exact largest exponent \(\beta\) for which \(F_{m,\varepsilon}(\delta)\le C_\beta\delta^\beta\) holds for all sufficiently small \(\delta\) is

\[
\beta_*(m,\varepsilon)=\frac{\log 2}{\log 3}\min\!\left\{\varepsilon,\frac1m\right\}.
\]

## Assumptions and scope

The measure is exactly the equal-weight middle-third Cantor measure, with no separation or weight variation beyond its standard construction. The neighbourhood is taken in the ambient line \(\mathbb R\), and \(m\) is a positive integer. The claim is a sharp model bound for a thickened analytic sublevel set; it is not a general quantitative Łojasiewicz theorem and makes no direct claim about Fourier decay rates.

## Proof

For \(0<\delta<1\), the sublevel set \(\{x:|x|^m<\delta\}\) is the interval \((-\delta^{1/m},\delta^{1/m})\). Its open \(\delta^\varepsilon\)-neighbourhood is the interval

\[
(-R_\delta,R_\delta),\qquad R_\delta=\delta^{1/m}+\delta^\varepsilon.
\]

Writing \(a=\min\{\varepsilon,1/m\}\), the larger of the two powers is \(\delta^a\), so

\[
\delta^a\le R_\delta\le2\delta^a.
\]

The leftmost level-\(n\) Cantor cylinder is \([0,3^{-n}]\) and has \(\mu\)-mass \(2^{-n}\). If \(3^{-(n+1)}\le r\le3^{-n}\), monotonicity gives

\[
2^{-(n+1)}\le\mu([0,r])\le2^{-n},\qquad
2^{-(n+1)}\le r^s\le2^{-n},
\]

because \(3^{-s}=1/2\). Thus \(\mu([0,r])\asymp r^s\) for all sufficiently small \(r>0\). The measure is supported in \([0,1]\) and has no atoms, hence

\[
F_{m,\varepsilon}(\delta)=\mu([0,R_\delta])\asymp R_\delta^s\asymp\delta^{sa}.
\]

This proves both bounds. If \(\beta\le sa\), the upper bound implies \(F_{m,\varepsilon}(\delta)\le C\delta^\beta\) for \(0<\delta<\min\{\delta_0,1\}\). If \(\beta>sa\), the lower bound gives

\[
\frac{F_{m,\varepsilon}(\delta)}{\delta^\beta}\ge c\,\delta^{sa-\beta}\longrightarrow\infty
\quad\text{as }\delta\downarrow0,
\]

so no constant \(C_\beta\) can make that estimate hold. Therefore \(\beta_*=sa\), including the boundary case \(\varepsilon=1/m\).

## Verification

The argument is analytic and uses only exact cylinder masses and interval inclusions; no numerical experiment is used as proof. The comparison \(\delta^a\le\delta^{1/m}+\delta^\varepsilon\le2\delta^a\) holds for all \(0<\delta<1\). The cylinder estimate handles every sufficiently small radius, not only triadic radii. The lower bound explicitly rules out every exponent above \(\beta_*\), while the upper bound attains \(\beta_*\) itself.

## Relationship to prior work

Banaji and Yu's qualitative study of nonlinear images of self-similar measures proves a uniform measure Łojasiewicz-type estimate with some positive exponent for compact families of nonzero analytic maps, and identifies quantitative dependence on non-degeneracy as a direction for further work. The formula here is an exact one-dimensional sharpness benchmark for the monomial family under the standard Cantor measure, rather than a replacement for that general theorem. Their earlier quantitative Fourier-decay paper studies pushforward Fourier exponents under curvature and related hypotheses; it does not state the exact thickened-sublevel exponent computed here. The inspected sources do not establish a general formula for arbitrary measures or analytic functions.

## Limitations

The result is confined to one measure and the monomials \(x\mapsto x^m\). It does not determine the optimal exponent for a general self-similar measure, for zeros away from a point with known local scaling, or for multivariable analytic maps. Its contribution is the exact sharp cap in this canonical model; the proof is elementary and should not be read as a broad Fourier-decay theorem.

## References

1. A. Banaji and H. Yu, “Fourier transform of nonlinear images of self-similar measures: qualitative aspects,” arXiv:2606.09743v2, first submitted 8 June 2026, especially Theorem 3.7 and Section 8. https://arxiv.org/abs/2606.09743
2. A. Banaji and H. Yu, “Fourier transform of nonlinear images of self-similar measures: quantitative aspects,” arXiv:2503.07508v2, especially Theorem 1.1 and Section 5.4. https://arxiv.org/abs/2503.07508
3. J. E. Hutchinson, “Fractals and self similarity,” Indiana University Mathematics Journal 30 (1981), 713–747.
