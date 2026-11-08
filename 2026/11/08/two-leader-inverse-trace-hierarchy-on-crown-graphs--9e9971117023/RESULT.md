# Two-leader inverse-trace hierarchy on crown graphs

## Finding

For every integer \(m\ge4\), let \(\operatorname{Cr}_m=K_{m,m}-M_m\) be the unweighted crown graph, with vertex classes \(A=\{a_1,\ldots,a_m\}\), \(B=\{b_1,\ldots,b_m\}\), and deleted matching \(M_m=\{\{a_i,b_i\}:1\le i\le m\}\). For exactly two distinct noise-free leaders \(S\), let \(F=V\setminus S\) and set
\[
J_m(S)=\operatorname{tr}\!\bigl(L_{FF}^{-1}\bigr),
\]
where \(L\) is the ordinary combinatorial graph Laplacian. There are precisely three pair orbits, and their objective values satisfy the *strict hierarchy*
\[
\begin{aligned}
J_m(\{a_i,b_i\})&=C_{\mathrm{missing}}
 =\frac{6(m-1)^2}{m(2m-3)},\\
J_m(\{a_i,a_j\})=J_m(\{b_i,b_j\})&=C_{\mathrm{same}}
 =\frac{3m^2-4m+3}{m(m-1)},\quad i\ne j,\\
J_m(\{a_i,b_j\})&=C_{\mathrm{adjacent}}
 =\frac{2(m-1)(3m^2-5m+3)}{m(m-2)(2m-1)},\quad i\ne j,\\
C_{\mathrm{missing}}&<C_{\mathrm{same}}<C_{\mathrm{adjacent}}.
\end{aligned}
\]
Consequently **the exactly \(m\) optimal two-leader sets are the endpoints of the deleted matching edges**, even though those leaders are *not adjacent*. The strict separation is quantified by
\[
C_{\mathrm{same}}-C_{\mathrm{missing}}
=\frac{m^2-3}{m(m-1)(2m-3)},\qquad
C_{\mathrm{adjacent}}-C_{\mathrm{same}}
=\frac{m^2+1}{(m-2)(m-1)(2m-1)}.
\]
Each positive gap is asymptotic to \(1/(2m)\). These formulas supply all pair-placement costs without searching the \(\binom{2m}{2}\) possible leader sets.

## Assumptions and scope

All edge conductances equal \(1\). The graph is connected for \(m\ge3\); the statement is made for \(m\ge4\), thereby excluding the six-cycle \(m=3\) already encompassed by one-dimensional cycle literature. Vertices \(a_i,b_j\) are joined exactly when \(i\ne j\). Exactly two vertices are clamped to a common deterministic trajectory, and every other vertex is a noisy follower. The objective is the **unscaled** grounded-Laplacian inverse trace; stochastic-state variance under the common convention of unit white-noise intensity is one half of this trace. This factor does not affect optimizer identity. No claim concerns noisy leaders, more than two leaders, weighted edges, or arbitrary bipartite graphs.

## Proof

Let \(d=m-1\), the common degree. With follower classes \(A_F,B_F\) having cardinalities \(p,q\), the grounded Laplacian is
\[
L_{FF}=
\begin{pmatrix}
dI_p&-C\\
-C^{\mathsf T}&dI_q
\end{pmatrix},
\]
where \(C\) is the \(p\times q\) surviving cross-adjacency matrix. Every such matrix is positive definite because the original crown graph is connected and at least one leader is grounded. If the positive singular values of \(C\) are \(\sigma_1,\ldots,\sigma_r\), and \(p\le q\), an orthogonal singular-value decomposition gives the exact identity
\[
\operatorname{tr}(L_{FF}^{-1})=
\frac{q-p}{d}+\sum_{i=1}^{p}\frac{2d}{d^2-\sigma_i^2},
\]
where the list \(\sigma_1,\dots,\sigma_p\) includes zeros if needed. The inverses and all denominators are well defined by positive definiteness.

**Missing-edge leaders \(\{a_i,b_i\}\).** The remaining cross-adjacency matrix is \(C=J_{m-1}-I_{m-1}\). Its squared singular values are \((m-2)^2\) once and \(1\) with multiplicity \(m-2\). Inserting these into the trace identity gives
\[
C_{\mathrm{missing}}=
\frac{2d}{d^2-(m-2)^2}
+(m-2)\frac{2d}{d^2-1}
=\frac{6(m-1)^2}{m(2m-3)}.
\]

**Same-class leaders \(\{a_i,a_j\}\).** Here \(p=m-2\), \(q=m\), and every row of \(C\) has \(m-1\) ones; two distinct rows share \(m-2\) ones. Therefore
\[
CC^{\mathsf T}=I_{m-2}+(m-2)J_{m-2},
\]
with eigenvalues \((m-2)^2+1\) once and \(1\) with multiplicity \(m-3\). Because two extra \(B\)-coordinates are uncoupled in the singular-value decomposition,
\[
C_{\mathrm{same}}
=\frac{2}{d}+\frac{2d}{d^2-((m-2)^2+1)}
 +(m-3)\frac{2d}{d^2-1}
=\frac{3m^2-4m+3}{m(m-1)}.
\]

**Adjacent cross-class leaders \(\{a_i,b_j\}\), \(i\ne j\).** Set \(t=m-2\). Relabel the \(m-1\) followers in each class so the \(t\) doubly surviving indices come first. The cross-adjacency matrix is
\[
C=\begin{pmatrix}
J_t-I_t&\mathbf 1_t\\
\mathbf 1_t^{\mathsf T}&1
\end{pmatrix}.
\]
On the \((t-1)\)-dimensional subspace orthogonal to \(\mathbf 1_t\), \(CC^{\mathsf T}\) acts as \(I\). Its remaining two eigenvalues \(\lambda_+,\lambda_-\) have
\[
\lambda_++\lambda_-=m^2-4m+6,\qquad
\lambda_+\lambda_-=1,
\]
as follows by taking trace and determinant on the span of \(\mathbf1_t\) and the final coordinate. Consequently
\[
C_{\mathrm{adjacent}}
=(m-3)\frac{2d}{d^2-1}
+2d\,\frac{2d^2-(m^2-4m+6)}
{d^4-(m^2-4m+6)d^2+1}
=\frac{2(m-1)(3m^2-5m+3)}{m(m-2)(2m-1)}.
\]

Every unordered pair of distinct vertices falls into exactly one of these three cases: missing-edge pairs (\(m\) choices), same-class pairs (\(m(m-1)\) choices) or adjacent cross-class pairs (\(m(m-1)\) choices). Direct subtraction yields the two rational gap formulas displayed in the finding, both strictly positive for every \(m\ge4\). This proves both the unique optimal orbit and exact count. Multiplying each gap by \(m\) and taking \(m\to\infty\) gives the claimed \(1/(2m)\) leading term.

## Verification

A standalone Python program `verify.py` uses exact `fractions.Fraction` Gauss–Jordan inversion of the grounded Laplacian built directly from graph edges, independently of the singular-value derivation. It tests **all 365** two-leader subsets over \(m=3,\ldots,8\), nine further representatives for \(m\in\{9,10,12\}\), and 148 integer parameter instances of the two rational gap identities (\(m=3,\ldots,150\)). Its expected successful output is:

`PASS exhaustive_2sets 365 representative_larger 9 exact_gap_identities 148 m_range 3..8`

Run with `python -S verify.py` using a standard Python 3 installation. A finite exact check supports implementation reproducibility; the proof of the infinite family is the preceding symbolic eigenvalue and inequality argument, not extrapolation from these tests.

## Relationship to prior work

Lin, Fardad and Jovanović (2013) formulate the noise-free leader objective as a grounded-Laplacian inverse trace and give general optimization/relaxation methods. Fitch and Leonard (2014) express leader-set error via joint centrality and solve specific path/cycle examples. Patterson, McGlohon and Dyagilev (2014) give algorithms on one-dimensional paths and cycles. These formulations apply abstractly to the present graph, but their inspected classification results do not give the three crown-graph pair orbits, numerical rational traces or their strict order.

The unweighted crown graph is a perfect-matching deletion from a complete bipartite graph, not itself a complete bipartite graph. Consequently complete-bipartite two-leader formulas do not transfer by substituting parameters. The \(m=3\) crown is a six-cycle and is deliberately excluded from the stated new range. Combinatorial results about crown-graph restrained domination and perfect Roman domination select deleted-matching pairs under different, nonmetric objectives; those conclusions alone do not imply any of the inverse-trace formulas or the strict three-orbit hierarchy.

## Limitations

The result is exact for one natural fixed leader budget only; it does not solve arbitrary-\(k\) leader allocation, nonuniform conductances, or other noise models. The self-review is not an independent audit. Relevant unindexed specialist literature could contain an equivalent statement; none was identified in the sources actually inspected. The rational formulas are established analytically, and exact computation is only a separate finite verification.

## References

1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450 (first public 2013-02-03), https://arxiv.org/html/1302.0450v2 .
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public 2014-07-07), https://arxiv.org/html/1407.1569v2 .
3. S. Patterson, N. McGlohon, K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first public 2014-12-20), https://arxiv.org/html/1412.6595v1 .
