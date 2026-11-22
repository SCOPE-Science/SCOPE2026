# Boundary spectral outliers in cubic Schoenberg–Greville averaging

## Finding
Let \(n\ge4\) and let \(S_n\) be the classical clamped uniform degree-three Schoenberg operator on \([0,n]\), with knots \(0,0,0,0,1,2,\ldots,n-1,n,n,n,n\) and Greville sampling sites. The nontrivial finite-dimensional spectrum contains \(n+1\) positive, simple eigenvalues strictly below \(1\), in addition to the double eigenvalue \(1\) corresponding to affine functions.

Exactly one of those eigenvalues lies in \((0,1/3)\) when \(4\le n\le7\); exactly one lies there and another equals \(1/3\) when \(n=8\); and exactly two lie in \((0,1/3)\) for every \(n\ge9\). These are the two lowest eigenvalues for \(n\ge9\); all remaining nontrivial eigenvalues exceed \(1/3\).

Put \(p(s)=9-10s+s^2-4s^3\), \(q(s)=4-s+10s^2-9s^3\), and let \(s_*\in(0,1)\) be the unique root of \(p\). Then \(s_*=0.774277225966546\ldots\) and the two lowest eigenvalues \(\lambda_{1,n}<\lambda_{2,n}\) for \(n\ge9\) both converge to
\[
\lambda_* = \frac{4-s_*-s_*^{-1}}6=0.322365950030849\ldots.
\]
Their splitting satisfies the sharp limit
\[
\lim_{n\to\infty}\frac{\lambda_{2,n}-\lambda_{1,n}}{s_*^{\,n-1}}=
\frac{(s_*^{-2}-1)q(s_*)}{3[-p'(s_*)]}
=0.071778232687578\ldots.
\]
Thus a finite-cell threshold precedes two exponentially coupled, boundary-localized spectral modes below the interior cubic cardinal-spline band \([1/3,1]\).

## Assumptions and scope
The degree is precisely three, all mesh cells have equal positive length, and endpoints have multiplicity four. A common rescaling from \([0,n]\) to \([0,1]\) leaves the matrix and its spectrum unchanged. For \(N_i\), \(0\le i\le n+2\), the normalized cubic B-spline basis with the stated clamped knots, set \(\xi_i=(t_{i+1}+t_{i+2}+t_{i+3})/3\) and \((S_nf)(x)=\sum_{i=0}^{n+2}f(\xi_i)N_i(x)\). No positivity or spectral claim is made for changing the knot spacings, a different sampling rule, or degrees other than three. The zero eigenvalue of \(S_n\) on the infinite-dimensional space \(C([0,n])\) is not included among the finite-dimensional nontrivial eigenvalues.

## Proof
**1. Exact collocation matrix.** The nonzero spectrum of \(S_n\) is that of \(B=(N_j(\xi_i))_{i,j=0}^{n+2}\). Its first and last rows are identity endpoint rows. Removing their indices leaves an \((n+1)\)-square matrix \(T_n\). Index its rows and columns by \(1,\ldots,m\), where \(m=n+1\). Its first row has entries \(61/108,43/324,1/162\) in columns \(1,2,3\); its second row has entries \(1/4,7/12,1/6\) in columns \(1,2,3\); every row \(3\le j\le m-2\) has entries \(1/6,2/3,1/6\) in columns \(j-1,j,j+1\). The last two rows are reversals of the first two. These values follow by substituting the Greville sites \(0,1/3,1,\ldots,n-1,n-1/3,n\) in the cubic Cox–de Boor recurrence.

B-spline collocation matrices are totally nonnegative. The principal block \(T_n\) is nonsingular by strict row diagonal dominance; its adjacent super- and sub-diagonal entries are strictly positive. Therefore it is an oscillatory totally nonnegative matrix and has \(m\) distinct positive real eigenvalues. The endpoint-positive Markov matrix \(B\) fixes affine functions, giving exactly two occurrences of eigenvalue \(1\); since \(T_n\) is an irreducible substochastic matrix with a strictly deficient boundary row, its spectral radius is strictly below \(1\). (The oscillatory-matrix conclusion is the classical Gantmacher–Krein criterion.)

**2. Exact subband equations.** For \(0<\lambda<1/3\), put \(s\in(2-\sqrt3,1)\) so that \(\lambda=(4-s-s^{-1})/6\). In interior rows the eigenvalue equation is the second-order recurrence \(v_{j+1}=(6\lambda-4)v_j-v_{j-1}\), with characteristic roots \(-s\) and \(-1/s\). Elimination of the first two rows yields the scalar left boundary condition
\[
v_3=h(\lambda)v_2,\qquad h(\lambda)=6\lambda-\frac72-\frac32\frac{\lambda+3}{27\lambda-15}.
\]
The right boundary is its reflection. Because \(T_n\) commutes with reversal and has simple eigenvalues, every eigenvector has definite reflection parity. Substituting the two exponential solutions in the two boundary equations gives exactly one of the scalar equations
\[
p(s)-s^{\,n-1}q(s)=0,\qquad p(s)+s^{\,n-1}q(s)=0.
\]
Indeed the identity \((h(-s)-(-s))/(1+s h(-s))=-p(s)/(s^2q(s))\), with \(h(-s)\) denoting substitution of \(\lambda=(4-s-s^{-1})/6\) into \(h\), gives the two equations after multiplying by \(s^{n-1}\). Conversely, every solution inside \((2-\sqrt3,1)\) constructs a nonzero eigenvector by the two-exponential ansatz; neither boundary elimination has a pole in this interval.

**3. Exact root counts.** For \(0<s<1\), \(q(s)=4-s+s^2(10-9s)>0\). Direct differentiation gives
\[
\left(\frac{p}{q}\right)'=-\frac{31(1-s)^4+296s(1-s)^2+112s^2}{q(s)^2}<0.
\]
Also \(p'(s)=-10+2s-12s^2<0\), so \(p\) has one root \(s_*\in(0,1)\). Since \(p(2-\sqrt3)>q(2-\sqrt3)>0\) and \(p(s_*)=0\), the first equation has exactly one root in \((2-\sqrt3,s_*)\) for every \(n\ge4\).

For the second equation consider \(R(s)=-p(s)/q(s)>0\) on \((s_*,1)\), and its logarithmic elasticity \(K(s)=sR'(s)/R(s)\). A direct differentiation gives
\[
K'(s)=\frac{12(s-1)(s+1)E(s)}{p(s)^2q(s)^2}<0,
\]
where, with \(u=s+s^{-1}-2\ge0\),
\[
E(s)=s^4(93u^4+1776u^3+4528u^2+3200u+2560)>0.
\]
Thus \(K\) decreases from \(+\infty\) to \(K(1)=7\). The equation \(R(s)=s^{n-1}\) has no interior root if \(n\le8\), and exactly one if \(n\ge9\): the logarithmic ratio begins at zero, ends at one, and its derivative changes sign exactly once when \(n-1>7\). At \(\lambda=1/3\) the interior recurrence has the repeated root \(-1\), hence \(v_j=(-1)^{j-2}(A+B(j-2))\). The left boundary forces \(B=-A/3\), and the right boundary then holds precisely when \(n=8\). This proves all stated finite-size counts.

**4. Exponential splitting.** Because \(p'(s_*)<0\), the implicit-function expansion at the simple root of \(p\) gives the lower and upper solutions, respectively,
\[
s_{1,n}=s_*+\frac{q(s_*)}{p'(s_*)}s_*^{n-1}+O(ns_*^{2n-2}),\quad
s_{2,n}=s_*-\frac{q(s_*)}{p'(s_*)}s_*^{n-1}+O(ns_*^{2n-2}).
\]
The function \(\lambda(s)=(4-s-s^{-1})/6\) has derivative \((s^{-2}-1)/6>0\). Applying the mean-value theorem to the two roots proves the displayed sharp splitting constant. The exponential solutions also show spatial localization near the two boundary collars.

## Verification
The standalone `checker.py` reconstructs \(T_n\) directly from its rational entries and separately checks those entries using the exact Cox–de Boor recursion, verifies the critical polynomial identities symbolically, checks exact rational determinants at \(\lambda=1/3\) for \(4\le n\le12\), and compares numerical eigenvalues against both root equations for \(4\le n\le41\). It prints the limiting algebraic constants and the finite-size splitting ratios. These finite tests do not substitute for the complete analytical root-count argument.

## Relationship to prior work
Nagler, Cerejeiras and Forster (first public arXiv version 11 February 2014) establish general spectral and iterated-convergence properties of Schoenberg operators, and explicitly state that their individual eigenvalues and eigenfunctions were unknown; they do not analyze the cubic subband edge or its finite-size threshold. Nagler and Kähler (first public arXiv version 19 December 2013) establish approximation and iteration bounds, not the cubic low-spectrum classification. The standard total-positivity theory of B-spline collocation supplies the oscillatory-matrix lemma. Later work on generalized-spline isogeometric collocation treats differential-operator eigenproblems, whose matrices are not the positive averaging matrix studied here. A prior explicit quadratic uniform case has different interior coefficients and does not imply the cubic boundary transition.

## Limitations
This is an exact statement about the fixed cubic averaging matrix and its spectral bottom, not a general spline-degree theorem, a theorem for arbitrary meshes, or a convergence-rate theorem for the second-largest eigenvalue. The larger part of the finite spectrum is not tabulated here. Originality is a best-knowledge comparison with accessible research; an unindexed earlier computation of the identical edge polynomial remains possible. There is no independent mathematical audit.

## References
1. J. Nagler, P. Cerejeiras, B. Forster, *Lower bounds for the approximation with variation-diminishing splines*, arXiv:1402.2403v1 (11 February 2014), https://arxiv.org/abs/1402.2403.
2. J. Nagler, U. Kähler, *A lower bound for the uniform Schoenberg operator*, arXiv:1312.5546v1 (19 December 2013), https://arxiv.org/abs/1312.5546.
3. C. de Boor, *A Practical Guide to Splines*, Springer, 1978 (B-spline recursion and collocation).
4. M. S. Floater, *On the positivity of B-spline Wronskians*, Calcolo 61 (2024), article 56, https://doi.org/10.1007/s10092-024-00613-0 (historical B-spline total-positivity context).
5. C. Manni, A. Reali, H. Speleers, *Isogeometric collocation methods with generalized B-splines*, Comput. Math. Appl. 70 (2015), 1659–1675, https://doi.org/10.1016/j.camwa.2015.03.027 (distinct differential-equation collocation problem).
