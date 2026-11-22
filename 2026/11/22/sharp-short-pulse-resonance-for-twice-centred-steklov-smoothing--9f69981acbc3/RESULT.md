# Sharp short-pulse resonance for twice-centred Steklov smoothing on the circle

## Finding

On the unit circle \(\mathbb T=\mathbb R/\mathbb Z\) with probability-normalized Lebesgue measure, set
\[
(S_a f)(x)=\frac1a\int_{-a/2}^{a/2}f(x+u)\,du,\qquad T_a=S_a^2,\qquad 0<a\le\frac13.
\]
For real periodic \(f\in BV(\mathbb T)\), use the full circular Jordan variation \(V(f)=|Df|(\mathbb T)\). Define
\[
p(z)=1-\frac{8z}{3}+2z^2-\frac{2z^3}{3}+\frac{z^4}{4},\quad
\Phi(z)=z-\frac{4z^2}{3}+\frac{2z^3}{3}-\frac{z^4}{6}+\frac{z^5}{20}.
\]
Let \(r\) be the unique zero of \(p\) in \((0,1)\), with \(r=0.611114325406299\ldots\). Then, for **every** \(0<a\le1/3\),
\[
\boxed{\sup_{V(f)>0}\frac{\|f-T_af\|_{L^2(\mathbb T)}^2}{V(f)^2}
=\frac a4\,\Phi(r)=0.0615835934466545\ldots\,a.}
\]
The complete set of nonconstant equality cases consists of
\[
f(x)=b+c\,\mathbf1_{[s,s+ar)}(x)\quad\text{a.e.},\qquad b\in\mathbb R,\ c\in\mathbb R\setminus\{0\},\ s\in\mathbb T,
\]
with arcs interpreted modulo one. Thus the extremal discontinuities form a **short pulse of length \(ar\)** (or its complement, equivalently via changing the sign and constant), not a semicircle or two well-separated jumps.

If \(0<a\le1/4\), any arc whose length and complementary length are both at least \(2a\) has squared residual \(a/5\), whereas an extremal short arc has squared residual \(a\Phi(r)\). The relative squared-residual advantage is \(5\Phi(r)-1=0.23167186893309\ldots\), a genuine interaction of two nearby jump layers.

## Assumptions and scope

\(S_a\) uses **centred** box averaging of width \(a\), so \(T_a\) is convolution with the nonnegative, even, unit-mass triangular kernel
\[
K_a(x)=\sum_{m\in\mathbb Z}\frac{(a-|x+m|)_+}{a^2},\qquad
\widehat K_a(k)=\operatorname{sinc}^2(\pi ka),\quad \operatorname{sinc}(u)=\frac{\sin u}{u}.
\]
The square \(S_a^2\) means two sequential centred box averages, not a squared numerical value of \(S_af\), and equals a translate of a forward double Steklov mean; nevertheless the residual \(I-T_a\) is not a translate of \(I-A_a^2\) for forward averaging \(A_a\). The norm is ordinary \(L^2\) and the inputs are real \(BV\) functions. The endpoints \(a=1/3\) and all singular-continuous derivative measures are included. Constants have zero variation and zero residual and are excluded from the quotient.

## Proof

**1. Reduction to single arcs and equality rigidity.** Since \(Df\) is a finite signed measure of total mass zero, its positive and negative Jordan parts each have mass \(V(f)/2\). Couple their normalized measures by any probability transport measure \(\pi(ds\,dt)\). If \(I(s,t)\) is the oriented counterclockwise arc from \(s\) to \(t\), then distributionally \(D\mathbf1_{I(s,t)}=\delta_s-\delta_t\). Consequently, modulo a constant,
\[
f=\frac{V(f)}2\int\mathbf1_{I(s,t)}\,d\pi(s,t).
\]
The triangle inequality in real \(L^2\) gives
\[
\|(I-T_a)f\|_2\le\frac{V(f)}2\max_{0\le L\le1}\|(I-T_a)\mathbf1_{[0,L)}\|_2.
\]
Every arc of length \(L\) has \(V(\mathbf1_I)=2\), so the bound is sharp for a length-maximizing arc. Equality in the Hilbert-space triangle inequality requires its nonzero arc residuals to be identical and maximizing almost surely. The Fourier multipliers of \(I-T_a\) are \(1-\operatorname{sinc}^2(\pi ka)>0\) for every nonzero integer \(k\): hence \(I-T_a\) is injective modulo constants. Two arc indicators with equal residual must be identical modulo a constant. Thus every nonconstant equality function is one arc indicator up to scaling and a constant, once the maximizing arc lengths are known. No finite-dimensional approximation of \(BV\) is assumed in this argument.

**2. Exact arc residual curvature.** Write \(f_L=\mathbf1_{[0,L)}\) and \(F_a(L)=\|(I-T_a)f_L\|_2^2\). By Parseval,
\[
F_a(L)=\sum_{k=1}^{\infty}\frac{1-\cos(2\pi kL)}{\pi^2k^2}
\bigl(1-\operatorname{sinc}^2(\pi ka)\bigr)^2.
\]
The residual is unchanged by taking an arc complement and translating, giving \(F_a(L)=F_a(1-L)\). In distributional derivatives on the open circle (or by twice differentiating the Fourier series away from \(L=0\)),
\[
F_a''(L)=2\bigl[(K_a*K_a)(L)-2K_a(L)\bigr]\quad(0<L<1).
\]
As \(L\downarrow0\), \(\|f_L\|_2^2=L\), while the other terms in \(\|f_L-T_af_L\|_2^2\) are \(O_a(L^2)\); therefore \(F_a'(0+)=1\). The four-fold centred box convolution \(K_a*K_a\) is the periodization of \(a^{-1}b_4(x/a)\), where on the positive half-axis
\[
b_4(z)=\begin{cases}
\frac23-z^2+\frac{z^3}{2},&0\le z\le1,\\
\frac{(2-z)^3}{6},&1\le z\le2,\\
0,&z\ge2.
\end{cases}
\]
For \(0<L<a\le1/3\), the other translates of this compactly supported four-box density vanish: \(1-L\ge1-a\ge2a\). Also \(K_a(L)=a^{-1}(1-L/a)\). Hence
\[
F_a''(L)=\frac1a\left(-\frac83+4z-2z^2+z^3\right),\quad z=L/a.
\]
Combining with \(F_a'(0+)=1\), then integrating once again, yields the **exact**, not asymptotic, formulas
\[
F_a'(az)=p(z),\qquad F_a(az)=a\Phi(z),\qquad 0\le z\le1.
\]

**3. Global maximization, including wrapping and boundaries.** One has \(p(0)=1\) and \(p(1)=-1/12\), while
\[
p''(z)=3z^2-4z+4=3(z-2/3)^2+8/3>0.
\]
Thus \(p\) has exactly one root \(r\) in \((0,1)\) and changes from positive to negative there; the exact rational sign tests \(p(0.6111143254)>0>p(0.6111143255)\) isolate it. For \(a\le L\le1/2\), the triangular kernel \(K_a(L)\) is zero, and the periodized convolution \((K_a*K_a)(L)\) is nonnegative. It follows that \(F_a''(L)\ge0\) on this entire second regime, even when fourfold-convolution support begins to wrap around the circle. Reflection symmetry gives \(F_a'(1/2)=0\), so \(F_a'\le0\) for \(a\le L\le1/2\). On \([0,a]\), the derivative is positive only before \(L=ar\). Consequently \(L=ar\) is the unique maximizer on \([0,1/2]\), and reflection gives precisely \(L=ar\) and \(L=1-ar\) on \([0,1]\). The reduction in step 1 now proves the asserted sharp constant and every equality case.

**4. Separated-jump comparison.** If \(a\le1/4\), then on \([a,2a]\) no periodized four-box term wraps and \(F_a'(az)=-(2-z)^4/12\), while \(F_a'=0\) on \([2a,1-2a]\). Since \(\Phi(1)=13/60\), direct integration yields \(F_a(L)=a/5\) on that plateau. Strict decrease after \(L=ar\) gives \(\Phi(r)>1/5\).

## Verification

`check.py` is a standalone Python standard-library checker. It tests the quartic derivative identity and its primitive with exact fractions, verifies the rational root enclosure, checks the four-box spline formulas and plateau identities, and compares the analytical pulse energy with independently summed Fourier series at bandwidths \(1/6\), \(1/4\), and \(1/3\). The Fourier sum is truncated but has a stated explicit tail bound. The analytical proof above—not numerical enumeration—establishes the continuum maximum and all equality cases. Run `python3 check.py` with no external packages.

## Relationship to prior work

Iterated Steklov averages and B-spline kernels are classical. Mejía–Silvestre (2015) study periodic functions of bounded higher \(p\)-variation and bounds via fractional moduli, including iterated **forward** Steklov averages; those estimates do not state this sharp full-Jordan-variation-to-\(L^2\) centred-triangular norm or its pulse rigidity. Costarelli–Vinti (2014, full text including Section 6) study sampling Kantorovich reconstruction with central B-spline windows and Lipschitz/Orlicz approximation rates, not the convolution residual \(I-S_a^2\) on periodic \(BV\). Angeloni–Vinti and collaborators (2023, sections on variation convergence and kernels) address sampling-Kantorovich convergence in variation, not the present exact sharp norm. The distinct circular one-sided boxcar residual, circle Poisson-mixture residual and periodic hat reconstruction results do not imply the triangular convolution theorem: their multipliers, output operator and maximizing arc structures differ. Searches in available indexed research and existing claim ledgers found no directly covering theorem. Nonindexed historical priority remains a risk, not an assertion of uniqueness across all literature.

## Limitations

The exact bandwidth law and extremizer classification are proved only for \(0<a\le1/3\); no phase diagram is claimed for wider triangular windows. The result uses **centred** averaging and does not transfer unchanged to forward-shifted iterated Steklov averages, higher B-spline orders, different \(L^p\) targets, or weighted variation.

## References

1. D. Costarelli and G. Vinti, *Rate of approximation for multivariate sampling Kantorovich operators on some functions spaces*, J. Integral Equations Appl. 26 (2014), 455–481. Public arXiv version 2014-11-09, https://arxiv.org/abs/1411.2261; DOI https://doi.org/10.1216/JIE-2014-26-4-455.
2. O. Mejía and P. Silvestre, *Functions of Bounded kth p-Variation and Continuity Modulus*, Journal of Function Spaces (2015), article 253636, https://doi.org/10.1155/2015/253636.
3. L. Angeloni et al., *Multidimensional sampling-Kantorovich operators in BV-spaces*, Open Mathematics 21 (2023), https://doi.org/10.1515/math-2022-0573.
4. MSC2020, 41A44: Best constants in approximation theory, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=41Axx.
