# All-order bond-cumulant sign staircases on finite cactus random-cluster models

## Finding
Let \(G=(V,E)\) be any finite simple cactus graph, possibly disconnected, and let \(q>0\) and all edge activities \(v_e>0\). In its free-boundary random-cluster distribution,
\[
\Pr(A)=\frac{q^{k(A)}\prod_{e\in A}v_e}{\sum_{B\subseteq E}q^{k(B)}\prod_{e\in B}v_e},\qquad A\subseteq E,
\]
let \(X_e=\mathbf1_{\{e\in A\}}\). Choose \(r\ge2\) **distinct** edges \(S=\{e_1,\dots,e_r\}\). If no single simple cycle of \(G\) contains all of \(S\), their connected joint cumulant \(\kappa_r(X_{e_1},\dots,X_{e_r})\) is exactly zero.

Otherwise let \(C\) be their unique containing cycle and put
\[
u_e=\frac{v_e}{q+v_e},\quad R_C=\prod_{f\in C}u_f,\quad b_C=(q-1)R_C.
\]
Let \(E_s(z)=\sum_{j=0}^{s-1}\left\langle {s\atop j}\right\rangle z^j\) be the classical Eulerian polynomial, where the coefficient is the number of permutations of \(s\) letters with exactly \(j\) descents. Then, for every allowable \(r\),
\[
\boxed{\displaystyle
\kappa_r(X_{e_1},\ldots,X_{e_r})=
\left(\prod_{i=1}^{r}(1-u_{e_i})\right)
\frac{b_C E_{r-1}(-b_C)}{(1+b_C)^r}.}
\]

This gives the **complete sign diagram**, with all zero cases included. For \(0<q<1\), every such same-cycle cumulant is strictly negative, whatever its order and the positive edge weights; for \(q=1\), all distinct-edge mixed cumulants vanish. For \(q>1\), write the \(r-2\) positive simple roots of \(E_{r-1}(-b)\) as
\[
0<\beta_{r,1}<\cdots<\beta_{r,r-2}
\]
(the list is empty for \(r=2\)). The sign is that of \(\prod_{j=1}^{r-2}(\beta_{r,j}-b_C)\); hence it alternates at exactly these roots, starting positive near \(b_C=0\).

In particular, fix arbitrary positive base activities \(w_e\) and set \(v_e=t w_e\) for \(t>0\). Then the \(r\)-edge cumulant on \(C\) changes sign **exactly once for each root** with \(\beta_{r,j}<q-1\), and never elsewhere. Each crossing is simple and occurs at the unique \(t>0\) solving
\[
\prod_{f\in C}\frac{t w_f}{q+t w_f}=\frac{\beta_{r,j}}{q-1}.
\]
Equality \(\beta_{r,j}=q-1\) produces no finite crossing. Every choice of \(r\) distinct edges on the same cycle crosses at the same activity scales. For sufficiently large \(q\), all \(r-2\) crossings occur, for every cycle of length at least \(r\). These are finite-graph analytic sign changes, **not thermodynamic phase transitions**.

For order four, \(E_3(-b)=1-4b+b^2\), whose roots are \(2\pm\sqrt3\). Thus on every cycle of length at least four, the fourth distinct-edge cumulant undergoes two sign reversals if and only if \(q>3+\sqrt3\); for \(3-\sqrt3<q\le3+\sqrt3\) it undergoes exactly one. On a four-cycle with \(q=6\) and uniform activities it has the sign sequence \(+,-,+\). For order five, \(E_4(-b)=(1-b)(1-10b+b^2)\), with roots \(5-2\sqrt6,1,5+2\sqrt6\). A five-cycle with \(q=12\) and uniform activities has exactly three consecutive sign reversals.

## Assumptions and scope
A simple cactus is a finite simple undirected graph in which each edge lies on at most one simple cycle. Cycles may intersect in articulation vertices but not in edges; bridges and isolated vertices are allowed. \(k(A)\) is the number of components of the spanning subgraph \((V,A)\), including isolated vertices. The cluster weight \(q\) is an arbitrary real positive number (it need not be an integer), and every \(v_e\) is strictly positive and finite. The cumulant is the mixed derivative
\[
\kappa_r(X_{e_1},\ldots,X_{e_r})=
\left.\frac{\partial^r}{\partial t_1\cdots\partial t_r}
\log\mathbb E\exp\left(\sum_{i=1}^r t_iX_{e_i}\right)\right|_{t_1=\cdots=t_r=0}.
\]
Every edge in the cumulant must be distinct. The statements about sign changes under uniform scaling assume all base weights \(w_e\) are fixed and positive while \(q\) is held fixed.

## Proof
**1. Independent cycle-block factorization.** Write \(\mathcal C\) for the edge-disjoint host cycles. The only cycles of any spanning subgraph \((V,A)\) are fully present host cycles; therefore its cyclomatic number equals \(\sum_{C\in\mathcal C}\mathbf1_{\{C\subseteq A\}}\). The graphical identity gives
\[
k(A)=|V|-|A|+\sum_{C\in\mathcal C}\mathbf1_{\{C\subseteq A\}}.
\]
Consequently the unnormalized weight is
\[
q^{|V|}\prod_{e\in A}(v_e/q)
\prod_{C\in\mathcal C}\left[1+(q-1)\mathbf1_{\{C\subseteq A\}}\right].
\]
This factors over disjoint edge blocks: each bridge is an independent Bernoulli variable of parameter \(u_e=v_e/(q+v_e)\), and the cycles are mutually independent. A cycle block is an independent Bernoulli product measure with probabilities \(u_e\), tilted by \(1+(q-1)\mathbf1_{\{X_f=1\ \forall f\in C\}}\). Its normalizer relative to the Bernoulli product is \(1+b_C>0\), including when \(0<q<1\). Mixed cumulants of variables belonging to independent blocks vanish, proving the first part.

**2. Exact cumulant operator.** Restrict to \(S\subseteq C\). Set \(m_i(t)=1-u_{e_i}+u_{e_i}e^t\). The exact joint moment-generating function is
\[
M_S(\boldsymbol t)=
\frac{\prod_{i=1}^r m_i(t_i)+b_Ce^{t_1+\cdots+t_r}}{1+b_C}.
\]
Factoring the first product, \(\log M_S\) is the sum of single-variable terms \(\sum_i\log m_i(t_i)\), the constant \(-\log(1+b_C)\), and
\[
\log\left(1+b_C\prod_{i=1}^r\frac{e^{t_i}}{m_i(t_i)}\right).
\]
For distinct derivatives, the single-variable terms do not contribute. Since \(e^t/m_i(t)\) equals one at zero and has derivative \(1-u_{e_i}\) there, repeated mixed differentiation yields
\[
\kappa_r(X_{e_1},\ldots,X_{e_r})=
\left(\prod_{i=1}^r(1-u_{e_i})\right)
\left[(b\partial_b)^r\log(1+b)\right]_{b=b_C}.
\]
This is an identity of rational functions and remains valid for negative \(-1<b_C<0\); it does not rely on an invalid positive-mixture interpretation when \(q<1\).

**3. Eulerian rational function and simple positive sign roots.** Define \(D=b\partial_b\). The classical power-series identity (initially for \(|b|<1\), then by rational continuation) is
\[
D^r\log(1+b)=\sum_{m\ge1}(-1)^{m+1}m^{r-1}b^m
=\frac{bE_{r-1}(-b)}{(1+b)^r},\qquad r\ge2.
\]
For completeness, put \(Q_r(b)=E_{r-1}(-b)\). It is characterized without any external root theorem by \(Q_2=1\) and
\[
Q_{r+1}(b)=(1-(r-1)b)Q_r(b)+b(1+b)Q'_r(b).
\]
This recurrence gives \(Q_3=1-b\), \(Q_4=1-4b+b^2\), and \(Q_5=1-11b+11b^2-b^3\). It also proves by induction that \(Q_r(0)=1\), its degree is \(r-2\), and its leading coefficient has sign \((-1)^{r-2}\). Suppose its \(r-2\) roots are distinct and positive. At every such root \(\beta\),
\[
Q_{r+1}(\beta)=\beta(1+\beta)Q'_r(\beta).
\]
These values alternate in sign between successive roots. Together with \(Q_{r+1}(0)=1\) and its opposite sign beyond the last root, the intermediate-value theorem forces \(r-1\) distinct positive roots of \(Q_{r+1}\), one in every complementary interval of \([0,\infty)\). Its degree is \(r-1\), so all these roots are simple and exhaustive. The base case \(Q_2=1\) completes induction. The Eulerian coefficients are positive, so \(Q_r(b)>0\) whenever \(b\le0\). Combining these facts with the rational cumulant formula proves the full fixed-parameter sign classification.

**4. Sharp crossing count.** When \(q>1\) and \(v_e=t w_e\), every factor \(t w_e/(q+t w_e)\) increases strictly and continuously from zero to one as \(t\) increases from zero to infinity. Thus \(b_C(t)=(q-1)\prod_{f\in C}t w_f/(q+t w_f)\) increases bijectively from \((0,\infty)\) onto \((0,q-1)\). It crosses a simple root \(\beta_{r,j}\) exactly once if and only if \(\beta_{r,j}<q-1\). The product prefactor and denominator are strictly positive. Hence every finite zero is a genuine sign reversal, there are no additional ones, and the same \(b_C(t)\) controls all choices of \(r\) distinct cycle edges. The order-four and order-five statements follow from the displayed polynomials. \(\square\)

## Verification
The standalone `verify.py` uses only the Python standard library. It enumerates every edge subset in four small cactus networks (including one and two cycles, articulation vertices, and bridges), computes exact component counts and rational random-cluster weights at six distinct values \(q\in\{1/2,1,3/2,2,6,12\}\), and compares cumulants obtained independently from the set-partition Möbius formula against the claimed closed form. It passed 2,154 exact-rational cumulant comparisons for distinct edge subsets of sizes two through five. It also checks the explicit Eulerian polynomials through order five and exact positive/negative/positive order-four and positive/negative/positive/negative order-five sign witnesses. Execute `python3 verify.py`; the output is `CYCLE_BLOCK_CUMULANTS_EXACT_OK 2154 polynomial_orders_2_to_5 cycle4_signs [1, -1, 1] cycle5_signs [1, -1, 1, -1]`. These finite tests supplement rather than replace the all-graph proof.

## Relationship to prior work
Grimmett's foundational random-cluster survey (first submitted 23 May 2002) defines the Fortuin–Kasteleyn measure and its relation to Ising/Potts models, but the inspected finite-graph definitions and correlation sections do not supply this higher-order cycle sign staircase. An existing cactus negative-association analysis (research record `3f0dfb35e019`) gives a block-factorization and a rank-one pair-covariance formula for \(0<q\le1\); those structural ingredients are not claimed to be new here. Its theorem does not establish arbitrary-order joint cumulants at \(q>1\), the Eulerian root thresholds, or the possibility of \(r-2\) separate positive-activity sign reversals. Çiçeksiz and Ravichandran study edge-pair negative correlations in forests and \(0<q<1\) random-cluster models on other graph classes, without a same-cycle all-order result. Classical real-rootedness of Eulerian polynomials is also not claimed as new; a complete induction is included so the sign analysis is self-contained.

## Limitations
The exact cancellation and block independence require a cactus: graphs with overlapping cycles need not satisfy the formula. This result concerns cumulants of **distinct bond occupations**, not spin cumulants, repeated-edge cumulants, aggregate energy cumulants, or connectivity-event cumulants. It concerns finite simple graphs, arbitrary positive activities and free-boundary measures. The crossing counts are for uniform positive scaling at fixed \(q\); they are not assertions about thermodynamic singularities or general joint variation of activities. An unindexed prior all-order cycle result or an earlier analytic extension of known rank-one formulas could cover some or all of the stated classification. Independent external mathematical audit and independent historical-priority review have not been performed.

## References
1. Geoffrey Grimmett, *The Random-Cluster Model*, arXiv:math/0205237v1 (first public 2002-05-23), https://arxiv.org/abs/math/0205237 . Relevant material: definitions and coupled Potts/cluster constructions in Sections 2.1–2.3.
2. *Conditional negative association without real stability in random-cluster and forest measures on cactus graphs* (2026 research record `3f0dfb35e019`). Relevant material: the full stated cycle-block decomposition and pair-covariance theorem for \(0<q\le1\); this is a closest structural precursor, not a proof of the present sign staircase.
3. R. Altar Çiçeksiz and Mohan Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model*, arXiv:2610.00549v1 (first public 2026-09-30), https://arxiv.org/html/2610.00549v1 . Relevant material: Introduction and Sections 1, 5 (pairwise Rayleigh differences and negative correlations).
