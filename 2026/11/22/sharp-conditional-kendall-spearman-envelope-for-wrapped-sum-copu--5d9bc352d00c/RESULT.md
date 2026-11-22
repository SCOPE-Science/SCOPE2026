# Sharp conditional Kendall–Spearman envelope for wrapped-sum copulas

## Finding
Let \(f\) be any Lebesgue probability density on \([0,1]\), and let the bivariate copula \(C_f\) have density \(c_f(u,v)=f((u+v)\bmod 1)\). Write \(r=\rho_S(C_f)\) and \(t=\tau(C_f)\) for population Spearman rho and Kendall tau. For each fixed \(-1<r<1/2\), the **sharp supremum of \(t\) over all such densities with \(\rho_S(C_f)=r\)** is

\[
T(r)=\begin{cases}
(2r-r^2)/3, & -1<r\le 0,\\
\tfrac23\left(\sqrt{1-2r}-(1-2r)\right),&0\le r<1/2.
\end{cases}
\]

For \(0\le r<1/2\), equality holds, uniquely up to null sets, at the centered uniform generator
\[ f_r(x)=\frac{1}{2a_r}\mathbf 1_{[1/2-a_r,\,1/2+a_r]}(x),\qquad a_r=\frac{\sqrt{1-2r}}{2}. \]
For \(-1<r<0\), the displayed bound is strict for every density but is a supremum approached by explicitly given densities with **exactly the prescribed** \(r\). Thus the upper envelope changes from an unattained atom-limit to an attained single-interval uniform generator at \(r=0\).

## Assumptions and scope
The only hypotheses are that \(f\) is measurable, nonnegative, and \(\int_0^1f(x)\,dx=1\). No smoothness, symmetry, or boundedness is assumed. The copula is two-dimensional, with the unreflected wrapped **sum** (not the wrapped difference); its margins are uniform by periodic integration. The coefficients are population concordance coefficients, not sample estimators. Every real \(r\in(-1,1/2)\) is feasible: the displayed positive-branch generators achieve \(r\ge0\), and the fixed-moment mixtures constructed below achieve all \(r<0\). Both range endpoints are excluded for densities. No lower Kendall envelope or full two-dimensional attainable \((r,t)\)-region is asserted.

## Proof
**1. Reduce concordance to a fixed-moment CDF problem.** Let \(X,X'\) be independent with density \(f\); let \(F\) be its continuous CDF, \(m=\int_0^1F(x)\,dx\), \(q=\mathbb E[(X-1/2)^2]\), and \(J(F)=\int_0^1(F(x)-m)^2\,dx\). The exact rank-coefficient identities established for this family by Lalancette and Zimmerman (2025), Propositions 4 and 5, give
\[r=6\mathbb E[X(1-X)]-1=\tfrac12-6q,\]
\[t=4\mathbb E[X(1-X)]+2\mathbb E|X-X'|-4\operatorname{Var}(X)-1.\]
Since \(\mathbb E|X-X'|=2\int_0^1F(1-F)\,dx\), \(m=1-\mathbb EX\), and \(\operatorname{Var}(X)=q-(\mathbb EX-1/2)^2\), direct expansion yields the exact variational identity
\[\boxed{\quad t=1-8q-4J(F).\quad}\]
Integration by parts also yields
\[q=\tfrac14-2\int_0^1(x-1/2)F(x)\,dx.\]
Consequently fixing \(r\) is equivalent to fixing \(q=(1/2-r)/6\), and maximizing \(t\) is equivalent to minimizing \(J\) over continuous nondecreasing CDFs with the corresponding moment constraint.

**2. Nonpositive rho.** For \(-1<r\le0\) set \(k=1+r\in(0,1]\). Since \(\int_0^1(x-1/2)\,dx=0\), the fixed-moment equation gives
\[\int_0^1(x-1/2)(F(x)-m)\,dx=k/12.\]
Cauchy–Schwarz and \(\int_0^1(x-1/2)^2dx=1/12\) show \(J(F)\ge k^2/12\). Substitution in the boxed identity gives \(t\le(2r-r^2)/3\). Equality requires \(F(x)-m=k(x-1/2)\) for almost every \(x\). For a continuous CDF with \(F(0)=0\) and \(F(1)=1\), this identity forces \(k=1\), hence \(r=0\), \(m=1/2\), and \(F(x)=x\). Thus equality holds only at independence when \(r=0\), and is impossible for negative \(r\).

To prove sharpness **at exactly each** negative \(r\), fix \(q=(1/2-r)/6\in(1/12,1/4)\). For small \(\varepsilon\in(0,1/2)\) put
\[q_{\varepsilon}=\tfrac14-\tfrac{\varepsilon}{2}+\tfrac{\varepsilon^2}{3},\qquad
w_{\varepsilon}=\frac{q-1/12}{q_{\varepsilon}-1/12}\in(0,1),\]
\[f_{\varepsilon}(x)=1-w_{\varepsilon}+\frac{w_{\varepsilon}}{2\varepsilon}\bigl(\mathbf1_{[0,\varepsilon]}(x)+\mathbf1_{[1-\varepsilon,1]}(x)\bigr).\]
By linearity of the second centered moment, \(\mathbb E_{f_\varepsilon}[(X-1/2)^2]=q\) exactly, so each density has Spearman rho exactly \(r\). As \(\varepsilon\downarrow0\), its CDF converges almost everywhere in \((0,1)\) to \(F_*(x)=(-r/2)+(1+r)x\), which is the interior CDF of a probability measure with uniform bulk mass \(1+r\) and endpoint atoms \(-r/2\) each. Dominated convergence yields \(J(F_\varepsilon)\to(1+r)^2/12\), and therefore \(t(f_\varepsilon)\to(2r-r^2)/3\). The limiting atoms are **not** asserted to be an admissible density.

**3. Positive rho.** If \(0<r<1/2\), write \(a=\sqrt{3q}=\sqrt{1-2r}/2\in(0,1/2)\). Let \(G\) be the CDF of \(\mathrm{Unif}(1/2-a,1/2+a)\): it is zero below \(1/2-a\), increases linearly from zero to one across the interval, and is one above \(1/2+a\). Its centered second moment is \(a^2/3=q\), its CDF mean is \(1/2\), and direct integration gives \(J(G)=1/4-a/3\).

For any other feasible CDF \(F\), set \(\delta=F-G\) and \(\bar\delta=\int_0^1\delta\). The equal-moment condition implies \(\int_0^1(x-1/2)\delta(x)\,dx=0\), while expansion of the centered squared norms gives
\[J(F)-J(G)=2\int_0^1(G(x)-1/2)\delta(x)\,dx +\int_0^1(\delta(x)-\bar\delta)^2\,dx.\]
Use the moment constraint to subtract \((x-1/2)/(2a)\) inside the first integral. The function
\[R_a(x)=G(x)-1/2-\frac{x-1/2}{2a}\]
is zero in the middle interval, positive to its left, and negative to its right. On the left \(\delta=F\ge0\), while on the right \(\delta=F-1\le0\). Hence \(\int R_a\delta\ge0\), proving \(J(F)\ge J(G)\). If equality occurs, the nonnegative second integral forces \(\delta\) to be constant almost everywhere; continuity and the CDF endpoint conditions make that constant zero. Thus \(G\) is the unique minimizer. The resulting \(t=1-8a^2/3-4(1/4-a/3)=(4a-8a^2)/3\) simplifies to the positive branch displayed in Finding. The shared boundary \(r=0\) follows by the Cauchy equality case in step 2, completing all quantifiers and endpoints.

## Verification
The attached standard-library script `check.py` computes the exact rational \(q\), \(J\), \(r\), and \(t\) for piecewise-constant generators by integrating each CDF segment, and checks centered-uniform equality, prescribed-rho negative approximate optimizers, and thousands of independent partitioned-density comparisons. It completed with `PASS: 4444 exact-rational/randomized consistency assertions.` The positive-branch general inequality is also checked numerically against its algebraic square-root expression; the equality and negative-branch checks use exact fractions. These finite tests support rather than establish the universal inequalities; their proofs are steps 2–3 above. Run locally with `python check.py`.

As a diagnostic, at \(r=-1/2\) the sharp upper supremum is \(-5/12\) and is not attained, while at \(r=3/8\) the centered uniform on \([1/4,3/4]\) attains \(t=1/6\), a global extremum already known from the 2025 paper.

## Relationship to prior work
Lalancette and Zimmerman (2022) introduced the wrapped-sum copulas and their generator construction. Their 2025 follow-up explicitly derived the separate rho and tau formulas (Propositions 4–5), the **unconditional** Kendall tau maximum \(1/6\) and its centered-uniform maximizer (Proposition 6), and the identity \(\xi=2r-3t\ge0\) for directional rank dependence (Proposition 7 and Corollary 2). Thus the bound \(t\le2r/3\), including its implication at \(r=0\), is **already contained in that prior work**. The present claim is instead the **sharp conditional upper envelope at every fixed Spearman rho**, with its two exact formulas, all equality cases, and strictly unattained negative-rho branch. Neither the separate marginal ranges nor the bound \(t\le2r/3\) yields these sharp fixed-rho bounds: at each nonzero \(r\) the new upper envelope is strictly below \(2r/3\). The unrestricted exact Kendall–Spearman region of Schreyer, Paulin and Trutschnig concerns all copulas, not this constrained density family. Exact regions for extreme-value copulas concern a structurally different class. An absence of matching records is not proof of absolute publication novelty.

## Limitations
The result covers only the unreflected bivariate wrapped-sum copula family, not all signatures, all copulas, higher dimensions, or the lower conditional envelope. The negative-rho supremum requires a singular limiting generator and is not attained by any allowed Lebesgue density. Bibliographic coverage is bounded and residual priority uncertainty remains for unindexed literature and equivalent formulations under other names. The proof assumes the published exact rank formulas; those formulas' derivations were also inspected in the 2025 primary full text.

## References
- Michaël Lalancette and Robert Zimmerman (2022), *A new family of smooth copulas with arbitrarily irregular densities*, arXiv:2204.04336, first posted 9 April 2022. https://arxiv.org/abs/2204.04336
- Michaël Lalancette and Robert Zimmerman (2025), *A Tractable Family of Smooth Copulas with Rotational Dependence: Properties, Inference, and Application*, arXiv:2509.26635, Propositions 4–7, Corollary 2. https://arxiv.org/html/2509.26635v1
- Manuela Schreyer, Roland Paulin and Wolfgang Trutschnig (2015), *On the exact region determined by Kendall's tau and Spearman's rho*, arXiv:1502.04620. https://arxiv.org/abs/1502.04620
- N. Kamnitui, C. Genest, P. Jaworski and W. Trutschnig (2019), *On the size of the class of bivariate extreme-value copulas with a fixed value of Spearman's rho or Kendall's tau*, Journal of Mathematical Analysis and Applications 472, 920–936. https://doi.org/10.1016/j.jmaa.2018.11.057
