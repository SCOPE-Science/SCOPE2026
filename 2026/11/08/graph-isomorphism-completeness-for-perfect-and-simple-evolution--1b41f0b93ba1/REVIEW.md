# Scientific review: Graph-isomorphism completeness for perfect and simple evolution algebras over fixed finite fields

## Correctness — PASS

The proof starts from the defining multiplication and independently derives monomial rigidity when the structure matrix is invertible. Its complete scalar equations are \(a_{ij}s_j=s_i^2b_{\sigma(i),\sigma(j)}\). The two-colored graph's multiplicative-generator cycles compel exactly the admissible permutation-and-scaling maps; its square arcs enforce these same equations, including all zero entries. The vertex count is \(n(q-1)\), so graph encoding is polynomial for a fixed field. A directed edge-color-preserving graph reduces to ordinary graph isomorphism by source/target/edge-type incidence gadgets.

For GI-hardness, adjoining a unique universal hub and \(n+2\) leaves preserves and reflects isomorphism of an input graph while making it connected. The block matrix \(\left(\begin{smallmatrix}I+C&I\\I&0\end{smallmatrix}\right)\) is invertible, and its multiplication digraph is strongly connected. The looped versus unlooped natural-basis positions, one-to-one cross links, and unit loop coefficients force any algebra isomorphism to recover the original connected graph. The reduction yields simple algebras of dimension \(4n+6\) over every field.

The supplied independent algorithmic comparison exhausts \(2{,}340\) ordered pairs of invertible two-dimensional matrices over \(\mathbb F_2\) and \(\mathbb F_3\), plus \(225\) sample pairs over \(\mathbb F_4\), and verifies the simple-algebra construction on every simple graph with at most four vertices. These checks corroborate rather than prove the universal assertions. No unsupported lower bound in computational complexity is claimed.

## Originality — PASS (qualified)

The motivating October 15, 2026 survey of Kaygorodov, Martín González and Viruel explicitly poses the complexity of finite-field perfect evolution-algebra isomorphism relative to graph isomorphism as Question 50. Its monomial-rigidity theorem and graph-realization methods are acknowledged and used as foundations, not claimed as new. The resulting full two-way polynomial-time equivalence, including the simple-algebra restriction and \(n(q-1)\)-vertex scalar-action graph encoding, was not identified in the compared literature.

Falcón, Falcón and Núñez (2019) construct a total-colored graph from pairs of arbitrary algebra elements and discuss a faithful isotopy-to-graph functor. The full article's indexed Sections 3–5 explicitly leave the converse graph-morphism characterization open. Their graph can require exponentially many vertices in natural-basis dimension, and its announced functor does not furnish the present fixed-field many-one GI upper bound. Earlier Elduque–Labra work derives graph automorphism structure rather than this complexity equivalence. The strongest residual risk is that an equivalent efficient graph encoding appears in a less readily indexed computational-algebra source; an independent historical review remains outstanding.

## Mathematical value — PASS

The theorem resolves a specifically formulated 2026 complexity question for each fixed finite field, identifies the exact graph-isomorphism complexity class rather than offering merely a decision procedure, and remains hard under a stringent simplicity promise. The linear-size colored encoding is valuable for direct comparison of arbitrary perfect algebras, while the characteristic-independent simple-algebra gadget shows the obstruction is structural, not an artifact of singular or disconnected multiplication graphs. These are all-dimensional statements, not isolated small computations.

## Closest literature and limits

The relevant primary works are the 2026 evolution-algebra survey (arXiv:2610.22248v1, Question 50), Elduque and Labra's 2013 and 2019 graph/automorphism papers (arXiv:1312.4685 and arXiv:1902.02191), and Falcón–Falcón–Núñez (2019, DOI 10.3390/math7111068). Their covered structural ingredients are explicitly identified in the proof. Source-access limitations, potential implicit stronger coverage, and the varying-field input model are explained in the full audit and result. A separate independent audit has not taken place.

Self-review: passed. Independent audit: not yet performed.
