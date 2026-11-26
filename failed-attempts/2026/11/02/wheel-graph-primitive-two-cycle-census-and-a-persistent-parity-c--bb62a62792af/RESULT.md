# Wheel-graph primitive two-cycle census and a persistent parity correction

## Finding
Let \(W_n=K_1\vee C_n\) be the labelled wheel with one hub and \(n\ge3\) rim vertices in cyclic order. For ordinary synchronous parallel chip-firing, let \(N_n\) be the number of distinct primitive two-cycle orbits of nonnegative integer chip configurations. These are actual two-state orbits, not merely firing-pattern orbits. Then the orbit-count polynomial indexed by \(k\), the number of rim vertices firing during the unique phase when the hub waits, is
\[
B_n(z)=z\frac{d}{dz}\operatorname{tr}(T(z)^n),\qquad
T(z)=\begin{pmatrix}0&1&0&0\\0&0&3z&2z\\1&2&0&0\\0&0&2z&z\end{pmatrix}.
\]
In particular, \(N_n=B_n(1)=n a_n\), where
\[
a_3=20,\quad a_4=69,\quad a_5=225,\qquad
a_n=2a_{n-1}+4a_{n-2}+a_{n-3}\quad(n\ge6).
\]
Equivalently, setting \(\lambda_\pm=(3\pm\sqrt{13})/2\), the count is
\[
\boxed{N_n=n\left[\left(\frac23-\frac{\sqrt{13}}{39}\right)\lambda_+^n+\left(\frac23+\frac{\sqrt{13}}{39}\right)\lambda_-^n+\frac23(-1)^n\right].}
\]
Thus
\[
N_n\sim\left(\frac23-\frac{\sqrt{13}}{39}\right)n\lambda_+^n,
\]
with an exact alternating \(\frac{2n}{3}(-1)^n\) contribution and an exponentially decaying third contribution after division by \(n\). The first totals, for \(n=3,4,5,6\), are \(60,276,1125,4476\).

## Assumptions and scope
Each vertex \(v\) has an integer chip height \(c(v)\ge0\) and degree \(d(v)>0\). At each integer time every vertex with \(c(v)\ge d(v)\) fires once, sending one chip to each neighbor simultaneously. The graph is simple, connected, with labelled hub and rim positions, and \(n\ge3\). Orbits are distinct configurations modulo temporal rotation only; spatial graph automorphisms are **not** quotiented. No fixed points or periods other than primitive two are included in \(N_n\). The polynomial variable \(z\) records the number \(k\in\{0,\ldots,n\}\) of rim vertices firing when the hub does not fire. The count has no restriction on total energy, but every primitive two-cycle automatically lies in the finite height box \(0\le c(v)\le2d(v)-1\).

## Proof
**1. Two-step firing structure.** Write \(f_t(v)\in\{0,1\}\) for the firing indicator. The update is \(c_{t+1}=c_t-L f_t\), where \(L\) is the graph Laplacian. If \(c_2=c_0\), then \(L(f_0+f_1)=0\); connectivity makes \(f_0(v)+f_1(v)\) independent of \(v\). The common value is either \(0,1,2\). Values \(0\) and \(2\) give an immediately fixed state because respectively nobody or everybody fires at both updates. Consequently a primitive two-cycle has exactly one firing time per vertex, with \(f_1=1-f_0\).

**2. Exact height intervals.** Let \(S=\{v:f_0(v)=1\}\), and let \(k_v\) be the number of neighbors of \(v\) across the cut \((S,V\setminus S)\). At a firing vertex \(v\in S\), the first update subtracts precisely \(k_v\) chips: \(c_1(v)=c_0(v)-k_v\). The requirements that \(v\) fire at time zero and wait at time one are exactly
\[
d(v)\le c_0(v)\le d(v)+k_v-1.
\]
At \(v\notin S\), the first update adds \(k_v\) chips, and the opposite requirements are exactly
\[
d(v)-k_v\le c_0(v)\le d(v)-1.
\]
Each interval has \(k_v\) nonnegative integer choices; an interval is empty if \(k_v=0\). Conversely, choosing independently any heights in these intervals yields the prescribed complementary firing sets. The second update returns exactly to \(c_0\), because over two updates all vertices fire once, whence the net Laplacian increment is zero. Every such state is genuinely primitive two because \(S\) and its complement must differ. Thus one temporal orbit corresponds to two complementary phase descriptions and its number of states with any prescribed first-phase cut is \(\prod_v k_v\).

**3. Fix the hub phase.** In every primitive two-cycle there is exactly one state in which the hub waits. Encode the rim firing indicators in that state by the cyclic binary word \(b_1\cdots b_n\). The hub has \(k_h=\sum_i b_i\) cut neighbors; rim vertex \(i\) has
\[
k_i=b_i+\mathbf 1_{b_{i-1}\ne b_i}+\mathbf 1_{b_{i+1}\ne b_i},
\]
with cyclic indices. The exact number of orbits with this rim word is
\[
\left(\sum_i b_i\right)\prod_{i=1}^n\left(b_i+\mathbf 1_{b_{i-1}\ne b_i}+\mathbf 1_{b_{i+1}\ne b_i}\right).
\]
This is a complete bijective weighted enumeration, not a limiting or numerical approximation.

**4. Four-state transfer.** Index pairs \((0,0),(0,1),(1,0),(1,1)\). Allow a transition from \((a,b)\) to \((b,c)\), of weight \(z^b[b+\mathbf 1_{a\ne b}+\mathbf 1_{c\ne b}]\). This is precisely the displayed \(T(z)\). Its closed length-\(n\) walks correspond bijectively to labelled cyclic rim words, so \(\operatorname{tr}T(z)^n\) enumerates \(z^{\sum b_i}\prod k_i\). Applying \(z\,d/dz\) supplies the hub factor \(\sum b_i\). Therefore \(B_n(z)\) is exactly the stated orbit-count polynomial.

**5. Exact rational generating function.** Direct expansion of the four-by-four determinant gives
\[
P(t,z)=\det(I-tT(z))=1-zt-6zt^2-(3z+2z^2)t^3-z^2t^4.
\]
The formal power-series identity \(-\log\det(I-tT)=\sum_{n\ge1}t^n\operatorname{tr}(T^n)/n\) now yields
\[
\sum_{n\ge1}\frac{B_n(1)}n t^n
=-\left.\frac{zP_z(t,z)}{P(t,z)}\right|_{z=1}
=\frac{t(1+5t+2t^2)}{(1+t)(1-3t-t^2)}.
\]
Although the graph definition uses \(n\ge3\), coefficients for larger \(n\) are unaffected by the formal values at one and two. Extracting coefficients gives \(a_3=20,a_4=69,a_5=225\) and the recurrence above. Partial fractions at \(t=-1\) and at the two roots of \(1-3t-t^2\) give the displayed closed form. Since \(|\lambda_-|<1<\lambda_+\), its asymptotic follows. Every step applies to all \(n\ge3\).

## Verification
Two independent executable checks accompany this result. `wheel_period_two_verify.py` enumerates every configuration in the necessary finite height box \(0\le c(v)<2d(v)\) for \(3\le n\le6\), tests the actual two-step update, divides the count of primitive states by two, and compares with a separately coded cut enumeration and the recurrence. It also compares the cut count with an independent cyclic-word expression for \(7\le n\le15\). `wheel_transfer_symbolic.py` checks the symbolic determinant, rational generating function and polynomial coefficients using SymPy. Both programs were executed from their packaged source paths and passed. Finite checks are corroboration; the all-\(n\) proof is Steps 1–5.

## Relationship to prior work
Jiang's 2010 preprint establishes general equal-firing and height-confinement principles and treats exact possible periods on complete bipartite and multipartite graphs. Jiang, Scully and Zhang's 2012 preprint proves a universal obstruction to clumpy periodic firing patterns and develops motor constructions. These results supply general background for two-cycle structure. They do not state or directly evaluate the labelled wheel's exact primitive-two orbit polynomial, third-order recurrence, growth constant or alternating term. The cut-height intervals in Step 2 are elementary and not independently claimed as novel; the evaluated wheel enumeration is the asserted contribution. Existing local counts on cycles, ladders, cliques, book graphs and clique-windmills concern different graph families and do not imply the wheel recurrence through an identified graph equivalence. The case \(n=3\) coincides with the complete graph on four vertices and is included as a boundary check, not offered as a separate finding.

## Limitations
No claim is made about three- or higher-period orbits, all periodic states, transient lengths, basins of attraction or fixed-energy conditioned probabilities. The result treats ordinary synchronous chip-firing on simple undirected wheels, not sink sandpiles or directed or asynchronous variants. The originality comparison is based on inspected primary preprints and searched mathematical records; an unindexed historical equivalent is possible. Program tests end at the stated finite sizes and are not infinite proofs. Independent external validation has not been performed.

## References
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first public version 4 March 2010), especially Section 2 on conserved firing counts and confined positions.
- T.-Y. Jiang, Z. Scully, Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (first public version 29 November 2012), especially Sections 6–7 on nonclumpy periodic patterns.
- J. Bitar and E. Goles, *Parallel Chip Firing Games on Graphs*, Theoretical Computer Science **92** (1992), 291–300, DOI:10.1016/0304-3975(92)90316-8 (historical background; full text not inspected here).
