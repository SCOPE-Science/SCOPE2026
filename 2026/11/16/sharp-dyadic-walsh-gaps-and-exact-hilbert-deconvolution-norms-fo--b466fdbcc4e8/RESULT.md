# Sharp dyadic Walsh gaps and exact Hilbert deconvolution norms for wheel spanning trees

## Finding
For every integer \(n\ge3\), let \(W_{n+1}\) denote the wheel with a hub and a labelled rim cycle of \(n\) vertices. Encode each spanning tree by its indicator in \(G_n=(\mathbb Z/2\mathbb Z)^{2n}\), with \(n\) spoke coordinates and \(n\) rim-edge coordinates. Let \(f_n\) indicate these spanning-tree indicators and let \(T_n g=f_n*g\), with unnormalized convolution on \(G_n\). The Walsh eigenvalues are
\[
\widehat f_n(\xi)=\sum_{\text{spanning trees }U\subset W_{n+1}}(-1)^{\langle\xi,1_U\rangle}.
\]
For context, a previously established wheel-spectrum divisibility law states that for **every** frequency \(\xi\),
\[
3\nmid n\implies\widehat f_n(\xi)\text{ is odd},\qquad
3\mid n\implies\widehat f_n(\xi)\equiv0\pmod4.
\]
**The finding here is the sharpness of that modular bound:** the exact smallest *positive* absolute Walsh eigenvalue is
\[
\delta_n:=\min_{\widehat f_n(\xi)\ne0}|\widehat f_n(\xi)|=
\begin{cases}1,&3\nmid n,\\4,&3\mid n.\end{cases}
\]
In the singular cases \(3\mid n\), the previously known zero-frequency existence is reconstructed in Step 4. The **new exact Hilbert stability conclusion** in counting-measure norm is
\[
\|T_n^{\dagger}\|_{2\to2}=\delta_n^{-1},\qquad
\kappa_+(T_n)=\frac{\tau(W_{n+1})}{\delta_n},
\]
where \(\dagger\) denotes the Moore--Penrose pseudoinverse, \(\kappa_+\) the ratio of largest to smallest nonzero singular value, and \(\tau(W_{n+1})=L_{2n}-2\) is the classical wheel spanning-tree count (\(L_j\) is the Lucas sequence).

## Assumptions and scope
The wheel is a simple undirected graph with \(n\ge3\) rim vertices \(0,\ldots,n-1\), one hub, rim edges \(\{i,i+1\pmod n\}\) and spokes \(\{i,\mathrm{hub}\}\). Edges are separately labelled. Frequencies specify signs \(r_i=(-1)^{\xi_{\text{rim},i}}\) and \(s_i=(-1)^{\xi_{\text{spoke},i}}\); all signs range independently over \(\{+1,-1\}\). Convolution uses \((f*g)(x)=\sum_{y\in G_n}f(y)g(x-y)\), without normalizing by \(|G_n|\). No exact rank is asserted for the singular \(3\mid n\) cases.

## Proof
**1. Determinantal Walsh representation.** The weighted matrix-tree identity, valid as a polynomial identity also at negative edge weights, gives
\[
\widehat f_n(\xi)=\det M(r,s),\qquad
M_{ii}=s_i+r_{i-1}+r_i,
\quad M_{i,i+1}=M_{i+1,i}=-r_i,
\]
with indices taken modulo \(n\) (for \(n=3\), each off-diagonal pair appears once). This is the Laplacian minor formed using signed **weights**, not the alternative signed-graph Laplacian using absolute degrees.

**2. Modular obstruction.** Put \(A=M(\boldsymbol1,\boldsymbol1)\). Its reduction over \(\mathbb F_2\) is \(I+S+S^{-1}\), where \(S\) cyclically shifts \(n\) coordinates. A kernel vector obeys \(u_{i+1}=u_i+u_{i-1}\) in \(\mathbb F_2\); its two-coordinate state is three-periodic, and no nonzero state has period one or two. Therefore \(A\) is nonsingular modulo two when \(3\nmid n\), and has nullity exactly two when \(3\mid n\). Reducing each weighted tree monomial modulo two shows every signed multiplier has the same parity as \(\tau=\det A\). This proves universal oddness for \(3\nmid n\).

When \(3\mid n\), integer Smith reduction gives \(4\mid\det A\), since \(A\) has at least two even Smith factors. Every entry of \(\operatorname{adj}(A)\) is even because every minor of order \(n-1\) vanishes modulo two. For each edge \(e\) let \(b_e\) be its reduced incidence vector, and let \(c_e\) be the number of spanning trees containing it. Differentiating the weighted tree polynomial at all weights equal to one yields
\[
c_e=b_e^{\mathsf T}\operatorname{adj}(A)b_e\equiv0\pmod2.
\]
If \(F\) is the set of negative-weight edges, then for every tree \(U\), \((-1)^{|F\cap U|}\equiv1-2|F\cap U|\pmod4\). Summing gives
\[
\widehat f_n(\xi)\equiv\tau-2\sum_{e\in F}c_e\equiv0\pmod4.
\]
This argument includes every choice of rim and spoke signs.

**3. Exact transfer-determinant identity.** For any nonzero rim weights \(r_i\), define
\[
P_i(\lambda)=\begin{pmatrix}
(s_i+r_{i-1}+r_i-\lambda)/r_i&-r_{i-1}/r_i\\1&0
\end{pmatrix},\quad P(\lambda)=P_{n-1}(\lambda)\cdots P_0(\lambda).
\]
The recurrence \((M-\lambda I)u=0\) is exactly the transfer recurrence for \((u_{i+1},u_i)\). It admits a nonzero periodic solution precisely when \(\operatorname{tr}P(\lambda)=2\), since \(\det P(\lambda)=1\). Consequently the two degree-\(n\) expressions
\[
\det(M-\lambda I)
=\left(\prod_i r_i\right)(\operatorname{tr}P(\lambda)-2)
\]
coincide: for generic independent diagonal weights the symmetric cyclic matrix has distinct eigenvalues, so they have the same \(n\) roots, and both leading coefficients are \((-1)^n\); polynomial continuation proves the identity at every specialization. All products are ordinary \(2\times2\) integer matrices for rim signs.

When all rim weights are \(+1\) and a spoke is \(-1\) (respectively \(+1\)), its transfer matrix is
\[
B=\begin{pmatrix}1&-1\\1&0\end{pmatrix}
\quad\text{(respectively }D=\begin{pmatrix}3&-1\\1&0\end{pmatrix}\text{)},
\qquad B^3=-I,\quad B^6=I.
\]
In particular, all-negative spokes give determinant \(\operatorname{tr}(B^n)-2\), which equals \(-4\) for \(n\equiv3\pmod6\) and \(-1\) for \(n\equiv1,5\pmod6\). One positive spoke and all other negative spokes give \(\operatorname{tr}(DB^{n-1})-2=-1\) when \(n\equiv2\pmod6\). For \(n\equiv0\pmod6\), take all rim weights \(+1\), the first six spokes \((+1,+1,+1,-1,+1,-1)\), and the remaining spokes \(-1\). The six-transfer product is
\[
\begin{pmatrix}5&-2\\18&-7\end{pmatrix}
\]
with trace \(-2\); adding blocks of six negative spokes multiplies it by \(B^6=I\), so the determinant is always \(-4\).

For \(n\equiv4\pmod6\), use rim signs \((+1,-1,+1,+1,\ldots,+1)\), spoke signs \((-1,+1,+1,+1,-1,\ldots,-1)\). At the four-vertex base case the full transfer product is \(D\), with trace \(3\), and the rim-sign product is \(-1\), yielding \(\det M=-1\). The inserted extra \(6k\) vertices have both incident rim weights \(+1\) and spoke weights \(-1\); they insert \(B^{6k}=I\) into the transfer monodromy, preserving its trace and determinant. These witnesses establish the exact lower positive bound in every residue class, combining with Step 2.

**4. Zero witnesses in the divisible-by-three classes.** If \(3\mid n\), choose all rim weights \(+1\) and three-periodic spoke signs \((+1,+1,-1)\). Then \(M\) has diagonal pattern \((3,3,1)\), each off-diagonal neighbor entry \(-1\), and the nonzero real vector with repeating values \((1,1,2)\) belongs to its kernel. Thus a Walsh eigenvalue is exactly zero in every such dimension.

**5. Convolution norm.** Characters diagonalize convolution on the finite group \(G_n\), and the singular values are the absolute Walsh multipliers. Their maximum is \(\tau(W_{n+1})\), attained at zero frequency by the triangle inequality. The sharp smallest positive value established above immediately gives the pseudoinverse norm, positive condition number and invertibility equivalence. This establishes the sharp spectral gap and norm. The nonvanishing/divisibility background is included for a self-contained derivation.

## Verification
The standalone `wheel_checker.py` constructs all wheel spanning-tree indicators for rim lengths \(3\) through \(9\), applies an integral fast Walsh transform to all \(349{,}504\) frequencies, and verifies the exact gap, parity/divisibility, singularity, tree count and Parseval identity. Exact Bareiss determinants and independent transfer products are checked against sampled character sums. Explicit sharpness signings are also checked by transfer multiplication through rim length \(90\), and directly by integer determinant through rim length \(20\). The output marker is `WHEEL_SPANNING_TREE_WALSH_GAP_PASS`. These checks supplement, but do not replace, the all-order proof.

## Relationship to prior work
The classical wheel spanning-tree count and an unsigned combinatorial bijection were established in prior work by Benjamin and Yerger (2006), referring to older proofs by Sedláček and Myers. Bernardi's 2006 arXiv paper concerns a Tutte-polynomial expansion by embedding activities. Scott and Sokal's 2013 preprint concerns completely monotone inverse powers of graph spanning-tree polynomials on positive cones. Weighted matrix-tree determinants are classical. Earlier analysis of the wheel support has already established its three-periodic invertibility and the universal modulo-four constraint. Those are treated here as background, not novelty. The new question is whether the lower arithmetic bounds are **attained at some frequency for every wheel size** and what exact Hilbert pseudoinverse norm follows. The six-periodic sharpness witnesses answer that question. General weighted matrix-tree determinants and the unsigned wheel enumeration alone do not determine this minimum. Historical-priority claims remain bounded by the documented literature comparison.

## Limitations
The singular-range rank and complete nonzero Walsh-magnitude distribution for \(3\mid n\) are not determined. No endpoint \(\ell^1\) or \(\ell^\infty\) projection constant is asserted. The theorem is for labelled wheels and unnormalized binary Walsh convolution; it does not extend without proof to arbitrary signed graphs or other graph families. Self-review is not independent mathematical validation.

## References
- A. T. Benjamin and C. R. Yerger, *Combinatorial Interpretations of Spanning Tree Identities*, Bulletin of the Institute of Combinatorics and its Applications **47** (2006), 37--42. Full text: https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/Combinatorial-Interpretations-of-Spanning-Tree-Identities.pdf . Journal publication is year-dated; the 2004 date printed in the manuscript is **not** treated as a verified public-release date.
- O. Bernardi, *A characterization of the Tutte polynomial via combinatorial embeddings*, arXiv:math/0608057v1, first public posting **2006-08-02**; https://arxiv.org/abs/math/0608057 .
- A. D. Scott and A. D. Sokal, *Complete monotonicity for inverse powers of some combinatorially defined polynomials*, arXiv:1301.2449v1, first public posting **2013-01-11**; https://arxiv.org/abs/1301.2449 .
