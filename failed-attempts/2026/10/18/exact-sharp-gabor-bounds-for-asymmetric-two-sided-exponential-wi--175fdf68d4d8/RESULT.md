# Exact sharp Gabor bounds for asymmetric two-sided exponential windows at integer redundancy

## Finding
Fix an integer \(m\ge2\) and two arbitrary real decay rates \(a,b>0\). Define the continuous, unnormalized two-sided exponential
\[
g(t)=\begin{cases}e^{-at},&t\ge0,\\ e^{bt},&t<0.\end{cases}
\]
For all integer translations and modulations, the rectangular Gabor family
\[
\mathcal G(g)=\{e^{2\pi int}g(t-k/m):k,n\in\mathbb Z\}
\]
is a frame of \(L^2(\mathbb R)\), with the following **exact optimal squared frame bounds**.

For \(j=0,\ldots,m-1\), set
\[
\begin{aligned}
u_j&=\frac{e^{-aj/m}}{1+e^{-a}},&v_j&=\frac{e^{-b(1-j/m)}}{1+e^{-b}},\\
\widetilde u_j&=\frac{e^{-aj/m}}{1-e^{-a}},&\widetilde v_j&=\frac{e^{-b(1-j/m)}}{1-e^{-b}},\\
U&=\sum_j u_j^2,&V&=\sum_jv_j^2,&C&=\sum_j u_jv_j.
\end{aligned}
\]
Define the positive quadratic root and its logarithmic position by
\[
t_* =\frac{(b-a)C+\sqrt{(a-b)^2C^2+4abUV}}{2bV},
\qquad x_* =\frac{\log t_*}{a+b}.
\]
Then \(0<x_*<1/m\), and the **optimal constants** are
\[
\boxed{A=Ue^{-2ax_*}+Ve^{2bx_*}-2Ce^{(b-a)x_*}
=\sum_{j=0}^{m-1}(u_je^{-ax_*}-v_je^{bx_*})^2>0,}
\]
\[
\boxed{B=\sum_{j=0}^{m-1}(\widetilde u_j+\widetilde v_j)^2.}
\]
The lower spectral edge has a unique Zak-fiber representative \((x_*,1/2)\), and the upper edge has \((0,0)\) (with periodic boundary representatives identified). In particular \(0<A<B<\infty\). All expressions involve only finite sums, exponentials, a square root, and a logarithm; no variational search remains.

## Assumptions and scope
Our time-frequency convention is \(M_nf(t)=e^{2\pi int}f(t)\) and \(T_yf(t)=f(t-y)\). The frame inequality is the **unscaled** one
\[
A\|f\|_2^2\le \sum_{k,n\in\mathbb Z}|\langle f,M_nT_{k/m}g\rangle|^2\le B\|f\|_2^2
\quad(f\in L^2(\mathbb R)).
\]
Neither \(g\) nor its shifts are normalized to unit norm. Integer redundancy is exactly \(m\); the modulation spacing is exactly one. The formulas cover the symmetric case \(a=b\) without taking limits. In contrast, this statement does not optimize over the continuous lattice shape.

## Proof
**1. Exact Zak-frame multiplier.** Define the unitary Zak transform
\[
Zf(x,\omega)=\sum_{k\in\mathbb Z}f(x-k)e^{2\pi ik\omega},
\qquad (x,\omega)\in[0,1)^2.
\]
For a Gabor window with modulation step one and translation step \(1/m\), Fourier orthogonality of the integer modulation and integer translation indices gives the Zak-diagonal frame operator, with symbol
\[
S(x,\omega)=\sum_{j=0}^{m-1}|Zg(x+j/m,\omega)|^2,
\quad 0\le x<1/m,
\]
whose essential infimum/supremum equal the sharp squared frame bounds. The sign of the shift is immaterial after reindexing because the Zak transform is quasi-periodic in its spatial coordinate.

For \(0\le y<1\), the two convergent geometric series give
\[
Zg(y,\omega)=\frac{e^{-ay}}{1-e^{-a}e^{-2\pi i\omega}}
+\frac{e^{-b(1-y)}e^{2\pi i\omega}}{1-e^{-b}e^{2\pi i\omega}}.
\]
Put \(q=e^{-a}\), \(r=e^{-b}\), and \(z=e^{2\pi i\omega}\). Combining the fractions gives a numerator \(H(y)+J(y)z\), where
\[
H(y)=e^{-ay}-qr e^{by}\ge0,\qquad
J(y)=r(e^{by}-e^{-ay})\ge0,
\quad 0\le y\le1.
\]
Their squared modulus has numerator \(H^2+J^2+2HJ\cos(2\pi\omega)\) and positive denominator
\[
(1-2q\cos(2\pi\omega)+q^2)
(1-2r\cos(2\pi\omega)+r^2).
\]
For every fixed \(y\), the numerator is nondecreasing and the denominator strictly decreasing as \(\cos(2\pi\omega)\) rises from \(-1\) to \(1\). At least one of \(H,J\) is nonzero, so \(|Zg(y,\omega)|^2\) increases strictly. Hence all lower/upper extrema of \(S\) occur at \(\omega=1/2\) and \(\omega=0\), respectively, reducing the two-dimensional optimization to one variable.

**2. Exact upper bound.** The Zak transform at integer frequency is
\[
Zg(y,0)=\frac{e^{-ay}}{1-e^{-a}}+\frac{e^{-b(1-y)}}{1-e^{-b}}.
\]
Consequently \(S(x,0)=\sum_j(\widetilde u_je^{-ax}+\widetilde v_je^{bx})^2\). Each positive summand is strictly convex in \(x\), hence so is \(S(x,0)\). Zak quasi-periodicity and the translated sum imply \(S(0,0)=S(1/m,0)\). A strictly convex function on this closed interval has its maximum only at the endpoints, giving the stated \(B\).

**3. Unique interior minimum.** The half-period Zak transform is real:
\[
Zg(y,1/2)=\frac{e^{-ay}}{1+e^{-a}}-\frac{e^{-b(1-y)}}{1+e^{-b}}.
\]
Thus its sum of squares is \(F(x)=Ue^{-2ax}+Ve^{2bx}-2Ce^{(b-a)x}\). Differentiation yields
\[
F'(x)=2e^{-2ax}\left[-aU+(a-b)C e^{(a+b)x}
+bV e^{2(a+b)x}\right].
\]
For \(t=e^{(a+b)x}>0\), the bracket is a quadratic with positive leading coefficient and negative constant term, so it has **exactly one positive root**. Its explicit root is \(t_*\) above; the derivative changes from negative to positive there. The boundary values satisfy \(F(0)=F(1/m)\) by the same Zak quasi-periodicity. The function cannot be constant because it has at most one stationary point, with a strict derivative sign change. Therefore the stationary point is inside \((0,1/m)\), and it is the unique global minimum.

For \(m\ge2\), the positive vectors \((u_j)_j\) and \((v_j)_j\) are linearly independent: their coordinate ratios form a strictly changing geometric progression with common ratio \(e^{-(a+b)/m}\). Thus \(C^2<UV\), and the squared norm \(F(x)=\|e^{-ax}u-e^{bx}v\|_2^2\) is positive for all real \(x\). This proves \(A>0\) and finishes the exact sharp frame inequality. Sharpness of the bounds follows by taking Zak-domain functions concentrated in arbitrarily small neighborhoods of the continuous extremizing fibers. The frame is not tight because its symbol is strictly increasing in the cosine of the frequency for every spatial fiber, so \(A<B\).

## Verification
The accompanying `verify.py` evaluates the closed formulas and the directly summed complex Zak transform on 240 parameter triples, with redundancy \(m\in\{2,3,4,6,10,25\}\), randomly chosen positive decay rates, and 20 additional Zak fibers for each triple. It checks all four boundary/Zak identities, the strict location of the lower-frequency minimizing fiber, the global finite-grid inequality, and an independent scalar minimization, giving `VERIFY_OK 4800 complex-Zak direct comparisons across 240 parameter triples`. The checks use Python, NumPy, and SciPy. These computations are not a proof for all parameters; the geometric-series identity, monotonicity, and quadratic root above are the proof.

## Relationship to prior work
De Dios Pont, Gröchenig, Liehr, Shafkulovska and Taylor (2026, arXiv:2608.04992v1) prove the **qualitative** sharp frame-set criterion for continuous integrable totally positive windows, including all asymmetric two-sided exponentials; they do not state the optimal frame-bound formula above. The earlier Gröchenig--Stöckler finite-type theorem also establishes qualitative existence. Faulhuber--Shafkulovska (2023, *Gabor frame bound optimizations*) explicitly study **even** two-sided exponentials \(e^{-\gamma|t|}\) and their optimal rectangular lattices, not the two-independent-rate \((a,b)\) family and unique Zak spectral-edge location here. Kloos--Stöckler (2014) similarly give frame existence and near-critical estimates for even two-sided exponential windows. Related exact translated-grid **sampling** inequalities in shift-invariant spaces are different operators from the full time-frequency Gabor frame operator analyzed here. All standard Zak diagonalization and geometric-series identities are acknowledged as established methods, not new lemmas.

## Limitations
The family has only one break point and exponential decay with two positive rates. Its exact bounds are obtained only for translation step \(1/m\), integer \(m\ge2\), and modulation step one. They are **not** a complete quantitative solution for all totally positive windows or arbitrary noninteger redundancy. Other authors may have derived equivalent formulas in earlier classical frame-bound calculations not indexed by the searches performed; mathematical originality has not been independently audited. The finite verifier is only a consistency check. Normalization and lattice conventions matter: multiplying the window by a constant multiplies both squared frame bounds by its squared modulus.

## References
1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1, submitted 2026-08-05. https://arxiv.org/abs/2608.04992.
2. K. Gröchenig and J. Stöckler, *Gabor Frames and Totally Positive Functions*, Duke Mathematical Journal 162 (2013), 1003--1031, arXiv:1104.4894. https://doi.org/10.1215/00127094-2141944.
3. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, Applied and Computational Harmonic Analysis 67 (2023), 101574, arXiv:2204.02917. https://doi.org/10.1016/j.acha.2023.101574.
4. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, Journal of Approximation Theory 184 (2014), 209--237, arXiv:1311.7359. https://doi.org/10.1016/j.jat.2014.05.010.
