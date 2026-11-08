# An explicit Gaussian–Laguerre witness to the Fock endpoint Schatten gap

## Finding

Let \(F^2\) be the classical one-dimensional Bargmann–Fock space with norm from \(d\mu(z)=(2\pi)^{-1}e^{-|z|^2/2}\,dA(z)\). For an admissible measurable symbol \(g\), write \(T_gf=P(gf)\), initially on its natural domain, and define its endpoint heat transform by
\[
\mathcal H g(a)=\pi^{-1}\int_{\mathbb C}g(z)e^{-|z-a|^2}\,dA(z).
\]
Here \(\mathcal H g=g^{(1/4)}\) in the Berger–Coburn normalization. We give a completely prescribed, real-valued, \(C^\infty\) symbol \(g\), assembled from explicit translated Gaussian–Laguerre polynomials, for which
\[
 g\in\mathcal T_1,\qquad T_g\in\bigcap_{p>1}S_p,\qquad\sup_{a\in\mathbb C}|\mathcal H g(a)|=\infty.
\]
The class \(\mathcal T_1\) means that \(\int_{\mathbb C}|g(z)|^2e^{-|z-a|^2/4}\,dA(z)<\infty\) for every \(a\in\mathbb C\). In particular, the symbol satisfies the coherent-state Toeplitz-domain condition, and \(T_g\notin S_1\) by the known trace-class endpoint inequality.

The construction is nonexistential: for each integer \(j\ge1\), set
\[
 N_j=2^{j^2},\quad t_j=N_j^{-4},\quad b_j=j/N_j,\quad w_j=2^{N_j^3}\in\mathbb R.
\]
For every integer \(m\ge0\) and \(0<t\le1/16\), define the ordinary Laguerre polynomial
\[
 L_m(u)=\sum_{\ell=0}^m(-1)^\ell\binom m\ell\frac{u^\ell}{\ell!},
\]
and the real radial Gaussian–Laguerre symbol
\[
 G_{m,t}(z)=(-1)^m t^{-(m+1)}\exp\!\left[-\frac{t^{-1}-1}{2}|z|^2\right]L_m\!\left(\frac{|z|^2}{2t}\right).
\]
Set \(G_{N,t}=\sum_{m=0}^{N-1}(-1)^mG_{m,t}\) and finally
\[
 \boxed{g(z)=\sum_{j=1}^{\infty}b_jG_{N_j,t_j}(z-w_j).}
\]
The individual Gaussian–Laguerre blocks and their binomial diagonal were constructed earlier by Esmeral García and Maximenko [5]. The present contribution is the explicit signed parity-block assembly, trace-norm control, and globally separated all-\(p>1\) endpoint example. No choice principles, unspecified approximants, or Baire-category argument enter the displayed construction.

## Assumptions and scope

We work over \(\mathbb C\), in one complex dimension. The normalized monomial basis is \(e_k(z)=z^k/\sqrt{2^k k!}\), \(k\ge0\), and \(P\) denotes the orthogonal Fock projection. The Schatten norm is \(\|A\|_{S_p}=(\sum_k s_k(A)^p)^{1/p}\) for \(p\ge1\). The source's \(\mathcal T_1\) condition is a symbol-integrability condition, not the trace class \(S_1\). The centers \(w_j\) are positive real numbers, not Gaussian widths. All statements about the infinite series are proved for the fixed numerical sequences displayed above; no claim is made for arbitrary centers.

## Proof

**1. Exact Laguerre Toeplitz eigenvalues.** For a radial symbol \(h\), angular orthogonality makes \(T_h\) diagonal, with
\[
 \langle T_he_k,e_k\rangle=\frac1{k!}\int_0^\infty h(\sqrt{2s})e^{-s}s^k\,ds.
\]
Integrating the polynomial definition of \(G_{m,t}\) against the gamma integral gives
\[
 \boxed{\langle T_{G_{m,t}}e_k,e_k\rangle=\begin{cases}
 0,&0\le k<m,\\ \binom{k}{m}t^{k-m},&k\ge m.
 \end{cases}}
\]
The identity follows, for example, from
\[
 \sum_{\ell=0}^m(-1)^\ell\binom m\ell\binom{k+\ell}{\ell}=(-1)^m\binom{k}{m},
\]
with the usual zero convention for \(k<m\). In particular, each \(T_{G_{m,t}}\) is positive trace class and
\[
 \operatorname{tr}(T_{G_{m,t}})=(1-t)^{-(m+1)}.
\]
Although the function \(G_{m,t}\) changes sign when \(m\ge1\), positivity here concerns its diagonal Toeplitz operator.

**2. Quantitative approximation to parity projections.** Let \(J_Ne_k=(-1)^ke_k\) for \(0\le k<N\) and \(J_Ne_k=0\) for \(k\ge N\). Linearity and the preceding eigenvalues yield
\[
 \|T_{G_{N,t}}-J_N\|_{S_1}
 \le \sum_{m=0}^{N-1}\big((1-t)^{-m-1}-1\big).
\]
When \(t=N^{-4}\) and \(N\ge2\), Bernoulli's inequality and \((m+1)t\le N^{-3}\le1/8\) give
\[
 (1-t)^{-m-1}-1\le\frac{(m+1)t}{1-(m+1)t}\le 2(m+1)t.
\]
Consequently,
\[
 \boxed{\|T_{G_{N,N^{-4}}}-J_N\|_{S_1}\le 2N^{-2},\qquad
 \|T_{G_{N,N^{-4}}}\|_{S_p}\le N^{1/p}+2N^{-2}\ (p\ge1).}
\]
This is an approximation, not an exact finite-rank Toeplitz realization.

**3. Exact endpoint peaks.** Direct Gaussian integration, or summation of the diagonal parity trace for the trace-class block, shows
\[
 \mathcal H G_{m,t}(0)=\frac{2(-1)^m}{(1+t)^{m+1}}.
\]
Hence the alternating block satisfies the exact formula
\[
 \boxed{\mathcal H G_{N,t}(0)=2\sum_{m=0}^{N-1}(1+t)^{-m-1}
 =\frac{2[1-(1+t)^{-N}]}{t}.}
\]
For \(N\ge2\) and \(t=N^{-4}\), the elementary lower bound \((1+t)^{-r}\ge1-rt\) gives
\[
 \mathcal H G_{N,t}(0)\ge2N-N(N+1)t\ge\tfrac32N.
\]
Thus the \(j\)-th translated, rescaled block has endpoint peak at least \(3j/2\), while its \(S_p\)-norm is at most \(jN_j^{1/p-1}+2jN_j^{-3}\).

**4. Gaussian envelopes and absolute convergence.** For \(u\ge0\), the Laguerre sum satisfies
\[
 |L_m(u)|\le\sum_{\ell\ge0}\frac{(mu)^\ell}{(\ell!)^2}
 \le e^{2\sqrt{mu}}\le e^{2m+u/2}.
\]
Since \(t=N^{-4}\le1/16\), it follows that
\[
 \boxed{|G_{N,N^{-4}}(z)|\le e^{6N^2}e^{-7|z|^2/2}.}
\]
Convolving against the endpoint Gaussian therefore gives the pointwise bound
\[
 \boxed{|\mathcal HG_{N,N^{-4}}(a)|\le e^{6N^2}e^{-|a|^2/2}.}
\]
The two centers corresponding to different indices satisfy \(|w_j-w_k|\ge\frac12\max\{w_j,w_k\}\). As \(w_j^2/8=2^{2N_j^3}/8\ge11N_j^3\), the upper bound on the endpoint heat transform gives, for each \(j\),
\[
 \sum_{k\ne j}b_k|\mathcal HG_{N_k,t_k}(w_j-w_k)|
 \le\sum_{k\ge1}\frac{k}{N_k}e^{6N_k^2-w_k^2/8}
 \le\sum_{k\ge1}2^{-k-5}<1/32.
\]
The last displayed inequality uses \(N_k\ge\max\{2,k\}\), and holds by direct elementary comparison of exponents. Therefore
\[
 |\mathcal Hg(w_j)|\ge\tfrac32j-1/32\longrightarrow\infty,
\]
provided the convolution may be interchanged with the series. This interchange is justified next.

**5. Symbol admissibility and smoothness.** Define for each positive integer \(j\) the weighted norm
\[
 Q_j(h)^2=(2\pi)^{-1}\int_{\mathbb C}|h(z)|^2
 e^{-|z|^2/4+j|z|}\,dA(z).
\]
The bound in Step 4, the inequality \(j|z|\le|z|^2/8+2j^2\), and a Gaussian integral imply
\[
 Q_j\big(b_jG_{N_j,t_j}(\cdot-w_j)\big)^2
 \le\frac4{57}\exp\big(12N_j^2+2j^2-7w_j^2/57\big)
 \le2^{-2j}.
\]
For each fixed \(a\in\mathbb C\) and all sufficiently large \(j\), this dominates the weighted \(L^2\) norm with weight \(e^{-|z-a|^2/4}\). The triangle inequality therefore shows that the entire series defines a symbol in \(\mathcal T_1\), as well as a symbol with \(gk_a\in L^2(d\mu)\) for every \(a\). Cauchy–Schwarz in the Gaussian kernel then permits absolute termwise endpoint convolution.

Each summand is a polynomial of degree \(2(N_j-1)\) in the two real coordinates times a centered Gaussian. Differentiating any fixed number of times introduces polynomial factors and powers of \(N_j\), bounded by an exponential of a polynomial in \(N_j\); on any fixed compact set their Gaussian factor at distance at least \(w_j-O(1)\) dominates these factors, because \(w_j=2^{N_j^3}\). Thus the series and all its real-coordinate derivative series converge uniformly on compact sets. The symbol is real-valued and \(C^\infty\).

**6. The Schatten conclusion.** Translation covariance gives \(T_{h(\cdot-w)}=W_wT_hW_w^*\) for the Fock Weyl unitary \(W_w\). For every fixed \(p>1\), Step 2 yields the convergent series
\[
 \sum_{j\ge1}b_j\|T_{G_{N_j,t_j}}\|_{S_p}
 \le\sum_{j\ge1}\left(j\,2^{-j^2(1-1/p)}+2j\,2^{-3j^2}\right)<\infty.
\]
The Toeplitz operators therefore converge in \(S_p\) to a bounded operator. The admissibility proved in Step 5 identifies this limit on the dense span of reproducing kernels with the Toeplitz form of the full symbol \(g\). Hence \(T_g\in S_p\) for every \(p>1\). The known trace-class endpoint estimate \(\|\mathcal Hg\|_\infty\le2\|T_g\|_{S_1}\) forces \(T_g\notin S_1\), since its endpoint transform is unbounded. This concludes the proof.

## Verification

The accompanying `CHECK.py` is standalone Python using only integer arithmetic and `fractions.Fraction`. It checks the gamma/Laguerre moment identity, each diagonal prefix identity, the exact endpoint heat coefficients, and the quantitative trace-error and heat-peak inequalities for \(2\le N\le16\), at the stated rational parameters. It reports `GAUSSIAN_LAGUERRE_MOMENTS_EXACT_OK 3160` (3,160 assertions). The Gaussian envelopes, infinite-series convergence, and all-Schatten conclusion are analytical, not finite-enumeration claims. The numerical centers beyond the first are astronomically large by design; no attempt is made to evaluate the entire series numerically.

## Relationship to prior work

Virtanen [1, Theorem 1.1(ii), Theorem 3.3] proves abstract existence of an admissible symbol with \(T_g\in\bigcap_{p>1}S_p\) and unbounded endpoint transform, expressly noting that the example is nonconstructive. Its proof approximates finite-rank parity truncations using a density theorem and Baire category, without explicit formulae for the approximating Toeplitz symbols. The present contribution is therefore **not** the existential implication, which is already known. Moreover, Esmeral García and Maximenko [5, Definition 3 and Lemma 4.2] already give precisely the individual Gaussian–Laguerre blocks and their binomial eigenvalues, in a rescaled Fock normalization. The new claim is their quantitative **signed parity-block trace-norm assembly**, together with closed-form rapidly separated centers and amplitudes that realize the simultaneous all-\(p>1\) Schatten versus endpoint-heat separation. Their paper treats uniform eigenvalue approximation of convergent sequences; it does not construct this unbounded endpoint heat transform with all-\(p>1\) Schatten membership.

Looi [2] gives a different explicit translated-Schwartz construction disproving the original boundedness endpoint conjecture, without establishing simultaneous membership in all \(S_p\) for \(p>1\). Looi [3] gives smooth real symbols with prescribed sets of bounded heat times, again without the present explicit all-\(p>1\) Toeplitz-ideal conclusion. The classical finite-rank obstruction [4] is respected: every individual Gaussian–Laguerre Toeplitz approximant has an infinite, exponentially decaying diagonal tail.

## Limitations

The proof is one-dimensional and does not assert optimal size of the translation centers, boundedness of the symbol, or finite trace norm of \(T_g\). The exact spectral identities are for individual radial blocks, not for the translated sum. This is a constructive refinement of a published existence theorem, not a new endpoint exponent or a disproof of a still-open boundedness conjecture. The individual Laguerre block formula and exact binomial diagonal are already published in [5] and are not claimed novel; the claim concerns their specific trace-norm endpoint assembly. Other prior explicit series with the same all-\(p>1\) separation may exist. Publication priority has not been independently certified.

## References

1. J. A. Virtanen, *Critical Schatten exponents for the Berger–Coburn endpoint problem*, arXiv:2609.11853v3 (first submitted 2026-09-10), https://arxiv.org/html/2609.11853v3.
2. S. Looi, *A counterexample to the Berger–Coburn conjecture*, arXiv:2601.20859v1 (2026), https://arxiv.org/html/2601.20859.
3. S. Looi, *Bounded Toeplitz operators and unbounded projected multiplication*, arXiv:2601.10711v2 (2026), https://arxiv.org/html/2601.10711v2.
4. A. Borichev and G. Rozenblum, *The finite rank theorem for Toeplitz operators in the Fock space*, arXiv:1303.2996 (2013), https://arxiv.org/abs/1303.2996.
5. K. Esmeral García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators*, arXiv:2503.23276v1 (2025), https://arxiv.org/html/2503.23276v1, especially Definition 3 and Lemma 4.2.
