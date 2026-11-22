# Single-edge detuning and the exact 104-set Petersen controllability census

## Finding
Let the ten-vertex Petersen graph have outer vertices \(0,1,2,3,4\), inner vertices \(5,6,7,8,9\), and edges \(\{i,i+1\}\) (outer indices modulo five), \(\{i,5+i\}\), and \(\{5+i,5+(i+2)\}\) (inner indices modulo five). Every edge has conductance one except \(\{0,1\}\), which has conductance \(t>0\). Write \(L(t)\) for the weighted combinatorial Laplacian. For each set \(S\subseteq\{0,\ldots,9\}\), independently actuate those coordinates in the linear system
\[
\dot x=-L(t)x+B_Sv,\qquad B_S=[e_j:j\in S].
\]

Define the controllability-set polynomial \(\mathcal C_t(z)=\sum_{S:\,(-L(t),B_S)\,\mathrm{controllable}}z^{|S|}\). The exact, globally exhaustive answer is
\[
\boxed{\mathcal C_t(z)=
\begin{cases}
162z^5+195z^6+120z^7+45z^8+10z^9+z^{10},&t=1,\\
104z^4+210z^5+203z^6+120z^7+45z^8+10z^9+z^{10},&t>0,\ t\ne1.
\end{cases}}
\]
In particular, the minimum number of independently controlled vertices drops sharply from five to four at any nontrivial positive single-edge detuning, and **exactly 104** four-vertex subsets are controllable for **every** \(t>0\) other than one. There are no further positive-parameter resonances.

An exact placement test does not require computing parameter-dependent eigenvectors. Let \(L_0=L(1)\), \(b=e_0-e_1\), and let \(U_2=E_2(L_0)\cap b^\perp\), the fixed four-dimensional eigenspace of eigenvalue two orthogonal to \(b\). Put \(T=\{0,1,2,4,5,6\}\). For every \(t>0\), \(t\ne1\),
\[
\boxed{(-L(t),B_S)\text{ is controllable}\ \Longleftrightarrow\
\operatorname{rank}\bigl(\operatorname{res}_S\!\mid_{U_2}\bigr)=4\ \text{and}\ S\cap T\ne\varnothing.}
\]
Here \(\operatorname{res}_S\) retains only the coordinates indexed by \(S\). This criterion applies to *all* subsets, not just minimum ones. The only four-vertex set satisfying the rank condition but failing the intersection condition is \(\{3,7,8,9\}\).

## Assumptions and scope
All ten labelled vertices and fifteen undirected edges are fixed as above, with all conductances exactly one except the single positive parameter \(t\). The Laplacian is the ordinary weighted symmetric Laplacian (not an adjacency matrix or normalized Laplacian). There is one independent real input per selected coordinate, unrestricted control signals, and exact full-state Kalman controllability at a fixed value of \(t\). No claim is made about practical control energy or numerical conditioning near \(t=1\), or about simultaneous control for uncertain \(t\) using a single open-loop signal.

## Proof
**1. Spectral decomposition of the unit Petersen Laplacian.** The ordinary Petersen adjacency eigenvalues are \(3\) once, \(1\) five times and \(-2\) four times. Equivalently, exact determinant expansion of its ten-by-ten Laplacian gives
\[
\det(\lambda I-L_0)=\lambda(\lambda-2)^5(\lambda-5)^4.
\]
Put \(b=e_0-e_1\). The orthogonal spectral projections onto the eigenvalues two and five are respectively
\[
P_2=\frac{L_0(5I-L_0)}6,\qquad P_5=\frac{L_0(L_0-2I)}{15}.
\]
Direct integer matrix multiplication yields \(P_0b=0\), and
\[
\begin{aligned}
a=P_2b&=\tfrac13(1,-1,-1,0,1,1,-1,0,0,0)^{\mathsf T},\\
c=P_5b&=\tfrac13(2,-2,1,0,-1,-1,1,0,0,0)^{\mathsf T}.
\end{aligned}
\]
Thus \(b=a+c\), \(a\perp c\), \(\|a\|^2=2/3\), \(\|c\|^2=4/3\), and the support of both \(a\) and \(c\) is precisely \(T\).

**2. Universal spectral factorization.** With \(\delta=t-1\),
\[
L(t)=L_0+\delta bb^{\mathsf T}.
\]
The four-dimensional space \(U_2=E_2(L_0)\cap b^\perp\) retains eigenvalue two, and the three-dimensional space \(U_5=E_5(L_0)\cap b^\perp\) retains eigenvalue five. The constant vector retains eigenvalue zero. The orthogonal complement is the span of \(a,c\). Using their orthogonal squared norms, the latter block has characteristic polynomial
\[
q_t(\lambda)=(\lambda-2)(\lambda-5)-\delta\left[\tfrac23(\lambda-5)+\tfrac43(\lambda-2)\right]
=\lambda^2-(2t+5)\lambda+(6t+4).
\]
Consequently
\[
\det(\lambda I-L(t))=\lambda(\lambda-2)^4(\lambda-5)^3q_t(\lambda).
\]
For \(t>0\), the two zeros of \(q_t\) are distinct because its discriminant is \(4t^2-4t+9>0\); neither zero is \(0\), since \(q_t(0)=6t+4>0\). For \(t\ne1\), they also avoid the retained eigenvalues, since \(q_t(2)=2(t-1)\) and \(q_t(5)=-4(t-1)\). The two new eigenvectors have nonzero projections on both \(a\) and \(c\), since the off-diagonal entry of the rank-one perturbation in their normalized basis is nonzero for \(\delta\ne0\).

**3. PBH criterion and the parameter-independent placement test.** For a real symmetric matrix, the Popov–Belevitch–Hautus criterion says that a coordinate set \(S\) controls the system if and only if restriction to \(S\) is injective on *each* eigenspace. The eigenspaces \(U_2\) and \(U_5\) must therefore both restrict injectively. For this finite graph, an exact minor computation shows that for every set \(S\), whenever \(\operatorname{rank}(U_2|_S)=4\), one also has \(\operatorname{rank}(U_5|_S)=3\). Both statements are exhaustive exact-rational assertions checked over all subsets by the supplied reproducible program, using the graph itself to construct these spaces.

It remains to check the two simple split eigenvectors. Suppose \(S\cap T=\varnothing\); then both \(a,c\) vanish on \(S\), so neither new eigenvector can be observed. Conversely suppose \(S\cap T\ne\varnothing\). If \(a|_S,c|_S\) are linearly independent, each nonzero vector in their span is observed. If they are dependent, the displayed coordinate vectors show that necessarily \(c|_S=2a|_S\) or \(c|_S=-a|_S\), with \(a|_S\ne0\). In the first case the unique invisible line is \(\operatorname{span}(c-2a)\); this is perpendicular to \(b\), and \(L(t)(c-2a)=5c-4a\), not a multiple of \(c-2a\). In the second case the invisible line is \(\operatorname{span}(a+c)=\operatorname{span}(b)\), but \(L(t)b=(2+2\delta)a+(5+2\delta)c\) is not a multiple of \(b\). Hence no eigenvector of the split block vanishes on \(S\), at any \(t>0\), \(t\ne1\). The constant eigenvector is visible whenever \(S\) is nonempty; the full-rank condition implies nonemptiness. This establishes the boxed criterion over the entire positive detuning range.

**4. Exhaustive exact finite census.** The parameter-independent criterion reduces the result to 1024 finite rational rank tests, *not* to sampling real parameters. A basis for the rank-four space \(U_2\) is given by the columns of the following explicit integer matrix (rows indexed zero through nine):
\[
M_2=\begin{pmatrix}
1&0&-1&-1\\
1&0&-1&-1\\
-1&0&0&0\\
-2&-1&1&1\\
-1&-1&0&1\\
1&1&0&-1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
\]
For each of the 1024 subsets \(S\), retain its rows and test \(\operatorname{rank}(M_2[S,:])=4\) exactly; then enforce \(S\cap T\ne\varnothing\). The counts by subset size are respectively \(0,0,0,0,104,210,203,120,45,10,1\). In particular, among all 210 four-subsets, exactly 105 have full rank in \(M_2\), and the unique one of these disjoint from \(T\) is \(\{3,7,8,9\}\). At \(t=1\), use the five-dimensional \(E_2(L_0)\) and four-dimensional \(E_5(L_0)\), checking simultaneous injectivity. The counts are \(0,0,0,0,0,162,195,120,45,10,1\). Every one of these assertions follows from exact rational elimination over a *complete finite list*. The script `checker.py` reconstructs all spaces independently from the fifteen edge incidences and repeats both exact enumerations. The coefficients yield the two generating polynomials in the finding.

**5. Optimal actuator numbers.** The maximum eigenspace dimensions are five at \(t=1\) and four at every nonunit positive \(t\), so the PBH lower bound excludes smaller coordinate input sets. The exact placement census explicitly supplies 162 admissible five-sets at \(t=1\) and 104 admissible four-sets at nonunit \(t\), proving both sharp minima and all optimizer counts.

## Verification
`checker.py` requires Python 3 standard library only and outputs `VERIFY_OK`. It reconstructs the graph and projections with exact `fractions.Fraction` arithmetic, derives the fixed eigenspaces by rational Gaussian elimination, enumerates all \(2^{10}=1024\) coordinate subsets, certifies the implication from the rank-four to the rank-three condition, checks the special dependent restriction ratios, and derives both full generating polynomials. As an independent implementation-level check, it tests Kalman ranks modulo the prime \(1000003\) for all 252 five-subsets at \(t=1\) and for all 210 four-subsets at each of \(t\in\{1/2,2,3\}\). Modular full rank witnesses full rational rank, while observed modular deficiency alone is *not* used as proof of real deficiency; the PBH and exact rational proof above handles noncontrollability. The checks are finite because the graph has ten vertices; the assertions for every real \(t>0\) use the preceding spectral decomposition, not a numerical grid of parameter values.

## Relationship to prior work
Yuan and collaborators [1] give the general exact controllability theorem using maximum eigenspace multiplicity; their paper supplies the lower-bound mechanism, not this labelled single-edge Petersen placement classification or its 104-set, parameter-stable census. Monshizadeh, Zhang and Camlibel [2] characterize control for *all matrices in a graph's qualitative class* through zero forcing; that stronger family-wide quantifier does not identify exactly which coordinate input sets control this particular one-parameter Laplacian. Zhang, Camlibel and Cao [3] develop controllable-subspace bounds for distance-regular diffusion networks, but their inspected abstract focuses on single leaders and general multiple-leader conditions, not this weighted one-defect complete census.

A separate published theorem [4] constructs minimum consecutive outer actuators on **unweighted** generalized Petersen graphs, but expressly does not classify all minimum placements and does not allow a single exceptional edge conductance. Another published result [5] determines the full actuator polynomial for a **complete bipartite graph** with one exceptional link; its graph, spectral multiplicities, and polynomial are different. Neither statement implies the 104 Petersen sets merely by renaming parameters. The elementary spectral projectors, rank-one update, and PBH criterion used in the proof are classical tools and are not claimed new. The contribution is the exact all-subsets, all-positive-detunings classification on the canonical Petersen network.

## Limitations
This is an exact finite-network theorem. It does not extend without proof to other generalized Petersen graphs, multiple changed edges, independent edge uncertainties, nonlinear dynamics, finite-precision control or minimum-energy objectives. The loss of robustness as \(t\to1\) may make four-input controls arbitrarily ill-conditioned even though they remain algebraically controllable; no quantitative energy bound is proved. Publication priority remains provisional because not all older specialized graph-control literature, including one 2014 paper with accessible abstract but not full text [6], could be exhaustively inspected. No independent mathematical audit has been performed.

## References
[1] Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, *Exact controllability of complex networks*, first public 12 September 2013, *Nature Communications* 4, 2447. https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/

[2] N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868, first public 19 March 2014. https://arxiv.org/abs/1403.4868

[3] S. Zhang, M. K. Camlibel and M. Cao, *Controllability of diffusively-coupled multi-agent systems with general and distance regular coupling topologies*, CDC-ECC (2011), DOI:10.1109/CDC.2011.6160658. https://doi.org/10.1109/CDC.2011.6160658

[4] *Multiplicity-optimal consecutive outer actuators on every generalized Petersen graph* (published 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-multiplicity-optimal-consecutive-outer-actuators-on-every-genera--5e26f62694e6

[5] *Exact actuator-set polynomials for a single-link defect in complete bipartite networks* (published 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-actuator-set-polynomials-for-a-single-link-defect-in-compl--30587e524e61

[6] A. Farrugia and I. Sciriha, *Controllability of undirected graphs*, *Linear Algebra and its Applications* 454 (2014), 138–157. https://www.um.edu.mt/library/oar/handle/123456789/28166
