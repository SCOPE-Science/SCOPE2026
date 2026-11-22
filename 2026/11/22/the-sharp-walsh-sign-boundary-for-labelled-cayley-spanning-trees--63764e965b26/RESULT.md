# The sharp Walsh sign boundary for labelled Cayley spanning trees

## Finding

Let \(n\ge3\), let \(E=E(K_n)\), and let \(f_n:\mathbb F_2^E\to\{0,1\}\) indicate the edge-incidence vectors of all labelled spanning trees of the complete simple graph \(K_n\). For each frequency support \(S\subseteq E\), write its unnormalized Walsh coefficient as
\[
W_n(S)=\sum_{T\text{ spanning tree of }K_n}(-1)^{|S\cap T|}.
\]
Let \(C_n g=f_n*g\) denote unnormalized counting convolution on the Boolean edge group.

**Odd orders.** For every odd \(n\ge3\), \(W_n(S)\) is odd for every \(S\). Consequently \(C_n\) is invertible on all complex-valued functions on \(\mathbb F_2^E\), and has rank \(2^{\binom n2}\).

**Even orders and their first spectral zeros.** For \(n=2m\ge4\):

1. Every \(W_n(S)\) is strictly positive if \(|S|\le m-2\).
2. Every \(W_n(S)\) is nonnegative if \(|S|=m-1\). At that degree it equals zero **if and only if** \(S\) is an \((m-1)\)-edge star (all its edges meet at one vertex).
3. At degree \(m\), there exist strictly negative coefficients: an \(m\)-edge star is one such example.

Thus the first vanished Walsh frequency has exactly \(m-1\) edges. For \(n=4\) there are precisely \(\binom42=6\) first-degree zeros; for every even \(n\ge6\), their number is exactly
\[
n\binom{n-1}{n/2-1}.
\]
In particular, for all \(n\ge3\), the counting-convolution operator is invertible **if and only if \(n\) is odd**. No total nullity for the even case is claimed.

For completeness, a \(k\)-edge star \(S_k\), \(1\le k\le n-1\), has the exact signed coefficient
\[
W_n(S_k)=n^{n-2}\left(1-\frac{2(k+1)}n\right)\left(1-\frac2n\right)^{k-1}.
\]
This formula makes both the first zero at \(k=m-1\) and the first negative star at \(k=m\) explicit.

## Assumptions and scope

All graphs are finite, simple, undirected and vertex-labelled by \([n]\). All tree incidence vectors are considered as *distinct points* of \(\mathbb F_2^E\); each spanning tree has exactly \(n-1\) edges. The Walsh transform and convolution are unnormalized; in particular, \(W_n(\varnothing)=n^{n-2}\) by Cayley's enumeration. A frequency's degree is its number of selected *edges*, not its number of vertices. Statements about signs refer to real integers \(W_n(S)\), and convolution invertibility refers to the full complex (equivalently real) signal space.

The first-zero count distinguishes \(n=4\), because a single edge admits two choices of star centre. For larger even orders, a star of at least two edges has a unique centre. The theorem does not cover \(n=2\); in that trivial case its single-tree convolution is invertible.

## Proof

**1. Signed tree sum as a Laplacian determinant.** Let \(H_S=([n],S)\), and write \(L_S\) for its ordinary graph Laplacian, including isolates. Give each edge of \(K_n\) weight \(-1\) on \(S\) and \(+1\) off \(S\). The corresponding *net* weighted Laplacian is
\[
L_{\mathrm{signed}}=L_{K_n}-2L_S=nI-J-2L_S,
\]
where \(J\) is the all-ones matrix. The weighted matrix-tree identity, valid for these negative weights by its polynomial/Cauchy--Binet proof, makes each principal cofactor \(W_n(S)\). All Laplacians annihilate the all-ones vector. Thus, if \(0=\lambda_1,\lambda_2,\ldots,\lambda_n\) are the Laplacian eigenvalues of \(H_S\), counted with multiplicity and with any ordering of zero eigenvalues,
\[
\boxed{W_n(S)=\frac1n\prod_{j=2}^n(n-2\lambda_j).}\tag{1}
\]
Indeed, on the orthogonal complement of constants, \(nI-J-2L_S\) acts as \(nI-2L_S\), while the product of its \(n-1\) eigenvalues equals \(n\) times every cofactor. The identity continues to hold when further eigenvalues vanish.

**2. Sharp sparse Laplacian lemma.** Any simple graph \(H\) with exactly \(k\ge1\) edges (and any number of isolated vertices) satisfies
\[
\lambda_{\max}(L_H)\le k+1.
\tag{2}
\]
Equality holds exactly when its nonisolated edges form a star. To establish this without assuming connectedness, orient each of the \(k\) edges arbitrarily, let \(B\) be the vertex-edge incidence matrix, and note \(L_H=BB^T\). The nonzero eigenvalues equal those of the \(k\)-by-\(k\) Gram matrix \(B^TB\). Its diagonal entries are \(2\), and its off-diagonal entries are \(0\) for disjoint edges and \(\pm1\) for intersecting edges. The maximum absolute row sum is at most \(k+1\), proving (2).

If equality holds, the spectral radius of the entrywise absolute Gram matrix must equal \(k+1\). Its nonnegative row sums are at most \(k+1\). Equality forces every pair of the \(k\) edges to intersect: otherwise a connected component of its line graph has at most \(k-1\) edges (giving spectral radius at most \(k\)), or its connected full line graph has a row sum below \(k+1\) (giving strictly smaller Perron root). A pairwise-intersecting family of edges in a simple graph is either a star or, when \(k=3\), a triangle. The triangle has largest Laplacian eigenvalue \(3\), strictly smaller than \(k+1=4\). Stars have Laplacian spectrum \(k+1\) once, \(1\) with multiplicity \(k-1\), and zeros otherwise, so equality does occur and the characterization is complete. The case \(k=1\) is itself a star.

**3. Odd-order invertibility.** Modulo two, each summand in the Walsh coefficient is congruent to \(1\); hence
\[
W_n(S)\equiv n^{n-2}\pmod2.
\]
For odd \(n\), this is \(1\), independently of \(S\). No coefficient vanishes. The characters of the Boolean edge group diagonalize convolution, with multiplier \(W_n(S)\), proving full invertibility and the rank assertion.

**4. First zeros and first negative frequencies at even orders.** Let \(n=2m\). If \(|S|=k\le m-2\), (2) gives every \(\lambda_j\le k+1\le m-1\), so all factors \(n-2\lambda_j\) in (1) are strictly positive. For \(k=m-1\), they are nonnegative; a factor is zero exactly if \(\lambda_{\max}=m=k+1\), which by the equality case in (2) means exactly that \(S\) is a star.

For \(k=m\), an \(m\)-edge star has one Laplacian eigenvalue \(m+1\), its other positive eigenvalues being \(1\). Thus exactly one factor in (1) is negative and the coefficient is strictly negative. For \(n=4\), the first-zero stars are simply all six edges. For even \(n\ge6\), the unique star centre may be chosen in \(n\) ways and its \(m-1\) leaves in \(\binom{n-1}{m-1}\) ways. This proves the count, sharp sign boundary and even-order singularity.

**5. Star multipliers.** Substitute the displayed star Laplacian eigenvalues into (1). The \(n-1\) factors consist of \(n-2(k+1)\) once, \(n-2\) repeated \(k-1\) times, and \(n\) repeated \(n-k-1\) times. Rearranging yields the exact star formula stated above.

## Verification

The standalone standard-library program `verify_cayley.py` performs two independent types of exact arithmetic checks. It enumerates every labelled tree by Prüfer sequences at orders \(n=3,4,5,6\), constructs the Boolean tree indicator and executes an integer fast Walsh--Hadamard transform; for every frequency with at most three edges it independently compares its coefficient to an integer Laplacian cofactor. It finds no zeros at odd orders \(3,5\), and tests the exact edge-degree boundary at even orders \(4,6\).

Separately, a fraction-free Bareiss determinant calculation exhausts **every** edge-frequency with degree at most \(n/2-1\) for \(n=4,6,8\), verifying strict positivity below the boundary, zero equivalence with stars at the boundary, and exact counts \(6,60,280\). The program also checks a negative star frequency at degree \(n/2\) at those orders. Run `python3 verify_cayley.py` with Python 3 and no external packages. These finite checks corroborate the mathematical proof; they do not replace its all-order arguments.

## Relationship to prior work

Weighted matrix-tree methods express signed spanning-tree sums as cofactors. Klee and Stamps (2019, arXiv:1903.03575, especially Theorem 2 and the weighted matrix-tree discussion) specialize *vertex-product* edge weights \(x_ix_j\), whereas arbitrary negative **edge-frequency sets** need not have that form. Mallik (2022, arXiv:2210.03711, Theorem 3.6) gives the signed-tree difference for a general signed graph but does not derive a sharp frequency-support sign transition for complete-graph tree indicators. Farber and Kaminer (2011, arXiv:1106.0769) study general Laplacian eigenvalue bounds, not the equality classification of the first Walsh zeros.

A published theorem on quadratic Walsh sampling over the spanning-tree slice of \(K_n\) determines linear independence among degree-two coordinate functions **restricted to trees**; that sampling-rank question does not determine Fourier coefficients of the **tree-indicator function on the full Boolean edge group**. Published spectra for spanning trees of \(K_{2,n}\) address a different complete-bipartite host and do not imply the complete-graph formula. The present result is limited to the stated new sign and first-zero boundary, not an assertion that the general matrix-tree mechanism is new.

## Limitations

For even \(n\), the theorem establishes the exact *first* Walsh zero degree and all zero frequencies at that degree, but not all higher-degree zeros, total nullity, or sharp nonzero conditioning. The claimed generality does not extend automatically to other host graphs or to weighted tree measures. The all-order proof is mathematical rather than an external formal certificate. The literature comparison is bounded; an unindexed equivalent signed-tree specialization remains a priority risk. Independent mathematical audit has not been performed.

## References

1. M. Farber and I. Kaminer, *Upper bound for the Laplacian eigenvalues of a graph*, arXiv:1106.0769, first public version June 3, 2011, https://arxiv.org/abs/1106.0769.
2. S. Klee and M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, arXiv:1903.03575, first public version February 27, 2019, https://arxiv.org/abs/1903.03575.
3. S. Mallik, *Matrix tree theorem for the net Laplacian matrix of a signed graph*, arXiv:2210.03711, first public version October 7, 2022, https://arxiv.org/abs/2210.03711.
4. *Quadratic Walsh uniqueness on the spanning-tree slice of a complete graph*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quadratic-walsh-uniqueness-on-the-spanning-tree-slice-of-a-compl--8fece1c0bd0f.
5. *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-walsh-spectrum-and-sharp-fourier-projection-norms-for-t--89f45551846c.
