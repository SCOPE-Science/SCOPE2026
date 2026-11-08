# Exact cube affine-projection norms and a second-order stability law

## Finding

Let \(d\ge3\) be an integer and let \(P_d\) be real \(L^2\)-orthogonal projection, with normalized uniform volume measure, onto all affine functions on the cube \(Q_d=[-1,1]^d\). Its sharp \(L^\infty\)-operator norm \(\Lambda_d\) is the following **rational number**:

\[
\boxed{\Lambda_d=1+\frac{2}{6^d(d+1)!}
 \sum_{k=0}^{\lfloor(3d-1)/6\rfloor}(-1)^k\binom dk
 (3d-1-6k)^{d+1}.}
\]

Only the \(2^d\) vertices of \(Q_d\) are norming evaluation points. The complete norming inputs (modulo null sets) are \(f(y)=\pm\operatorname{sgn}(1+3v\cdot y)\) for some cube vertex \(v\). Moreover, among \(0\le f\le1\), the exact smallest value of \((P_df)(x)\), optimized over \(x\in Q_d\), is \(-(\Lambda_d-1)/2\); sharp witnesses at a vertex \(v\) are the indicators of \(\{y:1+3v\cdot y<0\}\).

The sequence of sharp norms is strictly increasing, with the **exact dimension-increment identity**

\[
\boxed{\Lambda_{d+1}-\Lambda_d=
 \frac16\,\mathbb E\left[(3-|1+3S_d|)_+^2\right]>0,\qquad
 S_d=\sum_{i=1}^{d}U_i,\quad U_i\overset{\rm iid}{\sim}\operatorname{Unif}[-1,1].}
\]

Its two-term high-dimensional asymptotic is

\[
\boxed{\Lambda_d=\sqrt{\frac{6d}{\pi}}
\left(1+\frac{13}{60d}+O(d^{-2})\right).}
\]

The results also hold for any nondegenerate axis-parallel box, by an invertible affine change of coordinates. For context, the one- and two-dimensional specializations \(\Lambda_1=5/3\) and \(\Lambda_2=233/108\) are **not claimed as new**; the planar square is already a case of the previously studied regular-polygon affine projector.

## Assumptions and scope

Every function and coefficient is real. The measure is normalized Lebesgue volume on the whole cube, not surface area, vertex counting measure, or an empirical sampling measure. The map \(P_d:L^\infty(Q_d)\to L^\infty(Q_d)\) takes inputs to their real affine \(L^2\) projections. Equalities for extremizing inputs are interpreted almost everywhere. The dimension is any integer \(d\ge3\), with lower-dimensional values displayed only as consistency checks. No claim concerns higher-degree polynomials or arbitrary product weights.

## Proof

**1. Kernel and norming points.** Under normalized cube volume the functions \(1,\sqrt3 y_1,\ldots,\sqrt3 y_d\) form an orthonormal basis for the affine subspace. Hence

\[
(P_df)(x)=\int_{Q_d}(1+3x\cdot y)f(y)\,d\mu_d(y),\qquad
\lambda_d(x)=\int_{Q_d}|1+3x\cdot y|\,d\mu_d(y).
\]

By separate convexity of \(\lambda_d\) in the coordinates of \(x\), a maximum occurs at a cube vertex. To exclude all other maximizers, fix a coordinate \(i\) for which \(|x_i|<1\) and replace each remaining coordinate by a signed endpoint without reducing \(\lambda_d\). By symmetry it suffices to study

\[
\Phi(t)=\mathbb E|W+3tU|,\quad 0\le t\le1,\qquad
 W=1+3\sum_{j=1}^{d-1}U_j,
\]

where \(U,U_1,\ldots,U_{d-1}\) are independent uniforms on \([-1,1]\). For a fixed real \(w\) and \(t>0\), elementary integration gives

\[
\mathbb E_U|w+3tU|=
\begin{cases}|w|,&|w|\ge3t,\\[2pt]
(9t^2+w^2)/(6t),&|w|<3t.
\end{cases}
\]

The right side is nondecreasing in \(t\), and is strictly increasing whenever \(3t>|w|\). For \(d\ge2\), \(W\) has a density strictly positive in a neighborhood of zero, so \(\Phi(1)>\Phi(t)\) for every \(t<1\). This excludes all nonvertex maximizers. All vertices have the same value by coordinate reflections. Since \(K(v,y)=1+3v\cdot y\) is nonzero except on a null hyperplane, equality in the integral triangle inequality forces \(f(y)=\pm\operatorname{sgn}K(v,y)\) almost everywhere, proving the norming-input classification.

**2. Exact formula.** At a vertex, coordinate reflections give

\[
\Lambda_d=\mathbb E|1+3S_d|=1+6\mathbb E(S_d-1/3)_+.
\]

Writing \(S_d=2Z_d-d\), where \(Z_d\) is the sum of \(d\) independent \(\operatorname{Unif}[0,1]\) variables, the standard inclusion-exclusion formula for the Irwin--Hall tail yields, for every real \(b\),

\[
\mathbb E(Z_d-b)_+=\frac1{(d+1)!}
\sum_{k=0}^d(-1)^k\binom dk (d-k-b)_+^{d+1}.
\]

Substitute \(b=(d+1/3)/2\). Only indices \(0\le k\le\lfloor(3d-1)/6\rfloor\) survive, giving exactly the rational formula above. There is no numerical interpolation, truncation, or asymptotic approximation in this identity.

**3. Increment and positivity.** Conditioning on a further uniform \(U\), the elementary formula in step 1 with \(t=1\) gives, pointwise for every \(w\in\mathbb R\),

\[
\mathbb E_U|w+3U|-|w|=\tfrac16(3-|w|)_+^2.
\]

Putting \(w=1+3S_d\) proves the increment identity. Its expectation is strictly positive because \(S_d\) has positive probability in the open interval \((-4/3,2/3)\). The reproducing kernel integrates to \(1\) for every \(x\); consequently its negative mass is \((\lambda_d(x)-1)/2\). Minimizing against \(0\le f\le1\), and then maximizing the negative mass over \(x\), proves the stated exact positivity defect and witnesses.

**4. Second-order asymptotic.** The characteristic function of \(S_d\) is \((\sin t/t)^d\). The exact absolute-moment identity reads

\[
\mathbb E|S_d|=\frac2\pi\int_0^\infty
\frac{1-(\sin t/t)^d}{t^2}\,dt.
\]

On the scale \(t=u/\sqrt d\), the expansion

\[
(\sin(u/\sqrt d)/(u/\sqrt d))^d=e^{-u^2/6}
\left[1-\frac{u^4}{180d}+O\left(\frac{u^6+u^8}{d^2}\right)\right]
\]

holds uniformly on growing bounded windows; integration with a Gaussian weight gives

\[
\mathbb E|S_d|=\sqrt{\frac{2d}{3\pi}}
\left(1+\frac1{20d}+O(d^{-2})\right).
\]

For completeness, this integration is justified by choosing \(0\le u\le d^{1/10}\) for the Taylor remainder. In \(d^{1/10}<u<c\sqrt d\), use \(|\sin t/t|\le e^{-c_1t^2}\) for a fixed positive \(c_1\) and sufficiently small fixed \(c\). On the remaining interval, split \(c\le t\le2\) and \(t\ge2\), where \(|\sin t/t|\le q<1\) on the first and \(|\sin t/t|\le1/t\) on the second. These bounds make the neglected integral exponentially small, giving the displayed uniform integrated remainder.

Let \(p_d\) be the density of \(S_d\). Fourier inversion by the same argument (using the integrable characteristic function for \(d\ge2\)) gives

\[
p_d(u)=\sqrt{\frac3{2\pi d}}\,[1+O(d^{-1})]
\quad\text{uniformly for }|u|\le1/3.
\]

By symmetry and the identity \(\partial_a^2\mathbb E|S_d+a|=2p_d(a)\),

\[
\mathbb E|S_d+1/3|-\mathbb E|S_d|
=2\int_0^{1/3}(1/3-u)p_d(u)\,du
=\frac19\sqrt{\frac3{2\pi d}}+O(d^{-3/2}).
\]

Finally \(\Lambda_d=3\mathbb E|S_d+1/3|\). The absolute-moment contribution \(1/(20d)\) and the shift contribution \(1/(6d)\) add to \(13/(60d)\), with relative error \(O(d^{-2})\), as claimed.

## Verification

A standalone Python 3 checker, `check_cube_affine.py`, is included. It compares the closed finite binomial sum against an independently integrated piecewise polynomial Irwin--Hall density using exact rational arithmetic in all dimensions from 1 to 18, verifies the low-dimensional specializations, and performs auxiliary finite-dimensional and asymptotic diagnostics. Command: `python3 check_cube_affine.py`. Its execution completed with `ALL_CUBE_AFFINE_PROJECTION_CHECKS_PASSED`. These checks corroborate, but do not substitute for, the universal analytical proof and the asymptotic remainder estimates above.

## Relationship to prior work

The general role of \(L^\infty\)-norms of \(L^2\) projectors in stable approximation is established in Hangelbroek--Narcowich--Sun--Ward (arXiv:1005.2424), which studies local kernel spaces on smooth manifolds, not this degree-one uniform cube projector. The numerical mesh framework of Białas-Cież--Kenne--Sommariva--Vianello (arXiv:2311.18656) includes discrete least-squares and hyperinterpolation examples on squares but gives no all-dimensional exact rational law or second-order dimension asymptotic for the present continuous-volume projector. Cohen--Davenport--Leviatan (arXiv:1111.4422) gives empirical least-squares stability conditions; that is a different operator and norm question.

A prior regular-polygon affine-projection result already covers the **two-dimensional square**; a prior Euclidean-ball affine-projection result covers the one-dimensional interval. These are acknowledged, not duplicated as novelty. Earlier finite-alphabet additive product projection formulas have discrete product supports and subspaces, not the present continuous cube with affine polynomials. The new claim is the complete formula and strict growth mechanism for every \(d\ge3\), together with a corrected high-dimensional asymptotic and complete norming geometry. The arXiv preprint 1005.2424 was first made public on 2010-05-13; dates on later versions and journal publication are not used as its earliest source date.

## Limitations

Only affine real projection under normalized uniform **volume** on a cube or box is treated. The exact norm and positivity defect depend on this chosen measure and polynomial space. No claim is made for nonlinear polynomial degrees, the discrete vertex-measure hypercube, weighted product densities, arbitrary convex bodies, complex-coefficient interpolation, or operator norms for other exponent pairs. The novelty comparison is subject to incomplete bibliographic indexing; independent expert assessment has not been performed.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The L-infinity-norm of the L2-projector*, arXiv:1005.2424 (first publicly posted 2010-05-13), https://arxiv.org/abs/1005.2424.
2. A. Cohen, M. A. Davenport, D. Leviatan, *On the stability and accuracy of least squares approximations*, arXiv:1111.4422 (first publicly posted 2011-11-18), https://arxiv.org/abs/1111.4422.
3. L. Białas-Cież, D. J. Kenne, A. Sommariva, M. Vianello, *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex and ball*, arXiv:2311.18656 (first publicly posted 2023-11-30), https://arxiv.org/abs/2311.18656.
4. Irwin--Hall inclusion-exclusion density for sums of independent uniform variables (classical formula; used as a standard input, not claimed new).
