# Spectral multiplicity phase transition in bilinear-resolvent Naimark dilations

## Finding

The minimal joint Naimark dilation of every bilinear-resolvent joint Hausdorff measure in the spectral-and-cyclicity class of Tian (2026, Theorem 5.1) has an explicit spectral multiplicity function. Write \(d=\dim\mathcal H\in\{2,3,\ldots\}\cup\{\infty\}\), \(c=ab-\gamma\), and use logarithmic coordinates \(u=-\log s\), \(v=-\log t\) on the moment square.

* **Interior completion, \(0<c<ab\).** The unique representing positive operator-valued measure is equivalent to two-dimensional Lebesgue measure on \((0,\infty)^2\), with an everywhere boundedly invertible operator-valued density. The minimal dilation has constant joint spectral multiplicity \(d\) almost everywhere.
* **Critical completion, \(c=0\).** The measure splits into three mutually singular pieces: a rank-one singular measure on \(\Gamma=\{(at,bt):t>0\}\), a planar piece of constant density rank \(d-1\) on \(\Omega_A=\{(u,v):u>av/b,\ v>0\}\), and a planar piece of constant density rank \(d-1\) on \(\Omega_B=\{(u,v):v>bu/a,\ u>0\}\). The minimal dilation has multiplicity \(1\) on the curve and multiplicity \(d-1\) on either open wedge, with no further spectral component. Here \(\infty-1=\infty\).

Thus the critical completion changes both the spectral type and the full multiplicity function, even for infinite-dimensional irreducible examples with continuous spectrum in their defining operators. These multiplicities refer to the **minimal joint dilation**, not to the spectra of the original noncommuting operators.

## Assumptions and scope

Let \(\mathcal H\) be a complex Hilbert space with \(\dim\mathcal H\ge2\). Let \(A,B\) be bounded, strictly positive self-adjoint operators, with respective smallest spectral values \(a,b>0\), both simple isolated eigenvalues with unit eigenvectors \(q,p\). Assume \(p\) is cyclic for \(A\). Suppose the equivalent positive-completion condition of Tian holds:

\[
(A-aI)(B-bI)=\gamma(I-R),\qquad
R=\frac{|p\rangle\langle q|}{\langle q,p\rangle},\qquad 0<\gamma\le ab.
\]

Cyclicity ensures \(\langle q,p\rangle\ne0\). Tian proves the unique positive completion is \(C=BA-\gamma R\), and the unique normalized positive operator-valued measure \(E\) on \([0,1]^2\) satisfies

\[
\int_{[0,1]^2}s^mt^n\,dE(s,t)=(I+mA+nB+mnC)^{-1}
\quad(m,n\in\mathbb N_0).
\]

The boundary parameters \(\gamma=0\) and \(c=ab\) are **not** in the hypotheses. The operator dimension may be countably infinite, and \(A,B\) may have nontrivial continuous spectral parts. The cyclicity assumption implies separability. The multiplicity statement is modulo the usual equivalence of scalar measure classes in a direct-integral spectral representation.

## Proof

**1. Resolvent decomposition and scalar kernel (prior ingredients).** Set

\[
K_0=aA^{-1}+bB^{-1}-I,\quad K_1=I-aA^{-1},\quad K_2=I-bB^{-1}.
\]

Tian's Theorem 5.1 proves \(K_j\ge0\), \(K_0+K_1+K_2=I\), and, with \(c=ab-\gamma\),

\[
(I+xA+yB+xyC)^{-1}
=\frac{K_0+K_1(I+xA)^{-1}+K_2(I+yB)^{-1}}
{1+ax+by+cxy}.
\tag{1}
\]

Let \(\mu_c\) denote the unique scalar probability distribution on the logarithmic quadrant with Laplace transform \((1+ax+by+cxy)^{-1}\). For \(0<c<ab\), its density is

\[
f_c(u,v)=\frac1c e^{-(bu+av)/c}
\sum_{k=0}^\infty\frac{((ab-c)uv/c^2)^k}{(k!)^2},\qquad u,v>0.
\tag{2}
\]

This is strictly positive everywhere by its \(k=0\) term. It follows by writing the geometric-series inverse of the scalar denominator and applying the gamma integral in each coordinate. For \(c=0\), \(\mu_0\) is the law of \((aT,bT)\) with \(T\) exponential of mean one. For \(\lambda>0\), the scalar resolvent \((1+x\lambda)^{-1}\) is the Laplace transform of an exponential law of mean \(\lambda\). Spectral integration and uniqueness of mixed Hausdorff moments therefore give the decomposition

\[
E=K_0\mu_c+\mathcal M_{A,c}+\mathcal M_{B,c},
\tag{3}
\]

where \(\mathcal M_{A,c}\) is the convolution of \(\mu_c\) with the first-coordinate exponential spectral kernel of \(K_1\) and \(A\), and \(\mathcal M_{B,c}\) is the analogous second-coordinate convolution for \(K_2,B\). These are positive operator-valued measures. Equation (3) is an explicit interpretation of Tian's measure construction, not a new existence theorem.

**2. The ranks of the positive coefficients.** Since the eigenvalues \(a,b\) are simple isolated minima, functional calculus gives

\[
\ker K_1=\mathbb Cq,\qquad\ker K_2=\mathbb Cp,
\]

and each \(K_i\) is boundedly invertible on the orthogonal complement of its displayed kernel. To analyze \(K_0\), use Tian's canonical block form relative to \(\mathcal H=\mathbb Cp\oplus p^\perp\):

\[
A=\begin{pmatrix}a+\langle z,D^{-1}z\rangle&z^*\\z&aI+D\end{pmatrix},\qquad
B=\begin{pmatrix}b&0\\0&bI+\gamma D^{-1}\end{pmatrix},
\tag{4}
\]

where \(D\) is bounded, positive and boundedly invertible on \(p^\perp\). Set \(A_1=aI+D\), \(B_1=bI+\gamma D^{-1}\), \(\sigma=a+\langle z,D^{-1}z\rangle-\langle z,A_1^{-1}z\rangle>0\), and \(w=(1,-A_1^{-1}z)\). Block inversion yields the exact identity

\[
K_0=\frac a\sigma|w\rangle\langle w|
+c\begin{pmatrix}0&0\\0&A_1^{-1}B_1^{-1}\end{pmatrix}.
\tag{5}
\]

For \(c=0\), this is a nonzero rank-one operator. For \(c>0\), the lower block is boundedly positive on \(p^\perp\), and \(w\) has first coordinate one. Consequently the sum is boundedly positive on the whole space: if \(\langle K_0x_j,x_j\rangle\to0\) for unit vectors \(x_j=(\alpha_j,y_j)\), then coercivity forces \(y_j\to0\), and the first term forces \(\alpha_j\to0\), a contradiction. Thus \(K_0\ge\varepsilon I\) for some \(\varepsilon>0\) when \(c>0\).

**3. Interior spectral density.** For \(c>0\), all three terms in (3) are absolutely continuous with respect to planar Lebesgue measure because \(\mu_c\) is, and convolution preserves absolute continuity. Let \(W_c(u,v)\) be their operator-valued density. Positivity and (2), (5) give

\[
W_c(u,v)\ge f_c(u,v)K_0\ge\varepsilon f_c(u,v)I>0,
\tag{6}
\]

at every \(u,v>0\), taking the continuous densities provided by the integral formulas. Thus \(W_c(u,v)\) is boundedly invertible on \(\mathcal H\) at every positive pair (pointwise bounds need not be uniform in \(u,v\)). In particular the scalar measure class of \(E\) is exactly planar Lebesgue measure, and its pointwise rank is \(d\).

**4. Critical spectral strata.** For \(c=0\), the first term of (3) is the singular curve measure \(K_0\mu_0\); it has fiber rank one. The other two pieces are planar and lie on opposite sides of \(\Gamma\). Indeed, the spectral exponential kernel of \(A\) adds a positive amount \(r\) to the first log-coordinate, yielding points \((at+r,bt)\) with \(r>0\), which precisely fill \(\Omega_A\). Conditional on \(t=v/b\), their operator density is

\[
W_A(u,v)=\frac{e^{-v/b}}b\,\mathbf1_{\Omega_A}(u,v)
\int_{\sigma(A)}\frac{1-a/\lambda}{\lambda}
\exp\!\left(-\frac{u-av/b}{\lambda}\right)dP_A(\lambda).
\tag{7}
\]

Here \(P_A\) is the projection-valued spectral measure. Likewise the \(B\)-convolution fills \(\Omega_B\) with density

\[
W_B(u,v)=\frac{e^{-u/a}}a\,\mathbf1_{\Omega_B}(u,v)
\int_{\sigma(B)}\frac{1-b/\lambda}{\lambda}
\exp\!\left(-\frac{v-bu/a}{\lambda}\right)dP_B(\lambda).
\tag{8}
\]

For each fixed positive excess \(r\), the scalar function \((1-a/\lambda)\lambda^{-1}e^{-r/\lambda}\) vanishes exactly at \(\lambda=a\) and has a positive minimum on the compact remainder of \(\sigma(A)\), since \(a\) is isolated. Therefore \(\ker W_A(u,v)=\mathbb Cq\), and \(W_A\) is boundedly positive on \(q^\perp\) throughout its wedge. Symmetrically \(\ker W_B(u,v)=\mathbb Cp\), with bounded positivity on \(p^\perp\). These ranks are \(d-1\). All exponential distributions have support in strictly positive log-coordinates, and \(T>0\) almost surely, so no axes, point, or additional curve mass occurs. The open wedges and the curve partition the positive quadrant up to null boundaries.

**5. Identifying ranks with minimal joint-dilation multiplicities.** For completeness, consider a positive normalized \(\mathcal B(\mathcal H)\)-valued measure with a weak operator Radon–Nikodym density \(W\) relative to a scalar \(\nu\), as in (6)–(8). Start from finite sums of elementary functions \(f=\sum_j\mathbf1_{U_j}h_j\) with inner product \(\int\langle W(z)f(z),f(z)\rangle d\nu(z)\), factor out the null functions and complete. The map \(Vh=[z\mapsto h]\) is an isometry by normalization of \(E\); pointwise multiplication by Borel indicators is a projection-valued measure \(P\), and \(V^*P(U)V=E(U)\). The span of these indicator sections is dense by construction, so this is the **minimal** dilation. Under the map \(f\mapsto W^{1/2}f\), its fiber over \(z\) is the closure of \(\operatorname{ran}W(z)^{1/2}\), whose dimension equals the rank of \(W(z)\). For the mutually singular pieces in step 4, take the direct sum of the corresponding weighted \(L^2\) spaces, with the rank-one curve fiber. Steps 2–4 now yield precisely the multiplicities asserted.

## Verification

The included `CHECK.py` reproduces, with exact rational matrix arithmetic, the block example (4) in dimensions \(2,3,4,5\), at the critical coupling and two interior couplings. It tests \(588\) instances of identity (1), the critical/interior ranks of \(K_0,C\), and the codimension-one kernels of \(K_1,K_2\). Floating-point tests additionally examine \(24\) wedge-density rank instances at positive excess distances. Run `python CHECK.py` with Python 3, NumPy and SymPy installed. These finite checks are diagnostic only; the positivity and multiplicity theorems for arbitrary Hilbert spaces follow from steps 1–5, independently of numerical computations.

## Relationship to prior work

Tian (2026), Theorem 5.1, Lemma 2.1, and equation (5.10), already establish existence and uniqueness of the completion and provide all three positive moment-measure ingredients; these parts are **not** claimed as new. Section 6 explicitly asks for the spectral multiplicity and spectral-measure structure of the **minimal** simultaneous Naimark dilation. The present contribution gives the entire multiplicity function and its critical transition for Tian's spectral-and-cyclicity class, including arbitrary separable Hilbert dimension and continuous-spectrum examples. The published *A sharp total-variation jump for unique bilinear-resolvent joint measures* (2026) already detects absolute-continuity/singular rank-drop for a specific \(2\times2\) family, but does not classify the minimal dilation's multiplicity or the two open-wedge ranks in arbitrary dimension. Classical Naimark dilation theory supplies the rank-to-fiber principle, not the specialized coefficient-rank and geometric-support calculation carried out here.

## Limitations

The classification assumes Tian's simple isolated bottom eigenvalues and cyclicity; it neither solves the noncyclic positive-completion problem nor claims a classification for all positive resolvent pencils. Interior density coercivity is pointwise and need not be uniform over the unbounded log-quadrant. The phase transition varies the coupling inside the canonical Tian family; it does not assert norm continuity of arbitrary operator pairs. Possible implicit coverage in general operator-valued measure or direct-integral literature is a remaining bibliographic risk. No independent mathematical audit has been conducted.

## References

- J. Tian, *Joint Moments of Bilinear Resolvents* (2026), arXiv:2611.03081v1, first publicly posted 2026-11-02; sections 2, 3, 5, and 6. https://arxiv.org/html/2611.03081v1
- *A sharp total-variation jump for unique bilinear-resolvent joint measures* (2026), publicly accessible research note, 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-sharp-total-variation-jump-for-unique-bilinear-resolvent-joint--3b321b9e0369
- M. McLaren, S. Plosker, C. Ramsey, *On Operator Valued Measures* (2018), arXiv:1801.00331, background on POVMs and Radon–Nikodym constructions. https://arxiv.org/abs/1801.00331
