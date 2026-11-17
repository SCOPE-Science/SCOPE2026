# Sharp simplicity failure and scheme rigidity in random finite-field evolution algebras

## Finding
Fix any prime power \(q\ge 2\). For each \(n\ge 1\), choose \(M\) uniformly from \(\operatorname{GL}_n(\mathbb F_q)\), and define the perfect evolution algebra \(E_M\) with natural basis \(e_1,\ldots,e_n\) by \(e_ie_j=0\) for \(i\ne j\) and \(e_i^2=\sum_j M_{ij}e_j\). Then, as \(n\to\infty\) with \(q\) fixed,
\[
\Pr(E_M\text{ is not absolutely simple})
=\frac{2n(q-1)}{q^n-1}+O_q(n^2q^{-2n}). \tag{1}
\]
Moreover, the full affine automorphism *group scheme* of \(E_M\), not merely its rational-point group, is trivial with probability tending to one exponentially fast. More precisely, let
\[
c_{q,n}=\prod_{j=1}^{n}(1-q^{-j}),\qquad
\alpha_q=(q-1)^2/q^2+1/q^2<1.
\]
For \(n\ge2\), the joint failure probability satisfies
\[
\Pr\bigl(E_M\text{ not absolutely simple}\ \text{or}\
\operatorname{Aut}(E_M)\ne\mathbf 1\bigr)
\le c_{q,n}^{-1}\left(
\sum_{s=1}^{n-1}\binom ns q^{-s(n-s)}+q^{-n}
+\sum_{k=2}^{n} n^k\alpha_q^{(2nk-k^2)/2}
\right). \tag{2}
\]
The right-hand side is exponentially small at fixed \(q\). Consequently, if \(M\) is instead uniform among *all* \(n\times n\) matrices, the unconditional simplicity probability satisfies
\[
\Pr(E_M\text{ simple})=c_{q,n}\left(1-\frac{2n(q-1)}{q^n-1}+O_q(n^2q^{-2n})\right), \tag{3}
\]
so it tends to \(c_q=\prod_{j\ge1}(1-q^{-j})>0\).

## Assumptions and scope
The structure coefficients are independent uniform elements of \(\mathbb F_q\) before conditioning on invertibility; the conditional model is the uniform distribution on \(\operatorname{GL}_n(\mathbb F_q)\). The bound in (2) is for \(n\ge2\), and (1) and (3) are fixed-\(q\) asymptotics with constants that may depend on \(q\). A simple algebra means a nonzero algebra with nonzero multiplication and no nonzero proper two-sided ideals; for commutative evolution algebras these are ordinary ideals. Absolutely simple means simple after extending scalars to any field extension. The affine group scheme is trivial when its functor of automorphisms has one element for every commutative \(\mathbb F_q\)-algebra. We count labeled structure matrices, not isomorphism classes.

## Proof
**1. Ideals and strong connectivity.** Let \(\Gamma_M\) be the directed support graph with an arrow \(i\to j\) exactly when \(M_{ij}\ne0\), allowing loops. When \(M\) is invertible, \(E_M\) is simple if and only if \(\Gamma_M\) is strongly connected. Indeed, if the graph is not strongly connected, a nonempty proper terminal union of strongly connected components is closed under outgoing arrows, and its basis span is a proper nonzero ideal. Conversely, let \(I\) be a nonzero ideal and choose \(v=\sum v_i e_i\in I\) with \(v_i\ne0\). Multiplying by \(e_i\) shows \(e_i^2\in I\). Each arrow \(i\to j\) then implies \(e_j^2\in I\), by multiplying \(e_i^2\in I\) with \(e_j\) and dividing by its nonzero coefficient. Strong connectivity gives every \(e_j^2\in I\); since these squares form a basis, \(I=E_M\). The same argument holds after any field extension, proving that simplicity and absolute simplicity coincide for these algebras. A finite directed graph is not strongly connected exactly when some nonempty proper set of vertices has no outgoing arrow to its complement.

**2. Sharp first-order simplicity failure.** For \(n\ge2\), for each vertex \(i\), let \(A_i\) denote the event that row \(i\) has all off-diagonal entries zero, and let \(B_i\) denote the analogous column event. An individual row or column of a uniform invertible matrix is uniform on \(\mathbb F_q^n\setminus\{0\}\), hence
\[
\Pr(A_i\mid M\in\mathrm{GL}_n)=\Pr(B_i\mid M\in\mathrm{GL}_n)=\frac{q-1}{q^n-1}.
\]
The event \(A_i\) is a one-vertex outward cut, while \(B_i\) is an outward cut whose complementary set has one vertex. For any two *distinct* events from the \(2n\) events, at least \(2n-3\) distinct entries are forced to zero. Since \(\Pr(M\in\mathrm{GL}_n)=c_{q,n}\ge c_q>0\), their pairwise conditional intersection probability is at most \(c_q^{-1}q^{-(2n-3)}\). The union of the singleton cut events therefore has probability
\[
\frac{2n(q-1)}{q^n-1}+O_q(n^2q^{-2n}).
\]
All other cuts have size \(2\le s\le n-2\). For a specified cut of size \(s\), the unconditional probability that all \(s(n-s)\) crossing entries vanish is \(q^{-s(n-s)}\), so the conditional probability is at most \(c_q^{-1}q^{-s(n-s)}\). Summing over choices gives
\[
 c_q^{-1}\sum_{s=2}^{n-2}\binom ns q^{-s(n-s)}=O_q(n^2q^{-2n}).
\]
For this last estimate the \(s=2,n-2\) summands are \(O_q(n^2q^{-2n})\); for \(3\le s\le n-3\), use \(s(n-s)\ge3(n-3)\) and bound the binomial sum by \(2^nq^{-3(n-3)}\le q^9 q^{-2n}\). Equation (1) follows from the graph criterion, including the case of overlapping cuts. Equation (3) follows by multiplying by \(c_{q,n}\), because \(E^2\) is an ideal and every simple algebra with nonzero multiplication must have \(E^2=E\).

**3. A graph-theoretic certificate for triviality of the full group scheme.** Suppose \(\Gamma_M\) is strongly connected, has at least one loop, and has no nonidentity directed-graph automorphism. The exact sequence of affine group schemes for perfect evolution algebras due to Elduque and Labra embeds the algebra automorphism scheme into the constant graph automorphism scheme, with kernel the diagonal graph scheme. Since the graph has no nontrivial automorphism, only diagonal automorphisms remain. For every commutative test algebra \(R\) over \(\mathbb F_q\), a diagonal automorphism has multipliers \(\lambda_i\in R^\times\) with \(\lambda_j=\lambda_i^2\) along every arrow \(i\to j\). At a loop, \(\lambda_i=\lambda_i^2\), which with invertibility forces \(\lambda_i=1\). Directed paths from this vertex reach all others, forcing every multiplier to be one. Hence the **group scheme itself** is trivial, not merely its points over \(\mathbb F_q\) or over an algebraic closure.

**4. Uniform random-support bound.** Before invertibility conditioning, the directed support indicators, loops included, are independent Bernoulli variables with nonzero probability \(p=1-q^{-1}\). A failure of strong connectivity is contained in the union of outward-cut events, giving the first sum in (2). The event of no loops has probability \(q^{-n}\). Let a nonidentity vertex permutation \(\sigma\) move exactly \(k\ge2\) vertices. Of the \(n^2\) ordered vertex pairs, exactly \(2nk-k^2\) move under the induced action. Its nontrivial orbits have lengths \(\ell\ge2\); the probability that all support indicators are constant on an orbit is \(p^\ell+(1-p)^\ell\le(p^2+(1-p)^2)^{\ell/2}=\alpha_q^{\ell/2}\), by monotonicity of \(\ell^r\)-norms. Thus the probability \(\sigma\) is a graph automorphism is at most \(\alpha_q^{(2nk-k^2)/2}\). The number of permutations moving \(k\) vertices is at most \(n^k\). A union bound and division by \(c_{q,n}\) give equation (2). For \(k\le n\), the exponent satisfies \(2nk-k^2\ge nk\), so the automorphism sum is at most \(\sum_{k=2}^{n}(n\alpha_q^{n/2})^k=O_q(n^2\alpha_q^n)\) for large \(n\). Together with the cut and loop bounds, this proves exponential decay.

## Verification
`verify.py` exhaustively enumerates all invertible matrices over \(\mathbb F_2\) for dimensions one through four and over \(\mathbb F_3\) for dimensions one through three, totaling 31,617 matrices. For each it independently computes directed reachability, graph automorphisms, and all monomial *point* automorphisms of the algebra. The computer checks 31,617 instances of the structural certificate (strong connectivity + a loop + graph asymmetry) without false positives and compares the observed certificate failure fraction with the stated bound. The recorded direct check ends with `VERIFY_OK perfect_matrices=31617 cases=7 certificate_no_false_positive=True`. This is finite corroboration only; the group-scheme conclusion for arbitrary coefficient rings and the infinite asymptotics are established by the proof, not finite enumeration.

## Relationship to prior work
Kaygorodov, Martín González, and Viruel explicitly ask for asymptotic simplicity and automorphism probabilities of random evolution algebras in Question 22 of their October 2026 survey. Their work also explains the simple/perfect/strong-connectivity relation but does not give the conditional sharp coefficient or joint group-scheme bound in (1)–(2). Elduque and Labra (2019) supply the exact graph-to-automorphism group-scheme sequence used in Step 3; that sequence is **prior work**. Cabrera Casado, Siles Molina, and Velasco (2016) established ideal-theoretic foundations. Wei and Zou (2023) count isomorphism classes of perfect evolution algebras in low dimension, not probabilities for uniform invertible matrices at growing dimension. Standard random digraph estimates apply to the unconditioned support graph; the present explicit conditional leading term retains the invertibility normalization and the scheme-level conclusion. Searches of relevant literature and research databases did not identify a theorem implying the combined conclusions. The literature-priority risk of an earlier equivalent conditioning argument is noted in the accompanying scientific review.

## Limitations
The bound is for a fixed field size as dimension grows, not a sparse regime where the zero probability depends on \(n\). A uniform random singular structure matrix is not covered by the group-scheme assertion; the unconditional statement (3) concerns simplicity only. The proof supplies a one-sided explicit bound for nontrivial group schemes rather than their exact probability or a sharp asymptotic constant. Verification enumerates prime fields of size two and three, not all prime powers. An earlier result on conditioned random digraphs might imply the sharp simplicity term; the priority comparison is qualified accordingly. Independent mathematical audit has not been performed.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), Question 22 and the graph discussion. https://arxiv.org/html/2610.22248v1
2. A. Elduque, A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191 (2019), Definition 2.1 and Theorem 3.2. https://arxiv.org/abs/1902.02191
3. Y. Cabrera Casado, M. Siles Molina, M. V. Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832 (2016). https://arxiv.org/abs/1601.01832
4. Y. Wei, Y. Zou, *Isomorphism classes of idempotent evolution algebras*, arXiv:2310.12368 (2023). https://arxiv.org/abs/2310.12368
