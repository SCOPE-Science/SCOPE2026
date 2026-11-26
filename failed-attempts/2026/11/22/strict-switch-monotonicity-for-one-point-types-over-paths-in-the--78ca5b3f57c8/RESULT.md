# Strict switch monotonicity for one-point types over paths in the transitive-triangle-free homogeneous oriented graph

## Finding
Let \(\mathcal H\) be the countable Fraïssé limit of finite oriented graphs with no transitive three-vertex tournament. For any \(n\ge 3\), name individually the vertices \(v_1,\ldots,v_n\) of an induced oriented path, with no arcs except one directed arc between consecutive vertices. Write \(\epsilon_i=0\) for \(v_i\to v_{i+1}\), and \(\epsilon_i=1\) for the opposite orientation, and put \(\sigma_i=\epsilon_i\oplus\epsilon_{i+1}\) for \(1\le i\le n-2\). Let \(t_n(\sigma)\) count complete nonalgebraic one-types over these individually named parameters. The initial direction is immaterial by reversing all arcs.

**Strict switch theorem.** Holding all switch indicators other than \(\sigma_i\) fixed, replacing \(\sigma_i=0\) by \(\sigma_i=1\) strictly increases \(t_n\), for every \(n\ge3\) and every \(1\le i\le n-2\). Consequently the only minimizing orientations (up to overall reversal) are consistently directed paths, and the only maximizing orientations are alternating source/sink paths.

Writing \(m_n\) and \(M_n\) for these extrema, their exact initial values and all-order recurrences are
\[
(m_1,m_2,m_3)=(3,6,13),\qquad m_n=m_{n-1}+2m_{n-2}+m_{n-3}\quad(n\ge4),
\]
\[
(M_1,M_2,M_3)=(3,6,14),\qquad M_n=2M_{n-1}+M_{n-2}-M_{n-3}\quad(n\ge4).
\]
Their asymptotic exponential bases are respectively the largest real roots \(\alpha=2.1478990357\ldots\) of \(z^3-z^2-2z-1\) and \(\beta=2.2469796037\ldots\) of \(z^3-2z^2-z+1\); in particular \(M_n/m_n\) grows exponentially like a positive constant times \((\beta/\alpha)^n\).

## Assumptions and scope
An *oriented graph* has neither loops nor opposite directed arcs. A *transitive triangle* means a three-vertex tournament with an acyclic (total-order) orientation, distinct from a directed three-cycle. A finite graph belongs to the age if it contains no transitive triangle, not necessarily induced. The Fraïssé class has free amalgamation, hence every compatible finite one-point extension of any finite parameter substructure has infinitely many realizations in \(\mathcal H\). The finite relational homogeneous limit has quantifier elimination, so an allowed vector of binary arc/nonarc relations to the named parameters determines one complete nonalgebraic one-type. The theorem concerns an induced path with all its vertices individually named; it does not concern unnamed orbit types, the cyclic-triangle-free class, general oriented trees, or longer tuples.

## Proof
**1. Three-state extension transfer.** Relative to a new vertex \(x\), encode its relation with \(v_i\) by \(0\) for no arc, \(+\) for \(x\to v_i\), and \(-\) for \(v_i\to x\). If \(v_i\to v_{i+1}\), precisely the three ordered state pairs \((+,+),(-,-),(-,+)\) create a transitive triangle with \(x\). The pair \((+,-)\) creates a directed cycle and is permitted. If the old arc is reversed, the forbidden pairs are \((+,+),(-,-),(+,-)\). Since the old parameters induce a path, these adjacent constraints are the only possible forbidden triangles involving \(x\); every permitted word realizes exactly one complete nonalgebraic one-type.

For a path prefix, let \(a,b,c\) count permitted state words ending respectively in \(0,+,-\), and set \(S=a+b+c\). Appending a forward edge transforms the column \((a,b,c)^\mathsf T\) into \((S,a,a+b)^\mathsf T\). Appending a reverse edge transforms it into \((S,a+c,a)^\mathsf T\). Start with \((1,1,1)^\mathsf T\). The matrices are
\[
A=\begin{pmatrix}1&1&1\\1&0&0\\1&1&0\end{pmatrix},\qquad
B=\begin{pmatrix}1&1&1\\1&0&1\\1&0&0\end{pmatrix}=JAJ,
\]
where \(J\) exchanges the last two coordinates. In particular after a forward last edge \(c>b\), while after a reverse last edge \(b>c\): the differences equal the previous prefix counts ending at \(+\) and \(-\), respectively, and are positive (a word with only this one nonzero state always exists).

**2. Exact local switch improvement.** Fix \(1\le i\le n-2\) and all other switch indicators. For comparison, choose the old orientations so that \(\epsilon_i=\epsilon_{i+1}\), and toggle \(\sigma_i\). This changes the orientation of the bridge \(v_{i+1}v_{i+2}\) and reverses all subsequent edges, keeping previous edges fixed and all other switches unchanged. Split the path into a left subpath on \(v_1,\ldots,v_{i+1}\) and a right subpath on \(v_{i+2},\ldots,v_n\). Reverse the labels \(+,-\) on the right-hand state words when reversing its edges; this is a bijection of internally admissible right words.

Write \(L_+,L_-\) for left admissible words with their final state \(+,-\), and \(R_+,R_-\) for right admissible words with their first state \(+,-\) before the comparison. The total number of pairs of internally admissible words is the same before and after the toggle. If the original bridge and the left last edge are forward, the forbidden-bridge pair counts are respectively
\[
L_+R_+ + L_-(R_++R_-),\qquad
L_+(R_++R_-) + L_-R_+.
\]
Subtracting gives the strict increase in allowed pairs
\[
t_n(\sigma_i=1)-t_n(\sigma_i=0)=(L_--L_+)R_->0.
\]
If both old edges are reverse, the same calculation with \(+\) and \(-\) interchanged gives
\[
t_n(\sigma_i=1)-t_n(\sigma_i=0)=(L_+-L_-)R_+>0.
\]
The left differences are positive by step 1, and each right factor is positive (take one root state and all other states \(0\)). Hence the improvement is strict regardless of all other switch indicators. Repeated coordinate changes show the asserted unique extremizers.

**3. Exact recurrences and rates.** For the consistent orientation, \(t_n=\mathbf1^\mathsf T A^{n-1}\mathbf1\). Its characteristic polynomial is \(z^3-z^2-2z-1\). Cayley–Hamilton gives the stated recurrence and initial values. For alternating orientations, use \(B=JAJ\) and change the state coordinates at every second step by \(J\). Then the fixed transition matrix is \(AJ\), with characteristic polynomial \(z^3-2z^2-z+1\). Cayley–Hamilton again yields its recurrence. Both nonnegative primitive matrices have simple positive Perron roots, and the all-positive initial/final vectors have positive leading coefficients. The displayed numerical values of the roots follow from those cubic polynomials, establishing the exponential ratio.

## Verification
The fully standalone script `check.py` computes each allowed state word by direct enumeration and also via the independent three-state transfer for all 255 orientations through eight vertices. It exhaustively checks strict increase on every switch coordinate for all orientations from three through fourteen vertices (45,057 strict comparisons), the two recurrence-derived extrema, and the exact prefix/suffix improvement identity in 4,097 cases through eleven vertices. Running `python3 check.py` requires only Python 3 standard library and reproduces the embedded `verification_output.txt`. These are finite checks; the universal theorem follows from the proof above.

## Relationship to prior work
Cherlin's work on homogeneous directed graphs, including the forbidden-tournament free-amalgamation construction, establishes the ambient homogeneous structures. Kühn, Osthus, Townsend and Zhao study asymptotic *global* counts and typical structure of transitive-triangle-free and directed-cycle-free oriented graphs; their Theorem 1.2 concerns bipartiteness of a uniformly sampled large finite graph, rather than numbers of complete named-parameter one-types over each oriented path. Exact path-orientation switch monotonicity and the two extremal recurrence sequences do not follow from the cited global theorem. Analogous calculations for directed-cycle-free parameter paths use a different excluded three-vertex tournament and different local forbidden pairs, so cannot imply the present statement. A finite-state rewriting of the claim remains possible in earlier transfer-matrix literature; see limitations.

## Limitations
The monotonicity is specific to path-shaped named bases and one-point types in the homogeneous transitive-triangle-free *oriented* graph. No extremal result for general connected parameter graphs, for the directed-cycle-free class, or for tuple arity greater than one is asserted. Historical priority is based on targeted literature/record searches and is not a proof of uniqueness or an independent audit.

## References
1. G. L. Cherlin, *Infinite homogeneous directed graphs*, exposition available at https://ow3.math.rutgers.edu/~cherlin/Paper/1992Digraph.pdf, especially §2.1.3–2.1.4 on free amalgamation of tournament-forbidden oriented graphs. See also *The Classification of Countable Homogeneous Directed Graphs and Countable Homogeneous n-tournaments*, Memoirs Amer. Math. Soc. **131** (1998), no. 621, https://doi.org/10.1090/memo/0621.
2. D. Kühn, D. Osthus, T. Townsend and Y. Zhao, *On the structure of oriented graphs and digraphs with forbidden tournaments or cycles*, arXiv:1404.6178 (first posted 2014-04-24), https://arxiv.org/abs/1404.6178, particularly Theorem 1.2 and Sections 4–5.
