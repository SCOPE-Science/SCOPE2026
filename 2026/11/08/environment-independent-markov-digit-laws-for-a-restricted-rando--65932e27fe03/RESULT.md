# Environment-independent Markov digit laws for a restricted random Lüroth map

## Finding
For the six-branch restricted standard/alternating Lüroth maps described below, the digit process is the **same in distribution for every fixed sequence of map selections**. In fact, the three-state interval itinerary is a stationary homogeneous Markov chain with transition matrix
\[
Q=\begin{pmatrix}\frac16&\frac16&\frac23\\0&0&1\\\frac14&\frac14&\frac12\end{pmatrix},\qquad
\pi=\left(\frac3{16},\frac3{16},\frac58\right).
\]
This conclusion holds simultaneously for all deterministic switching sequences in the following sense: for each specified infinite binary sequence, the asserted law holds when the initial point is sampled from the same absolutely continuous measure. No probabilistic assumption on the switching sequence is required.

Let \(Z_t\) be the indicator of Lüroth digit \(3\) at time \(t\). For each switching sequence, the exact joint digit laws give
\[
\mathbb E Z_t=\frac3{16},\qquad
\operatorname{Cov}(Z_0,Z_n)=\frac3{256}\left(-\frac13\right)^n\quad(n\ge1),
\]
\[
\operatorname{Var}\left(\sum_{t=0}^{N-1}Z_t\right)
=\frac{75N}{512}+\frac9{2048}\left(1-\left(-\frac13\right)^N\right)\quad(N\ge1),
\]
and the nondegenerate normal limit
\[
\frac{\sum_{t=0}^{N-1}Z_t-3N/16}{\sqrt N}
\ \Longrightarrow\ \mathcal N\left(0,\frac{75}{512}\right).
\]
These are distributional statements for the initial-point measure and do not assert that identical *individual points* produce identical digit strings under different switching sequences.

## Assumptions and scope
Let \(I=[1/3,1]\). Define the standard Lüroth branches \(L(x)=6x-2\) for \(1/3\le x<1/2\) and \(L(x)=2x-1\) for \(1/2\le x\le1\). On the same digit bands define the alternating branches \(A(x)=1-L(x)\). Divide \(I\) at
\[
\frac13,\quad\frac7{18},\quad\frac49,\quad\frac12,\quad\frac23,\quad\frac56,\quad1.
\]
Call the successive six intervals \(I_1,\ldots,I_6\), ignoring the values at their finitely many endpoints. The map \(T_0\) uses the alternating branch on \(I_1\cup I_4\), and the standard branch on \(I_2\cup I_3\cup I_5\cup I_6\). The map \(T_1\) uses the alternating branch on \(I_1\cup I_2\cup I_4\cup I_5\), and the standard branch on \(I_3\cup I_6\). These are the restricted maps of Kalle and Maggioni, *Invariant densities for random systems of the interval*, Section 7.

Fix **arbitrarily** \(\omega=(\omega_0,\omega_1,\ldots)\in\{0,1\}^{\mathbb N_0}\), independently of the random initial point. Define \(X_{t+1}=T_{\omega_t}(X_t)\), with \(X_0\) distributed with density
\[
h(x)=\frac98\mathbf1_{[1/3,2/3]}(x)+\frac{15}8\mathbf1_{(2/3,1]}(x).
\]
Set \(J_t=0\) when \(X_t\in[1/3,1/2)\), \(J_t=1\) when \(X_t\in[1/2,2/3)\), and \(J_t=2\) when \(X_t\in[2/3,1]\). Define the Lüroth digit \(D_t=3\) if \(J_t=0\), and \(D_t=2\) otherwise; thus \(Z_t=\mathbf1_{\{D_t=3\}}\). All finite endpoint/preimage ambiguities lie in an initial-point null set, for each fixed switching sequence.

For any length \(m\ge1\), write \(E_3=\operatorname{diag}(1,0,0)\), \(E_2=\operatorname{diag}(0,1,1)\), and let \(\mathbf1\) be the three-dimensional all-ones column. The **entire stationary digit-cylinder law** is
\[
\Pr(D_0=d_0,\ldots,D_{m-1}=d_{m-1})
=\pi E_{d_0}QE_{d_1}\cdots QE_{d_{m-1}}\mathbf1,
\qquad d_j\in\{2,3\}.
\]
The same formula holds starting at any fixed time \(t\ge0\), regardless of the selected maps before or after it.

## Proof
**1. Common Markov partition and the equal-image property.** Let the three coarse atoms be \(H_0=[1/3,1/2)\), \(H_1=[1/2,2/3)\), \(H_2=[2/3,1]\). Both maps have the same images for their respective restrictions to every \(I_j\). Independently of which map is selected, the images in order are
\[
T_\omega(I_1)=H_2,\quad
T_\omega(I_2)=H_0\cup H_1,\quad
T_\omega(I_3)=H_2,\quad
T_\omega(I_4)=H_2,\quad
T_\omega(I_5)=H_0\cup H_1,\quad
T_\omega(I_6)=H_2,
\]
up to endpoints. The absolute derivative is \(6\) on the first three intervals and \(2\) on the last three. Switching changes only the orientation of the restrictions to \(I_2\) and \(I_5\), never their image or absolute slope. Each restriction covers its image *entirely* with constant absolute derivative.

If a point is uniform on \(H_0\), the respective source pieces \(I_1,I_2,I_3\) have equal lengths \(1/18\). The first and third go to \(H_2\), whereas \(I_2\) sends equal probabilities to \(H_0,H_1\). Thus the next-atom probabilities are \((1/6,1/6,2/3)\). From \(H_1\), the unique piece \(I_4\) goes entirely to \(H_2\), giving \((0,0,1)\). From \(H_2\), pieces \(I_5,I_6\) each have length \(1/6\), and \(I_5\) maps half its mass to each of \(H_0,H_1\), giving \((1/4,1/4,1/2)\). These three rows yield \(Q\), the same for \(T_0\) and \(T_1\).

**2. Conditional uniformity and the universal full law.** Uniform measure on a source coarse atom, restricted to any one of the contributing affine pieces, pushes forward to a constant multiple of Lebesgue measure on its whole target coarse atom. When several pieces contribute to the same target atom, their constant densities add. Therefore, conditional on the next coarse atom, the image point is again uniform on it. This remains true after additionally conditioning on an *entire preceding finite coarse itinerary*: apply the same fact inductively. The initial density is constant on each \(H_j\), with masses \(\pi\) and \(\pi Q=\pi\). Consequently the finite-dimensional laws of \((J_t)\) are exactly those of the stationary homogeneous Markov chain \((\pi,Q)\), for **every** fixed infinite sequence \(\omega\), with no averaging over map choices. Summing over the hidden coarse states yields the displayed digit-cylinder formula.

**3. Correlations and finite-sample variance.** The characteristic polynomial of \(Q\) is \((z-1)z(z+1/3)\). For \(n\ge1\), direct diagonalization or the recurrence gives
\[
(Q^n)_{00}=\frac3{16}+\frac1{16}\left(-\frac13\right)^n.
\]
Since \(Z_t=\mathbf1_{\{J_t=0\}}\), the two-point law immediately gives the covariance formula. In particular \(\operatorname{Var}(Z_0)=39/256\), and expanding the variance of the sum gives
\[
N\frac{39}{256}+2\sum_{k=1}^{N-1}(N-k)\frac3{256}\left(-\frac13\right)^k
=\frac{75N}{512}+\frac9{2048}\left(1-\left(-\frac13\right)^N\right).
\]

**4. Central limit theorem.** The matrix \(Q\) is irreducible and aperiodic: each state reaches \(H_2\), \(H_2\) reaches every state, and \(Q_{00}>0\). A bounded additive functional of a stationary irreducible aperiodic finite-state Markov chain obeys the central limit theorem, for example by solving the finite-state Poisson equation and applying the bounded-increment martingale central limit theorem. Its asymptotic variance is the absolutely convergent covariance series,
\[
\frac{39}{256}+2\sum_{k\ge1}\frac3{256}\left(-\frac13\right)^k=\frac{75}{512}>0.
\]
The entire finite-dimensional digit process agrees with this Markov-derived process for each fixed \(\omega\), so the same limit applies under the initial-point distribution for that \(\omega\). This proves all claims.

## Verification
A standalone standard-library Python checker uses exact rational arithmetic. It reconstructs the image-to-atom transition proportions for both maps, verifies stationarity and the covariance/variance formulas, and independently integrates four-step original-point cylinders for all \(16\) fixed switching words, comparing \(3888\) state-cylinder probabilities with the Markov law. Run `python3 checker.py` from this package. The checker tests finite depths, while the proof above establishes all lengths and all deterministic switching sequences.

## Relationship to prior work
Kalle and Maggioni's 2018 preprint, later published in *Ergodic Theory and Dynamical Systems*, Section 7, introduces the six restricted branches, constructs the density \(h\), and obtains the one-digit frequency \(3/16\) for digit \(3\) under Bernoulli map selection. The density and the one-digit frequency are **prior results**, not the contribution here. Their subsequent *On approximation by random Lüroth expansions* (2021 preprint), Proposition 5.1, establishes the existence of Markov partitions for rational lower cutoffs and studies expansions, stationary measures and digit frequencies. Neither inspected treatment states the common three-state stochastic matrix, the independence of every finite digit law from an *arbitrary fixed switching path*, or these exact autocovariance/variance/CLT formulas. General Markov-partition theory provides background technique but does not itself assert the equal-image and equal-transition property used here. Results concerning ordinary i.i.d. Lüroth digits apply to a different digit process and do not imply this non-i.i.d. law.

## Limitations
The probability distribution here is the specified absolutely continuous initial law, not arbitrary initial distributions. Switching sequences are fixed independently of the initial sample; the result does not cover state-dependent adversarial selection that observes the current point, and does not assert pathwise equality across switching schedules. The maps are precisely the special restricted six-branch pair with cutoff \(1/3\); no universality across all cutoffs is claimed. Every endpoint statement is modulo an initial-measure null set. The proof uses standard finite-state Markov limit theory for the central limit statement; it is not an independent external audit. Although the inspected sources do not contain the quantitative result, publication priority beyond them is not definitively established.

## References
1. C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430, initial version posted 2018-05-29, Section 7; *Ergodic Theory and Dynamical Systems* 42 (2022), 141–179, DOI: 10.1017/etds.2020.127.
2. C. Kalle and M. Maggioni, *On approximation by random Lüroth expansions*, arXiv:2101.01982, initial version posted 2021-01-06, especially Section 5 and Proposition 5.1; *International Journal of Number Theory* 18 (2022), 1013–1046, DOI: 10.1142/S1793042122500531.
3. J. Barrionuevo, R. M. Burton, K. Dajani and C. Kraaikamp, *Ergodic properties of generalized Luroth series*, TU Delft Report 94–105 (1994), background on generalized Lüroth expansions.
