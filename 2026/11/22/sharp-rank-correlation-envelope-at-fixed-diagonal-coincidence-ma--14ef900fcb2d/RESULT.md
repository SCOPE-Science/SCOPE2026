# Sharp rank-correlation envelope at fixed diagonal coincidence mass in max-quotient copulas

## Finding

Let \(f:(0,1)\to[0,1]\) be Lebesgue measurable, and define the max-quotient expression
\[
C_f(u,v)=uv\left[1+\int_{\max(u,v)}^1\frac{f(t)}{t^2}\,dt\right],\quad 0<u,v\le1,
\]
with zero boundary values on the axes. Restrict attention to precisely those \(f\) for which \(C_f\) is a copula. For its associated uniform-marginal random pair \((U,V)\), put \(p=\Pr(U=V)\) and \(\rho=\rho_S(U,V)\), Spearman's population rank correlation.

**Theorem (exact two-statistic region and rigidity).** As \(f\) ranges over all such generators, the set of attainable pairs \((p,\rho)\) is exactly
\[
\mathcal R=\bigl\{(p,\rho):0\le p\le1,\quad p^2\le\rho\le1-(1-p)^3\bigr\}.
\]
Every point of this closed region is attained. For each \(0<p<1\), the unique (up to Lebesgue-null sets) generator attaining the lower bound, with \(a=\sqrt p\), is
\[
f_{\mathrm{lo}}(t)=a\,\mathbf1_{(0,a)}(t).
\]
The unique upper-bound generator, with \(b=1-p\), is
\[
f_{\mathrm{hi}}(t)=\mathbf1_{(b,1)}(t).
\]
At \(p=0\) and \(p=1\), the only generators up to null sets are respectively \(f=0\) and \(f=1\). The lower-bound proof includes an exact nonnegative deficit identity, not only an inequality.

## Assumptions and scope

The word *copula* means a two-increasing bivariate distribution function on \([0,1]^2\) with both margins uniform. The generator is any Lebesgue-measurable function \(f:(0,1)\to[0,1]\); no continuity or differentiability of \(f\) is imposed. All equalities and uniqueness of generators are modulo Lebesgue-null sets. The integral defining \(C_f\) is interpreted as an ordinary Lebesgue integral for positive lower endpoint, and the copula expression has its continuous extension to the axes.

For \(0<t\le1\) define the absolutely continuous-on-compact-subintervals function
\[
k(t)=t\left[1+\int_t^1\frac{f(s)}{s^2}\,ds\right],
\qquad
h(t)=k'(t)=1+\int_t^1\frac{f(s)}{s^2}\,ds-\frac{f(t)}{t}\quad\text{a.e.}
\]
A useful exact criterion is that \(C_f\) is a copula **if and only if** \(h(t)\ge0\) almost everywhere. This criterion is within the displayed fixed max-quotient family, not a claim about all bivariate copulas or arbitrary quotient functions.

## Proof

**1. Positive measure and the admissibility criterion.** Write \(C_f(u,v)=\min(u,v)k(\max(u,v))\). The identities \(k(1)=1\) and \(f(t)=k(t)-tk'(t)\) hold almost everywhere. If \(h\ge0\), introduce a bivariate measure with ordinary density \(h(\max(u,v))\) off the diagonal and one-dimensional density \(f(t)\,dt\) at the diagonal point \((t,t)\). Both component measures are nonnegative. Fix \(u\in(0,1)\). Its first marginal density equals
\[
u h(u)+\int_u^1h(v)\,dv+f(u)
=u k'(u)+k(1)-k(u)+k(u)-u k'(u)=1.
\]
The other marginal is also uniform by symmetry. Moreover, for \(0<u<v\le1\), the conditional probability at the horizontal coordinate \(u\) that the vertical coordinate does not exceed \(v\) is
\[
u h(u)+f(u)+\int_u^v h(t)\,dt=k(v).
\]
Integrating in \(u\) produces the joint CDF \(u k(v)=C_f(u,v)\); symmetry deals with \(u>v\). Thus \(C_f\) is a copula. Conversely, if \(C_f\) is a copula, its mixed distributional derivative off the diagonal has Lebesgue density \(k'(\max(u,v))=h(\max(u,v))\), which must be nonnegative almost everywhere. This proves necessity and sufficiency, including nonsmooth generators.

The preceding decomposition also shows
\[
p=\Pr(U=V)=\int_0^1 f(t)\,dt.
\]
Fubini's theorem and \(\int_{[0,t]^2}uv\,du\,dv=t^4/4\) give
\[
\rho=12\int_0^1\int_0^1(C_f(u,v)-uv)\,du\,dv
=3\int_0^1 t^2 f(t)\,dt.
\]
Tonelli's theorem applies to the nonnegative integrand.

**2. The sharp upper bound.** Given \(0<p<1\), put \(b=1-p\) and \(f_{\mathrm{hi}}(t)=\mathbf1_{(b,1)}(t)\). Its associated function \(k\) equals \(t/b\) on \((0,b)\) and \(1\) on \((b,1)\), hence \(h=1/b\) on \((0,b)\) and \(0\) on \((b,1)\). It is admissible, with \(p=1-b\) and \(\rho=1-b^3\). For any other admissible \(f\) with the same \(p\), mass equality yields
\[
\rho(f_{\mathrm{hi}})-\rho(f)
=3\int_0^1(t^2-b^2)\bigl(\mathbf1_{(b,1)}(t)-f(t)\bigr)\,dt\ge0.
\]
The integrand is pointwise nonnegative on both sides of \(b\), using \(0\le f\le1\). Equality forces \(f=f_{\mathrm{hi}}\) almost everywhere.

**3. A sharp lower-bound deficit identity.** For \(a\in(0,1)\), let \(w_a(t)=4t(a^2-t^2)\) for \(0<t<a\). This weight is strictly positive there and satisfies \(\int_0^a w_a(t)\,dt=a^4\). Substitute the displayed definition of \(h\), apply Tonelli/Fubini (or separate nonnegative terms), and simplify to obtain the **exact identity**
\[
\begin{aligned}
a^4+\rho-2a^2p
&=\int_0^a4t(a^2-t^2)h(t)\,dt\\
&\quad+\int_a^1\frac{(t^2-a^2)(3t^2+a^2)}{t^2}\,f(t)\,dt.
\end{aligned}
\]
For explicit verification, interchanging the integrals in the first term on the right gives the expansion
\[
\int_0^a w_a(t)h(t)\,dt
=a^4+\int_0^a(3t^2-2a^2)f(t)\,dt
+\int_a^1\frac{a^4}{t^2}f(t)\,dt.
\]
The missing contribution for \(t>a\) is exactly \((t^2-a^2)(3t^2+a^2)f(t)/t^2\). These expressions are finite because \(f\le1\) and the relevant integrations avoid a nonintegrable lower-endpoint singularity.

Now choose \(a=\sqrt p\). Since \(a^4+\rho-2a^2p=\rho-p^2\), nonnegativity of \(h\) and \(f\) proves \(\rho\ge p^2\). Equality forces \(h=0\) almost everywhere on \((0,a)\) and \(f=0\) almost everywhere on \((a,1)\). Consequently \(k(t)=k(a)=a\) for almost every \(t<a\), because \(f=0\) above \(a\) implies \(k(a)=a\). Thus \(f=k-tk'=a\) almost everywhere below \(a\). Conversely, \(f_{\mathrm{lo}}(t)=a\mathbf1_{(0,a)}(t)\) gives \(k(t)=a\) for \(t<a\) and \(k(t)=t\) for \(t>a\); its \(h\) is \(0\) below \(a\) and \(1\) above \(a\). It is admissible with \(p=a^2\) and \(\rho=a^4=p^2\). This proves sharpness and uniqueness.

**4. Exhausting the region and endpoints.** For fixed \(p\in(0,1)\), each \(f_\lambda=(1-\lambda)f_{\mathrm{lo}}+\lambda f_{\mathrm{hi}}\), \(0\le\lambda\le1\), lies in \([0,1]\), preserves \(p\), and has \(h_\lambda=(1-\lambda)h_{\mathrm{lo}}+\lambda h_{\mathrm{hi}}\ge0\). Its Spearman coefficient is exactly \((1-\lambda)p^2+\lambda[1-(1-p)^3]\), so every intermediate value occurs. At \(p=0\) (respectively \(p=1\)) the condition \(0\le f\le1\) and \(\int f=p\) forces \(f=0\) (respectively \(f=1\)) almost everywhere, producing independence (respectively comonotonicity) and \(\rho=0\) (respectively \(\rho=1\)). The theorem follows.

## Verification

The accompanying standalone `check.py` runs exact SymPy identity checks for the weight integral, the sharp-deficit kernel, both generators, their mass and rank integrals, the uniform-generator deficit identity, and rational-parameter mixture examples. The exact symbolic checks passed. These finite examples are supporting diagnostics; all-parameter validity and sharpness follow from the analytic proof above, not from enumeration.

As a concrete calibration, at \(p=1/4\) the attainable interval is \([1/16,37/64]\), while the Fréchet-mixture generator \(f(t)=1/4\) gives \(\rho=1/4\). Thus equal exact diagonal coincidence mass does not determine the strength of rank concordance even within this restricted natural family.

## Relationship to prior work

Cuadras (2024, Definition 3, Theorem 1 and Proposition 4) establishes the max-quotient construction, its split into off-diagonal and diagonal densities, and the formula \(p=\int f\). Durante (2007, Theorem 2.1, Example 3 and Proposition 3.4) characterizes a broad class \(C(u,v)=\min(u,v)k(\max(u,v))\), gives individual rank-correlation formulas, and exhibits the ordinal-sum family containing the **upper extremizer** constructed above. These are pre-existing results, not claimed as new. The finding here is the **joint sharp range at fixed diagonal mass**, the **lower extremizer and nonnegative deficit certificate**, and **complete boundary uniqueness and attainability**. The upper extremizer itself is an already-known copula; its optimality at a fixed diagonal mass is the additional statement.

Cuadras (2015) concerns the more general diagonal expansion and continuous canonical extensions; its abstract was checked but its full journal text could not be inspected. No accessible compared result has been found stating or implying the displayed joint envelope. This limited comparison is not proof of global historical novelty.

## Limitations

The inequalities describe the max-quotient family with \(0\le f\le1\) and nonnegative off-diagonal density. They are **not** asserted for all copulas; outside this family there may be different dependence/collision tradeoffs. Uniqueness is only modulo null sets. No estimation, finite-sample confidence procedure, robustness bound beyond the displayed deficit, or independent external validation is established. Historical originality remains subject to fuller examination of inaccessible material and broader literature.

## References

1. C. M. Cuadras, “On Bivariate Distributions with Singular Part,” *Axioms* **13** (2024), 433, first published 27 June 2024, https://doi.org/10.3390/axioms13070433 ; https://www.mdpi.com/2075-1680/13/7/433 .
2. F. Durante, “A new family of symmetric bivariate copulas,” *Comptes Rendus Mathématique* **344** (2007), 195–198, https://doi.org/10.1016/j.crma.2006.12.004 ; open text https://www.numdam.org/item/10.1016/j.crma.2006.12.004.pdf .
3. C. M. Cuadras, “Contributions to the diagonal expansion of a bivariate copula with continuous extensions,” *Journal of Multivariate Analysis* **139** (2015), 28–44, https://doi.org/10.1016/j.jmva.2015.02.015 (abstract inspected; full text unavailable during this review).
