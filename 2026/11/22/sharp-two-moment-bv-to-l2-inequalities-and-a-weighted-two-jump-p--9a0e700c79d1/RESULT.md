# Sharp two-moment BV-to-\(L^2\) inequalities and a weighted two-jump principle

## Finding

For every strictly positive continuous probability density \(\rho\) on \([0,1]\), the optimal embedding constant for real functions of bounded variation satisfying **two affine moment cancellations** is the maximum of an explicit two-variable kernel. With \(d\pi(x)=\rho(x)\,dx\), \(m=\int x\,d\pi(x)\), and for \(0<s<1\)
\[
F(s)=\int_0^s\rho(x)\,dx,\qquad h(s)=\int_s^1(x-m)\rho(x)\,dx,
\]
put, for \(0<s<t<1\),
\[
K_\pi(s,t)=\frac{h(t)^2F(s)(1-F(s))+h(s)^2F(t)(1-F(t))-2h(s)h(t)F(s)(1-F(t))}{(h(s)+h(t))^2}.
\]
Then \(h(s)>0\) in \((0,1)\), and the **exact sharp inequality** is
\[
\left\|f\right\|_{L^2(\pi)}\le \left(\max_{0<s<t<1}\sqrt{K_\pi(s,t)}\right)|Df|((0,1))
\]
whenever \(\int f\,d\pi=\int xf\,d\pi=0\). Every pair \(s<t\) gives a valid two-jump test function with norm ratio \(\sqrt{K_\pi(s,t)}\); in particular the weighted sharp constant is attained.

For the uniform density \(\rho\equiv1\), the sharp constant and complete nonzero equality class are
\[
\boxed{\;\|f\|_{L^2(0,1)}\le\tfrac14|Df|((0,1)),\qquad
f(x)=c\bigl(\mathbf1_{(1/4,3/4)}(x)-\tfrac12\bigr),\ c\ne0.\;}
\]
Writing \(H(u)=u(1-u)\) and \(d=t-s\), the two-jump squared ratio satisfies the **exact deficit identity**
\[
\frac1{16}-K_1(s,t)=\frac{(d-1/2)^2}{4}+\frac{(H(s)-H(t))^2\,d(1-d)}{4(H(s)+H(t))^2}.
\]
Thus sharpness simultaneously forces jump separation \(1/2\) and symmetry about the midpoint.

## Assumptions and scope

Here \(f\) is a real \(BV((0,1))\) equivalence class, \(Df\) is its distributional derivative, and variation is \(|Df|((0,1))\); pointwise endpoint modifications do not enter either side. The density is continuous and strictly positive on the closed interval and normalized to unit integral. Both moments are Lebesgue integrals against \(\rho\). The weighted formula is an exact finite-dimensional optimization, **not** a claim that its maximizing pair has a closed form for every density. The uniform equality statement is up to almost-everywhere equivalence.

## Proof

**1. Centered Heaviside representation.** Set \(v_s(x)=\mathbf1_{[s,1]}(x)-(1-F(s))\). For every \(f\in BV((0,1))\) of zero \(\pi\)-mean, its signed derivative measure \(\mu=Df\) obeys, almost everywhere,
\[
f(x)=\int_{(0,1)}v_s(x)\,d\mu(s).
\]
This follows by the fundamental theorem for one-dimensional distributional BV and mean subtraction. Let \(X\sim\pi\). The first-moment condition is
\[
0=\int xf(x)\,d\pi(x)=\int_{(0,1)} h(s)\,d\mu(s).
\]
The identity \(h(s)=\operatorname{Cov}(X,\mathbf1_{X\ge s})\), together with strict positivity of \(\rho\), gives \(h(s)>0\) for interior \(s\). For example \(h(s)=F(s)(1-F(s))\left[\mathbb E(X\mid X\ge s)-\mathbb E(X\mid X<s)\right]\).

**2. Reduction of every derivative to two atoms.** Write \(\mu=\mu^+-\mu^-\). Unless \(f=0\), both positive measures are nonzero and
\[
B=\int h\,d\mu^+=\int h\,d\mu^->0.
\]
Define probability measures \(dP=h\,d\mu^+/B\) and \(dQ=h\,d\mu^-/B\), and choose the product coupling \(\gamma=P\otimes Q\). For \(s\ne t\) set
\[
U_{s,t}=\frac{h(t)v_s-h(s)v_t}{h(s)+h(t)}.
\]
For coincident \(s=t\) set \(U_{s,s}=0\). Directly integrating the derivative representation gives
\[
f=\int B\left(\frac1{h(s)}+\frac1{h(t)}\right)U_{s,t}\,d\gamma(s,t),
\quad
\int B\left(\frac1{h(s)}+\frac1{h(t)}\right)d\gamma=|\mu|((0,1)).
\]
The integrals converge in \(L^2(\pi)\), since \(\|v_s\|_2\le1\) and the displayed scalar coefficients are integrable. Each \(U_{s,t}\) has zero zeroth and first moments and \(|DU_{s,t}|((0,1))=1\) when \(s\ne t\). Minkowski therefore gives
\[
\|f\|_2\le |Df|((0,1))\sup_{s<t}\|U_{s,t}\|_2.
\]
Conversely, every \(U_{s,t}\) is admissible, proving exact sharpness.

**3. Computing the two-atom norm.** Since \(v_s\) is a centered indicator,
\[
\|v_s\|_2^2=F(s)(1-F(s)),\qquad \langle v_s,v_t\rangle=F(s)(1-F(t))\quad (s<t).
\]
Expansion yields \(\|U_{s,t}\|_2^2=K_\pi(s,t)\) exactly. The expression extends continuously by zero to the sides and diagonal of the closed triangular parameter region. At the sides this follows from \(h(s)=O(s)\) and \(h(t)=O(1-t)\) and the vanishing \(L^2\) norm of the respective centered indicators. At the diagonal the two Heaviside terms cancel as their positions coalesce. Therefore the positive maximum occurs at an interior pair.

**4. Uniform constant and sharp equality.** For \(\rho\equiv1\), \(F(s)=s\) and \(h(s)=H(s)/2\). Simplifying gives
\[
K_1(s,t)=\frac{H(s)H(t)}{(H(s)+H(t))^2}d(1-d).
\]
Both factors are bounded by \(1/4\). Equality requires \(d=1/2\) and \(H(s)=H(t)\), which with \(s<t\) forces \((s,t)=(1/4,3/4)\). Using \(4H(s)H(t)=(H(s)+H(t))^2-(H(s)-H(t))^2\) proves the deficit identity. In the positive-weight pairing of Step 2, equality in the final sharp inequality forces almost every nonzero paired atomic profile to have the unique maximizing unordered support \(\{1/4,3/4\}\). As \(\mu^+\) and \(\mu^-\) are mutually singular, the derivative must be a scalar multiple of \(\delta_{1/4}-\delta_{3/4}\). The two moment constraints then force precisely the displayed plateau function. Conversely its \(L^2\) norm equals \(|c|/2\) and its variation equals \(2|c|\).

## Verification

The included standard-library Python checker uses exact fractions and polynomial-density integration. It verifies both vanishing moments, derivative normalization and the covariance-kernel identity across four positive polynomial weights and five rational grids; the uniform deficit and its unique sampled equality point are also checked. Execution: `python3 checks/checker.py`. Its output is `PASS: 1764 exact rational assertions (pair identities, moments, gap and equality).` These finite tests do not prove the general inequality; the preceding measure decomposition, exact covariance identity, and equality argument do.

## Relationship to prior work

Bouchez and Van Schaftingen (2010) establish existence and describe extremals for a class of Poincaré–Sobolev inequalities in higher-dimensional \(BV\) domains under one nonlinear mean constraint. Pinelis (2012) proves general finite-atomicity principles for moment-constrained positive measures. Those general techniques are relevant predecessors and are not claimed as new. The result here concerns real one-dimensional \(BV\) with **two independent linear moment constraints**, a signed derivative, a complete weighted two-jump kernel, and the sharp uniform coefficient \(1/4\) with its complete equality class. Available comparisons did not disclose that full statement; an unindexed equivalent remains possible.

## Limitations

Only real-valued distributional \(BV\), two affine moments, and strictly positive continuous probability densities are covered. The weighted coefficient generally remains a two-dimensional maximum rather than an elementary closed form. The uniform equality classification is not automatically a classification for unequal densities. The literature comparison is not a formal priority guarantee, and no independent mathematical audit has been conducted.

## References

1. V. Bouchez and J. Van Schaftingen, *Extremal functions in Poincaré–Sobolev inequalities for functions of bounded variation*, first public preprint 26 January 2010, arXiv:1001.4651, https://arxiv.org/abs/1001.4651.
2. I. Pinelis, *On the extreme points of moments sets*, first public preprint 1 April 2012, arXiv:1204.0249, https://arxiv.org/abs/1204.0249.
3. P. Horta and M. Montenegro, *Asymmetric affine Poincaré–Sobolev–Wirtinger inequalities on BV and characteristic one-dimensional extremizers*, Nonlinear Analysis (2025), https://doi.org/10.1016/j.na.2024.113673 (abstract-only comparison; full-text equivalence not assessed).
