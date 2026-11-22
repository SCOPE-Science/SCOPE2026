# The nine-vertex threshold for nonunimodular single-node Laplacian reachability on trees

## Finding

For every unweighted tree \(T\) with \(n\le8\), and any single coordinate input at vertex \(r\), the integer-valued Kalman controllability matrix
\[
K(T,r)=[e_r,(-L_T)e_r,\ldots,(-L_T)^{n-1}e_r]
\]
is either singular or unimodular. The smallest failure occurs at **nine vertices**: exactly one unrooted nine-vertex tree shape has any coordinate actuator for which the matrix is nonsingular but nonunimodular. This shape has exactly two such vertices, interchanged by an automorphism, and their determinant is \(-2\). There are no other nonunit nonzero determinants on trees of order at most nine.

This resolves the sharp finite-size onset of a distinction between ordinary real controllability and unrestricted signed **integer-input** reachability. At the exceptional root, exactly half the integer target states are unreachable.

## Assumptions and scope

All graphs are simple, connected, undirected, with **unit edge conductances**. The combinatorial graph Laplacian is \(L_T=D_T-A_T\). Vertices are labeled \(0,\ldots,n-1\) when a representative is displayed. Set \(B=-L_T\), and take the system \(x_{t+1}=Bx_t+e_ru_t\), with \(x_0=0\) and arbitrary signed \(u_t\in\mathbb Z\). The \(n\)-step reachable set is exactly the column lattice \(K(T,r)\mathbb Z^n\); column reversal does not affect this lattice. The result does not address weighted trees, fractional controls, multiple inputs, or minimization of control magnitude.

For the exceptional nine-vertex representative use the edges

```text
(0,1) (0,2) (0,3) (1,4) (1,5) (2,6) (3,7) (4,8)
```

Only roots \(2\) and \(3\) have \(|\det K|=2\). The automorphism \((2\,3)(6\,7)\) interchanges them. For the root \(2\), a parity witness is the vector with ones at indices \(0,5,6,7\) and zeros elsewhere.

## Proof

**1. Exhaustive shape generation.** Begin with the unique one-vertex tree. From each nonisomorphic \((n-1)\)-vertex tree, attach a new vertex to each possible existing vertex, and remove isomorphic duplicates. Every \(n\)-vertex tree has a leaf; deleting it produces an \((n-1)\)-vertex tree, proving by induction that this generates every tree. Duplicates are removed by the canonical code obtained as follows: for a fixed root, write a pair of parentheses around the lexicographically sorted list of the codes of its child branches; minimize this code across all root choices. By induction on rooted trees, these balanced-parenthesis codes agree exactly for isomorphic rooted trees. Minimization yields a complete invariant for unrooted trees. This proves the generator exhaustiveness independent of a published tree table.

**2. Exact determinant evaluation.** For each generated tree and every vertex, construct all powers of \(-L_T\) applied to \(e_r\) using only integer arithmetic. Replacing \(-L_T\) by \(L_T\) only changes column signs, so the absolute determinant is unchanged. Compute the determinant twice: fraction-free Bareiss elimination with exact divisions and an independent rational Gaussian elimination with pivoting. The independent methods agree on every one of the \(749\) rooted instances with \(n\le9\). The following complete count table gives, for each order, all possible determinant absolute values and their number of rooted **representative** instances. These are not counts of labeled trees.

| \(n\) | Unrooted shapes | \(|\det|=0\) | \(|\det|=1\) | \(|\det|=2\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 | 0 |
| 2 | 1 | 0 | 2 | 0 |
| 3 | 1 | 1 | 2 | 0 |
| 4 | 2 | 4 | 4 | 0 |
| 5 | 3 | 9 | 6 | 0 |
| 6 | 6 | 26 | 10 | 0 |
| 7 | 11 | 62 | 15 | 0 |
| 8 | 23 | 146 | 38 | 0 |
| 9 | 47 | 361 | 60 | 2 |

In order nine the two \(|\det|=2\) instances have the single edge list displayed above and roots \(2,3\), each with determinant \(-2\). All nonzero values at lower orders have absolute value one. This finite exhaustive certificate establishes the first and uniqueness assertions. Its algorithm, exact arithmetic, full checks and expected outputs are embedded in `verify_tree_census.py`; it uses only the Python standard library.

**3. Integer-reachability obstruction and completeness.** For root \(2\) of the exceptional tree, let \(w=e_0+e_5+e_6+e_7\). Direct integer matrix multiplication, also asserted by the checker, gives \(w^\mathsf{T}K(T,2)\equiv0\pmod2\). Since the integral matrix has determinant \(-2\), its full-rank image lattice has index \(2\) in \(\mathbb Z^9\). The kernel of the nonzero parity map \(z\mapsto w^\mathsf{T}z\bmod2\) also has index \(2\), hence the image lattice equals that kernel. The graph symmetry proves the same result for root \(3\). For \(n\)-step integer-input reachability, the image of \(K\) is precisely the set of possible states, because chronological input order only reverses its columns. By the characteristic-polynomial identity and its *integer* coefficients, all higher powers of \(-L_T\) lie in the integer span of its first \(n\) powers, so allowing more steps does not enlarge the reachable lattice. In particular, the target \(e_0\) is real-reachable but is never integer-reachable at the exceptional roots.

## Verification

Run `python verify_tree_census.py` with a standard Python interpreter. No packages or external files are needed. It enumerates all tree shapes on one through nine vertices using canonical leaf-extension, constructs \(749\) root instances, computes each exact determinant by two independent algorithms, verifies every frequency in the table, and checks the parity witness. The resulting terminal line is `PASS all n <= 9, independent rational and fraction-free determinants`. The certificate is finite and exhaustive through order nine; it makes no all-orders claim.

## Relationship to prior work

Ji, Lin, Lee and Ling (2010) give a tree-topology criterion for ordinary real multi-agent controllability through eigenspace conditions and follower-submatrix eigenvalue interlacing. Parlangeli and Notarstefano (2011) characterize real reachability for paths and cycles. Their conclusions do not determine the **integer index** of a nonsingular Kalman column lattice, nor the sharp nine-vertex threshold under arbitrary unweighted tree shape and coordinate root. Earlier exact unimodularity results on paths and hub-actuated spiders concern restricted tree families and do not imply the present first nonunimodular double-branch example or its finite minimality.

## Limitations

The minimality and uniqueness result is a completely enumerated finite-size classification, **not** an infinite classification of all trees. It is sensitive to unit weights, the fixed Laplacian normalization and integer-control assumptions. The numerical certificate is reproducible and exact, but independent third-party validation and publication-priority determination have not been performed. Related general walk-matrix literature not located by the searches could contain equivalent tables or deductions.

## References

- Z. Ji, H. Lin, T. H. Lee and Q. Ling, *Multi-agent Controllability with Tree Topology*, American Control Conference, Baltimore, June 30–July 2, 2010. https://www3.nd.edu/~hlin1/Papers/2010/ACC10_MAS.pdf
- G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, publicly submitted September 16, 2011. https://arxiv.org/abs/1109.3556
