# Exact primitive two-cycle chip-mass spectrum on wheel graphs

## Finding

Let \(W_m=K_1\vee C_m\), where \(m\ge3\), with a distinguished hub and a labelled simple rim cycle of length \(m\). Write \(F\) for synchronous parallel chip-firing: a vertex with at least its degree in chips sends one chip to each neighbour, simultaneously with every other firing vertex. Write \(|x|\) for the total number of chips of a configuration \(x\). Define
\[
H_m(z)=\sum_{\substack{x\in\mathbb Z_{\ge0}^{m+1}\\F^2x=x,\ Fx\ne x}}z^{|x|}.
\]
Thus the polynomial counts **initially primitive-two configurations**, not transient configurations later attracted to two-cycles.

Use \([j]_z=\sum_{h=0}^{j-1}z^h\) for integers \(j\ge1\), and \([0]_z=0\). Define the four-state matrix \(T(z,y)\) with rows and columns indexed by \((p,c)\in\{0,1\}^2\). Its entries are zero unless the transition is \((p,c)\to(c,e)\), in which case its weight is
\[
T(z,y)_{(p,c),(c,e)}=y^{1-c}\begin{cases}
z^3[2-p-e]_z,&c=1,\\
z^{2-p-e}[1+p+e]_z,&c=0.
\end{cases}
\]
The exact chip-mass enumerator is
\[
\boxed{H_m(z)=\frac{2z^m}{1-z}\left(\operatorname{tr}(T(z,1)^m)-\operatorname{tr}(T(z,z)^m)\right).}
\]
The quotient cancels to a nonnegative-integer polynomial. Its **exact integer support** is
\[
\boxed{[3m-\lfloor m/2\rfloor,\;4m+\lfloor m/2\rfloor-1]\cap\mathbb Z.}
\]
At **each** endpoint the coefficient is \(4\) for even \(m\), and \(2m\) for odd \(m\). Moreover
\[
\boxed{H_m(z)=z^{7m-1}H_m(z^{-1}).}
\]
For the unweighted count, the matrix at \(z=1\), indexed in the order \((0,0),(0,1),(1,0),(1,1)\), is
\[
T(1,y)=\begin{pmatrix}y&2y&0&0\\0&0&2&1\\2y&3y&0&0\\0&0&1&0\end{pmatrix}.
\]
Consequently
\[
H_m(1)=2\left.\frac{\partial}{\partial y}\operatorname{tr}(T(1,y)^m)\right|_{y=1},
\]
and the number of distinct temporal two-cycle orbits is \(H_m(1)/2\). As an optional closed recurrence encoding, the ordinary generating function of these total counts is
\[
\sum_{m\ge3}H_m(1)t^m=
\frac{-2t(3t^4+6t^3-10t-1)}{(1+t)^2(1-3t-t^2)^2}-2t-28t^2.
\]
The first totals, for rim lengths \(m=3,4,5,6\), are \(120,552,2250,8952\).

## Assumptions and scope

All rim vertices are distinguished by their labels. The edges comprise the simple cycle \(C_m\) and every spoke to the hub; hence the hub degree is \(m\), every rim degree is three, and there are \(2m\) edges. Chips are nonnegative integers with no a priori global mass bound. The update threshold equals the graph degree, and no sinks, dissipation, stochastic redistribution, or asynchronous moves are present. The only counted states satisfy \(F^2x=x\) but \(Fx\ne x\). The variable \(z\) is a formal weight for conserved total chip count. All formulas hold for every integer \(m\ge3\).

## Proof

**1. Alternating firing phases.** If a connected graph returns after two updates, the two-step number of firings \(u_v\in\{0,1,2\}\) obeys \(\sum_{w\sim v}(u_w-u_v)=0\) at each vertex, because the chip count returns to its original value. The graph Laplacian kernel on a connected graph consists of constants, so all \(u_v\) are equal. If the common number is zero or two, respectively every vertex waits or every vertex fires at both steps; the configuration is fixed from the outset. In a primitive two-cycle the common number therefore equals one, and each vertex reverses its firing status after one step. Conversely, if every vertex fires in exactly one of two steps, the two-step chip changes sum to zero and the configuration returns, with two distinct states.

**2. Necessary and sufficient local intervals.** Partition the vertices into those firing at time zero (phase A) and those waiting (phase B). Write \(a_v\) for the number of neighbours of \(v\) in phase A, and \(d_v\) for its degree. A vertex in phase A must have
\[
d_v\le x_v\le 2d_v-a_v-1,
\]
while a vertex in phase B must have
\[
d_v-a_v\le x_v\le d_v-1.
\]
These follow by applying the two opposite threshold tests to \(x_v\) and \(x_v'=x_v+a_v-d_v\) (phase A) or \(x_v'=x_v+a_v\) (phase B). Conversely every choice inside all these intervals gives the prescribed opposite firing pattern after one step, and hence a primitive two-cycle. No cases are omitted.

**3. Wheel phase words.** First fix the hub in phase A. Denote by \(w_i=1\) a rim vertex in phase A and \(w_i=0\) a rim vertex in phase B, with cyclic indices; let \(b=\#\{i:w_i=0\}\). The hub requires \(b\ge1\), and has the interval \([m,m+b-1]\). For a rim triple \((p,c,e)=(w_{i-1},w_i,w_{i+1})\), the interval is
\[
\begin{cases}
[3,\,3+(2-p-e)-1],&c=1,\\
[2-p-e,\,2],&c=0.
\end{cases}
\]
An interval is empty precisely when a phase-A rim vertex has two phase-A rim neighbours, that is, when the cyclic word contains \(111\). Every other word with \(b\ge1\) is feasible. Its generating polynomial is the product of the hub interval factor \(z^m[b]_z\) and all rim interval factors appearing in the definition of \(T\).

Each initially primitive two-cycle has exactly one of its states with the hub firing; the other state has its hub waiting. The one-step map is a mass-preserving bijection between these two sets. Thus the full polynomial is twice the generating polynomial for hub-A states.

**4. Transfer polynomial.** A closed walk of length \(m\) in the pair-state graph \((p,c)\to(c,e)\) corresponds bijectively to a labelled cyclic binary phase word. The entry weight multiplies the chip-interval polynomial for the center rim vertex and the marker \(y\) if the center belongs to phase B. Hence \(\operatorname{tr}(T(z,y)^m)\) is exactly the rim interval sum weighted by \(y^b\). Since \([b]_z=(1-z^b)/(1-z)\), the difference of traces at \(y=1\) and \(y=z\), multiplied by \(2z^m/(1-z)\), proves the displayed polynomial identity. Terms with \(b=0\) cancel, and forbidden words have zero local weight.

**5. Extremal mass and no gaps.** In a feasible word, let \(a\) be its number of phase-A rim vertices, let \(e_{AA}\) and \(e_{BB}\) be its numbers of A-A and B-B rim edges, and let \(r\) count its isolated A-runs. Every A-run has length at most two, so \(a-2e_{AA}=r\). Since the rim is a cycle, \(e_{BB}-e_{AA}=b-a\). Adding the lower endpoints of the hub and rim intervals yields
\[
L=m+3a+2e_{BB}=3m-r.
\]
Adding all upper endpoints yields \(U=4m+r-1\); equivalently, the total lengths of the independent chip intervals minus the number of vertices equal \(m+2r-1\). Products of intervals of consecutive integers realize every integer chip mass in \([L,U]\). Since each isolated A-run needs a distinct separating B-vertex, \(0\le r\le\lfloor m/2\rfloor\), and the upper value is attained by alternating A and B with one extra B if \(m\) is odd. These per-word intervals are nested as \(r\) increases, so the union is exactly the asserted integer band, with no omissions.

At the minimal chip mass, every vertex is at its unique lower endpoint and a phase word must have \(r=\lfloor m/2\rfloor\). For even \(m\), exactly two alternating labelled rim words maximize \(r\); for odd \(m\), exactly \(m\) rotations of the word with isolated A's and exactly one doubled B-gap maximize it. The bijection between hub-A and hub-B states doubles these counts to \(4\) and \(2m\), respectively. The same conclusion holds at maximal mass by the interval symmetry in the next step.

**6. Reciprocal symmetry.** For each fixed feasible phase word, every vertex contributes an interval of consecutive chip counts. The product of these interval polynomials is palindromic between its minimum and maximum total masses. As \(L+U=7m-1\), the center of this palindrome is independent of the word. Summing over words and doubling preserves \(H_m(z)=z^{7m-1}H_m(z^{-1})\). This also follows from the usual confined-state chip complementation, but does not require it.

**7. Total-count generating function.** At \(z=1\) the hub interval contributes its length \(b\), so differentiating the marker \(y^b\) proves \(H_m(1)=2\partial_y\operatorname{tr}(T(1,y)^m)|_{y=1}\). Direct calculation gives
\[
\det(\lambda I-T(1,y))=\lambda^4-y\lambda^3-6y\lambda^2-(2y^2+3y)\lambda-y^2.
\]
Using \(\sum_{m\ge1}\operatorname{tr}(T^m)t^m=-t\partial_t\log\det(I-tT)\), differentiating in \(y\) and evaluating at one yields the stated rational generating function, after subtracting the formal \(m=1,2\) terms \(2t+28t^2\). No graph interpretation is asserted for those two auxiliary terms.

## Verification

The standalone `check_direct.py` exhaustively iterates every chip vector with \(0\le x_v\le2d_v-1\), for wheel rim lengths \(3\) through \(6\), using the original nonlinear firing rule. It tests \(F^2x=x\ne Fx\) directly and compares its full chip-mass histogram against an independently constructed phase-word polynomial. This covers exactly \(649296\) state vectors and gives the totals \(120,552,2250,8952\). All period-two vectors must lie in these boxes by Step 2, so these finite-graph checks are exhaustive for their stated sizes.

The standalone `check_transfer.py` independently computes the polynomial trace difference with a four-state polynomial-valued matrix and compares it to direct cyclic-word multiplication, for every rim length from \(3\) through \(12\). It checks all coefficients, exact support, endpoint multiplicities, palindromicity, and total counts. Both source files and their captured outputs are included. These computations corroborate the proof; checking finitely many sizes does not prove the unrestricted assertions. The unrestricted claims follow from Steps 1–7.

## Relationship to prior work

Bitar and Goles established the parallel chip-firing model and tree period restrictions. Jiang's general firing-count and chip-complement results supply qualitative structure, while Jiang, Scully and Zhang develop firing-pattern constraints. Dall'Asta analysed the cycle (one-dimensional ring) rather than the wheel. Selig's wheel graph enumeration concerns the *sink-based Abelian and stochastic sandpile* recurrence sets, which are different state spaces and dynamics; the fact that both use wheel graphs does not imply an enumeration here. The present object is the complete **mass-graded primitive-two state census of the undissipated parallel process on a wheel**, with a sharp parity-sensitive support and endpoint census. No claim is made that the general equal-firing-count criterion or the ungauged two-cycle cut enumeration is new.

## Limitations

The theorem concerns only states already on primitive two-cycles, not transients, attracting basins, fixed points, or periodic orbits of other lengths. The cyclic rim is simple and has length at least three. The transfer formula requires no numeric evaluation at \(z=1\) before cancelling \(1-z\). An earlier unindexed exact wheel enumeration remains a possible priority limitation; the accessible full texts considered here do not provide the specific polynomial and endpoints. The full text of Bitar and Goles (1992) was not available through the searched open routes, so that historical comparison rests on its abstract and citations rather than a full-text exclusion.

## References

1. J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science **92** (1992), 291–300, doi:10.1016/0304-3975(92)90316-8. Publication listed as 1992-01-20.
2. L. Dall'Asta, *Exact solution of the one-dimensional deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0601267, first submitted 2006-01-12; Phys. Rev. Lett. **96** (2006), 058003.
3. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, first submitted 2010-03-04; especially Section 2.
4. T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786, first submitted 2012-11-29; SIAM J. Discrete Math. **29** (2015), 615–630.
5. T. Selig, *Combinatorial aspects of sandpile models on wheel and fan graphs*, arXiv:2202.06487, first submitted 2022-02-14, especially Sections 2–3 (dissipative sandpile recurrence, not this parallel model).
