# Sharp two-input variation sensitivity of centered maximal averaging on the smallest cycles

## Finding
Let \(C_n\) be the unweighted cycle of \(n\in\{3,4,5\}\) vertices, with indices modulo \(n\). For nonnegative real vectors \(f\), write \(M_nf\) for the centered graph-ball Hardy--Littlewood maximal average and \(V_n(f)=\sum_{i=0}^{n-1}|f_{i+1}-f_i|\). The sharp constants in the **pairwise**, rather than single-input, variation estimate are
\[
\boxed{V_n(M_nf-M_ng)\le K_n V_n(f-g),\quad
K_3=1,\qquad K_4=\frac54,\qquad K_5=\frac75}
\]
for all \(f,g\in[0,\infty)^n\). Each constant is attained by distinct, strictly admissible input pairs. In particular, a pairwise variation expansion is possible already on \(C_4\), whereas the classical one-input estimate on these cycles is a strict contraction, with sharp factors \(1-1/n\). The three sizes constitute all ordinary cycles whose graph diameter is at most two.

## Assumptions and scope
A graph ball is \(B(i,r)=\{j:\operatorname{dist}_{C_n}(i,j)\le r\}\), and
\[
(M_nf)_i=\max_{0\le r\le\lfloor n/2\rfloor}
\frac1{|B(i,r)|}\sum_{j\in B(i,r)}f_j.
\]
For \(n=3\), the radius-one ball is all of \(C_3\). For \(n=4,5\), the radius-one ball has three vertices and the radius-two ball is the whole graph. The input pairs must be nonnegative; this restriction matters, because replacing \(f\) by \(|f|\) destroys translation equivariance on sign-changing pairs. The normalization of the seminorm is the **unweighted**, undirected edge sum, counting each edge once. A constant difference causes constant output difference, so the estimate includes the zero-seminorm case. No claim is made beyond three, four, and five vertices.

## Proof
**1. Reduction to averaging selectors.** Along the segment \(f+t(g-f)\), \(0\le t\le1\), each output coordinate is the maximum of finitely many affine functions of \(t\). Therefore the output is continuous and piecewise affine with finitely many pieces. On each open piece its derivative has the form \(B(g-f)\), where row \(i\) of \(B\) is the uniform averaging row of one of the balls centered at \(i\). Such a row-selector matrix preserves the constant vector \(\mathbf1\). We may bound **all** selectors, whether or not a particular selector pattern occurs on an open piece: this only strengthens the upper bound. The triangle inequality for the integral of these finitely many derivatives then reduces the nonlinear pairwise estimate to a bound on \(V_n(Bh)\) for every real \(h\) and every selector matrix \(B\).

**2. Cyclic arc-extreme lemma.** For any real vector \(h\), let \(d_i=h_{i+1}-h_i\). The numbers \(d_i\) sum to zero. Couple their positive and negative parts, both having mass \(V_n(h)/2\), and for every coupled positive-negative pair choose the oriented contiguous cyclic arc whose indicator has precisely the corresponding positive and negative boundary differences. Consequently
\[
h=c\mathbf1+\sum_A t_A\mathbf1_A,
\qquad t_A\ge0,\qquad \sum_A t_A=V_n(h)/2,
\]
where each \(A\) is a nonempty proper contiguous cyclic arc. (If one reverses which boundary is positive, choose the complementary oriented arc.) Since \(B\mathbf1=\mathbf1\),
\[
V_n(Bh)\le \frac{V_n(h)}2\max_A V_n(B\mathbf1_A).
\]
Rotation of a selector and complementing an arc leave its worst-case variation unchanged, because \(B(\mathbf1-\mathbf1_A)=\mathbf1-B\mathbf1_A\). It is therefore enough to consider the arcs \(A=\{0,\ldots,L-1\}\), for \(1\le L\le\lfloor n/2\rfloor\).

**3. Exact interval-box bound.** Fix one such arc. For each vertex \(i\), the number \((B\mathbf1_A)_i\) is one of the finitely many ball proportions \(|A\cap B(i,r)|/|B(i,r)|\). Let \(\ell_i\) and \(u_i\) be its smallest and largest possible values. The resulting vector lies in the rectangular box \(\prod_i[\ell_i,u_i]\). The map \(y\mapsto V_n(y)\) is convex, so its maximum on this box occurs at an endpoint vector, with each \(y_i\in\{\ell_i,u_i\}\). Direct exact rational evaluation of all endpoint vectors gives:

| \(n\) | Arc length \(L\) | Lower endpoints \((\ell_i)\) | Upper endpoints \((u_i)\) | Maximum \(V_n(y)\) |
|---|---:|---|---|---:|
| 3 | 1 | \((1/3,0,0)\) | \((1,1/3,1/3)\) | \(2\) |
| 4 | 1 | \((1/4,0,0,0)\) | \((1,1/3,1/4,1/3)\) | \(5/2\) |
| 4 | 2 | \((1/2,1/2,0,0)\) | \((1,1,1/2,1/2)\) | \(2\) |
| 5 | 1 | \((1/5,0,0,0,0)\) | \((1,1/3,1/5,1/5,1/3)\) | \(12/5\) |
| 5 | 2 | \((2/5,2/5,0,0,0)\) | \((1,1,2/5,2/5,2/5)\) | \(14/5\) |

This is a complete finite calculation, not a numerical experiment: the five rows require respectively \(8,16,16,32,32\) explicit rational vertex evaluations, exactly as implemented in the standalone `verify_exact.py`. Combining the largest variations in each \(n\) with Step 2 gives the linear selector bounds \(1\), \(5/4\), and \(7/5\). Integrating the selector derivatives from Step 1 establishes the inequalities for all nonnegative input pairs.

**4. Attained sharpness.** Let \(\varepsilon=1/100\). In each example put \(g=f+\varepsilon h\); all values are nonnegative; adding the same positive constant to both inputs makes them strictly positive without changing the amplification. On the indicated base input, the radius-zero average uniquely wins at every entry with value \(1\), and the whole-graph average uniquely wins at the single low entry with value \(0\). The same selector pattern remains valid along the entire segment to \(g\).

For \(C_3\), take \(f=(1,1,0)\), \(h=(1,0,0)\). Then \(V_3(h)=2\) and
\[
\varepsilon^{-1}(M_3g-M_3f)=(1,0,1/3),
\quad V_3(\varepsilon^{-1}(M_3g-M_3f))=2.
\]
For \(C_4\), take \(f=(1,1,0,1)\), \(h=(1,0,0,0)\), obtaining
\[
\varepsilon^{-1}(M_4g-M_4f)=(1,0,1/4,0),
\quad V_4(\varepsilon^{-1}(M_4g-M_4f))=5/2.
\]
For \(C_5\), take \(f=(1,1,1,1,0)\), \(h=(0,1,1,0,0)\), obtaining
\[
\varepsilon^{-1}(M_5g-M_5f)=(0,1,1,0,2/5),
\quad V_5(\varepsilon^{-1}(M_5g-M_5f))=14/5.
\]
Each \(h\) has variation \(2\). The ratios therefore attain precisely \(1,5/4,7/5\). Together with the upper bound, this completes the proof.

## Verification
Run `python3 verify_exact.py` using only the Python standard library. The checker derives the box bounds from the ball-averaging rows, exhausts all \(104\) rational box vertices, checks each exact sharpness pair with \(\varepsilon=1/100\), and additionally tests \(3000\) deterministic rational input pairs. The exhaustive box calculation is a finite proof certificate for the stated five cases; random pair testing is not part of the proof of the unrestricted inequalities. All analytical reductions and hypotheses are stated above.

## Relationship to prior work
Bober--Carneiro--Hughes--Pierce (first public 2010) motivated the discrete variation problem but studied \(V(Mf)\) for a single input on \(\mathbb Z\), not the seminorm distance \(V(Mf-Mg)\). González-Riquelme--Madrid (first public 2020) proved one-input variation results and a distinct continuity assertion in the full \(BV\) norm, without determining these pairwise sharp seminorm constants. González-Riquelme--Kovač--Madrid (2026) computed one-input variation constants on small finite graphs, including \(C_4\). The published exact weighted-cycle one-input result likewise proves \(V(Mf)\le(1-w_*/W)V(f)\) for \(C_3,C_4,C_5\), not a bound for \(V(Mf-Mg)\). Such a one-input bound does not imply a difference estimate for a nonlinear maximal operator. The new sharp pairwise factors strictly exceed the known one-input factors, with a first expansion at four vertices. Related published pairwise variation results for cyclic median filters address different operators and do not imply the centered maximal-averaging formula.

## Limitations
The theorem is exactly for nonnegative real signals and ordinary unweighted centered graph-ball means on \(C_3,C_4,C_5\). It does not assert that the same constants apply on the whole signed domain, where an absolute value is needed in the maximal-operator definition; in fact no finite variation-seminorm Lipschitz bound can hold on all signed pairs without additional restrictions, because constants can cross zero in a nonconstant background. It does not determine sharp constants for cycles with six or more vertices, weighted vertex masses, weighted edge variation, or other maximal operators. Historical priority beyond the inspected publications and published records cannot be guaranteed. No independent mathematical validation is asserted.

## References
- J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030v1 (2010-05-17), https://arxiv.org/abs/1005.3030 ; full text: https://arxiv.org/html/1005.3030v4 .
- C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1 (2020-05-06), https://arxiv.org/html/2005.03146v3 .
- C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy--Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (2026-03-12), https://arxiv.org/html/2603.12462v1 .
- *Sharp weighted variation of centered maximal averages on cycles of diameter at most two*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-weighted-variation-of-centered-maximal-averages-on-cycles--e3a2f5b97b74 .
