# The logarithmic Ornstein–Uhlenbeck window for a fixed-increment Friedman–Pólya urn

## Finding
Let \(a,b\) be positive integers satisfying \(a<3b\), and set \(s=a+b\), \(p_*=s/(4b)\), \(v_*=p_*(a-b)^2+(1-p_*)s^2\). Fix any real \(\theta\). For each integer \(N\ge3\) large enough that \(p_N=p_*+\theta/\log N\in(0,1)\), independently run a two-color urn from fixed positive integer counts \((Y_0^1,Y_0^2)\) for \(N\) steps. At every step, draw one ball uniformly and return it. Independently choose the Friedman replacement with probability \(p_N\), adding \(a\) balls of the drawn color and \(b\) of the opposite color, or choose the Pólya replacement with probability \(1-p_N\), adding \(s\) of the drawn color. Write \(D_{N,j}=Y^1_{N,j}-Y^2_{N,j}\), and put
\[
 X_N(t)=\frac{D_{N,\lfloor N^t\rfloor}}{\sqrt{\lfloor N^t\rfloor\log N}},\quad 0\le t\le1,\qquad \delta=\frac{2b\theta}{s}.
\]
Then, in the Skorokhod \(J_1\) topology on \(D([0,1])\),
\[
 X_N\Longrightarrow X,\qquad dX(t)=-\delta X(t)\,dt+\sqrt{v_*}\,dB(t),\quad X(0)=0.
\]
Equivalently, \(X(t)=\sqrt{v_*}\,e^{-\delta t}\int_0^t e^{\delta u}\,dB(u)\), a continuous centered Gaussian process with
\[
 \operatorname{Cov}(X(t),X(r))=v_*e^{-\delta(t+r)}\int_0^{\min(t,r)}e^{2\delta u}\,du.
\]
In particular, for the first-color proportion \(Z_{N,N}=Y^1_{N,N}/(Y^1_{N,N}+Y^2_{N,N})\),
\[
 \sqrt{\frac{N}{\log N}}\left(Z_{N,N}-\frac12\right)\Longrightarrow
 \mathcal N\!\left(0,\frac{v_*}{4s^2}\int_0^1 e^{-2\delta(1-u)}\,du\right).
\]
The variance factor is \((1-e^{-2\delta})/(2\delta)\) for \(\delta\ne0\), with continuous value \(1\) at \(\delta=0\). For the natural balanced-addition case \(a=b=1\), the endpoint variance is \((1-e^{-2\theta})/(16\theta)\) for \(\theta\ne0\), and \(1/8\) at \(\theta=0\).

## Assumptions and scope
There are exactly two colors. Initial positive counts and \(a,b,\theta\) do not vary with \(N\). Each replacement mode is chosen independently of the past and the draw. Crucially, both modes add the same total \(s=a+b\) at each step. The probability \(p_N\) is constant *within* the length-\(N\) experiment and differs between experiments; it is not an adaptive or time-inhomogeneous probability within a row. The condition \(a<3b\) guarantees \(0<p_*<1\). No coupling between experiments at distinct \(N\) is required.

## Proof
Write \(T_j=Y^1_{N,j}+Y^2_{N,j}=T_0+sj\), \(\tau=T_0/s>0\), and \(D_j=D_{N,j}\), suppressing the fixed row \(N\). Let \(\eta_{j+1}\in\{-1,1\}\) be \(+1\) when color one is drawn. Given the past, \(\mathbb E(\eta_{j+1}\mid\mathcal F_j)=D_j/T_j\). Independently let \(K_{j+1}=a-b\) with probability \(p_N\) and \(K_{j+1}=s\) otherwise. Then
\[
 D_{j+1}=D_j+K_{j+1}\eta_{j+1},\quad
 \bar k_N=\mathbb E K_{j+1}=s-2bp_N=s\lambda_N,\quad
 \lambda_N=\frac12-\frac{\delta}{\log N}.
\]
Define \(\xi_{j+1}=K_{j+1}\eta_{j+1}-\bar k_N D_j/T_j\). The sequence of \(\xi\)'s is a bounded martingale-difference array with \(|\xi_{j+1}|\le2s\) and
\[
 \mathbb E(\xi_{j+1}^2\mid\mathcal F_j)=v_N-\bar k_N^2(D_j/T_j)^2,\qquad
 v_N=p_N(a-b)^2+(1-p_N)s^2\longrightarrow v_*.
\]
The exact linear recursion is
\[
 D_{j+1}=\left(1+\frac{\lambda_N}{j+\tau}\right)D_j+\xi_{j+1}.
\]
Introduce the deterministic multiplier
\[
 h_{j,N}=\prod_{\ell=0}^{j-1}\left(1+\frac{\lambda_N}{\ell+\tau}\right)
 =\frac{\Gamma(j+\tau+\lambda_N)\Gamma(\tau)}{\Gamma(j+\tau)\Gamma(\tau+\lambda_N)}.
\]
The exact solution is \(D_j=h_{j,N}(D_0+\sum_{i=1}^j\xi_i/h_{i,N})\). Gamma-ratio bounds, uniformly for \(\lambda_N\) in a compact neighborhood of \(1/2\), give
\[
 h_{j,N}=g_Nj^{\lambda_N}(1+O(j^{-1})),\qquad
 g_N=\Gamma(\tau)/\Gamma(\tau+\lambda_N),
\]
with constants depending only on the fixed initial counts and the parameter bounds.

For completeness, the exact conditional second-moment recursion is
\[
 \mathbb E D_{j+1}^2=\left(1+\frac{2\lambda_N}{j+\tau}\right)\mathbb E D_j^2+v_N.
\]
For all sufficiently large \(N\) and \(0\le j\le N\), comparison with the corresponding gamma products yields
\[
 \mathbb E D_j^2\le C(j+1)(1+\log(j+1)),
\]
where \(C\) is independent of \(N,j\). Indeed, \(2\lambda_N=1-2\delta/\log N\), and the integrating-factor sum is bounded by a constant times \(\sum_{i\le j}i^{-1+2\delta/\log N}\le C(1+\log(j+1))\), since \(j\le N\). Consequently \(\mathbb E(D_j/T_j)^2\le C(1+\log(j+1))/(j+1)\).

Consider the logarithmic-clock martingale
\[
 W_N(t)=\frac1{\sqrt{\log N}}\sum_{i=1}^{\lfloor N^t\rfloor}i^{-\lambda_N}\xi_i.
\]
The jump magnitudes are uniformly \(O((\log N)^{-1/2})\). Its predictable quadratic variation is, uniformly over \(t\in[0,1]\),
\[
 \langle W_N\rangle(t)=\frac1{\log N}\sum_{i\le\lfloor N^t\rfloor}
 i^{-1+2\delta/\log N}\left[v_N-\bar k_N^2\left(\frac{D_{i-1}}{T_{i-1}}\right)^2\right]
 \xrightarrow{\mathbb P}v_*\int_0^t e^{2\delta u}\,du.
\]
To verify uniformity, the deterministic weighted harmonic sum is a uniform Riemann approximation under \(u=\log i/\log N\), while the expected absolute supremum of the nonnegative error from the squared proportion is bounded by
\[
 \frac C{\log N}\sum_{i=1}^N i^{-1+2\delta/\log N}\frac{1+\log i}{i}=O((\log N)^{-1}).
\]
The martingale functional central limit theorem (bounded jumps plus predictable quadratic variation) therefore yields \(W_N\Rightarrow\sqrt{v_*}\int_0^{\cdot}e^{\delta u}\,dB(u)\).

Finally, the uniform gamma-ratio bounds and Doob's \(L^2\) inequality show
\[
 \sup_{0\le t\le1}\left|\frac{D_{\lfloor N^t\rfloor}}{\sqrt{\lfloor N^t\rfloor\log N}}-e^{-\delta t}W_N(t)\right|\xrightarrow{\mathbb P}0.
\]
Here the fixed initial term is \(O((\log N)^{-1/2})\); replacing \(h_{i,N}^{-1}\) by \(g_N^{-1}i^{-\lambda_N}\) introduces square-summable errors of order \(i^{-\lambda_N-1}\), and the relative error in \(h_{j,N}\) is \(O(j^{-1})\). Split at a fixed index \(J\), apply Doob to the large-index martingale, then take \(J\to\infty\); small indices vanish after division by \(\sqrt{\log N}\). Also \(\lfloor N^t\rfloor^{-\delta/\log N}\) differs uniformly from \(e^{-\delta t}\) by \(o(1)\). Continuous mapping proves the asserted Ornstein–Uhlenbeck limit. The formula for proportions follows from \(T_N=T_0+sN\) and Slutsky's theorem.

## Verification
A standalone standard-library Python checker in `check.py` enumerates exact rational finite-state distributions, independently checks exact first- and second-moment recursions, checks the conditional innovation variance, and compares critical-window second moments against the predicted asymptotic values. Executing it against the packaged contents produced `PASS 206 exact/algebraic/asymptotic checks`. These checks test premises and arithmetic; the infinite-dimensional weak convergence rests on the displayed martingale argument, not on numerical extrapolation.

## Relationship to prior work
Shi–Yin–Miao (2026), Theorem 3.3, treats *fixed* replacement probability with \(2\Gamma-1>0\), where \(\Gamma=2bp/[p(a+b)+(1-p)c]\); at fixed equal increment \(c=s\), this is the strictly diffusive side. At the moving scale \(p_N=p_*+\theta/\log N\), that fixed-parameter Gaussian variance denominator approaches zero, so its theorem does not allow passing to the limit by substitution. Alves–Rosales (2025) proves almost-sure convergence of the mixture's color proportion for fixed positive \(p\), without the logarithmic path-level fluctuations. Classical generalized-urn martingale limit theory (Laulin 2020; Gouet 1993; Janson 2004) provides fixed-matrix critical invariance principles, including the zero-drift case. The present result instead identifies the explicit, nonzero-drift interpolation when the replacement probabilities vary *between* growing-horizon experiments. Bai and Hu (1999), and Bai, Hu and Zhang (2002), address nonhomogeneous random urn matrices and Gaussian approximations more generally. The accessible abstracts do not state a triangular family that keeps a near-critical replacement rule fixed for a horizon of length \(N\), or its explicit logarithmic-clock Ornstein–Uhlenbeck limit; the uninspected full texts are a remaining priority risk. It does not assert that its martingale tools are new.

## Limitations
Only deterministic equal total increments \(c=a+b\) are treated; randomly varying totals require a separate argument. Parameters \(a,b,\theta\) and the initial urn are fixed, and \(p_N\) is constant within each row. No Berry–Esseen estimate or density convergence is asserted. Existing general triangular-array martingale theory supplies the convergence mechanism; the claimed contribution is its precise fixed-increment mixed-urn critical-window identification and explicit covariance law. Historical priority beyond the inspected sources is not certified.

## References
1. Jianan Shi, Qing Yin, Yu Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669v1 (first public 2026-05-26), https://arxiv.org/html/2605.26669v1 .
2. Raphael Alves and Rafael A. Rosales, *Friedman vs Pólya*, arXiv:2502.16768v1 (first public 2025-02-24), https://arxiv.org/abs/2502.16768 .
3. Lucile Laulin, *A martingale approach for Pólya urn processes*, arXiv:2003.04592v1 (first public 2020-03-10), https://arxiv.org/html/2003.04592v1 .
4. Raúl Gouet, *Martingale functional central limit theorems for a generalized Pólya urn*, Annals of Probability 21 (1993), 1624–1639.
5. Svante Janson, *Functional limit theorems for multitype branching processes and generalized Pólya urns*, Stochastic Processes and their Applications 110 (2004), 177–245.
6. Z. D. Bai and Feifang Hu, *Asymptotic theorems for urn models with nonhomogeneous generating matrices*, Stochastic Processes and their Applications 80 (1999), 87–101, https://doi.org/10.1016/S0304-4149(98)00094-5 .
7. Z. D. Bai, Feifang Hu, and Li-Xin Zhang, *Gaussian approximation theorems for urn models and their applications*, Annals of Applied Probability 12 (2002), 1149–1173, https://doi.org/10.1214/aoap/1037125857 .
