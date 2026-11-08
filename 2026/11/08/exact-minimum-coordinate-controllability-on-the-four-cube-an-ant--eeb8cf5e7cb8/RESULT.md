# Exact minimum-coordinate controllability on the four-cube: an antipodal parity rule and eight symmetry types

## Finding

Let \(Q_4\) be the unweighted, undirected hypercube with vertex set \(V=\{0,1\}^4\), where adjacent vertices differ in one coordinate. Consider the continuous-time linear system
\[
\dot z(t)=-Lz(t)+B_Su(t),\qquad L=4I-A(Q_4),
\]
where \(S\subseteq V\) is a set of *independently actuated vertices* and \(B_S\) is the \(16\)-by-\(|S|\) matrix whose columns are the standard coordinate vectors indexed by \(S\).

The minimum number of actuated vertices needed for Kalman controllability is **six**. A six-vertex set \(S\) is controllable **if and only if** both conditions hold:

1. It contains exactly one vertex from each of six distinct antipodal pairs \(\{x,x\oplus1111\}\), leaving exactly two antipodal pairs unrepresented.
2. The two unrepresented pairs have opposite Hamming-weight parity (one even and one odd; parity is well-defined on each pair).

Consequently there are exactly **\(1024\)** controllable six-vertex sets among the \(\binom{16}{6}=8008\) possible choices, or a fraction \(128/1001\). Under the graph automorphism group \(\operatorname{Aut}(Q_4)\cong(\mathbb Z/2\mathbb Z)^4\rtimes S_4\), these \(1024\) sets form exactly **eight orbits**, with sizes
\[
32,\ 32,\ 96,\ 96,\ 192,\ 192,\ 192,\ 192.
\]
By duality, the same classification applies to coordinate-state observability from six vertices.

## Assumptions and scope

All graph edges have unit weight, and the state generator is the full \(16\)-state combinatorial Laplacian \(-L\), not a reduced follower-only matrix. Inputs at distinct vertices are independently prescribed; one shared scalar input across the selected vertices is not covered. Controllability refers to the ordinary continuous-time Kalman/PBH property over \(\mathbb R\), for unrestricted real-valued time-varying inputs. Vertex labels are length-four binary vectors, and \(\oplus\) denotes bitwise addition modulo two. Hamming-weight parity is \(|x|\bmod2\). Because the dimension is even, \(x\) and its antipode \(x\oplus1111\) share parity.

## Proof

**Step 1: spectrum and sharp lower bound.** For each subset \(T\subseteq\{1,2,3,4\}\) define the Walsh character \(\chi_T(x)=(-1)^{\sum_{j\in T}x_j}\). Directly summing the four neighbors of \(x\) yields
\[
L\chi_T=2|T|\chi_T.
\]
The five eigenspaces, indexed by \(k=|T|\in\{0,1,2,3,4\}\), have dimensions \(\binom4k=(1,4,6,4,1)\). The PBH criterion for a real symmetric state matrix says that \((-L,B_S)\) is controllable precisely when each restricted Walsh matrix
\[
M_k(S)=\big(\chi_T(x)\big)_{x\in S,\ |T|=k}
\]
has full column rank \(\binom4k\). The dimension-six middle eigenspace therefore requires \(|S|\ge6\).

**Step 2: antipodal obstruction.** Suppose \(|S|=6\). Every degree-two character satisfies \(\chi_T(x\oplus1111)=\chi_T(x)\). Thus two selected antipodes would give identical rows of the square matrix \(M_2(S)\); it would be singular. Necessarily, \(S\) contains representatives of six different antipodal classes.

**Step 3: a complementary-minor equivalence.** Let \(H=\mathbb F_2^4/\langle1111\rangle\), an eight-element group, whose elements are precisely the antipodal classes. The degree-zero, degree-two, and degree-four characters exhaust its eight distinct real characters. Let \(W\) be the corresponding \(8\times8\) Walsh character table, with columns indexed by the even-weight subsets of \(\{1,2,3,4\}\). Orthogonality gives \(W^TW=8I\); hence \(W^{-1}=W^T/8\).

Let \(R\subset H\) consist of the six represented antipodal classes, let \(J\) consist of the six degree-two columns, and write \(H\setminus R=\{a,b\}\), \(J^c=\{\varnothing,\{1,2,3,4\}\}\). The selected square middle-eigenspace matrix agrees, up to row ordering, with \(W_{R,J}\). By Jacobi's complementary-minor identity for invertible matrices,
\[
\det(W_{R,J})\ne0\quad\Longleftrightarrow\quad
\det\big((W^{-1})_{J^c,\{a,b\}}\big)\ne0.
\]
The latter determinant is \(1/64\) times the determinant of
\[
\begin{pmatrix}1&1\\(-1)^{|a|}&(-1)^{|b|}\end{pmatrix}.
\]
It is nonzero exactly when the omitted antipodal classes have opposite parity. This proves that the two conditions are necessary and sufficient for full rank at eigenvalue \(4\).

**Step 4: the other eigenspaces cause no obstruction.** A nonzero real linear combination of the four degree-one characters is \(f(x)=\sum_{j=1}^4a_j(-1)^{x_j}\), with at least one \(a_i\ne0\). For any assignment to the other three bits, at most one of the two choices of \(x_i\) solves \(f(x)=0\). Hence at most eight of the sixteen vertices are zeros of \(f\). As \(f(x\oplus1111)=-f(x)\), its zero set consists of at most four antipodal pairs. Any six distinct antipodal classes therefore contain a sample where \(f\) is nonzero, proving \(\operatorname{rank}M_1(S)=4\). The degree-three character columns equal, up to reordering, the degree-one columns multiplied rowwise by the nowhere-vanishing parity character \(\chi_{\{1,2,3,4\}}\), so \(\operatorname{rank}M_3(S)=4\). The unique degree-zero and degree-four characters are nonzero at every vertex, giving rank one for each outer eigenspace. The PBH condition now holds at all eigenvalues.

**Step 5: exact counts and symmetry.** There are four even-parity and four odd-parity antipodal classes. Choose the omitted pair of classes in \(4\cdot4=16\) ways, and then independently choose one of two vertices in each of the six represented classes. This gives \(16\cdot2^6=1024\) distinct minimum actuation sets. The automorphism group acts as coordinate permutations followed by independent coordinate-bit flips; it has order \(4!2^4=384\). Exact finite orbit enumeration of this specified action on all the sets characterized above gives eight orbits of the stated sizes. A complete standalone verifier implements both this orbit calculation and a separate exact PBH-rank enumeration over every six-subset; its arithmetic is exact, and its assertions check the count, parity characterization, and eight orbit representatives. That certificate is the finite exhaustive justification of the orbit count.

The lower bound in Step 1 and the constructions in Steps 2–4 establish minimality. Since \(L\) is symmetric, replacing actuation by observation at the same coordinates transposes the Kalman matrices and gives the final dual statement.

## Verification

Run `python3 verify.py` using Python 3.8 or later, with no third-party dependencies. It checks all \(\binom{16}{6}=8008\) six-subsets against the PBH eigenspace-rank condition and against the independent antipodal-parity criterion; it also forms all automorphism orbits and asserts their sizes and representatives. Ranks are computed modulo \(257\). Every relevant determinant is a minor of a matrix with entries \(\pm1\) and order at most six, so Hadamard's bound gives absolute determinant at most \(6^3=216<257\). Therefore zero/nonzero modulo \(257\) is equivalent to zero/nonzero over \(\mathbb Q\); no probabilistic or floating-point rank inference is used. The structural proof of the parity characterization is independent of the exhaustive verification.

The canonical orbit representatives are specified by integers \(0,\ldots,15\), each denoting its four-bit binary expansion, with the least significant bit representing coordinate one:

| Orbit size | Representative (integer vertex labels) |
|---:|---|
| 32 | `0,1,2,5,6,7` |
| 32 | `0,1,6,7,10,11` |
| 96 | `0,1,2,3,4,5` |
| 96 | `0,1,6,7,10,13` |
| 192 | `0,1,2,3,4,9` |
| 192 | `0,1,2,4,9,10` |
| 192 | `0,1,2,5,6,11` |
| 192 | `0,1,2,5,11,12` |

## Relationship to prior work

The PBH test, the Cartesian-product Laplacian eigenstructure, and general necessary-and-sufficient grid-controllability tests are established in Notarstefano and Parlangeli (first arXiv public version 1 March 2012). In particular, its higher-dimensional repeated-eigenspace determinant procedure can be applied to the four-cube. The present classification is a specialized evaluation of those general conditions: an explicit *antipodal-parity rule*, a count of *all* minimum coordinate-input placements, and a complete *symmetry-orbit census*, which are not stated in its inspected treatment. Olshevsky (first arXiv version 10 April 2013) studies sparse diagonal actuation and proves general complexity and approximation results; those do not provide the four-cube's exact placement classification. Dai (2022) discusses general leader-set methods and solves other graph families, not this cube classification. General maximum-eigenvalue-multiplicity results explain the six-input lower bound but not its attainability with coordinate inputs, the parity obstruction, the \(1024\) count, or the orbit decomposition.

## Limitations

This theorem concerns exactly the unweighted four-dimensional cube and ordinary independent coordinate actuation/observation. It does not classify minimum leader sets for higher-dimensional hypercubes, under perturbed edge weights, or for follower-only principal submatrix dynamics. The orbit census is finite and exact, not an infinite-family claim. Reachability is algebraic; no statement is made about controllability Gramian conditioning, energy-optimal controls, numerical robustness, or structural controllability under arbitrary weights. The originality comparison is based on the inspected primary material and accessible research records, not a proof of publication priority; unindexed or inaccessible work may contain equivalent results. No independent mathematical audit has been performed.

## References

1. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129, first submitted 2012-03-01, https://arxiv.org/abs/1203.0129.
2. A. Olshevsky, *Minimal Controllability Problems*, arXiv:1304.3071, first submitted 2013-04-10, https://arxiv.org/abs/1304.3071; HTML https://arxiv.org/html/1304.3071v7.
3. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, first published 2022-10-29, https://doi.org/10.1049/cth2.12385.
4. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, and Y.-C. Lai, *Exact controllability of complex networks*, published 2013-09-12, https://doi.org/10.1038/ncomms3447 (general eigenvalue-multiplicity framework; accessible abstract only during this comparison).
