# A sharp trace-nine inverse-spectral bifurcation for two-pole Hankel operators

## Finding

For real parameters \(0\leq a<b<1\), let \(v_t=(1,t,t^2,\ldots)\in\ell^2(\mathbb N_0)\), with \(v_0=(1,0,0,\ldots)\), and define the positive rank-two Hankel operator
\[
\Gamma_{a,b}=v_a\otimes v_a+v_b\otimes v_b.
\]
Equivalently, its matrix is \((a^{j+k}+b^{j+k})_{j,k\geq0}\), with the value at a zero base and exponent zero interpreted as one. This fixes both atomic coefficients to one, rather than allowing variable masses.

Let \(\lambda_+>\lambda_->0\) be its nonzero eigenvalues and put \(T=\lambda_++\lambda_-\), \(D=\lambda_+\lambda_-\). Then \(T>2\), and the map from the unordered pair of pole locations \(\{a,b\}\) to the two nonzero eigenvalues has the following sharp dichotomy:

1. If \(2<T\leq9\), every attainable spectrum with trace \(T\) identifies exactly one unordered pair \(\{a,b\}\).
2. If \(T>9\), a nonempty open interval of attainable determinants has **exactly three** distinct unordered pole pairs with the same two nonzero eigenvalues. No attainable spectral pair has more than three preimages.

The exact inverse is determined by the pole product \(p=ab\), confined to \(0\leq p<(T-2)/T\), which solves
\[
D=\frac{T-2-Tp}{(1-p)^2(1+p)}. \tag{1}
\]
For \(T>9\), set
\[
p_\pm=\frac{T-3\pm\sqrt{(T-1)(T-9)}}{2T},\qquad
D_\pm=\frac{T-2-Tp_\pm}{(1-p_\pm)^2(1+p_\pm)}.
\]
Every determinant in the nonempty interval \((D_-,\min\{D_+,T-2\})\) has exactly three preimages. At the critical trace \(T=9\), the unique stationary point is a cubic flat point:
\[
D_9(p)=\frac{27}{4}-\frac{729}{64}(p-1/3)^3+O((p-1/3)^4).
\]

## Assumptions and scope

The Hilbert space is complex \(\ell^2(\mathbb N_0)\), and the rank-one convention is \((v\otimes v)x=\langle x,v\rangle v\). The two pole parameters are real, nonnegative, distinct and strictly below one; their masses are **equal and fixed at one**. Eigenvalues are counted without the infinite-dimensional zero eigenspace. The inverse question observes only the two nonzero eigenvalues, not a spectral measure, norming eigenvectors, the shifted Hankel spectrum, or the full moment sequence. The number nine refers to the unnormalized trace \(T\) with unit masses; it is not invariant under rescaling both masses.

The motivating inverse-Hankel framework and the standard Hardy Hankel convention are given in [1] and [2]. This is an explicit two-atom constrained inverse-spectral theorem, not a general statement about arbitrary positive Hankel operators.

## Proof

**Step 1: exact rank-two Gram reduction.** Let \(V:\mathbb C^2\to\ell^2(\mathbb N_0)\) have columns \(v_a,v_b\). Then \(\Gamma_{a,b}=VV^*\), whose two strictly positive eigenvalues are those of
\[
G=V^*V=\begin{pmatrix}
(1-a^2)^{-1}&(1-ab)^{-1}\\
(1-ab)^{-1}&(1-b^2)^{-1}
\end{pmatrix}.
\]
The columns are linearly independent because \(a\ne b\), and the Cauchy–Schwarz inequality is strict. The trace and determinant are therefore
\[
T=\frac1{1-a^2}+\frac1{1-b^2},\quad
D=\frac{(a-b)^2}{(1-a^2)(1-b^2)(1-ab)^2}>0.
\]
In particular \(T>2\), and knowing \((T,D)\) is equivalent to knowing the unordered positive eigenvalue pair.

**Step 2: an exact scalar spectral fiber.** Set \(p=ab\), \(q=a^2+b^2\), and \(\delta=(1-a^2)(1-b^2)=1-q+p^2\). From the trace formula,
\[
T=1+\frac{1-p^2}{\delta},\quad
\delta=\frac{1-p^2}{T-1},\quad
q=\frac{T-2+Tp^2}{T-1}.
\]
The determinant simplifies without approximation:
\[
D=\frac1\delta-\frac1{(1-p)^2}
=\frac{T-2-Tp}{(1-p)^2(1+p)},
\]
which is (1). Conversely, for any \(0\leq p<(T-2)/T\), set
\[
u_\pm=\frac{q\pm\sqrt{q^2-4p^2}}2,\qquad
q^2-4p^2=\frac{(1-p^2)((T-2)^2-T^2p^2)}{(T-1)^2}>0.
\]
These are the two distinct nonnegative numbers \(a^2,b^2\). Their product is \(p^2<1\), while \((1-u_+)(1-u_-)=(1-p^2)/(T-1)>0\); hence both \(u_\pm<1\). The ordered choice \(a=\sqrt{u_-}\), \(b=\sqrt{u_+}\) is uniquely determined. Conversely, any admissible \(a<b\) must have \(p<(T-2)/T\) by the displayed discriminant and the trace formula. Thus the scalar parameter interval parametrizes every unordered pole pair **bijectively**, including the endpoint \(p=0\), and the only excluded upper endpoint corresponds to coincident poles and rank one.

**Step 3: sharp inversion transition.** Differentiate (1):
\[
\frac{dD_T}{dp}=-\frac{2Q_T(p)}{(1-p)^3(1+p)^2},\quad
Q_T(p)=Tp^2+(3-T)p+1.
\]
Its discriminant is \((T-1)(T-9)\). When \(2<T<9\), \(Q_T>0\) on the entire parameter interval. At \(T=9\), \(Q_9(p)=9(p-1/3)^2\), so \(D_T\) remains strictly decreasing despite one stationary point. Since \(D_T(0)=T-2\) and \(D_T(p)\to0\) at the excluded upper endpoint, each attainable determinant gives exactly one pole pair.

When \(T>9\), the two roots \(p_-<p_+\) displayed above both lie strictly between zero and \((T-2)/T\). Since \(Q_T\) has sign pattern \(+,-,+\), the determinant decreases strictly from \(T-2\) to \(D_-\), then increases strictly to \(D_+\), then decreases strictly to zero. Hence each \(D\in(D_-,\min\{D_+,T-2\})\) has exactly one preimage on **each** of the three monotone branches. Cross-multiplication in (1) gives a cubic equation for \(p\), so no spectral fiber can contain four or more preimages. Finally, directly differentiating once more at \(T=9,p=1/3\) gives the displayed cubic expansion; its first and second derivatives vanish and its third derivative is \(-2187/32\). This proves all assertions.

## Verification

The standalone `check.py` uses exact rational arithmetic to verify the trace–determinant reduction and inverse discriminant identity for many distinct rational poles. It separately uses bisection and finite Gram computations to check an explicit threefold fiber. For \(T=12\) and \(D=199/20\), the three pole pairs approximately are
\[
(0.029493012607,0.953458815849),\quad
(0.258384915039,0.953150464649),\quad
(0.766750145030,0.946331644017).
\]
All produce the same positive eigenvalues \((12\pm\sqrt{144-4(199/20)})/2\). Run `python3 check.py` from the directory containing this document. The observed run reported `PASS 3708 assertions`. The proof above, not finite sampling or numerical root finding, establishes the infinite-dimensional result and exact fiber counts.

## Relationship to prior work

General Hankel inverse theory distinguishes spectra of a single Hankel operator from stronger data including the shifted Hankel operator [1,3]. The present claim specifies a *unit-mass two-atom subclass* and counts the exact multiplicity of its inverse under **one** unaugmented eigenvalue list. The Cauchy-matrix spectral-map theorem [4] uses eigenvalues together with spectral weights, and its kernel is of sum-Cauchy rather than geometric Szegő-Gram form; it does not state the trace-nine cubic bifurcation. The positive integral Hankel spectral map [5] also uses a cyclic-vector spectral measure, not just eigenvalues. The Hardy Hankel norm paper [2] studies norm saturation rather than inverse poles. None of these formulations supplies the derivative sign criterion in Step 3 directly. This is a claim of noncoverage in the inspected material, not a proof of historical uniqueness.

## Limitations

The statement does not classify the inverse problem for unequal masses, complex or negative poles, more than two atoms, or general nonpositive Hankel operators. If one observes the entire sequence of moments, the poles can of course be recovered by a standard recurrence. Stronger spectral data can also restore uniqueness; the theorem is only about the two nonzero eigenvalues and fixed unit masses. Published priority for equivalent two-point kernel-Gram parameterizations is not exhaustively resolved; specialist review is advisable.

## References

[1] Z. Liang and S. Treil, *A Dynamical System Approach To The Inverse Spectral Problem For Hankel Operators: The General Case*, first posted 31 March 2022, https://arxiv.org/abs/2204.00115.

[2] O. F. Brevig and K. Seip, *Maximal norm Hankel operators*, first posted 19 January 2023, https://arxiv.org/abs/2301.07937 (primary MSC2020 47B35).

[3] P. Gérard and S. Grellier, *Spectral inverse problems for compact Hankel operators*, first posted 24 January 2012, https://arxiv.org/abs/1201.4971.

[4] A. Pushnitski and S. Treil, *The spectral map for weighted Cauchy matrices is an involution*, first posted 25 April 2025, https://arxiv.org/abs/2504.18707.

[5] A. Pushnitski and S. Treil, *Inverse spectral problems for positive Hankel operators*, first posted 28 March 2025, https://arxiv.org/abs/2503.22189.
