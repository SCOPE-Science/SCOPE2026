# A sharp transverse-instability gap and a singular neutral-coupling cusp in a quadratic Cournot map

## Finding

Consider the symmetric two-firm bounded-rationality map
\[
F_{a,c,d,k}(x,y)=\bigl(x[1+k(a-(2+c)x-dy)],\ y[1+k(a-(2+c)y-dx)]\bigr),
\]
where \(a,k,c>0\), \(d\geq 0\), and \(ka=3\). The diagonal supports the full logistic map at parameter \(4\). Put \(s=2+c\) and \(\eta=s/(s+d)\). Along Lebesgue-almost every diagonal point in its invariant logistic interval, the transverse Lyapunov exponent exists and is exactly
\[
\Lambda_\perp(d)=
\begin{cases}
\log(2\eta),&0\le d\le s,\\
\log\!\left(2\left[1-\eta+\sqrt{1-2\eta}\right]\right),&d>s.
\end{cases}
\]
It is strictly positive at every \(d\geq0\) except the unique neutral coupling \(d=s\), where it vanishes. Its approach to neutrality is asymmetric:
\[
\Lambda_\perp(d)\sim \frac{s-d}{2s}\quad(d\uparrow s),
\qquad
\Lambda_\perp(d)\sim\sqrt{\frac{2(d-s)}s}\quad(d\downarrow s).
\]
The second limit is taken from \(d>s\). At \(d=s\), every nonzero iterate satisfies the exact ratio conservation \(x_{n+1}/y_{n+1}=x_n/y_n\) whenever both ratios are defined; the competition law acts by the same scalar on both firms.

In the economically specified substitute-products domain \(0\le d\le1\) and \(c>0\), the exact formula reduces to
\[
\boxed{\Lambda_\perp=\log\frac{2(2+c)}{2+c+d}>\log\frac43>0.}
\]
The infimum \(\log(4/3)\) is sharp and is approached as \(c\downarrow0\) and \(d=1\). It is not attained for strictly positive \(c\). Thus the fully chaotic synchronized state is linearly transversely unstable for almost every invariant-diagonal initial condition, with a universal strictly positive Lyapunov gap independent of \(a\) and \(k\) subject to \(ka=3\).

## Assumptions and scope

The map is treated as a polynomial map on \(\mathbb R^2\), and the physical output region is the positive quadrant where the iterates are nonnegative. The original economic model specifies \(a,k,c>0\) and \(d\in[0,1]\), representing substitutable products. The extension \(d>1\) is a mathematical positive-cross-coupling continuation, **not** an assertion about the economic parameter range. The principal exponent statement concerns the natural absolutely continuous invariant probability of the invariant diagonal's logistic-map restriction; it is not a claim for every diagonal orbit or for every off-diagonal orbit. In particular, periodic points and precritical orbits may have different or undefined time averages.

The invariant diagonal interval is \(0\le x=y\le 4/[k(s+d)]\). Define the normalized logistic coordinate \(u=k(s+d)x/4\) on the diagonal. The invariant probability for \(u\) has density \(\rho(u)=1/[\pi\sqrt{u(1-u)}]\) for \(0<u<1\). Its invariance and ergodicity follow from the standard conjugacy \(u=\sin^2(\pi t)\) with the doubling map on the circle. This is the natural logistic measure, not planar Lebesgue measure.

## Proof

**Step 1 (reduction and eigendirections).** On \(x=y=q\), direct substitution gives \(q'=q[4-k(s+d)q]\). With \(u=k(s+d)q/4\) this becomes \(u'=4u(1-u)\). The two symmetry eigendirections are \((1,1)\) and \((1,-1)\). Differentiating the **full** polynomial map before restricting to the diagonal gives eigenvalues
\[
\lambda_{\parallel}(q)=4-2k(s+d)q,
\quad \lambda_\perp(q)=4-2ksq=4(1-2\eta u).
\]
The eigendirections are fixed for every diagonal point. Hence the linearized transverse cocycle is scalar and its finite-time multiplier is exactly the product of these \(\lambda_\perp\) values, with no unaccounted matrix-orientation factor.

**Step 2 (existence of the exponent).** For \(0<\eta\le1\), the function \(\log|4(1-2\eta u)|\) has at most one logarithmic interior singularity and is integrable against \(\rho(u)\); it is also integrable at endpoints. Ergodicity and Birkhoff's theorem give the almost-everywhere limit
\[
\Lambda_\perp=\int_0^1\log|4(1-2\eta u)|\,\frac{du}{\pi\sqrt{u(1-u)}}.
\]
Setting \(u=(1-\cos\theta)/2\) gives \(\Lambda_\perp=\log4+\pi^{-1}\int_0^\pi\log|1-\eta+\eta\cos\theta|\,d\theta\).

**Step 3 (exact logarithmic integral).** The elementary Jensen cosine identity states, for \(A\ge0\) and \(B>0\),
\[
\frac1\pi\int_0^\pi\log|A+B\cos\theta|d\theta=
\begin{cases}
\log(B/2),&0\le A\le B,\\
\log\bigl((A+\sqrt{A^2-B^2})/2\bigr),&A>B.
\end{cases}
\]
For completeness: write \(\cos\theta=(z+z^{-1})/2\) on \(|z|=1\). After multiplying by \(z\), the integrand is the logarithm of the modulus of a quadratic polynomial \((B/2)z^2+Az+B/2\). Jensen's formula says its circle mean equals \(\log(B/2)\) plus the logs of the moduli of its roots outside the unit circle. When \(A\le B\), both roots have modulus one. When \(A>B\), the roots are negative reciprocal reals and the exterior root has modulus \((A+\sqrt{A^2-B^2})/B\). This proves the two formulas including the integrable double-root boundary. Apply with \(A=1-\eta\), \(B=\eta\), yielding the displayed piecewise \(\Lambda_\perp\).

**Step 4 (positivity and sharpness).** In \(d\le s\), \(\eta\ge1/2\), so \(\Lambda_\perp=\log(2\eta)\ge0\) with equality only for \(d=s\). If \(d>s\), then \(0<\eta<1/2\); because \(1-\eta+\sqrt{1-2\eta}>1/2\), the second expression is strictly positive. If \(0\le d\le1\) and \(s=2+c>2\), then \(\eta=s/(s+d)\ge s/(s+1)>2/3\), yielding the strict uniform gap. Along \(d=1\) and \(c\downarrow0\) the exponent tends to \(\log(4/3)\), proving the optimal infimum rather than merely a lower bound.

For the singular cusp, write \(d=s-\varepsilon\) and \(d=s+\varepsilon\). In the first case \(\Lambda_\perp=\log[2s/(2s-\varepsilon)]=\varepsilon/(2s)+O(\varepsilon^2)\). In the second case \(\eta=s/(2s+\varepsilon)\), \(\sqrt{1-2\eta}=\sqrt{\varepsilon/(2s+\varepsilon)}\), hence \(\Lambda_\perp=\sqrt{2\varepsilon/s}+O(\varepsilon)\). At exactly \(d=s\), the equations become \((x',y')=(x,y)[4-ks(x+y)]\), proving exact ray conservation wherever the ratios exist.

## Verification

Run `python checker.py` with Python 3, SymPy, and mpmath installed. Its symbolic calculations verify the diagonal reduction and both Jacobian eigendirections. Two hundred independently generated exact-rational parameter trials check the conjugacy and transverse multiplier. Eight independent high-precision logarithmic quadratures and one analytically handled boundary case (with the interior singularity split explicitly) agree with the stated closed forms, and exact rational cases check the physical parameter inequality. Output ends with `PASS symbolic eigendirections, 200 exact-rational trials, 8 independent quadratures, 1 analytic endpoint, physical sharp inequality`.

These finite checks are auxiliary. Birkhoff ergodicity and Jensen's integral identity, with the explicit proofs and assumptions above, support the infinite-time conclusion. No numerical sample establishes the infinitely many-orbit claim by itself.

## Relationship to prior work

Askar and Alshamrani (2024) introduce the same symmetric computed-quadratic-cost Cournot map, establish the diagonal logistic reduction, write transverse multipliers and the general transverse Lyapunov-exponent criterion, and study synchronization numerically. Their accessible complete text does not evaluate the maximal-chaos exponent as a closed function of \(c,d\), give a sharp uniform physical lower bound, or describe the exceptional mathematical neutral-coupling cusp.

Bischi, Stefanini and Gardini (1998) study a related linear-cost Cournot map with a fixed cross/self competition ratio \(1/2\). They define the same general type of transverse exponent and explicitly note its positivity at the full-chaos endpoint. This prior observation already covers the *qualitative* positive-exponent statement at that fixed ratio (corresponding here to the limiting \(c=0,d=1\)); the contribution here is the exact quantitative parameter law, the sharp physical gap for the positive quadratic-cost range, and the unique neutral-coupling cusp in the positive-cross-coupling continuation. We do not present the logistic conjugacy, the Jensen integral identity, or the Lyapunov-exponent criterion as new mathematical methods.

## Limitations

The theorem concerns **infinitesimal transverse perturbations** of almost every synchronized chaotic orbit. It does not establish a complete off-diagonal basin, global escape classification, or the measure of the synchronized set's basin. A positive generic transverse exponent is not an assertion that every synchronized periodic point repels transversely. Extended cross coupling \(d>1\) is purely mathematical, not part of the source's specified product-substitutability domain. The quadratic-logarithmic integral and ergodic facts are classical, so mathematical novelty is confined to their sharp model-specific consequences; an older unindexed exact formula remains a publication-priority risk. Independent validation has not been performed.

## References

1. S. S. Askar and A. M. Alshamrani, “Dynamic Analysis of a Simple Cournot Duopoly Model Based on a Computed Cost,” *Discrete Dynamics in Nature and Society* 2024, Article 9912671, first published March 25, 2024. DOI: https://doi.org/10.1155/2024/9912671. Full article including equations (7)–(9), (26)–(33) and appendix: https://onlinelibrary.wiley.com/doi/pdf/10.1155/2024/9912671.
2. G.-I. Bischi, L. Stefanini, and L. Gardini, “Synchronization, intermittency and critical curves in a duopoly game,” *Mathematics and Computers in Simulation* 44 (1998), 559–585. DOI: https://doi.org/10.1016/S0378-4754(97)00100-6. Full text: https://www.mdef.it/public/fileadmin/whoiswho/bischi/Selected_publications/Research_papers/BiSteGa98.pdf.
3. Classical tools: Birkhoff's ergodic theorem for the doubling map and Jensen's formula for the circular mean of the logarithm of a polynomial. These facts are used with proofs/definitions above, not claimed as new results.
