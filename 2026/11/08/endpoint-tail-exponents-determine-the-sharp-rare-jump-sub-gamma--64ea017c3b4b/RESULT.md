# Endpoint-tail exponents determine the sharp rare-jump sub-gamma correction

## Finding

Let \(Z\sim N(0,1)\), let \(N_\lambda\sim\operatorname{Pois}(\lambda)\), and let \((J_i)\) be independent copies of a nonnegative random variable \(J\), all independent. Fix \(\sigma>0\) and \(b>0\). Suppose \(J\le b\) almost surely and, for some \(\beta>0\) and \(C>0\),

\[
\Pr(J>b-u)=Cu^\beta(1+o(1))\qquad(u\downarrow0).
\]

Define the centered Gaussian--compound-Poisson law

\[
X_\lambda=\sigma Z+\sum_{i=1}^{N_\lambda}J_i-\lambda\mathbb E J,
\qquad V_\lambda=\sigma^2+\lambda\mathbb E J^2,
\]

and its **optimal variance-exact right sub-gamma scale**

\[
c_\lambda=\inf\left\{c\ge0:\log\mathbb E e^{tX_\lambda}\le
\frac{V_\lambda t^2}{2(1-ct)}\ \text{for all }0\le t<1/c\right\}.
\]

As \(\lambda\downarrow0\), write

\[
\delta_\lambda=\frac{\lambda\mathbb E J^2}{V_\lambda},\qquad
L_\lambda=\log(1/\delta_\lambda),\qquad
K=\frac{2C\,\Gamma(\beta+1)b^{\beta+2}}{\mathbb E J^2}.
\]

Then

\[
\boxed{\frac{b}{c_\lambda}=L_\lambda+(\beta+3)\log L_\lambda+1-\log K+o(1).}
\]

More precisely, every maximizer \(s_\lambda\) of the dimensionless variational objective defined below is interior for sufficiently small \(\lambda\) and satisfies

\[
\boxed{s_\lambda=L_\lambda+(\beta+3)\log L_\lambda-\log K+o(1).}
\]

No uniqueness of the maximizer is asserted or needed. An equivalent expansion of the scale is

\[
\frac{c_\lambda}{b}=\frac1{L_\lambda}-
\frac{(\beta+3)\log L_\lambda+1-\log K}{L_\lambda^2}
+o(L_\lambda^{-2}).
\]

Thus all such bounded-jump laws share the leading inverse-logarithmic decay, but the first logarithmic correction remembers the upper-endpoint power \(\beta\).

## Assumptions and scope

The statement is for a *fixed* jump law \(J\) with essential maximum \(b\), a fixed positive Gaussian variance \(\sigma^2\), and Poisson intensity \(\lambda\downarrow0\). The endpoint assumption has exponent \(\beta>0\), so there is no atom at \(b\). The variable \(J\) may have other atoms or singular mass away from \(b\); no density is assumed. The variance \(V_\lambda\) is the **actual** variance, not a freely increased quadratic proxy. The comparison is one-sided, for nonnegative MGF arguments. All little-oh statements are for the specified \(\lambda\to0\) limit, with the jump law and \(\sigma\) fixed.

This is a probability-distribution result (MSC2020 60E07). It does not treat a varying jump law or unbounded positive jumps.

## Proof

**1. Exact reduction.** Let \(J^\#\) have the second-size-biased jump law

\[
\Pr(J^\#\in A)=\frac{\mathbb E[J^2\mathbf1_{\{J\in A\}}]}{\mathbb E J^2},
\]

and take \(B\sim\operatorname{Beta}(1,2)\) independently. Define \(F(s)=\mathbb E\exp(sBJ^\#/b)\). Since \(\mathbb Ee^{zB}=2(e^z-1-z)/z^2\) (with its continuous value at zero),

\[
F(s)=\frac{2b^2}{s^2\mathbb E J^2}
\left(\mathbb Ee^{sJ/b}-1-\frac{s}{b}\mathbb E J\right),\qquad s>0.
\]

The cumulant generating function of \(X_\lambda\) is

\[
\log\mathbb Ee^{tX_\lambda}=
\frac{V_\lambda t^2}{2}\bigl[1+\delta_\lambda(F(bt)-1)\bigr].
\]

Write \(H_\delta(s)=\delta(F(s)-1)\) and

\[
\psi_\delta(s)=\frac{H_\delta(s)}{s(1+H_\delta(s))}.
\]

Elementary rearrangement of the sub-gamma inequality yields the exact variational identity

\[
\frac{c_\lambda}{b}=\sup_{s>0}\psi_{\delta_\lambda}(s).
\]

Indeed, if \(s<b/c\), its inequality is equivalent to \(c/b\ge\psi_\delta(s)\); if \(s\ge b/c\), then \(\psi_\delta(s)\le1/s\le c/b\), so those arguments impose no additional restriction. This also proves the converse when the supremum is finite.

**2. Upper-endpoint Laplace lemma.** Put \(Y=1-J/b\) and \(D=Cb^\beta\). Then \(Y\in[0,1]\) and

\[
\Pr(Y\le y)\sim Dy^\beta\qquad(y\downarrow0).
\]

Stieltjes integration by parts followed by the substitution \(z=sy\) gives

\[
T(s):=\mathbb Ee^{-sY}=s\int_0^\infty e^{-sy}\Pr(Y\le y)\,dy
\sim D\Gamma(\beta+1)s^{-\beta}.
\]

The same integration by parts, now applied to \(y e^{-sy}\), gives

\[
\mathbb E[Ye^{-sY}]=\int_0^\infty(sy-1)e^{-sy}\Pr(Y\le y)\,dy
\sim\beta D\Gamma(\beta+1)s^{-\beta-1}.
\]

For completeness, these limits follow by splitting at a fixed small \(y_0>0\), applying the upper/lower power bounds from \(\Pr(Y\le y)\sim Dy^\beta\) below \(y_0\), and using exponential damping above it. The first integrals give \(\Gamma(\beta+1)\); for the second, \(\int_0^\infty(z-1)e^{-z}z^\beta dz=\beta\Gamma(\beta+1)\). Therefore

\[
\mathbb Ee^{sJ/b}=e^sT(s)
\sim D\Gamma(\beta+1)e^ss^{-\beta},
\]

and its logarithmic derivative is \(1-\beta/s+o(1/s)\). Substitution into the exact expression for \(F\), with the polynomial terms exponentially negligible, establishes

\[
F(s)=K\frac{e^s}{s^{\beta+2}}(1+o(1)),\qquad
\frac{F'(s)}{F(s)}=1-\frac{\beta+2}{s}+o(s^{-1}).
\]

These statements are *asymptotic consequences of the full endpoint-tail hypothesis* and do not assume differentiability of its distribution function.

**3. All global maxima are at the logarithmic scale.** Write \(L=\log(1/\delta)\) and let

\[
s_0=L+(\beta+3)\log L-\log K.
\]

The last display implies \(H_\delta(s_0)\sim L\) and hence \(\psi_\delta(s_0)\sim1/L\). Since \(0\le BJ^\#/b\le1\), the inequality \(e^{sz}-1\le sz e^s\) gives

\[
\psi_\delta(s)\le\delta e^s\qquad(s>0).
\]

Thus \(\sup_{s\le(1-\eta)L}\psi_\delta(s)\le e^{-\eta L}\) for every fixed \(\eta\in(0,1)\). Also \(\psi_\delta(s)\le1/s\), so \(\sup_{s\ge(1+\eta)L}\psi_\delta(s)\le[(1+\eta)L]^{-1}\). Both are eventually strictly below the competitor \(\psi_\delta(s_0)\). Hence **every** maximizer satisfies \(s_\delta/L\to1\). The objective is continuous, has a finite limit at zero and tends to zero at infinity; the competitor exceeds its value at zero for small \(\delta\), so such global maximizers exist and are interior.

**4. Stationarity and the constant term.** At each interior maximizer, differentiation yields

\[
s_\delta H_\delta'(s_\delta)=H_\delta(s_\delta)
\bigl(1+H_\delta(s_\delta)\bigr).
\]

Since \(H_\delta=\delta(F-1)\) and \(s_\delta\to\infty\), Step 2 gives

\[
H_\delta(s_\delta)=\frac{s_\delta F'(s_\delta)}{F(s_\delta)-1}-1
=s_\delta-(\beta+3)+o(1).
\]

In particular \(H_\delta(s_\delta)/s_\delta\to1\). Taking logarithms of \(\delta(F(s_\delta)-1)=H_\delta(s_\delta)\) yields

\[
s_\delta=L+(\beta+3)\log s_\delta-\log K+o(1).
\]

Step 3 implies \(\log s_\delta=\log L+o(1)\), proving the displayed optimizer expansion. Finally, at a global maximizer,

\[
\frac{b}{c_\lambda}=
\frac{s_\delta(1+H_\delta(s_\delta))}{H_\delta(s_\delta)}
=s_\delta+1+o(1),
\]

which establishes the asserted exact constant term and both forms of the scale expansion. The proof applies simultaneously to every possible global maximizer. \(\square\)

## Verification

The independent finite diagnostic script `check.py` uses rational arithmetic to confirm 200 Taylor-coefficient identities for two exact continuous-endpoint families. It checks the finite-dimensional stationary equation, high-precision-scale behavior and maximizing-point asymptotics at four logarithmic dilution levels for each family (262 assertions total). It uses only the Python standard library. Run `python check.py` in the extracted file directory. The infinite-family theorem is proved in the preceding steps; no finite experiment establishes a universal asymptotic result.

For \(b=1\) and \(J\sim\operatorname{Uniform}(0,1)\), one has \(\beta=1\), \(C=1\), \(\mathbb E J^2=1/3\), \(K=6\), giving

\[
\frac1{c_\lambda}=L_\lambda+4\log L_\lambda+1-\log6+o(1).
\]

For \(J\) with density \(2(1-x)\) on \([0,1]\), one has \(\beta=2\), \(C=1\), \(\mathbb E J^2=1/6\), \(K=24\), giving

\[
\frac1{c_\lambda}=L_\lambda+5\log L_\lambda+1-\log24+o(1).
\]

The script uses their exact transformed MGFs \(F(s)=6(e^s-1-s-s^2/2)/s^3\) and \(F(s)=24(e^s-1-s-s^2/2-s^3/6)/s^4\), respectively.

## Relationship to prior work

Chen's arXiv:2610.00032v1 establishes the canonical Beta-remainder transform and variational characterization for spectrally positive infinitely divisible laws, and discusses Gaussian convolution and Gamma/two-point jump examples. These are essential premises; the new assertion is the **asymptotic classification across arbitrary continuous upper-endpoint powers \(\beta>0\)**, which is not an instance of its displayed finite-example formulas.

Chen and Wang's arXiv:2609.02590v1 proves an optimizer expansion with coefficient three in front of \(\log\log(1/p)\) for the rare positive *fixed-size* jump in a Skellam law. It does not state the \(\beta+3\) law for non-atomic, regularly varying endpoints in Gaussian-smoothed compound Poisson families. The atom-at-the-endpoint boundary is deliberately excluded here.

Leskelä and Välimaa's arXiv:2508.12103 concerns optimal **sub-Poisson variance proxies**, not the true-variance **sub-gamma pole** treated here. The common concentration terminology does not equate the optimization problems. Classical endpoint Laplace asymptotics alone do not supply global optimizer localization or the sub-gamma correction constant; Steps 3--4 establish these links.

## Limitations

The result has the fixed-Gaussian-background and rare-intensity regime \(\lambda\downarrow0\). It requires a finite positive maximum and a pure power-law endpoint asymptotic with \(\beta>0\); it does not classify logarithmically varying endpoint tails, unbounded jumps, moving jump laws or multivariate concentration. It proves asymptotics for every global optimizer but does not establish uniqueness. The result does not determine higher-order correction terms beyond the stated little-oh order.

## References

1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public version September 2, 2026), https://arxiv.org/html/2610.00032v1.
2. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1 (September 2, 2026), https://arxiv.org/pdf/2609.02590.
3. L. Leskelä and I. Välimaa, *Sub-Poisson distributions: Concentration inequalities, optimal variance proxies, and closure properties*, arXiv:2508.12103v1 (August 16, 2025), https://arxiv.org/abs/2508.12103.
