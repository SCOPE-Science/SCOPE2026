# Sharp mixed time–Fourier sampling with two spatial observations

## Finding

Let \(n\ge4\), and let \(F\) be the unitary discrete Fourier transform on \(\mathbb C^{\mathbb Z_n}\), with \(F_{k,t}=n^{-1/2}e^{-2\pi i kt/n}\). Select **two** distinct time indices \(T=\{t_0,t_1\}\subset\mathbb Z_n\) and **two** distinct unobserved Fourier indices \(B=\{k_0,k_1\}\subset\mathbb Z_n\). The critically sampled measurement map is
\[
\mathcal M_{T,B}f=\big((f(t))_{t\in T},\,((Ff)(k))_{k\in\mathbb Z_n\setminus B}\big)\in\mathbb C^n.
\]
Write \(a=t_1-t_0\), \(b=k_1-k_0\), interpreted modulo \(n\), and
\[
 c=\left|\cos\left(\frac{\pi ab}{n}\right)\right|,\quad
 u_\pm=\frac{2}{n}(1\pm c).
\]
The **entire eigenvalue multiset** of the measurement frame operator \(S=\mathcal M_{T,B}^*\mathcal M_{T,B}\) is
\[
\{1-\sqrt{1-u_-},\,1+\sqrt{1-u_-},\,1-\sqrt{1-u_+},\,1+\sqrt{1-u_+}\}\ \cup\ \{1\}^{n-4}.
\]
In particular, the sharp squared stability bounds are
\[
 A(T,B)=1-\sqrt{1-\tfrac2n(1-c)},\qquad
 B(T,B)=1+\sqrt{1-\tfrac2n(1-c)}=2-A(T,B).
\]
The measurements recover every signal if and only if \(ab\not\equiv0\pmod n\).

Among **all** unordered pairs \(T,B\), the maximum possible lower frame bound is
\[
 A_n^\star=1-\sqrt{1-\frac{2}{n}(1-\eta_n)},\qquad
 \eta_n=\begin{cases}0,&n\text{ even},\\\sin(\pi/(2n)),&n\text{ odd} .\end{cases}
\]
This optimum is attained **exactly** by pairs satisfying
\[
 ab\equiv\begin{cases}n/2\pmod n,& n\text{ even},\\
 (n-1)/2\text{ or }(n+1)/2\pmod n,& n\text{ odd}.
 \end{cases}
\]
For every invertible measurement matrix its ordinary spectral condition number is \(\kappa=\sqrt{B(T,B)/A(T,B)}\); thus these and only these configurations minimize the condition number.

Let \(\varphi\) denote Euler's totient function. The exact number of optimal **unordered** configurations \((T,B)\) is
\[
 \mathcal N_n^\star=
 \begin{cases}
 \dfrac{n^2\varphi(n)}2,&n\text{ odd},\\[4pt]
 \dfrac{n^2}{4}\displaystyle\sum_{d\mid n/2}d\varphi(n/d),&n\text{ even}.
 \end{cases}
\]
The exact number of singular configurations is
\[
 \mathcal N_n^{\mathrm{sing}}=\frac{n^2}{4}\sum_{\substack{d\mid n\\d<n}}\varphi(n/d)(d-1).
\]
Thus all configurations are invertible for prime \(n\); a singular configuration exists for every composite \(n\ge4\). As \(n\to\infty\), the optimal lower frame bound satisfies
\[
 A_n^\star=\begin{cases}
 n^{-1}+(2n^2)^{-1}+O(n^{-3}),&n\text{ even},\\
 n^{-1}+(1-\pi)/(2n^2)+O(n^{-3}),&n\text{ odd}.
 \end{cases}
\]

## Assumptions and scope

There are no support, positivity, or sparsity assumptions on \(f\). Both spatial observations and retained Fourier coefficients are complex-valued, exact, and equally weighted, with the unitary transform normalization above. The choice of the two missing frequencies is free, as is the choice of the two spatial indices. The measurement count equals the dimension. The stability bounds refer to squared Euclidean norms and hence to \(\|\mathcal M_{T,B}f\|_2^2\) for \(\|f\|_2=1\); condition number refers to singular values of \(\mathcal M_{T,B}\).

## Proof

**1. Complementary projections.** Let \(P_T\) be coordinate projection onto the time sites, and let \(Q_B=F^*P_BF\) be the orthogonal projection onto the two unobserved Fourier characters. Orthogonality of the DFT rows gives
\[
 S=P_T+F^*(I-P_B)F=I+P_T-Q_B.
\]
The subspaces \(\mathcal R(P_T)\) and \(\mathcal R(Q_B)\) have dimension two. By the two-subspace principal-angle decomposition, if \(\sigma_1,\sigma_2\in[0,1]\) are the singular values of the matrix of inner products between their orthonormal bases, then the spectrum of \(P_T-Q_B\) is \(\{\pm\sqrt{1-\sigma_1^2},\pm\sqrt{1-\sigma_2^2}\}\) with \(n-4\) additional zeros. The formula includes the endpoint cases \(\sigma_j=0,1\), counted with multiplicity. To verify directly, take a principal unit vector \(u\) from the first space and \(v\) from the second, with \(\langle u,v\rangle=\sigma\); on the span of \(u\) and \((v-\sigma u)/\sqrt{1-\sigma^2}\), the difference of projections has trace zero and determinant \(-(1-\sigma^2)\). The limiting endpoint cases follow by continuity, or directly from the common/orthogonal components.

**2. Exact principal angles.** The \(2\)-by-\(2\) inner-product matrix is the restriction of \(F^*\), up to transposition and conjugation, to rows \(T\) and columns \(B\). Its two squared singular values are exactly
\[
 \sigma_{1,2}^2=\frac2n\left(1\pm\left|\cos\left(\frac{\pi ab}{n}\right)\right|\right)=u_\pm.
\]
Indeed its Gram matrix has diagonal entries \(2/n\) and off-diagonal modulus \(2|\cos(\pi ab/n)|/n\). Inserting these values into Step 1 proves the full spectral formula. Since \(u_-\le u_+\), the extremal bounds are the pair determined by \(u_-\). They are both strictly positive precisely when \(c<1\), equivalently \(ab\not\equiv0\pmod n\). The apparent choice of signs of \(a,b\) does not affect \(c\).

**3. Global optimization.** The function \(1-\sqrt{1-2(1-c)/n}\) is strictly decreasing in \(c\in[0,1]\). Since \(ab\bmod n\) is an integer residue, its cosine modulus is minimized at residue \(n/2\) if \(n\) is even, or residues \((n\pm1)/2\) if \(n\) is odd, with respective minimum \(0\) or \(\sin(\pi/(2n))\). These residues are attainable by taking \(a=1\), and choosing \(b\) accordingly. They characterize every optimizer, and optimizing \(A\) also minimizes \(\kappa\) because \(B=2-A\).

**4. Counting all optimal and singular placements.** Ordered indices \((t_0,t_1,k_0,k_1)\) with distinct entries within each pair correspond to a choice of \(t_0,k_0\) (\(n^2\) choices) and of nonzero residues \(a,b\). Each unordered pair of two-element sets has exactly four such orderings. For odd \(n\), each target residue \((n\pm1)/2\) is coprime to \(n\); exactly \(\varphi(n)\) choices of \(a\) are units and each has a unique matching \(b\) per target. For even \(n\), a congruence \(ab\equiv n/2\pmod n\) has exactly \(d=\gcd(a,n)\) solutions for \(b\) when \(d\mid n/2\) and none otherwise. There are \(\varphi(n/d)\) residues \(a\) of a given gcd \(d\), yielding the stated optimizer count. Similarly, \(ab\equiv0\pmod n\) has exactly \(d-1\) **nonzero** solutions for \(b\) for each nonzero \(a\) of gcd \(d\). Summing over proper divisors \(d\mid n\) gives the singular count. A composite modulus admits \(1<a,b<n\) with \(ab=n\), while prime moduli admit no such pair.

**5. Dimension dependence.** Apply \(1-\sqrt{1-z}=z/2+z^2/8+O(z^3)\) to \(z=2(1-\eta_n)/n\), using \(\eta_n=0\) for even \(n\) and \(\eta_n=\pi/(2n)+O(n^{-3})\) for odd \(n\). This gives the two stated expansions.

## Verification

Run `python -m pip install -r requirements.txt` and then `python CHECK.py` in the directory containing the supplied files. The checker independently forms the full mixed-sampling matrix, diagonalizes its frame operator for many placements, exhaustively counts optimizers and singular configurations for \(4\le n\le19\), and verifies both the formulas and endpoint relations. The stored checker reports `CRITICAL_MIXED_FOURIER_SAMPLING_CHECKS_PASSED 129994`. These finite tests corroborate the algebra but do not establish the universal theorem; Steps 1–5 above give its infinite-parameter proof.

## Relationship to prior work

Kayaalp and Szehr (2026, arXiv:2603.16242, Sections III and V) analyze recovery from joint time and Fourier samples and give numerical conditioning comparisons, but do not derive the present all-modulus sharp placements, full eigenvalue multiset, and arithmetic counts. The classical Donoho–Stark uncertainty principle and Chebotarev/full-spark criteria concern support, uniqueness, and concentration rather than this exact critically sampled spectral optimization. Results on contiguous partial DFT submatrices likewise do not provide the optimal arbitrary two-site/two-frequency-complement classification. The exact two-subspace principal-angle identity is classical; the contribution here is the explicitly optimized cyclic Fourier instance and its complete arithmetic counting.

## Limitations

The theorem does not address nonuniform measurement weights, noisy or missing measurements beyond the specified two Fourier omissions, other transform matrices, or budgets differing from \(n\). It proves sharp worst-case linear stability, not nonlinear or sparse-recovery guarantees. The use of classical two-projection algebra should not be confused with independent priority certification; equivalent formulations in specialist filter-bank literature remain a literature risk.

## References

1. M. Kayaalp and O. Szehr, *Signal Recovery from Time and Frequency Samples*, arXiv:2603.16242 (first submitted 2026-03-17), especially Sections III and V. https://arxiv.org/abs/2603.16242
2. D. L. Donoho and P. B. Stark, *Uncertainty Principles and Signal Recovery*, SIAM J. Appl. Math. **49** (1989), 906–931, doi:10.1137/0149053. https://doi.org/10.1137/0149053
3. A. H. Barnett, *How Exponentially Ill-Conditioned Are Contiguous Submatrices of the Fourier Matrix?*, SIAM Review **64** (2022), 105–131, doi:10.1137/20M1336837. https://doi.org/10.1137/20M1336837
