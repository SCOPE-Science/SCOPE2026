# Marked temporal lasso laws at a preferential reset vertex

## Finding
A deterministic labeled transition system whose independent successor choices favor one reset vertex has an explicit **finite-size joint transient/cycle mark-count law**. In the critical reset window, the marked cycle and transient have a common random Rayleigh–hub scale and are generally dependent; when the reset weight exceeds the birthday scale they split into *independent multivariate geometric* mark-count vectors. The result determines probabilities of simultaneous temporal eventualities and recurrence properties at a distinguished root.

Fix \(n\ge2\), \(W_n=\{0,1,\ldots,n-1\}\), root \(o=1\), and a reset vertex \(h=0\). For each vertex \(x\), independently draw \(f(x)\), with probabilities
\[\alpha_n=\Pr(f(x)=h)=p_n+\frac{1-p_n}{n},\qquad \beta_n=\Pr(f(x)=y)=\frac{1-p_n}{n}\quad(y\ne h),\]
where \(0\le p_n\le1\). Write the distinct forward vertices as \(v_0=o,v_1,\ldots,v_{T_n-1}\), where \(f(v_{T_n-1})=v_{J_n}\). The transient is \(v_0,\ldots,v_{J_n-1}\), and the cycle is \(v_{J_n},\ldots,v_{T_n-1}\). The cycle has length \(T_n-J_n\). The index \(J_n\) may be zero.

Set \(F_{n,k}=(n-2)_{\underline k}\), the falling factorial, for \(k\ge0\), with \(F_{n,0}=1\) and \(F_{n,k}=0\) for \(k>n-2\). For \(1\le t\le n\) let \(Q_{n}(t,j)=\Pr(T_n=t,J_n=j)\). The exact **joint finite-size law** is
\[Q_n(1,0)=\beta_n;\]
for \(2\le t\le n\),
\[Q_n(t,0)=F_{n,t-1}\beta_n^t+(t-1)\alpha_n F_{n,t-2}\beta_n^{t-1},\]
and for each \(1\le j<t\),
\[Q_n(t,j)=F_{n,t-1}\beta_n^t+\alpha_n F_{n,t-2}\beta_n^{t-2}\bigl(\alpha_n+(t-2)\beta_n\bigr).\]
Its tail identity is
\[\Pr(T_n>k)=F_{n,k}\beta_n^k+k\alpha_n F_{n,k-1}\beta_n^{k-1}\quad(1\le k\le n).\]

Assign a fixed number \(d\ge1\) of independent propositional labels \(P_i\), each present at every vertex independently with probability \(q_{i,n}\in[0,1]\). All marks are also independent of \(f\). Let \(A_{i,n}\) and \(B_{i,n}\) be the counts of \(P_i\) on the transient and cycle, respectively. For \(s_i,t_i\in[0,1]\) the **exact joint probability generating function** is
\[\mathbb E\prod_{i=1}^d s_i^{A_{i,n}}t_i^{B_{i,n}}=\sum_{t=1}^n\sum_{j=0}^{t-1}Q_n(t,j)\prod_{i=1}^d(1-q_{i,n}+q_{i,n}s_i)^j(1-q_{i,n}+q_{i,n}t_i)^{t-j}.\tag{1}\]

**Critical window.** Suppose \(p_n\sqrt n\to a\in[0,\infty)\) and \(q_{i,n}\sqrt n\to c_i\in[0,\infty)\). Let \(U\) be uniform on \([0,1]\), independent of a positive random variable \(R_a\) having survival function
\[\Pr(R_a>r)=(1+ar)\exp(-r^2/2-ar)\qquad (r\ge0).\tag{2}\]
Then \((T_n/\sqrt n,J_n/T_n)\) converges to \((R_a,U)\). Jointly, conditional on \((R_a,U)\), the entire family of limiting mark counts \((A_i,B_i)_{i=1}^d\) consists of independent Poisson variables with respective means \(c_i U R_a\) and \(c_i(1-U)R_a\). Thus the limiting generating function is
\[\mathbb E\exp\left(-R_a\sum_{i=1}^dc_i\bigl[U(1-s_i)+(1-U)(1-t_i)\bigr]\right).\tag{3}\]
At the unbiased endpoint \(a=0\), \(R_0\) is Rayleigh with density \(r e^{-r^2/2}\), and the negative dependence is explicit:
\[\operatorname{Cov}(A_i,B_j)=c_i c_j\left(\frac13-\frac\pi8\right)<0\quad (c_i c_j>0).\tag{4}\]

**Reset-dominated window.** Suppose instead \(p_n\to0\), \(np_n^2\to\infty\) and \(q_{i,n}/p_n\to c_i\in[0,\infty)\). There are independent mean-one exponential random variables \(E_1,E_2\) such that the normalized transient and cycle lengths converge jointly to \((E_1,E_2)\):
\[ (p_nJ_n,p_n(T_n-J_n))\ \xrightarrow{\mathrm d}\ (E_1,E_2).\tag{5}\]
Conditional on the exponential lengths, the limiting transient and cycle mark counts are independent Poisson variables of respective means \(c_iE_1\) and \(c_iE_2\). Consequently their **two multivariate count vectors are independent**, with joint generating function
\[\left(1+\sum_{i=1}^dc_i(1-s_i)\right)^{-1}\left(1+\sum_{i=1}^dc_i(1-t_i)\right)^{-1}.\tag{6}\]
Each coordinate is geometric on \(\{0,1,\ldots\}\) with mean \(c_i\). For an individual proposition \(P_i\), its temporal eventuality \(\mathbf F P_i\) is true at the root iff \(A_i+B_i>0\), and its recurrence \(\mathbf{GF} P_i\) is true iff \(B_i>0\). Therefore the respective limiting truth probabilities in (5) are
\[ 1-(1+c_i)^{-2}\qquad\text{and}\qquad \frac{c_i}{1+c_i}.\tag{7}\]

## Assumptions and scope
The successor map is a total single-valued map, not an independent-arc or branching transition relation. The distinguished root is **not** the hub. A label \(P_i\) may occur on both the transient and the cycle but only at different vertices, and different labels at the same vertex are independent by assumption. There is a fixed finite set of atomic propositions. LTL formulas use standard infinite-run semantics; the unique infinite run eventually repeats its directed cycle. The asymptotic results hold for all sequences with the specified limiting scales, not only exact power laws. Formula (1) holds at finite \(n\) even at boundary values \(p_n=0\) or \(p_n=1\), interpreting empty products and zero powers in their combinatorial meaning.

## Proof
**Exact finite joint cells.** Before the first repetition, the successors of *distinct* visited vertices are independent with the stated probabilities. For \(t\ge2\), if the hub never appears among the \(t\) distinct visited vertices, there are \(F_{n,t-1}\) ordered non-hub choices after the root, each receiving probability \(\beta_n\). Repeating a particular visited non-hub at step \(t\) has probability \(\beta_n\), yielding the common term \(F_{n,t-1}\beta_n^t\). If the hub appears, there are \(t-1\) possible positions among \(1,\ldots,t-1\), and the remaining \(t-2\) positions can be filled in \(F_{n,t-2}\) ways. A return to the root gives the second term in \(Q_n(t,0)\). For \(j\ge1\), either the hub is at position \(j\) and is repeated with probability \(\alpha_n\), or it is at one of the other \(t-2\) positions and a non-hub at \(j\) is repeated with probability \(\beta_n\). This gives exactly the second term in \(Q_n(t,j)\). The case \(t=1\) is a root self-loop, with probability \(\beta_n\). This proves all cells. Counting \(k\) novel successor selections similarly gives the survival identity: either none hits the hub, or exactly one hits it, at any of the \(k\) positions. By conditioning on \((T_n,J_n)\), the transient and cycle contain distinct vertices with disjoint independent marks, proving (1).

**Critical joint lasso limit.** Write \(t=\lfloor r\sqrt n\rfloor\), with \(r>0\) in a fixed compact subinterval of \((0,\infty)\), and use \(p_n\sqrt n\to a\). The product defining \(F_{n,t-2}\beta_n^{t-2}\) converges uniformly to \(\exp(-r^2/2-ar)\). For \(1\le j<t\), the exact cell formula gives uniformly
\[nQ_n(t,j)\longrightarrow (1+a^2+ar)\exp(-r^2/2-ar).\tag{8}\]
The total mass of \(J_n=0\) tends to zero. The exact tail formula yields (2), so \(T_n/\sqrt n\) is tight with a positive limiting law. Equation (8) is independent of \(j\); therefore the conditional index fraction tends to a uniform \(U\) independent of \(R_a\). The density of \(R_a\) is \(r(1+a^2+ar)e^{-r^2/2-ar}\), consistent with the integration of (8) over the triangular region \(0<j<t\). Conditional on lengths, each count is binomial with parameters \((J_n,q_{i,n})\) or \((T_n-J_n,q_{i,n})\), and all these binomials are mutually independent. Their joint generating functions converge on every bounded length window to the conditional Poisson expression, yielding (3) by tightness and dominated convergence.

For (4), \(\mathbb E R_0=\sqrt{\pi/2}\), \(\mathbb E R_0^2=2\), \(\mathbb E U=1/2\), and \(\mathbb E[U(1-U)]=1/6\). Conditional independence thus gives \(c_i c_j(2/6-(\pi/2)/4)\), the asserted coefficient. This negative covariance contrasts with independence in (6).

**Dominant-hub limit.** Explore successors until the hub is seen twice. In the independent destination choices, successive hits of the hub have Bernoulli probability \(\alpha_n\sim p_n\). Their waiting times are independent geometric variables, which converge after multiplying by \(p_n\) to independent mean-one exponentials. The probability that a non-hub vertex repeats before the second hub hit is bounded by \(O(1/(np_n^2))\): condition on the geometric total number of choices, whose second moment is \(O(p_n^{-2})\), and apply a union bound using the \(O(1/n)\) probability of each specified non-hub destination. The root is non-hub and its possible earlier repetition satisfies the same bound. Thus on an event of probability tending to one, the first repeated vertex is the hub and the two geometric waiting times equal the transient and cycle lengths, up to at most unit-index offsets. This proves (5). Finally the conditional binomial-to-Poisson limit gives independent Poisson counts with rates \(c_iE_1\) and \(c_iE_2\); integrating the two independent exponential densities yields (6). The temporal truth conditions give (7).

## Verification
The included standalone `checker.py` exhaustively sums the probabilities of all successor maps on \(2\), \(3\), \(4\), and \(5\) worlds for three rational reset probabilities, checking the entire array of exact cells against brute-force orbit exploration. It independently enumerates all labeled maps and valuations for a four-world test to confirm the bivariate generating formula and checks the critical/supercritical survival expressions numerically at increasing sizes. Execute with `python checker.py` using only the Python standard library. The program checks finite identities and illustrative convergence only; it is not a substitute for the infinite analytical argument above.

## Relationship to prior work
Lopuhaä-Zwakenberg, *Towards realistic large random models of labeled transition systems and their 0–1 laws*, arXiv:2607.15029 (first public version July 16, 2026), investigates logical limit behavior for independently present arcs and atomic labels in comparatively dense/random Kripke structures. The present random **function** with a preferred reset destination has exactly one successor per state; its repeated orbit and rare labels are a different regime.

Camarri and Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, *Electronic Journal of Probability* **5** (2000), paper 2, particularly Theorems 4 and 14, already establish strong general results about unequal-probability repeat times and first-occurrence indices. Accordingly **no novelty is claimed for the unmarked critical lasso limit by itself**, or for general weighted birthday distributions. What is claimed here is the finite explicit **labeled** joint generating function (1), its simultaneous rare-label temporal limit laws (3) and (6), and the change from negative transient/cycle mark correlation to independent multivariate geometric vectors. These require a distinct independent-valuation analysis absent from the inspected paper. Earlier random-mapping statistics provide a further background context.

## Limitations
The limit theorems assume fixed finitely many independent labels. Correlated propositional valuations, multiple outgoing edges, growing numbers of propositions, or uniform error rates are not addressed. Each regime is a weak-limit statement; finite enumeration is not an infinite proof. The underlying first-repeat/return-index scaling is substantially covered by Camarri–Pitman, and independent mark thinning makes the new labeling conclusions mathematically accessible; historical priority of the precise marked statements remains uncertain. A relevant older weighted-random-mappings thesis and other specialist sources were not available in complete text. No independent audit has been performed.

## References
1. M. Lopuhaä-Zwakenberg, *Towards realistic large random models of labeled transition systems and their 0–1 laws*, arXiv:2607.15029, version of July 16, 2026. https://arxiv.org/abs/2607.15029
2. M. Camarri and J. Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, *Electronic Journal of Probability* **5** (2000), paper 2, DOI: 10.1214/EJP.v5-58. https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/58/58-115-1-PB.pdf
3. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, in *Advances in Cryptology—EUROCRYPT '89*, Springer, 1990, DOI: 10.1007/3-540-46885-4_34 (background; accessible abstract only).
