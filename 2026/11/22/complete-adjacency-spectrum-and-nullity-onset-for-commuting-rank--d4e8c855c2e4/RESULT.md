# Complete adjacency spectrum and nullity onset for commuting rank-one partial bijections

## Finding

Let \(\mathcal I_n\) denote the symmetric inverse monoid on an \(n\)-element set. Its rank-one Green \(\mathcal J\)-class consists of the \(n^2\) nonempty arrows \(a\mapsto b\). Form the simple **rank-one commuting graph** \(G_n\): distinct arrows are adjacent if they commute under partial-function composition. For every integer \(n\ge3\), the full real adjacency characteristic polynomial is
\[
\boxed{\det(tI-A_n)=\left[t^2-(n-1)^2t+(n-1)(n-2)\right]\left[t^2+(n-1)t-(n-2)\right]^{n-1}(t-n+2)^{n-1}(t+2)^{(n-1)(n-2)/2}t^{n(n-3)/2}.}
\]
Each quadratic factor contributes both of its real roots with its stated multiplicity. In particular
\[
\boxed{(n_+(A_n),n_-(A_n),n_0(A_n))=\left(2n,\frac{n(n-1)}2,\frac{n(n-3)}2\right).}
\]
The adjacency matrix is nonsingular at \(n=3\) and is singular for every \(n\ge4\), with exact nullity \(n(n-3)/2\) and rank \(n(n+3)/2\). This is the complete spectrum, not merely the inertia or the degree census.

## Assumptions and scope

The graph has precisely \(n^2\) vertices indexed by ordered pairs \((a,b)\), identified with a partial injection having domain \(\{a\}\), image \(\{b\}\) and value \(a\mapsto b\). All rank-one arrows are noncentral for \(n\ge3\); hence this is an induced subgraph of the standard commuting graph with central elements omitted. An edge joins two **distinct** arrows exactly when their products in either order are equal. The adjacency matrix has a zero diagonal, even if a single arrow has square zero. The spectrum and inertia are taken over \(\mathbb R\), not over a finite field. The case \(n=2\) is excluded because a surjectivity step changes at that boundary.

## Proof

**1. Semigroup multiplication becomes a two-coordinate graph condition.** Write \(e_{ab}\) for the arrow \(a\mapsto b\). The composition \(e_{ab}e_{cd}\) is empty unless \(b=c\), in which case it is the arrow \(a\mapsto d\). Similarly the reversed product is empty unless \(d=a\). For distinct arrows, if both products are nonempty then their source and target data force different arrows (unless the original arrows coincide). Consequently, for **distinct** \((a,b)\) and \((c,d)\), commutation holds exactly when \(b\ne c\) and \(d\ne a\).

**2. A linear operator on an \(n\)-by-\(n\) array.** Let \(X=(X_{ab})\) be a real matrix indexed by arrows, and set \(S=\sum_{a,b}X_{ab}\), \(R_a=\sum_b X_{ab}\), and \(C_a=\sum_b X_{ba}\). Inclusion--exclusion on the two forbidden index coordinates, followed by removal of the loop at every off-diagonal arrow, gives the **exact** adjacency action
\[
(A_nX)_{ab}=S-R_b-C_a+X_{ba}-(1-\delta_{ab})X_{ab}.
\]
This also makes clear why retaining the diagonal of the mutual-zero-product relation would give a different spectral problem. Since the formula commutes with transpose, real symmetric and skew-symmetric arrays form invariant direct-sum subspaces.

**3. Skew-symmetric sector.** If \(X^{\mathsf T}=-X\), then \(S=0\), \(C_a=-R_a\), and \(X_{aa}=0\). Thus
\[
(A_nX)_{ab}=R_a-R_b-2X_{ab}, \qquad R_a(A_nX)=(n-2)R_a(X).
\]
The map \(X\mapsto(R_a)_a\) from skew arrays onto the zero-sum vectors is surjective: a zero-sum vector \(r\) is realized by \(X_{ab}=(r_a-r_b)/n\). On its kernel the adjacency action is \(-2I\); on the quotient it is \((n-2)I\). This contributes \((t+2)^{(n-1)(n-2)/2}(t-n+2)^{n-1}\).

**4. Symmetric sector and the nullspace.** If \(X=X^{\mathsf T}\), write \(d_a=X_{aa}\). The operator and its row sums and diagonal obey
\[
(A_nX)_{ab}=S-R_a-R_b+\delta_{ab}d_a,
\]
\[
R_a(A_nX)=(n-1)S-nR_a+d_a,\qquad d_a(A_nX)=S-2R_a+d_a.
\]
The linear map from symmetric matrices to the pair of vectors \((R,d)\) is surjective for \(n\ge3\). Indeed, after prescribing the diagonal, assigning symmetric off-diagonal entries to arbitrary residual row sums is surjective because the unsigned vertex--edge incidence matrix of the complete graph has full row rank for \(n\ge3\): any vector \(u\) orthogonal to every edge column satisfies \(u_a+u_b=0\) for all distinct \(a,b\), hence \(u=0\). The kernel therefore has dimension \(n(n+1)/2-2n=n(n-3)/2\), and the displayed operator formula shows that \(A_n\) vanishes there.

On the constant subspace \(R_a=r,\ d_a=d\), so \(S=nr\), the induced two-by-two matrix in coordinates \((r,d)\) is
\[
M_0=\begin{pmatrix}n(n-2)&1\\n-2&1\end{pmatrix},\quad
\det(tI-M_0)=t^2-(n-1)^2t+(n-1)(n-2).
\]
On the \((n-1)\)-dimensional zero-sum space for \(R\) and \(d\), the repeated two-by-two matrix is
\[
M_1=\begin{pmatrix}-n&1\\-2&1\end{pmatrix},\quad
\det(tI-M_1)=t^2+(n-1)t-(n-2).
\]
This gives all factors of the asserted characteristic polynomial, since the invariant sectors and dimensions sum to \(n^2\).

**5. Exact inertia and sharp boundary.** For \(n\ge3\), the two roots of \(\det(tI-M_0)\) are positive because their sum is \((n-1)^2>0\), their product \((n-1)(n-2)>0\), and the real symmetric adjacency matrix ensures their reality. The two roots of \(\det(tI-M_1)\) have opposite signs because their product is \(-(n-2)<0\). Also \(n-2>0\) and \(-2<0\). Hence the positive count is \(2+(n-1)+(n-1)=2n\), the negative count is \((n-1)+(n-1)(n-2)/2=n(n-1)/2\), and the only zero eigenvalues are those from the symmetric kernel, of multiplicity \(n(n-3)/2\). This proves the stated singularity transition.

## Verification

Run `python3 checker.py` using Python 3 and SymPy. The independent checker constructs all rank-one partial maps, composes them in both orders rather than trusting the criterion in Step 1, checks that the criterion agrees for every pair, and computes exact rational/integer characteristic polynomials at \(n=3,4,5,6\). It also compares graph degrees and nullities. The companion `checker_output.txt` contains the actual recorded output. These finite tests support, but do not replace, the proof for every \(n\ge3\).

## Relationship to prior work

Araújo, Bentz and Konieczny [1] study the commuting graph of the entire symmetric inverse semigroup, including its clique numbers and diameters; they provide the semigroup and graph context, but do not give the complete adjacency spectrum of the rank-one induced subgraph. The previously published paper *Exact inertia of the mutual-annihilation matrix of the rook monoid* [2] determines inertia and a spectral product for the **loop-retaining mutual-zero-product matrix indexed by all ranks**. Its rank-one principal block is not the simple adjacency matrix here: for rank-one non-idempotent arrows its diagonal must be removed. Its result does not give the present eigenvalues, their multiplicities, or the rank-one nullity threshold. Ghosh and Parui [3] consider spectral questions for commuting graphs of **finite groups**, not partial injection monoids. The new calculation targets the minimal nonzero \(\mathcal J\)-class and all of its eigenvalues. An unknown broader association-scheme result could subsume the formula; search noncoverage is not a proof of novelty.

## Limitations

The theorem concerns the induced graph on rank-one partial bijections, not the full commuting graph or its higher-rank induced strata. All eigenvalues are over \(\mathbb R\). Computed small cases are not treated as a proof for unbounded \(n\). The precise formula is established here, but an independent audit and an exhaustive historical-priority verification have not been performed.

## References

1. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664, first posted 8 May 2012, https://arxiv.org/abs/1205.1664; published in Israel Journal of Mathematics 207 (2015), DOI: https://doi.org/10.1007/s11856-015-1173-9 .
2. *Exact inertia of the mutual-annihilation matrix of the rook monoid*, published research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-inertia-of-the-mutual-annihilation-matrix-of-the-rook-mono--72b990ba98ea/RESULT.md .
3. G. Ghosh and S. Parui, *On the spectra of Commuting Graphs*, arXiv:2104.14967, posted 29 April 2021, https://arxiv.org/abs/2104.14967 .
