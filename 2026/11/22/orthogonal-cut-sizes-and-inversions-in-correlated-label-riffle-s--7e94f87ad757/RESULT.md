# Orthogonal cut sizes and inversions in correlated-label riffle shuffles

## Finding

**Theorem (exact regression and a dependence transition).** Start from the ordered deck of \(n\ge2\) distinct cards. Draw a stationary fair binary Markov label word \(L_1,\ldots,L_n\) with independently occurring changes, each of probability \(h/2\), where \(0<h\le1\). Stably sort first the zero-labelled cards, then the one-labelled cards. Let \(K_n\) count zero labels (the inverse-riffle cut size) and let \(I_n\) count inversions created by this one shuffle. Write \(p=1-h\).

For every \(n\ge2\), every \(0<h\le1\) and every \(k\) with positive probability,
\[
\boxed{\mathbb E[I_n\mid K_n=k]=\frac{k(n-k)}2,\qquad
\operatorname{Cov}(K_n,I_n)=0.}
\]
Nevertheless \(K_n\) and \(I_n\) are *not* independent for any such finite \(n,h\).

For a triangular sequence \(h=h_n\in(0,1]\) with \(nh_n\to\infty\), define
\[
A_n=\frac{K_n-n/2}{\sqrt{n(1+p_n)/(4h_n)}},\qquad
B_n=\frac{I_n-\mathbb EI_n}{\sqrt{n^3(1+p_n)/(48h_n)}},
\quad p_n=1-h_n.
\]
Then
\[
\boxed{(A_n,B_n)\ \Longrightarrow\ (Z_1,Z_2),\qquad
Z_1,Z_2\text{ independent }N(0,1).}
\]
In contrast, if \(nh_n\to\lambda\in(0,\infty)\), the joint limit
\[
\boxed{\left(K_n/n,I_n/n^2\right)\Longrightarrow
\left(\int_0^1\mathbf1\{S(t)=-1\}\,dt,
\int_{0<s<t<1}\mathbf1\{S(s)=+1,S(t)=-1\}\,ds\,dt\right)}
\]
has zero covariance but dependent coordinates. Here \(S\) is the stationary, fair-initial, two-state continuous-time Markov chain whose sign switches at rate \(\lambda/2\). Thus exact uncorrelatedness at finite size coexists with genuine dependence at the Poisson-switch scale and asymptotic Gaussian independence on the many-switch scale.

## Assumptions and scope

The theorem concerns one *inverse* correlated-label riffle from the identity deck, not repeated shuffles or the other adhesive riffle rules. The label chain is stationary, symmetric, with transition probabilities \(\mathbb P(L_{i+1}\ne L_i)=h/2\) and independent switch indicators. For finite statements \(n\ge2\) and \(0<h\le1\); the many-switch limit permits arbitrary parameter sequences in that domain, provided \(nh_n\to\infty\). The Poisson-switch limit assumes \(nh_n\to\lambda\in(0,\infty)\). The process \(S(t)\) has values \(\pm1\), starts fair, and has a Poisson switch process of rate \(\lambda/2\). All convergence statements concern \(n\to\infty\) through integers. For reference, \(\mathbb EI_n=\tfrac14\sum_{d=1}^{n-1}(n-d)(1-p^d)\).

## Proof

**1. Exact identity and regression.** Write \(S_i=2L_i-1\), \(W_n=\sum_{i=1}^nS_i\), and \(a_i=n+1-2i\). A pair \(i<j\) is inverted precisely when its labels are \((1,0)\), so direct expansion gives the finite identity
\[
I_n=\frac{n^2}{8}+\frac14\sum_{i=1}^na_iS_i-\frac18W_n^2,\qquad
K_n=\frac{n-W_n}{2}.\tag{1}
\]
More generally, under *any* reversal-invariant law on binary words, reversal preserves \(K_n\) but maps \(I_n\) to \(K_n(n-K_n)-I_n\). The stationary symmetric two-state Markov law is reversal-invariant, so taking conditional expectations proves the regression identity. The label-complement map preserves the law and maps \(K_n\) to \(n-K_n\); therefore the conditional regression is symmetric about \(n/2\) and its covariance with \(K_n\) is zero. The variables are not independent: \(\mathbb P(K_n=0)>0\) and \(I_n=0\) necessarily when \(K_n=0\), whereas \(\mathbb P(I_n>0)>0\) because the word \((1,0,0,\ldots,0)\) has positive probability. Independence would contradict these two facts.

**2. Weighted Markov-chain central limit.** Put \(h=1-p\) and \(D_j=S_j-pS_{j-1}\) for \(2\le j\le n\), with the natural label filtration. They are martingale differences satisfying \(|D_j|\le2\) and \(\mathbb E[D_j^2\mid\mathcal F_{j-1}]=1-p^2=h(1+p)\), a deterministic quantity. For deterministic weights \(b_i\), the exact identity
\[
\sum_{i=1}^nb_iS_i=
S_1\sum_{i=1}^nb_ip^{i-1}+
\sum_{j=2}^nD_j\sum_{i=j}^nb_ip^{i-j}\tag{2}
\]
follows by iterating \(S_j=pS_{j-1}+D_j\). For each of the two weight profiles \(b_i=1\) and \(b_i=a_i\), replace the inner coefficient by \(b_j/h\). Since \(a_{j+r}=a_j-2r\), for the second profile the absolute replacement error is at most
\[
\frac{n p^{n-j+1}}{h}+\frac{2p}{h^2}.\tag{3}
\]
The first profile has the simpler bound \(p^{n-j+1}/h\). Orthogonality of the martingale differences, geometric summation, and the initial-term bounds show that the squared \(L^2\) error is \(O(n^2/h^2+n/h^3)\) for the \(a_i\) profile and \(O(h^{-2}+h^{-2})\) for the constant profile (these bounds can be enlarged uniformly when \(p=0\)); both errors are negligible on the respective scales \(n^3/h\) and \(n/h\) when \(nh\to\infty\). The exact sums
\[
\sum_{j=1}^na_j=0,\qquad
\sum_{j=1}^na_j^2=\frac{n(n^2-1)}3\tag{4}
\]
make the normalized predictable cross-bracket vanish, while the two normalized predictable diagonal brackets tend to one. The maximal normalized martingale summand is \(O((nh)^{-1/2})\), so the scalar martingale central limit theorem applied to every linear combination (or the multivariate martingale theorem) proves
\[
\left(\frac{W_n}{\sqrt{n(1+p)/h}},
\frac{\sum_i a_iS_i}{\sqrt{n^3(1+p)/(3h)}}\right)
\Longrightarrow N_2(0,I_2).\tag{5}
\]
Also \(\mathbb EW_n^2\le n+2n/h=O(n/h)\). Hence \(W_n^2-\mathbb EW_n^2=O_{\mathbb P}(n/h)=o_{\mathbb P}(n^{3/2}/\sqrt h)\). Subtract the expectation in (1), apply (5) and Slutsky's theorem; the sign in the first coordinate does not affect independence. This proves the joint Gaussian limit with the stated normalizations, for any \(nh_n\to\infty\), not merely fixed \(p\).

**3. Poisson-switch regime and nonindependence.** The change indicators are independent Bernoulli variables of success probability \(h_n/2\). If \(nh_n\to\lambda\), their rescaled occurrence times converge to a Poisson point process on \([0,1]\) of rate \(\lambda/2\), independent of the initial fair sign. With finitely many jumps, the occupation-time and ordered inversion-area maps are continuous at configurations of distinct interior jump times. Consequently the two normalized statistics converge jointly to the displayed functionals of \(S\). Boundedness, combined with the finite exact covariance zero, yields limiting covariance zero. But the event that \(S\) starts \(+1\) and has no switches has probability \(e^{-\lambda/2}/2>0\), gives zero time in sign \(-1\), and forces zero inversion area. The inversion area is positive with positive probability, for example on the event of precisely one switch from \(+1\) to \(-1\). The limiting coordinates therefore cannot be independent.

## Verification

The accompanying \(\texttt{verify_joint.py}\) uses exact rational probabilities and exhaustively evaluates all binary strings at every size \(2\le n\le9\) and five rational adhesion parameters. It tests the algebraic identity (1), probability normalization, the exact conditional regression for every possible cut size, zero covariance, the published inversion mean and nondegeneracy. Run \(\texttt{python3 verify_joint.py}\) with Python 3; 5,560 exact assertions pass. These checks verify finite algebra and boundary cases only. The infinite-limit claims follow from the martingale and Poisson-process arguments, not from enumeration.

## Relationship to prior work

Jiang, arXiv:2611.02092v1 (2026), Definition 2.4, defines the correlated-label inverse riffle and studies mixing. The published published-finding corpus finding *Three-scale inversion laws for correlated-label inverse riffle shuffles* establishes the marginal inversion central limit, the marginal Poisson-switch inversion area, and a rare-switch regime. Its full proof includes identity (1) and the weighted martingale representation; those are **credited inputs** here. It does not assert a joint limit with the cut size, the exact conditional mean at every cut size, or the transition from zero covariance with dependence to Gaussian independence. In particular, marginal convergence of inversions does not imply independence of a joint limiting cut-size statistic. The resulting joint theorem requires checking the cross-bracket and the conditional symmetry, not just citing the marginal limit.

The published published-finding corpus finding *A spatial descent–inversion sign transition and joint Gaussian law for biased two-packet riffle shuffles* concerns independent biased labels, joint descents and inversions, and a different covariance; it does not cover the correlated Markov labels and cut-size statistic here. The published published-finding corpus finding *Conditional sign reversal for fixed points and inversions in a packet-reversal shuffle* studies independent packet cuts and fixed cards rather than the present inverse-riffle Markov cut. Classical independent-label riffle inversion results, such as Işlak (2013), provide special cases but do not directly establish this parameter-uniform joint law.

## Limitations

The finite conditional expectation is a consequence of reversal symmetry and is not claimed as a new general theorem about all reversible binary words. The marginal inversion CLT and telegraph-area law are existing results, not independent new findings. The contribution claimed here is the **joint dependence structure with the cut size**, including exact conditional regression and simultaneous Gaussian independence versus non-Gaussian dependence. The theorem gives no mixing-time bounds, no Gaussian convergence rate, and no claim of finite independence. A general historical analysis of Markov-binomial joint inversion generating functions, including an uninspected clumpy-shuffle dissertation, remains a priority risk. No independent assessment has been performed.

## References

1. Y. Jiang, *Adhesive riffle shuffles: one-parameter models and mixing bounds*, arXiv:2611.02092v1, first publicly posted 2026-11-01. https://arxiv.org/abs/2611.02092
2. *Three-scale inversion laws for correlated-label inverse riffle shuffles*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-scale-inversion-laws-for-correlated-label-inverse-riffle-s--6806b0a229ff .
3. *A spatial descent–inversion sign transition and joint Gaussian law for biased two-packet riffle shuffles*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-spatial-descent-inversion-sign-transition-and-joint-gaussian-l--b654a1e0b626 .
4. *Conditional sign reversal for fixed points and inversions in a packet-reversal shuffle*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-conditional-sign-reversal-for-fixed-points-and-inversions-in-a-p--f30d3de5d0f1 .
5. Ü. Işlak, *Descent-Inversion Statistics in Riffle Shuffles*, arXiv:1303.2387 (2013). https://arxiv.org/abs/1303.2387
