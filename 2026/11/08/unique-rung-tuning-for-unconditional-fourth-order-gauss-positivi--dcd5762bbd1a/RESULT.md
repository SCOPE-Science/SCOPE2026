# Unique rung tuning for unconditional fourth-order Gauss positivity on the six-vertex ladder

## Finding
Let \(L\) be the weighted combinatorial Laplacian of the six-vertex ladder with two parallel three-vertex rails, identical rail-edge conductance \(a>0\), and three positive rung conductances \(b_1,b_2,b_3\). The completed fourth-order two-stage Gauss–Legendre heat step is
\[
T(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1},\qquad h\ge0.
\]
Then \(T(h)\) is entrywise nonnegative for **every** real \(h\ge0\) if and only if
\[
(b_1,b_2,b_3)=a\left(\frac12,\frac74,\frac12\right).
\]
At this unique tuning all entries of \(T(h)\) are strictly positive for every finite \(h>0\). At any other strictly positive rung triple there is an off-diagonal entry that is strictly negative for all sufficiently large \(h\). With unit rails and unit rungs, the entry joining the first pair of rail vertices at \(h=8\) is exactly \(-1471112/79673503\).

## Assumptions and scope
Vertices are ordered \((1,0),(1,1),(2,0),(2,1),(3,0),(3,1)\). Each of the four rail edges \((i,\sigma)\!\sim\!(i+1,\sigma)\), \(i=1,2\), \(\sigma=0,1\), has conductance \(a\); the rung \((i,0)\!\sim\!(i,1)\) has conductance \(b_i\). All conductances are strictly positive. The Laplacian has diagonal weighted degrees and off-diagonal negative conductances. Positivity means entrywise nonnegativity of the completed update matrix, for all initial nonnegative data, rather than stage positivity or a general method-wide SSP statement. Scale time by \(a\), so the proof takes \(a=1\), \(r_i=b_i/a\) and \(h\) replaced by \(ah\).

## Proof
**1. Laplacian and asymptotic necessity.** Let
\[
P=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},\quad
M=P+2\operatorname{diag}(r_1,r_2,r_3),\quad G=M^{-1}.
\]
The lane-symmetric and lane-antisymmetric unitary change of basis block-diagonalizes the six-vertex Laplacian into \(P\) and \(M\). The latter is a strictly positive definite irreducible symmetric \(M\)-matrix, hence every entry of \(G\) is strictly positive. The Moore–Penrose inverse satisfies
\[
L^+_{(i,\sigma),(j,\tau)}=\tfrac12\left(P^+_{ij}+(-1)^{\sigma-\tau}G_{ij}\right),\qquad
P^+=\frac19\begin{pmatrix}5&-1&-4\\-1&2&-1\\-4&-1&5\end{pmatrix}.
\]
For \(F(x)=(x^2-6x+12)/(x^2+6x+12)\), the spectral theorem gives \(F(hL)=I-12L^+/h+O(h^{-2})\) in off-diagonal entries as \(h\to\infty\). Therefore the assumed all-step entrywise nonnegativity implies \(L^+_{uv}\le0\) for all \(u\ne v\). Choosing both ends of rung 1 and rung 3, both ends of rung 2, and neighboring same-lane pairs yields
\[
G_{11}\ge5/9,\quad G_{33}\ge5/9,\quad G_{22}\ge2/9,
\qquad 0<G_{12}\le1/9,\quad0<G_{23}\le1/9.
\]
From \(MG=I\), its first-row, first-column and first-row, second-column identities are
\[
1=(1+2r_1)G_{11}-G_{12},\qquad
G_{22}=(1+2r_1)G_{12}.
\]
The first, using \(G_{11}\ge5/9\) and \(G_{12}\le1/9\), gives \(1+2r_1\le2\); the second, using \(G_{22}\ge2/9\) and \(G_{12}\le1/9\), gives \(1+2r_1\ge2\). Hence \(r_1=1/2\), with all the used inequalities equalities, so \(G_{11}=5/9\), \(G_{12}=1/9\), \(G_{22}=2/9\). Reflecting the argument at the last row gives \(r_3=1/2\), \(G_{33}=5/9\), \(G_{23}=1/9\). Finally the middle diagonal identity \(-G_{12}+(2+2r_2)G_{22}-G_{23}=1\) forces \(r_2=7/4\). This proves **global uniqueness of any potentially all-step-positive rung triple**, without presuming its reflection symmetry.

**2. Exact sufficiency certificate.** At the forced triple, \(M=\begin{psmallmatrix}2&-1&0\\-1&11/2&-1\\0&-1&2\end{psmallmatrix}\), with eigenvalues \(3/2,2,6\), whereas \(P\) has eigenvalues \(0,1,3\). Writing spectral projectors as
\[
\begin{aligned}
P_0&=J/3,\qquad P_1=\tfrac12\begin{pmatrix}1&0&-1\\0&0&0\\-1&0&1\end{pmatrix},\quad
P_3=\tfrac16\begin{pmatrix}1&-2&1\\-2&4&-2\\1&-2&1\end{pmatrix},\\
Q_{3/2}&=\tfrac19\begin{pmatrix}4&2&4\\2&1&2\\4&2&4\end{pmatrix},\quad
Q_{2}=P_1,\quad
Q_{6}=\tfrac1{18}\begin{pmatrix}1&-4&1\\-4&16&-4\\1&-4&1\end{pmatrix},
\end{aligned}
\]
set \(A=P_0+F(h)P_1+F(3h)P_3\), \(B=F(3h/2)Q_{3/2}+F(2h)Q_2+F(6h)Q_6\). Then
\[
T(h)_{(i,\sigma),(j,\tau)}=\frac{A_{ij}+(-1)^{\sigma-\tau}B_{ij}}2.
\]
A strictly positive common denominator on \(h\ge0\) is
\[
H(h)=(h^2+6h+12)(3h^2+6h+4)(3h^2+12h+16)(h^2+3h+3)(3h^2+3h+1).
\]
The six orbit representatives of the 15 off-diagonal entries are indexed by zero-based vertex pairs in the ordering above. For each representative the polynomial \(H(h)T_{uv}(h)\) is \(h^k\sum_{j=0}^{s}c_jh^j\), with all coefficients given *exactly* (ascending order):

| Pair | \(k\) | \((c_0,\ldots,c_s)\) |
|---|---:|---|
| \((0,1)\) | 1 | \((1152,6048,14472,19440,15478,7188,1812,189)\) |
| \((2,3)\) | 1 | \((4032,12096,14496,9144,3208,600,48)\) |
| \((0,2)\) | 1 | \((2304,9504,17448,17460,10234,3516,660,54)\) |
| \((0,3)\) | 2 | \((2592,10152,16308,14490,7740,2496,450,36)\) |
| \((0,4)\) | 2 | \((1152,5184,10044,10716,6840,2685,612,63)\) |
| \((0,5)\) | 3 | \((1056,4572,7540,6432,3027,756,81)\) |

All coefficients are strictly positive. The identities are exactly reproducible using the bundled symbolic verifier, which checks every off-diagonal pair. Hence every off-diagonal entry is strictly positive for all \(h>0\). Each diagonal entry is a sum of orthogonal-projector diagonal weights times strictly positive factors \(F(\lambda h)\), since \(F(x)>0\) for \(x\ge0\) because its numerator equals \((x-3)^2+3\). Thus the diagonal entries are also strictly positive for \(h>0\), and \(T(0)=I\).

**3. Sign failure off tuning.** If a different positive rung triple had no off-diagonal positive entry of \(L^+\), it would satisfy all five necessary inequalities and the preceding uniqueness argument would force the tuned triple, a contradiction. Thus for every untuned triple some \(L^+_{uv}>0\), giving \(T_{uv}(h)<0\) for all sufficiently large finite \(h\) by its leading asymptotic term. This completes the proof.

## Verification
The standalone `verify.py` uses exact SymPy integer and rational arithmetic. It constructs the scaled blocks, their Green inverse, each spectral projector and all 15 off-diagonal update entries. It checks that the entries coincide with the six listed nonnegative-coefficient certificates, directly inverts four six-by-six rational step matrices, and computes the unweighted-ladder negative witness. Run `python3 verify.py` with SymPy installed. The proof of the unbounded timestep assertion uses symbolic polynomial identities and a rigorous asymptotic sign argument; finite test timesteps alone would be insufficient.

## Relationship to prior work
Wade and coauthors (2004) study positivity-preserving Padé smoothing for parabolic problems; the available abstract does not establish this six-node iff graph-weight design law, but its full text could not be inspected, so overlap cannot be ruled out. Horváth (2005) studies Runge–Kutta positivity step thresholds, while Horváth, Song and Terlaky (2014, Theorem 3.12) give general rational-method invariance sufficient criteria. Neither accessible theorem yields the specific global three-rung all-step classification. Existing fourth-order Gauss positivity calculations for weighted four-vertex paths and rectangular four-cycles involve distinct graph topologies and parameters. Known weighted-ladder spanning-tree Green kernels concern a different invariant. The claim is not uniqueness of the integrator, only uniqueness of this graph's rung tuning under the specified rail constraint.

## Limitations
Only the six-vertex two-rail, three-rung graph with all four rail conductances equal and every rung positive is classified. More general six-vertex graphs, varying individual rail conductances, higher ladders and other methods are not addressed. The statement is for the completed matrix update and does not assert positivity of intermediate stages or independent mathematical certification. The exact publication-priority relationship to two inaccessible older full texts remains unresolved.

## References
1. Wade et al., *Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data*, published September 29, 2004, https://doi.org/10.1002/num.20039.
2. Z. Horváth, *On positivity step size threshold of Runge-Kutta methods*, *Applied Numerical Mathematics*, 2005, https://doi.org/10.1016/j.apnum.2004.08.026.
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, 2014, https://arxiv.org/abs/1406.6755 (especially §3.2, Theorem 3.12).
