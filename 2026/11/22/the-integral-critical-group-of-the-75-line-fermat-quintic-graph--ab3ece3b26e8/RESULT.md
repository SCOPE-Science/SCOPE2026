# The integral critical group of the 75-line Fermat quintic graph

## Finding

Let \(X\subset\mathbb P^3_{\mathbb C}\) be the smooth Fermat quintic
\[
X:\quad x_0^5+x_1^5+x_2^5+x_3^5=0.
\]
Let \(G\) be the **simple** graph whose vertices are all 75 geometric projective lines on \(X\), with two **distinct** vertices adjacent if and only if their lines intersect. Its reduced integral graph Laplacian has Smith normal form
\[
\operatorname{diag}\bigl(1^{[26]},5^{[11]},15^{[13]},60,300^{[12]},1500^{[9]},7500^{[2]}\bigr).
\]
Here superscripted bracketed integers denote multiplicity. Consequently the *graph* critical group is
\[
\boxed{K(G)\cong(\mathbb Z/5\mathbb Z)^{11}\oplus(\mathbb Z/15\mathbb Z)^{13}\oplus\mathbb Z/60\mathbb Z\oplus(\mathbb Z/300\mathbb Z)^{12}\oplus(\mathbb Z/1500\mathbb Z)^9\oplus(\mathbb Z/7500\mathbb Z)^2.}
\]
Its order and exponent are, respectively,
\[
|K(G)|=2^{48}3^{37}5^{84},\qquad \exp K(G)=7500.
\]
In particular, the 5-primary elementary-divisor valuation distribution of the reduced Laplacian is exactly \(0^{[26]},1^{[25]},2^{[12]},3^{[9]},4^{[2]}\). This is an assertion about integral chip-firing on a line-incidence graph, **not** about torsion in \(\operatorname{Pic}(X)\) or the discriminant group of its Néron–Severi lattice.

## Assumptions and scope

Work over \(\mathbb C\); there are no claims about all lines after reduction in exceptional positive characteristic. The classical completeness theorem for the three coordinate-pairing families of lines is used from [1, §3]. Let \(\zeta\) be a primitive fifth root of unity. With \(a,b\in\mathbb Z/5\mathbb Z\), the 75 lines are
\[
\begin{aligned}
A_{a,b}:&\ x_0=-\zeta^a x_1,\quad x_2=-\zeta^b x_3,\\
B_{a,b}:&\ x_0=-\zeta^a x_2,\quad x_1=-\zeta^b x_3,\\
C_{a,b}:&\ x_0=-\zeta^a x_3,\quad x_1=-\zeta^b x_2.
\end{aligned}
\]
Each family has 25 lines. Enumerate first all \(A\), then \(B\), then \(C\), lexicographically by \((a,b)\) with both labels in \(\{0,1,2,3,4\}\). The adjacency matrix \(A_G\) has zero diagonal; the Laplacian is \(L=18I-A_G\). By definition \(K(G)\) is the torsion cokernel of \(L\), equivalently the cokernel of any \(74\times74\) reduced Laplacian since the graph is connected.

## Proof

**Geometric incidence.** Two different lines in the same family meet exactly when their first labels agree or their second labels agree. Direct elimination of the four linear equations from two different families gives, with labels as written above,
\[
\begin{aligned}
A_{a,b}\sim B_{c,e}&\iff a+e\equiv b+c\pmod5,\\
A_{a,b}\sim C_{c,e}&\iff a+b+e\equiv c\pmod5,\\
B_{a,b}\sim C_{c,e}&\iff a+b\equiv c+e\pmod5.
\end{aligned}
\]
For example, at an \(A\)–\(C\) intersection, the equations force \((-\zeta^a)(-\zeta^e)(-\zeta^b)=-\zeta^c\), giving the middle equivalence. For an \(A\)–\(B\) intersection the condition is \((-\zeta^a)(-\zeta^e)=(-\zeta^c)(-\zeta^b)\). For \(B\)–\(C\) it is \((-\zeta^a)(-\zeta^b)=(-\zeta^c)(-\zeta^e)\). No other cross-family intersection is possible because each solution to a common coordinate equation is determined up to scale. Thus each line meets exactly eight others in its own family and five in each other family; \(G\) has 75 vertices, 675 edges and degree 18. These predicates agree with the classical intersection conditions [1, Eq. (5)] after the displayed choice of roots.

**Exact spectrum and tree number.** The adjacency polynomial and power traces have the following *exact* certificates, reproduced by the standalone verifier using integer matrix multiplication:
\[
(A_G-18I)(A_G-3I)(A_G+2I)(A_G+7I)=0,
\]
\[
\bigl(\operatorname{tr}(A_G^j)\bigr)_{j=0}^3=(75,0,1350,2550).
\]
Since \(A_G\) is symmetric and the four roots of the annihilating polynomial are distinct, a nonsingular Vandermonde system forces its spectrum to be \(18^{[1]},3^{[38]},(-2)^{[24]},(-7)^{[12]}\). Hence \(G\) is connected (the valency eigenvalue 18 has multiplicity one), and the nonzero Laplacian spectrum is \(15^{[38]},20^{[24]},25^{[12]}\). Kirchhoff's matrix-tree theorem gives
\[
\det(L_{\mathrm{red}})=\frac{15^{38}20^{24}25^{12}}{75}=2^{48}3^{37}5^{84}.
\]
The spectral classification and tree count are already implied by the all-degree result [3]; neither is asserted as original here. They supply an independently checkable determinant constraint for the integral calculation below.

**Exact local Smith decomposition.** Choose the \(74\times74\) Laplacian minor obtained by deleting any one matching row and column. Over \(\mathbb Z/p^K\mathbb Z\), choose in each remaining submatrix an entry of minimal \(p\)-valuation \(v\), move it to the upper left, write it as \(p^v u\) where \(u\) is a unit, and eliminate the other entries in its column and row by invertible row/column operations (using \(u^{-1}\) modulo \(p^{K-v}\)). The residual block has entries divisible by \(p^v\); the operation records one invariant valuation and reduces the size by one. For each \(p\in\{2,3,5\}\), take \(K\) equal to one more than the proved \(p\)-adic valuation of the determinant. All true invariants have valuation strictly less than \(K\), so the modular diagonalization recovers the integral local elementary divisors, not merely lower bounds.

The exhaustive modular computations give

| Prime | Valuations \(v\) and multiplicities of the 74 Smith factors |
| --- | --- |
| \(2\) | \(0:50,\ 2:24\) |
| \(3\) | \(0:37,\ 1:37\) |
| \(5\) | \(0:26,\ 1:25,\ 2:12,\ 3:9,\ 4:2\) |

The valuation-weighted sums are exactly 48, 37 and 84. Each distribution is checked independently using three distinct deleted vertices, one in each line family, and gives identical results. No other prime can occur by the determinant formula. Aligning the sorted exponent lists produces 26 units and the invariant factors stated in the Finding; their product equals the independently obtained spanning-tree count. This establishes the complete integral graph critical group.

## Verification

The attached standalone file `verify_fermat_quintic.py` uses only the Python standard library. It constructs all 75 vertices and 2,775 unordered line pairs from the symbolic congruence rules, and independently tests every pairing by a direct \(4\times4\) projective-span determinant over \(\mathbb F_{11}\), where the five roots of \(t^5=-1\) are distinct. This finite-field check corroborates the *symbolically proved* complex incidence formulas, rather than replacing the geometric proof. It checks 18-regularity, 675 edges, connectivity, the exact adjacency annihilating polynomial, four traces, Kirchhoff's determinant, and 74-pivot local Smith reductions for primes 2, 3 and 5, each with three distinct deleted vertices and precision greater than the corresponding determinant valuation. Finally it checks the invariant-factor divisibility chain and product. A successful run prints `FERMAT_QUINTIC_75_LINE_CRITICAL_GROUP_OK` and the factor multiplicities. The verifier is a finite exact computation of a fully specified finite graph; no experiment is extrapolated to a variable degree.

## Relationship to prior work

The enumeration of all 75 lines and the explicit pairwise incidence predicates are classical and appear in Schütt–Shioda–van Luijk [1, §3, Eq. (5)]. Their §6.2 computes the geometric Néron–Severi discriminant \(5^{12}\), rather than this graph's Laplacian Smith form. Degtyarev [2] establishes the integral generation of the surface Picard group by these lines, again a different lattice and cokernel. The all-degree graph spectrum and tree count [3] **already determine** the 75-line graph's Laplacian eigenvalues and the order \(2^{48}3^{37}5^{84}\); the published result explicitly leaves Smith normal forms outside its claim. The quartic critical group [4] is for a different 48-vertex graph and does not determine this 75-vertex decomposition. A separate characteristic-two 325-line Hermitian-quintic line-lattice computation [5] concerns the surface's intersection matrix, not this complex 75-line *graph* Laplacian.

The contribution here is only the missing 74-factor integral invariant decomposition, especially its 5-primary depth, not rediscovery of geometry, spectrum or tree number. Exact full-text comparisons and targeted searches did not identify an earlier published decomposition of this specific graph; the known incidence equations nevertheless permit it to be computed, and unidentified historical or unindexed tables remain a priority risk.

## Limitations

The graph-Jacobian group is not the surface's Picard group, Néron–Severi discriminant, nor the Jacobian of any algebraic curve. The theorem is for the 75 classical lines of the complex Fermat quintic, without positive-characteristic extra lines or arithmetic Frobenius descent. The Smith reduction is verified by transparent finite integer operations, not an independently supplied external proof certificate. Historical priority and mathematical significance have not been independently audited; no stronger all-degree Smith classification is claimed.

## References

1. M. Schütt, T. Shioda, R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377, first publicly posted 2008-12-12; §3 Eq. (5), §6.2. https://arxiv.org/abs/0812.2377
2. A. Degtyarev, *Lines generate the Picard groups of certain Fermat surfaces*, arXiv:1305.3073, first publicly posted 2013-05-14; Theorem 1.2 and §2.4. https://arxiv.org/abs/1305.3073
3. *Integral adjacency spectra and spanning-tree counts for all Fermat-surface line configurations*, public mathematical record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-adjacency-spectra-and-spanning-tree-counts-for-all-ferm--e239fc6da92d
4. *Critical group of the 48-line intersection graph on the complex Fermat quartic*, public mathematical record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-critical-group-of-the-48-line-intersection-graph-on-the-complex--e6a8bff17712
5. *The exact Smith form of the Hermitian quintic line lattice*, public mathematical record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-exact-smith-form-of-the-hermitian-quintic-line-lattice--38c504a00bda
