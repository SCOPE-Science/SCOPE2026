# A reentrant sharp variation-error transition for the three-bit biased Ehrenfest semigroup

## Finding

Consider a system of three independently refreshed Bernoulli bits with common equilibrium success probability \(0<p<1\) and retention parameter \(0\le\rho<1\). On the four possible counts \(k\in\{0,1,2,3\}\), let \(P_{p,\rho}\) be the induced transition operator and \(\mu_p(k)=\binom3k p^k(1-p)^{3-k}\). Put \(V(f)=\sum_{k=0}^{2}|f(k+1)-f(k)|\) and
\[
C(p,\rho)^2=\sup_{V(f)>0}\frac{\|(I-P_{p,\rho})f\|_{L^2(\mu_p)}^2}{V(f)^2}.
\]
The exact sharp value is \(C(p,\rho)^2=\max\{F_1,F_2,F_3\}\), with the explicit polynomials below. Every nonconstant extremizer, up to nonzero scaling and addition of a constant, is one of the single thresholds \(h_j(k)={\bf1}_{\{k\ge j\}}\) for which \(F_j=C(p,\rho)^2\).

There is a **reentrant optimal-threshold region**. For \(p\le1/2\), only \(h_1\) and \(h_2\) can be optimal. Define
\[
 B(p,\rho)=3p^2+2p-1+p^2\left[(1+\rho+\rho^2)^2-\frac{2-3p}{1-p}(1+\rho)^2\right],
\]
and \(p_0=(\sqrt{17}-3)/4\), \(p_1=2\cos(4\pi/9)\), and \(p_*\) the unique number in \((p_1,1/2)\) for which \(\min_{0\le\rho\le1}B(p_*,\rho)=0\). Numerical values are
\[
p_0=0.280776406404415\ldots,\quad p_1=0.347296355333861\ldots,\quad p_*=0.350477911893407\ldots.
\]
For \(p_1<p<p_*\), the polynomial \(B(p,\cdot)\) has exactly two simple roots \(0<\rho_-(p)<\rho_+(p)<1\). The uniquely norming jump is \(h_2\) for \(0\le\rho<\rho_-\) and \(\rho_+<\rho<1\), but \(h_1\) for \(\rho_-<\rho<\rho_+\); both threshold types norm at the crossing values. Thus the optimizer returns to its initial form as retention increases. At the unique critical pair \((p_*,\rho_*)\), \(\rho_*=0.205490953240252\ldots\), these two switches coalesce tangentially. In particular, at the exact rational bias \(p=87/250\), there are two switches (approximately \(\rho_-=0.026389419722758\), \(\rho_+=0.362890585296152\)). For \(p>1/2\) the complete statement follows by exchanging zeros and ones, with \(h_j\) replaced by \(h_{4-j}\).

The remaining cases for \(0<p\le1/2\) are: \(h_1\) alone for \(p\le p_0\); one interior switch from \(h_1\) to \(h_2\) for \(p_0<p<p_1\); at \(p=p_1\), a tie at \(\rho=0\) followed by an \(h_1\)-then-\(h_2\) switch; at \(p=p_*\), \(h_2\) alone except for the unique tangential tie; and \(h_2\) alone for \(p>p_*\) through \(p=1/2\). All these statements concern \(0\le\rho<1\); at \(\rho=1\) the defect vanishes identically and the extremizer classification changes.

## Assumptions and scope

Fix exactly three bits \(X_i\in\{0,1\}\). Conditional on their present values, each coordinate independently remains unchanged with probability \(\rho\), and with complementary probability it is redrawn independently from \(\mathrm{Bernoulli}(p)\). The count process is Markov and reversible under \(\mathrm{Binomial}(3,p)\). Real signals \(f\) are defined on \(\{0,1,2,3\}\), with unweighted adjacent variation. All sharp norms use the equilibrium-weighted \(L^2\) output and the **identity-minus-transition** operator, not a mixing-distance or noise-stability quotient. The time parameter of the associated continuous semigroup is \(t=-\log\rho\) when \(0<\rho<1\).

Write \(v=p(1-p)\) and \(w_m=(1-\rho^m)^2\), for \(m=1,2,3\). Then the exact formulas are
\[
\begin{aligned}
F_1&=3v(1-p)^4w_1+3v^2(1-p)^2w_2+v^3w_3,\\
F_2&=12v^3w_1+3v^2(1-2p)^2w_2+4v^3w_3,\\
F_3&=3vp^4w_1+3v^2p^2w_2+v^3w_3.
\end{aligned}
\]

## Proof

**(1) Sharp reduction and equality.** Every real count signal has the exact decomposition \(f(k)=f(0)+\sum_{j=1}^3d_jh_j(k)\), where \(d_j=f(j)-f(j-1)\) and \(V(f)=\sum|d_j|\). Since \(P_{p,\rho}\mathbf1=\mathbf1\), the triangle inequality gives
\[
\|(I-P_{p,\rho})f\|_2\le\sum_j|d_j|\,\|(I-P_{p,\rho})h_j\|_2\le V(f)\max_j\sqrt{F_j}.
\]
Each threshold attains its own \(F_j\). The three threshold residues are linearly independent: on the quotient of functions by constants, \(P_{p,\rho}\) has eigenvalues \(\rho,\rho^2,\rho^3<1\), so \(I-P_{p,\rho}\) is invertible there, while the threshold classes form a basis. Strict convexity of the Hilbert norm rules out an extremizer containing two nonzero increments, even when their individual norms tie.

**(2) Exact spectral identities.** With \(\xi_i=X_i-p\), distinct products \(\prod_{i\in S}\xi_i\) are orthogonal, with squared norms \(v^{|S|}\), and are multiplied by \(\rho^{|S|}\) under the refresh operator. Expand the three thresholds on the product cube:
\[
\begin{aligned}
h_1&=1-\prod_{i=1}^3(1-X_i),\\
h_2&=X_1X_2+X_1X_3+X_2X_3-2X_1X_2X_3,\\
h_3&=X_1X_2X_3.
\end{aligned}
\]
The respective squared Fourier masses at levels \(1,2,3\) are exactly the coefficients of \(w_1,w_2,w_3\) in \(F_1,F_2,F_3\). This establishes the displayed formulas. For \(p<1/2\), \(F_1>F_3\) because the level-one and level-two coefficients of \(F_1\) strictly exceed those of \(F_3\), and all \(w_m>0\). At \(p=1/2\), they tie, but \(F_2>F_1\).

**(3) Difference polynomial and convexity.** Direct factoring gives
\[
F_2-F_1=3p(1-p)^3(1-\rho)^2 B(p,\rho).
\]
Put \(S=1+\rho+\rho^2\), \(T=1+\rho\), and \(a=(2-3p)/(1-p)\). For \(0<p\le1/2\), \(1\le a<2\), \(S\ge T\) and \(T^2\le4\). Hence
\[
\begin{aligned}
\partial_p B&=2+6p+2p(S^2-aT^2)+p^2T^2/(1-p)^2\ge2-2p>0,\\
\partial_{\rho\rho}B&=2p^2[(1+2\rho)^2+2S-a]>0.
\end{aligned}
\]
For \(p<1/2\), \(\partial_\rho B(p,0)=2p^2(1-a)<0\), while \(\partial_\rho B(p,1)=2p^2(9-2a)>0\). Thus \(B(p,\cdot)\) has one strict interior minimum. Its endpoint values are
\[
B(p,0)=\frac{p^3-3p+1}{p-1},\qquad B(p,1)=\frac{2p^2+3p-1}{1-p}.
\]
The respective unique zeroes in \((0,1/2)\) are \(p_1\) and \(p_0\), with \(p_0<p_1\). The strict pointwise increase in \(p\) implies the minimum is strictly increasing in \(p\); it is negative at \(p_1\) (the derivative at \(\rho=0\) is negative) and positive at \(1/2\). Hence there is exactly one \(p_*\), and strict convexity gives all of the stated zero patterns and norming jumps. The complementary-bit isometry \((p,k)\mapsto(1-p,3-k)\) proves the reflected classification.

**(4) Minimality of three bits for reentry.** With two bits, the only thresholds are \(1_{\{k\ge1\}}\) and \(1_{\{k\ge2\}}\). Their level-two Fourier masses agree, while for \(p<1/2\) the level-one mass of the first is strictly larger. Therefore no switching is possible for two bits. Three bits are the first count model in this family allowing two noise-dependent reversals.

## Verification

Run the standalone `check.py` with the Python 3 standard library. It forms the exact rational three-bit transition matrices and independently verifies the spectral formulas, the factorization and the symmetric reflection on a rational parameter grid; it checks strict rational sign witnesses for the two-switch regime and checks numerical enclosures for the unique critical pair. The proof above, not the finite checker grid, establishes the statements for every real bias and retention parameter.

## Relationship to prior work

The Bernoulli composition-chain construction and Krawtchouk eigenstructure are classical; see Diaconis and Griffiths (2012, 2013). Bouyrie (2014) develops noise-stability and influence bounds in both balanced and biased discrete cubes. Their inspected statements concern spectral representation, mixing, hypercontractive estimates and influences, rather than the exact four-state variation-to-\(L^2\) identity-residual norm and the three-part reentrant optimizer phase diagram. The sharp threshold selection here does **not** follow merely from the eigenvalues: it uses the competing degree-wise masses of three specific count thresholds and a strictly convex quartic sign analysis.

## Limitations

The complete classification concerns precisely three independently refreshed, *identically biased* bits and real signals of unweighted adjacent count variation. It does not extend automatically to unequal refresh rates, other counts or hypercube edge variation. Numeric constants are approximations to uniquely defined algebraic quantities, not independently certified publication values. The 2012 primary paper was inspected at its public abstract and bibliographic record rather than in full; priority risk from inaccessible text or unindexed results remains. No independent mathematical audit has been performed.

## References

1. P. Diaconis and R. Griffiths, “Exchangeable pairs of Bernoulli random variables, Krawtchouck polynomials, and Ehrenfest urns,” *Australian & New Zealand Journal of Statistics* 54 (2012), 81–101, first publicly available online 2012-05-04. DOI: https://doi.org/10.1111/j.1467-842X.2012.00654.x
2. P. Diaconis and R. Griffiths, “An introduction to multivariate Krawtchouk polynomials and their applications,” arXiv:1309.0112, initially posted 2013-08-31. https://arxiv.org/abs/1309.0112
3. R. Bouyrie, “On quantitative noise stability and influences for discrete and continuous models,” arXiv:1401.7337, initially posted 2014-01-28. https://arxiv.org/abs/1401.7337
