# Complete-flag shattering, Gaussian-multinomial supports, and exact online dimension

## Finding
Fix a prime power \(q\ge2\) and an integer \(n\ge1\). Let \(V=\mathbb F_q^n\), and regard each *complete flag* \(0=V_0<V_1<\cdots<V_n=V\), \(\dim V_i=i\), as one Boolean hypothesis on the set of all linear subspaces of \(V\): a query \(U\le V\) has response one precisely when \(U=V_i\) for some \(i\).

**Theorem.** A finite support \(S\) of distinct queried subspaces is VC-shattered by all complete flags if and only if \(S\) is a strict chain of nonzero proper subspaces, with the empty support allowed. In particular, the family of shattered supports is *exactly* the abstract simplicial order complex of the proper nonzero subspace lattice, also called the spherical building of type \(A_{n-1}\).

Define the Gaussian binomial \(\begin{bmatrix}m\\r\end{bmatrix}_q\) as the number of \(r\)-dimensional subspaces of \(\mathbb F_q^m\). With \(s_k(q,n)\) counting unordered \(k\)-subspace shattered supports, the complete shattering polynomial is
\[
\Phi_{q,n}(z)=\sum_{k=0}^{n-1}s_k(q,n)z^k,\qquad
s_k(q,n)=\sum_{\substack{b_1+\cdots+b_{k+1}=n\\b_i\ge1}}
\prod_{i=1}^{k+1}\begin{bmatrix}n-\sum_{j<i}b_j\\b_i\end{bmatrix}_q.
\]
The sum is over ordered compositions into positive parts. In particular, \(s_0(q,n)=1\), all coefficients above degree \(n-1\) vanish, and
\[
s_{n-1}(q,n)=\prod_{j=1}^{n}\frac{q^j-1}{q-1},\qquad
\operatorname{VCdim}=\operatorname{Ldim}=n-1.
\]
For instance, \(\Phi_{2,4}(z)=1+65z+315z^2+315z^3\).

## Assumptions and scope
We include both trivial subspaces as possible queries, although every flag contains them and hence no shattered support can contain them. Flags have one subspace in each dimension. The hypothesis class is the *entire* set of complete flags, not an arbitrary flag code. A shattered support realizes every possible Boolean labeling on the same fixed queried subspaces; Littlestone dimension measures complete binary adaptive query trees with a different allowed query at each node. We use \(\operatorname{Ldim}=0\) when no nontrivial binary split is possible. The result includes \(n=1\), when the one flag produces the polynomial \(1\).

## Proof
**1. Necessity of nesting.** If \(S\) is shattered, its all-one labeling is witnessed by a complete flag. Thus all its members are pairwise comparable by inclusion. Any occurrence of \(0\) or \(V\) has constant response one in every hypothesis and cannot be shattered. Every shattered support is therefore a strict chain of proper nonzero subspaces.

**2. Sufficiency, including all-zero labels.** Let \(S=(U_1<\cdots<U_k)\) be a chain of proper nonzero subspaces, and prescribe arbitrary zeros and ones. Fix the subspaces prescribed one and add the anchors \(0\) and \(V\). Consider any consecutive anchors \(A<B\); in this interval let the (necessarily nested) support subspaces prescribed zero be \(W_1<\cdots<W_t\). If \(t=0\), choose any complete chain of subspaces from \(A\) to \(B\). If \(t\ge1\), choose \(v\in B\setminus W_t\); this is possible because \(W_t<B\). Since \(A\subset W_1\subseteq W_t\), we have \(v\notin A\), and \(A+\langle v\rangle\) has dimension \(\dim A+1\). Extend this first step to any maximal chain of subspaces ending at \(B\). Every intermediate member after the first step contains \(v\), whereas every omitted \(W_i\) excludes \(v\). Hence no omitted subspace appears in the chosen chain. Concatenate these chains for successive intervals between positive anchors. The resulting complete flag includes every positive query and excludes every negative query. Every labeling is realized.

**3. Exact counting.** A length-\(k\) chain of proper nonzero subspaces defines a uniquely determined ordered positive composition \((b_1,\ldots,b_{k+1})\) of \(n\), consisting of successive dimension gaps from \(0\) through the selected chain to \(V\). For a fixed composition, choosing successive subspaces amounts to choosing a \(b_i\)-dimensional subspace of each quotient of dimension \(n-b_1-\cdots-b_{i-1}\). There are precisely the displayed products of Gaussian binomial coefficients. Sum over compositions. At \(k=n-1\), all gaps equal one, yielding the classical full-flag count.

**4. Exact adaptive dimension.** For a fixed strict chain \(P\) of \(r\) proper nonzero subspaces, let \(\mathcal H_P\) be the family of complete flags containing every member of \(P\). We prove, by descending induction on \(r\), that
\[
\operatorname{Ldim}(\mathcal H_P)\le n-1-r,\qquad 0\le r\le n-1.
\]
When \(r=n-1\), the chain already specifies one subspace of every possible proper dimension, hence exactly one flag, and the dimension is zero. Suppose the bound holds for chains of size \(r+1\), and consider any query \(U\) at the root of a complete shattered decision tree for \(\mathcal H_P\). If \(U\) equals an anchor, belongs to \(P\), or is incomparable with a member of \(P\), its answer is constant over \(\mathcal H_P\) and it cannot split the hypothesis family. Otherwise \(P\cup\{U\}\) is a strict chain of size \(r+1\), so the positive branch has Littlestone dimension at most \(n-2-r\) by induction. The root of any shattered depth-\(d\) tree would require that positive branch to shatter depth \(d-1\). It follows that \(d\le n-1-r\). Setting \(P=\varnothing\) yields \(\operatorname{Ldim}\le n-1\). The inner members of any complete flag give a VC-shattered \((n-1)\)-element support by Step 2; a fixed shattered set of size \(n-1\) also yields a shattered adaptive tree of that depth, so the converse inequalities follow.

## Verification
A standalone exact checker `verify_flags.py` constructs *all* linear subspaces by finite-field span closure, all complete flags by nested inclusion, and the Boolean trace of every support within the declared ranges. It independently evaluates the Gaussian-binomial composition formula. The checker passed for prime-field cases \((q,n)=(2,2),(3,2),(2,3),(3,3),(5,3),(2,4)\). For the last pair it tests all 45,826 supports up to size three and all 315 complete flags. A separate checker `verify_boolean_limit.py` tests the formal Boolean-lattice limit \(q\to1\). Both scripts use only Python's standard library. The mathematical argument, rather than the finite test list, proves the claim for arbitrary prime powers and dimensions.

## Relationship to prior work
Flag-code literature studies collections of nested subspaces with metrics and code-distance parameters. Alonso-González, Navarro-Pérez and Soler-Escrivà (2020) construct distance-optimal flag codes; Alonso-González and Navarro-Pérez (2021) analyze combinatorial flag-distance patterns. Neither inspected paper gives these Boolean trace conditions, Gaussian-multinomial shattered-support counts, or adaptive-dimension equality. Braun and Hough (2018) investigate maximal chains in graded posets via homomorphism complexes; their chain-complex invariants differ from Boolean shattering. Guingona and collaborators (2021) examine VC and Littlestone dimensions of zero sets of functions, not complete-flag membership in a subspace lattice. The classical order-complex and complete-flag counts are not claimed as independently new: the contribution is identifying precisely the *shattered* support complex, all its face numbers, and the adaptive bound for this concept class.

Formally setting the Gaussian parameter to one gives the Boolean-lattice counterpart: the coefficient becomes \((k+1)!\left\{\begin{smallmatrix}n\\k+1\end{smallmatrix}\right\}\), where the braces denote Stirling numbers of the second kind. This degeneration illustrates the connection to permutation-prefix chains but does not treat the formal value one as a finite field.

## Limitations
Independent mathematical validation and exhaustive publication-priority verification have not been performed. An equivalent result may be recorded under a general maximal-chain shattering theorem or alternate terminology. The theorem addresses the full complete-flag family only, not restricted codebooks, rank-selected partial flags, or flag distance. The finite checker explicitly handles prime fields, while the proof uses only finite-dimensional linear algebra and therefore covers all prime powers. One intermediate historical comparison record was unavailable, and historical coverage cannot be treated as proof of uniqueness. The topology of the spherical building itself is classical and is not presented as a new homotopy computation.

## References
1. B. Braun and W. K. Hough, *Homomorphism Complexes and Maximal Chains in Graded Posets*, arXiv:1812.07335 (first public 2018-12-18).
2. C. Alonso-González, M. Á. Navarro-Pérez and X. Soler-Escrivà, *An Orbital Construction of Optimum Distance Flag Codes*, arXiv:2011.02724 (first public 2020-11-05).
3. C. Alonso-González and M. Á. Navarro-Pérez, *A Combinatorial Approach to Flag Codes*, arXiv:2111.15388 (first public 2021-11-30).
4. V. Guingona, A. Kolesnikov, J. Nierwinski and C. Soucy, *Littlestone and VC-Dimension of Families of Zero Sets*, arXiv:2109.04805 (2021).
