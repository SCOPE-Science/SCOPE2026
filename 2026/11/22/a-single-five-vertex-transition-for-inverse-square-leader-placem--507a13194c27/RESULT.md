# A single five-vertex transition for inverse-square leader placement on weighted friendship graphs

## Finding
Let \(m\ge 2\) be an integer and \(t>0\). Let \(F_m(t)\) be the weighted friendship graph consisting of \(m\) triangles meeting at exactly one common hub, with each hub-to-peripheral edge of conductance \(1\) and each peripheral-pair edge of conductance \(t\). Select exactly two distinct vertices as perfectly grounded leaders. Write \(F\) for the remaining vertices, \(L_{FF}\) for the principal grounded weighted combinatorial Laplacian, and
\[
J_2(S)=\operatorname{tr}(L_{FF}^{-2}).
\]
Put
\[
\tau=\frac{2\sqrt{61}-7}{15}=0.5746999567\ldots.
\]
All minimizers, and no other sets, are classified as follows.

* If \(m=2\) and \(0<t<\tau\), the minimizers are precisely the four pairs consisting of the hub and one peripheral vertex.
* If \(m=2\) and \(t=\tau\), those four pairs and the four pairs consisting of peripheral vertices in distinct triangles all minimize.
* If \(m=2\) and \(t>\tau\), precisely the four different-triangle peripheral pairs minimize.
* If \(m\ge3\), for every \(t>0\), precisely the \(2m\) hub-plus-peripheral pairs minimize.

Two peripheral leaders from the same triangle are strictly suboptimal throughout the domain. In particular, at three triangles there is **no** hub-abandonment transition for \(J_2\), unlike the first-inverse objective \(J_1(S)=\operatorname{tr}(L_{FF}^{-1})\), whose already-known threshold is \(t=3\). Thus for every \(m=3\) and every \(t>3\), the optimal leader classes for \(J_1\) and \(J_2\) are disjoint. For \(m=2\), they are also disjoint when \(1/3<t<\tau\).

For exact objective values, define
\[
\begin{aligned}
H_m(t)&=\frac1{(1+t)^2}+(m-1)\left(1+\frac1{(1+2t)^2}\right),\\
Q_m(t)&=(4m^2+4m-39)t^2+(8m^2-46)t+(4m^2+4m-11).
\end{aligned}
\]
The minimum is
\[
\min_{|S|=2}J_2(S)=H_m(t)+\min\left\{0,\frac{Q_m(t)}{4(1+2t)^2}\right\}.
\]

## Assumptions and scope
There are \(2m+1\) vertices, one hub and two distinguishable peripheral vertices per triangle. Each undirected edge has strictly positive conductance as specified, with no further edges. The Laplacian is **unnormalized**: \(L_{ij}=-c_{ij}\) for adjacent distinct vertices and \(L_{ii}=\sum_{j\ne i}c_{ij}\). Grounding deletes leader rows and columns but retains every edge-to-leader contribution in follower diagonals. The two leaders are ideal, zero-noise, perfectly pinned vertices; their positions are unrestricted. The integer \(m\) is at least two and \(t\) is arbitrary finite positive real. Since the graph is connected and some vertices are grounded, \(L_{FF}\) is positive definite. No claim is made for leader gains that are finite, nonidentical triangle conductances, more than two leaders, or other damping/noise models.

For a second-order follower model with independent unit acceleration disturbances,
\[
\ddot z+\gamma L_{FF}\dot z+\delta L_{FF}z=w,
\qquad \gamma,\delta>0,
\]
the stationary positional variance is \(J_2(S)/(2\gamma\delta)\). To see this, a mode of eigenvalue \(\lambda>0\) has state matrix \(\left(\begin{smallmatrix}0&1\\-\delta\lambda&-\gamma\lambda\end{smallmatrix}\right)\). Its stationary Lyapunov equation gives position–velocity covariance zero, velocity variance \(1/(2\gamma\lambda)\), and position variance \(1/(2\gamma\delta\lambda^2)\). Thus the same leader sets minimize second-order positional coherence for every fixed positive \(\gamma,\delta\).

## Proof
**1. Exhaustive symmetry classes.** The automorphism group of \(F_m(t)\) permutes triangles and swaps the two vertices within each triangle. Every unordered two-leader pair has exactly one of the following forms: \(H\), hub plus one peripheral; \(S\), two peripherals in one triangle; or \(D\), two peripherals from distinct triangles. Their multiplicities are respectively \(2m\), \(m\), and \(2m(m-1)\). There are no other possibilities.

**2. An exact squared-inverse block identity.** For a positive-definite matrix
\[
M=\begin{pmatrix}d&-u^{\mathsf T}\\-u&B\end{pmatrix},
\quad s=d-u^{\mathsf T}B^{-1}u>0,
\quad q_j=u^{\mathsf T}B^{-j}u,
\]
block inversion and direct multiplication give
\[
\operatorname{tr}(M^{-2})
=\operatorname{tr}(B^{-2})+\frac{(1+q_2)^2}{s^2}+\frac{2q_3}{s}.
\tag{1}
\]
Indeed, the inverse has blocks \(s^{-1}\), \(s^{-1}u^{\mathsf T}B^{-1}\), \(s^{-1}B^{-1}u\), and \(B^{-1}+s^{-1}B^{-1}uu^{\mathsf T}B^{-1}\); taking its squared Frobenius norm yields (1). This is an identity for every finite positive-definite block matrix of the displayed form.

**3. Hub–peripheral leaders.** Grounding the hub and one peripheral leaves one isolated scalar block \([1+t]\) and \(m-1\) copies of
\[
T=\begin{pmatrix}1+t&-t\\-t&1+t\end{pmatrix}.
\]
The eigenvalues of \(T\) are \(1\) and \(1+2t\). Consequently
\[
J_2(H)=H_m(t)=\frac1{(1+t)^2}+(m-1)\left(1+\frac1{(1+2t)^2}\right).
\tag{2}
\]

**4. Same-triangle peripheral leaders.** The hub is a follower of diagonal \(2m\), attached to \(m-1\) intact copies of \(T\). Applying (1) with \(B=T^{\oplus(m-1)}\), \(u\) consisting of \(m-1\) copies of \((1,1)^{\mathsf T}\), and \(s=2\), gives \(q_2=q_3=2(m-1)\) and
\[
J_2(S)=m^2+2m-\frac{11}{4}+\frac{m-1}{(1+2t)^2}.
\tag{3}
\]
Subtracting (2),
\[
J_2(S)-J_2(H)=m^2+m-\frac74-\frac1{(1+t)^2}>0
\tag{4}
\]
for every \(m\ge2\), \(t>0\), since the right side exceeds \(6-7/4-1=13/4\). Thus \(S\) is never optimal.

**5. Different-triangle peripheral leaders.** Here the follower hub is joined to two scalar blocks \([1+t]\) and \(m-2\) copies of \(T\). In (1), take
\[
\begin{aligned}
B&=[1+t]^{\oplus2}\oplus T^{\oplus(m-2)},\\
s&=4-\frac{2}{1+t}=\frac{2(1+2t)}{1+t},\\
q_2&=\frac{2}{(1+t)^2}+2(m-2),\\
q_3&=\frac{2}{(1+t)^3}+2(m-2),\\
\operatorname{tr}(B^{-2})&=\frac2{(1+t)^2}+(m-2)\left(1+\frac1{(1+2t)^2}\right).
\end{aligned}
\]
The identities for \(q_2,q_3\) follow from \(T(1,1)^{\mathsf T}=(1,1)^{\mathsf T}\). Substitution into (1) and rational simplification yield
\[
J_2(D)-J_2(H)=\frac{Q_m(t)}{4(1+2t)^2}.
\tag{5}
\]
This formula remains valid for \(m=2\), when the empty direct sum of \(T\)-blocks is omitted.

**6. Exact signs and all ties.** For \(m\ge3\), the coefficients of \(t^2\), \(t\), and the constant term in \(Q_m(t)\) are respectively at least \(9\), \(26\), and \(37\), and increase with \(m\). Hence \(J_2(D)>J_2(H)\) for every \(t>0\). For \(m=2\),
\[
Q_2(t)=13-14t-15t^2.
\]
This polynomial strictly decreases on \(t>0\), starts positive, tends to negative infinity, and has exactly one positive root \(\tau=(2\sqrt{61}-7)/15\). Its sign is positive below \(\tau\), zero at \(\tau\), and negative above. Combining (4) and (5) proves the complete optimizer classification, exact minimum, and counts. No finite enumeration or generic optimizer assumption is used in the proof.

**7. Precise first-/second-order separation.** The established first-inverse orbit comparison on the same weighted graph is
\[
J_1(D)-J_1(H)=\frac{(2m-7)t+2m-3}{2(1+2t)}.
\]
For \(m=2\) this changes sign at \(t=1/3\), strictly below \(\tau\); for \(m=3\) it changes sign at \(t=3\), while the numerator of (5) remains positive. These strict opposite-sign intervals prove the asserted disagreement without assuming any equivalence of the two stochastic objectives. For example, at \(m=3,t=4\), the differences are \(J_1(D)-J_1(H)=-1/18\) and \(J_2(D)-J_2(H)=95/108\).

## Verification
Run `python3 verify.py` with SymPy 1.14 (see `requirements.txt`). The program builds each complete weighted Laplacian independently from its edge list, deletes every candidate unordered leader pair, performs exact rational matrix inversion, compares the traces of squared inverses to the three formulas, and exhaustively checks every minimizing pair. It tests each \(m\) from \(2\) through \(7\) at seven positive rational conductances, totaling **4,354 exact matrix/orbit assertions**, together with eight independent symbolic/formula checks. It verifies the quadratic radical root symbolically. Its recorded deterministic checker output is `verification_output.txt`. This finite test only corroborates the explicit all-parameter proof above. The proof is valid for arbitrary real \(t>0\), including its irrational threshold, and all integers \(m\ge2\).

## Relationship to prior work
Patterson and Bamieh (arXiv:1310.2592, first public version 2013-10-09) formulate first- and second-order stochastic network coherence and identify the inverse-square Laplacian moment for second-order dynamics; their article treats leaderless fractal families, not the present optimal two-leader weighted friendship problem. Fitch and Leonard (arXiv:1407.1569, first public version 2014-07-07) give general first-order noisy leader-selection formulas, including biharmonic-distance expressions, and explicit cycle/path placements; their objective is the *first* inverse grounded trace and the presence of a squared pseudoinverse in their general reduction does not establish the present second-inverse optimization. Fardad, Lin and Jovanović (CDC-ECC 2011) likewise use the first-inverse grounded objective and algorithmic relaxations.

An accessible prior public theorem, *Two-leader phase transitions on weighted friendship graphs* (2026-11-02, published research record), covers **exactly the same graph and leader budget but the first-inverse objective**. Its exact comparison is quoted in Proof step 7 and is not misrepresented as a new result. The broader first-inverse *Two-leader coherence transitions in weighted clique windmills* (2026-10-25) contains the friendship graph as its two-vertex-petal specialization but likewise does not treat the squared inverse. Nearby results on second-order wheel leaders, finite-gain first-order friendship pinning, and ungrounded spectral-moment conductance allocation have different mathematical objectives or graph families. They do not imply the classification in this result without new analysis.

Sun, Li and Liu, *Noisy consensus dynamics in windmill-type graphs* (Chaos 2020, DOI 10.1063/5.0020696), is a close windmill-specific paper whose abstract mentions freely assigned leader locations. Its full text could not be inspected through available open access or institutional access; the available abstract does **not** establish a weighted \(t\)-dependent inverse-square two-leader theorem, but possible stronger coverage is a genuine unresolved priority risk. This result asserts a proved mathematical theorem, not an independently verified universal priority claim.

## Limitations
The exact optimizer law depends on identical hub conductances, identical peripheral conductances, two perfectly grounded leaders, and the inverse-square objective. The special transition at \(m=2\) is not claimed to persist under heterogeneous weights or leader gains. The result is self-contained and checked with symbolic and finite exact computations; it has not received independent mathematical audit. Specialist work unavailable in full text may affect originality, though the clear first-inverse comparisons do not algebraically settle the inverse-square phase diagram.

## References
1. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592, first public version 2013-10-09, https://arxiv.org/abs/1310.2592.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public version 2014-07-07, https://arxiv.org/abs/1407.1569.
3. M. Fardad, F. Lin, and M. R. Jovanović, *Algorithms for Leader Selection in Large Dynamical Networks: Noise-Free Leaders*, IEEE CDC-ECC 2011, https://viterbi-web.usc.edu/~mihailo/papers/farlinjovCDC11.pdf.
4. *Two-leader phase transitions on weighted friendship graphs*, public research result dated 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-leader-phase-transitions-on-weighted-friendship-graphs--82f6daf71fff.
5. *Two-leader coherence transitions in weighted clique windmills*, public research result dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-leader-coherence-transitions-in-weighted-clique-windmills--0c2bf4c3c159.
6. W. Sun, Y. Li, and S. Liu, *Noisy consensus dynamics in windmill-type graphs*, *Chaos* 30 (2020), 123131, https://doi.org/10.1063/5.0020696 (full text not accessible; abstract inspected).
