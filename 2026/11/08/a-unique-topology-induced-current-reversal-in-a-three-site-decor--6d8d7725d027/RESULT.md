# A unique topology-induced current reversal in a three-site-decorated exclusion ring

## Finding

**Theorem (sharp minimal side-branch current reversal).** Let \(m\geq2\) be an integer and consider a periodic asymmetric simple exclusion process with \(L=2m\) backbone sites and \(N=m+2\) indistinguishable particles. The clockwise and counterclockwise rates on backbone bonds are \(h_f>h_b\geq0\). Compare two systems having exactly three additional sites, with the same outward/inward tree hopping-rate ratio \(q>1\) and strictly positive tree rates:

- The **leaf decoration** has three one-edge dead-end branches at three distinct backbone vertices (depth multiset \((1,1,1)\)).
- The **chain decoration** has one three-edge dead-end branch at a backbone vertex (depth multiset \((1,2,3)\)).

Write \(J_{\mathrm{leaf}}(m,q)\) and \(J_{\mathrm{chain}}(m,q)\) for the unique stationary **net clockwise current across one backbone bond**. There is exactly one number \(q_m>1\) such that

\[
\begin{aligned}
1<q<q_m&\quad\Longrightarrow\quad J_{\mathrm{chain}}>J_{\mathrm{leaf}},\\
q=q_m&\quad\Longrightarrow\quad J_{\mathrm{chain}}=J_{\mathrm{leaf}},\\
q>q_m&\quad\Longrightarrow\quad J_{\mathrm{chain}}<J_{\mathrm{leaf}}.
\end{aligned}
\]

The crossing is the unique positive root of the explicit degree-six polynomial

\[
\begin{aligned}
F_m(q)={}&(2m^2+6m+4)q^6+(m^2+3m+2)q^5\\
&-6(m^2+m+1)q^4-(10m^2+6m+2)q^3\\
&-(14m^2+6m-2)q^2-3(m-1)(5m+4)q\\
&-6m(m-1).
\end{aligned}
\]

Furthermore \(q_m\) grows **strictly** with \(m\), and

\[
q_m=Q-\frac{c}{m}+O(m^{-2}),\qquad
Q=2.39645145449\ldots,\qquad c=2.02742009796\ldots,
\]

where \(Q\) is the unique root greater than one of \(2Q^3-5Q^2+3Q-6=0\), and

\[
c=\frac{3(Q-1)^2(2Q^2+Q+2)}{(Q+1)(6Q^2-10Q+3)}>0.
\]

**Minimality in decoration size.** For every backbone length \(L\geq3\), every \(1\leq N\leq L+1\), and every \(q>1\), a single depth-two chain \((1,2)\) and two depth-one leaves \((1,1)\) have a **fixed current ordering independent of \(q\)**: the chain has smaller current when \(N\leq\lfloor(L+2)/2\rfloor\), and larger current when \(N>\lfloor(L+2)/2\rfloor\). Both currents are multiplied by the same positive factor \(h_f-h_b\). One side site offers no nonisomorphic depth alternative. Thus three side sites are the smallest decoration size at which a change of ranking with \(q>1\) is possible in this leaf-versus-chain comparison.

For example, at \(L=4\), \(N=4\) and normalized backbone bias \(h_f-h_b=1\), the current difference \(J_{\mathrm{chain}}-J_{\mathrm{leaf}}\) is \(2031/800080>0\) at \(q=3/2\) but \(-152/83721<0\) at \(q=2\). Here \(q_2=1.80891189065\ldots\).

## Assumptions and scope

The backbone is a simple directed ring with \(L\geq3\) vertices and exclusion occupancy \(\eta_v\in\{0,1\}\). On each backbone nearest-neighbor bond, particles move clockwise at rate \(h_f\) and counterclockwise at rate \(h_b\), only when the destination is empty. Branch edges have outward rate \(h_t>0\) and inward rate \(h_r>0\), with \(q=h_t/h_r>1\). There are no particle sources or sinks. The total particle number is fixed as specified. The stationary process is irreducible on its fixed-particle-number sector because the underlying graph is connected and every branch edge can be traversed in both directions, while the backbone has clockwise hopping \(h_f>0\). The comparison involves **net current per backbone bond**, not a sum over all backbone bonds or total activity on branch edges. The choice \(N=m+2\) is the **upper half-filling particle sector** of the full \(2m+3\)-site network, placing the backbone current near its exclusion-limited maximum before strong tree occupation shifts particles away from the ring.

For a decoration with \(M\) side sites of depths \(d_1,\ldots,d_M\), define the elementary-symmetric polynomial \(e_i(q^{d_1},\ldots,q^{d_M})\), with \(e_0=1\), and set binomial coefficients with out-of-range lower arguments to zero. The conditional backbone occupation given \(k\) occupied backbone vertices is uniform on the \(\binom Lk\) configurations. All statements refer to the continuous-time stationary law, not transient mixing or an infinite-volume nonequilibrium limit.

## Proof

**1. Exact stationary weights and bond current.** Every configuration \(\eta\) with exactly \(N\) occupied sites has stationary weight proportional to

\[
w(\eta)=\prod_{\text{occupied side sites }v}q^{d(v)}.
\]

Indeed, tree-edge moves satisfy detailed balance because moving one particle outward raises the exponent by one and changes the forward-to-reverse rate by \(q\). On the backbone, the weight is constant under a hop. For every cyclic binary backbone configuration, the number of \(10\) bonds equals the number of \(01\) bonds, so the total backbone inflow and outflow balance even when \(h_f\ne h_b\). Summing the two balanced parts proves stationarity; irreducibility gives uniqueness.

Conditional on \(i\) particles in the side sites, \(k=N-i\) backbone particles occupy a uniformly chosen \(k\)-subset. Consequently

\[
\begin{aligned}
Z&=\sum_{i=0}^{M}\binom{L}{N-i}e_i(q^{d_1},\ldots,q^{d_M}),\\
J&=(h_f-h_b)\frac{K}{Z},\qquad
K=\sum_{i=0}^{M}\binom{L-2}{N-i-1}e_i(q^{d_1},\ldots,q^{d_M}).
\end{aligned}
\]

This reproduces the stationary structure and the two classes of backbone-current formulas in Ishiguro and Ando [1]. The new question is the **exact global ordering between the two network topologies** as \(q\) changes.

**2. Exact comparison at three side sites.** For the leaves and chain, respectively, the four elementary-symmetric functions are

\[
(e_0,e_1,e_2,e_3)_{\mathrm{leaf}}=(1,3q,3q^2,q^3),
\]
\[
(e_0,e_1,e_2,e_3)_{\mathrm{chain}}=
(1,q+q^2+q^3,q^3+q^4+q^5,q^6).
\]

Put \(L=2m\), \(N=m+2\), \(b=\binom{2m}{m}\), \(s=m(m-1)/[(m+1)(m+2)]\) and \(t=m/(m+1)\). Write \(Z_X=bz_X\) and \(K_X=bk_X/[L(L-1)]\). The four coefficients corresponding to side occupancy \(i=0,1,2,3\) are \((s,t,1,t)\) for \(z_X\), and \((s(m^2-4),t(m^2-1),m^2,t(m^2-1))\) for \(k_X\). In particular,

\[
\begin{aligned}
z_{\mathrm{leaf}}&=s+3tq+3q^2+tq^3,\\
z_{\mathrm{chain}}&=s+t(q+q^2+q^3)+(q^3+q^4+q^5)+tq^6,\\
k_{\mathrm{leaf}}&=s(m^2-4)+3t(m^2-1)q+3m^2q^2+t(m^2-1)q^3,\\
k_{\mathrm{chain}}&=s(m^2-4)+t(m^2-1)(q+q^2+q^3)\\
&\quad+m^2(q^3+q^4+q^5)+t(m^2-1)q^6.
\end{aligned}
\]

Direct polynomial multiplication and collection of like powers gives the **exact identity**

\[
k_{\mathrm{chain}}z_{\mathrm{leaf}}-k_{\mathrm{leaf}}z_{\mathrm{chain}}
=-\frac{m q(q-1)}{(m+1)^2(m+2)}F_m(q).
\]

Both partition functions are strictly positive. Hence the sign of the current difference is the opposite of the sign of \(F_m(q)\) whenever \(q>1\) and \(h_f>h_b\).

**3. Existence, uniqueness and orientation of the crossing.** For every \(m\ge2\), the coefficients of \(F_m\), in descending degree, have signs \((+,+,-,-,-,-,-)\). Descartes' rule of signs therefore gives **at most one** positive zero, counted with multiplicity. Moreover

\[
F_m(1)=-12(2m-1)(2m+1)<0,
\]

and \(F_m(q)\to+\infty\) as \(q\to\infty\). The intermediate value theorem supplies a positive zero greater than one, so it is unique and simple. The sign changes from negative to positive there, establishing all three current orderings.

**4. Increasing size and sharp large-size law.** Exactly group the polynomial as

\[
F_m(q)=m^2 A(q)+m B(q)+C(q),
\]

where

\[
\begin{aligned}
A(q)&=(q+1)^3(2q^3-5q^2+3q-6),\\
B(q)&=3(q-1)^2(q+1)^2(2q^2+q+2),\\
C(q)&=2q\left[6+q(q-1)(q+1)^2(2q-1)\right].
\end{aligned}
\]

For \(q>1\), both \(B(q)\) and \(C(q)\) are strictly positive, so \(A+B/m+C/m^2\) is strictly decreasing in \(m\) at each fixed \(q>1\). Since it has exactly one zero there and is negative to its left, its zero \(q_m\) increases strictly with \(m\).

The cubic \(H(q)=2q^3-5q^2+3q-6\) has precisely one root \(Q>1\): after setting \(q=1+u\), it becomes \(2u^3+u^2-u-6\), which has exactly one positive zero by Descartes' rule and the intermediate value theorem. In fact \(H(2)=-4\) and \(H(3)=12\), so \(Q\in(2,3)\), where \(H'(q)=6q^2-10q+3>0\). At \(Q\), \(A(Q)=0\) while \(B(Q),C(Q)>0\), so \(q_m<Q\). The locally uniform limit of \(F_m/m^2\) is \(A\), forcing \(q_m\uparrow Q\). Finally \(A'(Q)=(Q+1)^3(6Q^2-10Q+3)>0\), and Taylor expansion of \(0=A(q_m)+B(q_m)/m+C(q_m)/m^2\) yields

\[
Q-q_m=\frac{B(Q)}{mA'(Q)}+O(m^{-2}),
\]

which is the asserted expression for \(c\).

**5. Why three side sites are minimal.** For only two side sites let the depth multisets be \((1,2)\) and \((1,1)\), and define \(A_0=\binom LN\), \(B_0=\binom L{N-1}\), \(C_0=\binom L{N-2}\), and \(f(k)=k(L-k)/[L(L-1)]\) (its polynomial expression is used even outside the occupancy range, where the corresponding binomial coefficient vanishes). If the unnormalized current numerator is \(K\), the same stationary calculation gives

\[
\begin{aligned}
&K_{\mathrm{chain}}Z_{\mathrm{leaf}}-K_{\mathrm{leaf}}Z_{\mathrm{chain}}\\
&=-q(q-1)\bigl[A_0B_0(f(N)-f(N-1))\\
&\qquad+A_0C_0q(f(N)-f(N-2))\\
&\qquad+B_0C_0q^2(f(N-1)-f(N-2))\bigr].
\end{aligned}
\]

The consecutive differences have respective signs determined by \(L-2N+1\), \(L-2N+2\), and \(L-2N+3\). For odd \(L=2a+1\), all nonzero bracket terms are nonnegative for \(N\le a+1\) and nonpositive for \(N\ge a+2\). For even \(L=2a\), the same statement holds for \(N\le a\) and \(N\ge a+2\). At the sole intermediate value \(N=a+1\), one has \(A_0=C_0\) and the bracket equals \(A_0B_0(q^2-1)/[L(L-1)]>0\). In every nontrivial sector one inequality is strict. This proves the fixed two-site ordering and rules out a topology-induced crossing for smaller decorations.

## Verification

The included `verify.py` uses only the Python standard library. Running `python verify.py` completed **2,298** exact rational/polynomial/generator-balance checks, including: coefficient-by-coefficient verification of the displayed six-degree factorization for \(2\le m\le40\), current signs at five rational tree biases, the full two-site comparison for \(3\le L\le22\) and all nontrivial particle numbers, and stationary-master-equation balance by enumerating every fixed-particle configuration in selected seven- and nine-site systems. It also prints the numerically bisected values of five critical ratios. These finite checks are diagnostic; the quantifiers for all \(m\), all \(q>1\), and all allowed two-site occupancies are established by the proof above.

## Relationship to prior work

Ishiguro and Ando [1] derived the fixed-particle stationary Gibbs weights on an exclusion ring with attached trees and exact hypergeometric and mixed hypergeometric formulas for currents of multiple short trees and one long tree. Those weights, solvability, and the individual current formulas **are prior work**, and the present proof explicitly starts from them. Their comparison plots vary particle number for fixed hopping ratios. The present result instead fixes the particle number and compares **two distinct topologies as the same outward bias varies**, proving a unique order reversal for every even backbone length, a monotone exact threshold with a universal limit, and the minimal side-site count. These conclusions were not located in the inspected full text of [1].

Ishiguro and Sato [2] established the more general transition-decomposition construction of exact ASEP steady states, which covers the invariant measure as a prior structural result. It does not, from the accessible abstract, settle the specific topology-comparison inequalities. Earlier exclusion models on trees, including Mottishaw, Waclaw and Evans [3], have different boundary-driven and aggregate-hopping setups; their phase diagrams do not directly imply the fixed-number closed-ring comparison here. The current-ranking result is a consequence of explicit prior stationary measures **plus new all-parameter polynomial sign and minimality analysis**, not an independently new steady-state construction.

## Limitations

The result concerns fixed-particle finite rings, two explicitly defined branch topologies, common branch hopping-rate ratio \(q>1\), and positive backbone net bias. It makes no assertion about a fixed total hopping budget, disordered branch rates, open reservoirs, current fluctuations, spectral gaps, thermodynamic current nonanalyticity, or every possible side-tree topology. The limiting critical ratio as \(m\to\infty\) is a **limit of finite-system ordering thresholds**, not a claimed bulk phase transition. The general stationary measure and individual current expressions were already known. A broader unlocated comparative-statics theorem may entail the new ordering, so publication priority requires independent checking.

## References

[1] Y. Ishiguro and Y. Ando, “Asymmetric simple exclusion process with tree-like network branches,” arXiv:2603.09694v1 (first publicly posted 2026-03-10), https://arxiv.org/html/2603.09694 , especially Sections II–IV and equations (15), (20)–(21), (27)–(28), (31)–(32), (40)–(41).

[2] Y. Ishiguro and J. Sato, “Exact steady states in the asymmetric simple exclusion process beyond one dimension,” arXiv:2403.01934 (first publicly posted 2024-03-04), https://arxiv.org/abs/2403.01934 .

[3] P. Mottishaw, B. Waclaw and M. R. Evans, “An exclusion process on a tree with constant aggregate hopping rate,” *Journal of Physics A* **46** (2013), 405003, https://arxiv.org/abs/1306.0360 .
