# Sharp inverse-Gaussian ultracontractivity and first-order rank-one collapse

## Finding

The inverse Ornstein–Uhlenbeck semigroup associated with an arbitrary stable real drift and strictly positive diffusion has an exact, attained (for \(1<p<\infty\)) \(L^p\)-to-\(L^\infty\) norm and a Gaussian point-evaluation norm profile. Its normalized long-time limit is a rank-one operator, and the first-order operator-norm defect has an exact coefficient governed by the largest singular value of the covariance-normalized drift flow.

In the notation below, for \(1<p<\infty\) and \(r=p/(p-1)\), define
\[
N_p(t)=(2\pi)^{-d/(2p)}r^{-d/(2r)}(\det Q_t)^{-1/(2p)}e^{t\operatorname{tr}B}\left(\frac{\det Q_\infty}{\det(Q_\infty-Q_t/r)}\right)^{1/(2r)}.
\]
For \(p=1\), put \(N_1(t)=(2\pi)^{-d/2}(\det Q_t)^{-1/2}e^{t\operatorname{tr}B}\). Then, for all \(t>0\) and \(1\le p<\infty\),
\[
\boxed{\|H_t\|_{L^p(\mu)\to L^\infty(\mu)}=N_p(t).}
\]
More precisely, each evaluation at \(x\in\mathbb R^d\) has norm
\[
\boxed{\|\delta_xH_t\|=N_p(t)\exp\!\left[-\frac12x^{\mathsf T}\bigl(Q_t+p(Q_\infty-Q_t)\bigr)^{-1}x\right].}
\]
For \(1<p<\infty\), the only nonzero norm-extremizing inputs, up to scalar multiples, are
\[
f_{p,t}(u)=\exp\!\left[-\frac{u^{\mathsf T}(S_t^{\mathsf T}Q_t^{-1}S_t+Q_\infty^{-1})u}{2(p-1)}\right].
\]
No nonzero \(L^1(\mu)\) input attains the \(L^1\)-to-\(L^\infty\) norm.

Let \(c_\infty=(2\pi)^{-d/2}(\det Q_\infty)^{-1/2}\) and
\[
(\Pi f)(x)=c_\infty e^{-x^{\mathsf T}Q_\infty^{-1}x/2}\int_{\mathbb R^d} f(u)\,du,
\qquad
(\mathcal R_S f)(x)=c_\infty e^{-x^{\mathsf T}Q_\infty^{-1}x/2}
 x^{\mathsf T}Q_\infty^{-1}S\int_{\mathbb R^d}u f(u)\,du.
\]
For each fixed \(1\le p<\infty\),
\[
\boxed{\|e^{-t\operatorname{tr}B}H_t-\Pi-\mathcal R_{S_t}\|_{p\to\infty}=O(\|S_t\|_2^2).}
\]
Consequently, with \(A_t=Q_\infty^{-1/2}S_tQ_\infty^{1/2}\), \(\beta_p=(\mathbb E|Z|^r)^{1/r}\) for a standard real Gaussian \(Z\), and
\[
C_p=(2\pi)^{-d/(2p)}(r-1)^{-d/(2r)}(\det Q_\infty)^{-1/(2p)},\quad
\kappa_p=e^{-1/2}\beta_p/\sqrt{r-1}\qquad(1<p<\infty),
\]
with \(C_1=(2\pi)^{-d/2}(\det Q_\infty)^{-1/2}\) and \(\kappa_1=e^{-1}\), the *sharp* first-order defect is
\[
\boxed{\|e^{-t\operatorname{tr}B}H_t-\Pi\|_{p\to\infty}
=C_p\kappa_p\|A_t\|_2+O(\|S_t\|_2^2).}
\]
Here \(\|\cdot\|_2\) on finite matrices means the Euclidean operator norm, not the Hilbert–Schmidt norm. This identifies the first correction for nonnormal, anisotropic drifts and includes possible Jordan-block polynomial factors in \(\|S_t\|_2\).

## Assumptions and scope

Let \(d\ge1\), let \(Q\) be a real symmetric positive-definite \(d\)-by-\(d\) matrix, and let \(B\) be real and Hurwitz (all its eigenvalues have strictly negative real part). Write
\[
S_t=e^{tB},\quad Q_t=\int_0^t e^{sB}Qe^{sB^{\mathsf T}}\,ds,\quad
Q_\infty=\int_0^\infty e^{sB}Qe^{sB^{\mathsf T}}\,ds,
\quad C=Q_\infty^{-1}.
\]
The positive matrices satisfy \(Q_\infty-Q_t=S_tQ_\infty S_t^{\mathsf T}\). Equip \(\mathbb R^d\) with the inverse-Gaussian measure \(d\mu(u)=\exp(u^{\mathsf T}Cu/2)\,du\). For \(t>0\), define, initially on bounded compactly supported inputs,
\[
(H_tf)(x)= (2\pi)^{-d/2}(\det Q_t)^{-1/2}e^{t\operatorname{tr}B}
\int_{\mathbb R^d} \exp\!\left[-\frac12(S_tu-x)^{\mathsf T}Q_t^{-1}(S_tu-x)\right]f(u)\,du.
\]
The results hold for the unique bounded extensions \(H_t:L^p(\mu)\to L^\infty(\mu)\), \(1\le p<\infty\). No full spectral or \(p=\infty\) asymptotic classification is asserted.

## Proof

**Step 1: exact row-norm computation.** Relative to \(\mu\), the positive integral kernel is
\[
K_{t,x}(u)=c_t\exp\!\left[-\frac12(S_tu-x)^{\mathsf T}Q_t^{-1}(S_tu-x)-\frac12u^{\mathsf T}Cu\right],
\quad c_t=(2\pi)^{-d/2}(\det Q_t)^{-1/2}e^{t\operatorname{tr}B}.
\]
For \(1<p<\infty\), let \(r=p/(p-1)\), \(M=S_t^{\mathsf T}Q_t^{-1}S_t+C/p\), and apply Gaussian integration to \(\int K_{t,x}^r\,d\mu\):
\[
\|K_{t,x}\|_{L^r(\mu)}=c_t(2\pi/r)^{d/(2r)}(\det M)^{-1/(2r)}
\exp\!\left[-\frac12x^{\mathsf T}(Q_t+pS_tQ_\infty S_t^{\mathsf T})^{-1}x\right].
\]
The matrix determinant lemma and \(Q_\infty-Q_t=S_tQ_\infty S_t^{\mathsf T}\) yield
\[
\det M=\frac{\det(Q_\infty-Q_t/r)}{(\det Q_t)(\det Q_\infty)}.
\]
Thus the claimed row and operator norms follow; the row norm is strictly largest at \(x=0\). Hölder equality forces input proportional to \(K_{t,0}^{r-1}\), yielding the displayed Gaussian extremizers. For \(p=1\), completing the square gives
\[
\|K_{t,x}\|_{L^\infty(\mu)}=c_t\exp[-x^{\mathsf T}C x/2]
\]
(the unique maximizing source point depends continuously on \(x\)); strict Gaussian concavity makes the maximizing source set have \(\mu\)-measure zero, so the norm is never attained by nonzero \(L^1\) inputs.

**Step 2: precise large-time normalization.** For \(S=S_t\), observe \(Q_t=Q_\infty-SQ_\infty S^{\mathsf T}\). The kernel of \(e^{-t\operatorname{tr}B}H_t\) relative to \(\mu\) is
\[
\mathcal K_{S,x}(u)=(2\pi)^{-d/2}\det(Q_\infty-SQ_\infty S^{\mathsf T})^{-1/2}
\exp\!\left[-\frac12(Su-x)^{\mathsf T}(Q_\infty-SQ_\infty S^{\mathsf T})^{-1}(Su-x)-\frac12u^{\mathsf T}Cu\right].
\]
At \(S=0\), this is \(c_\infty\exp[-x^{\mathsf T}Cx/2-u^{\mathsf T}Cu/2]\), the \(\mu\)-kernel of \(\Pi\). The first derivative in direction \(S\) is exactly the \(\mu\)-kernel of \(\mathcal R_S\). All second derivatives in a sufficiently small real matrix ball are finite sums of fixed-degree polynomials in \(Su-x,u\) multiplied by these positive Gaussian kernels. Uniform ellipticity of \(Q_\infty-SQ_\infty S^{\mathsf T}\) supplies a common bound of the form \(C(1+|Su-x|^m)(1+|u|^m)e^{-c|Su-x|^2-c|u|^2}\), for some fixed integer \(m\) and \(c>0\), in the row kernel measured against \(\mu\). For every fixed \(1<p<\infty\), integrating the \(r\)-th powers against \(\mu\) is uniformly bounded in \(x\) because the remaining Gaussian input factor has exponent \(-(r-1)u^{\mathsf T}Cu/2\). For \(p=1\) the same uniform estimate follows by taking the joint supremum in \(x,u\). Taylor's integral remainder and the row-norm characterization therefore imply the asserted \(O(\|S\|_2^2)\) operator-norm bound; all constants may depend on fixed \(B,Q,p,d\).

**Step 3: exact norm of the first correction.** For \(1<p<\infty\), let \(r=p/(p-1)\). At fixed \(x\), the \(r\)-th dual norm of the row kernel of \(\mathcal R_S\) factors as the norm of \(\Pi\)'s Gaussian row times the absolute \(r\)-th moment of a centered normal with covariance \(Q_\infty/(r-1)\). Consequently
\[
\|\delta_x\mathcal R_S\|=C_p\frac{\beta_p}{\sqrt{r-1}}
\exp(-x^{\mathsf T}Cx/2)\sqrt{x^{\mathsf T}CSQ_\infty S^{\mathsf T}Cx}.
\]
After setting \(y=Q_\infty^{-1/2}x\), maximizing \(e^{-|y|^2/2}|A_t^{\mathsf T}y|\) gives \(e^{-1/2}\|A_t\|_2\), achieved in a top singular-vector direction at \(|y|=1\). At \(p=1\), maximizing also over \(u\) gives the additional exact factor \(e^{-1/2}\), hence \(\kappa_1=e^{-1}\). The reverse triangle inequality applied to the Taylor remainder proves the boxed sharp first-order law.

**Step 4: endpoint and time limits.** Since \(Q_t=tQ+O(t^2)\) as \(t\downarrow0\) and \(Q_t\to Q_\infty\) as \(t\to\infty\), the norm formula yields
\[
N_p(t)\sim (2\pi)^{-d/(2p)}r^{-d/(2r)}(\det Q)^{-1/(2p)}t^{-d/(2p)}\quad(t\downarrow0),
\]
\[
N_p(t)\sim C_p e^{t\operatorname{tr}B}\quad(t\to\infty),\qquad 1<p<\infty,
\]
with the evident \(p=1\) limits \(N_1(t)\sim(2\pi)^{-d/2}(\det Q)^{-1/2}t^{-d/2}\) and \(N_1(t)\sim C_1 e^{t\operatorname{tr}B}\). In particular, the long-time decay exponent is independent of finite \(p\).

## Verification

The supplementary standalone checker `CHECK.py` recomputes the matrix determinant identity for 300 reproducible anisotropic stable systems in dimensions one through four, compares the two independent exact norm formulas, verifies strict improvement over the previously published nonsharp bound for \(p>1\), and checks one-dimensional Gaussian row norms by numerical quadrature. These finite checks diagnose normalization and algebra errors; the proof for all dimensions and times is analytic.

## Relationship to prior work

Bruno, Casarino, Ciatti and Sjögren, *Spectral and mapping properties of the inverse Ornstein–Uhlenbeck operator* (arXiv:2611.06826v1, submitted 4 November 2026), give the precise same inverse Mehler kernel and establish a finite nonsharp \(L^p(\mu)\)-to-\(L^\infty(\mu)\) estimate in Proposition 5.2. Their constant comes from the embedding into Lebesgue \(L^p\) and is, for \(p>1\), the sharp Lebesgue-to-\(L^\infty\) norm rather than the sharper inverse-Gaussian-domain norm determined here. In the present notation the ratio of exact inverse-Gaussian norm to their bound is
\[
\left(\frac{\det(Q_\infty-Q_t)}{\det(Q_\infty-Q_t/r)}\right)^{1/(2r)}<1 \qquad(1<p<\infty).
\]
The same paper establishes semigroup spectral properties in \(L^2\); it does not assert the sharp finite-\(p\) norm, its extremizers, or the rank-one first-order profile with the exact anisotropic coefficient. The earlier inverse-Gaussian maximal-operator literature addresses a different mapping problem. Classical Mehler-kernel Gaussian integration is a methodological antecedent; exact Gaussian integration alone is not represented here as novel. The additional sharp nonsymmetric drift-normalized rank-one defect is the structural distinction.

## Limitations

The result assumes strictly positive diffusion and strictly stable drift, finite \(p\), and finite Euclidean dimension. The decay estimate is a large-time norm asymptotic, not a statement about a nonnormal spectral decomposition. Singular diffusion matrices, marginally stable flows, uniformity as \(p\to\infty\), and an exact higher-order term are not covered. The historical literature search does not establish uniqueness or peer-reviewed priority; older equivalent Gaussian-kernel operator formulas could exist.

## References

1. T. Bruno, V. Casarino, P. Ciatti, P. Sjögren, *Spectral and mapping properties of the inverse Ornstein–Uhlenbeck operator*, arXiv:2611.06826v1 (2026), Proposition 5.2 and formula (2.6). https://arxiv.org/abs/2611.06826
2. T. Bruno, V. Casarino, P. Ciatti, P. Sjögren, *Boundedness properties of the maximal operator in a nonsymmetric inverse Gaussian setting* (2025). https://research.chalmers.se/publication/547853/file/547853_Fulltext.pdf
3. L. J. Deutsch, *Sharp bounds for the operator norm of the Mehler kernel operator*, doctoral thesis, California Institute of Technology (1981). https://thesis.caltech.edu/17690/1/Deustch_LJ_1981.pdf
