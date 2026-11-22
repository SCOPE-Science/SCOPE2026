# Universal three-path cumulant reversal at the two-state Potts boundary

## Finding

For the ferromagnetic random-cluster bond measure on a finite three-path theta network, the connected three-edge occupation correlation, with one marked edge on each path, has an explicit all-weight formula and a sharp cluster-weight transition at \(q=2\).

Let the three internally vertex-disjoint terminal paths be \(P_1,P_2,P_3\), each with at least two edges. For real \(q>1\) and individual edge activities \(v_e>0\), set
\[
p_e=\frac{v_e}{q+v_e},\qquad a_i=\prod_{e\in P_i}p_e,\qquad e_1=a_1+a_2+a_3,\quad e_2=a_1a_2+a_1a_3+a_2a_3,\quad e_3=a_1a_2a_3.
\]
Put
\[
H_q=1+(q-1)e_2+(q-1)(q-2)e_3
\]
and
\[
F_q=(2-q)+2(q-1)e_1+(q-1)(q-2)e_2+(q-1)(q^2-2q+2)e_3.
\]
For any distinct selected edges \(f_i\in P_i\), write \(X_{f_i}\in\{0,1\}\) for their open-bond indicators. Their third joint cumulant is exactly
\[
\boxed{\kappa_3(X_{f_1},X_{f_2},X_{f_3})
=-\frac{(q-1)e_3\prod_{i=1}^3(1-p_{f_i})}{H_q^3}\,F_q.}
\]
All factors outside \(-F_q\) are strictly positive.

For every \(1<q\le2\), this third cumulant is strictly **negative**, for arbitrary positive edge activities and path lengths. For every \(q>2\), fix arbitrary base activities \(w_e>0\) and scale all edge activities as \(v_e=s w_e\), \(s>0\). There exists a **unique** \(s_*\in(0,\infty)\) solving \(F_q=0\); the cumulant is strictly positive for \(0<s<s_*\), zero at \(s_*\), and strictly negative for \(s>s_*\). The location \(s_*\) is independent of which edge is selected on each path. At \(q=1\) the edges are independent and all such mixed cumulants vanish.

In particular, on \(K_{2,3}\), with each of the six edges having activity \(v>0\) and \(q=3\), put \(p=v/(3+v)\). The unique reversal satisfies
\[
10p^6+6p^4+12p^2-1=0,\qquad p\in(0,1),
\]
and occurs at \(v\approx1.1804220558\). In the \(q=2\) model on the same network the third cumulant is strictly negative at every finite positive activity.

## Assumptions and scope

The underlying network is a finite simple theta graph consisting of exactly three internally vertex-disjoint paths between two terminals. Each path has integer length at least two. The random-cluster probability of an open edge set \(A\subseteq E\) is proportional to
\[
q^{k(A)}\prod_{e\in A}v_e,
\]
where \(k(A)\) counts connected components of the spanning subgraph \((V,A)\); all edges have strictly positive finite activities. The theorem concerns one **distinct** bond indicator from each of the three paths, the mixed cumulant \(\mathbb E[X_1X_2X_3]-\sum_{i<j}\mathbb E[X_iX_j]\mathbb E[X_k]+2\prod_i\mathbb E[X_i]\). The last index \(k\) in the sum is the unique element of \(\{1,2,3\}\setminus\{i,j\}\). No thermodynamic-limit statement is intended.

## Proof

**1. Exact independent-path reference law.** For a spanning subgraph of this connected theta graph, the cycle surplus is \(b(A)=|A|-|V|+k(A)\). Let \(Y_i\) indicate whether every edge in path \(P_i\) is open and let \(R=Y_1+Y_2+Y_3\). Since there is no cycle until at least two entire terminal paths are present, and exactly \(R-1\) independent cycles if \(R\ge2\),
\[
b(A)=\max(R-1,0).
\]
Rewrite the weight as \(q^{|V|}\prod_{e\in A}(v_e/q)\,q^{b(A)}\). After normalization, this is a product law with independent bond probabilities \(p_e=v_e/(q+v_e)\), tilted by \(h(R)=q^{\max(R-1,0)}\). Under the untilted law the three path-completion indicators are independent Bernoulli random variables of probabilities \(a_1,a_2,a_3\). Since \(h(0)=h(1)=1\), \(h(2)=q\), and \(h(3)=q^2\), the tilt normalizer is
\[
H_q=1+(q-1)(a_1a_2+a_1a_3+a_2a_3)+(q-1)(q-2)a_1a_2a_3>0.
\]

**2. Third cumulant of the path-completion variables.** Under the tilted path-completion law, define its marked generating function
\[
G(t_1,t_2,t_3)=\sum_{S\subseteq\{1,2,3\}}h(|S|)\prod_{i\in S}(a_i e^{t_i})\prod_{i\notin S}(1-a_i).
\]
Then \(G(0,0,0)=H_q\) and the third mixed derivative of \(\log G\) at the origin is the third cumulant. Expanding its eight terms, using
\[
\kappa_3(Y_1,Y_2,Y_3)=\frac{G_{123}G^2-G(G_{12}G_3+G_{13}G_2+G_{23}G_1)+2G_1G_2G_3}{G^3}\bigg|_{t=0},
\]
gives the exact factorization
\[
\kappa_3(Y_1,Y_2,Y_3)=-\frac{(q-1)a_1a_2a_3\prod_{i=1}^3(1-a_i)}{H_q^3}F_q.
\]
This identity can also be expanded as a rational-polynomial identity in \(a_1,a_2,a_3,q\), and is independently checked in the included exact enumerator.

**3. From path completion to marked edges.** Conditional on \((Y_1,Y_2,Y_3)\), the bonds on different paths are independent; for a marked edge \(f_i\in P_i\),
\[
\mathbb E[X_{f_i}\mid Y_i]=\frac{p_{f_i}-a_i}{1-a_i}+\frac{1-p_{f_i}}{1-a_i}Y_i.
\]
Every \(a_i\) lies strictly between zero and one. The distinct-variable conditional independence implies that the third joint cumulant equals the product of the three slope factors \((1-p_{f_i})/(1-a_i)\) times the third cumulant of \((Y_1,Y_2,Y_3)\). Cancellation of \(\prod_i(1-a_i)\) yields the boxed formula.

**4. Sharp sign and unique transition.** For \(1<q<2\), we have \(0<e_2\le e_1\) and \(q^2-2q+2>0\), so
\[
F_q=(2-q)+(q-1)[2e_1-(2-q)e_2+(q^2-2q+2)e_3]>0.
\]
At \(q=2\), \(F_2=2(e_1+e_3)>0\). For \(q>2\), the constant coefficient \(2-q\) is negative and all coefficients of the nonconstant elementary symmetric terms in \(F_q\) are positive. Thus \(F_q\) is strictly increasing in each \(a_i\), with \(F_q(0,0,0)=2-q<0\) and \(F_q(1,1,1)=q^3>0\). Under uniform scaling \(v_e=s w_e\), each \(a_i(s)\) increases continuously and strictly from zero to one. Consequently \(F_q(a_1(s),a_2(s),a_3(s))\) has exactly one zero \(s_*\) and its sign switches there. The prefactor is strictly negative, proving the positive-to-negative cumulant reversal. For \(q=1\), the original spanning-subgraph measure is a product Bernoulli law.

**5. Six-edge illustration.** On \(K_{2,3}\), each path has length two, and under equal edge activity \(v\), \(a_1=a_2=a_3=p^2\). Inserting these into \(F_3\) gives \(-1+12p^2+6p^4+10p^6\), which is strictly increasing on \((0,1)\), negative at zero and positive at one. This gives the displayed unique threshold. Numerical digits are illustrative only; uniqueness follows symbolically.

## Verification

The included standalone `check_theta.py` uses exact rational arithmetic and independently enumerates all open-edge configurations, calculating each selected-edge third cumulant from its seven joint moments, rather than using the path-completion law. It matches the boxed formula in **972** distinct exact cases across five theta path-length triples, four rational cluster parameters \(q\in\{3/2,2,3,4\}\), three activity scales, and every choice of one edge from each path. It also independently confirms opposite signs at activities \(1/10\) and \(10\) for the uniform \(K_{2,3}\), \(q=3\) example. Run `python check_theta.py` with standard Python 3; no external dependencies are required. These tests supplement, rather than replace, the all-length proof.

## Relationship to prior work

The random-cluster representation and its positive-association theory are classical [1]. For \(q\ge1\), positive association controls pairwise increasing-event covariances, not the sign of distinct-bond third cumulants. Shrock's exact Potts/Tutte calculations for vertex-inflated networks include the uniform hammock family [2, Section IX], which contains equal-length theta networks; those partition-function formulas do not state the present all-weight three-edge connected-correlation sign law or its sharp \(q=2\) boundary. Existing published calculations for the \(q<1\) forest and subcritical-cluster regimes are on the other side of the cluster-weight boundary and do not establish the current \(q>2\) sign reversal. This finding does not claim originality of the random-cluster expansion, the hammock partition function, or ordinary two-point association.

## Limitations

The theorem applies only to three internally disjoint terminal paths with one marked edge from each. It does not cover four or more parallel terminal paths, three marked edges in one or two paths, general series-parallel graphs, negative activities, or all higher-order cumulants. Correlation sign changes are finite-system response crossings, not thermodynamic phase transitions. The search-based novelty assessment is provisional and cannot exclude earlier unindexed equivalent or stronger statements; independent review has not been performed.

## References

1. Geoffrey Grimmett, *The Random-Cluster Model*, initial arXiv public submission 2002-05-23, arXiv:math/0205237, https://arxiv.org/abs/math/0205237. The inspected source establishes the random-cluster definition and positive-association framework.
2. Robert Shrock, *Exact Results on Potts/Tutte Polynomials for Families of Networks with Edge and Vertex Inflations*, initial arXiv public submission 2011-01-30, arXiv:1101.5826, https://arxiv.org/abs/1101.5826. See the graphical expansion and Section IX on hammock networks.
