# A logarithmic-to-zeta transition in consecutive-power norms of lazy weighted shifts

## Finding

Fix \(0<\delta<1\). On complex \(\ell^1(\mathbb N)\), with coordinates indexed from one, let \(\alpha\ge1\) and define
\[
W_\alpha e_1=0,\qquad
W_\alpha e_j=\left(\frac{j}{j-1}\right)^\alpha e_{j-1}\quad(j\ge2),
\qquad T_{\alpha,\delta}=(1-\delta)I+\delta W_\alpha.
\]
For \(\alpha=1\), the exact leading norm growth of the successive-power difference is **logarithmic**:
\[
\boxed{\lim_{n\to\infty}\frac{\|T_{1,\delta}^{n+1}-T_{1,\delta}^{n}\|}{\log n}
=\frac{\delta}{2(1-\delta)\sqrt{2\pi e}}.}
\]
For every fixed \(\alpha>1\), it is **polynomial, with the Riemann zeta constant**:
\[
\boxed{\lim_{n\to\infty}n^{1-\alpha}\|T_{\alpha,\delta}^{n+1}-T_{\alpha,\delta}^{n}\|
=\frac{\delta^\alpha\zeta(\alpha)}{(1-\delta)\sqrt{2\pi e}}.}
\]
Both constants are positive and sharp. If \(j_n\) is a maximizing input-coordinate index for the exact column-sum formula below and \(\sigma_n=\sqrt{n\delta(1-\delta)}\), then the sequence \((j_n-n\delta)/\sigma_n\) is bounded and all its accumulation points belong to \(\{-1,1\}\). The theorem does not assert eventual selection of one sign.

The boundary \(\alpha=1\) is the same critical exponent at which the fractional Gaussian integral governing the known subcritical \(0<\alpha<1\) results ceases to be locally integrable. The new formulas cover the boundary and all supercritical exponents, not the previously treated subcritical range.

## Assumptions and scope

All operator norms are the norms on the infinite-dimensional complex space \(\ell^1(\mathbb N)\). Both parameters are held fixed as integer \(n\to\infty\), and \(\zeta(\alpha)=\sum_{h\ge1}h^{-\alpha}\) for \(\alpha>1\). The weights are bounded for every fixed \(\alpha\), and the lazy average is a bounded, positive operator. The theorem concerns \(\alpha\ge1\) exclusively. It does not assert absolute Cesàro boundedness in that range.

For completeness, \(\|W_\alpha^m\|=(m+1)^\alpha\), and its spectrum is the closed unit disk; therefore \(\sigma(T_{\alpha,\delta})=(1-\delta)+\delta\overline{\mathbb D}\), with the sole unit-circle contact at \(1\). These spectral facts do not themselves imply the norm asymptotics.

## Proof

**1. An exact finite column norm.** Put \(b_{n,k}=\binom nk\delta^k(1-\delta)^{n-k}\) for \(0\le k\le n\) and put it equal to zero otherwise. Define \(d_{n,k}=|b_{n,k}-b_{n,k-1}|\), for \(0\le k\le n+1\). The telescoping weight product gives
\[
W_\alpha^k e_j=\left(\frac j{j-k}\right)^\alpha e_{j-k}
\quad(0\le k<j),\qquad W_\alpha^k e_j=0\quad(k\ge j).
\]
Since \(T^{n+1}-T^n=\delta T^n(W_\alpha-I)\), its coefficient at \(W_\alpha^k\) is \(\delta(b_{n,k-1}-b_{n,k})\). Distinct powers applied to one basis vector occupy distinct output coordinates; taking absolute column sums therefore yields the exact identity
\[
\|T^{n+1}-T^n\|=\delta\max_{1\le j\le n+2}
 j^\alpha\sum_{k=0}^{\min(n+1,j-1)}\frac{d_{n,k}}{(j-k)^\alpha}.
\tag{1}
\]
Indeed, every column \(j\ge n+2\) includes all nonzero coefficients, while its factors \(j/(j-k)\) decrease with \(j\). Thus no omitted, later column can improve the maximum.

**2. First-difference local limit and global envelope.** Set \(\mu_n=n\delta\), \(\sigma_n=\sqrt{n\delta(1-\delta)}\), and \(u_{n,k}=(k-\mu_n)/\sigma_n\). Write \(\varphi(u)=e^{-u^2/2}/\sqrt{2\pi}\), \(g(u)=|u|\varphi(u)\), and \(a_{n,k}=\sigma_n^2d_{n,k}\). The exact ratio
\[
\frac{b_{n,k-1}}{b_{n,k}}=\frac{k(1-\delta)}{(n-k+1)\delta}\qquad(1\le k\le n)
\]
and uniform Stirling expansion imply, for each fixed \(L<\infty\),
\[
\sup_{|u_{n,k}|\le L}|a_{n,k}-g(u_{n,k})|\longrightarrow0.
\tag{2}
\]
Here and below the endpoint values use the zero-extension convention. In addition, standard binomial Gaussian estimates and the ratio identity give constants \(C,c>0\), depending on \(\delta\) but not on \(n,k\), such that
\[
0\le a_{n,k}\le C(1+|u_{n,k}|)^2e^{-cu_{n,k}^2}
\quad(0\le k\le n+1),\qquad
\sum_kd_{n,k}=2\max_k b_{n,k}\le C/\sigma_n.
\tag{3}
\]
For clarity, to obtain the first bound, split at \(|k-\mu_n|\le\eta n\) with fixed small \(\eta>0\). There \(b_{n,k}\le C\sigma_n^{-1}e^{-cu_{n,k}^2}\) and the ratio identity bounds the relative first difference by \(C(1+|u_{n,k}|)/\sigma_n\). Outside that strip, binomial Chernoff tails are exponentially small in \(n\), absorbing the polynomial factors in the desired Gaussian envelope after reducing \(c\). The second identity follows from unimodality (including the two endpoint differences). In particular, \(\sup_k a_{n,k}\le C\), and the envelope tends to zero when \(|u_{n,k}|\to\infty\).

**3. Columns on the central Gaussian scale, for \(\alpha>1\).** Reindex the sum in (1) by \(h=j-k\) and extend \(a_{n,k}=0\) outside the binomial range. For any sequence with
\[
\frac{j_n-\mu_n}{\sigma_n}\longrightarrow s\in\mathbb R,
\]
we have, by (2) and dominated convergence for the summable series \(\sum_{h\ge1}h^{-\alpha}\),
\[
\sum_{h\ge1}\frac{a_{n,j_n-h}}{h^\alpha}
\longrightarrow \zeta(\alpha)g(s).
\]
Furthermore, \(j_n^\alpha/(\sigma_n^2 n^{\alpha-1})\to \delta^{\alpha-1}/(1-\delta)\), so the column in (1), divided by \(n^{\alpha-1}\), tends to
\[
\frac{\delta^\alpha\zeta(\alpha)}{1-\delta}g(s).
\tag{4}
\]
If instead \(|(j_n-\mu_n)/\sigma_n|\to\infty\) while \(j_n\in[\mu_n/2,2\mu_n]\), split the series at fixed \(H\). Its terms with \(h\le H\) tend to zero by (3), and the remaining sum is at most \(C\sum_{h>H}h^{-\alpha}\). Sending \(H\to\infty\) proves that such columns vanish after the same normalization.

**4. Columns on the central Gaussian scale, for \(\alpha=1\).** If \((j_n-\mu_n)/\sigma_n\to s\), the relevant sum is
\[
\frac{\delta j_n}{\sigma_n^2\log n}
\sum_{h\ge1}\frac{a_{n,j_n-h}}h.
\]
Fix \(\eta\in(0,1)\) and split at \(h=\lfloor\eta\sigma_n\rfloor\). From (2), uniform continuity of \(g\), and \(u_{n,j_n-h}=(j_n-\mu_n)/\sigma_n-h/\sigma_n\), the lower part, divided by \(\log n\), differs from
\[
 g(s)\frac{\sum_{h\le\eta\sigma_n}h^{-1}}{\log n}
\]
by at most \(o(1)+O(\omega_g(\eta))\), where \(\omega_g\) is a modulus of continuity of \(g\) near \(s\). The harmonic quotient tends to \(1/2\). For the upper part, use (3):
\[
\sum_{h>\eta\sigma_n}\frac{a_{n,j_n-h}}h
\le\frac{\sigma_n^2}{\eta\sigma_n}\sum_kd_{n,k}
\le\frac C\eta.
\]
After division by \(\log n\) it vanishes. Send \(n\to\infty\) and then \(\eta\downarrow0\). Since \(\delta j_n/\sigma_n^2\to\delta/(1-\delta)\), the normalized column converges to
\[
\frac{\delta}{2(1-\delta)}g(s).
\tag{5}
\]
The same split proves localization: if \(j_n\in[\mu_n/2,2\mu_n]\) and \(|(j_n-\mu_n)/\sigma_n|\to\infty\), the lower part is \(o(\log n)\) by the decaying Gaussian envelope in (3), and the upper part is \(O_\eta(1)\). Thus the column divided by \(\log n\) tends to zero.

**5. Global maximization and sharpness.** It remains to exclude columns outside \([\mu_n/2,2\mu_n]\). For \(j\le\mu_n/2\), all contributing \(k<j\) lie in a fixed left large-deviation tail of the binomial distribution; the total expression in (1) is bounded by a polynomial in \(n\) times an exponentially small term. For \(j\ge2\mu_n\), split at \(k=3\mu_n/2\). In the first part, \(j/(j-k)\le4\), hence the contribution is at most \(4^\alpha\delta\sum_kd_{n,k}=O(n^{-1/2})\). The second part is exponentially small after multiplying by the uniform polynomial bound \((j/(j-k))^\alpha\le(n+2)^\alpha\). These estimates apply to all candidate indices \(1\le j\le n+2\), including cases where an outer range is empty.

The central limits (4)–(5), the just-proved localization, and subsequence compactness now identify the global maximum. The function \(g(s)=|s|e^{-s^2/2}/\sqrt{2\pi}\) attains its positive global maximum \(1/\sqrt{2\pi e}\) exactly at \(s=\pm1\). Taking \(j_n\) nearest to \(\mu_n\pm\sigma_n\) provides the matching lower bounds; every maximizing sequence must remain on this scale and has accumulation points only at these two locations. Substitution into (4) and (5) gives the two boxed limits.

Finally, the spectrum assertion follows from \(\|W_\alpha^m\|=(m+1)^\alpha\), which gives spectral radius one, and the eigenvectors \((z^{j-1}/j^\alpha)_{j\ge1}\in\ell^1\) for every \(|z|<1\). The affine spectral mapping theorem finishes the spectral description.

These operators are not absolutely Cesàro bounded when \(\alpha\ge1\). To see this, choose \(j_N=\lfloor\delta N/2\rfloor\) and use positivity to compute
\[
\frac1N\sum_{m=0}^{N-1}\|T^m e_{j_N}\|_1
=\frac1N\sum_{k<j_N}\left(\frac{j_N}{j_N-k}\right)^\alpha\sum_{m=k}^{N-1}b_{m,k}.
\]
The negative-binomial renewal identity gives \(\sum_{m=k}^\infty b_{m,k}=1/\delta\). For all \(k<j_N\), a Chernoff estimate on the binomial right tail yields \(\sum_{m\ge N}b_{m,k}=o(1)\), uniformly in these \(k\): the cumulative number of successes is at most half its typical value at time \(N\). Consequently the last display is bounded below by a fixed positive multiple of
\[
\frac{j_N^\alpha}N\sum_{h=1}^{j_N}h^{-\alpha},
\]
which grows like \(\log N\) for \(\alpha=1\) and like \(N^{\alpha-1}\) for \(\alpha>1\). This identifies the loss of absolute Cesàro boundedness precisely at the boundary of the known subcritical regime, without invoking any norm-difference asymptotic.

## Verification

The proof uses exact column identities, a binomial local central limit theorem with an independently justified envelope, singular harmonic-series truncation, and a global escape-of-maximizers argument. The packaged `check.py` verifies exact finite-dimensional column formulas against direct rational-coordinate iterations for 63 parameter cases and performs 24 supplementary numerical scaling/localization assertions, totaling 87 passing checks. These finite tests do **not** certify either limit or priority. Reproduce with Python 3 (standard library only): `python check.py`.

## Relationship to prior work

Arnold (2026), in Example 3.2 and Section 7, studies positive polynomially weighted backward shifts, absolute Cesàro boundedness, and lazy convex averaging, and discusses the Katznelson–Tzafriri phenomenon. The same operator family, including the identity (1), was analyzed quantitatively for \(0<\alpha<1\) in *Gaussian sharp constants for lazy positive weighted shifts* (2026), where both power and difference norms have fractional Gaussian asymptotics; that proof explicitly excludes \(\alpha=1\) because its kernel ceases to be integrable. The present theorem does not repeat or claim the subcritical result: it identifies the previously excluded critical and supercritical regimes and their different harmonic and zeta constants. *Sharp power growth and power-difference decay for positive lazy backward shifts on reflexive sequence spaces* (2026) is confined to \(1<p<\infty\), \(0<\alpha<1/p\) and cannot imply these \(\ell^1\) endpoint formulas.

Abbar–Arnold–Coine (2026) classify absolute Cesàro conditions and power growth for weighted shifts but do not state a sharp consecutive-power-difference law of this form. The classical Katznelson–Tzafriri theorem addresses power-bounded operators and hence does not imply norm decay here. In particular, this theorem does **not** constitute a counterexample to Katznelson–Tzafriri under its hypotheses. Searches for weighted-binomial, singular-convolution, and equivalent shift formulations found no directly covering statement; this is not an exhaustive priority proof.

## Limitations

The two limits concern this fixed power-weighted shift family on \(\ell^1\), not arbitrary positive operators. At \(\alpha\ge1\), the models lie outside the absolute-Cesàro-bounded hypothesis motivating the subcritical results, so they do not resolve the positive absolutely-Cesàro-bounded Katznelson–Tzafriri question. The parameters are fixed; there is no uniform transition formula when \(\alpha\downarrow1\) jointly with \(n\to\infty\). No upper-order correction or eventual sign selection for maximizing columns is claimed. An earlier equivalent asymptotic may exist under generalized binomial transforms or weighted convolution terminology; independent literature review remains necessary.

## References

1. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1 (first publicly submitted 2026-09-24), https://arxiv.org/abs/2610.00271 ; see Example 3.2 and Section 7.
2. A. Abbar, L. Arnold, C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1 (first publicly submitted 2026-09-21), https://arxiv.org/abs/2609.24601 ; see Section 3.
3. *Gaussian sharp constants for lazy positive weighted shifts* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-gaussian-sharp-constants-for-lazy-positive-weighted-shifts--57373dad5d93 ; see the exact subcritical statements and singular-integral lemma.
4. *Sharp power growth and power-difference decay for positive lazy backward shifts on reflexive sequence spaces* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-power-growth-and-power-difference-decay-for-positive-lazy--c5f2f187c821 .
5. Y. Katznelson, L. Tzafriri, *On power bounded operators*, Journal of Functional Analysis 68 (1986), 313–328.
