# The Poisson–Bernstein boundary of iterated Aluthge transforms of polynomial shifts

## Finding

Let \(W_\beta e_j=(j+1)^{-\beta}e_{j+1}\) on \(\ell^2(\mathbb N_0)\), for \(\beta>0\). For each integer \(n\ge1\), choose any \(t_n\in[0,1]\) and put \(m_n=nt_n\). There is a complete sharp boundary law for the \(n\)-fold generalized Aluthge iterate \(A_n=\Delta_{t_n}^{n}(W_\beta)\).

Fix a Schatten exponent \(r>0\) with \(\alpha=\beta r>1\). If \(m_n\to\lambda\in[0,\infty)\), then \(A_n\to\mathcal P_\lambda W_\beta\) in \(\mathcal S_r\), where
\[
\mathcal P_\lambda W_\beta e_j=b_j(\lambda)e_{j+1},\qquad b_j(\lambda)=\exp\bigl(-\beta\,\mathbb E\log(j+1+P_\lambda)\bigr),\quad P_\lambda\sim\mathrm{Poisson}(\lambda).
\]
If instead \(m_n\to\infty\), then the **sharp** decay law, for *every* such parameter sequence, is
\[
\|A_n\|_{\mathcal S_r}^{r}\sim\frac{m_n^{1-\alpha}}{\alpha-1}.
\]
For each \(\lambda\ge0\), the spectral trace \(F_r(\lambda)=\|\mathcal P_\lambda W_\beta\|_{\mathcal S_r}^{r}\) is strictly completely monotone, has \(F_r(0)=\zeta(\alpha)\), and satisfies the identical large-parameter equivalent \(F_r(\lambda)\sim\lambda^{1-\alpha}/(\alpha-1)\). It has an explicit infinite-divisibility representation given below. The maps \(\mathcal P_\lambda\) form a semigroup on strictly positive weight sequences for which the defining Poisson expectations are finite.

## Assumptions and scope

The Hilbert space is complex \(\ell^2(\mathbb N_0)\), indexed from \(j=0\). For \(T=U|T|\), use \(\Delta_t(T)=|T|^t U|T|^{1-t}\), \(0\le t\le1\). Schatten \(\mathcal S_r\) quasi-norms for \(0<r<1\) are permitted: \(\|T\|_{\mathcal S_r}^{r}\) is the sum of the \(r\)-th powers of its singular values. The strict condition \(\beta r>1\) is necessary because the original shift and all its finite iterates have weights asymptotic to \(j^{-\beta}\). The convergence assertions concern sequences \(n\to\infty\), with no requirement that \(t_n\) tend to a fixed interior value.

## Proof

**1. Exact binomial weights.** A positive unilateral shift with weights \(w_j\) transforms under \(\Delta_t\) to the shift with weights \(w_j^{1-t}w_{j+1}^{t}\). Induction, or commutation of \(I\) with the forward shift on logarithmic weights, gives
\[
A_ne_j=a_{n,j}e_{j+1},\qquad a_{n,j}=\exp\bigl(-\beta\,\mathbb E\log(j+1+K_n)\bigr),\quad K_n\sim\mathrm{Binomial}(n,t_n).
\]
All weights are positive and satisfy \(0<a_{n,j}\le(j+1)^{-\beta}\).

**2. Critical finite-mean boundary.** If \(m_n=nt_n\to\lambda<\infty\), the binomial generating functions \((1+t_n(z-1))^n\to e^{\lambda(z-1)}\) give \(K_n\Rightarrow P_\lambda\). The logarithmic functions are uniformly integrable because \(\log(j+1+k)\le\log(j+1)+k\), and the second moments of \(K_n\) are uniformly bounded. Thus \(a_{n,j}\to b_j(\lambda)\) for every fixed \(j\). Dominated convergence applied to \(\sum_{j\ge0}|a_{n,j}-b_j(\lambda)|^r\), bounded by a fixed multiple of \(\sum_{j\ge0}(j+1)^{-\beta r}\), proves convergence in \(\mathcal S_r\). This also establishes norm convergence for all \(\beta>0\).

**3. Uniform diverging-mean boundary.** Suppose \(m=m_n\to\infty\). Binomial concentration yields \(K_n/m\to1\) in probability and \(\delta_n:=\mathbb P(K_n<m/2)\le e^{-m/8}\). For each fixed \(u\ge0\), a lower-tail split and concentration show
\[
m^\alpha a_{n,\lfloor mu\rfloor}^{r}\longrightarrow(1+u)^{-\alpha}.
\]
For uniform integrable domination, the monotonicity of the logarithm gives, for every \(j\ge0\),
\[
a_{n,j}^{r}\le(j+1+m/2)^{-\alpha}\left(\frac{j+1+m/2}{j+1}\right)^{\alpha\delta_n}\le(1+m/2)^{\alpha e^{-m/8}}(j+1+m/2)^{-\alpha}.
\]
The prefactor tends to one. Therefore the normalized tail of the sum past \(j>Rm\) is at most an asymptotically negligible multiple of \(\int_R^\infty(u+1/2)^{-\alpha}du\), which tends to zero with \(R\). Riemann sums on \(0\le j\le Rm\), then \(R\to\infty\), give
\[
\sum_{j\ge0}a_{n,j}^r\sim m^{1-\alpha}\int_0^\infty(1+u)^{-\alpha}du=\frac{m^{1-\alpha}}{\alpha-1}.
\]
The same argument applies to Poisson variables with mean \(m=\lambda\), proving the stated large-\(\lambda\) law for \(F_r\).

**4. Nonlinear semigroup and Lévy representation.** For a positive weight sequence \(w\) with finite relevant expectations define \((\mathcal P_\lambda w)_j=\exp[\mathbb E\log w_{j+P_\lambda}]\). Independent Poisson increments and Fubini give \(\mathcal P_\lambda\mathcal P_\mu=\mathcal P_{\lambda+\mu}\). The Frullani logarithm representation and the Poisson probability-generating function yield
\[
\mathbb E\log(j+1+P_\lambda)-\log(j+1)
=\int_0^1(1-e^{-\lambda u})\frac{(1-u)^j}{-\log(1-u)}\,du.
\]
Consequently
\[
F_r(\lambda)=\sum_{j\ge0}(j+1)^{-\alpha}\exp\left[-\alpha\int_0^1(1-e^{-\lambda u})\frac{(1-u)^j}{-\log(1-u)}\,du\right].
\]
Each kernel \(\nu_j(du)=\alpha(1-u)^j\,du/[-\log(1-u)]\) has infinite mass near zero but finite \(\int_0^1u\nu_j(du)\). Truncating it below \(\varepsilon\), the exponential factor is the Laplace transform of a compound-Poisson sum. The compound-Poisson sums converge as \(\varepsilon\downarrow0\), since the expected discarded total jump is bounded by \(\int_0^\varepsilon u\nu_j(du)\to0\). Hence each factor is the Laplace transform of a strictly positive, infinitely divisible nonnegative random variable \(Z_j\). The jump intensities decrease with \(j\), so the variables can be coupled with \(0\le Z_j\le Z_0\). Bounded jumps and finite exponential moments of \(Z_0\) imply termwise differentiation of every order after summation against \((j+1)^{-\alpha}\). It follows that for every integer \(k\ge0\) and \(\lambda\ge0\),
\[
(-1)^kF_r^{(k)}(\lambda)=\sum_{j\ge0}(j+1)^{-\alpha}\mathbb E[Z_j^k e^{-\lambda Z_j}]>0.
\]
This proves strict complete monotonicity. At \(\lambda=0\), the weights equal \((j+1)^{-\beta}\), giving \(F_r(0)=\zeta(\alpha)\).

## Verification

The proof is analytical. Direct numerical checks used exact binomial probabilities and Poisson probability masses for \(\beta\in\{0.6,1.2\}\), \(\lambda\in\{0.4,1.5,4\}\), and iteration counts \(20,70,250\); the first-weight differences decreased toward zero. An independent truncated trace calculation with a Hurwitz-zeta tail correction at \(\alpha=1.8\) gave normalized ratios to the predicted large-parameter equivalent of approximately \(0.968,0.993,0.998,0.999\) at \(\lambda=5,20,60,120\). Finite tests are supplementary and do not prove the asymptotics or derivative signs.

## Relationship to prior work

Stanković (2026, Proposition 5.8) gives the binomial weight identity and convergence to zero for a **fixed** parameter strictly between zero and one. The theorem here concerns a varying Aluthge parameter, the nonvanishing critical Poisson limit, a continuous positive-weight semigroup, the exact infinitely divisible trace representation and all-order complete monotonicity. A separate earlier result on regularly varying weighted shifts gives sharp macroscopic profiles for fixed interior parameters; those fixed-parameter cases are not claimed as new. Research records concerning stretched-exponential unilateral or bilateral shifts likewise have different objects and scales. The original binomial identity and standard Poisson approximation are background facts, not claimed discoveries.

## Limitations

This theorem addresses the specific polynomial-weight positive unilateral shift and Schatten exponents satisfying \(\beta r>1\), rather than arbitrary compact operators. It does not establish an analogous completely monotone family for arbitrary positive weight sequences. The eigenvalues of these weighted shifts are not the spectral trace being studied: the trace uses singular values. An equivalent older Bernstein-function or weighted-shift formulation cannot be categorically ruled out without further bibliographic inspection. Independent mathematical validation has not been performed.

## References

- H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1 (first submitted 5 November 2026), especially Proposition 5.8 and its exact binomial weight formula.
- J. Antezana, E. Pujals and D. Stojanoff, *Iterated Aluthge transforms: a brief survey*, Revista de la Unión Matemática Argentina 49 (2008), 29–41.
- G. R. Exner, *Aluthge transforms and \(n\)-contractivity of weighted shifts*, Journal of Operator Theory 61 (2009), 419–438.
