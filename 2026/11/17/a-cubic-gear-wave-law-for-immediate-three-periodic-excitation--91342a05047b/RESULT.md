# A cubic gear-wave law for immediate three-periodic excitation

## Finding
Let \(G_n\), \(n\geq3\), be the gear graph obtained by subdividing every rim edge of the wheel with \(n\) rim vertices while leaving its spokes intact. Under synchronous three-state, threshold-one Greenberg–Hastings excitation, let \(P_n\) count labelled initial configurations of **least temporal period three**, including all three distinct temporal phases. Define integer sequences
\[
 a_0=3,\quad a_1=2,\quad a_2=8,\quad a_{k+3}=2a_{k+2}+2a_{k+1}+a_k,
\]
\[
 b_0=b_1=2,\qquad b_{k+2}=2b_{k+1}+b_k,
\qquad \omega_k=\begin{cases}2&3\mid k,\\-1&3\nmid k.\end{cases}
\]
Then, for **every** integer \(n\geq3\),
\[
 \boxed{P_n=3\bigl(a_n+\omega_n-(-1)^n-b_n\bigr).}
\]
In particular \(P_3,P_4,P_5,P_6,P_7,P_8=36,84,300,954,2940,8916\), and the number of distinct primitive three-cycle orbits is exactly \(P_n/3\). Let \(\lambda\) be the unique positive real root of \(z^3-2z^2-2z-1\), so \(\lambda=2.8311772072\ldots\). Then
\[
 P_n\sim3\lambda^n,\qquad
 \Pr_{X\,\mathrm{uniform}}(X\text{ has least period three})\sim(\lambda/9)^n.
\]
Thus the population of immediately recurrent three-step waves grows exponentially, but its proportion among the \(3^{2n+1}\) initial configurations vanishes exponentially. The claim concerns immediate period-three states, not other recurrent periods or eventual three-periodic attraction basins.

## Assumptions and scope
The \(2n+1\) labelled vertices are a hub \(h\), original rim sites \(u_i\), and edge-subdivision sites \(v_i\), with \(i\in\mathbb Z/n\mathbb Z\). The edges are exactly \(hu_i\), \(u_iv_i\), and \(v_iu_{i+1}\), with no loops or other edges. The synchronous update has states \(0\) (resting), \(1\) (excited), and \(2\) (refractory): a site in state \(1\) advances to \(2\), a site in state \(2\) advances to \(0\), and a site in state \(0\) advances to \(1\) if and only if at least one neighbor is in state \(1\), otherwise remaining \(0\). Sites and time phases are labelled. The graph is connected for all stated \(n\).

## Proof
**Step 1: Fully rotating characterization.** On any finite connected graph under this rule, if \(F^3(X)=X\) and \(X\) is not the all-zero state, then every vertex rotates its state by one modulo three at each update. Indeed, a site in state \(1\) or \(2\) on a three-periodic orbit must traverse \(1\to2\to0\to1\); a site that never does so must stay zero. A permanently resting site cannot be adjacent to a rotating site, since that neighbor is excited during one of the three phases. Connectivity eliminates the possibility of both types of vertices. Conversely, a coloring \(c\) rotates synchronously if and only if every vertex of color \(j\) has at least one neighbor of color \(j+1\pmod3\). This local condition is preserved under simultaneous increment. The only fixed state is all zero.

**Step 2: Nine-state cyclic transfer.** Fix the hub color to \(0\), using global color-rotation symmetry of the *set of fully rotating configurations*. Index nine states by ordered pairs \((u,v)\in\{0,1,2\}^2\), and define a \(9\times9\) integer matrix \(M\) with rows \((u,v)\) and columns \((u',v')\) by
\[
 M_{(u,v),(u',v')}=
 \mathbf1\{u=v+1\text{ or }u'=v+1\pmod3\}
 \mathbf1\{0=u'+1\text{ or }v=u'+1\text{ or }v'=u'+1\pmod3\}.
\]
The first condition provides the successor neighbor for \(v_i\), whose neighbors are \(u_i,u_{i+1}\); the second provides the successor neighbor for \(u_{i+1}\), whose neighbors are \(h,v_i,v_{i+1}\). A closed length-\(n\) walk of these pair states enforces every nonhub vertex condition exactly once. The hub condition requires at least one \(u_i=1\). Let \(N\) be obtained from \(M\) by setting every row with \(u=1\) to zero. The omitted closed walks are precisely those for which the hub lacks a successor-colored neighbor. Therefore
\[
 P_n=3\bigl(\operatorname{tr}(M^n)-\operatorname{tr}(N^n)\bigr).
\]
The factor three restores the three possible hub colors, not a quotient by temporal phase; each phase remains a separate configuration.

**Step 3: Characteristic polynomials and recurrence.** Direct exact expansion of the two explicitly defined nine-state matrices gives
\[
 \det(zI-M)=z^4(z^2+z+1)(z^3-2z^2-2z-1),
 \qquad \det(zI-N)=z^6(z+1)(z^2-2z-1).
\]
These factorizations can be verified independently using Newton's identities from the first nine integer power traces, as implemented in `verify_transfer.py`. For \(n\ge1\), the zero eigenvalues contribute nothing to a power trace. The cubic-root power sum is exactly \(a_n\), since its three roots have initial sums \(3,2,8\) and satisfy the displayed cubic. The pair of primitive cube roots of unity contributes \(\omega_n\). The two roots of \(z^2-2z-1\) have power sum \(b_n\), while \(-1\) contributes \((-1)^n\). Inserting these four contributions into the trace identity proves the formula for all \(n\ge3\).

**Step 4: Primitive orbits and asymptotic prevalence.** By Step 1 every nonzero state counted by \(P_n\) has primitive period three, so precisely three states belong to each temporal orbit. The dominant root of the cubic is positive and unique, by Descartes' rule of signs and positive-value comparison, and lies between \(2.8311\) and \(2.8312\). Its other two roots have modulus below one (a direct check from the cubic or an exact root bound). The positive root \(1+\sqrt2\) of the quadratic is strictly below \(\lambda\); all remaining eigenvalues also have smaller modulus. Thus \(P_n=3\lambda^n(1+o(1))\). Since \(G_n\) has \(2n+1\) vertices, division by \(3^{2n+1}\) gives the probability asymptotic.

## Verification
The standalone standard-library script `verify_transfer.py` reconstructs both integer matrices and uses exact Newton identities to check their characteristic polynomials, plus the trace-derived recurrence through \(n=50\). The independent C++17 program `verify_direct.cpp` constructs the original gear graph as adjacency lists, evolves all labelled ternary initial configurations three times, and tests true primitive periodicity, with no transfer-matrix or spectral computations. It examines every one of the \(2,187\), \(19,683\), \(177,147\), and \(1,594,323\) initial states for \(n=3,4,5,6\), respectively, finding \(36,84,300,954\) primitive period-three states, with the all-rest state the only fixed point. Executed outputs are captured in `verification_output.txt`. The infinite-family proof is the local transfer identity and exact characteristic-polynomial calculation, not an extrapolation from these finite tests.

## Relationship to prior work
Gravner, Lyu and Sivakoff (2016), Theorem 3, gives a general finite-graph synchronization/activity characterization through cycle integrals, while its Theorem 5 supplies a broad probability bound for eventual activity; neither theorem states an immediate least-period-three population formula on gear graphs. The published full-subdivision exact census (2026) concerns graphs obtained by subdividing **every** original edge and does not apply to \(G_n\), where all hub spokes remain unsubdivided and both hub and rim-original vertices have degree greater than two. The published open-ladder three-period census concerns a different boundary graph and yields a distinct cubic recurrence. The present statement makes an exact count for the naturally partially subdivided wheel (also called the gear or \(J_{2,n}\) graph), whose cubic root \(\lambda\) is not the open-ladder growth root \((3+\sqrt{17})/2\). The universal local fully-rotating criterion in Step 1 is background; the nine-state transfer, its factorization, the closed population law and the asymptotic are the claimed additions.

## Limitations
Only already-periodic least-period-three states are counted. This is not a complete attraction-basin census, a classification of larger primitive periods, or a claim that all other initial states become resting. Historic priority is based on the identified records and inspected full texts, not exhaustive worldwide coverage; an unindexed enumeration of successor-dominating three-colorings on gear graphs could overlap. No independent mathematical audit has been performed.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public arXiv preprint submitted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, original arXiv version submitted 2016-10-24; full text Sections 1–4, https://arxiv.org/html/1610.07320v1.
3. *Exact three-periodic excitation census on full graph subdivisions*, publicly accessible result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-three-periodic-excitation-census-on-full-graph-subdivision--3e82f66ce40c.
4. *Exact primitive-three wave census on open ladders*, publicly accessible result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-primitive-three-wave-census-on-open-ladders--c343292238f3.
5. E. W. Weisstein, *Gear Graph*, MathWorld, https://mathworld.wolfram.com/GearGraph.html (graph terminology only).
