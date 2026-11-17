# Rim subdivision creates exponential majority equilibria on gear graphs

## Finding
For every integer \(n\ge3\), let \(G_n\) be the gear graph obtained from the wheel \(K_1\vee C_n\) by subdividing every rim edge once, retaining all spokes. Each labelled vertex carries a bit. At each synchronous update it adopts the strict majority of its **open neighbors**, retaining its bit in a tie. Write \(E_n\) for the number of labelled fixed configurations.

For integers \(j,r\), binomial coefficients with nonnegative integer parameters have their usual values. Then the **exact** all-size fixed-state count is
\[
E_n=2\left(1+\sum_{j=1}^{\lfloor n/2\rfloor}\;\sum_{r=1}^{\min(j,\lfloor(n-j)/2\rfloor)}\frac nr\binom{j-1}{r-1}\binom{n-j-r-1}{r-1}\right).
\]
Equivalently, let \(T(z)\) be the four-state polynomial transfer matrix indexed in the order \(00,01,10,11\):
\[
T(z)=\begin{pmatrix}
1&z&0&0\\
0&0&1&z\\
1&0&0&0\\
0&0&1&z
\end{pmatrix}.
\]
Then
\[
E_n=2\sum_{j=0}^{\lfloor n/2\rfloor}[z^j]\operatorname{tr}(T(z)^n),\qquad
\det(I-tT(z))=1-(1+z)t+zt^2-zt^3.
\]
Let \(\lambda=1.75487766624669\ldots\) be the largest real root of \(\lambda^3-2\lambda^2+\lambda-1=0\). There exists a constant \(\eta\) satisfying \(0<\eta<\lambda\), independent of \(n\), such that
\[
E_n=2\lambda^n+O(\eta^n).
\]
Consequently the probability that a uniformly chosen initial bit assignment is already fixed is asymptotic to \((\lambda/4)^n\). The result concerns *immediate fixed points*, not the eventual convergence time or number of two-cycles.

## Assumptions and scope
The graph has one hub \(h\), original rim sites \(v_i\), and edge-subdivision sites \(w_i\), with indices in \(\mathbb Z/n\mathbb Z\). The edges are \(hv_i\), \(v_iw_i\), and \(w_iv_{i+1}\) for every \(i\); there are \(2n+1\) vertices and \(3n\) edges. The hub has degree \(n\), each original rim site has degree three, and each subdivision site has degree two. Each vertex and all labels are distinguished. There are no self-neighbor votes, randomized ties, or asynchronous updates. The count includes both choices of hub bit.

## Proof
**1. A canonical description of every fixed configuration.** Fix the hub bit at zero; complementation gives a bijection to those with hub bit one. Write \(x_i\in\{0,1\}\) for the bit at \(v_i\) and \(y_i\) at \(w_i\). The hub is fixed exactly when
\[
\sum_{i=0}^{n-1}x_i\le\lfloor n/2\rfloor.
\]
At a degree-two subdivision site, agreement of its two original-rim neighbors forces its own bit to equal theirs; disagreement causes a tie and imposes no constraint. At an original-rim site of bit one, the hub disagrees, so **both** neighboring subdivision sites must have bit one. Thus every subdivision site adjacent to any original-rim one must be one. At an original-rim site of bit zero, the hub agrees and at least one neighboring subdivision site must be zero; hence at least one adjacent original-rim site must be zero. An isolated original-rim zero (cyclic pattern \(101\)) is therefore forbidden.

Conversely, if the hub constraint holds and the cyclic rim word \(x\) avoids \(101\), define
\[
y_i=x_i\lor x_{i+1}.
\]
Every subdivision site is fixed, every one on the original rim has two neighboring subdivision ones, and every zero on the original rim has a zero subdivision neighbor. Thus all vertices are fixed. Furthermore, any fixed configuration **must** choose the same \(y_i\): if either adjacent rim bit is one, that rim site forces \(y_i=1\); if both are zero, the degree-two subdivision site forces \(y_i=0\). This proves a bijection between fixed configurations with hub zero and cyclic binary words with at most half ones and no isolated zeros. Complementation gives the factor two.

**2. Labelled cyclic-run enumeration.** The all-zero rim word contributes one for each hub color. Every other eligible rim word has \(j\ge1\) ones and \(n-j\ge2\) zeros, partitioned into \(r\) positive one-runs and \(r\) zero-runs each of length at least two. The positive compositions of the one-runs number \(\binom{j-1}{r-1}\), and the zero-runs number \(\binom{n-j-r-1}{r-1}\). Marking a run boundary among \(n\) labelled positions and dividing by the \(r\) choices of marked run gives the number of unmarked labelled cyclic words: \(\frac nr\binom{j-1}{r-1}\binom{n-j-r-1}{r-1}\). The bounds on \(r\) and \(j\) yield the displayed exact sum.

**3. Transfer construction.** Index states by two successive cyclic word bits \((a,b)\). The allowed transition \((a,b)\to(b,c)\) has weight \(z^c\), except for the forbidden triple \((a,b,c)=(1,0,1)\). A closed walk of length \(n\) records exactly one labelled length-\(n\) cyclic word, weighted by its number of ones. This gives the trace formula and direct determinant expansion yields the displayed cubic determinant. The characteristic polynomial at \(z=1\) is \(\ell(\ell^3-2\ell^2+\ell-1)\).

**4. Strictly sub-half density and the asymptotic.** For every positive \(z\), this transfer matrix has the same strongly connected aperiodic directed support, hence has a simple Perron eigenvalue \(\rho(z)>0\). At \(z=1\), \(\rho(1)=\lambda\). Implicit differentiation of \(\rho^3-(1+z)\rho^2+z\rho-z=0\) gives the limiting weighted density
\[
\mu=\left.\frac{z\rho'(z)}{\rho(z)}\right|_{z=1}
=\frac{\lambda^2-\lambda+1}{\lambda(3\lambda^2-4\lambda+1)},\qquad
1-2\mu=\frac1{\lambda(3\lambda^2-4\lambda+1)}>0.
\]
The last equality uses \(\lambda^3-2\lambda^2+\lambda-1=0\); numerically \(\mu\approx0.4114955887\). Therefore for some fixed \(z_*>1\) sufficiently close to one, \(\rho(z_*)/\sqrt{z_*}<\lambda\). With nonnegative coefficients, the number of cyclic admissible words having more than \(n/2\) ones is bounded by \(z_*^{-n/2}\operatorname{tr}(T(z_*)^n)=O((\rho(z_*)/\sqrt{z_*})^n)\). At \(z=1\), Perron separation gives \(\operatorname{tr}(T(1)^n)=\lambda^n+O(\theta^n)\) for some \(\theta<\lambda\). Subtracting the tail and restoring the two hub colors proves the claimed \(2\lambda^n+O(\eta^n)\), where \(\eta<\lambda\). Since there are \(2^{2n+1}\) labelled initial assignments, the fixed-point probability is asymptotic to \((\lambda/4)^n\).

## Verification
The standalone `verify_direct.py` computes the open-neighborhood update on the full graph, exhaustively comparing fixed states, their canonical-word characterization, and the run formula for every \(3\le n\le8\): altogether \(2^7+2^9+2^{11}+2^{13}+2^{15}+2^{17}=174720\) labelled configurations. The fixed totals are respectively \(8,18,22,44,72,146\). `verify_transfer.py` constructs its own weighted automaton and checks its coefficient array against the independently implemented run formula for all \(3\le n\le45\); for \(3\le n\le12\) it also compares against exhaustive cyclic words. `verify_symbolic.py` checks the determinant and the exact density identity using symbolic arithmetic. The actual standard-output records are included. These finite computations corroborate the theorem but do not prove any unbounded assertion; the proof is given in Sections 1–4.

## Relationship to prior work
Agur, Fraenkel and Klein (1988) enumerate local one-dimensional binary majority fixed points by forbidden cyclic patterns, including avoiding isolated bits; their graph has no hub, subdivision layer, or global half-density constraint. Kaaser, Mallmann-Trenn and Natale (2015) study voting-time bounds and general aspects of deterministic majority dynamics, not this exact gear-graph fixed-state census. The standard gear graph is the alternating-rim-subdivision of a wheel (MathWorld). Related results on ordinary wheels have only two majority fixed points, while an independently analyzed **helm** (wheel with a private leaf at each original rim site) has an exponentially growing majority fixed-state census with a different boundary pattern and an asymptotic \(n^{-1/2}\) penalty. The present geometry uses a degree-two **edge subdivision**, resulting instead in a unique subdivision layer given by an OR rule and a strictly sub-half typical rim density. The full primary texts of the first two references and the related helm analysis were inspected for covering statements; none supplies the displayed gear formula or asymptotic.

## Limitations
This is an exact count of configurations already fixed at time zero, not a classification of eventual attractors, transient populations, or temporal two-cycles. The result is restricted to open-neighbor strict binary majority with tie retention and wheel rims of length at least three. Independence or first-ever-publication status has not been externally certified. Relevant older enumerations may use different terminology (such as zero-temperature Ising equilibria on Jahangir or gear graphs); an inaccessible or unindexed equivalent statement remains possible. The finite checks are not substitutes for the analytic proof.

## References
1. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, doi:10.1016/0012-365X(88)90005-2. Full author-hosted text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf .
2. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, first public arXiv version August 14, 2015, https://arxiv.org/abs/1508.03519 .
3. E. W. Weisstein, *Gear Graph*, MathWorld, https://mathworld.wolfram.com/GearGraph.html .
4. *Sharp fixed-point entropy contrast for majority and minority dynamics on helm graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fixed-point-entropy-contrast-for-majority-and-minority-dyn--9b137598a71e .
5. *Oscillation-by-opening and exact two-cycle entropy on majority fan graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-oscillation-by-opening-and-exact-two-cycle-entropy-on-majority-f--f5691edd97d7 .
