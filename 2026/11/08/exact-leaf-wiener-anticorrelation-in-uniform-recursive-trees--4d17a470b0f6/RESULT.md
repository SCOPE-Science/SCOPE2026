# Exact leaf–Wiener anticorrelation in uniform recursive trees

## Finding
For every integer \(n\ge2\), construct the uniform random recursive tree \(T_n\) on \(\{1,\ldots,n\}\): independently for each \(j=2,\ldots,n\), choose the parent of \(j\) uniformly from \(\{1,\ldots,j-1\}\). Let \(L_n\) count vertices of outdegree zero, and let \(W_n=\sum_{1\le u<v\le n}d_{T_n}(u,v)\) be its Wiener index, summing unordered-pair edge distances. With \(H_n=\sum_{j=1}^n 1/j\),

\[
\operatorname{Cov}(L_n,W_n)=nH_n-\frac{n(n+5)}4+\frac12.
\]

The covariance vanishes for \(n=2,3\), is strictly negative for every \(n\ge4\), and satisfies \(\operatorname{Cov}(L_n,W_n)/n^2\to-1/4\). An accompanying exact identity exposes the local–global mechanism. Define the transmission \(s_T(v)=\sum_{u\in V(T)}d_T(u,v)\) and \(Q_n=\sum_{v:\operatorname{outdeg}_{T_n}(v)=0}s_{T_n}(v)\). Then

\[
\mathbb E Q_n-\mathbb E W_n=\frac{(n-1)(n-2)}4.
\]

Thus the expected aggregate transmission of leaves exceeds that of nonleaves by exactly \((n-1)(n-2)/2\), since all-vertex transmission is \(2W_n\). Using the established Wiener-index variance asymptotic of Neininger (2002) and the elementary leaf variance, the correlation also satisfies

\[
\operatorname{Corr}(L_n,W_n)\sim-\frac{3\sqrt6}{2\sqrt{31-3\pi^2}}\,n^{-1/2}.
\]

## Assumptions and scope
The parent selections are independent and uniformly distributed among older vertices. All distances are undirected edge distances, the Wiener index counts each unordered pair once, and leaves are **rooted** leaves (outdegree zero), not all unrooted degree-one vertices. The one-vertex tree has one rooted leaf and zero Wiener index; the formula is claimed for \(n\ge2\). No statement is made about preferential-attachment or uniform Cayley-tree laws.

## Proof
Let \(\mathcal F_m\) be the information in \(T_m\), and let \(U\) be the independent uniform parent selected from its \(m\) vertices for the next arrival. Set \(J=\mathbf1\{U\text{ is a rooted leaf}\}\), \(S=s_{T_m}(U)\), and \(Q_m=\sum_{v\text{ rooted leaf}}s_{T_m}(v)\). We have the pathwise updates

\[
L_{m+1}=L_m+1-J,\qquad W_{m+1}=W_m+m+S.
\]

Since \(\sum_{u}s_{T_m}(u)=2W_m\), the conditional expectations satisfy

\[
\mathbb E(J\mid\mathcal F_m)=\frac{L_m}{m},\quad
\mathbb E(S\mid\mathcal F_m)=\frac{2W_m}{m},\quad
\mathbb E(JS\mid\mathcal F_m)=\frac{Q_m}{m}.
\]

When adding vertex \(m+1\), every old rooted leaf \(v\) gains distance \(d(v,U)+1\) to the new vertex; an old leaf selected as parent ceases to be a leaf, and the new vertex is a leaf of transmission \(m+S\). Consequently, **pathwise**,

\[
Q_{m+1}=Q_m+\sum_{v\text{ old leaf}}(d(v,U)+1)-J(S+1)+m+S.
\]

Taking conditional expectations, and noting \(\mathbb E_U\sum_{v\text{ leaf}}d(v,U)=Q_m/m\), gives

\[
\mathbb E(Q_{m+1}\mid\mathcal F_m)=Q_m+m+\left(1-\frac1m\right)L_m+\frac{2W_m}{m}.
\]

Meanwhile \(\mathbb E(W_{m+1}\mid\mathcal F_m)=(1+2/m)W_m+m\). For \(m\ge2\), the well-known expectation \(\mathbb E L_m=m/2\) follows directly from the leaf update and the base case \(L_2=1\). Subtracting the expectation recurrences and using \(\mathbb E Q_2=\mathbb E W_2=1\) proves, by summing \((m-1)/2\),

\[
\Delta_m:=\mathbb E W_m-\mathbb E Q_m=-\frac{(m-1)(m-2)}4\quad(m\ge2).
\]

Let \(C_m=\operatorname{Cov}(L_m,W_m)\). The law of total covariance, including its conditional covariance term, gives

\[
\begin{aligned}
C_{m+1}
&=\left(1-\frac1m\right)\left(1+\frac2m\right)C_m
-\frac{\mathbb E Q_m}{m}+\frac{2\mathbb E(L_mW_m)}{m^2}\\
&=\frac{m+1}{m}C_m+\frac{\Delta_m}{m},\qquad(m\ge2).
\end{aligned}
\]

The initial covariance \(C_2=0\). Dividing by \(m+1\) and telescoping gives

\[
C_n=-\frac n4\sum_{m=3}^{n-1}\frac{(m-1)(m-2)}{m(m+1)}.
\]

The sum is empty for \(n=2,3\), and strictly positive for \(n\ge4\). For \(m\ge3\), partial fractions yield \((m-1)(m-2)/(m(m+1))=1+2/m-6/(m+1)\). Summation proves the claimed closed form. Its leading asymptotic follows from \(H_n=\log n+\gamma+O(1/n)\).

For the correlation refinement, the same conditional Bernoulli leaf update gives \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\); Neininger's random-recursive-tree theorem gives \(\operatorname{Var}(W_n)\sim (31-3\pi^2)n^4/18\). Substituting the proven covariance asymptotic yields the displayed correlation coefficient.

## Verification
Run `python3 checker.py` with Python 3 and no external dependencies. The verifier independently enumerates every valid parent sequence for \(2\le n\le9\) (the largest case has \(8!=40320\) trees), computes leaf counts and Wiener indices using breadth-first graph distances, computes \(Q_n\) directly, and verifies the three exact expectations and the covariance for each order. It separately checks the rational recurrences and closed forms for \(2\le n\le501\). An observed run passed 2532 exact assertions. These finite tests corroborate the algebraic proof; they do not prove the infinite quantifiers.

## Relationship to prior work
Neininger (2002) analyzes the exact expected Wiener index and its joint asymptotics with *internal path length* in random recursive trees. The accessible full-text manuscript was consulted, including Theorem 1.2, its random-recursive-tree recurrence, and searches for leaf terminology; it does not discuss rooted leaf count or its covariance with the Wiener index. Holmgren and Janson (2015) treat fringe-tree counts, including leaf-type local statistics, but their published abstract and accessible bibliographic materials do not state the present mixed local–global covariance; the complete article could not be retrieved in this examination. The separate source areas (Wiener/global path length and fringe/local counts) do not by themselves imply the exact cross-covariance identity. Comparisons were also made with existing records about recursive-tree root degree/path length, root degree/leaves, and fixed-label degrees/path length. None of those statements yields the mixed leaf-count/Wiener covariance, which is a distinct global distance functional.

## Limitations
The claim concerns the uniform recursive-tree model only. A negative covariance does not imply monotone regression or stochastic dominance conditional on the number of leaves; neither is asserted. Independence, external certification, and historical priority have not been established. Broad general-purpose additive-functional techniques could conceivably contain an implicit equivalent; a complete comparison with the full Holmgren–Janson paper was not possible. The correlation asymptotic uses a previously published variance constant rather than a new independent variance proof.

## References
- R. Neininger, *The Wiener Index of Random Trees*, Combinatorics, Probability and Computing **11** (2002), 587–597, https://doi.org/10.1017/S0963548302005321 ; accessible author manuscript https://www.math.uni-frankfurt.de/~neiningr/w-ind.pdf (Theorem 1.2).
- C. Holmgren and S. Janson, *Limit laws for functions of fringe trees for binary search trees and random recursive trees*, Electronic Journal of Probability **20** (2015), https://arxiv.org/abs/1406.6883 ; https://doi.org/10.1214/EJP.v20-3627.
- J.-F. Delmas, J.-S. Dhersin and M. Sciauveau, *Cost functionals for large random trees*, AofA 2016 conference proceedings, https://aofa.tcs.uj.edu.pl/proceedings/aofa2016.pdf (general local/global additive-functional context; not a proof source).
