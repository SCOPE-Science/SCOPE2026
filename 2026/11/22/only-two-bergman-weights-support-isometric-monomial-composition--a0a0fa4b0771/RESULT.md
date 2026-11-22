# Only two Bergman weights support isometric monomial composition with an analytic multiplier

## Finding

Fix any integer \(N\ge2\). On the analytic power-weighted Bergman spaces \(A_\alpha^2(\mathbb D)\), the noninjective composition symbol \(\varphi(z)=z^N\) admits an analytic isometric weighted-composition multiplier **only** for the weight exponents \(\alpha=0\) and \(\alpha=1\). Moreover, *every* analytic multiplier is explicitly classified:

\[
W_{w,\varphi}\text{ is isometric}\ \Longleftrightarrow \begin{cases}
\alpha=0,\quad w(z)=\sqrt N\,e^{i\theta}z^{N-1},\\
\text{or}\\
\alpha=1,\quad w(z)=\sqrt N\,z^{N-1}\sum_{j=0}^{N-1}e^{i\theta_j}z^j,
\end{cases}
\]
where all phases are arbitrary real numbers. The second case is an entire \(N\)-torus of multipliers, whereas the first has a single phase.

## Assumptions and scope

The disc is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). For real \(\alpha>-1\), normalize the measure by
\[
d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,\frac{dA(z)}\pi,
\qquad \|f\|_\alpha^2=\int_{\mathbb D}|f|^2d\mu_\alpha.
\]
Thus the monomials are an orthogonal complete family with squared norms
\[
m_k=(\alpha+1)\int_0^1 t^k(1-t)^\alpha\,dt
=\frac{\Gamma(\alpha+2)\Gamma(k+1)}{\Gamma(k+\alpha+2)},
\qquad k\ge0.
\]
Given an arbitrary holomorphic \(w(z)=\sum_{j\ge0}w_jz^j\), consider \((Wf)(z)=w(z)f(z^N)\) initially on polynomials. 'Isometric' means that this formula defines a bounded linear operator on all of \(A_\alpha^2\) preserving every vector norm. No multiplier polynomiality, boundedness, nonvanishing, or phase restrictions are imposed before the proof. The theorem concerns only \(N\ge2\), not automorphisms or arbitrary inner symbols.

## Proof

**Step 1: The diagonal moment identity determines every coefficient modulus.** If \(W\) is isometric, \(w=W1\in A_\alpha^2\). Let
\[
Q(t)=\sum_{j\ge0}|w_j|^2t^j\quad(0\le t<1).
\]
Analyticity of \(w\) gives convergence for \(t<1\), and \(\int_0^1Q(t)(1-t)^\alpha\,dt<\infty\). For each integer \(n\ge0\), the equality \(\|Wz^n\|_\alpha^2=\|z^n\|_\alpha^2\) reads
\[
\int_0^1t^{Nn}Q(t)(1-t)^\alpha\,dt
=\int_0^1u^n(1-u)^\alpha\,du.
\]
In the left integral, substitute \(u=t^N\). The resulting two finite positive measures on \([0,1]\) have equal moments for every \(n\ge0\); uniqueness in the Hausdorff moment problem therefore makes their densities equal almost everywhere. By continuity this gives, for every \(0<t<1\),
\[
\boxed{Q(t)=Nt^{N-1}S_N(t)^\alpha,\qquad
S_N(t)=1+t+\cdots+t^{N-1}.}\tag{1}
\]
Notice that this identity does not assume a polynomial multiplier.

**Step 2: Orthogonality rules out repeated residue classes.** For any integers \(n\ge0\), \(\ell\ge1\), the images of \(z^n\) and \(z^{n+\ell}\) are orthogonal, so
\[
0=\sum_{j\ge0}w_j\overline{w_{j+N\ell}}m_{N(n+\ell)+j}.
\]
For each \(\ell\) define the analytic function
\[
F_\ell(t)=\sum_{j\ge0}w_j\overline{w_{j+N\ell}}t^j.
\]
The Cauchy–Schwarz inequality and \(w\in A_\alpha^2\) imply integrability of \(t^{N\ell}F_\ell(t)(1-t)^\alpha\) on \((0,1)\), hence the preceding identities are all moments of a finite complex measure after \(u=t^N\). Uniqueness of complex measures against polynomials shows \(F_\ell(t)=0\) for almost every \(t\in(0,1)\); analyticity makes it identically zero. Therefore
\[
w_j\overline{w_{j+N\ell}}=0
\quad\text{for all}\quad j\ge0,\ \ell\ge1.\tag{2}
\]
Each residue class modulo \(N\) contains **at most one** index with a nonzero coefficient of \(w\). In particular \(Q\) is a polynomial with at most \(N\) monomials and at most one exponent in each congruence class.

**Step 3: The Bergman exponent is rigid.** Taking logarithmic derivatives of (1) for \(0<t<1\) gives the rational-function identity
\[
\frac{Q'(t)}{Q(t)}-\frac{N-1}{t}
=\alpha\frac{S_N'(t)}{S_N(t)}.\tag{3}
\]
Every nontrivial \(N\)-th root of unity \(\zeta\) is a simple zero of \(S_N\), so the right side has residue \(\alpha\) at \(\zeta\). The left side is the logarithmic derivative of a polynomial, apart from a term holomorphic at \(\zeta\); hence its residue is the nonnegative integer multiplicity of the zero of \(Q\). Equality of rational functions forces \(\alpha=d\in\{0,1,2,\ldots\}\).

If \(d\ge0\), equation (1) says \(Q(t)=Nt^{N-1}S_N(t)^d\). Every coefficient of \(S_N(t)^d\) in degrees \(0\) through \(d(N-1)\) is strictly positive. Thus \(Q\) has \(d(N-1)+1\) consecutive nonzero coefficient positions. Condition (2) allows at most \(N\) such positions, so
\[
d(N-1)+1\le N\quad\Longrightarrow\quad d\le1.
\]
For \(d=0\), equation (1) forces the single coefficient \(|w_{N-1}|=\sqrt N\). For \(d=1\), it forces \(|w_j|=\sqrt N\) exactly for \(N-1\le j\le 2N-2\), with all other coefficients zero. Orthogonality imposes no further phase relation because these are \(N\) distinct residue classes.

**Step 4: Both families really are isometries.** For \(\alpha=0\), \(m_j=1/(j+1)\), so
\[
\|Wz^n\|_0^2=N m_{N(n+1)-1}=\frac1{n+1}=m_n.
\]
For \(\alpha=1\), \(m_j=2/((j+1)(j+2))\), and the proposed multiplier has one coefficient of squared modulus \(N\) in each consecutive degree from \(N-1\) to \(2N-2\). Hence
\[
\|Wz^n\|_1^2
=2N\sum_{k=N(n+1)}^{N(n+2)-1}\frac1{k(k+1)}
=\frac2{(n+1)(n+2)}=m_n.
\]
For distinct \(n\), the image supports are disjoint: in the second case the support of \(Wz^n\) is exactly the degree interval from \(N(n+1)-1\) through \(N(n+2)-2\). Thus monomials map to an orthogonal system preserving their norms. Density of polynomials extends the formula uniquely to an isometry on the entire Bergman Hilbert space, completing both implications.

## Verification

The standalone, standard-library-only script `check.py` checks the exact rational telescoping identities, disjoint degree supports, and residue repetitions for higher integer weights over a finite set of degrees and parameters. It passes 7,106 assertions. These **finite checks are not the proof** of the claims for all \(N\), all \(n\), all real \(\alpha\), or arbitrary analytic \(w\); Steps 1–4 are the infinite-dimensional argument. An independent direct density calculation also confirms the two constructed families: summing \(|w|^2\) over the \(N\) inverse branches of \(z^N\) cancels the Bergman Jacobian and returns the target measure.

## Relationship to prior work

Chalendar and Partington, *Weighted composition operators: isometries and asymptotic behaviour*, arXiv:1910.01475 (first public 3 October 2019), Theorem 4.3 and Remark 4.4, discuss pullback-measure characterizations for Bergman and weighted Bergman isometries; Proposition 4.5 supplies the classical unweighted construction via a derivative multiplier. Zorboska, *Isometric weighted composition operators on weighted Bergman spaces* (2018), gives a general weighted pullback criterion, and a publicly available May 2018 lecture states this criterion explicitly. Neither inspected account specifies the full list of exponents and all analytic multipliers for fixed noninjective \(\varphi(z)=z^N\). The present result is the concrete arithmetic and analytic rigidity classification obtained from the moment and residue-class constraints, not a new general pullback criterion.

Kim's 2022 thesis, Section 5.3, treats *both* monomial composition and monomial multiplication symbols on weighted Hardy coefficient spaces, not the unrestricted analytic multipliers considered here. Mas and Vukotić (2022) concern invertible or surjective weighted-composition isometries and do not address these noninvertible maps. The inaccessible full text of Zorboska's 2018 journal article creates a residual historical-comparison risk; its May 2018 lecture slides and Chalendar–Partington's account were inspected, but do not replace a full-paper inspection.

## Limitations

The classification is for the **same** standard radial Bergman Hilbert space on both sides, normalized with \((1-|z|^2)^\alpha\), and the specific noninjective power composition symbol \(z^N\), \(N\ge2\). No analogous claim is made for general finite Blaschke maps, other radial weights, Hardy spaces, or Bergman \(L^p\) spaces with \(p\ne2\). Historical novelty is assessed on available sources and is not independently certified. There is no external independent mathematical audit.

## References

1. I. Chalendar and J. R. Partington, *Weighted composition operators: isometries and asymptotic behaviour*, arXiv:1910.01475 (posted 3 October 2019), https://arxiv.org/abs/1910.01475. See §4.1, Theorem 4.3, Remark 4.4, Proposition 4.5.
2. N. Zorboska, *Isometric weighted composition operators on weighted Bergman spaces*, Journal of Mathematical Analysis and Applications **461** (2018), 657–675, https://doi.org/10.1016/j.jmaa.2018.01.036. Related May 2018 lecture notes: https://analyse.mat.ulaval.ca/tr60/talks/Zorboska.pdf.
3. G. Kim, *Isometric, unitary and invertible weighted composition operators on spaces of holomorphic functions*, University of Manitoba thesis (2022), §5.3, https://mspace.lib.umanitoba.ca/server/api/core/bitstreams/0fc6edfc-66ac-43c2-b86c-123ccdd91545/content.
4. A. Mas and D. Vukotić, *Invertible and Isometric Weighted Composition Operators*, Mediterranean Journal of Mathematics **19** (2022), article 173, https://doi.org/10.1007/s00009-022-02071-w.
