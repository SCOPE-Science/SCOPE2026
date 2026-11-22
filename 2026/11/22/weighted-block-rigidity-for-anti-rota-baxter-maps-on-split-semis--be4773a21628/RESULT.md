# Weighted-block rigidity for anti–Rota–Baxter maps on split semisimple algebras

## Finding
Let \(k\) be a field and \(A=k^n\), \(n\ge1\), with coordinatewise multiplication. A linear operator \(R:A\to A\) is an *anti–Rota–Baxter operator* if
\[
R(x)R(y)=-R(R(x)y+xR(y))\qquad(x,y\in A).
\]
If \(\operatorname{char}k\ne3\), the zero map is the unique such operator. In characteristic three, the entire operator set has the following *unique weighted-block normal form*.

Choose a subset \(U\subseteq\{1,\ldots,n\}\) of *active* coordinates, partition it into nonempty, pairwise disjoint, unordered blocks \(C_1,\ldots,C_r\), and assign each inactive coordinate to one of these blocks or leave it unassigned. Write \(S_j\supseteq C_j\) for the resulting disjoint augmented supports; all coordinates in \(S_j\setminus C_j\) are inactive, and all active coordinates belong to exactly one \(C_j\). Choose nonzero weights \(d_s\in k^\times\) for \(s\in U\). Then every operator, and no other operator, is
\[
R(x)=\sum_{j=1}^r\Big(\sum_{s\in C_j}d_s x_s\Big)\mathbf1_{S_j},
\]
where \(\mathbf1_S\) is the coordinate indicator of \(S\). The rank of this operator is exactly \(r\). The empty configuration gives \(R=0\). For all \(R\) in this family,
\[
R(R(x)y)=R(x)R(y)=R(xR(y)).
\]
The strong identity \(R(x)R(y)z=xR(y)R(z)\) holds precisely for diagonal anti–Rota–Baxter maps.

For \(k=\mathbb F_q\) with \(q\) a power of three, the number of labeled operators of linear rank \(r\), for each \(0\le r\le n\), is
\[
N_{n,r}(q)=\sum_{a=r}^n\binom na\left\{\!\!\begin{matrix}a\\r\end{matrix}\!\!\right\}(r+1)^{n-a}(q-1)^a
=\frac1{r!}\sum_{j=0}^r(-1)^{r-j}\binom rj\big(r+1+j(q-1)\big)^n.
\]
Here the brace denotes a Stirling number of the second kind, and \(N_{n,0}(q)=1\). Consequently,
\[
\sum_{n\ge0}\sum_{r=0}^nN_{n,r}(q)u^r\frac{z^n}{n!}
=\exp\big(z+u(e^{qz}-e^z)\big).
\]
Every rank \(0,\ldots,n\) occurs. Exactly \((q-1)^n\) are invertible, and exactly \(q^n\) satisfy the strong identity.

The square-zero subfamily has its own exact bivariate exponential generating function:
\[
\sum_{n\ge0}\sum_{r\ge0}Z_{n,r}(q)u^r\frac{z^n}{n!}=
\exp\left(z+\frac{ue^z}{q}\left[e^{(q-1)z}-1+(q-1)(e^{-z}-1)\right]\right),
\]
where \(Z_{n,r}(q)\) counts the operators with \(R^2=0\) and rank \(r\). If \(\operatorname{char}\mathbb F_q\ne3\), all the above counts reduce to the sole zero operator, rather than the displayed characteristic-three formulas.

## Assumptions and scope
All algebras here are the split unital coordinate product \(k^n\), with their primitive coordinate idempotents labeled. The theorem holds over arbitrary fields without an algebraic-closure or infinitude assumption. The finite-field generating functions are formal power series in \(z\) with rational integer coefficients. No classification of non-split étale algebras, noncommutative algebras, or automorphism-conjugacy classes is asserted.

## Proof
Write \(e_s\) for the coordinate idempotents, and \(R(e_s)=\sum_i r_{is}e_i\). By bilinearity it is necessary and sufficient to test the defining identity on all \((e_s,e_t)\); its coefficient at \(e_i\) is
\[
r_{is}r_{it}+r_{it}r_{ts}+r_{is}r_{st}=0\qquad(1\le i,s,t\le n).\tag{1}
\]
Taking \(i=s=t\) gives \(3r_{ss}^2=0\). Taking \(s=t\) gives \(r_{is}^2+2r_{is}r_{ss}=0\). In characteristics other than three all diagonal entries vanish, hence every entry vanishes and \(R=0\).

Now assume characteristic three. Put \(d_s=r_{ss}\). The second equation becomes \(r_{is}(r_{is}-d_s)=0\). Thus every column with \(d_s=0\) is zero, while every active column with \(d_s\ne0\) has entries in \(\{0,d_s\}\) and contains its diagonal position \(s\). For distinct active indices \(s,t\), equation (1) with \(i=s\) implies \(r_{st}\ne0\Rightarrow r_{ts}=d_s\); the same equation with \(i=t\) gives the converse. Consequently any pair of active columns either has both cross entries nonzero or has both zero.

In the first case the two cross entries equal \(d_t,d_s\). Equation (1), at each output coordinate, then reads \(r_{is}r_{it}+d_s r_{it}+d_t r_{is}=0\). Since each entry is zero or its column weight, this forces the supports of the two columns to coincide. In the second case equation (1) reduces to \(r_{is}r_{it}=0\), hence their supports are disjoint. The active indices therefore partition into classes of identical-support columns, distinct classes having disjoint supports. Each such support contains precisely its class's active indices and may contain any disjoint collection of inactive indices. This is the claimed unique weighted-block form. Conversely, for two columns in the same block each term in (1) equals the product of their nonzero weights, so the sum is zero because the characteristic is three. For columns in different blocks every term is zero. Thus the normal form is sufficient.

Each image indicator \(\mathbf1_{S_j}\) is supported on a set disjoint from the others, and each block contains an active column. Hence the image indicators are independent and the rank is \(r\). Since multiplication of indicators from distinct blocks is zero, direct substitution into the normal form gives \(R(R(x)y)=R(x)R(y)=R(xR(y))\). Taking \(x=y=e_s\), \(z=e_i\), with \(i\ne s\), in the strong identity forces \(r_{is}^2=0\). Thus strong operators have no off-diagonal entries. Conversely every diagonal anti–Rota–Baxter operator is strong. Every rank-\(n\) configuration has \(n\) singleton active blocks with no inactive coordinates, hence is an invertible diagonal map.

To count rank \(r\) over \(\mathbb F_q\), choose \(a\) active coordinates, partition them into \(r\) nonempty blocks, choose \((q-1)^a\) nonzero weights, and assign each of the remaining \(n-a\) coordinates to one of the \(r\) blocks or to no block. This yields the first formula for \(N_{n,r}(q)\), with no overcounting by uniqueness. Labeled combinatorial exponential enumeration assigns the factor \(e^z\) to unassigned coordinates and \(e^z(e^{(q-1)z}-1)=e^{qz}-e^z\) to each nonempty weighted block, proving the exponential generating function. Expanding its rank-\(r\) coefficient yields the alternating closed formula.

Finally, applying \(R\) again to \(\mathbf1_{S_j}\) multiplies this indicator by \(\sum_{s\in C_j}d_s\). Therefore \(R^2=0\) exactly when all blocks have weight sum zero. The number of \(c\)-tuples of nonzero elements of \(\mathbb F_q\) summing to zero is \(W_c(q)=((q-1)^c+(q-1)(-1)^c)/q\), as follows by the elementary recurrence \(W_{c+1}=(q-1)^c-W_c\), \(W_1=0\). The nonempty active-weight block series is \(\sum_{c\ge1}W_c(q)z^c/c!\); multiplying by \(e^z\) for its inactive coordinates, then exponentiating over blocks and adjoining the outside factor \(e^z\), proves the square-zero generating function.

## Verification
Execute `python3 verify.py` using Python 3 standard library. The checker independently evaluates all \(n^3\) defining coefficient equations, reconstructs the combinatorial block criterion, verifies exact linear ranks, strong identities, square-zero conditions, rank counts, and both ways of computing \(N_{n,r}(q)\). It exhausts all \(q^{n^2}\) operator matrices for \((q,n)=(2,2),(3,1),(3,2),(3,3),(5,2),(9,2)\); the last case uses a separately implemented model of \(\mathbb F_9\). The characteristic-three rank distributions for \(n=2\) over \(\mathbb F_3\) and \(\mathbb F_9\) are \((1,12,4)\) and \((1,96,64)\), respectively; over \(\mathbb F_3\), \(n=3\) gives \((1,56,60,8)\). Finite computations support but do not replace the all-field algebraic proof.

## Relationship to prior work
Gao, Liu, and Bai introduced the anti–Rota–Baxter and strong anti–Rota–Baxter identities in Section 2.2 of their 2022 work; those definitions are used here. Their paper develops anti-dendriform theory and illustrative examples, rather than the present classification for products of fields. Gubarev studied *ordinary* Rota–Baxter operators on finite sums of fields in 2018; his nonzero-weight rooted-tree classification and the vanishing ordinary weight-zero case have different identities and do not determine the nonzero characteristic-three operators considered here. Published computations of anti–Rota–Baxter maps on dual numbers concern a nonreduced local algebra, rather than the split reduced algebra here. This distinction does not exclude future discovery of equivalent descriptions under averaging-operator terminology.

## Limitations
This is a labeled-operator classification, not a classification up to coordinate-permutation automorphisms. The values and counting formulas are characteristic-sensitive and cannot be extended to arbitrary fields by substituting a formal field size. The finite checks exhaust only the stated small cases. The originality comparison covers identifiable sources, not every older averaging-operator classification; publication priority is provisional. No external independent mathematical validation has been performed.

## References
1. D. Gao, G. Liu, and C. Bai, *Anti-dendriform algebras, new splitting of operations and Novikov type algebras*, arXiv:2209.08962, first posted 2022-09-19, Section 2.2, especially Definition 2.15 and Corollary 2.19. https://arxiv.org/abs/2209.08962
2. V. Gubarev, *Rota–Baxter operators on a sum of fields*, arXiv:1811.08219, first posted 2018-11-20, introduction and Sections 2–3. https://arxiv.org/abs/1811.08219
3. *Characteristic-three phase transition for anti–Rota–Baxter operators on the dual numbers*, public research result, 2026-10-13. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-characteristic-three-phase-transition-for-anti-rota-baxter-opera--810eb43c0979
4. *Rank-refined splitting Rota–Baxter operators on products of fields*, public research result, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rank-refined-splitting-rota-baxter-operators-on-products-of-fiel--68608c1caf70
