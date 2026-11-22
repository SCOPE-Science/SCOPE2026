# Sharp phase-sensitive mutual-link perturbation over disjoint tetrahedron-free hyperedges

## Finding
Let \(M\) be the countable homogeneous \(K_4^{(3)}\)-free \(3\)-uniform hypergraph. Individually name a base \(A_{n,t}\) of \(n\) vertices whose induced triples form a matching of \(t\) pairwise vertex-disjoint triples, with all other triples absent; thus \(0\le t\le\lfloor n/3\rfloor\). Consider complete types over this base of **ordered, distinct, nonparameter** vertices \((x,y)\), chosen uniformly from the finite set of types. Let \(K_{n,t}\) count those named vertices \(a\) satisfying \(R(x,y,a)\), and let \(T_{n,t}\) count all such types.

Define \(q=3/4\), \(b=\log(4/3)\), \(a=160/147\), \(c=1600/1323\), and \(\eta_0=\eta_1=1,\ \eta_2=a,\ \eta_3=c\). For a subset \(S\subseteq A_{n,t}\), put \(s_i=|S\cap B_i|\), where \(B_i\) are the disjoint named hyperedges, and \(Z(S)=\prod_{i=1}^t\eta_{s_i}\). Then the **exact number of pair types with the specified mutual-link set \(S\)** is
\[
N_{n,t}(S)=4^{\binom n2}(49/64)^t q^{\binom{|S|}{2}}Z(S).
\]
This expression is an integer, as is transparent from its local-pattern derivation below. In particular, if \(K_{n,0}\) is the mutual-link size for the *empty* induced base on the same number of vertices and \(\mu_n\) is the associated law on subsets,
\[
\boxed{\frac{T_{n,t}}{(49/64)^tT_{n,0}}=\mathbb E_{\mu_n}Z(S).}
\]
The factor \((49/64)^t\) represents a potentially exponential loss in the total pair-type count. Nevertheless, **uniformly for every choice of \(1\le t\le\lfloor n/3\rfloor\)** as \(n\to\infty\),
\[
\boxed{\frac{T_{n,t}}{(49/64)^tT_{n,0}}
=1+\frac{13}{49b^2}\frac{t(\log n)^2}{n^2}(1+o(1)).}
\]
In particular, the leading correction is positive and is sharp even when \(t\) is fixed. It arises from the rare event that a mutual-link set contains *two* vertices of the same named hyperedge.

There is also a **sharp total-variation perturbation law**, rather than just convergence to the same limiting shape. Let \(\rho_n\) be the unique solution in \((0,n)\) of
\[
\frac{n-\rho_n}{\rho_n+1}q^{\rho_n}=1,
\qquad m_n=\lfloor\rho_n\rfloor,\quad\delta_n=\rho_n-m_n.
\]
For \(\delta\in[0,1]\), define the discrete Gaussian on \(\mathbb Z\) by
\[
\pi_\delta(j)=\frac{\exp[-\tfrac b2(j-\delta-1/2)^2]}{\sum_{h\in\mathbb Z}\exp[-\tfrac b2(h-\delta-1/2)^2]},
\quad \alpha(\delta)=\mathbb E_{\pi_\delta}|J-\mathbb E_{\pi_\delta}J|.
\]
Then \(\alpha\) is continuous, strictly positive, and invariant under the identification of the endpoint phases, and
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(K_{n,t}),\mathcal L(K_{n,0})\bigr)
=\frac{13}{49}\frac{t m_n}{n^2}\alpha(\delta_n)(1+o(1)),}
\]
uniformly for \(1\le t\le\lfloor n/3\rfloor\). In particular, the two link-size laws are asymptotically indistinguishable, but the *first nonvanishing discrepancy* retains the lattice phase of the empty-base link law. No claim of a single phase-independent constant is made.

## Assumptions and scope
The language has a symmetric irreflexive ternary predicate \(R\), and \(K_4^{(3)}\) means **all four** possible triples on a four-element set; it does not mean the three-edge incomplete tetrahedron. Every named parameter is fixed pointwise. A complete pair type is identified with its full finite relational diagram by the finite-extension property and ultrahomogeneity, not with a uniformly sampled pair of actual vertices of the infinite structure. The base matching is an induced matching: its \(t\) triples are mutually vertex-disjoint and there are no other old hyperedges. The empty-base-on-\(n\)-vertices comparison \(T_{n,0}\) uses the same \(n\) named labels but no old hyperedges.

## Proof
**1. All admissibility constraints.** For each old pair \(\{u,v\}\), let \(X_{uv}=\mathbf1_{R(x,u,v)}\) and \(Y_{uv}=\mathbf1_{R(y,u,v)}\); let \(W_u=\mathbf1_{R(x,y,u)}\), and \(S=\{u:W_u=1\}\). Every forbidden four-set contains zero, one or two new vertices. Zero new vertices are allowed by the definition of the base. One new vertex and a named hyperedge \(B_i=\{u,v,w\}\) form a forbidden four-set exactly if the corresponding three \(X\)-bits (or three \(Y\)-bits) are all one. With two new vertices and two named vertices \(u,v\), the forbidden condition is exactly \(X_{uv}=Y_{uv}=W_u=W_v=1\). There are no other constraints. Every surviving diagram is realized as a complete pair type by the Fraïssé extension property.

**2. Exact block factors.** Fix \(S\), and let \(s=|S\cap B_i|\). Among the three old pairs internal to \(B_i\), the possible \(X\)- and \(Y\)-bits must each avoid the all-one vector. If \(s=0\) or \(1\), there are \(7^2=49\) patterns. If \(s=2\), precisely one old pair must avoid \((X,Y)=(1,1)\), so there are \(49-3^2=40\) patterns. If \(s=3\), all three pairs must avoid joint \((1,1)\): from the \(3^3=27\) possibilities remove the two forbidden cases where one entire vector is all ones and the other is all zeros, giving \(25\). Write these four counts as \(w=(49,49,40,25)\). Every other old pair independently contributes three patterns if both endpoints belong to \(S\), and four otherwise. Consequently, with \(k=|S|\), the exact integer count is
\[
3^{\binom k2-\sum_i\binom{s_i}{2}}
4^{\binom n2-\binom k2-3t+\sum_i\binom{s_i}{2}}
\prod_{i=1}^t w_{s_i}.
\]
Factoring out the empty-induced-base count \(4^{\binom n2}q^{\binom k2}\), each hyperedge contributes \(w_s/[3^{\binom s2}4^{3-\binom s2}]\), which equals \(49/64\) for \(s\le1\), \(5/6\) for \(s=2\), and \(25/27\) for \(s=3\). Dividing by \(49/64\) yields \(\eta_2=160/147\) and \(\eta_3=1600/1323\), proving the exact formula.

Equivalently, if \(h_{n,t}(k)=\mathbb E[Z(S)\mid |S|=k]\) when \(S\) is a uniform \(k\)-subset, then \(h_{n,t}(k)\) is the coefficient of \(z^k\) in
\[
(1+3z+3az^2+cz^3)^t(1+z)^{n-3t}
\]
divided by \(\binom nk\). This provides a finite, exact coefficient algorithm independent of the infinite structure.

**3. Rare double hits, with uniform errors.** Put \(d=a-1=13/147\) and \(e=c-1\). For a uniform \(k\)-subset of \(n\) vertices, a specified old triple is hit in exactly two points with probability \(3(k)_2/(n)_2-3(k)_3/(n)_3\), and in all three with probability \((k)_3/(n)_3\), where \((r)_j=r(r-1)\cdots(r-j+1)\). Expand the product \(Z(S)\) into its linear terms in the block-hit indicators and its terms involving at least two distinct hit blocks. For \(k\le L_n=\lceil20\log n\rceil\), a union bound over two chosen vertices per hit block and a binomial expansion bound the latter terms by \(O(t^2k^4/n^4)\). Thus, uniformly over \(0\le t\le n/3\) and \(k\le L_n\),
\[
\boxed{h_{n,t}(k)=1+\frac{13}{49}\,\frac{t(k)_2}{(n)_2}
+O\!\left(\frac{tk^3}{n^3}+\frac{t^2k^4}{n^4}\right).}
\]
The constants in the big-O are absolute for all sufficiently large \(n\). The same expansion covers \(t=0\), when every correction vanishes.

For rigorous tail control, note \(c\le a^3\), so \(Z(S)\le a^{\binom k2}\). The unnormalized \(k\)-weight after the perturbation is at most \(\binom nk(qa)^{\binom k2}\), with \(qa=40/49<1\). Since \(\binom nk\le n^k\), the sum over \(k>20\log n\) is superpolynomially small compared with the baseline partition function (which is at least one). This allows every preceding uniform expansion to be averaged over the full baseline law without losing its order.

**4. Sharp type-count correction.** The empty-base law has weights \(\binom nkq^{\binom k2}\). Their successive ratio \((n-k)q^k/(k+1)\) is decreasing; its real unit-ratio location is \(\rho_n\sim(\log n)/b\). Successive ratios also yield bounded, uniformly sub-Gaussian fluctuations around \(m_n\). In particular,
\[
\mathbb E_0[(K_{n,0})_2]\sim\frac{(\log n)^2}{b^2}.
\]
Averaging the expression in step 3 gives
\[
\mathbb E_0 Z(S)=1+\frac{13}{49}\frac{t}{(n)_2}\mathbb E_0[(K_{n,0})_2]
+O\!\left(\frac{t(\log n)^3}{n^3}+\frac{t^2(\log n)^4}{n^4}\right).
\]
For every \(1\le t\le n/3\), the error is \(o(t(\log n)^2/n^2)\), proving the asserted uniform multiplicative asymptotic.

**5. Sharp total variation and the residual phase.** Because the perturbation depends on \(S\) only through the symmetric block-hit counts, the law of \(K_{n,t}\) is the \(h_{n,t}(k)\)-tilt of the empty-base law. Subtract the normalization of this tilt, use step 3 and the baseline tail control, and obtain, uniformly for \(1\le t\le n/3\),
\[
d_{\mathrm{TV}}(\mathcal L(K_{n,t}),\mathcal L(K_{n,0}))
=\frac{13}{98}\frac{t}{(n)_2}\mathbb E_0\big| (K_{n,0})_2-\mathbb E_0 (K_{n,0})_2\big|
+o(t\log n/n^2).
\]
The baseline ratio calculation also proves, uniformly in the varying fractional phase \(\delta_n\), total-variation convergence of \(J_n=K_{n,0}-m_n\) to \(\pi_{\delta_n}\), with uniform moments of every fixed order. Since \(m_n\sim(\log n)/b\), expanding \((m_n+J_n)_2\) shows
\[
\mathbb E_0\big|(K_{n,0})_2-\mathbb E_0(K_{n,0})_2\big|
=2m_n\alpha(\delta_n)(1+o(1)).
\]
The factor \(2\) cancels the \(1/2\) in total variation, giving the stated sharp asymptotic. Positivity and phase continuity follow from the nondegenerate Gaussian-type lattice weights, whose tails are uniformly summable.

## Verification
Run the accompanying `verify.py` using the Python standard library. It **directly** exhausts all relational assignments of two new vertices for named bases with up to four vertices, with either zero or one old hyperedge, and compares the resulting coefficient vector to the exact factorization. It verifies the local block counts and the formulas for two disjoint old hyperedges on six vertices by evaluating all mutual-link subsets with the coefficient algorithm. Numerical checks at four larger sizes compare the exact polynomially computed type-count correction and total-variation distance with their first-order asymptotic formulas. The saved `verification_output.txt` ends in `VERIFY_OK`. These tests confirm finite instances and do not replace the unrestricted argument above.

## Relationship to prior work
Conant's *An axiomatic approach to free amalgamation* (arXiv:1505.00762, first posted 4 May 2015), §3, supplies the Fraïssé setting and identifies the generic complete-hypergraph-free age; it does not compute the present matched-base two-point law. The previously available empty-induced-base pair-link theorem supplies the weights \(\binom nk(3/4)^{\binom k2}\) and their discrete-Gaussian lattice phases, but expressly excludes nonempty induced parameter hypergraphs. The previously published *Sharp overlap-matching bounds for one-point types of the generic tetrahedron-free 3-hypergraph* concerns **single** new vertices and old triple intersections; its bound does not give the new two-point mutual-link tilt or the sharp phase-dependent total variation rate. Standard hypergeometric collision probabilities and discrete-Gaussian saddle-point arguments are acknowledged tools, not claimed as methodological innovations.

The new object is the **nonempty induced matching base**, and the new statements are its exact four-weight local correction (including \(49,49,40,25\)), its uniform sharp all-size type-count correction, and its first-order total variation perturbation with an explicit lattice-phase-dependent amplitude. No comprehensive historical uniqueness assertion is made: unindexed specializations of cluster-weighted random-graph partition functions remain a priority risk.

## Limitations
The named hyperedges must be vertex-disjoint; overlapping old hyperedges and arbitrary finite bases require different local dependency calculations. The result concerns complete **ordered injective two-point types**, with uniformly counted types, not actual randomly sampled vertices. The total-variation rate applies only to the scalar mutual-link size, not automatically to the full two-point type distribution. The phase oscillation is inherited from an established empty-base limiting law, while the perturbation constant and the matching-base reduction are the present claims. The proof is an all-size argument; finite checks are not treated as exhaustive across all \(n\). No independent mathematical audit or historical-priority certification has been performed.

## References
1. G. Conant, *An axiomatic approach to free amalgamation*, arXiv:1505.00762, first public version 4 May 2015, especially §3. https://arxiv.org/abs/1505.00762 .
2. *A discrete-Gaussian pair-link law for tetrahedron-free homogeneous hypergraphs*, previously published mathematical research record, finding `560b4959-b606-475a-b329-4c73e0a9f066` (empty induced base, exact mutual-link law and lattice phases).
3. *Sharp overlap-matching bounds for one-point types of the generic tetrahedron-free 3-hypergraph*, previously published mathematical research record, finding `5ae2c902-29c3-4f68-a194-53526b7753d9` (one-point constraints and matching-overlap inequalities). https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-sharp-overlap-matching-bounds-for-one-point-types-of-the-generic--5ae2c90229c3/RESULT.md .
