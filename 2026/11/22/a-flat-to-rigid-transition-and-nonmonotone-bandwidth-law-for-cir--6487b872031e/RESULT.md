# A flat-to-rigid transition and nonmonotone bandwidth law for circular boxcar smoothing

## Finding

For a circular one-sided moving-average kernel, the sharp real bounded-variation-to-mean-square **error norm** has a transition at half the circle: a continuum of maximizing jump separations collapses to the unique half-circle separation. Surprisingly, its sharp error is nonmonotone in the averaging-window length.

For \(0<a\le1\), write
\[
 A_a f(x)=\frac1a\int_0^a f(x+u)\,du,
 \qquad C(a)=\sup_{V(f)>0}\frac{\|(I-A_a)f\|_2}{V(f)}.
\]
Then the exact statement is
\[
 \boxed{C(a)^2=\begin{cases}
 a/6,&0<a\le 1/2,\\
 \frac{-8a^3+12a^2-1}{48a^2},&1/2\le a\le1.
 \end{cases}}
\]
All nonconstant equality cases, and no others, are \(f=b+c\mathbf 1_I\) almost everywhere, where \(c\ne0\) and \(I\) is a circular arc. The allowed arc lengths are \(d\in[a,1-a]\) when \(a<1/2\) and only \(d=1/2\) when \(a\ge1/2\). At \(a=1/2\), the two descriptions coincide.

There is exactly one global maximizer of the bandwidth-dependent squared error:
\[
 a_*=4^{-1/3},\qquad
 C(a_*)^2=\frac{1-a_*}4\approx0.09250986876314.
\]
Thus increasing the amount of averaging eventually *decreases* the worst normalized residual.

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Haar (Lebesgue) measure. All functions are real and considered almost everywhere. \(BV(\mathbb T)\) is defined distributionally with full circular total variation \(V(f)=|Df|(\mathbb T)\). In particular, an indicator of a nontrivial circular interval has variation exactly \(2\), including the jump crossing the identified endpoint. No continuity, sign, or zero-mean hypothesis is imposed. The norm \(\|\cdot\|_2\) is the standard \(L^2(\mathbb T)\) norm. The averaging window is deliberately *one-sided*; a centered window changes the phase of the Fourier multiplier and is not interchangeable in \(I-A_a\).

## Proof

**1. Reduction to a single arc with a fully general BV input.** Let \(\mu=Df\), a finite signed measure on the circle with \(\mu(\mathbb T)=0\) and \(|\mu|(\mathbb T)=V(f)\). Its Jordan decomposition is \(\mu=\frac{V(f)}2(P-Q)\) for probability measures \(P,Q\). For points \(s,t\), let \(h_{s,t}\) be the indicator of the oriented circular arc starting at \(s\) and ending at \(t\), so \(Dh_{s,t}=\delta_s-\delta_t\). Therefore \(f\), up to an additive constant, is the weak integral \(\frac{V(f)}2\iint h_{s,t}\,P(ds)Q(dt)\). The bounded operator \(E_a=I-A_a\) kills constants. Minkowski's integral inequality yields
\[
 \|E_a f\|_2\le \frac{V(f)}2\max_{s,t}\|E_a h_{s,t}\|_2.
\]
Conversely every nontrivial arc indicator has variation \(2\) and gives equality in the sup bound at a maximizing length. The residual norm is invariant under rotating or complementing the arc, so it suffices to consider \(h_d=\mathbf1_{[0,d]}\) for \(0\le d\le1/2\).

**2. Exact arc residual.** Its periodic autocorrelation at \(0\le h\le1\) is
\[
 c_d(h)=\int_0^1h_d(x)h_d(x+h)\,dx
 =(d-h)_++(d+h-1)_+.
\]
Expanding the square \(\|h_d-A_a h_d\|_2^2\), using the one-sided box kernel and its triangular self-correlation, gives the exact identity
\[
 R_a(d):=\|E_a h_d\|_2^2
 =d-\frac2{a^2}\int_0^a h\,c_d(h)\,dh.
\]
Writing \(p=\min(a,d)\) and \(e=(a+d-1)_+\), elementary integration yields
\[
 R_a(d)=d-\frac2{a^2}
 \left(\frac{dp^2}2-\frac{p^3}3+\frac{e^2(2a+1-d)}6\right).
\]

**3. Global maximization and transition.** Suppose first \(a\le1/2\). For \(0\le d<a\), the formula reduces to \(R_a(d)=d-d^3/(3a^2)\) and has derivative \(1-d^2/a^2>0\). For \(a\le d\le1/2\), \(R_a(d)=2a/3\) is constant. Complement symmetry gives exactly the interval of maximizing arc lengths \([a,1-a]\). Since \(V(h_d)=2\), \(C(a)^2=(2a/3)/4=a/6\).

Suppose now \(a>1/2\). On \(0\le d\le1-a\), the same strictly increasing formula holds. On \(1-a<d\le1/2\), direct differentiation gives
\[
 R_a'(d)=\frac{1-2d}{a^2}>0\qquad(d<1/2).
\]
Thus the unique maximizing shorter arc length is \(d=1/2\). Substitution gives
\[
 R_a(1/2)=\frac{-8a^3+12a^2-1}{12a^2},
\]
which produces the stated sharp constant. The two branches coincide at \(a=1/2\); the endpoint \(a=1\) is included.

**4. Exhaustiveness of equality cases.** Equality in the Hilbert-space Jensen/triangle argument above forces the residuals \(E_a h_{s,t}\) to be a common nonzero vector for \(P\times Q\)-almost all pairs, since every maximizing arc has the same positive residual norm. For every integer \(n\ne0\), the Fourier multiplier of \(A_a\) is
\[
 \widehat A_a(n)=\frac{e^{2\pi i n a}-1}{2\pi i n a},\qquad
 |\widehat A_a(n)|<1.
\]
Thus \(E_a\) is injective modulo constants. Equal residuals imply identical distributional derivatives \(\delta_s-\delta_t\). For nontrivial arcs the positive and negative atoms then uniquely determine \(s,t\). Consequently \(P,Q\) are point masses, proving that every nonconstant equality case is a single arc indicator plus a constant, with the lengths already classified.

**5. A nonmonotone bandwidth law.** The first branch has strictly positive derivative. The second has
\[
 \frac{d}{da}C(a)^2=\frac{1-4a^3}{24a^3},
\]
so it grows until \(a_*=4^{-1/3}\) and strictly decreases afterward. In particular \(C(1/2)^2=1/12\), \(C(a_*)^2=(1-a_*)/4\), and \(C(1)^2=1/16\).

## Verification

A standalone Python script `check.py` recomputes the residual energy from an exact rational decomposition into breakpoints of the original moving-average integral; it checks the closed forms, global comparison on rational grids, and the transition/derivative identities. An independent truncated Fourier-series check compares the same residual via the boxcar multiplier. The script reports 7,354 successful exact-rational, symbolic and Fourier consistency assertions. The finite tests support reproducibility and detect algebraic mistakes; the full real-bandwidth and full-BV conclusions follow from the analytic argument, not finite enumeration.

## Relationship to prior work

Angeloni–Vinti (2016) reviews variation-diminishing properties and approximation in variation for convolution integral operators; it does not provide this sharp one-sided-window \(BV(\mathbb T)\)-to-\(L^2\) *identity-residual* norm or equality characterization. Dron–Zhuk (2014) studies \(L^2\) deviations of modified Steklov averages in Jackson/modulus-of-smoothness comparisons, which are not an all-bandwidth sharp BV operator-error norm. Zhuk–Puerov (2009) compares \(L^2\) approximation errors for generalized Steklov means; its complete text was not available for comparison, so exact priority is not certified. Other sharp operator bounds for discrete boxcar variation amplification or Hardy–Steklov windows concern different spaces or operators. This result concerns the plain **forward one-sided window** and identifies a continuous family of extremizers before the critical width and rigidity afterward.

## Limitations

The theorem is one-dimensional, real-valued, uses full circular variation and normalized \(L^2\), and holds only for a uniform forward boxcar of window width at most one circle. It does not establish analogous sharp laws for centered windows, multi-wrap windows, nonuniform moving-average kernels, complex measures with complex variation, other \(L^p\) norms, or higher-dimensional tori. A historically earlier result with equivalent hypotheses could exist; the 2009 Zhuk–Puerov full text was inaccessible and is an explicit residual priority risk. No independent mathematical review has occurred.

## References

1. Laura Angeloni and Gianluca Vinti, *A Review on Approximation Results for Integral Operators in the Space of Functions of Bounded Variation*, Journal of Function Spaces 2016, Article ID 3843921, first published 26 September 2016. https://doi.org/10.1155/2016/3843921
2. V. O. Dron and V. V. Zhuk, *On approximation of periodic functions by modified Steklov averages in \(L^2\)*, Zapiski Nauchnykh Seminarov POMI 429 (2014), pp. 20–33. https://www.mathnet.ru/eng/znsl6064
3. V. V. Zhuk and G. A. Puerov, *Comparison of errors of approximation by generalized Steklov means in the space \(L^2\)*, St. Petersburg University proceedings (2009), no. 1, pp. 56–62. https://pureportal.spbu.ru/en/publications/-------l2%28988011c5-5120-4d02-8044-7ebc410ad96a%29.html
