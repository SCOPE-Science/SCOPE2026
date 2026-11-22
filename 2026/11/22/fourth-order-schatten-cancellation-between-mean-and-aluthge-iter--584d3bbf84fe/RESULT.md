# Fourth-order Schatten cancellation between mean and Aluthge iterations of two-isometric shifts

## Finding

Let \(c>0\), and define a unilateral weighted shift on \(\ell^2(\mathbb N_0)\) by
\[
 W_c e_n=\left(\frac{n+c+1}{n+c}\right)^{1/2}e_{n+1},\qquad n\ge0.
\]
The operator \(W_c\) is a non-isometric \(2\)-isometry. Let \(M(T)=(T+|T|V)/2\), where \(T=V|T|\) is its canonical polar decomposition, and let \(\Delta(T)=|T|^{1/2}V|T|^{1/2}\) be the classical Aluthge transform. Write \(M^{\circ k}\) and \(\Delta^{\circ k}\) for their respective \(k\)-fold nonlinear iterations, and put
\[
 D_{c,k}=M^{\circ k}(W_c)-\Delta^{\circ k}(W_c),\qquad k\ge1.
\]
Then \(D_{c,k}\) is compact, nonzero, and belongs to the Schatten quasi-ideal \(\mathcal S_p\) **if and only if** \(p>1/4\), for every finite real \(p>0\) and every \(k\ge1\). Moreover, for every \(p>1/4\),
\[
 \boxed{\lim_{k\to\infty}k^{3p-1}\|D_{c,k}\|_{\mathcal S_p}^{p}
 =\frac{1}{2^{p+1}(4p-1)}.}
\]
At the operator-norm endpoint,
\[
 \boxed{\lim_{k\to\infty} k^3\|D_{c,k}\|=\frac12.}
\]
The constants are independent of \(c\). In particular, every difference is trace class although neither of the two individual differences from the unweighted shift is trace class, and
\[
 \lim_{k\to\infty}k^2\|D_{c,k}\|_{\mathcal S_1}=\frac1{12}.
\]
A stronger, degree-resolved profile underlies these assertions: if \(d_{n,k}\) is the weight of \(D_{c,k}\) from \(e_n\) to \(e_{n+1}\), then for all \(t\ge0\),
\[
 \boxed{\lim_{k\to\infty}k^3d_{\lfloor tk\rfloor,k}
 =\frac{1}{32(t+1/2)^4}.}
\]
The convergence is uniform on compact intervals of \(t\).

## Assumptions and scope

The parameter \(c\) is any fixed strictly positive real number; the space is complex \(\ell^2(\mathbb N_0)\). The transforms are applied using the canonical polar decomposition at every step. For finite \(0<p<1\), \(\|T\|_{\mathcal S_p}^p\) denotes the sum of the \(p\)-th powers of the singular values, without claiming a norm triangle inequality. The formulas include all positive integral iteration counts \(k\), all finite Schatten exponents on either side of the sharp threshold, and the operator norm. No statement of norm convergence uniform in \(c\) is made.

## Proof

**1. Exact shift and iteration identities.** Put \(w_n=\sqrt{(n+c+1)/(n+c)}\). Directly,
\[
 w_n^2w_{n+1}^2-2w_n^2+1=\frac{n+c+2}{n+c}-2\frac{n+c+1}{n+c}+1=0,
\]
so the shift is a \(2\)-isometry by testing the defining operator polynomial on the canonical basis. For a positive weighted shift, \(M\) replaces adjacent weights by their arithmetic mean, whereas \(\Delta\) replaces them by their geometric mean. Let \(J_k\sim\operatorname{Bin}(k,1/2)\) and set
\[
 h(u)=\frac12\log\left(1+\frac1u\right),\qquad u>0.
\]
Induction on \(k\) shows that the two sets of iterated weights are, respectively,
\[
 a_{n,k}=\mathbb E\exp h(n+c+J_k),\qquad
 g_{n,k}=\exp\big(\mathbb E h(n+c+J_k)\big).
\]
Consequently
\[
 d_{n,k}=a_{n,k}-g_{n,k}>0,
\]
by the strict convexity of the exponential: the distribution of \(J_k\) is nondegenerate, and \(h\) is strictly decreasing. Because \(D_{c,k}e_n=d_{n,k}e_{n+1}\), its nonzero singular values, with multiplicity, are precisely the numbers \(d_{n,k}\).

**2. Exact tail and the Schatten threshold.** Fix \(k\ge1\). As \(n\to\infty\), uniformly over \(0\le j\le k\),
\[
 h(n+c+j)=h(n+c)+j h'(n+c)+O_{c,k}(n^{-3}),
 \quad h'(u)=-\frac1{2u(u+1)}.
\]
Since \(\operatorname{Var}(J_k)=k/4\), it follows that
\[
 \operatorname{Var}(h(n+c+J_k))=\frac{k}{16n^4}+O_{c,k}(n^{-5}).
\]
Taylor expansion of the exponential at the mean, with uniformly small fluctuations, gives
\[
 d_{n,k}=\frac12\operatorname{Var}(h(n+c+J_k))(1+o(1))
 =\frac{k}{32n^4}(1+o(1)).
\]
Thus \(D_{c,k}\) is compact and nonzero, and \(\sum_{n\ge0}d_{n,k}^p\) converges exactly when \(4p>1\). This conclusion is valid for all positive real \(p\), including the quasi-Banach range.

**3. The uniform binomial scale.** For \(n/k\to t\) with \(t\) in a fixed compact subset of \([0,\infty)\), center \(J_k\) at \(k/2\), and write \(u=n+c+k/2\). On the overwhelmingly likely event \(|J_k-k/2|\le k^{2/3}\), Taylor's formula yields
\[
 h(n+c+J_k)=h(u)+h'(u)(J_k-k/2)+R,
\qquad |R|\le Ck^{-3}(J_k-k/2)^2.
\]
The fourth central binomial moment is \(O(k^2)\), so \(\|R\|_{L^2}=O(k^{-2})\). The complementary event has exponentially small probability in \(k^{1/3}\), and \(h\) is bounded on \([c,\infty)\); hence it does not affect the stated orders. The linear part has \(L^2\) size \(O(k^{-3/2})\), and therefore
\[
 \operatorname{Var}(h(n+c+J_k))
 =\frac{k}{4}h'(u)^2+o(k^{-3})
 =\frac1{16k^3(t+1/2)^4}+o(k^{-3}),
\]
with uniform errors for \(t\) in compact sets. Since its mean tends to zero and its centered third absolute moment is \(o(k^{-3})\), expanding the exponential gives
\[
 d_{n,k}=\frac12\operatorname{Var}(h(n+c+J_k))+o(k^{-3}),
\]
proving the stated locally uniform weight profile.

**4. A summable domination, including the far tail.** For a real random variable \(Z\) in \([0,h(c)]\), Taylor's theorem gives
\[
 0\le \mathbb E e^Z-e^{\mathbb E Z}
 \le \frac{e^{h(c)}}2\operatorname{Var}(Z).
\]
Apply the Efron–Stein inequality to the function \(j\mapsto h(n+c+j)\) of a sum of \(k\) independent fair bits. With \(J_{k-1}\sim\operatorname{Bin}(k-1,1/2)\),
\[
 \operatorname{Var}(h(n+c+J_k))
 \le\frac{k}{4}\mathbb E\left|h(n+c+J_{k-1}+1)-h(n+c+J_{k-1})\right|^2.
\]
By \(|h'(u)|\le(2u^2)^{-1}\), the last expression is at most
\[
 \frac{k}{16}\mathbb E(n+c+J_{k-1})^{-4}.
\]
A binomial concentration bound gives constants \(C_c,\gamma>0\), independent of \(k,n\), such that
\[
 0\le d_{n,k}\le C_c k\left((n+k)^{-4}+e^{-\gamma k}(n+c)^{-4}\right),\qquad k\ge2,\ n\ge0.
\]
Indeed, split according to \(J_{k-1}\ge k/4\); the complement has probability at most \(C e^{-\gamma k}\), and small \(k\) can be absorbed by enlarging \(C_c\). This estimate also supplies an explicit global domination without assuming finite-dimensional truncation is exhaustive.

For any \(p>1/4\), the contribution of the exponential term to the rescaled \(p\)-sum vanishes, because \(\sum_{n\ge0}(n+c)^{-4p}<\infty\). The other term provides a Riemann-summable tail after the change \(n=kt\). Combining it with the compact-uniform profile proves
\[
 \begin{aligned}
 \lim_{k\to\infty} k^{3p-1}\sum_{n\ge0}d_{n,k}^p
 &=\int_0^\infty\frac{dt}{32^p(t+1/2)^{4p}}\\
 &=\frac{1}{2^{p+1}(4p-1)}.
 \end{aligned}
\]
For the operator norm, the same bound makes the normalized tail beyond \(n>Rk\) uniformly small as \(R\to\infty\); on \(0\le n\le Rk\), the uniform profile has its maximum at \(t=0\), equal to \(1/(32(1/2)^4)=1/2\). This proves the norm assertion.

## Verification

The companion standalone `check_gap.py` uses the Python standard library. Its finite, independently computed tests verify \(180\) rational \(2\)-isometry identities, \(108\) arithmetic/geometric iteration identities, and \(66\) fixed-degree and scaled-limit numerical checks. Running `python3 check_gap.py` prints its PASS counts. These tests check bookkeeping and constants; the infinite-dimensional claims rest on the preceding analytic proof, not on finite enumeration. Useful special cases of the exact law are
\[
 k^2\|D_{c,k}\|_{\mathcal S_1}\longrightarrow\frac1{12},
 \qquad k^5\|D_{c,k}\|_{\mathcal S_2}^2\longrightarrow\frac1{56}.
\]

## Relationship to prior work

Chabbabi and Ostermann, *The Aluthge and the mean transforms of \(m\)-isometries* (arXiv:2203.15658, initially public on 2022-03-29), classify the pertinent positive \(2\)-isometric weighted shifts and study which transforms preserve higher isometries. Chabbabi, Curto, and Mbekhta, *The mean transform and the mean limit of an operator* (arXiv:1812.03499, 2018), Section 4, give the binomial iteration formulas for both transforms and discuss norm/spectral limits. Those formulas are used as background rather than presented as new. Altwaijry, Conde, Feki, and Stanković, *Schatten \(p\)-norm related to some transforms of operators* (2024, DOI:10.3934/cpaa.2024078), establish general one-step norm inequalities and equality criteria for operators already in Schatten ideals. They do not evaluate the difference of the two infinite-dimensional nonlinear orbits here, which is itself in trace class even though the starting shifts are not. A later article by Zhou and Yang, *Power mean transforms of operators* (arXiv:2606.17556, 2026), studies another operator-mean family, its norm, spectrum, and numerical radius; it does not give this trace-ideal asymptotic. The new assertion is the critical \(p=1/4\) cancellation threshold, its complete singular-weight profile, and the exact all-\(p\) constants for the natural two-isometric family. A literature search cannot rule out unindexed antecedents.

## Limitations

Only classical \(1/2\)-Aluthge versus arithmetic-mean iteration is treated. No generalization to arbitrary weighted shifts, multi-variable shifts, or other operator means is asserted. The profile is asymptotic as \(k\to\infty\) for each fixed \(c>0\), not a uniform parameter theorem. Strict positivity of \(c\) is essential to boundedness of the initial weights at index zero. The result has received no independent mathematical validation.

## References

1. F. Chabbabi and M. Ostermann, *The Aluthge and the mean transforms of \(m\)-isometries*, arXiv:2203.15658, v1 2022-03-29, https://arxiv.org/abs/2203.15658.
2. F. Chabbabi, R. Curto, and M. Mbekhta, *The mean transform and the mean limit of an operator*, arXiv:1812.03499, v1 2018-12-09, https://arxiv.org/abs/1812.03499.
3. S. H. Lee, W. Y. Lee, and J. Yoon, *The mean transform of bounded linear operators*, J. Math. Anal. Appl. 410 (2014), 70–81, https://doi.org/10.1016/j.jmaa.2013.08.003.
4. N. Altwaijry, C. Conde, K. Feki, and H. Stanković, *Schatten \(p\)-norm related to some transforms of operators*, Commun. Pure Appl. Anal. 23 (2024), 1990–2004, https://doi.org/10.3934/cpaa.2024078.
5. J.-B. Zhou and S. Yang, *Power mean transforms of operators*, arXiv:2606.17556, 2026, https://arxiv.org/abs/2606.17556.
