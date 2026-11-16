# Sharp nonzero Walsh gaps for complete-graph spanning trees

## Finding

Let \(n\ge3\), let \(E_n\) be the edges of the complete simple graph on \(n\) labelled vertices, and let \(\mathcal T_n\subseteq\mathbb F_2^{E_n}\) be the edge-incidence vectors of its spanning trees. For every sign assignment \(s\in\{\pm1\}^{E_n}\), define the unnormalized Walsh coefficient
\[
W_n(s)=\sum_{T\in\mathcal T_n}\prod_{e\in T}s_e.
\]
Then the **smallest nonzero absolute Walsh coefficient**, taken over all frequencies, is exactly
\[
\boxed{\min_{s:\,W_n(s)\ne0}|W_n(s)|=\begin{cases}1,&n\text{ odd},\\ 2^{n-2},&n\text{ even}.\end{cases}}
\]
For odd \(n\), every coefficient is nonzero. For even \(n\ge4\), some coefficients vanish and **every** coefficient (including zero) is divisible by \(2^{n-2}\). At least \(\binom{n}{n/2}\) distinct frequencies have coefficient zero when \(n\) is even. All extrema and cancellations have explicit sign witnesses.

Let \(C_n\) be unnormalized convolution on \(\ell^2(\mathbb F_2^{E_n})\) by the indicator of \(\mathcal T_n\). Then \(\|C_n\|_{2\to2}=n^{n-2}\). For odd \(n\), \(C_n\) is invertible, \(\|C_n^{-1}\|_{2\to2}=1\), and \(\kappa_2(C_n)=n^{n-2}\). For even \(n\), \(C_n\) is singular; its Moore--Penrose pseudoinverse has norm \(\|C_n^\dagger\|_{2\to2}=2^{-(n-2)}\), and its positive-spectrum condition number is exactly \(n^{n-2}/2^{n-2}\). Here positive-spectrum condition number means the ratio of the largest to the smallest nonzero singular value, not an invertibility assertion.

## Assumptions and scope

The vertices are individually labelled and the ambient group is the binary edge-incidence space, not the set of trees itself. The Walsh transform is **unnormalized**: the trivial-frequency coefficient equals the number of trees. A frequency is equivalently an arbitrary edge sign assignment; signs on different edges need not be correlated. The theorem applies for every integer \(n\ge3\), with the singular statement restricted to even \(n\ge4\). All determinants and divisibilities are over the integers. There is no claim of a formula for the exact number of vanishing frequencies in the even case.

## Proof

**1. Signed matrix-tree representation.** For any signs \(s_{ij}=s_{ji}\in\{\pm1\}\), form the weighted Laplacian \(L(s)\) with diagonal entries \(L_{ii}=\sum_{j\ne i}s_{ij}\) and off-diagonal entries \(L_{ij}=-s_{ij}\). The weighted matrix-tree identity, valid for arbitrary real or integer weights, says that deleting any row and the same column gives
\[
W_n(s)=\det L(s)^{[v]},
\]
where \(L(s)^{[v]}\) denotes the resulting \((n-1)\)-square matrix. This also identifies the convolution eigenvalues with the displayed Walsh coefficients.

**2. Odd order: no zeros and a unit coefficient.** The ordinary number of labelled spanning trees is \(n^{n-2}\) by the Prüfer correspondence. Reducing each summand defining \(W_n(s)\) modulo two shows
\[
W_n(s)\equiv n^{n-2}\equiv1\pmod2
\]
when \(n\) is odd, so no coefficient can vanish. Choose vertex signs \(x_i\in\{\pm1\}\) with \(\sum_i x_i=1\) (possible for odd \(n\)), and put \(s_{ij}=x_ix_j\). A tree with degrees \(d_i\) then contributes \(\prod_i x_i^{d_i}\). Prüfer coding gives the multivariate Cayley identity
\[
\sum_T\prod_i x_i^{d_i}=\left(\prod_i x_i\right)\left(\sum_i x_i\right)^{n-2},
\]
so the chosen coefficient has absolute value one. This proves the odd minimum.

**3. Even order: uniform divisibility and many zeros.** Suppose \(n\ge4\) is even. In any reduced signed Laplacian of size \(n-1\), every entry is odd: off-diagonals are \(\pm1\), and diagonals sum \(n-1\) odd signs. Thus all rows are congruent modulo two. Subtract its first row from each of the remaining \(n-2\) rows and factor two from each of these rows. The determinant is divisible by \(2^{n-2}\), for every signing.

Choose balanced vertex signs \(x_i\) with \(\sum_i x_i=0\), and again take \(s_{ij}=x_ix_j\). The multivariate Cayley identity makes \(W_n(s)=0\). There are \(\binom n{n/2}/2\) distinct signings of this form, because \(x\) and \(-x\) determine the same edge signs and no other pair does. Negating every edge sign produces equally many further zero frequencies (each spanning tree uses exactly \(n-1\) edges). These two collections are disjoint: if \(x_ix_j=-y_iy_j\) for every distinct pair, then \(z_i=x_iy_i\) would satisfy \(z_iz_j=-1\) for every distinct pair, which is impossible on any three vertices. Hence at least \(\binom n{n/2}\) distinct frequencies vanish.

**4. Even order: sharp attainment.** Start with balanced vertex signs \(x\), arranging \(x_1=1\). Put \(s_{ij}=x_ix_j\) except on the edges of **any fixed spanning tree** \(H\) on the vertex set \(\{2,\dots,n\}\), where signs are reversed. Delete vertex \(1\) from the weighted Laplacian. Writing \(y=(x_2,\ldots,x_n)^\top\), we have \(\sum_i y_i=-1\). The initially balanced factor signing has Laplacian \(-xx^\top\), so its reduced Laplacian is \(-yy^\top\). Reversing the signs on \(H\) adds the weighted Laplacian \(M\) of that tree, with edge weights \(w_{ij}=-2x_ix_j\). Consequently the new reduced Laplacian is \(M-yy^\top\).

Since \(H\) is a tree on \(n-1\) vertices, \(M\) has determinant zero and every cofactor equals \(\prod_{e\in H}w_e\), by the weighted matrix-tree identity. As its rows and columns sum to zero, its adjugate is
\[
\operatorname{adj}(M)=\left(\prod_{e\in H}w_e\right)\mathbf1\mathbf1^\top.
\]
The rank-one determinant identity (which does not require \(M\) to be invertible) therefore gives
\[
\det(M-yy^\top)=\det M-y^\top\operatorname{adj}(M)y
=-\left(\prod_{e\in H}w_e\right)\left(\sum_i y_i\right)^2.
\]
There are \(n-2\) edges in \(H\) and each \(|w_e|=2\), so this determinant has absolute value exactly \(2^{n-2}\). The divisibility lower bound is sharp.

**5. Operator consequences.** The Walsh characters form an orthogonal eigenbasis for convolution on the finite binary group. The unsigned trivial frequency achieves \(|W_n|=|\mathcal T_n|=n^{n-2}\); the triangle inequality bounds every other coefficient by that count. Combining the sharp minimum absolute *nonzero* coefficients with the standard diagonal formulas for inverse and Moore--Penrose pseudoinverse norms gives every operator equality in the Finding.

## Verification

Run `python3 VERIFY.py` with the adjacent standalone Python file; only the Python standard library is needed. This generates all labelled trees independently from Prüfer codes and computes **complete** integer Walsh transforms for \(n=3,4,5,6\), respectively testing \(8,64,1024,32768\) frequencies. The resulting exact nonzero minima are \(1,4,1,16\); zero counts are \(0,30,0,15000\). It separately evaluates integer signed-Laplacian determinants for 50 deterministic pseudorandom signings in every dimension from \(3\) through \(13\), and tests the constructive sharp witnesses for every such dimension. The terminating marker is `COMPLETE_GRAPH_TREE_WALSH_SHARP_CHECKS_PASS`. These are finite consistency checks; the proof above, not the tests, covers unbounded \(n\).

## Relationship to prior work

The matrix-tree theorem, the Prüfer formula, and the **multivariate** Cayley--Prüfer identity are classical and are not claimed here. Martin--Reiner (2003, Section 1 and Section 2) explicitly state the latter identity for arbitrary vertex weights, so it already implies the balanced-sign cancellation and the odd-order unit witness after specialization. Burton--Pemantle (public preprint 2004, Theorems 1.1 and 4.2) determine spanning-tree edge-inclusion marginals via transfer impedances. Dall--Pfeifle (2014, Sections 3--4) treat weighted matroid/graph matrix-tree identities. These works give foundational formulas, but the inspected statements do not assert the **uniform optimal** even-order \(2^{n-2}\) divisibility/gap across *all* independent edge signings or the complete sharp convolution and pseudoinverse norms.

A separately inspected published result, *Quadratic Walsh uniqueness on the spanning-tree slice of a complete graph*, concerns the rank of degree-at-most-two coordinate-Walsh evaluations on the tree set. This is a restricted sampling Gram problem, not the all-frequency convolution multiplier minimum. Its theorem does not imply the claimed gap. Earlier general statements that explicitly imply this specialization remain a priority risk.

## Limitations

The theorem is specific to labelled complete graphs and binary edge characters. It determines the minimum nonzero multiplier and provides a lower bound for the number of zeros at even order; it does **not** classify all even-order zeros or their multiplicities. A minimum spectral gap does not supply sharp endpoint \(\ell^1\) or \(\ell^\infty\) inversion norms. The scientific assessment is self-review only; independent validation has not been performed. Exhaustive historical priority is not established.

## References

1. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, initial public arXiv preprint 2003-02-18, arXiv:math/0302213, especially Section 2. https://arxiv.org/abs/math/0302213
2. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, arXiv preprint 2004-04-02 (journal article 1993), arXiv:math/0404048. https://arxiv.org/abs/math/0404048
3. A. Dall and J. Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, initial public preprint 2014-04-15, arXiv:1404.3876. https://arxiv.org/abs/1404.3876
4. *Quadratic Walsh uniqueness on the spanning-tree slice of a complete graph*, publicly available mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quadratic-walsh-uniqueness-on-the-spanning-tree-slice-of-a-compl--8fece1c0bd0f
