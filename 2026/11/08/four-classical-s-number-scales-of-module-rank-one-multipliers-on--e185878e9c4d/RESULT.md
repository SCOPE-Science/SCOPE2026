# Four classical s-number scales of module-rank-one multipliers on atomic compact-operator algebras

## Finding

Let \(H_j\) (\(j\geq1\)) be nonzero complex Hilbert spaces, each either finite-dimensional or infinite-dimensional and separable, and let
\[
\mathcal A=\bigoplus_{j\geq1}^{c_0}K(H_j),\qquad a=(a_j)\in\mathcal A.
\]
Regard \(\mathcal A\) both as a Banach space with its operator-algebra norm and as the standard right Hilbert \(\mathcal A\)-module. Put \(L_a(x)=ax\). If \(d_j=\dim H_j<\infty\), write \(s_1(a_j)\geq\cdots\geq s_{d_j}(a_j)\geq0\) for the ordinary Hilbert-space singular values. Define, for every \(t>0\),
\[
N_a(t)=\sum_{j:d_j<\infty}d_j\#\{1\leq\ell\leq d_j:s_\ell(a_j)>t\},\quad
q_n(a)=\sup\bigl(\{t>0:N_a(t)\geq n\}\cup\{0\}\bigr),
\]
and
\[
\gamma(a)=\sup_{j:\dim H_j=\infty}\|a_j\|,\qquad \sup\varnothing=0.
\]
The count \(N_a(t)\) is finite for every positive \(t\). For each integer \(n\geq1\), all **four classical Banach-space** s-numbers of \(L_a\) agree exactly:
\[
\boxed{a_n(L_a)=b_n(L_a)=c_n(L_a)=d_n(L_a)
=\max\{q_n(a),\gamma(a)\}.}
\]
Here these are, respectively, approximation, Bernstein, Gelfand and Kolmogorov numbers, using the strict convention \(\operatorname{rank},\operatorname{codim},\dim<n\).

Every \(L_a\) is **representable by one elementary Hilbert-module operator of rank at most one** \(\theta_{x,y}(z)=x\langle y,z\rangle\), regardless of its classical Banach-space rank. Nevertheless,
\[
\boxed{
\operatorname{dist}(L_a,\mathcal K)
=\operatorname{dist}(L_a,\mathcal{FSS})
=\operatorname{dist}(L_a,\mathcal{SS})
=\gamma(a).}
\]
Thus \(L_a\) is classically compact if and only if \(a_j=0\) at every infinite-dimensional summand. The ideals on the displayed line are ideals of maps on the underlying Banach space, not of module maps.

## Assumptions and scope

All norms on \(M_d(\mathbb C)\) and \(K(H)\) are **operator norms**, not Hilbert–Schmidt norms. The algebra is the countable \(c_0\)-sum; in particular \(\|a_j\|\to0\). Each finite block has its own dimension \(d_j\), possibly unbounded across \(j\); infinite blocks need not be absent. The singular values in \(N_a(t)\) are repeated \(d_j\) times because a singular row contributes \(d_j\) independent columns. Infinite-dimensional summands contribute the flat floor \(\gamma(a)\), even when \(a_j\) has finite rank as an operator on \(H_j\).

The standard four s-number definitions for a bounded map \(T:X\to Y\) are
\[
\begin{aligned}
a_n(T)&=\inf_{\operatorname{rank}R<n}\|T-R\|,\\
b_n(T)&=\sup_{\dim E=n}\inf_{\substack{x\in E\\\|x\|=1}}\|Tx\|,\\
c_n(T)&=\inf_{\operatorname{codim}E<n}\|T|_E\|,\\
d_n(T)&=\inf_{\dim F<n}\|Q_FT\|,
\end{aligned}
\]
where \(Q_F:Y\to Y/F\) carries the quotient norm. When the ambient dimension is smaller than \(n\), use the usual zero-tail convention.

## Proof

**1. Exact finite-mode row spaces.** Fix \(t>0\). There are only finitely many \(j\) with \(\|a_j\|>t\), because \(a\in\mathcal A\). For each *finite-dimensional* such block, take the right singular projection \(P_j\) of \(|a_j|\) onto singular values greater than \(t\). Let \(Q_j\) be the range projection of \(a_jP_j\). Both projections have rank \(r_j=\#\{\ell:s_\ell(a_j)>t\}\). The row spaces
\[
E_t=\bigoplus_{j:d_j<\infty}P_jM_{d_j},\qquad
F_t=\bigoplus_{j:d_j<\infty}Q_jM_{d_j}
\]
are finite-dimensional, of common dimension \(N_a(t)=\sum_jr_jd_j\). The direct sum is over the finitely many nonzero projections. Left multiplication by \(a\) maps \(E_t\) bijectively onto \(F_t\), and
\[
\|L_ax\|\ge t\|x\|\quad(x\in E_t).
\]
Indeed, the smallest singular value on each chosen right singular space is strictly greater than \(t\), and the operator norm satisfies \(\|a_jX_j\|\ge t\|X_j\|\) whenever the range of \(X_j\) lies in \(P_jH_j\). The left-corner map \(x\mapsto(Q_jx_j)_j\), extended by zero on all other blocks, is a projection of norm at most one from \(\mathcal A\) onto \(F_t\).

**2. Infinite-dimensional rows.** If \(\dim H_j=\infty\) and \(t<\|a_j\|\), choose a unit \(u\in H_j\) with \(\|a_ju\|>t\). The subspace of operators supported at block \(j\) of the form \(u\otimes v^*\), \(v\in H_j\), is an infinite-dimensional Hilbertian subspace \(E\) of \(\mathcal A\). It is mapped by \(L_a\) onto the analogous row space \(F\) with normalized first vector \(a_ju/\|a_ju\|\), scaled by \(\|a_ju\|>t\). The target row space \(F\) is contractively complemented in \(\mathcal A\) by its rank-one left range projection.

**3. Four lower bounds from one complemented witness.** Suppose \(E\) is a subspace of dimension at least \(n\), \(T:E\to F=T(E)\) is onto and \(\|Tx\|\ge t\|x\|\), and \(F\) admits a contractive projection from the whole codomain. Rank-\(<n\) maps and codimension-\(<n\) subspaces have nonzero intersection with an \(n\)-dimensional subspace of \(E\); hence \(a_n(T_{\mathrm{full}}),c_n(T_{\mathrm{full}})\ge t\). Choosing that subspace directly yields \(b_n(T_{\mathrm{full}})\ge t\). For Kolmogorov numbers, \(T(B_E)\) contains \(tB_F\): its inverse on \(F\) has norm at most \(1/t\). Given a subspace \(Z\) of the entire codomain with \(\dim Z<n\), the contractive projection onto \(F\) reduces the distance to \(Z\) to distance in \(F\) from a subspace of dimension \(<n\). The unit-ball Kolmogorov width in any normed space of dimension at least \(n\) is one (the quotient norm and Riesz's lemma). Therefore \(d_n(T_{\mathrm{full}})\ge t\).

Apply this to Step 1 whenever \(N_a(t)\ge n\), and to Step 2 for any \(t<\gamma(a)\). Allow \(t\) to approach \(q_n(a)\) and \(\gamma(a)\) from below. We obtain all four lower bounds by \(\max\{q_n(a),\gamma(a)\}\).

**4. Matching finite-rank approximant.** Fix \(t>\max\{q_n(a),\gamma(a)\}\). On every infinite-dimensional block set the approximating symbol to zero. On each finite-dimensional block retain only singular summands with singular value strictly larger than \(t\). These form finitely many blocks, and the corresponding left multiplier \(R_t:\mathcal A\to\mathcal A\) has classical rank exactly \(N_a(t)<n\), because its range is the direct sum of its active output row spaces. The remaining operator has norm at most \(t\) on each finite block, and at most \(\gamma(a)<t\) on each infinite block. Therefore \(a_n(L_a)\le t\). Let \(t\downarrow\max\{q_n(a),\gamma(a)\}\); the common formula follows from Steps 3–4 and the elementary upper bounds of the other three s-number scales by \(a_n\).

**5. Module rank one.** For each \(j\), let \(a_j=u_j|a_j|\) be its polar decomposition on \(H_j\). Set
\[
x_j=u_j|a_j|^{1/2},\qquad y_j=|a_j|^{1/2}.
\]
Because \(a_j\) is compact and \(\|a_j\|\to0\), both \(x=(x_j)\) and \(y=(y_j)\) belong to \(\mathcal A\). In the right standard Hilbert module, \(\langle y,z\rangle=y^*z\), so
\[
\theta_{x,y}(z)=xy^*z=az=L_a(z).
\]
Thus \(L_a\) is a single elementary module operator (module rank at most one), even if it is not compact on the underlying Banach space.

**6. Exact classical ideal distances.** As \(n\to\infty\), \(q_n(a)\to0\): above every positive cutoff only finitely many finite-dimensional modes survive. Consequently \(\lim_n a_n(L_a)=\gamma(a)\). Since the underlying Banach-space maps are norm limits of finite-rank truncations exactly when \(\gamma(a)=0\), the distance to classical compact maps equals \(\gamma(a)\). More explicitly, erase all infinite-dimensional blocks and keep finitely many finite-dimensional blocks to approximate \(L_a\) within \(\gamma(a)+\varepsilon\) by a finite-rank map. For the reverse bound to **strictly singular** maps, Step 2 supplies an infinite-dimensional subspace on which \(L_a\) is bounded below by any \(t<\gamma(a)\); a strictly singular perturbation cannot be bounded below on this same subspace. Hence its distance from \(L_a\) is at least \(t\), then at least \(\gamma(a)\). The inclusions \(\mathcal K\subseteq\mathcal{FSS}\subseteq\mathcal{SS}\) give all three equalities.

**Example (cubic multiplicity).** Take \(H_j=\mathbb C^j\), \(a_j=j^{-\sigma}I_j\), for any \(\sigma>0\). Then \(\gamma(a)=0\) and the value \(j^{-\sigma}\) occurs \(j^2\) times among the four equal s-number sequences. Since \(\sum_{j\leq J}j^2\sim J^3/3\), the common s-number sequence satisfies
\[
\boxed{a_n(L_a)\sim(3n)^{-\sigma/3}.}
\]
In contrast, a single infinite-dimensional \(K(H)\) block with any nonzero compact symbol already forces a positive flat floor for every s-number.

## Verification

Run `python3 CHECK.py` in a directory containing this document and the accompanying checker. The checker uses rational arithmetic and performs exact finite-block row-count, truncation-rank, cutoff, and Frobenius-energy corroborations; its successful marker is `MATRIX_MODULE_ROWS_EXACT_OK 70357`. The infinite-dimensional complementability, four s-number lower bounds and module factorization are analytic proofs above, not consequences of finite testing.

## Relationship to prior work

Fufaev (arXiv:2610.39164v1, first posted October 29, 2026) studies geometric/seminorm criteria for compactness notions in Hilbert \(C^*\)-modules, rather than classical s-number sequences of left multipliers on atomic compact-operator algebras. In that work **“Banach-compact” denotes the closure of module maps \(\theta_{x,f}\) for bounded module functionals**, not compactness of maps between underlying Banach spaces; these notions are not conflated here.

Anoussis–Felouzis–Todorov (arXiv:0811.3848v1) study s-number membership in stable Calkin classes for elementary \(ax b\) operators on \(C^*\)-algebras. Their statements do not yield the simultaneous exact four-number, each-index expression here, and ordinary left multiplication by \(a\) on this nonunital algebra cannot be represented as \(M_{a,b}\) with a right identity coefficient \(b\in\mathcal A\).

The published results *Flat classical s-number profiles for one-sided multiplication on symmetric norm ideals* (September 20, 2026) and *Exact s-number profiles for finite-fiber multiplication operators* (September 20, 2026) provide pertinent limiting analogues. The former concerns a **single infinite-dimensional symmetric operator ideal**, whose one-sided s-number sequence is flat; the latter concerns **Bochner \(L^p\) spaces with Euclidean finite fibers**, not operator-norm matrix-algebra fibers. Neither covers the hybrid direct-sum classification with matrix-size multiplicities, the exact classical/ module-compactness gap, or the finite/infinite boundary in one formula.

## Limitations

The theorem is specific to countable \(c_0\)-sums of full compact-operator algebras, and only to one-sided left multipliers. It does not address non-atomic \(C^*\)-algebras, arbitrary two-sided elementary maps, or general Hilbert modules. The four s-numbers here are the *classical Banach-space* scales, not module-defined approximation quantities. The exact formulas have a complete analytical proof, but the publication-priority assessment is to the best of our knowledge: older general operator-ideal and diagonal-block approximation literature could contain an equivalent formulation under different language. No independent mathematical audit has been performed.

## References

1. D. V. Fufaev, *Locally unital \(C^*\)-algebras and limitations of seminorm criteria for compact operators*, arXiv:2610.39164v1 (October 29, 2026). https://arxiv.org/html/2610.39164v1
2. M. Anoussis, V. Felouzis and I. G. Todorov, *S-numbers of elementary operators on C*-algebras*, arXiv:0811.3848v1 (November 24, 2008). https://arxiv.org/abs/0811.3848
3. *Flat classical s-number profiles for one-sided multiplication on symmetric norm ideals*, published published-finding corpus record (September 20, 2026), suffix `0a8586db5330`. https://github.com/published-finding corpus/2026
4. *Exact s-number profiles for finite-fiber multiplication operators*, published published-finding corpus record (September 20, 2026), suffix `fe72e16da558`. https://github.com/published-finding corpus/2026
5. M. Ullrich, *Inequalities between s-numbers*, Advances in Operator Theory 9 (2024), 82. https://doi.org/10.1007/s43036-024-00386-x
