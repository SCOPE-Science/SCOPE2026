# Rigidity of every shortest tensor-product torus design curve

## Finding

Fix integers \(d\ge 1\) and \(t\ge 1\), and put \(q=t+1\). Among all closed arclength-weighted \(t\)-design curves on the flat torus \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), **every shortest curve**, not merely the known Korobov construction, is a translate of a straight primitive geodesic whose integer winding vector is a signed coordinate permutation of
\[
(1,q,q^2,\ldots,q^{d-1}).
\]
Conversely, each such curve is an exact \(t\)-design and has the sharp minimum length
\[
L_* = \left(\sum_{j=0}^{d-1}q^{2j}\right)^{1/2}
=\left(\frac{q^{2d}-1}{q^2-1}\right)^{1/2}.
\]
There are exactly \(2^{d-1}d!\) unoriented minimizing winding directions, independent of torus translations. In particular, no genuinely curved closed path realizes the length minimum.

## Assumptions and scope

A curve is a rectifiable lift \(\gamma:[0,L]\to\mathbb R^d\) parametrized by Euclidean arclength, with \(\gamma(L)-\gamma(0)\in\mathbb Z^d\). It is a tensor-product \(t\)-design when
\[
\frac1L\int_0^L e^{2\pi i m\cdot\gamma(s)}\,ds
=\begin{cases}1,&m=0,\\0,&0<\|m\|_\infty\le t,\end{cases}
\quad(m\in\mathbb Z^d).
\]
This is the unweighted (normalized arclength) design notion, not a freely weighted quadrature rule and not a total-degree or hyperbolic-cross design. Equality and classification are up to translation on \(\mathbb T^d\), parametrization origin and reversal of orientation. The sharp lower bound itself and one achieving geodesic were previously established by Ehler [1].

## Proof

**1. Orthogonal frequency family and its fixed energy.** Set \(N=q^d\) and
\[
A=\{-t/2,-t/2+1,\ldots,t/2\}^d,\qquad
f_a(s)=e^{2\pi i a\cdot\gamma(s)}\quad(a\in A).
\]
Although \(a\) can be half-integral, each difference \(a-b\) is integral with \(\|a-b\|_\infty\le t\). Design exactness therefore makes the \(N\) functions \(f_a\) orthonormal in \(L^2([0,L],ds/L)\). Arclength parameterization implies \(\|\gamma'(s)\|_2=1\) almost everywhere. The centered product grid has exact isotropic second moment
\[
\frac1N\sum_{a\in A}aa^{\mathsf T}=\frac{t(t+2)}{12}I_d.
\]
The chain rule for Lipschitz functions gives the identity
\[
\frac1N\sum_{a\in A}\frac1L\int_0^L|f'_a(s)|^2\,ds
=\frac{4\pi^2t(t+2)}{12}.\tag{1}
\]

**2. The spectral bound, including boundary parity.** Let \(v=\gamma(L)-\gamma(0)\in\mathbb Z^d\). When \(t\) is even, each \(f_a\) is periodic and \(N\) is odd. The unique subspace spanned by the \(N\) Fourier modes with smallest squared frequencies has frequencies \(-(N-1)/2,\ldots,(N-1)/2\); their mean squared frequency is \((N^2-1)/12\). When \(t\) is odd, \(N\) is even and every \(f_a\) is periodic if \(\sum_jv_j\) is even, or antiperiodic if this sum is odd. In the periodic case the \(N\) smallest integer squared frequencies have mean \((N^2+2)/12\), strictly larger than \((N^2-1)/12\). In the antiperiodic case, the \(N\) smallest half-integer squared frequencies \(-(N-1)/2,\ldots,(N-1)/2\) have mean \((N^2-1)/12\).

The Fourier min-max (trace/Bessel) inequality applied to \(N\) orthonormal functions, combined with (1), yields
\[
L^2\ge\frac{N^2-1}{t(t+2)}=\sum_{j=0}^{d-1}q^{2j}.\tag{2}
\]
Equality is impossible in the even-winding-sum periodic case when \(t\) is odd. In either other case the ordered squared-frequency threshold has a **strict gap** between the \(N\)-th and \((N+1)\)-st Fourier modes. Equality in (2) consequently forces the orthonormal family \(\{f_a:a\in A\}\) to be an orthonormal basis of exactly the unique lowest-\(N\)-mode Fourier subspace: any nonzero mass in a higher mode would strictly increase the sum of derivative energies.

**3. Constant-modulus spectral rigidity.** Any finite trigonometric polynomial, allowing a common half-integer shift of all exponents, whose absolute value is identically one is a single Fourier monomial. Indeed, if it had at least two nonzero coefficients, choose its smallest and largest exponents. The coefficient of the positive maximal exponent difference in its squared modulus is the product of those two extreme coefficients, which is nonzero; this contradicts constant squared modulus. Thus each \(f_a\) equals \(c_a e^{2\pi i k_as/L}\) for a single allowed integer or half-integer \(k_a\), with \(|c_a|=1\). Distinct \(a\)'s have distinct frequencies, and the \(k_a\)'s exhaust the unique lowest \(N\) frequencies.

For any coordinate \(j\), the grid \(A\) contains a pair \(a,a+e_j\). Their ratio satisfies
\[
e^{2\pi i\gamma_j(s)}=\frac{f_{a+e_j}(s)}{f_a(s)}
=c\,e^{2\pi i(k_{a+e_j}-k_a)s/L}.
\]
The difference of their Fourier frequencies is an integer. By continuity of the real lift \(\gamma_j\), the difference \(\gamma_j(s)-(k_{a+e_j}-k_a)s/L\) is a constant real number. For all coordinates,
\[
\gamma(s)=x_0+\frac{s}{L}v,\qquad v\in\mathbb Z^d.\tag{3}
\]
Its unit arclength speed forces \(L=\|v\|_2\). No nonstraight curve can be a minimizer.

**4. Exhaustion of all minimizing winding vectors.** By (3), the frequency \(k_a\) of \(f_a\) is exactly \(a\cdot v\). Since these frequencies exhaust the \(N\) consecutive lowest frequencies, none of the coordinates of \(v\) vanishes. Apply coordinate sign changes and write \(w_j=|v_j|>0\). Translation of the centered digit cube then shows that the \(q^d\) integer sums
\[
\left\{\sum_{j=1}^{d}r_jw_j:r_j\in\{0,\ldots,q-1\}\right\}
\]
are distinct and are exactly \(\{0,1,\ldots,q^d-1\}\). The following elementary digit-tiling lemma completes the classification.

*Digit-tiling lemma.* If positive integer weights \(w_1,\ldots,w_d\) have this full, collision-free base-\(q\) digit-sum set, their multiset is \(\{1,q,\ldots,q^{d-1}\}\). To prove it, sum \(1\) forces a weight equal to \(1\); move it first. The digit sums formed by the remaining weights are the disjoint starting points of length-\(q\) consecutive integer blocks whose union is \(\{0,\ldots,q^d-1\}\). The only possible such partition begins at \(0,q,2q,\ldots,q^d-q\). Hence each remaining weight is divisible by \(q\), and division by \(q\) reduces the hypothesis to dimension \(d-1\). Induction (including the immediate \(d=1\) case) yields the stated powers. This forces \(v\) to be a signed coordinate permutation of \((1,q,\ldots,q^{d-1})\).

**5. Converse and counting.** If \(v\) has these weights then \(m\cdot v=0\) for \(m\in\mathbb Z^d\), \(\|m\|_\infty\le q-1\), implies \(m=0\): take the relation modulo \(q\), forcing the coefficient of weight \(1\) to vanish, then divide by \(q\) and iterate. A straight unit-speed geodesic with that winding therefore integrates every nonzero requested character to zero. It has length \(\|v\|_2=L_*\) and attains (2). All powers are distinct for \(q\ge2\), so there are \(2^dd!\) oriented winding vectors and, after identifying opposite orientations, \(2^{d-1}d!\) unoriented directions. This includes \(d=1\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic to check the centered-grid variance, Fourier minimum-energy traces in all relevant parity cases, and the length formula for finite parameter ranges. It exhaustively checks small positive digit-tiling weight vectors subject to the necessary sum and first-weight conditions, tests Korobov frequency nonannihilation, and checks the signed-permutation orbit counts. Run `python verify.py` using Python 3. These finite checks are ancillary: Steps 1–5 above, not enumeration, establish the theorem for **all** \(d,t\) and all admissible rectifiable curves. The constant-modulus lemma is proved analytically and does not rely on a numerical certificate.

## Relationship to prior work

Ehler [1, Section 2, Theorem 2.1 and Proposition 2.4] establishes the **sharp length inequality** and exhibits a Korobov geodesic attaining it, including the periodic/antiperiodic Fourier proof. These facts and methods are credited; they are not new here. The added statement is the **complete equality classification**: equality forces straightness and forces every winding coordinate to form precisely the signed-permuted base-\(q\) powers, giving the exact number of extremal directions. This requires following the equality conditions through the trace bound, constant-modulus spectral rigidity and an integer digit-tiling argument. The construction and quasioptimality study by Kunis [2] is relevant background, but its full manuscript was not available for comparison; the coverage assessment of [2] is limited to its publicly accessible abstract and [1]'s discussion. This leaves possible unrecognized antecedents.

## Limitations

The theorem concerns tensor-product frequency exactness and normalized arclength on the standard flat torus, in exact mathematics. It says nothing about nonuniform density-weighted curves, other frequency sets, arbitrary flat torus metrics, or stability of approximate designs. It does not claim that the lower bound or the Korobov example are newly discovered. Unindexed prior equality classifications and unpublished equivalent treatments remain possible. Independent mathematical verification is not provided.

## References

[1] M. Ehler, *Optimal bounds for design curves on the torus*, arXiv:2611.03362v1, first public 2026-11-02. https://arxiv.org/abs/2611.03362 . In particular, Section 2, Theorem 2.1, Lemmas 2.2–2.3, Proposition 2.4, and Remark 2.5.

[2] S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915, 2026. https://arxiv.org/abs/2608.11915 . Full manuscript not inspected; the public abstract and citation discussion in [1] were consulted.
