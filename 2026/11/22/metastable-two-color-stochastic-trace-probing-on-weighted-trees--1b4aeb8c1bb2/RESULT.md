# Metastable two-color stochastic trace probing on weighted trees

## Finding

There are strictly positive weighted trees on every number \(n\ge 7\) of vertices for which the **proper bipartition** is a strict local minimizer of the two-probe Rademacher trace-estimation variance under both (i) every single vertex recoloring and (ii) every recoloring of either component of a deleted edge, but it is **not globally variance optimal**. A seven-vertex exact rational witness has a sharp open screening interval for this simultaneous local-trap and specified global-improvement behavior. At screening \(\mu=1/3\), all globally minimizing partitions of the seven-vertex witness are explicitly classified.

## Assumptions and scope

Let \(T=(V,E,c)\) be a connected finite undirected tree with strictly positive edge conductances \(c_e\). Its weighted Laplacian is \(L_c\). For the common positive killing/screening parameter \(\mu\), define \(G_\mu=(\mu I+L_c)^{-1}\). A two-class partition is encoded by signs \(s_i\in\{-1,+1\}\), with each class nonempty. One independent class-supported Rademacher vector is sampled for each class, and their quadratic forms in \(G_\mu\) are added. The estimator is unbiased for \(\operatorname{tr}(G_\mu)\); its variance is

\[
\mathcal V_\mu(s)=4\sum_{i<j:\,s_i=s_j}(G_\mu)_{ij}^{2}.
\]

This formula assumes **one** independent probe per class, without scaling the probes by class size. Flipping all signs does not change the partition. The local moves considered are every one-vertex flip and every deletion-edge component flip; any move leaving a class empty is not admissible.

The core witness has \(V=\{0,1,2,3,4,5,6\}\), with conductances \(c_{01}=c_{02}=2\), \(c_{06}=c_{13}=c_{14}=c_{15}=1\), and no other edges. Its proper bipartition is

\[
b=(+1,-1,-1,+1,+1,+1,-1).
\]

For \(x=\mu>0\), write

\[
F(x)=x^4+14x^3+58x^2+76x+28,
\qquad
P(x)=x^6+16x^5+83x^4+162x^3+112x^2-16.
\]

Let \(\alpha=0.306799619712031\ldots\) be the **unique positive zero** of \(P\), and \(\beta=\sqrt2-1=0.414213562373095\ldots\). Then, **for every** \(\alpha<x<\beta\), the partition \(b\) is strictly better than all its six one-edge-component neighbors and all its seven one-vertex neighbors, but is strictly worse than the partition obtained by reversing the signs at exactly \(\{1,3,4\}\). The interval is maximal for the conjunction of these particular six edge-neighbor and specified competitor inequalities (it is not asserted to exhaust all screening strengths producing any local trap).

At \(x=1/3\),

\[
\mathcal V(b)=\frac{384984171}{95452900},\qquad
\min_s\mathcal V(s)=\frac{377990793}{95452900},\qquad
\mathcal V(b)-\min_s\mathcal V(s)=\frac{3496689}{47726450}>0.
\]

There are exactly three optimizing **unlabeled** two-colorings, normalized by \(s_0=+1\): they satisfy \(s_1=+1\), \(s_2=s_6=-1\), and exactly one of \(s_3,s_4,s_5\) is \(+1\).

## Proof

**1. Exact variance reduction.** Set \(W(x)=G_x\circ G_x\), where \(\circ\) denotes entrywise multiplication. Since the same-color indicator is \((1+s_i s_j)/2\), we have

\[
\mathcal V_x(s)=2\sum_{i<j}W_{ij}(x)+\sum_{i<j}2s_i s_jW_{ij}(x).
\]

Therefore every variance difference equals the corresponding difference of the quadratic energies \(E_x(s)=s^{\mathsf T}W(x)s\), since diagonal entries and partition-independent constants cancel. The matrix \(\mu I+L_c\) is strictly positive definite for \(\mu>0\), so all inverses and rational calculations below are legitimate.

**2. Explicit local-neighbor gaps.** A direct Schur complement/inversion of the displayed seven-vertex precision matrix gives the following exact differences \(\mathcal V_x(s^{S})-\mathcal V_x(b)\), where \(s^{S}\) flips signs at vertices in \(S\):

\[
\begin{aligned}
S=\{1,3,4,5\}:\quad &\frac{16(x^2+2x-2)(x^4+6x^3+8x^2-4)}{x^2F(x)^2},\\
S=\{2\}:\quad &\frac{16x^6+224x^5+960x^4+1408x^3+640x^2+256x+128}{x^2F(x)^2},\\
S=\{6\}:\quad &\frac{4x^6+64x^5+336x^4+640x^3+240x^2+64x+128}{x^2F(x)^2},\\
S=\{3\},\{4\},\{5\}:\quad &\frac{4(x+2)P(x)}{x(x+1)^2F(x)^2}.
\end{aligned}
\]

All denominators are positive. The second and third numerators have positive coefficients. Both factors of the first numerator are negative throughout \(0<x<\beta\): the quadratic's positive zero is \(\sqrt3-1>\beta\), while the quartic is increasing for positive \(x\) and remains negative at \(x=1/2\). The polynomial \(P\) is strictly increasing on the positive half-line (its derivative has positive coefficients for every positive power), with \(P(0)=-16\), hence exactly one positive zero \(\alpha\). Consequently **all six** edge-component flips have strictly larger variance throughout \((\alpha,\beta)\). No claim is made that the local-edge conditions alone stop at \(\beta\).

The two remaining singleton-flip gaps have positive-coefficient numerators and positive denominators for **every** \(x>0\):

\[
\begin{aligned}
S=\{0\}:&\quad \frac{4(9x^5+104x^4+444x^3+800x^2+636x+176)}{xF(x)^2},\\
S=\{1\}:&\quad \frac{4(7x^6+80x^5+348x^4+688x^3+640x^2+256x+32)}{x^2F(x)^2}.
\end{aligned}
\]

All other singleton moves coincide with the five singleton edge-component moves listed above, hence every singleton flip is strictly unfavorable on \((\alpha,\beta)\).

The specified coordinated recoloring \(S=\{1,3,4\}\) instead has difference

\[
\mathcal V_x(s^S)-\mathcal V_x(b)
=\frac{4(x+2)^2(x^2+2x-1)(5x^3+28x^2+40x+16)}{x(x+1)^2F(x)^2}.
\]

Its sign is negative exactly for \(0<x<\beta\). These facts prove the sharp open window for six edge-neighbors plus this competitor. The singleton-flip analysis above proves that the full vertex-and-edge strict local-minimum condition holds throughout \((\alpha,\beta)\), and the competitor sign establishes a strict global improvement there.

**3. Complete seven-vertex optimization at \(\mu=1/3\).** The inverse can be checked exactly by forming

\[
Q=\begin{pmatrix}
16/3&-2&-2&0&0&0&-1\\
-2&16/3&0&-1&-1&-1&0\\
-2&0&7/3&0&0&0&0\\
0&-1&0&4/3&0&0&0\\
0&-1&0&0&4/3&0&0\\
0&-1&0&0&0&4/3&0\\
-1&0&0&0&0&0&4/3
\end{pmatrix},\qquad G=Q^{-1}.
\]

The six edge-flip gaps, in the edge order \((01),(02),(06),(13),(14),(15)\), are respectively

\[
\left(\frac{3321648}{23863225},\frac{20631024}{23863225},\frac{12053124}{23863225},\frac{730863}{47726450},\frac{730863}{47726450},\frac{730863}{47726450}\right)>0.
\]

The seven one-vertex gaps, in vertex order \(0,\ldots,6\), are

\[
\left(\frac{38945124}{23863225},\frac{51623244}{23863225},\frac{20631024}{23863225},\frac{730863}{47726450},\frac{730863}{47726450},\frac{730863}{47726450},\frac{12053124}{23863225}\right)>0.
\]

Fix \(s_0=+1\) and group the remaining \(2^6=64\) signs by \((s_1,s_2,s_6)=(a,b,c)\) and \(t=\#\{j\in\{3,4,5\}:s_j=+1\}\). Entries in the following exhaustive table are the nonnegative integers \(190905800[\mathcal V(s)-\mathcal V_*]\); a value at column \(t\) represents \(\binom3t\) colorings.

| \((a,b,c)\) | \(t=0\) | \(t=1\) | \(t=2\) | \(t=3\) |
|---|---:|---:|---:|---:|
| \((-,-,-)\) | 530849700 | 189197856 | 16910208 | 13986756 |
| \((-,-,+)\) | 380371140 | 121020480 | 31034016 | 110411748 |
| \((-,+,-)\) | 373411620 | 139255200 | 74462976 | 179034948 |
| \((-,+,+)\) | 478421316 | 326566080 | 344075040 | 530948196 |
| \((+,-,-)\) | 40559940 | **0** | 128804256 | 426972708 |
| \((+,-,+)\) | 36394596 | 78135840 | 289241280 | 669710916 |
| \((+,+,-)\) | 74224836 | 141160320 | 377460000 | 783123876 |
| \((+,+,+)\) | 325547748 | 474784416 | 793385280 | 1281350340 |

The sole zero cell has multiplicity three; every other entry is strictly positive. This proves both the claimed global optimum and every equality case, with no reliance on floating-point optimization.

**4. Strict local traps at every larger order.** Fix \(m\ge1\). Attach \(m\) new leaves to vertex \(3\), giving them a common small conductance \(\varepsilon>0\); retain all original weights and the common killing \(\mu=1/3\). Extend the proper bipartition by assigning each new leaf sign \(-b_3=-1\). As \(\varepsilon\downarrow0\), all old-to-old entries of the inverse tend to those of the seven-vertex inverse, and the original six edge-subtree gaps, seven old-vertex gaps, and specified coordinated-improvement gap converge to the strict seven-vertex values. In particular they retain their signs for sufficiently small positive \(\varepsilon\) (for each fixed \(m\)).

A new leaf \(z\) has Green cross-entries \((G_{\varepsilon})_{zj}=(\varepsilon/\mu)G_{3j}+O(\varepsilon^2)\) for original vertices \(j\). Interactions between two new leaves are \(O(\varepsilon^2)\), so their squared contributions to a singleton-flip gap are \(O(\varepsilon^4)\). Set

\[
H_3=b_3\sum_{j=0}^{6}b_jG_{3j}^2
=\frac{223184259}{190905800}>0.
\]

The variance change from flipping \(z\) alone is therefore

\[
\mathcal V_\varepsilon(s^{\{z\}})-\mathcal V_\varepsilon(s)
=4(\varepsilon/\mu)^2H_3+O_m(\varepsilon^3)>0.
\]

Flipping either component of the new leaf-edge is the same move up to global sign reversal, so it too strictly increases variance. Thus **every** edge-component and singleton move at the enlarged order is unfavorable, while the original coordinated recoloring still improves the variance. All conductances are positive. Since the inequalities are strict and the Green inverse depends continuously on the conductances, the construction persists under sufficiently small perturbations of the entire positive weight vector. The result holds for each integer \(n=7+m\) with \(m\ge0\).

## Verification

`verify_exact.py` uses only Python's standard library and reconstructs the matrix inverse by rational Gaussian elimination. It checks the variance/quadratic-energy identity on all \(64\) partitions, exact local gaps, exact best variance, the full reduced exhaustive table, and the exact anchor coefficient \(H_3\). `verify_symbolic.py` uses SymPy to reconstruct the entire seven-vertex Green inverse over the rational-function field in \(\mu\) and checks all seven factored identities. Run `python verify_exact.py` and `python verify_symbolic.py` alongside this document. The infinite-family extension rests on the stated rational-analytic perturbation argument, not on finite enumeration.

## Relationship to prior work

Hierarchical probing by Stathopoulos, Laeuchli and Orginos (arXiv:1302.4018v1; first public posting 2013-02-17) introduces inverse-trace probing and distance colorings. Frommer, Schimmel and Schweitzer (arXiv:2009.01589) analyze decay and distance-coloring probing errors. Frommer, Rinelli and Schweitzer (arXiv:2308.07722), particularly Definition 3.2 and Theorem 3.3, formally give the class-supported stochastic estimator and the exact variance formula. None of those inspected statements determines whether a proper bipartition can be strictly locally—but not globally—optimal for the exact squared-resolvent variance on a weighted tree. The finite witness and robust infinite family are separate claims from known graph-coloring costs and ordinary graph cut objectives.

## Limitations

The theorem is existential, not a classification of arbitrary weighted trees; its move neighborhood consists specifically of singleton flips and one-edge-component flips, not all multivertex recolorings. The seven-vertex screening interval only certifies this specified witness and competing partition. This does not establish that seven is the smallest possible witness, nor does it assert local-search behavior under random tie-breaking, different sampling budgets, Gaussian probes, or unequal per-vertex screening. Exhaustive enumeration is applied only to the seven-vertex case; the arbitrary-size statement is proved separately. The mathematical review described in accompanying materials is not independent validation, and full publication priority is not conclusively established.

## References

1. A. Stathopoulos, J. Laeuchli and K. Orginos, *Hierarchical Probing for Estimating the Trace of the Matrix Inverse on Toroidal Lattices*, arXiv:1302.4018v1, first posted 2013-02-17. https://arxiv.org/pdf/1302.4018
2. A. Frommer, C. Schimmel and M. Schweitzer, *Analysis of Probing Techniques for Sparse Approximation and Trace Estimation of Decaying Matrix Functions*, arXiv:2009.01589, first posted 2020-09-03. https://arxiv.org/pdf/2009.01589
3. A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of Stochastic Probing Methods for Estimating the Trace of Functions of Sparse Symmetric Matrices*, arXiv:2308.07722v1, first posted 2023-08-15. https://arxiv.org/pdf/2308.07722
