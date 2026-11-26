# Unique sparsest primitive bistochastic cube roots of complete triangle sweeps

## Finding

Let \(S_{ij}\) be the \(3\times3\) permutation matrix interchanging states \(i,j\), and let \(B_{ij}(p)=pI+(1-p)S_{ij}\) for \(0<p<1\). A **complete triangle sweep** is a product of the three matrices \(B_{12}(p),B_{23}(p),B_{13}(p)\), in any order, with a common weight \(p\).

Five positive entries are necessary and sufficient for the smallest support of a primitive three-state doubly stochastic matrix. Every primitive matrix with that support size is, up to simultaneous relabeling, the matrix
\[
P(p)=\begin{pmatrix}0&0&1\\ p&1-p&0\\1-p&p&0\end{pmatrix},\quad 0<p<1.
\]
Its third power is a complete triangle sweep. Conversely, every complete triangle sweep has **exactly one** primitive doubly stochastic cube root with five positive entries, as a matrix on the given labeled states. The root's parameter is the sweep's parameter \(p\). Thus an ordered sweep of three different pair updates can be implemented by iterating one time-homogeneous sparse transition three times, and that implementation is unique within the sparsest primitive bistochastic class.

## Assumptions and scope

Doubly stochastic means nonnegative with row and column sums one; primitive means that some positive integer power has all entries strictly positive. Support size counts positive entries, including loops. The sweep weights are equal and interior. The uniqueness is among primitive doubly stochastic roots of minimal support size. It does not rule out stochastic cube roots with more entries or with other invariant distributions.

## Proof

By the Birkhoff–von Neumann theorem, a doubly stochastic matrix is a convex combination of permutation matrices. Two distinct permutations disagree in at least two rows, so their union has at least five positive positions. A permutation matrix is not primitive. If the union has five positions, two distinct contributing permutations share a single cell. Their support is the shared cell and one alternating square on the other two rows and columns; it admits only those two perfect matchings. The combination is therefore strictly interior and unique. If the shared cell is diagonal, the shared state is absorbing. If it is off-diagonal, the two permutations are a transposition and a three-cycle. For each of the six ordered off-diagonal cells there is exactly one such pair: once the shared cell is specified, the other two rows can be matched in two ways. They all lie in one orbit under simultaneous relabeling.

For the cell \((1,3)\) the two permutations are \(S_{13}\) and the cycle
\[
C=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]
Their mixture \(pC+(1-p)S_{13}\) is \(P(p)\). It is primitive because its support contains a directed three-cycle and a self-loop on that cycle. In particular five entries suffice. The coefficient of the three-cycle is invariant under simultaneous relabeling and fixes the representation's parameter.

With matrices acting on the right of row vectors, \(S_{13}C^{-1}=S_{23}\), so \(P(p)=B_{23}(p)C\). Conjugating the transposition factor by successive powers of \(C\) gives the two other factors. Since \(C^3=I\),
\[
P(p)^3=B_{23}(p)B_{13}(p)B_{12}(p).
\]
Permuting vertices induces every permutation of the three edges of the triangle. Hence all complete triangle sweeps of weight \(p\) are conjugate to this product and have one of the stated cube roots.

Now fix a sweep \(M\) and suppose its root is primitive and doubly stochastic with five positive entries. It must be a relabeling of \(P(q)\) for some \(0<q<1\). The determinant of each \(B_{ij}(p)\) is \(2p-1\), while \(\det P(q)=2q-1\). Thus \((2q-1)^3=(2p-1)^3\) and \(q=p\).

It remains to show that no two relabelings give different sparse roots of the same labeled sweep. It suffices to check the representative \(M_0=B_{13}(p)B_{23}(p)B_{12}(p)\), since all sweep orders are conjugate. The diagonal of \(M_0\) is \((p^2+(1-p)^3,p^2,p^2)\): in expanding the three factors, products of two distinct swaps are three-cycles and contribute no diagonal; the three-swap product fixes state 1. The only nonidentity permutation preserving this diagonal is the swap of states 2 and 3. But \((M_0)_{12}=p(1-p)(2-p)\) and \((M_0)_{13}=p(1-p)\), as obtained by multiplying the corresponding row and columns, so that swap does not stabilize \(M_0\). The permutation stabilizer is trivial. If conjugating \(P(p)^3\) by two permutations gives the same \(M\), those permutations are therefore identical. This proves labeled uniqueness, including at \(p=1/2\) where the sweep is singular.

## Verification

The proof determines all roots within the stated class for every real \(p\in(0,1)\). The accompanying exact rational checker verifies the conjugacy classification, the power identity, and the uniqueness assertions on a finite parameter grid. Those checks supplement rather than replace the proof.

## Relationship to prior work

The dimension-three Birkhoff decomposition-length result [1] counts terms, not matrix entries. The complete sweep has been analyzed as a three-season population return [2], and for \(p>1/2\) as an equal-time heat sweep with \(2p-1=e^{-2t}\) [3]. The power identity above is an equality of matrices, up to the indicated relabeling. It transfers spectral rates and Jordan information from the known sweeps: the rate per sparse step is the cube root of the rate per completed sweep. In particular the known heat-sweep exceptional optimum corresponds to \(p=4-2\sqrt3\) and per-step rate \(2-\sqrt3\). No novelty is claimed for the spectral collision, optimization over the positive heat-time branch, or the transferred Jordan correction. General matrix-root theory [5] characterizes candidate roots and proves that a nonnegative root of an irreducible stochastic matrix has unit row sums; this does not by itself settle the support of the roots. The structural assertion here is exhaustive classification at the five-entry threshold and existence and uniqueness of sparse stochastic cube roots of the labeled sweeps.

## Limitations

No assertion is made about nonuniform stationary measures, unequal sweep weights, more than three states, or cube roots outside the minimum-support primitive class. The sweep is a discrete matrix product; this does not equate physical times or optimize finite-horizon total variation.

## References

1. *A complete two-endpoint minimum Birkhoff decomposition law in dimension three*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-complete-two-endpoint-minimum-birkhoff-decomposition-law-in-di--21b7692ab8b7).
2. *Complete three-transposition resonance in a quadratic population flow*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-complete-three-transposition-resonance-in-a-quadratic-population--88595ecbbef3).
3. *An exceptional-point optimum for cyclic three-edge heat sweeps*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-an-exceptional-point-optimum-for-cyclic-three-edge-heat-sweeps--e5717c1e661f).
4. G. Birkhoff, *Three observations on linear algebra*, Univ. Nac. Tucumán Rev. Ser. A 5 (1946), 147–151.
5. N. J. Higham and L. Lin, *On pth roots of stochastic matrices*, Linear Algebra Appl. 435 (2011), 448–463, [open preprint](https://eprints.maths.manchester.ac.uk/1429/1/covered/MIMS_ep2009_21.pdf), §3.
