# Universal quasinilpotent tails and exact analytic-core order for one-sided damped bilateral shifts

## Finding

For any \(1\le p<\infty\), let \(w=(w_j)_{j\ge1}\) be *any* positive sequence with \(0<w_j\le1\) and \(w_j\to0\); monotonicity is not assumed. On \(X=\ell^p(\mathbb Z;\mathbb C)\), define \(B_w e_j=a_j e_{j+1}\), with \(a_j=1\) for \(j\le0\) and \(a_j=w_j\) for \(j\ge1\). Put \(W_1=1\) and \(W_k=\prod_{j=1}^{k-1}w_j\) for \(k\ge2\). Then \(W_k^{1/k}\to0\).

The analytic core and the quasinilpotent part are exactly
\[
\boxed{\mathcal K(B_w)=\left\{x\in X:\ \exists C>0,\ R\ge1\ \forall k\ge1,\quad |x_k|\le C R^k W_k\right\},}
\]
\[
\boxed{\mathcal H_0(B_w)=\left\{x\in X:\ \lim_{n\to\infty}|x_{-n}|^{1/n}=0\right\}.}
\]
Thus the quasinilpotent part is **independent of the entire positive weight tail**, but the analytic core determines a nontrivial ordering of tails. For any other such sequence \(v\), with \(V_k\) defined analogously,
\[
\boxed{\mathcal K(B_w)\subseteq\mathcal K(B_v)\ \Longleftrightarrow\ \limsup_{k\to\infty}\left(\frac{W_k}{V_k}\right)^{1/k}<\infty.}
\]
Consequently, the two cores are equal exactly when the ratios \(W_k/V_k\) and \(V_k/W_k\) each have bounded exponential growth, equivalently \(|\log W_k-\log V_k|=O(k)\). All these shifts are injective, have nonclosed range and are not pseudo-Fredholm, although both cores are dense proper nonclosed subspaces and
\[\mathcal K(B_w)+\mathcal H_0(B_w)=\mathcal R(B_w)+\mathcal H_0(B_w)=X.\]

For example, \(w_j=2^{-j^2}\) and \(v_j=2^{-j}\) produce \(\mathcal K(B_w)\subsetneq\mathcal K(B_v)\) but exactly the same quasinilpotent part. The vector with positive coefficients \(x_k=2^{-k^2}\) and all nonpositive coefficients zero witnesses strictness.

## Assumptions and scope

The scalar field is complex; coordinate sequences belong to \(\ell^p\) with \(1\le p<\infty\). We use the standard analytic core definition: \(x\in\mathcal K(T)\) when there are \(x^{(n)}\in X\), \(x^{(0)}=x\), \(Tx^{(n+1)}=x^{(n)}\), and constants \(c>0\), \(r>0\) with \(\|x^{(n)}\|\le c r^n\) for all \(n\ge0\). The quasinilpotent part means \(\mathcal H_0(T)=\{x:\lim_{n\to\infty}\|T^n x\|^{1/n}=0\}\), with the zero vector included. The condition \(w_j\to0\) permits arbitrarily slow and nonmonotone decay. Only one half-line carries damping; the opposite half-line has weight one.

## Proof

**1. Superexponential cumulative weights.** For every \(\eta\in(0,1)\), there is \(J\) such that \(w_j\le\eta\) for all \(j\ge J\). Hence \(W_k\le W_J\eta^{k-J}\) for large \(k\). Taking \(k\)-th roots and then letting \(\eta\downarrow0\) gives \(W_k^{1/k}\to0\). In particular, \(\sum_{k\ge1}R^{pk}W_k^p<\infty\) for every fixed \(R\ge1\).

**2. Exact inverse-orbit identity.** All weights are positive, so \(B_w\) is injective. If \(B_w^n y=x\), uniqueness and coefficient comparison force
\[
 y_{k-n}=\begin{cases}
 x_k,&k\le0,\\
 x_k\,W_{\max(k-n,1)}/W_k,&k\ge1.
 \end{cases}
\]
For such \(y\), its \(p\)-th power norm is exactly
\[
\|y\|_p^p=\sum_{k\le0}|x_k|^p+
\sum_{k\ge1}\left|\frac{x_k}{W_k}\right|^p W_{\max(k-n,1)}^p.
\tag{1}
\]
The identity applies whenever the displayed sequence is summable. Since the shift is injective, every possible backward chain is this one.

**3. Analytic core.** If \(x\in\mathcal K(B_w)\), then the predecessor at depth \(n=k-1\) has coordinate \(1\) equal to \(x_k/W_k\). Thus \(|x_k/W_k|\le c r^{k-1}\), and after replacing \(r\) by \(\max(1,r)\) the asserted exponential bound follows. Conversely suppose \(|x_k/W_k|\le C R^k\). For each depth \(n\), the positive-coordinate contribution in (1) is bounded by
\[
 C^p\sum_{k=1}^{n+1}R^{pk}+C^p R^{pn}\sum_{m\ge2}R^{pm}W_m^p,
\]
which grows at most exponentially in \(n\) by step 1. The negative contribution is \(\sum_{k\le0}|x_k|^p\), independent of \(n\). Hence the candidate predecessors lie in \(X\), have exponentially bounded norms, and form a backward chain. This establishes the first box without a uniform lower bound on the weights.

**4. Quasinilpotent part.** The zeroth coordinate of \(B_w^n x\) is \(x_{-n}\). Thus \(x\in\mathcal H_0(B_w)\) implies the displayed root condition. For the converse split \(x=x_-+x_+\) by nonpositive/positive coordinate support. On the positive coordinate subspace, every block of \(n\) consecutive positive weights has at most \(J-1\) exceptional factors exceeding \(\eta\), and all factors are at most one. Therefore \(\|B_w^n|_{X_+}\|\le\eta^{\max(0,n-J+1)}\); the \(n\)-th root tends to zero since \(\eta\) is arbitrary.

For the nonpositive part, write \(x_- = \sum_{m\ge0}x_{-m}e_{-m}\). Its exact forward-orbit norm is
\[
\|B_w^n x_-\|_p^p=
\sum_{m\ge n}|x_{-m}|^p+
\sum_{0\le m<n}|x_{-m}|^pW_{n-m}^p.\tag{2}
\]
Assume \(|x_{-m}|^{1/m}\to0\). For every \(\eta\in(0,1)\), after enlarging a constant \(C_\eta\) to cover finitely many indices, both \(|x_{-m}|\le C_\eta\eta^m\) and \(W_k\le C_\eta\eta^k\) hold for all \(m,k\ge1\). Both sums in (2) are therefore at most a constant times \((n+1)\eta^{pn}\), and so \(\limsup\|B_w^n x_-\|_p^{1/n}\le\eta\). Since \(\eta\) is arbitrary, this root limit is zero. The identity for \(\mathcal H_0\) follows.

**5. Comparison of analytic cores.** If the root limsup of \(W_k/V_k\) is finite, choose \(D>0,S\ge1\) such that \(W_k\le D S^k V_k\) for every \(k\); applying the first box proves inclusion. Conversely take the single positive-half-line vector \(y_k=W_k\) for \(k\ge1\), with zero nonpositive coordinates. Step 1 gives \(y\in X\), and the first box shows \(y\in\mathcal K(B_w)\). The proposed inclusion forces \(W_k/V_k\le C R^k\), proving the root bound. Mutual inclusion gives the logarithmic comparison.

For the strict example, \(\log_2 V_k=-k(k-1)/2\), whereas \(\log_2 W_k=-(k-1)k(2k-1)/6\). The ratios \(W_k/V_k\) are at most one; their reciprocals grow faster than any exponential. For \(x_k=2^{-k^2}\), the quotient \(x_k/V_k=2^{-k(k+1)/2}\) is bounded, whereas \(x_k/W_k=2^{(k-1)k(2k-1)/6-k^2}\) has superexponential growth. This proves the asserted strict inclusion.

**6. Subspace geometry and absence of a generalized Kato decomposition.** Every finitely supported vector belongs to both cores, by the two coefficient tests; hence both are dense. The vector with positive coefficients \(\sqrt{W_k}\) is in \(X\) but not the analytic core, since \(W_k^{-1/2}\) grows superexponentially. The vector with negative coefficients \(x_{-m}=(m+1)^{-2}\) for \(m\ge1\) and other coordinates zero lies in \(X\) for all \(p\ge1\), but not \(\mathcal H_0\), since its root limit is one. Thus both cores are proper and nonclosed. Because \(X_-\subseteq\mathcal K(B_w)\subseteq\mathcal R(B_w)\) and \(X_+\subseteq\mathcal H_0(B_w)\), their two sums are all of \(X\).

The range of \(B_w\) is nonclosed: it is injective and \(\|B_we_j\|=w_j\to0\), contradicting the bounded-below theorem for injective operators with closed range. If \(B_w\) had a generalized Kato decomposition \(X=M\oplus N\) into closed invariant summands with \(B_w|_M\) semi-regular and \(Q=B_w|_N\) quasinilpotent, the bounded commuting projection \(P_N\) would map \(\mathcal K(B_w)\) into \(\mathcal K(Q)=\{0\}\): indeed a quasinilpotent operator cannot have a nonzero vector admitting an exponentially bounded full backward chain, because \(x=Q^n x^{(n)}\) and \(\|Q^n\|^{1/n}\to0\). Density forces \(P_N=0\), so \(N=0\), and semi-regularity would require \(\mathcal R(B_w)\) to be closed, a contradiction. Hence \(B_w\) is not pseudo-Fredholm.

## Verification

The complete argument is analytical. The accompanying standalone `verify.py`, executable with the Python standard library, tests exact product identities for forward and backward coefficient shifts, the predecessor factorization in (1), and the symbolic integer exponents used in the strict comparison example. Running `python verify.py` returns `PASS 2555 exact rational/integer identities; no numerical tolerance`. These finite checks cannot establish the infinite conclusions; the proof above establishes them for arbitrary admissible tails and all \(1\le p<\infty\).

## Relationship to prior work

Mbekhta's 1990 paper and Aznay–Chabbabi's 2026 Section 2 use the particular geometric-exponent damping \(w_j=2^{-j}\) on \(\ell^2\) to demonstrate failure of pseudo-Fredholmness. The latter proves the negative-tail criterion for \(\mathcal H_0\) in that single example (Proposition 2.2); that case is acknowledged, not claimed as new. Miller–Miller–Neumann's 2004 Lemma 1.1 and Proposition 1.2 provide a general backward-orbit/inner-local-spectral-radius characterization, which the analytic-core proof here specializes using a new explicit summation. Bourhim's 2003 preprint studies local spectra and Bishop/Dunford conditions for arbitrary bilateral shifts, not these exact coupled core membership and cross-weight inclusion statements. The contribution here is the **all-weight, all-\(p\)** simultaneous coefficient classification, tail independence, and necessary-and-sufficient comparison of distinct analytic cores. The general backward-orbit characterization is not asserted to be new.

## Limitations

This result does not classify shifts with nonconstant weights on the negative half-line, weights failing to tend to zero, or bilateral shifts with vanishing weights. No spectral theorem for these larger families is claimed. The result gives the exact algebraic cores and their inclusion order, not their normed-space completions or arbitrary local spectral subspaces. A specialized older formulation of the same coefficient-order criterion could exist in the extensive literature on local spectra; no absence of prior work is logically certified by search alone.

## References

1. Z. Aznay and F. Chabbabi, *On Mbekhta's conjecture and pseudo-Fredholm operators on Banach and Hilbert spaces*, arXiv:2610.23229 (first submitted 2026-10-16), Section 2, Propositions 2.1–2.2, https://arxiv.org/abs/2610.23229.
2. M. Mbekhta, *Opérateurs pseudo-Fredholm. I: Résolvant généralisé*, Journal of Operator Theory 24 (1990), 255–276, especially pp. 274–275.
3. T. L. Miller, V. G. Miller and M. M. Neumann, *Local spectral properties of weighted shifts*, Journal of Operator Theory 51 (2004), 71–88, especially Lemma 1.1 and Proposition 1.2; https://jot.theta.ro/jot/archive/2004-051-001/2004-051-001-005.pdf.
4. A. Bourhim, *On the local spectral properties of weighted shift operators*, arXiv:math/0303070, submitted 2003-03-05, Section 4; https://arxiv.org/abs/math/0303070.
