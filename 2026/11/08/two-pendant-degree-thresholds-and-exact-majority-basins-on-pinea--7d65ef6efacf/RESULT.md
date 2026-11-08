# Two pendant-degree thresholds and exact majority basins on pineapple graphs

## Finding
For integers \(r\ge2\) and \(s\ge1\), form the pineapple graph \(P_{r,s}\) from a clique \(K_{r+1}\) by attaching \(s\) leaves to one distinguished clique vertex. Under synchronous binary **open-neighbor majority**, ties retain the existing bit. The number of fixed labelled configurations is
\[
\#\operatorname{Fix}(F)=2+2\mathbf 1_{\{s\ge r\}},
\]
and the number of primitive period-two orbits is
\[
Q_{r,s}=\mathbf1_{\{r\text{ odd}\}}\binom{r}{(r-1)/2}+2\mathbf1_{\{s>r\}}.
\]
No other recurrent periods occur. Every configuration becomes periodic within at most three updates. The sharp worst-case first-periodic-entry time is
\[
T_{\max}(r,s)=
\begin{cases}
1,&s>r,\ r\text{ even},\\
2,&s>r,\ r\text{ odd},\\
2,&s=1,\ r\text{ odd},\\
3,&\text{otherwise}.
\end{cases}
\]
Thus two successive leaf thresholds have different effects: two polarized equilibria appear at \(s=r\), while two additional primitive two-cycles appear only at \(s=r+1\). Odd cliques retain a separate central-binomial family of primitive two-cycles at every leaf count.

In the leaf-dominant regime \(s>r\), let
\[
C_r=\begin{cases}\binom{r}{(r-1)/2},&r\text{ odd},\\0,&r\text{ even},\end{cases}
\quad
B_{r,s}=\begin{cases}\binom{r+s}{(r+s)/2},&r+s\text{ even},\\0,&r+s\text{ odd},\end{cases}
\]
\[
A_s=\sum_{j=0}^{\lfloor(s-1)/2\rfloor}\binom{s}{j},
\qquad M_{r,s}=2^{r+s}.
\]
For \(N_{t,p}\) the number of labelled initial configurations first becoming periodic at update \(t\), with eventual least period \(p\), the complete nonzero classes are
\[
\begin{aligned}
N_{0,1}&=4,&N_{0,2}&=4+2C_r,\\
N_{1,1}&=M_{r,s}+B_{r,s}-4-2C_rA_s,&
N_{1,2}&=M_{r,s}-B_{r,s}-4-2C_r,\\
N_{2,1}&=2C_rA_s.
\end{aligned}
\]
All remaining classes have size zero. In particular, for independent fair initial bits,
\[
\Pr(\text{eventual least period }2)=\frac12-\frac{B_{r,s}}{2^{r+s+1}},
\]
which is exactly one half whenever \(r+s\) is odd and approaches one half as \(r+s\) increases. In this regime \(F^4=F^2\) for odd \(r\), and \(F^3=F\) for even \(r\).

## Assumptions and scope
The graph is finite and simple. The \(r\) ordinary clique vertices are labelled and distinct; one further clique vertex is the hub; the \(s\) leaves are labelled and share only the hub as their neighbor. Each initial labelling assigns an independently chosen bit in \(\{0,1\}\), and counts refer to **labelled** configurations. For a vertex with \(d\) neighbors and \(b\) neighbors carrying bit one, the next bit is one when \(2b>d\), zero when \(2b<d\), and the current bit when \(2b=d\). Updates are simultaneous. A state first enters a periodic orbit at time \(T\) when \(T\) is the smallest nonnegative integer for which some \(p>0\) obeys \(F^{T+p}(x)=F^T(x)\); \(p\) is the eventual least period.

## Proof
**Exact local reduction.** Let \(S\subseteq\{1,\ldots,r\}\) be the ordinary-clique vertices in state one, let \(m=|S|\), hub bit \(h\), and let \(\ell\) be the number of one-leaves. At the next step all leaves carry \(h\). The new hub bit \(h'\) is one, zero or \(h\) according as \(2(m+\ell)\) is greater than, less than or equal to \(r+s\). For each ordinary clique vertex of current bit \(b\), its number of one-neighbors is \(m-b+h\).

If \(r=2u\) is even, all ordinary clique bits become one iff \(m+h\ge u+1\), otherwise all become zero. If \(r=2u+1\) is odd, all become zero when \(m+h\le u\), they all become one when \(m+h\ge u+2\), and **every one of them flips** when \(m+h=u+1\). A homogeneous ordinary-clique group stays homogeneous in its current bit, regardless of later hub bits, for every \(r\ge2\).

**Classification of recurrent states.** Every periodic state has a uniform leaf group, because all leaves have the same state after one update. If the ordinary clique is mixed in a periodic state, it cannot become homogeneous later, since homogeneity persists. Thus \(r\) is odd and the flip case occurs at every step. Writing \(r=2u+1\), this forces the hub to alternate, the leaf bit to be the opposite of the hub bit, and the ordinary clique to alternate between a subset of size \(u+1\) when \(h=0\) and its complement of size \(u\) when \(h=1\). Such paired states really are two-cycles: the hub at \((m,h,a)=(u+1,0,1)\) sees \(u+1+s\) one-neighbors, a strict majority for every \(s\ge1\); its partner hub at \((u,1,0)\) sees only \(u\), a strict minority. There are exactly \(\binom{r}{u}\) distinct such primitive orbits.

For a homogeneous ordinary clique with bit \(x\), the hub–leaf pair \((h,a)\) obeys the following reduced rule, followed in each case by \(a'=h\):
\[
h'=\begin{cases}x,&s<r,\\x\text{ if }a=x,\text{ else }h,&s=r,\\a,&s>r.\end{cases}
\]
At \(s<r\), only \((h,a)=(x,x)\) is recurrent; at \(s=r\), both \((0,0)\) and \((1,1)\) are fixed for each \(x\); at \(s>r\), the pair is exchanged and all four assignments are periodic (two fixed and one primitive two-cycle for each \(x\)). Counting proves the fixed-state and two-cycle formulas. This analysis is exhaustive because no mixed state can become periodic except the alternating states above.

**Uniform transient bound and sharpness.** After one update the leaf group is homogeneous and, except for the odd-\(r\) flip case, the ordinary clique is homogeneous. For a homogeneous ordinary clique the reduced hub–leaf rule becomes periodic within at most two further steps when \(s\le r\), and is periodic immediately when \(s>r\). In the odd flip case, if the new hub differs from the old one, the first image is already one of the mixed two-cycle states. If the hub does not change, the second image is the all-zero or all-one consensus state (according to the initial hub). This proves the global upper bounds.

For \(s\le r\), set the initial hub to zero, precisely \(\lfloor r/2\rfloor\) ordinary clique bits to one, and all leaves to one. When \(r\) is even, or when \(r\) is odd and \(s\ge2\), the first image has ordinary clique zero, hub one and leaves zero; the next images successively give \((h,a)=(0,1)\) and \((0,0)\), proving \(T=3\). For odd \(r=2u+1\) and \(s=1\), any initial condition outside the flip case that makes the ordinary clique uniform with bit \(x\) at time one also makes the hub bit \(h_1=x\): when \(m_0+h_0\le u\) the hub cannot acquire a strict majority of ones and becomes zero; when \(m_0+h_0\ge u+2\) it becomes one. Hence the leaf copies the stable hub at time two, so time three is impossible. A flip-case state with \(h_0=0\), \(m_0=u+1\), and the leaf zero first reaches consensus at time two. When \(s>r\), any nonhomogeneous initial ordinary clique proves \(T=1\) for even \(r\), while the analogous odd flip-case construction proves \(T=2\). Hence all displayed worst-case bounds are exact.

**Exact leaf-dominant temporal census.** Suppose \(s>r\). After one step the hub follows the current uniform leaf value thereafter, while the leaves follow the previous hub; consequently the hub and leaves are periodic from time one. Let \(h_0\) and \(h_1\) be the hub states initially and after one update. If \(h_1\ne h_0\), eventual period is two; otherwise it is one. There are \(M_{r,s}-B_{r,s}\) labelled initial states with \(h_1\ne h_0\), obtained by counting strict-majority flips among the \(r+s\) neighbors of the hub, separately for the two initial hub bits and excluding ties. There are \(M_{r,s}+B_{r,s}\) remaining states.

The only states not yet periodic at time one are those with odd \(r=2u+1\), initial \(m+h_0=u+1\), and unchanged hub \(h_1=h_0\). They first reach a consensus state at time two. For each value of \(h_0\), exactly \(\binom{r}{u}\) ordinary-clique masks satisfy the boundary condition. The allowed original leaf counts are the lower or upper complementary binomial tail \(\ell\le\lfloor(s-1)/2\rfloor\) or \(\ell\ge s-\lfloor(s-1)/2\rfloor\), respectively, giving \(2C_rA_s\) labelled initial states. Subtracting these from the fixed-attractor basin and subtracting the already-periodic populations obtained above gives the displayed exact \(N_{t,p}\) formulas. Their sum is \(2^{r+s+1}\), the size of the full state space.

## Verification
Two reproducible, source-available programs independently check the theorem. `code/reduced_checker.py` enumerates binomial-weighted reduced states for 437 parameter pairs with \(2\le r\le50\), including all three leaf regimes, while `code/direct_checker.cpp` constructs actual graph adjacency lists and evolves 1,395,984 labelled binary states across 49 small parameter pairs. Both return PASS and validate the periodic-state counts, the sharp transient cases, and the complete \(s>r\) first-entry census. Reproduce with `python3 code/reduced_checker.py`, and with `c++ -O2 -std=c++17 code/direct_checker.cpp -o direct_checker && ./direct_checker`; the expected outputs are included under `evidence/`. The finite checks corroborate but do not replace the all-parameter proof.

## Relationship to prior work
The general period-at-most-two theorem for symmetric Boolean threshold systems is due to Goles and Olivos (1980); period restriction by itself is not new. Benjamini et al. (2014) survey deterministic majority dynamics and prove results for infinite unimodular and random graphs. Kaaser, Mallmann-Trenn and Natale (2015) study generic worst-case voting times via graph modules and potential functions. These works do not provide the present exact pineapple-graph attractor counts, two sharp pendant-degree thresholds, or high-leaf full first-entry distribution. A separate previously known one-leaf case, \(s=1\), does not cover variable \(s\): the new equilibria and uniform-clique two-cycles exist only for larger leaf counts. The conclusions are a statement about the open-neighbor majority rule, not asynchronous voter models or parity updates.

## Limitations
The graph restriction is essential: the proof uses the identical neighborhood of the ordinary clique vertices and the common attachment hub for all leaves. The first-entry distribution is claimed in closed form only for \(s>r\); for \(s\le r\) the result proves the exact recurrent census and sharp maximal transient, not an explicit census of every transient layer. Literature searches cannot exclude an unindexed equivalent classification. The verification is a proof and self-review, not independent peer review or formal proof-assistant certification.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first public preprint 2014-05-11, arXiv:1405.2486v1, https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, first public preprint 2015-08-14, arXiv:1508.03519v1, https://arxiv.org/abs/1508.03519.
