# Exact logarithmic return-frequency constants for polynomially rescaled backward shifts on \(\ell^p\)

## Finding
For \(1\le p<\infty\), \(\alpha>0\), and \(0<\varepsilon<1\), put \(X=\ell^p(\mathbb N_0)\), \(B(x_0,x_1,\ldots)=(x_1,x_2,\ldots)\), and
\[R_\varepsilon(x)=\{n\in\mathbb N:\|n^\alpha B^nx-e_0\|_p<\varepsilon\}.\]
Define \(D_{p,\alpha}(\varepsilon)=\sup_{x\in X}\limsup_{N\to\infty}\#(R_\varepsilon(x)\cap\{1,\ldots,N\})/\log N\). Then
\[
D_{p,\alpha}(\varepsilon)=
\begin{cases}
\displaystyle\frac{\alpha}{\log(1+\varepsilon^{-1})},&p=1,\\[5pt]
\displaystyle\frac{\alpha p}{\log\!\left(1+\left(\varepsilon^{-p/(p-1)}-1\right)^{p-1}\right)},&1<p<\infty.
\end{cases}
\]
In every case there is an explicitly described vector for which the quotient converges to this value (so no limiting upper-frequency-only qualification is needed). When \(p=2\), the result simplifies to \(D_{2,\alpha}(\varepsilon)=\alpha/\log(1/\varepsilon)\). The theorem concerns returns to a fixed open ball around \(e_0\); it does not assert frequent hypercyclicity, or require that the extremal vector itself have a dense weighted orbit.

## Assumptions and scope
All scalars may be real or complex; \(n\) ranges over positive integers. The exponent \(p\) is finite and at least one, the orbit-growth power is positive, and the ball radius is strictly between zero and one. Logarithms are natural. The measured orbit is the non-autonomous sequence \(n^\alpha B^nx\), not powers of a single weighted operator. A return means a strict \(\ell^p\)-norm inequality.

## Proof
**1. Sharp one-step mass-loss factor.** Define
\[\rho_p(\varepsilon)=\begin{cases}
\displaystyle\frac{\varepsilon}{1+\varepsilon},&p=1,\\[4pt]
\displaystyle\frac{\delta^{p-1}}{\delta^{p-1}+(1-\delta)^{p-1}},\quad \delta=\varepsilon^{p/(p-1)},&1<p<\infty.
\end{cases}\]
For nonnegative \(u,t\) with \(|u-1|^p+t<\varepsilon^p\), the sharp geometric estimate is \(t/(u^p+t)\le\rho_p(\varepsilon)\). Indeed, at fixed \(u\) the fraction increases in \(t\), so set \(t=\varepsilon^p-|1-u|^p\). For \(u>1\), increasing \(u\) decreases the fraction. For \(1-\varepsilon<u<1\), maximize \((\varepsilon^p-(1-u)^p)/u^p\). Its derivative vanishes exactly at \(1-u=\varepsilon^{p/(p-1)}\) when \(p>1\); the endpoints contribute zero or a smaller value. When \(p=1\), the fraction increases up to \(u=1\) and decreases afterward. Substitution gives \(\rho_p\) above. For a complex first coordinate replace it by its modulus using \(\big||a|-1\big|\le|a-1|\).

**2. Uniform return packing.** Take any \(k\ge1\) return times \(1\le n_1<\cdots<n_k\le N\). Define \(S_i=\sum_{j=i}^k|x_{n_j}|^p\). The defining return inequality and the first-coordinate/tail decomposition give
\[|n_i^\alpha x_{n_i}-1|^p+n_i^{\alpha p}S_{i+1}<\varepsilon^p,\qquad 1\le i<k.\]
Applying Step 1 with \(u=n_i^\alpha|x_{n_i}|\) and \(t=n_i^{\alpha p}S_{i+1}\) proves \(S_{i+1}\le\rho_p S_i\). The first and last return inequalities imply
\[S_1<\frac{(1+\varepsilon)^p}{n_1^{\alpha p}},\qquad S_k>\frac{(1-\varepsilon)^p}{n_k^{\alpha p}}.\]
Combining these inequalities yields the finite bound
\[k<1+\frac{\alpha p\log N+p\log((1+\varepsilon)/(1-\varepsilon))}{\log(1/\rho_p(\varepsilon))}\]
(up to replacing strict by non-strict when necessary). Consequently \(D_{p,\alpha}(\varepsilon)\le\alpha p/\log(1/\rho_p)\).

**3. A sharp sparse witness.** Put
\[Q=\rho_p(\varepsilon)^{-1/(\alpha p)}>1,\quad m_j=\lceil Q^j(j+1)^2\rceil,\quad j\ge1.\]
For \(p=1\) set \(c=1\); for \(p>1\), set \(c=1-\varepsilon^{p/(p-1)}\). Define the vector \(x\) by \(x_{m_j}=c/m_j^\alpha\) and zero at all other coordinates. The indices \(m_j\) are strictly increasing and \(x\in\ell^p\), since \(m_j\ge Q^j\). For all integers \(h,j\ge1\),
\[m_{j+h}>Q^hm_j.\]
Indeed, \(m_{j+h}\ge Q^{j+h}(j+h+1)^2\) and \(m_j<Q^j(j+1)^2+1\), while \(Q^j((j+h+1)^2-(j+1)^2)>1\). Therefore
\[\begin{aligned}
\|m_j^\alpha B^{m_j}x-e_0\|_p^p
&=|1-c|^p+c^p\sum_{h\ge1}(m_j/m_{j+h})^{\alpha p}\\
&<|1-c|^p+\frac{c^p}{Q^{\alpha p}-1}=\varepsilon^p.
\end{aligned}\]
The equality on the right follows directly from the definitions: for \(p>1\), if \(\delta=\varepsilon^{p/(p-1)}\), then \(Q^{\alpha p}-1=((1-\delta)/\delta)^{p-1}\), so \(\delta^p+(1-\delta)\delta^{p-1}=\varepsilon^p\). For \(p=1\), \(Q^{\alpha}-1=\varepsilon^{-1}\). Thus every \(m_j\) belongs to \(R_\varepsilon(x)\). Finally \(\log m_j=j\log Q+2\log(j+1)+o(1)\), so \(\#\{j:m_j\le N\}\sim\log N/\log Q\). The uniform upper bound forces the full return count of this witness to have the same logarithmic asymptotic, proving equality.

## Verification
The standalone `checker.py` evaluates the one-step optimization and sharp-witness identity over a grid of \(p\) and \(\varepsilon\) values, and checks strict convergence for truncations of the sparse geometric witness. It passed 42,168 finite assertions. These computations are supplementary; Steps 1–3 constitute the proof for all real parameters in the stated ranges.

## Relationship to prior work
Li, Ruan and Yang (2026) analyze weighted hypercyclicity and the scalar weights for which it implies ordinary hypercyclicity. Their relevant construction uses disjoint coordinate blocks on a product Fréchet space; it does not calculate this fixed-ball return-frequency supremum in \(\ell^p\). Alshammari (2026) investigates uniformly approximate-periodic orbit translations and return-window profiles for weighted shifts, rather than visits of \(n^\alpha B^nx\) to a fixed target. Ernst and Mouze (2017) study weighted frequencies associated with the frequent-hypercyclicity criterion; the inspected abstract does not assert this parameter-specific optimum. Earlier estimates for this polynomially rescaled shift gave a general logarithmic upper bound and a lower coefficient \(\alpha p/\log(1+\varepsilon^{-p})\) but did not determine this exact constant for \(1<p<\infty\). The new mass-loss maximization closes that quantitative gap.

## Limitations
The result treats one fixed target \(e_0\) and an open ball of radius below one, on finite-exponent \(\ell^p\) spaces. It does not classify every maximizing vector, generalize to arbitrary targets, or claim the explicit witness has a dense weighted orbit. Numerical checks cannot certify the infinite-dimensional theorem on their own. An equivalent older formulation of the sharp return-packing coefficient is not conclusively excluded by the accessible literature.

## References
- Jian Li, Yonghang Ruan, Yini Yang, *Weighted orbits of hypercyclic vectors on F-spaces* (first posted 2026-11-03), arXiv:2611.04629v1, https://arxiv.org/html/2611.04629v1.
- Hadi Obaid Alshammari, *Return-Time Profiles and Quantitative Recurrence for Uniformly δ-Almost Periodic Vectors*, *Mathematics* 14 (2026), 1986, https://doi.org/10.3390/math14111986.
- Romuald Ernst and Augustin Mouze, *A quantitative interpretation of the frequent hypercyclicity criterion*, *Ergodic Theory and Dynamical Systems* (online 2017), https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/quantitative-interpretation-of-the-frequent-hypercyclicity-criterion/CD71C15170150A9484404EA6F3267159 (publisher abstract consulted).
