# A spatial descent–inversion sign transition and joint Gaussian law for biased two-packet riffle shuffles

## Finding

Fix a packet probability \(p\in(0,1)\), write \(r=1-p\), \(q=pr\), and \(\delta=r-p\). For each integer \(n\ge2\), let \(\Pi_n\) be a forward two-packet riffle shuffle: cut a sorted deck of \(n\) cards into piles of respective sizes \(K\sim\operatorname{Bin}(n,p)\) and \(n-K\), then choose a uniformly random order-preserving interleaving. Set
\[
B_{n,i}=\mathbf1\{\Pi_n(i)>\Pi_n(i+1)\},\quad
D_n=\sum_{i=1}^{n-1}B_{n,i},\quad
I_n=\sum_{1\le j<k\le n}\mathbf1\{\Pi_n(j)>\Pi_n(k)\}.
\]
For every \(1\le i<n\), the exact position-specific mixed covariance is
\[
\boxed{\operatorname{Cov}(B_{n,i},I_n)
=q\left[1-q+\delta\bigl(i-1-p(n-2)\bigr)\right].}
\]
For \(p\ne1/2\) this covariance is strictly monotone along the deck and takes **both strictly negative and strictly positive values** precisely when
\[
\boxed{n>2+\frac{1-q}{\min(p,r)|\delta|}.}
\]
If \(i_n/n\to x\in[0,1]\), the normalized profile converges to \(q\delta(x-p)\). The profile is constant and strictly positive when \(p=1/2\).

The joint fluctuation law, with \(p\) fixed as \(n\to\infty\), is
\[
\boxed{\left(\frac{D_n-(n-1)q}{\sqrt n},\frac{I_n-\binom n2q}{n^{3/2}}\right)
\ \xrightarrow{\ d\ }\ N_2(0,\Sigma_p),\qquad
\Sigma_p=q\begin{pmatrix}1-3q&\delta^2/2\\\delta^2/2&(1-3q)/3\end{pmatrix}.}
\]
The limiting covariance matrix is positive definite, and its two components are independent **if and only if** \(p=1/2\). For \(p\ne1/2\), the limiting correlation is
\[
\rho_p=\frac{\sqrt3\,\delta^2}{2(1-3q)}>0.
\]
The function \(\rho_p\) increases strictly with \(|p-1/2|\) and approaches the unattained supremum \(\sqrt3/2\) as \(p\downarrow0\) or \(p\uparrow1\).

## Assumptions and scope

The assertions concern the **forward** riffle-shuffle permutation in one-line card order, **one** shuffle, **two** packets, independent packet assignment with fixed \(0<p<1\), and integer \(n\ge2\). The CLT and correlation statement keep \(p\) fixed, independent of \(n\). The sharp sign condition concerns positions \(1,\dots,n-1\); it does not claim anything about the endpoints \(p=0,1\), at which both statistics become deterministic. The finite-size sign criterion is strict; equality produces a zero at a boundary position, not two opposing strict signs.

## Proof

**1. Coupling and exact mixed covariances.** By the inverse-shuffle digit representation (Işlak, Lemma 2.2), assign i.i.d. binary digits \(Z_1,\ldots,Z_n\) with \(\Pr(Z_i=1)=r\), and invert their stable sort. For all \(j<k\), the indicator of an inversion in the resulting forward shuffle equals \(Z_j(1-Z_k)\), simultaneously for all pairs. Consequently
\[
B_{n,i}=Z_i(1-Z_{i+1}),\qquad I_n=\sum_{j<k}Z_j(1-Z_k).
\]
Each such indicator has mean \(q\); a descent indicator has variance \(q(1-q)\). An inversion with endpoints disjoint from \(\{i,i+1\}\) has zero covariance with \(B_{n,i}\). For any \(j<i\), the two inversions \((j,i)\) and \((j,i+1)\) contribute respectively \(-q^2\) and \(qr^2\) to the mixed covariance. For any \(k>i+1\), the two inversions \((i,k)\) and \((i+1,k)\) contribute respectively \(qp^2\) and \(-q^2\). The inversion \((i,i+1)\) contributes \(q(1-q)\). Therefore
\[
\begin{aligned}
\operatorname{Cov}(B_{n,i},I_n)
&=q(1-q)+(i-1)q(r^2-q)+(n-i-1)q(p^2-q)\\
&=q[1-q+\delta(i-1-p(n-2))].
\end{aligned}
\]
Its difference at successive positions is exactly \(q\delta\). If \(\delta>0\), its minimum is at \(i=1\) and is negative exactly when \(p(n-2)\delta>1-q\); the opposite endpoint is positive. For \(\delta<0\), the minimum is at \(i=n-1\), negative exactly when \(r(n-2)|\delta|>1-q\); the opposite endpoint is positive. This proves the sharp sign condition. Dividing the exact expression by \(n\) proves the spatial limit.

**2. Exact second moments.** Disjoint descent indicators are independent; adjacent descents are mutually exclusive, with covariance \(-q^2\). Thus
\[
\operatorname{Var}(D_n)=(n-1)q(1-q)-2(n-2)q^2.
\]
For two different inversion indicators, only a shared index produces a nonzero covariance. Within every triple \(j<k<l\), the three pairwise covariances of inversions \((j,k),(j,l),(k,l)\) are respectively \(qp^2,-q^2,qr^2\). Their sum is \(q(1-3q)\), which yields
\[
\operatorname{Var}(I_n)=\binom n2q(1-q)+2\binom n3q(1-3q).
\]
Summing the exact positional mixed covariances gives
\[
\operatorname{Cov}(D_n,I_n)
=(n-1)q(1-q)+\binom{n-1}{2}q\delta^2.
\]
These equations yield, after dividing by the scales \(n\), \(n^3\), and \(n^2\), precisely the three entries of \(\Sigma_p\).

**3. Joint central limit theorem.** Put \(U_k=Z_k-r\), so \(\mathbb E U_k=0\), \(|U_k|\le1\), and \(\operatorname{Var}(U_k)=q\). The exact algebraic identity
\[
Z_j(1-Z_k)=q+pU_j-rU_k-U_jU_k
\]
gives the decomposition
\[
I_n-\binom n2 q
=\underbrace{\sum_{k=1}^n(np-k+r)U_k}_{L_n}
-\underbrace{\sum_{j<k}U_jU_k}_{Q_n}.
\]
The summands of \(Q_n\) are pairwise uncorrelated, even if their pairs share one index, since each centered, independent digit then contributes a factor of zero mean. Hence \(\mathbb E Q_n^2=\binom n2 q^2=O(n^2)\), and \(Q_n/n^{3/2}\to0\) in \(L^2\).

To prove a joint CLT for \(D_n\) and \(L_n\), fix arbitrary real coefficients \(a,b\). Their normalized linear combination is, up to a final independent weighted digit and a factor vanishing with \(n\), the \(n^{-1/2}\) sum of the uniformly bounded one-dependent triangular array
\[
a\bigl(Z_i(1-Z_{i+1})-q\bigr)
+b\left(p-\frac in+\frac rn\right)U_i,
\qquad 1\le i<n.
\]
For completeness, split the indices into successive blocks of length \(\lfloor n^{1/3}\rfloor\), omitting one index between blocks. Different retained blocks depend on disjoint digits and are independent. The omitted terms have total variance \(O(n^{2/3})\) because the array is uniformly bounded and one-dependent; divided by \(n\) this tends to zero. Each retained block is deterministically \(O(n^{1/3})=o(\sqrt n)\), so the independent blocks satisfy the Lindeberg condition. Exact moments in step 2 and the \(L^2\)-small remainder show the limiting variance of this linear combination is \((a,b)\Sigma_p(a,b)^\mathsf T\). By the Lindeberg–Feller theorem, the Cramér–Wold device, and Slutsky's theorem, the stated bivariate normal limit follows.

**4. Nondegeneracy and independence.** Direct calculation gives
\[
\det\Sigma_p=\frac{q^2}{12}(1-12q^2)>0
\]
since \(0<q\le1/4\). The off-diagonal entry \(q\delta^2/2\) vanishes exactly at \(p=1/2\). For a bivariate Gaussian, vanishing covariance is equivalent to independence. Substituting \(q=(1-\delta^2)/4\) yields \(\rho_p=2\sqrt3\,\delta^2/(1+3\delta^2)\), strictly increasing for \(\delta^2\in[0,1)\) and tending to \(\sqrt3/2\) at the excluded endpoints.

## Verification

The standalone standard-library script `verify.py` enumerates all \(2^n\) binary digit words for each \(n=2,\ldots,9\) at five distinct rational packet probabilities, and computes every claimed first and second moment using exact fractions. For \(n\le7\), it independently constructs the forward-shuffle distribution by every possible cut and interleaving and compares it with the inverse stable-sort distribution. It also checks the sharp finite sign condition, monotonicity and nondegeneracy. Executing the embedded script yielded **702 exact assertions passed**. These finite enumerations verify algebra and implementation; the proof above establishes statements for all permitted \(n\) and fixed \(p\).

## Relationship to prior work

Işlak's 2013 paper provides the simultaneous binary-word coupling and separate marginal asymptotic normality for riffle-shuffle inversions and descents (its Lemma 2.2 and Section 3). The claim here concerns the **joint** asymptotic law, its nonzero bias-dependent off-diagonal covariance and the exact **site-resolved sign transition**; these do not appear in the inspected theorem statements and proofs. Conger–Viswanath (2005) establish separate normal approximations for uniformly rearranged fixed-composition multisets and provide overlapping-pair moment tools; those tools can supply portions of the finite covariance calculation after conditioning but do not themselves state the joint biased-shuffle conclusion. Fulman (1997) develops biased riffle-shuffle generating functions but does not state the pointwise mixed covariance or joint Gaussian limit in the inspected relevant sections. Dörr–Heiny (2023/2025) prove joint limit laws for **uniform random permutations**, a different distribution with a different scaling and zero leading cross-covariance. This is a comparison of precisely stated results, not a claim of absolute novelty from absent keywords.

## Limitations

The two-packet distribution, one-shuffle setup and fixed-bias regime are essential to the stated proof. The result does not establish a uniform-in-\(p\) triangular-array CLT as \(p\to0,1\), nor a multivariate Berry–Esseen rate. The finite checks do not certify novelty or infinite-sample convergence. A related 2013 article by Thiel on inversions and the **major index** of words could not be fully inspected through the available sources, so implicit implications from broader joint generating-function identities remain a historical-priority risk; however, the major index is not the descent count, and no dominating statement was verified.

## References

- Ü. Işlak, *Descent-Inversion Statistics in Riffle Shuffles*, arXiv:1303.2387, first publicly posted 2013-03-10, https://arxiv.org/abs/1303.2387 .
- M. Conger and D. Viswanath, *Normal Approximations for Descents and Inversions of Permutations of Multisets*, arXiv:math/0508242, first publicly posted 2005-08-14, https://arxiv.org/abs/math/0508242 .
- J. Fulman, *The Combinatorics of Biased Riffle Shuffles*, arXiv:math/9712240 (1997), https://arxiv.org/abs/math/9712240 .
- P. Dörr and J. Heiny, *Extremes of Joint Inversions and Descents on Finite Coxeter Groups*, arXiv:2309.17314 (2023), https://arxiv.org/abs/2309.17314 .
- M. Thiel, *The Inversion Number and the Major Index Are Asymptotically Jointly Normally Distributed on Words*, arXiv:1302.6708 (2013), https://arxiv.org/abs/1302.6708 .
