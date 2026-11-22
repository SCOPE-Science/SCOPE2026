# Equidimensional zero-product-preserver arrangements in truncated polynomial algebras

## Finding

For each field \(K\) and integer \(n\ge2\), let \(A_n=K[t]/(t^n)\) and let \(\mathcal Z_n(K)\) be the monoid of all **linear zero-product preservers**:
\[
\mathcal Z_n(K)=\left\{T\in\operatorname{End}_K(A_n):ab=0\Longrightarrow T(a)T(b)=0\text{ for all }a,b\in A_n}\right\}.
\]
These maps need not be algebra homomorphisms, invertible, or unital. Regard their coefficient matrices as points of affine \(n^2\)-space and take the **reduced** algebraic set defined by the zero-product conditions.

**Theorem.** The geometrically irreducible components of this reduced locus are the distinct coordinate linear spaces
\[
L_\eta=\{T:T(t^i)\in(t^{\eta_i})\ (0\le i<n)\},
\]
indexed exactly by sequences of integers
\[
\eta_0=0\le\eta_1\le\cdots\le\eta_{n-1}\le n,
\qquad \eta_i+\eta_{n-i}=n\quad(1\le i<n).
\]
Every component has dimension \(n(n+1)/2\), and their number is
\[
\boxed{\binom{n-1}{\lfloor(n-1)/2\rfloor}}.
\]
The component number is field-independent and grows at the central-binomial rate, despite all components having the same dimension.

For \(K=\mathbb F_q\), write \(F_n(q)=|\mathcal Z_n(\mathbb F_q)|\), and set \(\mathcal P_n\) equal to the displayed set of profiles. Then the **exact count** is
\[
\boxed{F_n(q)=\sum_{\varnothing\ne S\subseteq\mathcal P_n}(-1)^{|S|+1}q^{n^2-\sum_{i=0}^{n-1}\max_{\eta\in S}\eta_i}}.
\]
In particular it is a polynomial in \(q\) of degree \(n(n+1)/2\) and leading coefficient \(\binom{n-1}{\lfloor(n-1)/2\rfloor}\), so
\[
F_n(q)=\binom{n-1}{\lfloor(n-1)/2\rfloor}q^{n(n+1)/2}+O_n(q^{n(n+1)/2-1}).
\]
For example, \(F_2(q)=q^3\), \(F_3(q)=2q^6-q^5\), and \(F_4(q)=3q^{10}-2q^9\).

Only the component corresponding to \(\eta_i=i\) contains invertible maps; all remaining components consist exclusively of singular maps. Indeed an invertible map has valuations \(\nu(T(t^i))=i\), and the opposite-pair equality forces the only profile below these valuations to be \(\eta_i=i\). Consequently, for each fixed \(n\), the proportion of zero-product preservers over \(\mathbb F_q\) that are invertible converges as the field size grows to \(\binom{n-1}{\lfloor(n-1)/2\rfloor}^{-1}\).

The invertible members form **the entire stabilizer of the \(t\)-adic flag** \((t)\supset\cdots\supset(t^{n-1})\), a Borel subgroup of \(\operatorname{GL}_n(K)\). Over \(\mathbb F_q\) its order is \((q-1)^n q^{n(n-1)/2}\). The weighted automorphisms \(a\mapsto u\phi(a)\), with \(u\in A_n^\times\) and \(\phi\) a \(K\)-algebra automorphism, form a subgroup of order \((q-1)^2q^{2n-3}\) and index
\[
\boxed{(q-1)^{n-2}q^{(n-2)(n-3)/2}}.
\]
They exhaust the invertible preservers exactly when \(n=2\), or \(n=3\) and \(q=2\) (for \(n\ge2\)).

## Assumptions and scope

All fields and characteristics are allowed; zero products are those of the *unital* truncated polynomial algebra \(A_n\). The space is the reduced set of solutions, **not** an assertion that the original quadratically defined equation scheme is reduced. For an element \(a\), let its valuation \(\nu(a)\) be its least nonzero \(t\)-exponent, and let \(\nu(0)=n\). Thus \(\nu(ab)=\min(n,\nu(a)+\nu(b))\). Ideals \((t^j)\) include \((t^0)=A_n\) and \((t^n)=0\).

## Proof

**1. Translate preservation into valuations.** Put \(e_i=t^i\), and \(v_i=\nu(T(e_i))\). The conditions \(e_ie_j=0\) for \(i+j\ge n\) are necessary. Conversely, if those pairs have zero image product, every pair \(a,b\) with \(ab=0\) has \(\nu(a)+\nu(b)\ge n\). Every monomial in the expansions of \(a,b\) then has exponents adding to at least \(n\); bilinearity of \(T\) proves \(T(a)T(b)=0\). Therefore
\[
\boxed{T\in\mathcal Z_n(K)\iff v_i+v_j\ge n\quad\text{for every }i+j\ge n}.
\]
The index \(i=0\) produces no constraints; its image is entirely unrestricted. This equivalence also shows that \(\mathcal Z_n\) is a finite union of coordinate linear spaces, since requiring \(v_i\ge a\) means the first \(a\) coefficients of column \(i\) vanish.

**2. Reduce to nondecreasing profiles.** Given a feasible \((v_1,\ldots,v_{n-1})\), define \(w_i=\min_{j\ge i}v_j\), \(1\le i<n\). Then \(w_i\le v_i\) and \(w_1\le\cdots\le w_{n-1}\). If \(i+j\ge n\), choose \(a\ge i,b\ge j\) attaining the minima. As \(a+b\ge n\), we have \(w_i+w_j=v_a+v_b\ge n\), so \(w\) remains feasible.

**3. Saturate opposite pairs without increasing valuations.** For odd \(n=2m+1\), set
\[
\eta_i=n-w_{n-i}\ (1\le i\le m),\qquad \eta_i=w_i\ (m+1\le i<n),\qquad \eta_0=0.
\]
For even \(n=2m\), use the same formula on \(1\le i<m\), set \(\eta_m=m\), and set \(\eta_i=w_i\) for \(m<i<n\). By feasibility each \(\eta_i\le w_i\). Weak monotonicity is preserved within both halves. At the central join it follows in the odd case from \(w_m+w_{m+1}\ge2m+1\) and \(w_m\le w_{m+1}\); in the even case from \(w_m\ge m\). Consequently every original feasible valuation vector dominates some \(\eta\) as in the theorem. Conversely, for such \(\eta\), whenever \(i+j\ge n\), monotonicity yields \(\eta_j\ge\eta_{n-i}=n-\eta_i\), making every map of \(L_\eta\) a preserver. Thus \(\mathcal Z_n=\bigcup_\eta L_\eta\), set-theoretically over any extension of \(K\).

**4. Determine irreducible components and count them.** The spaces \(L_\eta\) are geometrically irreducible. If \(L_\eta\subseteq L_\theta\), then \(\eta_i\ge\theta_i\) for every \(i\). Opposite equalities force \(\eta_i=\theta_i\) for every \(i\), so none of the distinct spaces contains another. Also
\[
\sum_{i=0}^{n-1}\eta_i=\frac{n(n-1)}2,
\]
because the \(n-1\) opposite-pair equalities sum to \(2\sum\eta_i=(n-1)n\). Hence all component dimensions are \(n^2-n(n-1)/2=n(n+1)/2\). If \(n=2m+1\), a profile is determined by a weakly increasing \(m\)-tuple chosen from \(0,\ldots,m\), giving \(\binom{2m}m\) possibilities. If \(n=2m\), its middle value is \(m\), and the first \(m-1\) values form a weakly increasing tuple chosen from \(0,\ldots,m\), giving \(\binom{2m-1}{m-1}\). Both equal the asserted central binomial coefficient.

**5. Finite-field count.** An intersection of component spaces has column \(i\) constrained to \((t^{\max_{\eta\in S}\eta_i})\). Its \(\mathbb F_q\)-dimension is \(n^2-\sum_i\max_{\eta\in S}\eta_i\). Inclusion–exclusion proves the exact formula. Pairwise intersections of distinct irreducible components have strictly lower dimension, so the coefficient of the highest power of \(q\) is exactly the number of components. This is a polynomial identity, not a claim that its coefficients are all nonnegative.

**6. Invertible preservers.** For nonzero \(a\in A_n\), \(\dim_K\operatorname{Ann}(a)=\nu(a)\). If \(T\) is invertible and zero-product preserving, then \(T(\operatorname{Ann}(a))\subseteq\operatorname{Ann}(T(a))\), and hence \(\nu(T(a))\ge\nu(a)\). Therefore \(T\) preserves each ideal of the valuation flag. Conversely any invertible flag-preserving map preserves each valuation *exactly* (its action on every one-dimensional graded piece is invertible), and hence preserves zero products. Its matrix is invertible triangular with respect to \(1,t,\ldots,t^{n-1}\), giving the Borel order. Finally, the unique factorization \(T=u\phi\) has \((q-1)q^{n-1}\) choices of \(u=T(1)\) and \((q-1)q^{n-2}\) choices of \(\phi(t)=a_1t+\cdots+a_{n-1}t^{n-1}\) with \(a_1\ne0\). Dividing the group orders gives the claimed index and its exceptional equality cases. An invertible map has \(\nu(T(t^i))=i\), so in any component \(L_\eta\) containing such a map, \(\eta_i\le i\) for every \(i\). Combined with \(\eta_i+\eta_{n-i}=n\), this forces \(\eta_i=i\); the converse holds because the triangular component contains the identity. As the group has leading field-size term \(q^{n(n+1)/2}\), while the full preserver locus has \(\binom{n-1}{\lfloor(n-1)/2\rfloor}q^{n(n+1)/2}\), their ratio tends to the reciprocal component count.

## Verification

The standalone `CHECK.py` (Python standard library) independently enumerates all feasible valuation profiles through \(n=7\), checks that their coordinate spaces satisfy the symmetric-saturation normal form and form an incomparable covering family, and checks inclusion–exclusion point counts over \(\mathbb F_2\) and \(\mathbb F_3\) through \(n=5\). It also enumerates all linear maps in the five cases \((n,q)=(2,2),(2,3),(3,2),(3,3),(4,2)\), testing zero products by **actual truncated polynomial multiplication** rather than by the valuation formula. The saved successful output is `CHECK_OUTPUT.txt`. These finite tests corroborate, but do not replace, the all-field proof.

## Relationship to prior work

Gardella–Thiel, arXiv:2210.07891 (first public version 2022-10-14), study zero-product-balanced algebras. Their Example 2.16 analyzes the valuations and zero products in the nonunital radical \(tK[t]/(t^m)\), establishing a related basic valuation rule; it does **not** give the full (generally nonsurjective) linear-preserver locus, classify its maximal coordinate spaces, or count its geometric components for the *unital* algebra \(K[t]/(t^n)\). Their weighted-epimorphism criterion applies under zero-product-balanced hypotheses absent here; the Borel/weighted index explicitly exhibits the boundary.

Li–Tsai–Wang–Wong, arXiv:2003.05317 (first public version 2020-03-10), classify nonsurjective zero-product preservers between **full** matrix algebras. Their full-matrix-domain decomposition does not imply the theorem for the proper commutative local algebra \(A_n\); its hypotheses are not met by restricting domain and range to truncated polynomial Toeplitz matrices. Słowik (2017) classifies bijections on the **entire upper triangular algebra** preserving zero products in both directions, rather than all one-directional linear maps on the uniserial commutative subalgebra; neither direction of specialization is automatic.

The elementary facts about valuations, annihilators, and binomial counts are standard; claimed new content is the **complete reduced component arrangement with a central-binomial count** and the simultaneous characterization of its invertible stratum. No claim is made of an independently audited proof or of established global publication priority.

## Limitations

This does **not** classify all nonlinear maps, all zero-product preserving maps between different chain rings, the scheme-theoretic nilpotent structure of the quadratic equations, or a universal extension to arbitrary nonprincipal Artinian rings. The finite-field point polynomial is given by finite explicit inclusion–exclusion, not by a single factored closed form for arbitrary \(n\). A broader unlocated general preserver theorem could still establish equivalent coverage; historical priority remains a residual risk. No independent mathematical audit has been performed.

## References

1. E. Gardella and H. Thiel, *Zero-product balanced algebras*, arXiv:2210.07891v1 (2022-10-14), https://arxiv.org/abs/2210.07891.
2. C.-K. Li, M.-C. Tsai, Y.-S. Wang and N.-C. Wong, *Nonsurjective zero product preservers between matrix spaces over an arbitrary field*, arXiv:2003.05317v1 (2020-03-10), https://arxiv.org/abs/2003.05317.
3. R. Słowik, *Maps on upper triangular matrices preserving zero products*, Czechoslovak Mathematical Journal **67** (2017), 1095–1103, DOI:10.21136/CMJ.2017.0416-16, https://www.dml.cz/manakin/handle/10338.dmlcz/146969.
