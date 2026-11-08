# Exact approximation-number plateaux for sparse tree-Hardy composition operators

## Finding

**Theorem (exact approximation numbers).** Fix an integer \(q\ge2\) and a real \(1\le p<\infty\). On the \((q+1)\)-homogeneous rooted tree, choose two sequences \((m_j)_{j\ge1}\) and \((n_j)_{j\ge1}\) of pairwise distinct positive integers, respectively, with \(m_j<n_j\). At each output level \(n_j\), choose exactly \(c_{m_j}\) distinct vertices and biject them with the input level \(m_j\). Define a self-map \(\phi\) by these bijections, mapping every remaining vertex to the root. Then the unweighted composition operator \(C_\phi:f\mapsto f\circ\phi\) on the discrete tree Hardy space \(\mathbb T_p\) satisfies \(\|C_\phi\|=1\), and it is compact if and only if
\[
 n_j-m_j\longrightarrow\infty.
\]
In the compact case, let \((w_k)_{k\ge1}\) be the nonincreasing rearrangement of the numbers
\[
 \delta_j=q^{-(n_j-m_j)/p},\qquad\text{each repeated }c_{m_j}\text{ times}.
\]
For the approximation-number convention \(a_k(S)=\inf_{\operatorname{rank}R<k}\|S-R\|\), the **complete exact profile** is
\[
 \boxed{a_1(C_\phi)=1,\qquad a_{k+1}(C_\phi)=w_k\quad(k\ge1).}
\]

**Arithmetic plateaux and sharp critical ideal.** For positive integers \(a,b\), specialize to \(m_j=aj\), \(n_j=(a+b)j\). Set
\[
 J_j=\sum_{i=1}^{j}c_{ai}=\frac{(q+1)q^{a-1}}{q^a-1}(q^{aj}-1),\qquad J_0=0.
\]
Then \(a_{k+1}(C_\phi)=q^{-bj/p}\) exactly when \(J_{j-1}<k\le J_j\). For every real \(r>0\),
\[
 \sum_{k\ge1}a_k(C_\phi)^r<\infty\quad\Longleftrightarrow\quad r>ap/b.
\]
For \(r>ap/b\), that sum equals
\[
 1+\frac{q+1}{q}\,\frac{q^{a-br/p}}{1-q^{a-br/p}}.
\]
At the critical exponent \(r_0=ap/b\), put \(K=(q+1)q^{a-1}/(q^a-1)\). The exact log-periodic envelope is
\[
 \liminf_{k\to\infty}k^{1/r_0}a_k(C_\phi)=K^{1/r_0}q^{-b/p},\qquad
 \limsup_{k\to\infty}k^{1/r_0}a_k(C_\phi)=K^{1/r_0}.
\]
Hence the sequence is in weak \(\ell_{r_0}\) but not in strong \(\ell_{r_0}\).

**Arbitrary positive thresholds.** For any real \(\rho>0\), take \(m_j=j\) and \(n_j=j+\lceil pj/\rho\rceil\). Then \(a_k(C_\phi)\asymp k^{-1/\rho}\), so its approximation-number sequence belongs to strong \(\ell_r\) exactly for \(r>\rho\), and belongs to weak \(\ell_\rho\) but not strong \(\ell_\rho\). These are unweighted compact composition operators, not externally weighted or general block-diagonal operators.

## Assumptions and scope

Let \(T\) be a countably infinite tree whose unrooted vertex degree is \(q+1\), with fixed root \(o\). The level sets are \(D_n=\{v\in T:|v|=n\}\), with \(c_0=1\) and \(c_n=(q+1)q^{n-1}\) for \(n\ge1\). On complex-valued vertex functions put
\[
 M_p(n,f)=\left(c_n^{-1}\sum_{v\in D_n}|f(v)|^p\right)^{1/p},\qquad
 \mathbb T_p=\{f:\|f\|_p:=\sup_{n\ge0}M_p(n,f)<\infty\}.
\]
Fix two injective sequences of positive integers \((m_j)\), \((n_j)\) with \(m_j<n_j\); neither needs to be sorted, and input and output sets of depths may intersect. At each \(n_j\), choose \(E_j\subset D_{n_j}\) of cardinality \(c_{m_j}\) and a bijection \(\tau_j:E_j\to D_{m_j}\). This is feasible since \(m_j<n_j\). Let \(\phi(v)=\tau_j(v)\) on \(E_j\), and \(\phi(v)=o\) otherwise. Distinctness of input depths and output depths is essential to the exact blockwise argument.

All approximation numbers are **Banach-space finite-rank approximation numbers**, not Hilbert-space singular values or Schatten norms. An ideal membership statement below refers only to summability of these approximation numbers.

## Proof

**1. Contractivity and decomposition.** For each \(j\), direct counting gives
\[
 M_p(n_j,C_\phi f)^p=\frac{c_{m_j}}{c_{n_j}}M_p(m_j,f)^p+
 \left(1-\frac{c_{m_j}}{c_{n_j}}\right)|f(o)|^p.
\]
Every remaining level has \(M_p(n,C_\phi f)=|f(o)|\). Hence \(C_\phi\) is contractive, and the constant-one function proves its norm is one. Write \(h=\mathbf1_{T\setminus\bigcup_jE_j}\), \(Rf=f(o)h\), and \(B_jf=\mathbf1_{E_j}(f\circ\tau_j)\). Then
\[
 C_\phi=R+\sum_{j\ge1}B_j,\qquad \operatorname{rank}R=1,
 \quad\operatorname{rank}B_j=c_{m_j},\quad\|B_j\|=\delta_j=q^{-(n_j-m_j)/p}.
\]
Because the \(B_j\) have disjoint output levels and disjoint input levels, every tail has exact norm \(\sup_{j\in F}\delta_j\) when indexed by a subset \(F\). Consequently \(n_j-m_j\to\infty\) makes \(C_\phi\) a norm limit of finite-rank operators. Conversely, if infinitely many \(\delta_j\ge\epsilon>0\), select unit functions supported on the corresponding distinct input levels. Their images have pairwise separated components of norm at least \(\epsilon\), so the images cannot have a convergent subsequence; \(C_\phi\) is not compact.

**2. Upper approximation bound.** Let \(w_k\) be the \(k\)-th largest weight in the multiplicity-expanded multiset. Each input level is a finite-dimensional \(\ell_p\) block with a normalized coordinate basis. Copying any individual coordinate from \(D_{m_j}\) to the corresponding single vertex of \(E_j\) is a rank-one map of norm \(\delta_j\). Keep the root rank-one term \(R\) and any \(k-1\) of those coordinates with the largest weights. Their sum has rank at most \(k\), while the discarded-coordinate map has operator norm at most \(w_k\): on a given input block coordinate deletion is a contractive projection, and output levels do not interact. Therefore \(a_{k+1}(C_\phi)\le w_k\).

**3. Lower approximation bound.** Select \(k\) distinct input coordinate directions whose copied weights are at least \(w_k\), and adjoin the root coordinate direction. These vectors span a \((k+1)\)-dimensional subspace \(F\). Every \(f\in F\) satisfies
\[
 \|C_\phi f\|_p\ge\max\left(|f(o)|,\sup_j\delta_j M_p(m_j,f)\right)
 \ge w_k\|f\|_p.
\]
Indeed the displayed lower bound observes the root output and, separately, the contribution on \(E_j\). Any linear map of rank less than \(k+1\) has a nonzero kernel vector in \(F\); for that vector its distance from \(C_\phi\) is at least \(w_k\). Thus \(a_{k+1}(C_\phi)\ge w_k\). This proves the exact profile; \(a_1=\|C_\phi\|=1\).

**4. Arithmetic counting and endpoints.** For \(m_j=aj\), \(n_j=(a+b)j\), weights strictly decrease as \(q^{-bj/p}\) and occur with multiplicity \(c_{aj}\). Summing the geometric level sizes yields \(J_j\). The series of \(r\)-th powers is
\[
 1+\sum_{j\ge1}c_{aj}q^{-bj r/p}
 =1+\frac{q+1}{q}\sum_{j\ge1}q^{j(a-br/p)},
\]
which converges precisely when \(r>ap/b\), with the claimed sum. At the critical exponent, compare the beginning and end of the \(j\)-th constant plateau. As \(j\to\infty\), \(J_j\sim Kq^{aj}\), so the beginning gives \(K^{1/r_0}q^{-b/p}\) and the end gives \(K^{1/r_0}\). Along each plateau the product \(k^{1/r_0}a_k\) increases, so these are the global liminf and limsup.

**5. Arbitrary thresholds.** With \(m_j=j\) and \(n_j=j+\lceil pj/\rho\rceil\), the \(j\)-th weight is bounded above and below by fixed positive multiples of \(q^{-j/\rho}\), while its multiplicity is comparable to \(q^j\). The cumulative multiplicity is comparable to \(q^j\), giving \(a_k\asymp k^{-1/\rho}\). Convergence and endpoint weak/strong membership follow by comparison with the corresponding power series.

## Verification

The standalone standard-library program `check_tree_approximations.py` checks exact finite-level averaging, contractivity, block size and plateau multiplicities, the geometric count, the critical-exponent inequality, and an unsorted depth-gap example. Executing the embedded program prints `TREE_SPARSE_COPY_EXACT_FINITE_OK 2166`. Its exact-rational checks are corroboration only; Steps 1–5 provide the infinite-dimensional proof. The checker does not enumerate the infinite tree or certify uniqueness in the literature.

## Relationship to prior work

Liu and Ma, *Compactness of composition operators on Hardy spaces of homogeneous rooted trees* (arXiv:2610.33717v1, publicly posted 2026-10-24), prove qualitative compactness criteria for composition operators and their finite linear combinations. Their Section 3 supplies general compactness statements; Section 4 gives cancellation examples. The present theorem constructs an explicit unweighted symbol family and computes every approximation number, multiplicity, ideal threshold, and critical oscillation, not merely compactness. The earlier treatments by Muthukumar and Ponnusamy formulate and study composition operators on these discrete Hardy spaces but do not supply this exact sparse-family profile. The block-diagonal finite-rank argument uses standard Banach-space approximation methods and does not claim that methodology as new. Approximation-number studies for analytic disk Hardy spaces and integral Hardy-type operators on trees concern different underlying spaces and operators.

## Limitations

The statement applies to sparse symbols with pairwise distinct input and output levels, not to general self-maps of the tree; overlapping source levels or multiple copies of one level can change the exact profile. It assumes \(1\le p<\infty\) and \(q\ge2\). It concerns approximation-number ideals, not Schatten classes on a Hilbert space. No independent mathematical audit or publication-priority certification has been performed. Equivalent statements in older general block-operator language remain a possible literature risk.

## References

1. Lei Liu and Wanxin Ma, *Compactness of composition operators on Hardy spaces of homogeneous rooted trees*, arXiv:2610.33717v1 (2026-10-24). https://arxiv.org/abs/2610.33717
2. T. Muthukumar and S. Ponnusamy, *Composition operators on Hardy spaces of the homogenous rooted trees*, arXiv:2004.03171v1 (2020). https://arxiv.org/abs/2004.03171
3. T. Muthukumar and S. Ponnusamy, *Composition operators on the discrete analogue of generalized Hardy space on homogeneous trees*, arXiv:1609.09729 (2016). https://arxiv.org/abs/1609.09729
4. G. Lechner, D. Li, H. Queffélec, and L. Rodríguez-Piazza, *Approximation numbers of weighted composition operators*, Journal of Functional Analysis 274 (2018), 1928–1958. https://orca.cardiff.ac.uk/id/eprint/108334/
