# Mesoscopic near-start visits and one-giant-jump paths in the harmonic descent chain

## Finding

Let the harmonic descent chain start at \(n\). Write \(E_n\) for the event of visiting \(n-h_n\), where \(h_n\to\infty\) and \(\log h_n/\log n\to\theta\in(0,1)\). On \(E_n\), let \(K_n\) be the jump count up to that visit. For each fixed \(k\ge1\), conditional on \(E_n\) and \(K_n=k\), write the decrements in time order as \((D_{n,1},\dots,D_{n,k})\); they sum to \(h_n\). Let \(J_n\) be the leftmost index attaining their maximum. Then \(D_{n,J_n}/h_n\to1\) in conditional probability, and
\[
\left(J_n,\bigl(\log D_{n,i}/\log h_n:i\ne J_n\bigr)\right)
\xrightarrow{d} (J,U_1,\ldots,U_{k-1}),
\]
where the vector omitting \(J_n\) is ordered by time, \(J\) is uniform on \(\{1,\ldots,k\}\), and the \(U_i\) are independent \(\operatorname{Unif}(0,1)\), independent of \(J\). In particular there is a unique decrement greater than \(h_n/2\) with conditional probability tending to one. For \(k=1\) the vector omitting the largest decrement is empty.

The count normalization is
\[
\Pr(K_n=k\mid E_n)\longrightarrow k(1-\theta)^2\theta^{k-1}.
\]
Thus the path law describes a random, finite number of decrements on the rare visiting paths. The asymptotic \(\Pr(E_n)\sim 1/[h_n\log n(1-\theta)^2]\) used for that normalization is also a consequence of prior exact occupation and harmonic-moment formulas, as described below; it is not claimed as a separate novelty.

## Assumptions and scope

For \(m\ge1\) set \(H_m=\sum_{j=1}^m j^{-1}\) and set \(H_0=0\). At a state \(j\ge2\), a decrement \(d\in\{1,\ldots,j-1\}\) has probability \(1/(dH_{j-1})\); state 1 is absorbing. Eventually \(1\le h_n\le n-2\) is integral. The conditional geometry is for fixed \(k\), not a uniform limit with \(k\) growing with \(n\). The count normalization requires a fixed limiting exponent strictly between zero and one. The proof does not assume an exact power law for \(h_n\).

## Proof

**1. Path weights.** Write \(h=h_n\) and
\[
b_{h,k}=\sum_{d_i\ge1,\;\sum_i d_i=h}\frac{1}{d_1\cdots d_k}
       =[z^h]L(z)^k,\qquad L(z)=-\log(1-z),
\]
with \(b_{0,0}=1\) and \(b_{h,0}=0\) for \(h>0\). The exact weight of a composition is \((\prod_i d_i^{-1})\prod_{i=0}^{k-1}H_{n-1-d_1-\cdots-d_i}^{-1}\), with an empty prefix at \(i=0\). Since intermediate states are in \([n-h+1,n]\), for all \(1\le k\le h\),
\[
\frac{b_{h,k}}{H_{n-1}^k}\le \Pr(E_n,K_n=k)\le\frac{b_{h,k}}{H_{n-h}^k}.\tag{1}
\]

**2. Count normalization.** Differentiating \(L(z)^k\) gives \(h b_{h,k}=k\sum_{j=0}^{h-1}b_{j,k-1}\). The sum counts reciprocal-product weights of \((k-1)\)-tuples with total at most \(h-1\). Ignoring the total restriction gives \(h b_{h,k}\le k H_{h-1}^{k-1}\). For fixed \(k\) and \(0<\varepsilon<1\), all tuples with entries at most \(\lfloor h^{1-\varepsilon}\rfloor\) are included for sufficiently large \(h\). Their weight is \(H_{\lfloor h^{1-\varepsilon}\rfloor}^{k-1}\). Letting \(\varepsilon\downarrow0\) proves
\[
b_{h,k}\sim\frac{k}{h}(\log h)^{k-1}.\tag{2}
\]
If \(aH_{h-1}\to\theta\) for positive \(a\), the terms \(h a^{k-1}b_{h,k}\) tend pointwise to \(k\theta^{k-1}\) and are bounded by \(k(aH_{h-1})^{k-1}\). The bounds are summable uniformly for all sufficiently large \(h\), since \(\theta<1\). Thus \(\sum_{k=1}^h a^k b_{h,k}\sim a/[h(1-\theta)^2]\). Apply this to both reciprocals in (1), using \(h=o(n)\) and \(a\log n\to1\). This gives the displayed asymptotic for \(\Pr(E_n)\). For fixed \(k\), (1) and (2) then give the count law; the limiting masses sum to one.

**3. Conditional paths.** Fix \(k\ge2\). Relative to \(H_{n-1}^{-k}\), the exact product of harmonic normalizers lies between 1 and \((H_{n-1}/H_{n-h})^k=1+o(1)\), uniformly in the composition. Upon conditioning on the hit and its count, the normalized path law is therefore within \(o(1)\) in total variation of the composition probability proportional to \(1/\prod_i d_i\).

Choose \(r\in\{1,\ldots,k\}\) and cutoffs \(0<t_i<1\) for \(i\ne r\). For each choice of \(1\le d_i\le \lfloor h^{t_i}\rfloor\) at these indices, the remaining decrement \(d_r=h-\sum_{i\ne r}d_i\) uniformly satisfies \(d_r/h\to1\). The weight of all these compositions is
\[
\frac{1+o(1)}h\prod_{i\ne r}H_{\lfloor h^{t_i}\rfloor}
\sim \frac{(\log h)^{k-1}}h\prod_{i\ne r}t_i.
\]
For large \(h\) the designated decrement is uniquely largest, so division by (2) yields joint limiting mass \(k^{-1}\prod_{i\ne r}t_i\) for that index and those logarithmic cutoffs. Taking all cutoffs to a common \(t<1\) and summing over indices, the disjoint events have limiting total mass \(t^{k-1}\). On their union the largest decrement has size at least \(h-(k-1)h^t\); letting \(t\uparrow1\) proves the probability assertion. The rectangular masses give the joint law because its continuous-coordinate limit has continuous distribution functions. The total-variation comparison transfers these statements to the descent chain. The case \(k=1\) is exact.

## Relationship to prior work

Aldous, Janson and Li identify fixed-target occupation limits. Brandenberger, Chin and Mossel give a near-start upper bound of order \(1/[hH_{n-h}]\) in sublinear ranges that include the present regime (Theorem 1.1(iii)). Their tagged-leaf identity, equation (1.5), identifies the conditioned paths with the tagged leaf's sequence of ancestral clade sizes up to a near-full-sized clade. The identity also gives \(\mathbb E N_n(n-h)=n\Pr(E_n)/(n-h)\). Iksanov gives a regenerative-composition representation to recover the fixed-target limit. Svihla's small-target spectral asymptotic treats a different asymptotic regime.

There is nevertheless a direct prior implication for the **unmarked hit probability**. Put \(q=n-h\). The exact finite-difference formula of Aldous–Janson–Li (as reproduced in Svihla, §2.1), together with Berg–Durán's harmonic moment representation, gives
\[
\Pr(E_n)=H_{q-1}\binom{n-1}{q-1}\int_0^1 t^{q-2}(1-t)^h\rho(t)\,dt,
\quad \rho(t)=\sum_{j\ge0}\alpha_j t^{\xi_j}.
\]
Berg–Durán give \(j<\xi_j<j+1\) for \(j\ge1\) and \(\alpha_j\sim1/\log^2 j\). The Abelian power-series estimate for slowly varying coefficients, squeezing \(t^{\xi_j}\) between \(t^{j+1}\) and \(t^j\), gives \((1-t)\rho(t)\sim1/\log^2(1/(1-t))\). Equivalently, \(\Pr(E_n)\) is \(H_{q-1}(n-1)/[h(q-1)]\) times the expectation of \(Y\rho(1-Y)\) for \(Y\sim\operatorname{Beta}(h,q-1)\). The function \(y\rho(1-y)\) is bounded, and \(Y\) lies in a factor-two neighborhood of its mean \(h/(n-1)\) except with probability \(O(1/h)\) by the beta variance formula. The expectation is therefore asymptotic to \(1/\log^2(n/h)\). This gives the same hit constant from prior results. The count law above is included as a normalization consequence of the hit mass and fixed-count coefficient asymptotics.

The reference composition law has a classical permutation interpretation: \(b_{h,k}=k!|s(h,k)|/h!\), where \(|s(h,k)|\) is an unsigned Stirling number of the first kind. Indeed a uniform permutation of \(h\) elements conditioned to have \(k\) cycles, with a uniformly random ordering of those cycles, gives the reciprocal-product weights on ordered cycle lengths. Granville's cycle-length theorem for a growing conditioned number of cycles is not the fixed-count statement above. The contribution here is the conditional path law for the descending tagged chain, with its joint distribution of the time index and all remaining logarithmic decrements. Neither the unmarked occupation formulas nor the cited global tree height and decrement count results specify those conditioned paths.

## Verification and limitations

The accompanying `checker.py` provides auxiliary checks of finite composition coefficients, finite hitting probabilities, and the harmonic sandwich, as well as numerical checks of the coefficient crossover. The conditional path theorem and its limits rely on the proof above, not on a finite checker. The result does not address the critical exponent \(\theta=1\), a growing conditioned jump count, or arbitrary decrement kernels. Priority of equivalent fixed-cycle statements outside the references below is not settled.

## References

1. D. J. Aldous, S. Janson, and X. Li, *The Harmonic Descent Chain*, Electron. Commun. Probab. 29 (2024), https://arxiv.org/abs/2405.05102.
2. A. Brandenberger, B. Chin, and E. Mossel, *Asymptotics for the Harmonic Descent Chain and Applications to Critical Beta-Splitting Trees*, Theorem 1.1 and equation (1.5), https://arxiv.org/abs/2505.24821.
3. S. P. Svihla, *Exact Asymptotics for the Harmonic Descent Chain and Extended Convergence Bounds for Recursive Statistics*, §2.1, https://arxiv.org/abs/2611.00347.
4. A. Iksanov, *A Comment on the Article ‘The Harmonic Descent Chain’ by D. J. Aldous, S. Janson and X. Li*, https://arxiv.org/abs/2412.06826.
5. C. Berg and A. J. Durán, *Some Transformations of Hausdorff Moment Sequences and Harmonic Numbers*, Canad. J. Math. 57 (2005), 941–960, pp. 953–954, https://doi.org/10.4153/CJM-2005-036-8.
6. A. Granville, *Cycle lengths in a permutation are typically Poisson*, Electron. J. Combin. 13 (2006), R107, Theorem 3, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1r107.
7. A. Iksanov, I. Nikitin, and A. Yakymiv, *An Infinite Balls-in-Boxes Approach to the Critical Beta-Splitting Tree: Some Central Limit Theorems*, https://do.csc.knu.ua/iksan/wp-content/uploads/sites/3/2026/02/iksnikyak130226-rev.pdf.
