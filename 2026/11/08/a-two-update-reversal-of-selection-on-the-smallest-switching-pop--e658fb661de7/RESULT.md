# A two-update reversal of selection on the smallest switching population network

## Finding
Consider three individuals on a labeled star (a length-two path) alternating with a triangle, beginning with the star. In each graph phase, precisely \(\tau\) birth–death reproduction updates occur before switching. Mutant fitness is \(r>0\), resident fitness is \(1\), and the initial single mutant is placed uniformly among the three vertices. Let \(\rho_\tau(r)\) be its eventual fixation probability and let \(m(r)=r^2/(1+r+r^2)\) denote the three-individual well-mixed Moran fixation probability.

**Theorem (first integer dwell-time reversal, uniformly in fitness).** The system with \(\tau=1\) is a strict suppressor of selection and the system with \(\tau=2\) is a strict amplifier of selection in the all-fitness sense: for every \(r>1\),
\[
\rho_1(r)<m(r)<\rho_2(r),
\]
whereas for every \(0<r<1\) both inequalities reverse. At \(r=1\), all three probabilities are \(1/3\). Consequently, the smallest positive integer dwell length at which this three-vertex switching arrangement is an amplifier is exactly \(2\). This is a statement about dwell lengths \(1\) and \(2\); it **does not** claim monotonicity or amplification for every longer dwell length.

The exact differences are
\[
\rho_1(r)-m(r)=
-\frac{r^2(r-1)(2r+1)(16r^2+31r+16)}{(r^2+r+1)D_1(r)},
\]
\[
\rho_2(r)-m(r)=
\frac{r^2(r-1)(r+2)(2r+1)^2P_6(r)}{(r^2+r+1)D_2(r)},
\]
where \(D_1(r)=80+532r+1334r^2+1751r^3+1334r^4+532r^5+80r^6\),
\[
P_6(r)=544+2960r+5560r^2+6379r^3+5560r^4+2960r^5+544r^6,
\]
and \(D_2(r)=\sum_{j=0}^{12}d_jr^j\), with the ascending coefficient tuple
\[
(d_0,\ldots,d_{12})=(14080,205696,1325168,4967936,12074388,20132868,23783565,20132868,12074388,4967936,1325168,205696,14080).
\]
Every coefficient in these denominator polynomials and in \(P_6\) is strictly positive.

## Assumptions and scope
Vertices \(0,1,2\) are labeled; the star has edges \(\{0,1\},\{0,2\}\), and the triangle adds \(\{1,2\}\). At each integer step, select a reproducing vertex with probability proportional to fitness and then replace the type at one of its neighbors chosen uniformly. The star is used for the first \(\tau\) updates, the triangle for the next \(\tau\), and this deterministic periodic schedule is repeated until all individuals share a type. The initial network phase is **not** randomized. Self-replacement is forbidden; the only self-transitions of the population state arise when parent and neighbor already share a type. No selection-strength approximation is used.

The primary application is evolutionary population dynamics (MSC2020 \(92D15\)); probabilities are computed via a finite absorbing Markov chain. The accepted domain is exactly \(r>0\) and \(\tau\in\{1,2\}\). The unbounded number of future reproduction updates is handled by an absorbing-chain equation, not finite simulation.

## Proof
Because leaves \(1,2\) are exchangeable in both graph phases, group configurations into the six states \((h,\ell)=(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)\), indexed \(0,1,2,3,4,5\). Here \(h\) is the mutant indicator at the star hub and \(\ell\) is the number of mutant leaves. States \(0\) and \(5\) are absorbing. Let \(S(r)\) and \(K(r)\) be the row-stochastic one-step matrices for the star and triangle. Their nonzero outgoing probabilities from the four transient states are given below; the terms \(j:p\) mean probability \(p\) of transition to state \(j\).

| State | Star transitions | Triangle transitions |
|---|---|---|
| \(1\) | \(0:1/[2(r+2)]\), \(1:3/[2(r+2)]\), \(4:r/(r+2)\) | \(0:1/(r+2)\), \(1:1/(r+2)\), \(2:r/[2(r+2)]\), \(4:r/[2(r+2)]\) |
| \(2\) | \(1:1/(2r+1)\), \(5:2r/(2r+1)\) | \(1:1/(2r+1)\), \(2:r/(2r+1)\), \(5:r/(2r+1)\) |
| \(3\) | \(0:2/(r+2)\), \(4:r/(r+2)\) | \(0:1/(r+2)\), \(3:1/(r+2)\), \(4:r/(r+2)\) |
| \(4\) | \(1:1/(2r+1)\), \(4:3r/[2(2r+1)]\), \(5:r/[2(2r+1)]\) | \(1:1/[2(2r+1)]\), \(3:1/[2(2r+1)]\), \(4:r/(2r+1)\), \(5:r/(2r+1)\) |

The absorbing rows satisfy \(S_{00}=K_{00}=S_{55}=K_{55}=1\), and all their other entries are zero. All rows above sum to one, by direct substitution. For a dwell length \(\tau\), put \(Q_\tau=S(r)^\tau K(r)^\tau\); this is the two-phase one-period transition. If \(I=(1,2,3,4)\) indexes transient states and \(f\) is the vector of mutant-fixation probabilities from those states at the start of a star phase, the Markov property and periodicity give
\[
\bigl(I_4-(Q_\tau)_{I,I}\bigr)f=(Q_\tau)_{I,5},\qquad
\rho_\tau(r)=\frac{2f_1+f_3}{3}.
\]
All transient states communicate with an absorbing state via positive-probability paths in a bounded number of periods for every \(r>0\), so the inverse exists and this is the unique absorption-probability solution.

For completeness, the exact polynomial certificate expanding the four-by-four linear system can be reconstructed without a symbolic-mathematics package. Define \(d(r)=2(r+2)(2r+1)\), \(\widehat S=dS\), \(\widehat K=dK\), \(B_\tau=\widehat S^\tau\widehat K^\tau\), and
\[
A_\tau=d^{2\tau}I_4-(B_\tau)_{I,I},\quad b_\tau=(B_\tau)_{I,5}.
\]
Let \(A_\tau^{[j]}\) replace column \(j\) (zero-indexed within the transient indices) by \(b_\tau\). Cramer's rule gives
\[
\rho_\tau(r)=\frac{2\det A_\tau^{[0]}+\det A_\tau^{[2]}}{3\det A_\tau}.
\]
For each \(\tau=1,2\), substituting the table into this identity, multiplying by the common positive denominators, and collecting integer coefficients gives exactly the two factored differences stated in **Finding**. The embedded `verify.py` checks both resulting polynomial identities coefficient-for-coefficient using only integer polynomial arithmetic. Unlike sampling fitness values, this identity check covers all real \(r\) where the rational expressions are defined; in the physical range \(r>0\) the determinant/inverse existence argument applies.

Every factor besides \(r-1\) in the numerators has strict positive value for \(r>0\), and the denominator polynomials have strictly positive coefficients. Hence the first difference has sign opposite to \(r-1\), and the second has the sign of \(r-1\). At \(r=1\), both differences vanish, and \(m(1)=1/3\). This proves the assertions.

## Verification
Run `python verify.py` in the extracted package directory with Python 3 and no external dependencies. The script constructs the normalized one-step matrices in polynomial form, checks both Cramer-derived rational identities exactly over the integers (including all coefficients), checks denominator and auxiliary-polynomial coefficient positivity, and independently constructs the unreduced eight-configuration Markov chain to compare the formula at 40 exact rational test cases. The all-fitness conclusion relies on the symbolic polynomial identity and positivity proof, **not** on these 40 samples.

## Relationship to prior work
Bhaumik and Masuda, *Fixation probability in evolutionary dynamics on switching temporal networks* (arXiv:2304.00170, first public posting 2023-03-31), introduce the same deterministic switching birth–death model and its Markov-chain solution. Their Appendix B, Fig. 7(a), explicitly reports that the three-vertex star/complete switching network suppresses at dwell \(\tau=1\) and amplifies at \(\tau=10\) and \(50\) for the numerical fitness values examined. The existence of a reversal between those regimes is **not** claimed new here. The present result identifies the exact **first** amplifying integer dwell length \(2\) and proves its fitness-uniform strict amplification as well as the all-fitness \(\tau=1\) inequality with exact rational identities. Their generic Markov-chain equation allows numerical determination for any fixed dwell length but does not state this sharp boundary. Related work on static star-graph Moran fixation and general amplifiers is background rather than a covering result for the alternating graph.

## Limitations
Only the three-vertex labeled star-to-triangle schedule and fixed initial star phase are treated; the theorem makes no statement about \(\tau\ge3\), switching with random initial phase, stochastic switching, changing graph sizes, or other replacement updates. All-fitness inequalities are exact for positive fitness, with equality at neutrality. Broader publication-priority uncertainty remains: unidentified equivalent special-case calculations might exist, and the source's general finite-state method implies the expressions computationally, though not the stated sharp sign result explicitly. No independent external mathematical audit is claimed.

## References
1. J. Bhaumik and N. Masuda, *Fixation probability in evolutionary dynamics on switching temporal networks*, arXiv:2304.00170, first public posting 2023-03-31; *Journal of Mathematical Biology* **87**, 64 (2023), https://arxiv.org/abs/2304.00170 and https://doi.org/10.1007/s00285-023-01987-5 . See Model, Section 3.2, Section 4.2.1 and Appendix B.
2. E. P. de Souza and A. G. M. Neves, *Exact fixation probabilities for the Birth-Death and Death-Birth frequency-dependent Moran processes on the star graph*, arXiv:2003.05462 (2020), https://arxiv.org/abs/2003.05462 . Background for fixed-graph star probabilities; not alternating phases.
3. J. Svoboda, S. Joshi, J. Tkadlec, K. Chatterjee, *Amplifiers of selection for the Moran process with both Birth-death and death-Birth updating*, arXiv:2401.14914 (2024), https://arxiv.org/abs/2401.14914 . Different fixed-network amplification setting.
