# Exponential Riesz-projection conditioning and Bessel crossover for compact generalized Cesàro operators

## Finding
For the compact generalized Cesàro operator \(C_t\) on \(\ell^2(\mathbb N_0)\) and the spectral (Riesz) projection \(P_m(t)\) at its simple eigenvalue \(\lambda_m=1/(m+1)\), the following exact formula holds for all integers \(m\ge0\) and \(0\le t<1\):
\[
\boxed{\|P_m(t)\|=(1-t^2)^{-m-1/2}\sum_{k=0}^{m}\binom{m}{k}^{2}t^{2k}.}
\]
For every fixed \(0<t<1\), the exact sharp exponential rate *and prefactor* are
\[
\boxed{\|P_m(t)\|=\frac{1+t}{2\sqrt{\pi t(1-t^2)}}m^{-1/2}
\left(\frac{1+t}{1-t}\right)^m\left(1+O_t(m^{-1})\right).}
\]
The vanishing-parameter transition is universal: if \(0\le t_m<1\) and \(m t_m\to\tau\in[0,\infty)\), then
\[
\boxed{\lim_{m\to\infty}\|P_m(t_m)\|=I_0(2\tau)
=\sum_{k=0}^{\infty}\frac{\tau^{2k}}{(k!)^2}.}
\]
For fixed \(0<t<1\), the eigenvectors form a complete minimal system but **no ordering is a Schauder basis**, and the operator is not similar to any normal or scalar-type spectral operator. At \(t=0\), the spectral projections are orthogonal and have norm one. Thus arbitrarily weak, fixed nonzero subdiagonal coupling creates exponential spectral-projection instability even though the spectrum is always the same simple positive sequence converging to zero.

## Assumptions and scope
All statements concern the complex Hilbert space \(\ell^2(\mathbb N_0)\), with \(\mathbb N_0=\{0,1,2,\ldots\}\), and real \(0\le t<1\). Define
\[
(C_tx)_n=\frac{1}{n+1}\sum_{k=0}^{n}t^{n-k}x_k,\qquad n\ge0.
\]
Let \(S e_k=e_{k+1}\) and \(D e_n=(n+1)^{-1}e_n\). Then \(C_t=D(I-tS)^{-1}\), so \(C_t\) is compact (indeed Hilbert–Schmidt) for every \(t<1\). Its isolated nonzero eigenvalues are \(\lambda_m=(m+1)^{-1}\), indexed by \(m\ge0\). The spectral projection \(P_m(t)\) means the resolvent contour projection associated with the single isolated point \(\lambda_m\). It is not an orthogonal projection unless \(t=0\).

The modified Bessel function is defined here without relying on special-function normalization conventions by \(I_0(z)=\sum_{k=0}^{\infty}(z/2)^{2k}/(k!)^2\). The fixed-parameter asymptotic is *not uniform* down to \(t=0\); the separate critical statement addresses the scale \(t\asymp m^{-1}\). No claim is made at \(t=1\), where compactness fails.

## Proof
**1. Eigenvectors and the Riesz projection.** For each \(m\ge0\), put
\[
v^{(m)}_n=\begin{cases}\binom{n}{m}t^{n-m},&n\ge m,\\0,&n<m,\end{cases}
\qquad
w^{(m)}_n=\begin{cases}\binom{m}{n}(-t)^{m-n},&0\le n\le m,\\0,&n>m.\end{cases}
\]
Both belong to \(\ell^2\). Substitution in the triangular matrix formula shows \(C_tv^{(m)}=\lambda_m v^{(m)}\) and \(C_t^*w^{(m)}=\lambda_mw^{(m)}\). The binomial identity
\[
\sum_{n=j}^{m}\binom{n}{j}\binom{m}{n}t^{n-j}(-t)^{m-n}=\delta_{mj},
\qquad 0\le j\le m,
\]
with the vanishing overlap for \(j>m\), yields \(\langle v^{(j)},w^{(m)}\rangle=\delta_{jm}\). In particular \(\langle v^{(m)},w^{(m)}\rangle=1\). Triangularity forces each nonzero eigenvalue and corresponding eigenspace to be indexed by the first nonzero coordinate of its eigenvector. The overlap also excludes generalized eigenvectors: a length-two Jordan chain would imply \((C_t-\lambda_m I)u=v^{(m)}\), contradicting \(\langle (C_t-\lambda_m I)u,w^{(m)}\rangle=0\). Compactness therefore makes \(\lambda_m\) algebraically simple, and
\[
P_m(t)x=\langle x,w^{(m)}\rangle v^{(m)},\qquad
\|P_m(t)\|=\|v^{(m)}\|_2\|w^{(m)}\|_2.
\]
The eigenvector formulas themselves are prior inputs; the quantitative norms and asymptotic conclusions below are the contribution.

**2. Exact norm.** Write
\[
W_m(t)=\|w^{(m)}\|_2^2
=\sum_{k=0}^{m}\binom{m}{k}^{2}t^{2k}
=\frac1{2\pi}\int_{0}^{2\pi}|1+te^{i\theta}|^{2m}\,d\theta.
\]
By the binomial generating series and Hardy-space Parseval,
\[
\|v^{(m)}\|_2^2
=\sum_{j=0}^{\infty}\binom{m+j}{m}^{2}t^{2j}
=\frac1{2\pi}\int_0^{2\pi}|1-te^{i\theta}|^{-2m-2}\,d\theta.
\]
For \(0\le t<1\), make the circle automorphism substitution \(z=(t+u)/(1+tu)\), with \(|z|=|u|=1\). Then
\[
|1-tz|=\frac{1-t^2}{|1+tu|},\qquad
|dz|=\frac{1-t^2}{|1+tu|^2}|du|.
\]
It follows exactly that \(\|v^{(m)}\|_2^2=(1-t^2)^{-2m-1}W_m(t)\), and hence \(\|P_m(t)\|=(1-t^2)^{-m-1/2}W_m(t)\). This also proves the hypergeometric identity
\[
\sum_{j=0}^{\infty}\binom{m+j}{m}^2z^j
=(1-z)^{-2m-1}\sum_{k=0}^m\binom{m}{k}^2z^k,
\quad 0\le z<1.
\]

**3. Fixed-coupling asymptotic.** For fixed \(0<t<1\), the positive function \(|1+te^{i\theta}|^2=(1+t)^2-2t(1-\cos\theta)\) has a unique maximum on the circle at \(\theta=0\). Its logarithm has the expansion
\[
\log|1+te^{i\theta}|^2
=2\log(1+t)-\frac{t}{(1+t)^2}\theta^2+O_t(\theta^4).
\]
Laplace's method, with an exponentially smaller complement outside a fixed neighborhood of the maximum, gives
\[
W_m(t)=\frac{(1+t)^{2m+1}}{2\sqrt{\pi m t}}
\bigl(1+O_t(m^{-1})\bigr).
\]
Substitution into the exact norm identity yields the stated sharp prefactor and the base \((1+t)/(1-t)>1\) of exponential growth.

**4. Critical boundary layer.** Assume \(m t_m\to\tau\in[0,\infty)\). For each fixed \(k\), \(\binom{m}{k}t_m^k\to\tau^k/k!\). Because \(\binom{m}{k}t_m^k\le (m t_m)^k/k!\) and the sequence \(m t_m\) is bounded, dominated convergence for series gives
\[
W_m(t_m)\longrightarrow\sum_{k=0}^\infty\frac{\tau^{2k}}{(k!)^2}=I_0(2\tau).
\]
Also \(m t_m^2\to0\), so \((1-t_m^2)^{-m-1/2}\to1\). The Bessel limit follows. When \(t=0\), only \(k=0\) contributes, yielding \(\|P_m(0)\|=1\).

**5. Spectral-structure consequences.** Minimality follows from the bounded biorthogonal vectors \(w^{(m)}\). To prove completeness, let \(y\perp v^{(m)}\) for every \(m\), and set \(F(z)=\sum_{n\ge0}\overline{y_n}z^n\), analytic on \(|z|<1\). Then \(F^{(m)}(t)/m!=\langle v^{(m)},y\rangle=0\) for every \(m\), hence \(F=0\) and \(y=0\). If the eigenvectors formed a Schauder basis in some order, the norms of their individual coordinate projections would be uniformly bounded, because each coordinate projection is the difference of two uniformly bounded partial-sum projections. Uniqueness of the biorthogonal system identifies those coordinate projections with \(P_m(t)\), contradicting their exponential growth for \(t>0\). Finally, a bounded similarity to a normal or scalar-type spectral operator would make all isolated spectral-projection norms uniformly bounded by a single similarity/spectral-measure constant; this is impossible.

## Verification
The included `checks/spectral_projection_check.py` uses only Python's standard library. It checks exact rational eigenvector equations, biorthogonality and coefficient identities, together with supplementary finite fixed-parameter and Bessel-limit diagnostics. Reproduce using `python3 checks/spectral_projection_check.py`, which prints `PASS: 2035 finite assertions`. These finite tests are **not** used as a proof of the infinite-dimensional or asymptotic assertions, which are established above by exact identities, complex-variable integration and Laplace/dominated-convergence arguments.

## Relationship to prior work
Rhaly (1984) introduced the generalized Cesàro matrices and established their early \(\ell^2\) operator-theoretic properties. Curbera–Ricker (first publicly posted 17 February 2023) identify the simple eigenvalues, compactness and the explicit right eigenvectors for generalized Cesàro operators on broad Banach lattices. Albanese–Bonet–Ricker (2023, open access) reproduce those right eigenvectors and give the corresponding finite-support dual eigenvectors (Section 6). These inputs are **not claimed as new**. The finding determines their rank-one spectral projection norms exactly, including the full exponential rate and sharp polynomial prefactor, an \(I_0\) crossover when the parameter scales as \(m^{-1}\), and the resulting failure of eigenvector Schauder-basis/spectral similarity despite completeness.

A relevant nearby result concerns sharp spectral-projection conditioning for atomic Bergman-kernel Cesàro dilations on Hardy space, a different family of operators; it does not imply the projection law for the discrete lower-triangular generalized Cesàro matrices. Earlier results proving non-normaloid or non-spectraloid properties for \(C_t\) likewise do not furnish the uniform Riesz-projection obstruction or the present quantitative law.

## Limitations
The asymptotic prefactor is pointwise in fixed \(t>0\), and the Bessel statement addresses bounded \(m t_m\); no uniform two-parameter expansion is claimed across all regimes. The operator at \(t=1\) is excluded. The right and left eigenvector formulas are existing literature, and all novelty claims are relative to the inspected accessible texts and available index records. An unindexed general theorem on spectral projections of triangular binomial transforms could yield equivalent results; no assertion of established worldwide priority is made. No independent mathematical audit has been performed.

## References
- H. C. Rhaly, *Generalized Cesàro Matrices*, Canadian Mathematical Bulletin 27 (1984), 417–422. https://doi.org/10.4153/CMB-1984-064-5
- G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices in* \(\mathbb C^{\mathbb N_0}\), arXiv:2302.08750 (initial submission 17 February 2023). https://arxiv.org/abs/2302.08750
- A. A. Albanese, J. Bonet and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales, Serie A. Matemáticas 117, 140 (2023). https://doi.org/10.1007/s13398-023-01470-2
