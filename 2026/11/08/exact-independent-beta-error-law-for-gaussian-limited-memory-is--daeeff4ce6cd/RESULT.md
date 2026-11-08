# Exact independent beta error law for Gaussian limited-memory IS-Krylov

## Finding

For a consistent real least-squares system with scaled-orthonormal columns and independent one-column Gaussian sketches, the positive squared-error contractions of the exact limited-memory IS-Krylov iteration are **mutually independent beta random variables** (with a final deterministic zero at full memory), even though the orthogonalization window is chosen adaptively from previous random directions. Their parameters depend only on dimension and the current memory-window size. Consequently, finite-time error moments, sharp inverse-error moment thresholds, the exact expected contraction, and the almost-sure logarithmic rate have closed forms.

Let \(d\ge 2\), \(n\ge d\), \(1\le\ell\le d\), \(A\in\mathbb R^{n\times d}\), and \(A^{\mathsf T}A=\lambda I_d\) for some \(\lambda>0\). Choose consistent data \(b=Ax_\star\), a deterministic \(x_0\ne x_\star\), and independent \(s_k\sim N(0,I_n)\). Apply the one-column-sketch, \(\ell\)-memory exact IS-Krylov update specified below. Put

\[
R_j=\frac{\|x_{j+1}-x_\star\|_2^2}{\|x_j-x_\star\|_2^2},\qquad
m_j=d-\min\{j,\ell-1\}.
\]

For every step before exact termination with \(m_j\ge 2\),

\[
\boxed{R_j\sim\operatorname{Beta}\!\left(\frac{m_j-1}{2},\frac12\right),\quad
\{R_j:\ m_j\ge2\}\ \text{mutually independent}.}
\]

If \(\ell=d\), the update at step \(j=d-1\) has \(R_{d-1}=0\) almost surely, so the method terminates after \(d\) updates; this finite-termination property itself was known in prior work. If \(\ell<d\), every \(R_j\) lies strictly between zero and one almost surely, so the method never reaches the exact solution in finitely many updates. In that case, for every \(k\ge1\) and real \(q\) with \(q>-(d-\ell)/2\),

\[
\boxed{
\mathbb E\left[\left(\frac{\|x_k-x_\star\|_2^2}{\|x_0-x_\star\|_2^2}\right)^{q}\right]
=\prod_{j=0}^{k-1}\frac{\Gamma(a_j+q)\Gamma(a_j+\tfrac12)}{\Gamma(a_j)\Gamma(a_j+\tfrac12+q)},
\quad a_j=\frac{m_j-1}{2}.}
\]

For \(k\ge\ell\) and negative \(q=-t\), this moment is finite **if and only if** \(t<(d-\ell)/2\). The exact normalized mean squared error is

\[
\frac{\mathbb E\|x_k-x_\star\|_2^2}{\|x_0-x_\star\|_2^2}
=\begin{cases}
(d-k)/d,&0\le k<\ell,\\
\dfrac{d-\ell+1}{d}\left(\dfrac{d-\ell}{d-\ell+1}\right)^{k-\ell+1},&k\ge\ell,
\end{cases}
\]

with the formula applying until termination; if \(\ell=d\), the second case gives zero at \(k=d\) and the iterate then remains exact. When \(\ell<d\), the almost-sure squared-error exponent is

\[
\boxed{\lim_{k\to\infty}\frac1k\log\frac{\|x_k-x_\star\|_2^2}{\|x_0-x_\star\|_2^2}
=\psi\!\left(\frac{d-\ell}{2}\right)-\psi\!\left(\frac{d-\ell+1}{2}\right),}
\]

where \(\psi\) is the digamma function. In the one-retained-direction case \(\ell=2\), this also specializes to rank-one Gaussian RCGLS. In dimension \(d=3\), the persistent contraction is \(\operatorname{Beta}(1/2,1/2)\): its mean is \(1/2\), but its almost-sure geometric squared-error factor is \(1/4\).

## Assumptions and scope

All assertions use exact real arithmetic, a consistent system, an initial point distinct from the solution, fresh independent Gaussian sketches, one Gaussian column per iteration, and an orthogonalization window containing the most recent \(\ell-1\) directions. The constant \(\lambda\) and ambient row dimension \(n\) do not affect the distribution because \(A^{\mathsf T}s_k/\sqrt\lambda\) are independent standard Gaussian vectors in \(\mathbb R^d\). The method is defined at each nonterminal step and terminates upon reaching zero residual.

Precisely, write \(e_j=x_\star-x_j\), \(d_j=A^{\mathsf T}s_j s_j^{\mathsf T}A e_j\), \(j_j=\max\{0,j-\ell+1\}\), and

\[
p_j=d_j-\sum_{i=j_j}^{j-1}\frac{\langle d_j,p_i\rangle}{\|p_i\|_2^2}p_i,\qquad
\alpha_j=\frac{|s_j^{\mathsf T}A e_j|^2}{\|p_j\|_2^2},\qquad
x_{j+1}=x_j+\alpha_jp_j.
\]

All denominators are nonzero almost surely before termination. These are the exact formulas of the one-column specialization of Sun, Han and Xie's IS-Krylov Algorithm 3; at \(\ell=2\) they agree with the one-step-conjugacy mechanism of Zeng, Cai, Han and Xie's RCGLS Algorithm 1 under the specified scaled-isometric design.

## Proof

**Step 1: deterministic orthogonality invariant.** Set \(W_j=\operatorname{span}\{p_i:\max(0,j-\ell+1)\le i<j\}\). By induction, the directions spanning \(W_j\) are nonzero and mutually orthogonal, and \(e_j\perp W_j\). Initially \(W_0=\{0\}\). The Gram--Schmidt definition makes \(p_j\perp W_j\); the update is the exact Euclidean projection of \(e_j\) onto \(p_j\), so \(e_{j+1}\perp p_j\), and it remains perpendicular to all retained old directions. Thus the invariant propagates and \(\dim W_j=\min\{j,\ell-1\}\) almost surely until termination.

**Step 2: Gaussian reduction and exact projection.** Let \(z_j=A^{\mathsf T}s_j/\sqrt\lambda\sim N(0,I_d)\). Because the residual is \(A e_j\) and \(A^{\mathsf T}A=\lambda I_d\),

\[
d_j=\lambda\langle z_j,e_j\rangle z_j,\qquad
p_j=\lambda\langle z_j,e_j\rangle v_j,\quad
v_j=(I-P_{W_j})z_j.
\]

The invariant gives \(\langle z_j,e_j\rangle=\langle v_j,e_j\rangle\), and the stated stepsize reduces to

\[
\alpha_jp_j=\frac{\langle e_j,v_j\rangle}{\|v_j\|_2^2}v_j,\qquad
e_{j+1}=e_j-\frac{\langle e_j,v_j\rangle}{\|v_j\|_2^2}v_j.
\]

The Gaussian \(v_j\), conditionally on all prior sketches, is rotationally invariant in the \(m_j\)-dimensional space \(W_j^\perp\). The current nonzero \(e_j\) lies in that space. The squared cosine \(\langle e_j,v_j\rangle^2/(\|e_j\|_2^2\|v_j\|_2^2)\) therefore has the \(\operatorname{Beta}(1/2,(m_j-1)/2)\) law, and the squared-error contraction is one minus that cosine. At \(m_j=1\), the cosine equals one. This also proves that the next direction and every needed denominator are nonzero almost surely before exact termination.

**Step 3: independence, expectations, and sharp boundaries.** The conditional distribution of \(R_j\) given all preceding sketches depends only on the *deterministic* integer \(m_j\). Therefore \(R_j\) is independent of all preceding sketches and of all preceding contractions; induction proves mutual independence. The beta Mellin identity gives the moment product. For \(\ell<d\), \(m_j\ge d-\ell+1\ge2\), and \(R_j>0\) almost surely. The smallest beta left-shape, attained from \(j=\ell-1\) onward, is \((d-\ell)/2\); the beta density near zero proves the claimed exact inverse-moment cutoff once at least one such factor appears. Taking \(q=1\) gives \(\mathbb ER_j=(m_j-1)/m_j\), and telescoping the transient factors yields the displayed expected error. In the persistent regime, the \(R_j\) are independent and identically distributed; their logarithms have finite absolute expectation equal to the stated digamma difference. The strong law proves the almost-sure exponent. Finally, if \(\ell=d\), after \(d-1\) nonterminal updates the error and projected Gaussian both belong to the same one-dimensional complement, so the \(d\)-th update is exact.

## Verification

Run `python3 verify.py` using the Python standard library. Its deterministic tests compare the actual nonnormalized source-style updates with Euclidean projection formulas, and sample independent sketches at multiple dimensions and memory lengths; observed first and second moments of each step and total squared error are compared with the exact formulas. These numerical checks supplement, but do not substitute for, the analytic proof.

## Relationship to prior work

Sun, Han and Xie's 2025 IS-Krylov paper defines the limited-memory iteration and establishes general expected convergence bounds, along with the **already-known** finite-termination fact for memory at least the matrix rank. Zeng, Cai, Han and Xie's 2026 RCGLS paper gives the corresponding one-previous-direction scheme and an expected convergence bound. Zeng, Han, Su and Xie's earlier stochastic conjugate-gradient analysis treats two-direction acceleration. The present theorem concerns instead the *entire finite-horizon error distribution*, mutual independence of adaptive contraction factors, exact inverse-moment integrability, and an almost-sure logarithmic rate for scaled-isometric data. The one-dimensional Gaussian squared-cosine beta law used in the proof is classical; the claimed result is its rigorous dynamical specialization to the sliding-window method, not a new beta-identity or a new finite-termination theorem.

General sketch-and-project spectral convergence theory gives broader matrix classes but does not, in the inspected material, supply this full adaptive-memory product distribution. An undiscovered equivalent probabilistic formulation remains possible.

## Limitations

The theorem does not treat anisotropic or ill-conditioned normal matrices, block sketches of width greater than one, non-Gaussian or structured sketches, noisy inconsistent systems, or finite-precision loss of orthogonality. Finite experimental testing cannot certify the infinite-dimensional parameter ranges or prove historical novelty. The exact distribution remains conditional on the stated scaled-isometric, independent-Gaussian and exact-arithmetic assumptions.

## References

- Y. Sun, D. Han, and J. Xie, *Connecting randomized iterative methods with Krylov subspaces*, arXiv:2505.20602v1, first public May 27, 2025, Algorithm 3, Theorem 3.3, Remark 3.6. https://arxiv.org/html/2505.20602v1
- Y. Zeng, J.-F. Cai, D. Han, and J. Xie, *Randomized conjugate gradient least squares*, arXiv:2605.25034v1, first public May 24, 2026, Algorithm 1 and Theorem 2.4. https://arxiv.org/html/2605.25034
- Y. Zeng, D. Han, Y. Su, and J. Xie, *On adaptive stochastic heavy ball momentum for solving linear systems*, arXiv:2305.05482, May 9, 2023, Theorem 5.1 and convergence analysis. https://arxiv.org/abs/2305.05482
- R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296, 2015. https://arxiv.org/abs/1506.03296
- M. Dereziński and E. Rebrova, *Sharp Analysis of Sketch-and-Project Methods via a Connection to Randomized Singular Value Decomposition*, arXiv:2208.09585, 2022. https://arxiv.org/abs/2208.09585
