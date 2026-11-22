# Exact three-step displacement law and a sixty-fold uniformization in the orthogonal tents map

## Finding

On the two-torus, let the symmetric orthogonal tents map be
\[
f(t)=2\min(\{t\},1-\{t\}),\qquad
H(x,y)=\bigl(\{x+f(y)\},\{y+f(\{x+f(y)\})\}\bigr).
\]
Start \((X_0,Y_0)\) in normalized Haar area, put \((X_n,Y_n)=H^n(X_0,Y_0)\), and define the circle-valued horizontal displacement \(\Delta_n=\{X_n-X_0\}\). At times \(n=1\) and \(n=2\), \(\Delta_n\) is exactly Haar-uniform. At time \(n=3\) its distribution is **not uniform**. It has the explicit, strictly positive, symmetric, continuous, piecewise-linear density
\[
\boxed{p_3(t)=1-\frac12\sum_{r\in R}d_r B_2(\{t-r\}),\qquad B_2(u)=u^2-u+\frac16,\quad 0\le u<1,}
\]
where the following table specifies *every* knot and coefficient:

| \(r\) | \(d_r\) |
|---|---|
| \(0\) | \(2524/1225\) |
| \(1/6,5/6\) | \(-432/1225\) each |
| \(1/5,4/5\) | \(-250/441\) each |
| \(1/4,3/4\) | \(-128/225\) each |
| \(1/3,2/3\) | \(-486/245\) each |
| \(2/5,3/5\) | \(250/441\) each |
| \(1/2\) | \(41344/11025\) |

In particular, \(\sum_{r\in R}d_r=0\); thus the quadratic terms cancel on each interval between adjacent knots. The sharp range is
\[
\boxed{\min_{t\in\mathbb T}p_3(t)=\frac{893}{1225}\quad(t=1/2),\qquad
\max_{t\in\mathbb T}p_3(t)=\frac{352}{315}\quad(t=1/4,3/4).}
\]
For every nonzero integer \(k\), the complete Fourier law is
\[
\boxed{\mathbb E\,e^{2\pi i k\Delta_3}
=-\frac1{4\pi^2k^2}\sum_{r\in R}d_r e^{2\pi i k r}.}
\]
Its zero set is **exactly**
\[
\boxed{\mathbb E\,e^{2\pi i k\Delta_3}=0\ \Longleftrightarrow\ 60\mid k\qquad(k\in\mathbb Z\setminus\{0\}).}
\]
Consequently \(\{60\Delta_3\}\) is precisely Haar-uniform, and **60 is the smallest positive integer multiplier** with that property. For example,
\[
\boxed{\mathbb E\,e^{2\pi i\Delta_3}=
\frac{6250\sqrt5+646}{44100\pi^2}>0.}
\]
This is a stationary finite-time transport law, not a claim of independence of the initial and final coordinates.

## Assumptions and scope

The state space is \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\); every brace denotes fractional part. Both tent shears are continuous circle-valued and preserve normalized area separately, so their composition preserves Haar area. The law concerns Haar-distributed initial conditions, not arbitrary deterministic initial points. The Fourier statement is for every nonzero integer frequency without a bandwidth cutoff; the density statement is for every point of the circle and the three-step horizon only. Branch-boundary conventions affect neither law nor any area integral, since the union of their preimages through a fixed number of iterates has Haar measure zero. The smallest multiplier is taken among all positive integers.

## Proof

**The first two steps.** The tent function \(f\) maps uniform circle measure to uniform circle measure: almost every output in \((0,1)\) has two inverse branches, each of inverse Jacobian \(1/2\). For one step, \(\Delta_1=f(Y_0)\), hence it is Haar-uniform. Put \(U=\{X_0+f(Y_0)\}\) and \(V=\{Y_0+f(U)\}\). Conditional on \(Y_0\), translation in the independent uniform variable \(X_0\) makes \(U\) Haar-uniform. Therefore \(f(U)\) is conditionally Haar-uniform, \(V\) is conditionally Haar-uniform, and so is \(f(V)\). As \(\Delta_2=\{f(Y_0)+f(V)\}\), its conditional distribution given \(Y_0\) is Haar-uniform. This proves the first two assertions for all Fourier frequencies, not just finitely many.

**Exact rational partition at the third step.** Work on the original unit square in initial variables \((u,v)\). On each open polygonal itinerary cell, maintain three objects: its exact rational polygon \(P\), an affine lift \(x(u,v)\) of the horizontal coordinate, and an affine lift \(y(u,v)\) of the vertical coordinate. Initially these are the unit square and \(x=u,y=v\). For an affine input \(s(u,v)\), split the polygon at *every* line \(s=j/2\), with integer \(j\), and retain each nonzero-area intersection with \(j/2<s<(j+1)/2\). On that strip the periodic tent equals \(2s-j\) when \(j\) is even and \(-2s+j+1\) when \(j\) is odd. First replace \(x\) by \(x+f(y)\) through that polygon split; then replace \(y\) by \(y+f(x)\) through a second split. Repeat for three full steps. Each split is exact rational convex-polygon clipping, so this is an exhaustive decomposition up to measure-zero boundaries. The resulting numbers of positive-area cells are exactly \(8\), \(56\) and \(320\); their total area is exactly one at every step.

On each final cell \(P\), write its *unwrapped* displacement as \(g(u,v)=x_3(u,v)-u=au+bv+c\), with integers \(a,b,c\). For nonzero integer \(k\), put \(\tau=2\pi i k\). When \((a,b)\ne(0,0)\), the divergence theorem gives the identity
\[
\int_P e^{\tau g}\,du\,dv
=\frac1{\tau(a^2+b^2)}\sum_{e:v\to w}
\bigl(a(w_2-v_2)-b(w_1-v_1)\bigr)
\int_0^1e^{\tau[g(v)+s(g(w)-g(v))]}\,ds.
\]
A constant displacement contributes \(\operatorname{area}(P)e^{\tau c}\). The edge integral is either \(e^{\tau g(v)}\) when \(g(w)=g(v)\), or \((e^{\tau g(w)}-e^{\tau g(v)})/[\tau(g(w)-g(v))]\) otherwise. All coefficients are rational, as are all endpoint phases. Because \(e^{2\pi i k m}=1\) for every integer \(m\), phases can be grouped by their exact fractional parts.

The exhaustive \(320\)-cell rational sums have no contributions of order \(\tau^0\) or \(\tau^{-1}\). Their order-\(\tau^{-2}\) term is precisely
\[
\sum_{r\in R}d_r e^{\tau r},
\]
with the twelve rational coefficients in the table. Therefore \(\mathbb E e^{\tau\Delta_3}=\tau^{-2}\sum_r d_r e^{\tau r}\), establishing the Fourier formula **for every integer \(k\ne0\)**. The supplied standalone checker independently performs the entire rational partition, edge integration and aggregation: it does not supply the coefficients as data for their derivation. In particular it verifies the absence of the lower-order terms and the exact displayed coefficient table. This is a finite exhaustive rational-algebra calculation, not statistical sampling or a finite-frequency extrapolation.

**Density and extrema.** The periodic second Bernoulli polynomial has nonzero complex Fourier coefficients \(1/(2\pi^2k^2)\). Hence the displayed continuous function \(p_3\) has exactly the computed Fourier coefficients, together with zeroth coefficient one. Uniqueness of Fourier–Stieltjes coefficients identifies it as the entire displacement measure. Since the sum of coefficients \(d_r\) is zero, its quadratic pieces have zero second derivative away from the knots. Evaluating the displayed rational formula at all twelve rational knots gives the exact minimum \(893/1225\) at \(1/2\) and exact maximum \(352/315\) at \(1/4\) and \(3/4\); piecewise affinity proves these are the global extrema. Positivity everywhere also follows.

**The exact arithmetic zero set.** The coefficients obey \(d_r=d_{1-r}\). Accordingly the Fourier numerator is real and equals
\[
\begin{aligned}
S(k)={}&\frac{2524}{1225}+\frac{41344}{11025}(-1)^k
-\frac{864}{1225}\cos\frac{\pi k}{3}
-\frac{500}{441}\cos\frac{2\pi k}{5}\\
&-\frac{256}{225}\cos\frac{\pi k}{2}
-\frac{972}{245}\cos\frac{2\pi k}{3}
+\frac{500}{441}\cos\frac{4\pi k}{5}.
\end{aligned}
\]
Each term has an integer period dividing \(60\). Direct exact reduction of the \(60\) residue classes in the field \(\mathbb Q(\sqrt5)\)—using only \(\cos(2\pi/5)=(\sqrt5-1)/4\), \(\cos(4\pi/5)=-(\sqrt5+1)/4\), and elementary half- and third-turn cosine values—shows \(S(k)=0\) only for \(k\equiv0\pmod{60}\). These exact residue comparisons are reproduced independently in the checker as rational pairs representing \(a+b\sqrt5\). Multiplication by \(60\) therefore erases every nontrivial Fourier coefficient, making \(\{60\Delta_3\}\) Haar-uniform by uniqueness; if any smaller integer multiplication were Haar-uniform, its first harmonic would force a forbidden zero \(S(k)=0\). Substituting \(k=1\) gives the displayed positive first harmonic.

## Verification

Run `python3 check.py` in a directory containing the supplied standalone Python file. Only the Python standard library is required. The checker reconstructs all \(320\) positive-area polygon pieces with `fractions.Fraction`, establishes exact total area, groups all boundary flux terms, verifies the twelve rational coefficients and both vanishing lower-order sums, checks the first Fourier harmonic, verifies all sixty arithmetic residue cases exactly in \(\mathbb Q(\sqrt5)\), and determines the sharp density extrema by rational arithmetic. In the checked package it prints three `PASS` lines. The analytic first-/second-step arguments and the Fourier and polygon identities above establish the theorem; the complete finite exact calculation establishes the specific rational coefficient table. Neither numerical quadrature nor Monte Carlo is used for acceptance.

## Relationship to prior work

The orthogonal composition of two nonmonotone shears and its symmetric tent endpoint were introduced by Myers Hill, Sturman and Wilson in *Exponential Mixing by Orthogonal Non-Monotonic Shears*, first public arXiv posting 2021-12-10. That paper analyzes hyperbolicity, Bernoulli behavior and exponential decay in open parameter windows, and notes the special symmetric endpoint. Their 2023 *Loss of Exponential Mixing in a Non-Monotonic Toral Map* establishes polynomial correlation decay at this endpoint. The 2022 thesis *Mixing in the Presence of Non-Monotonicity* analyzes the same map's dynamical partition, parabolic behavior and induced return estimates. The inspected portions of these primary sources do not contain the present exact finite-three-step displacement density, its rational knot table, or its minimal sixty-fold uniformization.

Periodic-point counts and published calculations of this map's parabolic residence-time areas concern different invariants and do not imply the stationary displacement law. A published two-step Fourier law for a **different** one-tent-plus-linear-shear toral map shares the method of Fourier analysis and also exhibits a uniform displacement at lag two, but does not determine the third-step law for the orthogonal *two-tent* map. The present result uses standard polygon clipping and Fourier inversion but supplies their particular exact closed-form consequences. The inspected literature and indexed comparison do not establish publication priority against all unindexed calculations.

## Limitations

The statement is confined to the exact symmetric orthogonal tents map under Haar-distributed initial conditions. It characterizes the three-step horizontal displacement and the exact first two-step uniformity, not the full joint law of \((X_0,X_3)\), higher-step displacement laws, mixing rates, physical dispersion on an unwrapped cover, or neighboring shear parameters. The coincidence of the sixty-fold pushforward with Haar is a statement about one *single-time* marginal, not independence of multiple observations. Finite exact clipping was exhaustively checked for this fixed third-iterate partition, but there is no general closed symbolic formula for arbitrary iterates. Possible equivalent unindexed short-time calculations remain an originality risk; independent audit has not been performed.

## References

1. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Exponential Mixing by Orthogonal Non-Monotonic Shears*, arXiv:2112.05463, first posted 2021-12-10, https://arxiv.org/abs/2112.05463.
2. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515, first posted 2023-03-15, https://arxiv.org/abs/2303.08515.
3. J. D. Myers Hill, *Mixing in the Presence of Non-Monotonicity*, University of Leeds PhD thesis, submitted September 2022, https://etheses.whiterose.ac.uk/id/eprint/32186/1/Thesis_final.pdf (source's first online availability not independently established).
4. *Exact rational residence tails in the orthogonal tents map*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rational-residence-tails-in-the-orthogonal-tents-map--0aa48787a5cd.
5. *Two-step Fourier law and hidden dependence in a non-monotonic toral shear*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-step-fourier-law-and-hidden-dependence-in-a-non-monotonic-to--b67848c6bf78.
