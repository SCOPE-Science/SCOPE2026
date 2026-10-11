# A Dunford--Pettis obstruction to finite-dimensional \(\ell_1\)-models of Lipschitz-free spaces
## Finding
Let \(X\) be a separable Banach space that fails the Dunford--Pettis property. Let \((M_j)_{j\ge1}\) be nonempty metric spaces such that, for every \(j\), there is a finite-dimensional normed space \(E_j\) and a bi-Lipschitz embedding of \(M_j\) into \(E_j\). Then
\[
Z=\left(\bigoplus_{j=1}^{\infty}\mathcal F(M_j)\right)_{\ell_1}
\]
has the Dunford--Pettis property, whereas \(\mathcal F(X)\) does not. Hence \(\mathcal F(X)\) is not isomorphic to a complemented subspace of \(Z\). In particular,
\[
\mathcal F(X)\not\cong
\left(\bigoplus_{j=1}^{\infty}\mathcal F(M_j)\right)_{\ell_1}.
\]
Taking \(M_j=E_j\) for any sequence of finite-dimensional subspaces of \(X\) gives
\[
\mathcal F(X)\not\cong
\left(\bigoplus_{j=1}^{\infty}\mathcal F(E_j)\right)_{\ell_1}.
\]
Thus the finite-dimensional \(\ell_1\)-decomposition obstruction proved in 2026 for \(\ell_p\), \(1<p<\infty\), extends to every separable Banach space failing the Dunford--Pettis property, and the finite pieces need not be linear sections of the source: arbitrary metric spaces with finite-dimensional bi-Lipschitz models are allowed.

## Assumptions and scope
The source space \(X\) is assumed separable because the lifting theorem used below gives a complemented linear copy of \(X\) inside \(\mathcal F(X)\) in that setting. The only property of \(X\) used after lifting is failure of the Dunford--Pettis property.

Each \(M_j\) may have its own finite-dimensional ambient normed space and its own bi-Lipschitz distortion. No uniform bound on dimensions or distortions is needed. The conclusion concerns complemented linear embeddings and linear isomorphism of the resulting Banach spaces; it does not rule out non-complemented embeddings of \(\mathcal F(X)\) into such sums.

A finite-dimensional normed space is linearly isomorphic, hence bi-Lipschitz equivalent, to a Euclidean space of the same dimension. Therefore the hypothesis on \(M_j\) is equivalent to requiring that \(M_j\) be bi-Lipschitz equivalent to a subset of some \(\mathbb R^{d_j}\).

## Proof
Fix \(j\). Choose a bi-Lipschitz embedding
\[
\phi_j:M_j\longrightarrow E_j
\]
into a finite-dimensional normed space, and let \(N_j=\phi_j(M_j)\). After choosing basepoints, \(\phi_j:M_j\to N_j\) is a bi-Lipschitz bijection. Its canonical linearization
\[
\widehat\phi_j:\mathcal F(M_j)\longrightarrow\mathcal F(N_j)
\]
is bounded, and the canonical linearization of \(\phi_j^{-1}\) is its bounded inverse. Hence \(\mathcal F(M_j)\cong\mathcal F(N_j)\).

Let \(d_j=\dim E_j\). Choosing any linear isomorphism \(T_j:E_j\to\mathbb R^{d_j}\) gives a bi-Lipschitz bijection between \(N_j\) and the subset \(T_j(N_j)\subset\mathbb R^{d_j}\). Therefore
\[
\mathcal F(M_j)\cong\mathcal F(T_j(N_j)).
\]
Mason's 2026 Corollary 2 states that \(\mathcal F(M)\) has the Dunford--Pettis property for every nonempty subset \(M\subset\mathbb R^d\). Since the Dunford--Pettis property is invariant under Banach-space isomorphism, every \(\mathcal F(M_j)\) has the Dunford--Pettis property.

The Dunford--Pettis property is preserved by countable \(\ell_1\)-sums. Consequently
\[
Z=\left(\bigoplus_{j=1}^{\infty}\mathcal F(M_j)\right)_{\ell_1}
\]
has the Dunford--Pettis property.

On the other hand, the isometric lifting theorem of Godefroy and Kalton implies that every separable Banach space \(X\) is linearly isometric to a complemented subspace of \(\mathcal F(X)\). If \(\mathcal F(X)\) had the Dunford--Pettis property, then its complemented subspace \(X\) would also have it. Since \(X\) fails the Dunford--Pettis property, \(\mathcal F(X)\) fails it as well.

Finally, suppose \(\mathcal F(X)\) were isomorphic to a complemented subspace of \(Z\). The Dunford--Pettis property passes to complemented subspaces and is invariant under isomorphism, so \(\mathcal F(X)\) would have the Dunford--Pettis property, a contradiction. This proves the complemented-embedding obstruction and therefore the asserted nonisomorphism.

## Verification
The proof is implication-theoretic and uses no numerical experiment. The critical chain is:

1. A bi-Lipschitz bijection of pointed metric spaces linearizes to a Banach-space isomorphism of their Lipschitz-free spaces.
2. Every finite-dimensional normed space is bi-Lipschitz equivalent to Euclidean space of the same dimension.
3. Mason's Theorem 1 and Corollary 2 give the Dunford--Pettis property for free spaces over all subsets of \(\mathbb R^d\).
4. Mason's Lemma 12 records preservation of the Dunford--Pettis property under complemented subspaces and countable \(\ell_1\)-sums.
5. Mason's Lemma 13, using the Godefroy--Kalton lifting theorem, gives failure of the Dunford--Pettis property for \(\mathcal F(X)\) whenever separable \(X\) fails it.

No uniform dimension or distortion estimate is used, so allowing the finite-dimensional models to vary with \(j\) causes no hidden compactness or boundedness assumption.

## Relationship to prior work
Fraser Mason, arXiv:2609.28842v1, proves that \(\mathcal F(\mathbb R^d)\) and, more generally, \(\mathcal F(M)\) for every nonempty \(M\subset\mathbb R^d\), have the Dunford--Pettis property. The same paper proves that for \(1<p<\infty\),
\[
\mathcal F(\ell_p)\not\cong
\left(\bigoplus_{n=1}^{\infty}\mathcal F(\ell_p^n)\right)_{\ell_1}.
\]
The present statement changes both quantifiers: the source is any separable Banach space failing the Dunford--Pettis property, and each summand may come from any metric space admitting a finite-dimensional bi-Lipschitz model. It also strengthens equality obstruction to nonexistence of a complemented embedding into the whole sum.

Candido--Cúth--Doucha, arXiv:1809.09957v2, posed the \(\ell_p\) finite-dimensional decomposition question explicitly as Question 8. Albiac--Ansorena--Cúth--Doucha, arXiv:2005.06555v2, develop broad \(\ell_1\)-sum decompositions and complemented embeddings for Lipschitz-free spaces, but their results do not imply the Dunford--Pettis obstruction above.

## Limitations
The theorem does not decide whether \(\mathcal F(X)\) can embed non-complementedly into a countable \(\ell_1\)-sum of the indicated free spaces. It also does not address source spaces \(X\) that themselves have the Dunford--Pettis property, notably the unresolved case \(X=\ell_1\) highlighted in Mason's 2026 paper. Finally, finite-dimensional bi-Lipschitz embeddability of each metric piece is essential to this proof; the argument does not establish the Dunford--Pettis property for free spaces over arbitrary doubling metric spaces.

## References
1. Fraser Mason, *The Dunford--Pettis property for Lipschitz-free spaces over \(\mathbb R^n\)*, arXiv:2609.28842v1, 2026.
2. Leandro Candido, Marek Cúth, Michal Doucha, *Isomorphisms between spaces of Lipschitz functions*, arXiv:1809.09957v2; J. Funct. Anal. 277 (2019), 2697--2727.
3. Fernando Albiac, José L. Ansorena, Marek Cúth, Michal Doucha, *Lipschitz free spaces isomorphic to their infinite sums and geometric applications*, arXiv:2005.06555v2; Trans. Amer. Math. Soc. 374 (2021), 7281--7312.
4. Gilles Godefroy, Nigel J. Kalton, *Lipschitz-free Banach spaces*, Studia Math. 159 (2003), 121--141.
