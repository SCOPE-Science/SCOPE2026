# Certified productivity of crown-graph cores for Schur idempotents

## Finding

Let \(C_n\) be the bipartite crown graph with \(n\) row and \(n\) column vertices and biadjacency matrix \(J_n-I_n\). Write \(T_{C_n}(1000^{[12]})\) for the bipartite graph obtained by attaching a regular rooted tree with \(1000\) children per vertex and height \(12\) to each vertex of \(C_n\). A graph carries the idempotent Schur multiplier formed by entrywise multiplication by its zero-one biadjacency matrix; its multiplier norm is \(\|\cdot\|_{\bullet}\).

**Theorem.** For every integer \(n\ge15\),
\[
\|T_{C_n}(1000^{[12]})\|_{\bullet}>\frac{20029}{10000}>2>\|C_n\|_{\bullet}=\frac{2(n-1)}n.
\]
In particular, every \(C_n\) with \(n\ge15\) is a productive core in the sense of Levene (2026), with parameters \((R_0,h_0)=(1000,12)\). The definition and sufficient criterion in that work then produce nondegenerate intervals of idempotent Schur norms from each such core. This last implication uses the established productive-core theorem and is not a new general half-line theorem.

## Assumptions and scope

The Schur multiplier norm is the norm on complex bounded operators between the two \(\ell^2\) spaces indexed by the row and column vertices. For a finite zero-one matrix \(B\), this is \(\sup_{\|X\|\le1}\|B\circ X\|\). All trees in the theorem are finite, with exactly twelve edges on a longest path starting at each core vertex. The graph \(C_n\) is row/column vertex-transitive: simultaneous permutations of row and column indices and interchanging the two parts preserve adjacency. The source's productivity criterion requires a norm strictly larger than both \(2\) and the core norm; it does not require a best-possible branching number or tree height.

## Proof

**1. The core.** The singular values of \(J_n-I_n\) are \(n-1\) once and \(1\) with multiplicity \(n-1\). The transitive-core Schur norm formula (Levene 2026, equation (3.1)) therefore gives
\[
\|C_n\|_{\bullet}=\frac{(n-1)+(n-1)}n=\frac{2(n-1)}n<2.
\]

**2. Exact tridiagonal reduction.** We establish the strict bound first at \(n=15\). Put \(h=12\), \(R=1000\), and choose the integer vector
\[
 u=(1000,691,622,556,493,432,373,317,262,208,155,103,51),
 \qquad S=\sum_{k=0}^{12}u_k^2.
\]
Assign total row weight and total column weight \(x_k=u_k^2/S\) at depth \(k\), uniformly over the \(15R^k\) vertices of either color at that depth. The dual trace-class formula for finite Schur multipliers yields a lower bound at this weight.

For a symmetric tridiagonal matrix, write \(Q(c_\ell,\ldots,c_{h-1})\) for the matrix of order \(h-\ell+1\) with zero diagonal and nonzero entries \(c_k\) immediately above and below the diagonal. Define
\[
 c_k=\frac{u_ku_{k+1}}{15R^k}\quad(0\le k<12),
 \quad A_+=\frac{14}{15}u_0^2 E_{11}+Q(c_0,\ldots,c_{11}),
 \quad A_-=\frac1{15}u_0^2 E_{11}+Q(c_0,\ldots,c_{11}).
\]
For \(1\le\ell\le11\) put \(A_\ell=15(R-1)R^{\ell-1}Q(c_\ell,\ldots,c_{11})\); equivalently, its off-diagonal entries in order are
\[
 (A_\ell)_{j,j+1}=(A_\ell)_{j+1,j}
 =\frac{(R-1)u_{\ell+j-1}u_{\ell+j}}{R^j},\qquad 1\le j\le12-\ell.
\]
All the matrices here have **rational** entries. The exact weighted-norm formula is
\[
 \|T_{C_{15}}(R^{[12]})\|_{\bullet}\ge
 \frac{\|A_+\|_1+14\|A_-\|_1+\sum_{\ell=1}^{11}\|A_\ell\|_1}{S}. \tag{1}
\]
For clarity, this formula follows by forming the weighted bipartite adjacency matrix and decomposing it under the depth-to-depth partial isometries. The core contributes two signed eigenvalue copies of each singular value; taking half the adjacency trace norm produces the coefficient \(1\) for \(A_+\) and \(14\) for \(A_-\). The other chains begin at each fresh layer, with multiplicity \(15(R-1)R^{\ell-1}\), exactly as in Levene (2026, Theorem 3.8). Thus (1) does not replace an infinite problem with an unproved finite heuristic.

**3. Exact rational certificate.** The attached file `schur_productive_certificate.json` stores thirteen symmetric integer matrices \(Z_B\), one for each matrix \(B\) in the collection \(A_+,A_-,A_1,\ldots,A_{11}\), and a common integer scale \(Q=10^7\). Put \(H_B=Z_B/Q\). The standalone checker `verify_schur_productivity.py` reconstructs all rational matrices independently from \(u\), \(R\), and \(n\), checks every symmetry and dimension, and verifies *exactly with integer arithmetic* that
\[
 \max_i\sum_j |(H_B^2-I)_{ij}|\le\frac{2}{100000}
 \quad\text{for all thirteen }B.\tag{2}
\]
Because \(H_B\) is symmetric, (2) implies \(\|H_B\|_{\mathrm{op}}^2\le1+2/100000\le(1+1/100000)^2\). The dual formula for trace norm therefore gives
\[
 \|B\|_1\ge\frac{\operatorname{tr}(H_B B)}{1+1/100000}.
\]
The same exact-rational checker calculates
\[
 T=\operatorname{tr}(H_{A_+}A_+)+14\operatorname{tr}(H_{A_-}A_-)
 +\sum_{\ell=1}^{11}\operatorname{tr}(H_{A_\ell}A_\ell)
\]
and verifies the strict *integer-rational* inequality
\[
 T>\frac{20029}{10000}\left(1+\frac1{100000}\right)S.\tag{3}
\]
Equations (1)--(3) prove the displayed finite-graph bound without trusting floating-point eigenvalues or numerical optimization. Approximate floating-point singular-vector calculations were used solely to discover the integer matrices; they play no role in verifying (2)--(3).

**4. All larger crown cores.** For each \(n\ge15\), choosing fifteen rows and the corresponding fifteen columns of \(J_n-I_n\), together with their attached depth-twelve trees, gives an induced copy of \(T_{C_{15}}(R^{[12]})\). The Schur multiplier norm cannot decrease when passing from an induced subgraph to the full graph, since the former is a matrix compression. Hence every \(n\ge15\) satisfies the same strict lower bound. The core norm from step 1 is less than \(2\), so the productivity criterion is fulfilled.

## Verification

Run `python verify_schur_productivity.py schur_productive_certificate.json` with Python 3's standard library. The executable proof reads the thirteen supplied integer dual matrices, constructs all rational tridiagonal blocks, bounds their operator norms by an exact matrix-square computation, and compares rational integers in (3). A successful execution prints `VERIFIED exact rational certificate` and a certified lower bound approximately \(2.002944900198419\), strictly exceeding \(2.0029\). This numerical rendering is explanatory; acceptance is decided by exact `Fraction` comparisons. The inputs, checker and its proof instructions are all embedded beside this document.

## Relationship to prior work

Rupert H. Levene's *A half-line of Schur idempotent norms* (2026), Theorem 3.8, supplies the general tridiagonal reduction and Section 4 supplies the productivity criterion. Section 5 proves productivity for \((J_3-I_3)\otimes(J_4-I_4)\). Crucially, Section 6 states that this was the only *proved* productive core and reports the crown-core case \(J_{15}-I_{15}\) at branching \(1000\), height \(12\), as a **numerical observation that had not been certified**. The theorem here rigorously establishes precisely that missing strict inequality, with an explicit margin, and consequently an entire family of productive crown cores. The paper's general existence of a half-line of Schur norms is credited, not claimed as new. Levene (2014) determines small Schur-idempotent norms, while Beke--Goh--Hatami--Jaffe--Naylor (2026) establish a structural block decomposition. Neither of these inspected results supplies the required strict crown-core spectral certificate.

## Limitations

The threshold \(15\) is a certified sufficient cutoff, not a proven least possible one. This proof does not compute the exact Schur multiplier norm, characterize optimal weights, improve the general first interval's location, establish a half-line starting at \(2\), or resolve whether other smaller crown cores are productive. It uses a particular large branching number and height. An unlocated independent certificate or more general theorem could predate the present computation; the searches reported in the review do not certify absolute priority.

## References

1. R. H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (first public 2026-11-05), especially Theorem 3.8, Definition 4.2 and Section 6. https://arxiv.org/html/2611.08419v1
2. R. H. Levene, *Norms of idempotent Schur multipliers*, New York J. Math. 20 (2014), 325--352. https://nyjm.albany.edu/j/2014/20-19v.pdf
3. C. Beke, M. K. Goh, H. Hatami, S. Jaffe and D. Naylor, *A characterization of idempotent Schur multipliers*, arXiv:2607.14316v3 (2026). https://arxiv.org/html/2607.14316v3
