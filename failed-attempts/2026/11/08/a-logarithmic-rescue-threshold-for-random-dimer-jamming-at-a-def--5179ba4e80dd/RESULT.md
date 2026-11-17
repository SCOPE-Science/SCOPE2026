# A logarithmic rescue threshold for random dimer jamming at a deficient clique vertex

## Finding

**Theorem.** For every even integer \(n\ge4\) and integer \(0\le m\le n-1\), let \(G_{n,m}\) consist of a clique on \(n-1\) vertices and one distinguished vertex \(h\) adjacent to exactly \(m\) clique vertices. Start with all vertices vacant. Repeatedly choose an edge uniformly among edges whose two endpoints are vacant and permanently occupy both endpoints with an irreversible dimer. Let \(F_{n,m}\) be the probability of exactly two vacant vertices when no further dimer can be placed.

The terminal number of vacancies belongs to \(\{0,2\}\). Put \(f(1,0)=1\), \(f(1,1)=0\), and, for odd \(k\ge3\), \(0\le a\le k\),
\[
f(k,a)=\frac{1}{\binom{k}{2}+a}\sum_{j=0}^{2}\binom{a}{j}\binom{k-a}{2-j}f(k-2,a-j),
\]
where binomial coefficients with infeasible indices are zero. Then \(F_{n,m}=f(n-1,m)\) is an exact rational finite-size probability.

For every sequence \(m=m_n\) with \(0\le m_n\le n-1\) and \(n\) tending to infinity through even integers,
\[
\frac{m_n\log n}{n}\longrightarrow c\in[0,\infty)
\quad\Longrightarrow\quad F_{n,m_n}\longrightarrow e^{-c}.
\]
If \(m_n\log n/n\to\infty\), then \(F_{n,m_n}\to0\). The finite boundary case of exactly one missing edge is
\[
F_{n,n-2}=\frac{3}{n^2-1}.
\]
In particular, every graph with \(m_n\ge1\) admits a perfect matching, but at the scale \(m_n\sim c n/\log n\) the probability that irreversible random adsorption fails to obtain one converges to \(e^{-c}\).

## Assumptions and scope

Edges are undirected and simple. All edges have equal exponential deposition rates, equivalently the next successful deposition is chosen uniformly among available edges. There is no desorption, diffusion, adaptive preference, or edge reactivation. The parameter \(n\) is the *total* even vertex count, including \(h\); \(m\) is its initial degree. A perfect matching exists whenever \(m\ge1\): match \(h\) to any one neighbor and match the remaining even clique arbitrarily. The limit concerns the terminal probability, not any finite-time coverage or bulk phase transition. Natural logarithms are used.

## Proof

**1. Exhaustive terminal alternatives and recurrence.** If two clique vertices are vacant, their edge is available, so a terminal state has at most one vacant clique vertex. As the initial total number of vertices is even and each deposition removes exactly two, the total vacancy count is even; hence it is either zero or two. A two-vacancy terminal state has vacant \(h\) and a vacant non-neighbor of \(h\).

While \(h\) is vacant, suppose \(k\) clique vertices remain, of which \(a\) are neighbors of \(h\). There are \(\binom{k}{2}+a\) available edges: all clique pairs plus the \(a\) hub edges. Choosing a hub edge guarantees eventual zero vacancies, because an even clique remains. Otherwise, choosing a clique pair with exactly \(j\) hub-neighbors has \(\binom{a}{j}\binom{k-a}{2-j}\) possibilities and leaves state \((k-2,a-j)\). This gives the recurrence and boundary conditions, with no unlisted absorbing cases.

**2. Random-permutation representation.** Let \(p=m/(n-1)\). Draw a uniformly random ordering of the \(n-1\) clique vertices, independently of deposition decisions. Under the conditional evolution in which only clique edges are selected, the unordered pair removed at each step is uniform among all pairs of the remaining clique vertices; hence this ordered deletion representation is exact. Let \(A_k\) be the number of original \(h\)-neighbors among the first \(k\) ranks, for each odd \(k\in\{1,3,\ldots,n-1\}\). At level \(k\ge3\), the conditional probability of choosing a clique edge instead of a hub edge is
\[
\frac{\binom{k}{2}}{\binom{k}{2}+A_k}=(1+X_k)^{-1},
\qquad X_k=\frac{2A_k}{k(k-1)}.
\]
If only one clique vertex remains, terminal failure occurs exactly when that vertex is a non-neighbor. Consequently
\[
F_{n,m}=\mathbb E\left[\mathbf1_{\{A_1=0\}}\prod_{k=3,5,\ldots,n-1}(1+X_k)^{-1}\right].\tag{1}
\]
This expression also couples different hub degrees monotonically: take nested neighbor sets in the same ordering. More hub neighbors weakly increase every \(A_k\), so \(F_{n,m}\) is nonincreasing in \(m\).

**3. Cumulative hazard and concentration.** Define \(S_n=\sum_{k=3,5,\ldots,n-1}X_k\). Since \(A_k\) is hypergeometric with expectation \(kp\),
\[
\mathbb E S_n=2p\sum_{k=3,5,\ldots,n-1}\frac{1}{k-1}
=p H_{(n-2)/2},
\]
where \(H_s=\sum_{j=1}^s1/j\). To control fluctuations, write
\[
S_n=\sum_{r\text{ a hub-neighbor rank}}g_n(r),\qquad
 g_n(r)=\sum_{\substack{3\le k\le n-1,\ k\text{ odd}\\ k\ge r}}\frac{2}{k(k-1)}.
\]
For every \(r\ge1\), \(0\le g_n(r)\le4/r\); therefore \(\sum_{r=1}^{n-1}g_n(r)^2\le16\sum_{r\ge1}r^{-2}\). Because the \(m\) occupied ranks form a uniform sample without replacement, the finite-population variance identity gives \(\operatorname{Var}(S_n)\le C p\) for an absolute constant \(C\) and all even \(n\ge4\).

Also, for hypergeometric \(A_k\), \(\mathbb E A_k^2\le kp+k^2p^2\). Hence
\[
\mathbb E\sum_{k=3,5,\ldots,n-1}X_k^2\le C'(p+p^2)
\]
for an absolute \(C'\). Since \(0\le x-\log(1+x)\le x^2/2\) for every \(x\ge0\), it follows that
\[
-\sum_k\log(1+X_k)=-S_n+o_{\mathbb P}(1)
\]
whenever \(p\to0\).

**4. The logarithmic window and endpoints.** If \(m_n\log n/n\to c<\infty\), then \(p\to0\), \(\mathbb E S_n\to c\), and \(\operatorname{Var}(S_n)\to0\). Thus the product in (1) converges in probability to \(e^{-c}\). Further, \(\Pr(A_1=1)=p\to0\). The integrand is between zero and one, so bounded convergence in probability yields \(F_{n,m_n}\to e^{-c}\).

If \(m_n\log n/n\to\infty\), for any fixed \(M>0\) eventually \(m_n\ge\lfloor M n/\log n\rfloor\); the monotonic coupling and the finite-window limit give \(\limsup F_{n,m_n}\le e^{-M}\). Letting \(M\to\infty\) proves the assertion without assuming \(m_n/n\to0\).

Finally, if \(m=n-2\), there is exactly one non-neighbor \(u\). To fail, every deposited edge must join two of the other \(n-2\) clique vertices; at a stage with \(2j+1\) clique vertices left this step has conditional probability
\(\binom{2j}{2}/(\binom{2j+1}{2}+2j)=(2j-1)/(2j+3)\).
The product over \(j=1,\ldots,(n-2)/2\) telescopes to \(3/(n^2-1)\).

## Verification

Run `python3 verify.py` using Python 3's standard library. For every even \(n\in\{4,6,8,10,12\}\) and every allowable \(m\), the exact rational two-variable recurrence is compared against a separately implemented labeled-state enumeration that chooses among all currently available edges. The script also checks the two boundary degrees and samples the random-permutation identity at three growing sizes as a numerical sanity check. The finite and stochastic computations are not substituted for the infinite-size proof above.

Selected exact values are \(F_{4,1}=1/2\), \(F_{6,1}=7/11\), and \(F_{8,6}=1/21\). The checker reports 53 assertions if successful.

## Relationship to prior work

Random sequential dimer deposition is a greedy matching process. Bennett and Bohman study random greedy matching on regular hypergraphs under co-degree assumptions, deriving macroscopic unmatched-vertex bounds; the graph here is strongly nonregular and the claimed observable is a constant-order terminal defect probability with a sharp exceptional-vertex degree window. Besser and Poloczek analyze approximation guarantees and limitations of several greedy matching algorithms; those coarse guarantees do not give this fixed-graph window. Dyer and Frieze's earlier uniform-edge randomized matching work is an important predecessor, but its complete paper was not available for full-text comparison, leaving a residual historical-priority question. The single-forbidden-edge boundary is compatible with previously studied rare-defect behavior for nearly complete graphs; novelty is not assigned to that boundary alone.

## Limitations

This result is specific to a complete core, one exceptional vertex, uniform successful-edge choice, and even total order. It does not apply to arbitrary sparse cores, multiple exceptional vertices, or degree-prioritizing matching algorithms. No statement is made about deposition time or the speed of convergence. The distinct edge-ordering model that uniformly proposes *all* graph edges and discards blocked attempts yields the same sequence of accepted edges only when proposals are independent and equally rated. Earlier literature may contain an equivalent exact window under different terminology; priority remains to be independently checked.

## References

- P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581, first posted 2012-10-12. https://arxiv.org/abs/1210.3581
- B. Besser and M. Poloczek, *Greedy Matching: Guarantees and Limitations*, arXiv:1505.04198, first posted 2015-05-15. https://arxiv.org/abs/1505.04198
- M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45. https://doi.org/10.1002/rsa.3240020104
- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401. https://doi.org/10.1137/0402034
