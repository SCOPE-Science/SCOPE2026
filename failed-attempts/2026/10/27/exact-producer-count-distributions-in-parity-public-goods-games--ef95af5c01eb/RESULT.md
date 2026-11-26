# Exact producer-count distributions in parity public-goods games on rook networks

## Finding

Fix integers \(m,n\ge2\) and place one binary-action agent in every cell of an \(m\)-by-\(n\) rectangle. Each agent is adjacent to every other agent in its own row or column, so the network is the rook graph \(K_m\square K_n\). Each agent has the strict unique best response \(T(k)=1\) when the number \(k\) of active neighbors is even, and \(T(k)=0\) when it is odd. Write \(P_{m,n}(z)=\sum_{x\in\mathcal E_{m,n}}z^{|x|}\), where \(\mathcal E_{m,n}\) is the set of pure Nash equilibria, \(x\) is the binary activity matrix, and \(|x|\) is its number of ones. All agents and cells are labeled; no quotient by symmetry is taken.

**Theorem.** The complete equilibrium producer-count polynomial is

\[
P_{m,n}(z)=\begin{cases}
z^{mn},&m,n\text{ even},\\[2mm]
\displaystyle\sum_{\substack{1\le a\le m\\a\text{ odd}}}\binom ma z^{na},&m\text{ even},\ n\text{ odd},\\[4mm]
\displaystyle\sum_{\substack{1\le b\le n\\b\text{ odd}}}\binom nb z^{mb},&m\text{ odd},\ n\text{ even},\\[4mm]
\displaystyle\sum_{\substack{1\le a\le m\\a\text{ odd}}}\sum_{\substack{1\le b\le n\\b\text{ odd}}}\binom ma\binom nb z^{ab+(m-a)(n-b)},&m,n\text{ odd}.
\end{cases}
\]

In particular, \(P_{m,n}(1)\) is \(1\), \(2^{m-1}\), \(2^{n-1}\), or \(2^{m+n-2}\), in the respective cases. The minimum feasible number of producers and the number of equilibria achieving it are, in the same order,

\[
(mn,1),\quad(n,m),\quad(m,n),\quad
\begin{cases}(m,n),&m<n,\\(n,m),&n<m,\\(m,2m),&m=n.\end{cases}
\]

If at least one dimension is odd, a uniformly selected equilibrium has expected production \(mn/2\); if both dimensions are even it has production \(mn\) with certainty. For example,
\[
P_{3,5}(z)=5z^3+3z^5+30z^7+25z^9+z^{15}.
\]

## Assumptions and scope

The network is a finite, simple, fully occupied, labeled rook graph with dimensions at least two. Each agent uses the same deterministic strict parity-alternating best-response rule, based on **other** agents in the same row or column. The polynomial enumerates pure (not mixed) Nash equilibria and counts individual producing agents; no equilibrium-selection mechanism is postulated except where the uniform distribution is explicitly invoked for the expectation. The graph-theoretic equivalent is the weight enumerator of subsets meeting every closed neighborhood in an odd number of vertices, known generally as odd dominating sets.

## Proof

All equations in this proof involving parity take place in \(\mathbb F_2\). Let \(x_{ij}\) be the activity of cell \((i,j)\), \(r_i=\sum_{j=1}^n x_{ij}\) its row parity, \(c_j=\sum_{i=1}^m x_{ij}\) its column parity, and \(A=\sum_i r_i\), \(B=\sum_j c_j\). The parity of the number of other active agents in cell \((i,j)\)'s row or column is \(r_i+c_j\), because its own action is removed twice and hence cancels in \(\mathbb F_2\). The strict best-response condition is therefore exactly

\[
 x_{ij}=1+r_i+c_j.\tag{1}
\]

Summing (1) across each row and each column gives the necessary identities

\[
 (1+n)r_i=n+B,\qquad (1+m)c_j=m+A.\tag{2}
\]

Conversely, suppose vectors \(r,c\) obey (2), with \(A\) and \(B\) their respective sums, and set \(x\) by (1). Equation (2) says that the computed row and column parities of \(x\) equal the prescribed \(r,c\). Therefore (1) really is the local best-response condition at every vertex. The construction is consequently sufficient as well as necessary. Every equilibrium also determines its own \(r,c\), so counting compatible parity vectors counts equilibria without repetition.

If both \(m\) and \(n\) are even, (2) implies \(r_i=B\) for all rows and \(c_j=A\) for all columns. Hence \(A=mB=0\) and \(B=nA=0\), whence \(r=c=0\), \(x_{ij}=1\), and the first case follows.

Suppose \(m\) is even and \(n\) is odd. The row equations force \(B=1\), and the column equations give \(c_j=A\). Summing the latter over the odd number of columns yields \(B=A=1\). Thus the row parity vector \(r\) can be **any** length-\(m\) binary vector with odd total parity, and all columns have parity one. Formula (1) simplifies to \(x_{ij}=r_i\). A row of parity one is fully producing, and if exactly \(a\) rows have parity one the producer count is \(na\). There are \(\binom ma\) choices, for odd \(a\). The case \(m\) odd and \(n\) even is symmetric.

If both dimensions are odd, (2) reduces to \(A=B=1\), leaving every odd-parity row vector and odd-parity column vector independently selectable. Formula (1) gives \(x_{ij}=1\) exactly when \(r_i=c_j\). If \(r\) has \(a\) ones and \(c\) has \(b\) ones, then precisely \(ab+(m-a)(n-b)\) cells produce; choosing the one-locations proves the fourth polynomial formula. The map is injective because \(r,c\) are recoverable from the resulting activity profile.

The total counts now follow by summing binomial coefficients of odd index: \(\sum_{a\text{ odd}}\binom ma=2^{m-1}\). In the mixed-parity cases, the minimum odd index is one, and the two respective sparse-equilibrium counts follow. In the odd-odd case, the producer count \(f(a,b)=ab+(m-a)(n-b)\) is affine separately in \(a\) and \(b\), so over the admissible discrete rectangle its minimum occurs at a corner. The four corner values are \(1+(m-1)(n-1)\), \(m\), \(n\), and \(mn\). Since both dimensions are at least three, the minimum is \(\min\{m,n\}\). No non-corner point can have this minimum: for any allowed fixed \(b\), the difference \(f(a+2,b)-f(a,b)=2(2b-n)\) is nonzero, and similarly \(f(a,b+2)-f(a,b)=2(2a-m)\) is nonzero, so every minimum forces both coordinates to be endpoints. The unique minimizing corner is \((a,b)=(m,1)\) if \(m<n\), or \((1,n)\) if \(n<m\); both occur for equal dimensions. The stated multiplicities follow from \(\binom m a\binom n b\).

Finally, in each nonunique regime each active coordinate is unbiased when parity vectors are chosen uniformly among the permitted odd-parity vectors. This follows by fixing any one coordinate and pairing the remaining admissible assignments, using that every vector length is at least two. In the mixed-parity cases \(x_{ij}\) is one parity-vector coordinate; in the odd-odd case \(x_{ij}=1+r_i+c_j\) and independently uniform row and column coordinates make it unbiased. Linearity of expectation gives \(\mathbb E|x|=mn/2\).

## Verification

Run the standalone standard-library program with `python3 verify.py`. It independently enumerates all binary profiles for all \(19\) rectangles with \(m,n\ge2\) and \(mn\le16\), covering \(314{,}512\) candidate profiles; every equilibrium is accepted or rejected by explicitly checking each agent's true number of active neighbors. For every one of the \(81\) rectangles with \(2\le m,n\le10\), the program independently calculates the binary rank of the closed-neighborhood matrix and checks it against the theorem's equilibrium total, and verifies the exact minimum-producer count and multiplicity. The \(3\)-by-\(5\) polynomial is explicitly replayed. Output: `VERIFY_OK parameter_cases=81 fully_enumerated_boards=19 profiles_tested=314512`. These finite checks do not substitute for the all-dimension proof.

## Relationship to prior work

Gilboa and Nisan (2022) formulate homogeneous strict binary public-goods games and already identify alternating parity response as a polynomial-time linear-equations case. Consequently neither the reduction to equations over \(\mathbb F_2\) nor equilibrium solvability is new. Batal (2020) identifies the same closed-neighborhood equations as odd domination and proves general parity facts about odd dominating sets. Peters, Goldwasser, and Young (2017, Proposition 3.1) **already establish** closed universal solvability on \(K_m\square K_n\) for even-even dimensions; this implies uniqueness of the equilibrium in the even-even regime. Curtis et al. (2018) give general Cartesian-product nullity methods capable of computing dimensions of solution spaces, but do not give these rook-graph producer-weight coefficients. The present assertion is the explicit **complete weight enumerator**, with precise sparsest-equilibrium multiplicities, for all four dimension-parity regimes. Ordinary rook-graph domination polynomials concern a different, non-parity neighborhood condition. The connected 2023 binary-public-goods work of Klimm and Stahlberg primarily studies existence and complexity for other response patterns.

## Limitations

The equilibrium-count claim is mathematical and complete for this precisely specified response rule and graph family, but it does not claim that parity-alternating behavior is representative of common economic preferences. The theorem does not cover arbitrary neighborhoods, other response rules, correlated equilibrium selection, dynamics, or social welfare functions unrelated to the number of producing agents. The structural linearization and the even-even unique-solution case are established in earlier work. Exact novelty of the full multivariate family against all unindexed odd-domination and coding-theory literature remains a bibliographic limitation; the inspected sources did not give the claimed coefficient formula. Computational verification is finite; universality rests on the proof above.

## References

- M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238, first public version July 9, 2022. https://arxiv.org/abs/2207.04238
- M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849, 2023. https://arxiv.org/abs/2301.11849
- A. Batal, *Parity of an odd dominating set*, arXiv:2011.10270, 2020. https://arxiv.org/abs/2011.10270
- T. Peters, J. Goldwasser, and M. Young, *Lights Out! on Cartesian Products*, Electronic Journal of Linear Algebra 32 (2017), 464–474, Proposition 3.1. https://doi.org/10.13001/1081-3810.3483
- B. Curtis, J. Earl, D. Livingston, and B. L. Shader, *Resolution of Conjectures Related to Lights Out! and Cartesian Products*, arXiv:1802.05359, 2018. https://arxiv.org/abs/1802.05359
- Y. Caro, W. Klostermeyer, and J. Goldwasser, *Odd and residue domination numbers of a graph*, Discussiones Mathematicae Graph Theory 21 (2001), 119–136. https://doi.org/10.7151/dmgt.1137
