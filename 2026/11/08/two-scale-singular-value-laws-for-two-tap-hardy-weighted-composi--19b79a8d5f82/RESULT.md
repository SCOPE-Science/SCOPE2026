# Two-scale singular-value laws for two-tap Hardy weighted compositions

## Finding
Let \(H^2(\mathbb D)\) be the complex Hardy space with orthonormal monomials \(e_j(z)=z^j\). Fix \(c\in\mathbb C\setminus\{0\}\), write \(a=|c|>0\), and define, for \(0<r<1\) and each integer \(m\ge1\),
\[
W_{r,m,c}f(z)=(1+c z^m)f(rz).
\]
For every integer \(k\ge1\) let \(\mathcal C_k\) comprise all cyclic integer height words \((h_0,\ldots,h_{k-1})\) satisfying \(h_i\ge0\), \(\min_i h_i=0\), and \(|h_i-h_{i+1}|\le1\) with cyclic indexing \(h_k=h_0\). Define the finite polynomial
\[
P_{k,a}(Q)=\sum_{h\in\mathcal C_k}
 (1+a^2)^{b(h)}a^{k-b(h)}Q^{\sum_i h_i},
\qquad b(h)=\#\{i:h_i=h_{i+1}\}.
\]
**Exact all-order moments.** The operator belongs to every Schatten class and, for every \(k\ge1\),
\[
\operatorname{Tr}|W_{r,m,c}|^{2k}
 =\frac{P_{k,a}(r^{2m})}{1-r^{2k}}.
\]
In particular,
\[
\operatorname{Tr}|W_{r,m,c}|^2=\frac{1+a^2}{1-r^2},\qquad
\operatorname{Tr}|W_{r,m,c}|^4=\frac{(1+a^2)^2+2a^2r^{2m}}{1-r^4}.
\]

**Complete concentration/bandwidth crossover.** Let \(r_j\uparrow1\) and let \(m_j\ge1\) be integers such that \(m_j(-\log r_j)\to\tau\in[0,\infty]\). With \(e^{-\infty}:=0\), for each \(k\ge1\),
\[
\lim_j(1-r_j)\operatorname{Tr}|W_{r_j,m_j,c}|^{2k}
 =\frac{P_{k,a}(e^{-2\tau})}{2k}.
\]
For every \(k\ge2\), this is continuous and strictly decreasing in \(\tau\), whereas the Hilbert--Schmidt coefficient \((1+a^2)/2\) is independent of \(\tau\). The endpoint polynomials satisfy
\[
P_{k,a}(0)=(1+a^2)^k,
\qquad P_{k,a}(1)=\sum_{b=0}^k\binom{k}{b}^{2}a^{2b}.
\]
Thus the fourth-power coefficient interpolates strictly between \(\big((1+a^2)^2+2a^2\big)/4\) and \((1+a^2)^2/4\).

**Counting distribution and norm.** Write \(s_n(T)\) for descending singular values with multiplicity, and \(N_T(u)=\#\{n:s_n(T)>u\}\) for \(u>0\). Let \(S\) be the unilateral shift on \(\ell^2(\mathbb N_0)\), \(D_qe_\ell=q^\ell e_\ell\), and \(A_{q,a}=(I+aS)D_q\) for \(0\le q<1\), with the boundary convention \(D_0e_0=e_0\), \(D_0e_\ell=0\) for \(\ell\ge1\). Then for every fixed \(u>0\),
\[
\lim_j(1-r_j)N_{W_{r_j,m_j,c}}(u)=F_{\tau,a}(u),
\]
where
\[
F_{\tau,a}(u)=
\begin{cases}
\displaystyle\frac1{2\pi}\int_0^{2\pi}\log^+\!\left(\frac{|1+a e^{i\theta}|}{u}\right)d\theta,&\tau=0,\\[5pt]
\displaystyle\int_0^\tau\#\{\ell\ge0:e^{-x}s_\ell(A_{e^{-\tau},a})>u\}\,dx,&0<\tau<\infty,\\[5pt]
\displaystyle\log^+\!\left(\frac{\sqrt{1+a^2}}{u}\right),&\tau=\infty.
\end{cases}
\]
Finally,
\[
\lim_j\|W_{r_j,m_j,c}\|=
\begin{cases}
1+a,&\tau=0,\\
\|A_{e^{-\tau},a}\|,&0<\tau<\infty,\\
\sqrt{1+a^2},&\tau=\infty.
\end{cases}
\]
For \(0<\tau<\infty\) the middle norm is continuous and strictly decreasing as a function of \(\tau\). These conclusions concern one coherent two-scale spectral law, not independent claims about arbitrary operator families.

## Assumptions and scope
All operators are on the standard complex Hilbert Hardy space with its coefficient norm, not a general weighted Dirichlet norm. Parameters are a **fixed nonzero** complex number \(c\), real numbers \(0<r<1\), and integer bandwidths \(m\ge1\). The double-scaling limit permits \(\tau=0\) with fixed or slowly growing bandwidth and \(\tau=\infty\) with bandwidth growing faster than the dilation scale. There is no dependence on the complex argument of \(c\), since it can be removed by diagonal unitary conjugacy. Counts use a strict threshold \(u>0\); no convergence uniform in \(u\) or spectral-gap rate is asserted.

## Proof
**1. Exact block decomposition.** The basis splits into orthogonal reducing subspaces \(E_b=\overline{\operatorname{span}}\{e_{b+\ell m}:\ell\ge0\}\), \(0\le b<m\), because
\[
W_{r,m,c}e_{b+\ell m}=r^{b+\ell m}(e_{b+\ell m}+c e_{b+(\ell+1)m}).
\]
Gauge away the phase of \(c\) on every chain. With \(q=r^m\), the result is the exact unitary equivalence
\[
W_{r,m,c}\simeq\bigoplus_{b=0}^{m-1}r^b A_{q,a}.
\]
Since \(q<1\), \(A_{q,a}\) is trace class. Therefore \(W_{r,m,c}\) belongs to every \(\mathcal S_p\), \(p>0\), and
\[
\operatorname{Tr}|W_{r,m,c}|^p=
\frac{1-r^{pm}}{1-r^p}\operatorname{Tr}|A_{q,a}|^p.
\]
In particular, \(\|W_{r,m,c}\|=\|A_{q,a}\|\) exactly.

**2. Cyclic-walk trace formula.** The Gram operator \(G_q=A_{q,a}^*A_{q,a}\) is the positive compact Jacobi matrix with diagonal \((1+a^2)q^{2\ell}\) and adjacent entries \(a q^{2\ell+1}\). Expand \(\operatorname{Tr}(G_q^k)\) as a sum over closed nearest-neighbor walks of \(k\) steps, allowing stays. A stay at height \(h\) contributes \((1+a^2)q^{2h}\); an adjacent step from \(h\) to \(h'\) contributes \(a q^{h+h'}\). Hence a closed walk contributes \((1+a^2)^{b(h)}a^{k-b(h)}q^{2\sum h_i}\). Each closed walk uniquely equals a cyclic height word of minimum zero shifted by some nonnegative integer \(v\). Summing the shift gives \(\sum_{v\ge0}q^{2kv}=1/(1-q^{2k})\), so
\[
\operatorname{Tr}(G_q^k)=\frac{P_{k,a}(q^2)}{1-q^{2k}}.
\]
The block geometric sum cancels its denominator, proving the exact moment identity. The polynomial is finite since a length-\(k\) closed nearest-neighbor walk with minimum zero has bounded maximum height. Its constant term is the all-zero word; positive higher coefficients exist for every \(k\ge2\), from a word having precisely one height-one entry. The identity at \(Q=1\) follows either by translating the interior trace density to the Laurent symbol \(1+a^2+a(z+z^{-1})=|1+az|^2\), or by expanding its \(k\)-th power. This yields \(\sum_b\binom{k}{b}^2a^{2b}\).

**3. Spectral-measure limit, including the endpoints.** For each \((r,m)\) define the finite positive measure
\[
\nu_{r,m}=(1-r)\sum_n s_n(W_{r,m,c})^2\delta_{s_n(W_{r,m,c})}
\quad\text{on }[0,1+a].
\]
Its total mass is bounded, and the already proved moment formula gives
\[
\lim_j\int s^{2k}d\nu_{r_j,m_j}(s)=
\frac{P_{k+1,a}(e^{-2\tau})}{2k+2}\qquad(k\ge0).
\]
Polynomials in \(s^2\) are dense in continuous functions on \([0,1+a]\), so these limits determine weak convergence of the finite measures. For \(0<\tau<\infty\), with \(q=e^{-\tau}\), its limit is explicitly
\[
\nu_{\tau,a}=\int_0^\tau\sum_{\ell\ge0}
 e^{-2x}s_\ell(A_{q,a})^2\,
 \delta_{e^{-x}s_\ell(A_{q,a})}\,dx.
\]
For \(\tau=0\) and \(\infty\), respectively, the limit measures are
\[
\nu_{0,a}=\int_0^\infty\int_0^{2\pi}
 e^{-2x}|1+a e^{i\theta}|^2\delta_{e^{-x}|1+a e^{i\theta}|}
 \frac{d\theta}{2\pi}\,dx,
\]
\[
\nu_{\infty,a}=\int_0^\infty
 (1+a^2)e^{-2x}\delta_{e^{-x}\sqrt{1+a^2}}\,dx.
\]
For \(0<\tau<\infty\), the first representation has the required moments by the block trace formula. The two endpoint representations have moments \(P_{k+1,a}(1)/(2k+2)\) and \(P_{k+1,a}(0)/(2k+2)\), respectively. All three measures have no atoms at positive singular values, because their nonzero locations are strictly monotone in the continuously integrated variable \(x\). At every \(u>0\), the bounded threshold test \(s\mapsto\mathbf 1_{\{s>u\}}/s^2\) is therefore continuous almost everywhere with respect to the limit measure. Weak convergence gives the stated counting law after evaluating its three integrals.

**4. Edge norm and strictness.** In the exact direct sum the largest scale factor is one, giving \(\|W\|=\|A_{q,a}\|\). When \(q\downarrow0\), the operators converge in norm to \((I+aS)P_{e_0}\), whose norm is \(\sqrt{1+a^2}\). When \(q\uparrow1\), the diagonal contractions \(D_q\) converge strongly to the identity, so \(\|A_{q,a}\|\to\|I+aS\|=1+a\), using the uniform upper bound and finite-vector norm approximation. For \(0<q_1<q_2<1\), all entries of \(G_{q_1}\) are bounded above by those of \(G_{q_2}\), and the inequality is strict off the initial diagonal. A top Rayleigh maximizer for the positive compact irreducible Jacobi matrix \(G_{q_1}\) can be chosen strictly positive: taking coordinatewise absolute values cannot decrease the Rayleigh quotient, and any zero coordinate contradicts the eigenvector recurrence and positive adjacent entries. Evaluating that vector on \(G_{q_2}\) yields a strictly larger Rayleigh quotient. Hence the norm is strictly increasing in \(q\), equivalently strictly decreasing in positive \(\tau\).

## Verification
The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It independently enumerates cyclic paths for six orders at three positive rational tap amplitudes, verifies the closed-form fourth- and sixth-power polynomials, verifies the boundary circle moments, and compares several direct finite Gram-matrix power traces against the *infinite* rational formula with an explicit positive error bound for omitted closed walks. Execution produced: `TWO_TAP_EXACT_CHECK_OK 129 rational assertions; infinite spectral limits require the written proof`. The code does not and cannot finitely certify weak convergence, the all-orders formula, or publication priority.

## Relationship to prior work
Sun and Liu, arXiv:2610.19658v1 (first publicly available October 14, 2026), analyze composition--differentiation operators and give exact singular values when the multiplicative weight is **one monomial** and the composition symbol is linear; see their Section 9.2 and Theorem 9.2. Here the minimal *two-monomial* weight creates a non-diagonal Gram operator. The claim is not inferred from singular values of the two monomial terms: singular values are not additive under operator sums. Earlier work of Putinar and Tener (arXiv:1612.03970) investigates singular-value bounds for weighted composition maps linked to univalent changes of domain, without the present two-scale spectral counting. Pushnitski (arXiv:1710.02652) proves fixed-band, power-decay singular asymptotics for compact matrices; the bandwidth here grows with the inverse dilation scale and entries decay geometrically, so his stated theorem does not directly imply this limit. Classical Toeplitz spectral-distribution results illuminate the \(\tau=0\) endpoint but do not by themselves identify the full interpolation, positive finite-\(\tau\) Jacobi law, or exact all-order polynomial profile. The known weighted-composition Schatten-membership criteria alone do not supply these sharp coefficients.

## Limitations
The coefficients \(P_{k,a}\) have exact finite walk formulas, but no simple closed form for the interior Jacobi singular values is claimed. The count limit is pointwise for each threshold \(u>0\), without a uniform error estimate. The result only treats two taps, a radial linear composition symbol and classical Hardy \(H^2\). The claimed literature originality is a best-knowledge mathematical comparison, not an independent priority determination; general results on nonstationary banded matrix families might require deeper comparison. A complete independent review has not been performed.

## References
- J. Sun and J. Liu, *Weighted composition--differentiation operators on mixed-norm, derivative Hardy and F(p,q,s) spaces*, arXiv:2610.19658v1, October 14, 2026. Full primary text, especially Section 9.2.
- M. Putinar and J. E. Tener, *Singular values of weighted composition operators and second quantization*, arXiv:1612.03970, December 12, 2016. Introduction and Theorem A.
- A. Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space*, arXiv:1710.02652, October 7, 2017. Theorem 1.2 and Section 1.3.
- E. A. Gallardo-Gutiérrez, R. Kumar, and J. R. Partington, *Boundedness, compactness and Schatten-class membership of weighted composition operators*, arXiv:0907.2370, July 14, 2009. Abstract and bibliographic information.
