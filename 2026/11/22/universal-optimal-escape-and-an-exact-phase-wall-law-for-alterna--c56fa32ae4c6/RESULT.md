# Universal optimal escape and an exact phase-wall law for alternating binary Markov holes

## Finding
Let \((X_j)_{j\ge0}\) be a stationary Markov chain on \(\{0,1\}\) with strictly positive transition matrix
\[
P=\begin{pmatrix}a&1-a\\ b&1-b\end{pmatrix},\qquad 0<a,b<1.
\]
At each time \(t\ge0\), a prescribed hole \(h_t\in\{0,1\}\) kills a trajectory if \((X_t,X_{t+1})=(h_t,h_t)\). Write \(S_N(h)\) for the probability of avoiding all holes at times \(0,\ldots,N-1\). With \(q=1-a\), \(r=bq\), \(d=b+q\), and \(\gamma=(a+1-b)/d\), the alternating schedule \(h_t=t\bmod2\) has, for every integer \(n\ge0\), the exact laws
\[
S_{2n}=r^n(1+n\gamma),\qquad
S_{2n+1}=\frac{q}{d}r^n\bigl[1+b+n(a+1-b)\bigr].
\]
For **every** deterministic prescribed sequence of holes \(h\), whether periodic or not,
\[
\limsup_{N\to\infty}-\frac1N\log S_N(h)\le -\frac12\log[b(1-a)].
\]
Strict alternation attains this optimal asymptotic escape exponent. Among all **periodic** hole schedules it is the unique maximizer up to a time shift; any nonalternating periodic schedule has a strictly smaller escape exponent. There is no assertion that alternation minimizes survival at every finite horizon for general \(a,b\).

For the alternating schedule, condition on surviving \(2n\) transitions, and inspect the even-time skeleton \((X_0,X_2,\ldots,X_{2n})\). Every permitted skeleton either never changes state or changes **exactly once**, from \(1\) to \(0\). Conditional on this change occurring, its block index \(J_n\in\{0,\ldots,n-1\}\) is exactly uniform. Its probability of occurring given survival is
\[
\Pr(\text{one change}\mid\text{survive }2n)=\frac{n\gamma}{1+n\gamma}.
\]
In particular, \(J_n/n\) conditioned on survival and the change converges weakly to uniform distribution on \([0,1]\), while the probability of no change under survival is \(1/(1+n\gamma)\).

## Assumptions and scope
All parameters are real and strictly satisfy \(0<a<1\) and \(0<b<1\). The initial law is the unique stationary law \(\pi=(b/d,q/d)\), and holes are fixed in advance (no dependence on realized trajectories). Survival is measured for \(N\) transitions, not \(N\) positions. Periodic optimization is only for the exponential asymptotic rate, not a pointwise finite-time comparison or uniqueness among nonperiodic schedules. A time shift of alternation is the schedule \(h_t=1-(t\bmod2)\). The theorem concerns a Markov measure on the full binary shift, with primary subject classification 37B10.

## Proof
Define the substochastic transition matrices for forbidden adjacent words \(00\) and \(11\):
\[
K_0=\begin{pmatrix}0&q\\b&1-b\end{pmatrix},\qquad
K_1=\begin{pmatrix}a&q\\b&0\end{pmatrix}.
\]
With \(\mathbf1=(1,1)^T\), the Markov property gives the exact path sum
\[
S_N(h)=\pi K_{h_0}\cdots K_{h_{N-1}}\mathbf1.
\]
Both determinants equal \(-r\). Their alternating two-step product is
\[
B=K_0K_1=\begin{pmatrix}r&0\\ c&r\end{pmatrix},\qquad c=b(a+1-b)>0.
\]
The nilpotent part \(B-rI\) squares to zero. Consequently, for every \(n\ge0\),
\[
B^n=\begin{pmatrix}r^n&0\\nc r^{n-1}&r^n\end{pmatrix}
\]
(with the lower-left entry interpreted as zero at \(n=0\)). Multiplication by \(\pi\), \(\mathbf1\), and \(K_0\mathbf1=(q,1)^T\) proves the displayed even- and odd-time laws. Because \(\gamma>0\), the exponential decay per transition is exactly \(-\frac12\log r\), and the nontrivial size-two Jordan block gives a linear survival prefactor.

For an arbitrary deterministic schedule, \(M_N=K_{h_0}\cdots K_{h_{N-1}}\) is nonnegative and \(|\det M_N|=r^N\). If \(\lambda_1,\lambda_2\) are its complex eigenvalues, the spectral radius satisfies \(\rho(M_N)\ge\sqrt{|\det M_N|}=r^{N/2}\). Writing \(\pi_*=\min(\pi_0,\pi_1)>0\), positivity of entries yields
\[
S_N(h)\ge\pi_*\sum_{i,j}(M_N)_{ij}\ge\pi_*\rho(M_N)\ge\pi_* r^{N/2}.
\]
The middle inequality holds because the spectral radius is at most the maximum row sum, which is at most the sum of entries. Taking logarithms and a limsup proves the universal upper bound for the escape exponent.

For a periodic schedule of primitive period \(m\), write \(A=K_{h_0}\cdots K_{h_{m-1}}\). Each \(K_i\) is invertible, with nonzero row and column sums. If the cyclic word contains two consecutive equal symbols, cyclically conjugate the product to place the pair together. Both \(K_0^2\) and \(K_1^2\) have strictly positive entries; multiplication on either side by any further \(K_i\) preserves strict positivity. Thus \(A\) is similar to a strictly positive matrix. Its positive Perron eigenvalue \(\rho(A)\) is simple and strictly dominates the other eigenvalue in modulus, so \(\rho(A)>\sqrt{|\det A|}=r^{m/2}\). The strict inequality also holds for a period-one constant schedule because \(K_0^2\) and \(K_1^2\) are strictly positive. Moreover, the twofold product \(A^2\) is strictly positive whenever the cyclic hole schedule is nonalternating: its doubled word contains an equal adjacent pair, and all other factors have nonzero rows and columns. This guarantees a nonzero positive Perron coefficient in the survival probability. The stationary survival for \(km\) transitions is \(\pi A^k\mathbf1\) and has exponential rate \(-m^{-1}\log\rho(A)<-\frac12\log r\). If no neighboring symbols coincide cyclically, the periodic word must alternate and have even period. This completes the periodic uniqueness claim.

Finally, the two-state skeleton has transition-weight matrix \(B\). Its only positive transitions are \(0\to0\) of weight \(r\), \(1\to1\) of weight \(r\), and \(1\to0\) of weight \(c\); \(0\to1\) is impossible. For each block index \(j\) exactly one crossing has path weight
\[
\pi_1 r^j c r^{n-1-j}=\pi_1c r^{n-1}=\gamma r^n,
\]
independent of \(j\). The total no-crossing weight is \((\pi_0+\pi_1)r^n=r^n\). These terms sum to \(S_{2n}=r^n(1+n\gamma)\), proving all conditional laws and the uniform limit. Inside the crossing block the intermediate symbol is \(0\) or \(1\), with respective conditional weights \(a/(a+1-b)\) and \((1-b)/(a+1-b)\).

## Verification
The standalone `CHECK.py` performs 846 exact-rational consistency tests over five distinct strictly positive transition matrices. It checks the two-step matrix factorization, both survival identities for finite lengths, independent direct enumeration of allowed strings for all hole schedules up to six transitions, and equality of crossing-block weights. The infinite-parameter statements and periodic uniqueness are proved above rather than inferred from those finite tests. Reproduce with `python3 CHECK.py` using the Python standard library.

## Relationship to prior work
Agarwal, Cheriyath and Tikekar, *On Escape rate for subshift with Markov measure* (arXiv:2401.05118, first public 2024-01-10), obtain a spectral-radius formula for **fixed** unions of cylinder holes under Markov measures. Their operator method supplies context, but the explicit one-way Jordan product, determinant minimax comparison across **time-varying** binary holes, and conditional switching law require additional statements not contained in their inspected fixed-hole theorem. Bonanno et al.'s binary Markov cylinder formula, discussed in that paper's Section 4.3, likewise concerns fixed cylinder holes.

The publicly indexed findings *Sharp moving-hole escape envelopes and a zero-entropy alternating phase for the doubling map* (2026-11-02) and *Optimal alternating Markov-hole escape in integer expanding maps* (2026-11-08) already prove finite-time alternating optimality in the uniformly weighted Bernoulli/doubling setting. That covered **fair case is not claimed as new**. Here the scope is all strictly positive binary Markov matrices: finite-time optimality can fail and only the sharp universal **asymptotic** bound and periodic uniqueness survive, accompanied by exact nonuniform Markov coefficients and a conditional uniform crossing location. General random/time-dependent hole thermodynamic formalism provides conceptual background but does not by itself state these sharp explicit comparisons.

## Limitations
No pointwise finite-horizon minimum is asserted for arbitrary Markov transitions. For example, at \(a=b=99/100\), forbidding \(00\) twice yields smaller two-transition survival than alternately forbidding \(00\), then \(11\). The equality classification is for **periodic** schedules only; nonperiodic schedules may share the optimal exponential rate. The result does not characterize quenched stochastic hole switching, higher-order Markov sources, nonstationary initial laws, or all conditional path distributions. Earlier or otherwise unindexed equivalent theorems remain a publication-priority risk; indexed abstract comparisons cannot establish exhaustiveness of the research record.

## References
1. N. Agarwal, H. Cheriyath, S. N. Tikekar, *On Escape rate for subshift with Markov measure*, arXiv:2401.05118 (initial preprint 2024-01-10). https://arxiv.org/html/2401.05118v2
2. H. Cheriyath, N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767 (2019). https://arxiv.org/abs/1905.11767
3. J. Atnip, G. Froyland, C. Gonzalez-Tokman, S. Vaienti, *Thermodynamic Formalism and Perturbation Formulae for Quenched Random Open Dynamical Systems*, arXiv:2307.00774 (2023). https://arxiv.org/abs/2307.00774
4. *Sharp moving-hole escape envelopes and a zero-entropy alternating phase for the doubling map* (public finding, 2026-11-02). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-moving-hole-escape-envelopes-and-a-zero-entropy-alternatin--91c8d26540fd
5. *Optimal alternating Markov-hole escape in integer expanding maps* (public finding, 2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-alternating-markov-hole-escape-in-integer-expanding-maps--962cd78c291c
