# Exact space-time occupation law and Gaussian concentration in Rule 73 three-cycles

## Finding
Consider the synchronous binary elementary cellular automaton Rule 73 on a labelled cyclic ring of length \(n\ge3\). For each temporal orbit \(\mathcal O=\{x,F(x),F^2(x)\}\) of least period three, define its **three-time occupation**
\[
K(\mathcal O)=|x|_1+|F(x)|_1+|F^2(x)|_1,
\]
which is independent of the choice of phase \(x\). Let \(W_n(u)=\sum_{\mathcal O}u^{K(\mathcal O)}\), with temporal orbits distinct unless identical as subsets (spatial translations are not identified).

Define
\[
\begin{aligned}
Q_3(z,u)&=(1+u^5z^4+u^6z^5)^2P(z,u),\\
P(z,u)&=1-u^6z^3-(u^6+2u^5)z^4-2u^6z^5-u^{11}z^7\\
&\quad+(2u^{11}-u^{12})z^8+2u^{12}z^9,\\
Q_1(z,u)&=1-u^6z^3-u^6z^4.
\end{aligned}
\]
Then the **complete space-time occupation enumerator at all lengths** is
\[
\boxed{\sum_{n\ge1}W_n(u)z^n=-\frac z3\,\partial_z\log\frac{Q_3(z,u)}{Q_1(z,u)}.}
\]
The coefficient identity holds even for \(n=1,2\) under the indexed periodic convention, but the stated physical scope is \(n\ge3\). In particular,
\[
W_7(u)=7u^{11},\quad W_8(u)=8u^{10}+8u^{12},\quad W_9(u)=18u^{11}.
\]

Choose one primitive temporal-three orbit uniformly from those on the \(n\)-ring; let \(K_n\) be its three-time occupation. Let \(r\) be the smallest positive real root of
\[
P(r,1)=1-r^3-3r^4-2r^5-r^7+r^8+2r^9=0.
\]
Numerically \(r=0.6469466411538236\ldots\), and the dominant growth base is \(\lambda=1/r=1.5457225316395628\ldots\). Write \(\Theta_u=u\partial_u\), \(\Theta_z=z\partial_z\), and set
\[
 a=\left.\frac{\Theta_u P}{\Theta_z P}\right|_{(z,u)=(r,1)},\qquad
 b=\left.\frac{\Theta_u^2P-2a\Theta_u\Theta_zP+a^2\Theta_z^2P}{\Theta_zP}\right|_{(r,1)}.
\]
Then \(a=1.46305640300557\ldots\), \(b=0.343769801111868\ldots>0\), and
\[
\boxed{\frac{K_n}{3n}\longrightarrow \mu=\frac a3=0.4876854676685245\ldots\ \text{in probability},\qquad
\sqrt n\left(\frac{K_n}{3n}-\mu\right)\Longrightarrow\mathcal N(0,b/9).}
\]
The limiting Gaussian variance coefficient is \(b/9=0.03819664456798536\ldots\). The finite-length polynomial and this asymptotic law concern **uniform temporal-three orbits**, not the eventual magnetization under random initial states.

## Assumptions and scope
Each ring site has value \(0\) or \(1\). The local rule is \(f(a,b,c)=1\) precisely when \((a,b,c)\) is \(000\), \(011\), or \(110\); the other five triples output zero. The synchronous global map is \(F_n(x)_i=f(x_{i-1},x_i,x_{i+1})\), using indices modulo \(n\). All sites are indexed, and neither shifts nor reflections are quotient symmetries. The measured variable \(K\) sums occupied sites across **all three temporal phases**, rather than measuring a single phase or a random-trajectory limiting frequency. Three-cycles are primitive temporal orbits, so fixed configurations are excluded exactly.

## Proof
For a state returning after three time steps, encode at each spatial coordinate its history \(h_i\in\{0,1\}^3\), with bits \(h_i(t)\) for \(t=0,1,2\). Three histories \((a,b,c)\) may be consecutive spatially precisely if \(f(a(t),b(t),c(t))=b(t+1\bmod3)\) for each \(t\). Define a directed graph on ordered pairs \((a,b)\) of history symbols, with \((a,b)\to(b,c)\) exactly when these equations hold. Weight this edge by \(u^{|b|_1}\). A labelled cyclic configuration returning after three updates is in bijection with a length-\(n\) closed walk with a marked starting site; its edge-weight product is \(u^{|x|_1+|F(x)|_1+|F^2(x)|_1}\). Thus the weighted count of \(\operatorname{Fix}(F_n^3)\) is \(\operatorname{tr}(A_3(u)^n)\).

Exhaustively applying the eight-entry local truth table to the \(8^3=512\) possible history triples leaves, among directed graph vertices lying on directed cycles, exactly one strongly connected component on 19 vertices with 32 directed edges. The other vertices lie on no closed walk and do not affect traces or determinants. Exact symbolic elimination of its 19-by-19 weighted adjacency matrix yields \(\det(I-zA_3(u))=Q_3(z,u)\) as displayed above. The entire graph is explicitly reconstructed by `verification/symbolic_transfer.py`; no unverified numerical interpolation enters the factorization.

A fixed configuration has all three time bits equal at each coordinate. Restricting histories to \(000\) and \(111\) gives a four-vertex pair graph, with weighted determinant \(\det(I-zA_1(u))=Q_1(z,u)\). Each primitive temporal-three orbit contributes exactly three configurations of identical total three-time occupation, while each fixed configuration contributes one. Hence \(W_n(u)=(\operatorname{tr}A_3(u)^n-\operatorname{tr}A_1(u)^n)/3\). The matrix identity \(\sum_{n\ge1}\operatorname{tr}(A^n)z^n=-z\partial_z\log\det(I-zA)\) establishes the boxed rational logarithmic-derivative formula for all \(n\).

The 19-vertex component is strongly connected and has directed cycles of both lengths three and four, so its adjacency matrix is primitive. The Perron root \(\lambda=1/r\) is simple and strictly dominates all other eigenvalue moduli. Exact rational positive-vector bounds give \(1.545722531639513<\lambda<1.545722531639620\), and the displayed polynomial has a unique root in \((0,1)\), with \(0.6469466411<r<0.6469466412\). The fixed-point subgraph has smaller spectral radius, since it is a proper subgraph of this irreducible 19-vertex component (strict Perron monotonicity). Consequently, in a neighborhood of \(u=1\), \(\sum_{\mathcal O}u^{K(\mathcal O)}\) has the dominant term \(\lambda(u)^n/3\) with exponentially smaller error, where \(\lambda(u)=1/r(u)\), \(P(r(u),u)=0\), and \(r(1)=r\).

Differentiating \(P(e^{-\kappa(s)},e^s)=0\) twice at \(s=0\), where \(\kappa(s)=\log\lambda(e^s)\), gives \(\kappa'(0)=a\) and \(\kappa''(0)=b\) as stated. The analytic quasi-power moment generating function implies the law of large numbers and the central limit theorem. Strict positivity \(b>0\) follows independently from the irreducible graph's existence of cycles with unequal mean edge occupation: its three-edge cycle \(56\to7\to63\to56\) has occupation sum six, whereas the four-edge cycle \(0\to7\to63\to56\to0\) also has sum six. Their means, two and three-halves, differ, precluding a constant-plus-coboundary occupation potential. This completes the all-length and limit claims.

## Verification
`verification/symbolic_transfer.py` independently generates the entire temporal-history graph from the Rule 73 truth table and reproduces both exact symbolic determinants. `verification/direct_simulation.py` enumerates every original binary ring state for lengths three through seventeen, independently applies the local update three times, and compares the weighted moment polynomials evaluated at \(u=2\) against traces obtained from the claimed determinants. It verifies the first ten explicit orbit counts, the fixed-state subtraction and the weight normalization. `verification/spectral_bound.py` reconstructs the graph, confirms strong connectivity and cycles of lengths three and four, isolates the unique root in \(0,1\), and verifies a rational Perron eigenvector enclosure. The supplied `.out` files are recorded outputs, not substitutes for source programs. All three checks were executed again from the delivered embedded paths.

## Relationship to prior work
Gorodkin, Sørensen and Winther (1993) identify Rule 73's unusual period-three magnetization oscillations under random initial configurations and show that mean-field analysis does not reproduce them; their simulation measure differs from the uniform primitive-orbit measure used here. Wolfram's *A New Kind of Science* (2002) likewise notes domains with period-three behavior. Sutner's *Linear Cellular Automata and Automaticity*, section 3.1, already gives the existence spectrum \(n\ge7\) and early unweighted Rule 73 primitive three-orbit counts \(7,16,18,20,44,68,65,119,250,368,\ldots\); those results are not new here. The all-length **occupation-weighted polynomial**, algebraic orbit-averaged occupation density and Gaussian fluctuation law refine these unweighted statements and were not found in the inspected primary material.

## Limitations
This result does not determine the magnetization law reached from uniformly random **initial** states, nor the joint phase-by-phase occupation distribution or attraction-basin weights. The Gaussian law concerns occupation aggregated over a complete temporal orbit. Priority against unpublished or unindexed weighted enumerations remains uncertain, and no independent external audit has been performed.

## References
- S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics 55 (1983), 601–644, published 1 July 1983, https://doi.org/10.1103/RevModPhys.55.601.
- J. Gorodkin, A. Sørensen, O. Winther, *Neural Networks and Cellular Automata Complexity*, Complex Systems 7 (1993), 1–23, https://content.wolfram.com/sites/13/2018/02/07-1-1.pdf.
- S. Wolfram, *A New Kind of Science* (2002), notes on density oscillations in Rule 73, https://wolframscience.com/nks/notes-6-5--density-oscillations-in-rule-73/.
- K. Sutner, *Linear Cellular Automata and Automaticity*, section 3.1, https://www.cs.cmu.edu/~sutner/papers/sutner-ca-automaticity.pdf (document date not independently established).
- A. Dennunzio, P. Di Lena, L. Margara, *Strictly Temporally Periodic Points in Cellular Automata*, EPTCS 90 (2012), 225–235, https://arxiv.org/abs/1208.2770.
