# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The subalgebra classification was checked directly from the central extension
\[
H_m=V\oplus \mathbb F_qz,\qquad [v,w]=\omega(v,w)z.
\]
A subalgebra containing \(z\) is exactly the full inverse image of a subspace of \(V\). If it does not contain \(z\), projection to \(V\) is injective, so it is a graph over a subspace \(W\); bracket closure is exactly total isotropy of \(W\).

For graph subalgebras \(A(W,f)\) and \(A(U,g)\), the criterion
\[
z\in A+B
\Longleftrightarrow
f|_{W\cap U}\ne g|_{W\cap U}
\]
was checked explicitly. When the restrictions differ, every bracket lies in the sum. When they agree, the sum contains no nonzero central vector, so permutability is equivalent to \(\omega(W,U)=0\).

For \(m=2\), the symplectic incidence counts were checked independently. A four-dimensional symplectic space has
\[
N=(q+1)(q^2+1)
\]
isotropic lines and the same number of Lagrangian planes. A fixed line has \(q^3\) nonorthogonal lines and is contained in \(q+1\) Lagrangian planes. For a fixed Lagrangian plane, \(q(q+1)\) other Lagrangians meet it in a line and \(q^3\) are disjoint. Combining these counts with the number \(q^{r+s-d}\) of functional pairs agreeing on a \(d\)-dimensional intersection gives
\[
B(q)=q^4(q+1)(q^2+1)(q^3+2q^2+4q+1).
\]
The total subalgebra count
\[
S(q)=q^5+3q^4+5q^3+6q^2+4q+6
\]
follows independently from the Gaussian-binomial count of subspaces containing the center and the isotropic-graph count.

The formula specializes for \(m=1\) to the published \(H_1\) expression, providing a consistency check. A direct exhaustive computation for \(q=2,3\), included as a compact verification artifact, gives respectively \((S,B)=(158,6000)\) and \((693,187920)\), exactly matching the symbolic formulas. The proof for arbitrary \(q\) is combinatorial and does not rely on the computation.

## Originality

PASS, to the best of our knowledge.

The full current text of arXiv:2609.19086v1 was inspected at Definition 1.1, the Heisenberg discussion and Theorem 1.2, its proof, and the Lazard-correspondence theorem. The paper explicitly asks for \(\operatorname{sd}(H_m)\) and gives a closed computation only for \(H_1\); no \(H_2\) formula appears in the current v1.

The group-theoretic subgroup commutativity degree is substantial prior art. Tărnăuceanu's arXiv:1312.0296 was inspected and treats finite \(P\)-groups rather than extraspecial Heisenberg-type groups. Searches for “subgroup commutativity degree” together with extraspecial \(p\)-groups or Heisenberg groups, and searches for the resulting subalgebra-count and numerator polynomials, did not locate an equivalent \(H_2\) formula. Literature on element commutativity degree and exterior degree of Heisenberg Lie algebras concerns different invariants and is not evidence of coverage.

There remains a material residual risk from older finite-group or finite-polar-space literature: for odd prime fields, the Lazard correspondence identifies the present Lie-algebra invariant with a subgroup commutativity degree of the corresponding exponent-\(p\) Heisenberg group, so an unlocated extraspecial-group formula could cover that specialization. Standard descriptions of Heisenberg subalgebras by isotropic geometry and standard symplectic incidence numbers are therefore treated as prior art rather than claimed discoveries.

The current source preprint was submitted on 16 September 2026 and is recent enough that later revisions or contemporaneous independent work are an additional originality risk.

## Value

PASS.

The source paper presents computing \(\operatorname{sd}(H_m)\) as a natural problem and solves only the three-dimensional case. The result supplies the next nontrivial case \(H_2\) in closed form over every finite field, while the graph/intersection criterion turns the entire Heisenberg family into a concrete finite symplectic-incidence problem. The computation is exact rather than asymptotic or experimental.

## Limitations

No closed formula for every \(m\ge3\) is claimed. The general structural reduction still leaves symplectic incidence enumeration to be performed. Originality is to the best of our knowledge and is not independent validation. The exhaustive artifact checks only \(q=2,3\); it supports the symbolic calculation but is not a substitute for the general proof.
