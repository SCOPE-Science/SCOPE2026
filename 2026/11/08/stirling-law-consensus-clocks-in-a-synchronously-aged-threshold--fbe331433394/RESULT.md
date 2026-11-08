# Stirling-law consensus clocks in a synchronously aged threshold cascade on a path

## Finding

An irreversible, endogenously aged threshold cascade on a path has an **exact finite-round law given by unsigned Stirling numbers of the first kind**. Its consensus time is almost surely finite but has infinite mean on every nontrivial path. As the number of initially nonadopting vertices grows, its *logarithm* has a Gaussian limit centered at the path length: typical consensus times increase exponentially with depth.

For the process defined below, write \(c(n,k)\) for the number of permutations of \(\{1,\ldots,n\}\) with exactly \(k\) cycles, with \(c(n,k)=0\) when \(k>n\). Then for all integers \(m\ge1\), \(t\ge0\), and \(0\le k<m\),

\[
\Pr(K_t=k)=\frac{c(t+1,k+1)}{(t+1)!},\qquad
\Pr(T_m>t)=\frac{1}{(t+1)!}\sum_{j=1}^{m}c(t+1,j).
\]

The absorbing probability is the complementary sum over \(j\ge m+1\). More strongly, \(K_t\) has the distribution of \(\min\{m,C_{t+1}-1\}\), where \(C_n\) counts the cycles in a uniformly random permutation of \(n\) labels. Consequently, for each **fixed** \(m\),

\[
\Pr(T_m>t)\sim\frac{(\log t)^{m-1}}{(m-1)!\,t}\quad(t\to\infty),\qquad
\mathbb E[T_m^r]<\infty\iff 0<r<1.
\]

The displayed moment criterion is for **positive real orders** \(r>0\). In the complementary **large-depth** limit,

\[
\frac{\log T_m-m}{\sqrt m}\ \Rightarrow\ \mathcal N(0,1)
\quad(m\to\infty),
\qquad \frac{\log T_m}{m}\xrightarrow{\mathsf P}1.
\]

In particular, for every fixed real \(x\), the probability of having completed the cascade by \(\lfloor\exp(m+x\sqrt m)\rfloor\) rounds tends to the standard-normal distribution function \(\Phi(x)\).

## Assumptions and scope

Let \(P_{m+1}\) have vertex set \(\{0,1,\ldots,m\}\), with edges between consecutive integers, and let \(m\ge1\). At time zero, vertex \(0\) is permanently adopted and all other vertices are nonadopters. Fix a homogeneous **strict** fractional adoption threshold \(0<\theta<1/2\).

The clock is discrete and synchronous: in each round \(s=0,1,2,\ldots\), every nonadopter independently receives one activation opportunity with probability \(p_s=1/(s+2)\), independent of prior rounds and other vertices. Activated nonadopters adopt precisely when the fraction of adopted adjacent vertices **at the beginning of the round** exceeds \(\theta\). Otherwise they remain nonadopters. Adoptions are irreversible. All nonadopters start with endogenous age zero and age one unit after each unsuccessful round, whether activated or not. Thus their age at the beginning of round \(s\) equals \(s\); after adoption their age is immaterial.

Let \(K_t\) denote the number of vertices \(1,\ldots,m\) adopted after \(t\) completed rounds, and \(T_m=\inf\{t\ge0:K_t=m\}\). These definitions differ deliberately from the original study's **random asynchronous Monte Carlo** update convention. This theorem is about a precisely stated synchronous one-opportunity-per-node variant of its endogenous-age activation rule, not an asserted exact law for asynchronous Monte Carlo time. Below, \(\Rightarrow\) is convergence in distribution.

## Proof

**1. Prefix reduction.** Initially the adopted vertices are the prefix \(\{0\}\). If the prefix is \(\{0,\ldots,k\}\) with \(k<m\), vertex \(k+1\) is the only nonadopter with any adopted neighbor. For \(k+1<m\) it has two neighbors, exactly one adopted, so its adopted-neighbor fraction is \(1/2>\theta\). For \(k+1=m\) it is a leaf, with fraction \(1>\theta\). Every other nonadopter has adopted-neighbor fraction zero. As the round's state is frozen for all adoption decisions, **at most one vertex can be added in one round**. Inductively, the adopted set remains a prefix and, conditional on \(K_s=k<m\),

\[
\Pr(K_{s+1}=k+1\mid K_s=k)=\frac1{s+2},\quad
\Pr(K_{s+1}=k\mid K_s=k)=1-\frac1{s+2}.
\]

No negative transition is possible; \(m\) is absorbing.

**2. Independent Bernoulli coupling.** Introduce independent variables \(B_j\sim\operatorname{Bernoulli}(1/j)\) for all \(j\ge2\). Coupling the Bernoulli test of the currently exposed frontier in round \(s\) with \(B_{s+2}\) yields, simultaneously for all \(t\),

\[
K_t=\min\left\{m,\sum_{j=2}^{t+1}B_j\right\}.
\]

Independence holds because each round uses independent fresh activation opportunities and only the exposed frontier's coin can alter the prefix. The equality is a coupling identity, not merely matching means.

**3. Permutation cycles and the full finite-time law.** By inserting the highest new label into a uniformly random permutation, independently at size \(j\), that label creates a new cycle with probability \(1/j\), otherwise it joins one of the existing cycles. Thus \(C_n\), the cycle count of a uniform random permutation of \(n\) labels, admits the independent Bernoulli representation

\[
C_n\overset d=1+\sum_{j=2}^{n}B_j.
\]

This is a standard classical result, not a newly claimed permutation theorem. Because \(\Pr(C_n=k)=c(n,k)/n!\), substituting \(n=t+1\) in the prefix coupling proves both exact displayed probability formulas, including the conventions for \(t=0\), \(m=1\), and sums with \(m>t+1\).

**4. Almost-sure completion, fixed-depth tail and moments.** The independent success probabilities obey \(\sum_{j=2}^{\infty}1/j=\infty\). By the second Borel–Cantelli lemma there are almost surely infinitely many successes, hence \(T_m<\infty\) for every fixed finite \(m\).

For every fixed integer \(k\ge1\), the unsigned Stirling recurrence

\[
c(n,k)=(n-1)c(n-1,k)+c(n-1,k-1)
\]

implies, after dividing by \((n-1)!\), and induction over \(k\),

\[
\frac{c(n,k)}{(n-1)!}\sim\frac{(\log n)^{k-1}}{(k-1)!}.
\]

The base case is \(c(n,1)=(n-1)!\). For the induction step, the scaled recurrence says that the increase from size \(n-1\) to size \(n\) is \(c(n-1,k-1)/[(n-1)(n-2)!]\), asymptotically \((\log n)^{k-2}/[(k-2)!(n-1)]\), whose partial sum is \((\log n)^{k-1}/(k-1)!\) by harmonic summation. For fixed \(m\), the term \(k=m\) therefore dominates the exact survival sum, yielding the displayed tail. For positive moment orders \(r>0\), the tail-sum integral criterion gives \(\mathbb E T_m^r<\infty\) for exactly \(0<r<1\), since the borderline \(r=1\) integral has a nonintegrable \((\log t)^{m-1}/t\) tail. In particular \(\mathbb E T_m=\infty\) for every \(m\ge1\).

**5. Gaussian logarithmic large-depth law.** The independent cycle-increment representation has mean \(\mathbb E C_n=H_n=\log n+O(1)\), variance \(\operatorname{Var}(C_n)=H_n-H_n^{(2)}=\log n+O(1)\), and bounded summands. Lindeberg's condition holds automatically, so

\[
\frac{C_n-\log n}{\sqrt{\log n}}\Rightarrow\mathcal N(0,1).
\]

For a fixed real \(x\), put \(t_m=\lfloor e^{m+x\sqrt m}\rfloor\), which is positive for all sufficiently large \(m\). The exact coupling gives

\[
\Pr(T_m\le t_m)=\Pr(C_{t_m+1}\ge m+1).
\]

At this choice of \(t_m\), \(\log(t_m+1)=m+x\sqrt m+o(1)\), and the standardized cycle-count threshold tends to \(-x\). Therefore \(\Pr(T_m\le t_m)\to\Phi(x)\), which is precisely \((\log T_m-m)/\sqrt m\Rightarrow\mathcal N(0,1)\). Tightness of the normalized logarithm implies \(\log T_m/m\xrightarrow{\mathsf P}1\).

## Verification

Run \(\texttt{python verify.py}\) with Python 3 and no third-party packages. It computes the independent finite-state prefix Markov chain using \(\texttt{fractions.Fraction}\), compares all state probabilities with unsigned-Stirling predictions for \(1\le m\le9\) and \(0\le t\le60\), and independently enumerates the cycle counts of all permutations through size eight. It passed 3,887 exact equalities and exhaustive finite permutations (\(\texttt{VERIFY\_OK}\)). The proof above, not finite computation, establishes the universal identities, asymptotic statements and moment cutoff.

## Relationship to prior work

Abella, San Miguel and Ramasco (2022/2023) introduce the endogenous-aging threshold process, the same inverse-age activation function and network-level cascade slowdown. Their published analysis treats the random asynchronous Monte Carlo process on random networks and a lattice, using approximations and simulation; it does not give the finite-round path distribution under the *explicitly different synchronous protocol* stated here.

The independent Bernoulli description of uniform-permutation cycles (Feller coupling) and their Gaussian limit are classical. The new content asserted here is their exact **model-specific** realization as the entire finite-time adoption law of the synchronous threshold path, together with its sharp completion-time moment and network-depth laws. A previously available continuous-time inverse-age threshold-path analysis already covers comparable fixed-length long-time tail behavior; the finite-round Stirling identity and depth-scaling law are different assertions, not deductions merely by changing notation or time units.

## Limitations

These claims concern a fixed-seed simple path, homogeneous thresholds \(0<\theta<1/2\), synchronized frozen-state rounds and globally aged independent per-vertex activations. They do **not** cover random asynchronous Monte Carlo time, heterogeneously reset endogenous ages, cyclic graphs, thresholds at or above \(1/2\), exogenous aging, or nonirreversible adoption. The exact finite-time formulas do not imply corresponding laws for a different update schedule. The classical probability and permutation theorems used in the proof are not claimed to be new. Unindexed equivalent model-specific literature remains a publication-priority risk. This work has not undergone independent external audit.

## References

1. D. Abella, M. San Miguel and J. J. Ramasco, *Aging in binary-state models: The Threshold model for Complex Contagion*, arXiv:2209.05990 (first public version 13 September 2022); *Physical Review E* **107**, 024101 (2023), DOI:10.1103/PhysRevE.107.024101. https://arxiv.org/abs/2209.05990
2. J. Najnudel and J. Pitman, *Feller coupling of cycles of permutations and Poisson spacings in inhomogeneous Bernoulli trials*, arXiv:1907.09587. https://arxiv.org/abs/1907.09587
3. D. Abella et al., *Ordering dynamics and aging in the symmetrical threshold model*, arXiv:2307.02977. https://arxiv.org/abs/2307.02977 (a different reversible model considered for overlap).
