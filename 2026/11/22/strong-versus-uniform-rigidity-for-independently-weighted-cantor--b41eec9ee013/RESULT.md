# Strong versus uniform rigidity for independently weighted Cantor multipliers

## Finding
Fix an integer \(b\ge3\), a strictly increasing sequence \(1\le s_1<s_2<\cdots\) of integers, and probabilities \(0<p_j<1\) with a limit \(p_\infty\in[0,1]\). Set
\[
K_S=\left\{\sum_{j\ge1}\varepsilon_jb^{-s_j}:\varepsilon_j\in\{0,1\}\right\},\qquad
X=\sum_{j\ge1}\xi_jb^{-s_j},\quad \Pr(\xi_j=1)=p_j,
\]
where the digits are independent. Write \(\mu\) for the law of \(X\) and \(U f(x)=e^{2\pi i x}f(x)\) on \(L^2(K_S,\mu)\). Then \(U\) is unitary with full spectral support \(e^{2\pi i K_S}\), and:

1. \(U\) is uniformly rigid, meaning \(\|U^{n_k}-I\|\to0\) for increasing positive integers \(n_k\), **if and only if** \(\sup_j(s_{j+1}-s_j)=\infty\).
2. \(U\) is strongly rigid, meaning \(U^{n_k}f\to f\) for every \(f\in L^2(\mu)\), **if and only if** either \(\sup_j(s_{j+1}-s_j)=\infty\) or \(p_\infty\in\{0,1\}\).

In particular, when \(s_j=j\) and \(p_j=1/(j+1)\), the measure \(\mu\) is non-atomic and has full support on the ordinary deleted-digit Cantor set, and \(U^{b^k}\to I\) strongly but \(U\) is not uniformly rigid. Its return on the cyclic vector \(\mathbf1\) has the exact first-order law
\[
\lim_{k\to\infty}k\,\|(U^{b^k}-I)\mathbf1\|_2^2
=4\sum_{h=1}^\infty\sin^2(\pi b^{-h})\in(0,\infty).
\]
With the **same support** and \(p_j=1/2\) instead, the multiplier is not strongly rigid. Thus the underlying Cantor spectral set does not determine strong rigidity, even among non-atomic full-support spectral measures.

## Assumptions and scope
The ambient Hilbert space is \(L^2(\mu)\), not \(C(K_S)\). Convergence of the probabilities is essential to the stated complete strong-rigidity dichotomy; no assertion about arbitrary oscillating probabilities is made. The digit representation is injective for \(b\ge3\): if two binary sequences first differ at position \(s_j\), the leading difference exceeds the total later possible discrepancy, because \(\sum_{r\ge1}b^{-r}=1/(b-1)<1\). All spectral-support assertions concern the unitary multiplication operator, not a composition or Koopman shift.

## Proof
**Support and the strong convergence test.** Each digit cylinder has strictly positive probability since \(0<p_j<1\); hence \(\operatorname{supp}\mu=K_S\). Multiplication by \(e^{2\pi i x}\) is unitary, with spectrum its essential range, equal to \(e^{2\pi i K_S}\). For any increasing integers \(n_k\), the bound \(|e^{2\pi i n_kx}-1|\le2\) and density of bounded functions in \(L^2(\mu)\) show that \(U^{n_k}\to I\) strongly exactly when \(\mathbb E|e^{2\pi i n_kX}-1|^2\to0\). Full support also gives \(\|U^n-I\|=\max_{x\in K_S}|e^{2\pi i nx}-1|\).

**Unbounded gaps.** Let \(g_j=s_{j+1}-s_j\). If \(g_{j_k}\to\infty\), take \(n_k=b^{s_{j_k}}\). The digits preceding the cut contribute an integer and the remaining tail lies between zero and \(b^{-g_{j_k}}/(1-b^{-1})\). Hence
\[
\|U^{n_k}-I\|\le 2\pi\,b^{-g_{j_k}}/(1-b^{-1})\to0.
\]
Consequently the multiplier is uniformly and strongly rigid independently of the probabilities.

**Bounded gaps and probabilities bounded away from zero and one.** Suppose \(g_j\le L\) for all sufficiently large \(j\), and \(p_\infty\in(0,1)\). For every sufficiently large integer \(n\), choose the first \(j\) with \(b^{s_j}\ge2n\). Then
\[
\frac1{2b^L}<\frac n{b^{s_j}}\le\frac12.
\]
The single-digit point \(b^{-s_j}\in K_S\) gives the uniform-norm obstruction
\[
\|U^n-I\|\ge2\sin\!\left(\frac\pi{2b^L}\right)>0.
\]
Moreover, condition on all digits except \(\xi_j\) and use the variance formula for the unit-modulus random variable \(e^{2\pi i nX}\):
\[
\begin{aligned}
\mathbb E|e^{2\pi i nX}-1|^2
&\ge 1-|\mathbb E e^{2\pi i nX}|^2\\
&\ge 4p_j(1-p_j)\sin^2(\pi n/b^{s_j}).
\end{aligned}
\]
The right side stays bounded below by a positive constant because \(p_j\to p_\infty\in(0,1)\), excluding strong rigidity along **any** sequence. The norm obstruction above applies for all convergent bias limits whenever the gaps are bounded.

**Endpoint bias zero.** If \(p_j\to0\), take \(n_k=b^{s_k}\). Write \(n_kX=\text{integer}+R_k\) with \(0\le R_k=\sum_{j>k}\xi_jb^{s_k-s_j}\le1/(b-1)\). Then
\[
\mathbb E R_k\le\frac{\sup_{j>k}p_j}{b-1}\longrightarrow0.
\]
Since \(|e^{2\pi it}-1|^2\le 2|e^{2\pi it}-1|\le4\pi t\) for \(t\ge0\), the strong convergence test applies.

**Endpoint bias one.** If \(p_j\to1\), put \(\eta_j=1-\xi_j\), \(\delta_k=\sup_{j>k}(1-p_j)\to0\),
\[
a_k=\sum_{j>k}b^{s_k-s_j},\qquad B_k=\sum_{j>k}\eta_jb^{s_k-s_j}.
\]
Choose integers \(Q_k\to\infty\) with \(Q_k\delta_k\to0\). Dirichlet's one-dimensional approximation lemma supplies \(1\le q_k\le Q_k\) with \(\|q_ka_k\|_{\mathbb R/\mathbb Z}\le1/Q_k\). Setting \(n_k=q_kb^{s_k}\) gives
\[
\mathbb E\operatorname{dist}(n_kX,\mathbb Z)
\le Q_k^{-1}+Q_k\mathbb E B_k
\le Q_k^{-1}+\frac{Q_k\delta_k}{b-1}\longrightarrow0.
\]
Therefore \(U^{n_k}\to I\) strongly. Combining the four cases proves both equivalences.

**Non-atomic example and exact return constant.** Take \(s_j=j\) and \(p_j=1/(j+1)\). Every infinite digit sequence has measure zero: after sufficiently many coordinates its point probability is bounded by \(\prod_{j\ge J}(1-p_j)=0\). Injectivity of digit coding gives nonatomicity; all cylinders have positive mass and therefore support is the full Cantor set. With \(n=b^k\), the integer head disappears from the phase. The product formula is
\[
\mathbb E e^{2\pi i b^kX}
=\prod_{h\ge1}\left(1+\frac{e^{2\pi i b^{-h}}-1}{k+h+1}\right).
\]
The summability of \(|e^{2\pi i b^{-h}}-1|\) and the elementary product remainder estimate imply
\[
k\left(\mathbb E e^{2\pi i b^kX}-1\right)
\longrightarrow\sum_{h\ge1}(e^{2\pi i b^{-h}}-1).
\]
Taking \(2-2\operatorname{Re}\) yields the claimed positive finite series. For the fair-digit measure, the bounded-gap/interior-bias case precludes strong rigidity. Both measures are non-atomic and have identical full support, completing the proof.

## Verification
All implications are analytic and hold for infinitely many digits without relying on finite truncation. The only probabilistic input is independent Bernoulli factorization; the endpoint-one case uses a direct one-dimensional pigeonhole approximation. The exact rare-digit coefficient follows by dominated convergence in the absolutely summable product expansion, not by replacing individual phases with small-angle approximations. A supplementary numerical checker of finite products and variance bounds is provided separately; those finite checks do not certify infinite-dimensional assertions.

## Relationship to prior work
Beltrán-Meneu, Galindo and Jordá (2026, arXiv:2611.09186) characterize rigidity and uniform rigidity for multipliers of commutative Banach algebras and characterize Dirichlet spectral ranges on \(C(K)\), but do not give the nonstationary Bernoulli \(L^2\)-multiplier strong-rigidity criterion or the quantitative rare-digit return coefficient. Barbieri, Dikranjan, Giordano Bruno and Weber (2017) give a more general arithmetic-gap characterization of **Dirichlet Cantor sets** (Theorem 1.7, Theorem 4.8), which covers the topological gap phenomenon in related positional constructions: that ingredient is background, **not** a novelty claim. The added classification concerns strong-operator convergence versus uniform convergence for full-support probability measures and the non-atomic same-spectrum contrast. The conventional spectral-theorem reduction to Fourier coefficients is also prior mathematics.

## Limitations
The convergence assumption on \(p_j\) cannot be dropped without a different characterization. The result does not classify strong rigidity for general compactly supported measures, nor ergodic transformations. No independent validation has been performed. Closely related older literature on nonstationary Riesz products may contain equivalent statements; comprehensive historical exclusion is not asserted.

## References
1. M. J. Beltrán-Meneu, J. Galindo and E. Jordá, *Recurrent and rigid multipliers on commutative Banach algebras. The Fourier algebra*, arXiv:2611.09186, first posted 2026-11-06, https://arxiv.org/abs/2611.09186.
2. G. Barbieri, D. Dikranjan, A. Giordano Bruno and H. Weber, *Dirichlet sets vs characterized subgroups*, Topology and its Applications 231 (2017), 50–76, https://doi.org/10.1016/j.topol.2017.08.017.
3. Standard Dirichlet pigeonhole approximation and independent Bernoulli product identities, proved as used above.
