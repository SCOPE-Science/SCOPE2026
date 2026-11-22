# Sharp fixed-area annular observation of the first three radial Zernike modes

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|\le1\}\), with normalized planar area \(dA/\pi\). Let \(\mathcal R=\{p(|z|^2):p\in\mathbb C[u],\ \deg p\le2\}\), the three-dimensional span of the axisymmetric Zernike modes of radial orders zero, two and four. For \(0<q<1\) and \(0\le a\le1-q\), consider the concentric annular observation region \(E_{a,q}=\{z\in\mathbb D:a\le|z|^2\le a+q\}\), of area fraction \(q\). Define

\[
\Lambda(a,q)=\inf_{0\ne f\in\mathcal R}\frac{\int_{E_{a,q}}|f(z)|^2\,dA(z)}{\int_{\mathbb D}|f(z)|^2\,dA(z)}.
\]

For every \(q\in(0,1)\), the **unique** annulus maximizing the worst observed energy is the *squared-radius-centered* annulus \(a=(1-q)/2\). Put

\[
T(q)=\frac q4(9-10q^2+9q^4),\qquad
\lambda_\pm(q)=\frac{T(q)\pm\sqrt{T(q)^2-4q^6}}2.
\]

The complete spectrum of its observation Gram operator is

\[
\boxed{\lambda_-(q)<q^3<\lambda_+(q)},
\]

and the sharp maximin energy is \(\boxed{\lambda_-(q)}\). For each displaced annulus, write \(\delta=a-(1-q)/2\), \(\lambda=\lambda_-(q)\), and

\[
\beta=\frac{q^3-\lambda}{12(q-\lambda)},\qquad
D_0=\frac1{80}-\frac\beta6+\beta^2.
\]

Then \(0<\beta<1/4\), and the following *quantitative strict loss* holds:

\[
\boxed{\Lambda(a,q)\le\lambda\frac{D_0}{D_0+(\frac12-2\beta)\delta^2+\delta^4}<\lambda\quad\text{if }\delta\ne0.}
\]

The centered optimizer is a radial polynomial proportional to \((|z|^2-1/2)^2-\beta\). In the narrow-annulus regime \(q\downarrow0\), its sharp least-observed energy obeys \(\lambda_-(q)\sim(4/9)q^5\); the largest eigenvalue is asymptotic to \((9/4)q\), so the centered observation's sharp squared condition number is asymptotic to \((81/16)q^{-4}\).

## Assumptions and scope

All norms and observation integrals use ordinary planar area, without renormalizing the observed area. An annulus may touch the center or the outer boundary. The field space is exactly the three-dimensional axisymmetric polynomial subspace, not all Zernike modes of total order at most four. Optimization is among single concentric annuli of *fixed area fraction*, not arbitrary measurable masks, multiple rings or discrete point sensors. Complex coefficients are allowed. Endpoints \(q=0,1\) are excluded from the uniqueness statement.

## Proof

**Step 1: Uniform radial coordinate.** Writing \(u=|z|^2\), polar integration gives \(\pi^{-1}\int_{\mathbb D}|p(|z|^2)|^2dA=\int_0^1|p(u)|^2du\) and \(\pi^{-1}\int_{E_{a,q}}|p(|z|^2)|^2dA=\int_a^{a+q}|p(u)|^2du\). Thus \(\Lambda\) is the least eigenvalue of interval restriction in the degree-at-most-two polynomial Hilbert space on \([0,1]\).

**Step 2: Spectrum at the centered annulus.** Let \(y=u-1/2\) and \(I_q=[-q/2,q/2]\). An orthonormal basis for \(L^2([-1/2,1/2])\) in this polynomial space is

\[
\phi_0(y)=1,\quad\phi_1(y)=2\sqrt3\,y,\quad
\phi_2(y)=\sqrt{180}\,(y^2-1/12).
\]

Oddness makes the \(\phi_1\) sector orthogonal to the other two on \(I_q\), and its squared restriction norm is \(q^3\). The even block is

\[
B(q)=\begin{pmatrix}
q & (\sqrt5/2)q(q^2-1)\\
(\sqrt5/2)q(q^2-1)&(q/4)(9q^4-10q^2+5)
\end{pmatrix}.
\]

Its trace is \(T(q)\), and its determinant is exactly \(q^6\). Since \(T(q)-2q^3=(9q/4)(1-q^2)^2>0\), the two even eigenvalues straddle \(q^3\) strictly and are precisely \(\lambda_\pm(q)\). In particular \(0<\lambda_-(q)<q^3<q<1\).

**Step 3: Structure of the least-observed field.** The least eigenvalue is simple and lies in the even sector, so the eigenpolynomial can be normalized to \(p_0(y)=y^2-\beta\), because the least eigenvector cannot be constant (the off-diagonal entry of \(B(q)\) is nonzero). Testing its generalized eigenvalue equation against the constant function yields

\[
q^3/12-q\beta=\lambda(1/12-\beta),\qquad
\beta=(q^3-\lambda)/(12(q-\lambda)).
\]

Because \(0<\lambda<q^3<q\), we have \(\beta>0\). Further, \(q^3+2\lambda<3q^3<3q\), which is equivalent to \(\beta<1/4\).

**Step 4: Global, strictly optimal placement.** For a displaced observation interval \([\delta-q/2,\delta+q/2]\) in the centered coordinate, test the admissible degree-two polynomial \(p_\delta(y)=(y-\delta)^2-\beta\). Its energy on that observation interval is independent of \(\delta\), namely the centered numerator \(N=\int_{I_q}|p_0(y)|^2dy=\lambda D_0\). Its full-disk squared norm is, by exact polynomial integration,

\[
\begin{split}
\int_{-1/2}^{1/2}|p_\delta(y)|^2dy
&=D_0+(1/2-2\beta)\delta^2+\delta^4,\\
D_0&=\int_{-1/2}^{1/2}(y^2-\beta)^2dy
=1/80-\beta/6+\beta^2.
\end{split}
\]

As \(\beta<1/4\), this is strictly larger than \(D_0\) unless \(\delta=0\). Applying the Rayleigh variational principle to \(p_\delta\) proves the advertised quantitative upper bound on \(\Lambda\) and hence the global uniqueness of the centered annulus. The argument makes no discretization or assumption about \(\delta\) other than admissible placement.

**Step 5: Thin-annulus law.** The explicit trace has \(T(q)\sim(9/4)q\); since the even determinant is \(q^6\), its smaller eigenvalue satisfies \(\lambda_-(q)=q^6/\lambda_+(q)\sim(4/9)q^5\). The two extreme eigenvalues are \(\lambda_+\) and \(\lambda_-\), giving the stated squared condition-number asymptotic.

## Verification

The standalone `check_annulus.py` reproduces the centered Gram identities with symbolic polynomial integration and independently checks the disk-area Gram with numerical polar quadrature. It additionally checks the global displacement upper bound against smallest eigenvalues on 288 representative parameter pairs. The checker passed all seven symbolic identities, nine independent polar-quadrature comparisons, and 288 least-eigenvalue comparisons. These finite checks supplement rather than replace the analytic all-parameter proof above.

At the illustrative area fraction \(q=1/2\), the exact optimal least energy is \((113-9\sqrt{145})/256=0.018068940589333\ldots\), and the unique squared-radius-centered annulus is bounded by squared radii \(1/4\) and \(3/4\).

## Relationship to prior work

Radial Slepian spectral concentration and circular prolate theory provide the broad motivating context: Boulsane (2020), arXiv:2002.00170, studies the spectrum of the finite Hankel transform and its infinite-dimensional bandlimited concentration operator, not placement of a fixed-area annular mask for a three-dimensional radial Zernike band. Ramos-López and collaborators (2015), arXiv:1511.00449, optimize *discrete Zernike interpolation nodes*, rather than this continuum worst-energy objective. Published work on thin *outer* Zernike annuli studies different fixed-boundary conditioning asymptotics. The exact three-mode placement theorem, its sharp spectral formula and strict translated-eigenpolynomial inequality are not implied by those stated results. This is a best-knowledge priority comparison, not proof that no equivalent exists elsewhere.

## Limitations

The result is an exact three-mode theorem, not an all-Zernike-band or arbitrary-mask theorem. The quantitative off-center inequality is a strict valid upper bound but is not asserted to equal the true least eigenvalue away from the optimum. Small-area asymptotics are for the optimal centered annulus, not every possible annulus. A historical-equivalence risk persists for older polynomial-design and radial-observability literature; independent validation has not been conducted.

## References

- M. Boulsane, *Non-asymptotic behavior and the distribution of the spectrum of the finite Hankel transform operator*, arXiv:2002.00170, first submitted 2020-02-01, https://arxiv.org/abs/2002.00170.
- D. Ramos-López, M. A. Sánchez-Granero, M. Fernández-Martínez, A. Martínez-Finkelshtein, *Optimal sampling patterns for Zernike polynomials*, arXiv:1511.00449, first submitted 2015-11-02, https://arxiv.org/abs/1511.00449.
