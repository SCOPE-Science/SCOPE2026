# Exact cyclic Bergman kernel approximation and its Gamma capture law

## Finding
Let \(\beta>0\), and let \(\mathcal H_\beta\) be the analytic reproducing-kernel Hilbert space on the open unit disk with kernel \(K_\beta(z,w)=(1-z\overline w)^{-\beta}\). Fix integers \(m\ge2\) and \(N\ge0\). Denote by \(f_N(z)=\sqrt{a_N}z^N\) the unit monomial, where \(a_n=(\beta)_n/n!\). For \(0<r<1\), let \(V_m(r)\) be the span of the \(m\) evaluation kernels at \(r\exp(2\pi i k/m)\), for \(0\le k<m\). Their common rotation does not affect the conclusions.

Write \(N=qm+j\), with \(q\ge0\), \(0\le j<m\), and put \(u=r^{2m}\). The squared energy captured by orthogonal projection onto this cyclic kernel span is **exactly**
\[
 P_{\beta,m,N}(u)=\|\Pi_{V_m(r)}f_N\|^2
 =\frac{a_N u^q}{\displaystyle\sum_{\ell=0}^{\infty}a_{j+m\ell}u^\ell}.
\]
If \(q=0\), its supremum is \(1\) as \(r\downarrow0\), and this supremum is not attained at positive radius. If \(q\ge1\), it has exactly one maximizing radius \(r_*\in(0,1)\): writing
\[
 M(u)=\frac{\sum_{\ell\ge0}\ell a_{j+m\ell}u^\ell}{\sum_{\ell\ge0}a_{j+m\ell}u^\ell},
\]
its unique defining equation is \(M(r_*^{2m})=q\). Thus the sharp squared approximation error within the regular-orbit class is \(1-P_{\beta,m,N}(r_*^{2m})\).

For fixed \(\beta>0,m\ge2,0\le j<m\), as \(q\to\infty\), the maximizing parameter and captured energy obey the **residue-independent Gamma law**
\[
 1-r_*^{2m}\sim\frac{\beta}{q},\qquad
 q\max_{0<u<1}P_{\beta,m,qm+j}(u)
 \longrightarrow \frac{\beta^\beta e^{-\beta}}{\Gamma(\beta)}.
\]
For the ordinary unweighted Bergman space \(\beta=2\), this becomes an algebraic **finite-degree classification**. With \(A=j+1\) and \(B=m-j-1\),
\[
 P_{2,m,N}(u)=\frac{(N+1)u^q(1-u)^2}{A+Bu},
\]
and for \(q\ge1\) its unique maximizer is the root in \((0,1)\) of
\[
 (q+1)Bu^2+\big((q+2)A-(q-1)B\big)u-qA=0.
\]
If \(B=0\), the formula reduces to \(u=q/(q+2)\). The first correction to the Gamma law is **sensitive to the Fourier residue**:
\[
 u_*=1-\frac2q+\frac{2+2A/m}{q^2}+O_{m,j}(q^{-3}),\quad
 \max P_{2,m,qm+j}=\frac{4e^{-2}}q
 \left(1-\frac{A}{mq}+O_{m,j}(q^{-2})\right).
\]

## Assumptions and scope
All radii are strictly between zero and one, all projections use the Hilbert norm specified by \(K_\beta\), and \(\beta\) is a fixed positive real. For \(\beta=2\), this is the standard disk Bergman space with normalized area measure. The optimization is **only** over common radii of regular \(m\)-point kernel orbits, not over arbitrary node locations, arbitrary angular configurations, derivatives, or the full unrestricted \(m\)-best kernel-approximation problem. The high-degree asymptotics require \(m,j,\beta\) fixed while \(q\to\infty\); no uniformity is claimed if \(m\) or \(\beta\) grows.

## Proof
**1. Fourier-residue decomposition.** In \(\mathcal H_\beta\), the vectors \(e_n(z)=\sqrt{a_n}z^n\) form an orthonormal basis, because \(K_\beta(z,w)=\sum_{n\ge0}a_n(z\overline w)^n\). For \(\omega=e^{2\pi i/m}\), the discrete Fourier transform of the kernels at \(r\omega^k\) splits their span into orthogonal, nonzero residue vectors
\[
 h_j(r)=\sum_{\ell\ge0}\sqrt{a_{j+m\ell}}r^{j+m\ell}e_{j+m\ell},\qquad 0\le j<m.
\]
Indeed the root-of-unity sum cancels all other degrees. Their squared norms are \(r^{2j}\sum_{\ell\ge0}a_{j+m\ell}u^\ell\), while \(|\langle f_N,h_j(r)\rangle|^2=a_Nr^{2N}\) in the residue \(j\equiv N\pmod m\). Orthogonality proves the exact projection identity. It also proves that common angular rotation is immaterial.

**2. Unique finite-radius maximization.** Let \(F(u)=\sum_{\ell\ge0}a_{j+m\ell}u^\ell\), which is positive for \(0<u<1\). Direct differentiation gives
\[
 \frac{d}{d\log u}\log P=q-\frac{uF'(u)}{F(u)}=q-M(u).
\]
The strictly positive weights \(a_{j+m\ell}u^\ell/F(u)\) define a probability distribution on all nonnegative integers. Differentiating its mean yields
\[
 \frac{dM}{d\log u}=\operatorname{Var}_u(\ell)>0.
\]
Consequently \(M\) is strictly increasing. As \(u\downarrow0\), \(M(u)\to0\); as \(u\uparrow1\), the coefficient asymptotic \(a_{j+m\ell}\sim(m\ell)^{\beta-1}/\Gamma(\beta)\) gives \(M(u)\sim\beta/(1-u)\to\infty\). For \(q\ge1\), the derivative changes sign once and only once, so the critical radius is a strict global maximum. For \(q=0\), the derivative is strictly negative, the supremum is \(a_j/a_j=1\) at the excluded endpoint, and every positive-radius capture is strictly less than one.

**3. Gamma asymptotics.** For fixed \(m,j,\beta\), the coefficient asymptotic and comparison of positive power series with their Laplace integrals yield
\[
 F(u)\sim m^{\beta-1}(1-u)^{-\beta},\qquad
 M(u)\sim\beta(1-u)^{-1}
 \quad(u\uparrow1).
\]
The unique equation \(M(u_q)=q\) implies \(1-u_q\sim\beta/q\), hence \(u_q^q\to e^{-\beta}\). Also \(a_{qm+j}\sim(mq)^{\beta-1}/\Gamma(\beta)\). Substituting in the exact projection identity proves the Gamma law without relying on a finite numerical experiment.

**4. Ordinary Bergman specialization and correction.** For \(\beta=2\), one has \(a_n=n+1\) and the geometric and differentiated-geometric sums give
\[
 F(u)=\frac{A+Bu}{(1-u)^2}.
\]
Differentiating the resulting rational expression gives exactly the stated quadratic. The general strict-variance argument establishes that it has a unique root in \((0,1)\), including the linear case \(B=0\). Expanding this algebraic equation around \(u=1\) gives \(1-u_q=2/q-(2+2A/m)/q^2+O(q^{-3})\). Substitution into the explicit rational expression and expansion of \(q\log u_q\) gives the stated residue-dependent correction. All remainders here are for fixed \(m,j\).

## Verification
The standalone `verify.py` uses only the Python 3 standard library. Running `python3 verify.py` solves finite evaluation-kernel Gram systems using a separate linear-system implementation, compares them against the exact residue formula, checks maximizing radii and the explicit quadratic, and diagnoses the Gamma and first-correction limits. Its final output is `PASS: 347 finite checks (direct Gram, root, expansions, Gamma scaling)`. These computations are supplementary; the universal and asymptotic assertions are established analytically in the proof above. For illustration, in the ordinary Bergman case, \((m,N)=(2,2)\) gives \(u_*=(\sqrt{17}-3)/4\) and optimal captured energy approximately \(0.3402016367\); \((m,N)=(3,7)\) gives approximately \(u_*=0.4748096336\) and captured energy \(0.2010114218\).

## Relationship to prior work
Qu, Qian, and Deng (2020) and Qian (2022) establish general existence of best approximants by kernel sections in analytic reproducing-kernel Hilbert spaces. In particular, their **unrestricted** approximation problems differ from the **fixed cyclic angular orbit with variable radius** treated here; their inspected theorem statements and main sections do not give the exact cyclic monomial projection, radius equation, or Gamma limit. Gröchenig and Ortega-Cerdà (2021) study polynomial sampling and interpolation in Fock spaces, a related but different kernel and optimization regime. The present result does not claim to settle unrestricted best approximation and does not reassert general kernel existence.

## Limitations
Only same-author mathematical checking of the derivation and reproducible finite diagnostics have been carried out; no independent audit or complete historical-priority determination is claimed. The literature comparison leaves a residual possibility of an equivalent older circulant-Gram or optimal kernel-dictionary theorem, especially outside the reviewed papers. The 2020 preprint could be assessed only through its accessible abstract, not its complete full text. Finite experiments do not independently certify an infinite-dimensional proof. Rotations give the same capture, and the uniqueness assertion is about the positive radius, not a unique physical orientation.

## References
- W. Qu, T. Qian, G.-T. Deng, *A sufficient condition for n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, first posted 5 June 2020, arXiv:2006.03290. https://arxiv.org/abs/2006.03290
- T. Qian, *n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, first posted 18 January 2022, arXiv:2201.07228. https://arxiv.org/abs/2201.07228
- K. Gröchenig, J. Ortega-Cerdà, *Marcinkiewicz-Zygmund Inequalities for Polynomials in Fock Space*, first posted 24 September 2021, arXiv:2109.11825. https://arxiv.org/abs/2109.11825
