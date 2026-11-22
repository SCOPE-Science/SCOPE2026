# A zero-entropy atomic system with infinite admissible return-time invariants

## Finding

The measure-theoretic return-time questions raised in Pannipitiya [1, Question 6.8] have a positive answer, including a separation between the mean and variance thresholds. For every real \(s>1\), there is a probability-preserving, invertible, countable atomic system of Kolmogorov–Sinai entropy zero with a **two-atom forward generating partition** whose maximal positive-overlap return time at depth \(n\) is **exactly \(n\)**. Writing \(A_n\), \(V_n\), and \(H_n\) for its weighted mean return time, return-time variance, and Shannon entropy, respectively, the following sharp trichotomies hold:

\[
\begin{aligned}
 A_n&\longrightarrow\infty &&\Longleftrightarrow\quad 1<s\le 2,\\
 V_n&\longrightarrow\infty &&\Longleftrightarrow\quad 1<s\le 3,\\
 H_n&\longrightarrow H_\infty<\infty &&\text{for every }s>1.
\end{aligned}
\]

At the boundaries, \(A_n=(\log n)/\zeta(2)+O(1)\) if \(s=2\), and \(V_n=(\log n)/\zeta(3)+O(1)\) if \(s=3\). Away from the boundaries, \(A_n=\Theta(n^{2-s})\) for \(1<s<2\), and \(V_n=\Theta(n^{3-s})\) for \(1<s<3\). Consequently both *system-level* normalized invariants \(\Lambda_\mu\) and \(\Lambda_{V,\mu}\) of [1] are infinite for \(1<s\le2\), while the canonical generating partition has finite limiting mean and divergent normalized variance for \(2<s\le3\).

More strongly, for every integer \(k\ge1\), the entire moment hierarchy has a critical exponent: \(\mathbb E[\tau_n^k]\) tends to \(\zeta(s-k)/\zeta(s)\) for \(s>k+1\), diverges as \(\Theta(n^{k+1-s})\) for \(1<s<k+1\), and equals \((\log n)/\zeta(k+1)+O(1)\) for \(s=k+1\).

## Assumptions and scope

Let \(\zeta(s)=\sum_{m\ge1}m^{-s}\). Take the disjoint union of cyclic orbits

\[
X=\{(m,j):m\in\mathbb N,\ 0\le j<m\},\quad
T(m,j)=(m,j+1\bmod m),\quad
\mu_s(\{(m,j)\})=\frac{1}{\zeta(s)m^{s+1}}.
\]

Every point has positive measure and \(T\) is an invertible, probability-preserving permutation. The binary partition \(\mathcal P=\{P_0,P_1\}\) records whether the point is at phase zero: \(P_1=\{(m,0):m\ge1\}\), and \(P_0=X\setminus P_1\). Its length-\(n\) forward join \(\mathcal P^{(n)}=\bigvee_{j=0}^{n-1}T^{-j}\mathcal P\) consists of finitely many nonempty binary word atoms.

For a positive-measure set \(B\), the *overlap return time* is

\[
\tau(B)=\min\{r\ge1:\mu_s(B\cap T^{-r}B)>0\}.
\]

For each \(x\in X\), let \(\tau_n(x)\) be the return time of its length-\(n\) word atom. The statistics are \(A_n=\int\tau_n\,d\mu_s\), \(V_n=\int(\tau_n-A_n)^2\,d\mu_s\), and \(H_n=-\sum_{B\in\mathcal P^{(n)}}\mu_s(B)\log\mu_s(B)\). The system-level \(\Lambda\) quantities are the suprema over admissible finite generating partitions of the limsup of \(A_n/(1+H_n)\) and \(V_n/(1+H_n)^2\), as defined in [1]. This theorem establishes their **infinite lower bounds** from the displayed partition, not global finiteness assertions in other regimes.

## Proof

**1. Generating property and finite entropy.** Along \((m,j)\), the observed symbol at time \(t\) equals one exactly when \(j+t\equiv0\pmod m\). Every forward word of length at least \(2m\) contains two consecutive marked positions at distance \(m\). That distance recovers the cycle length; one marked position recovers the phase. Therefore the forward joins distinguish any two points, so \(\mathcal P\) generates the complete atomic sigma algebra. Invariance is immediate from constant mass within each orbit. The Shannon entropy of the singleton partition is finite:

\[
H_\infty=\log\zeta(s)-(s+1)\frac{\zeta'(s)}{\zeta(s)}<\infty.
\]

The refined binary partitions increase to the singleton partition, so \(H_n\uparrow H_\infty\). Their entropy rate and hence the Kolmogorov–Sinai entropy is zero.

**2. The exact overlap rule.** If a word has at least two ones, it can be realized on only one orbit: the distance between its first two ones is the period \(m\). The word then determines one point in that orbit, so its overlap time is \(m\). If it contains exactly one one in position \(i\in\{0,\ldots,n-1\}\), it can occur on orbit \(m\) precisely when \(m\ge L_i:=\max\{i+1,n-i\}\); the unique point of that orbit in the atom returns after exactly \(m\) steps. Thus its shortest overlap time is \(L_i\). If the word is all zero, any orbit with \(m\ge n+2\) contains neighboring phase points that both realize the word, so the overlap time is one. These three cases give \(1\le\tau_n\le n\) at every point. The single-marker word beginning with one and followed by \(n-1\) zeros has return time \(n\), so

\[
\max_{B\in\mathcal P^{(n)}}\tau(B)=n.
\]

This is exactly the linear maximal-overlap bound required for return-time admissibility.

**3. Exact word-mass and moment formula.** The zero word has mass \(\zeta(s)^{-1}\sum_{m>n}(m-n)m^{-s-1}\). The single-marker word with the mark at position \(i\) has mass \(\zeta(s)^{-1}\sum_{m\ge L_i}m^{-s-1}\). For every \(m<n\), exactly \(\min(m,n-m)\) phase words have at least two marks; each is a singleton of mass \(1/(\zeta(s)m^{s+1})\). Therefore for every integer \(k\ge0\),

\[
\boxed{\mathbb E_{\mu_s}[\tau_n^k]=\frac1{\zeta(s)}\left[\sum_{m>n}\frac{m-n}{m^{s+1}}+\sum_{i=0}^{n-1}L_i^k\sum_{m\ge L_i}\frac1{m^{s+1}}+\sum_{m=1}^{n-1}\frac{\min(m,n-m)m^k}{m^{s+1}}\right].}
\]

These series are absolutely convergent for \(s>1\), and the identity includes the case \(n=1\).

**4. Moment thresholds.** Refinement of atoms makes \(\tau_n(x)\) nondecreasing in \(n\). A point of cycle length \(m\) has \(\tau_n(x)\le\min(m,n)\) and \(\tau_n(x)=m\) for all \(n\ge2m\). Hence \(\tau_n(x)\uparrow m\). For every \(k\ge1\),

\[
\frac1{\zeta(s)}\sum_{m\le\lfloor n/2\rfloor}m^{k-s}
\ \le\ \mathbb E[\tau_n^k]\ \le\
\frac1{\zeta(s)}\left(\sum_{m\le n}m^{k-s}+n^k\sum_{m>n}m^{-s}\right).
\]

Power-sum comparisons give \(\Theta(n^{k+1-s})\) for \(1<s<k+1\). For \(s=k+1\), the lower and upper bounds equal \((\log n)/\zeta(s)+O(1)\), since their harmonic sums differ by \(O(1)\) and the remaining upper tail is bounded. For \(s>k+1\), monotone convergence yields \(\zeta(s-k)/\zeta(s)\).

**5. Variance and global invariants.** For \(1<s<2\), the second moment is \(\Theta(n^{3-s})\), whereas \(A_n^2=O(n^{4-2s})=o(n^{3-s})\). At \(s=2\), \(A_n=O(\log n)\) and the second moment is \(\Theta(n)\). If \(s>2\), \(A_n\) is bounded. Thus the variance has the stated growth for every \(1<s<3\); at \(s=3\) its logarithmic coefficient comes entirely from the second moment. For \(s>3\),

\[
V_n\longrightarrow\frac{\zeta(s-2)}{\zeta(s)}-\left(\frac{\zeta(s-1)}{\zeta(s)}\right)^2.
\]

Because \(H_n\uparrow H_\infty<\infty\), diverging \(A_n\) or \(V_n\) gives an infinite normalized limsup for this admissible generating partition, and hence for the system-level supremum.

## Verification

The accompanying standalone `checker.py` uses exact rational point masses on finite truncations of this family. It independently enumerates all length-\(n\) atoms, computes overlap by explicit cyclic intersection, compares the three-case formula, tests the generating threshold, and checks the exact moment identity for several exponents. Invoke with `python3 checker.py` from the extracted package directory. The reported finite test results are reproducibility checks, not a substitute for the infinite proof in the preceding section.

## Relationship to prior work

Pannipitiya [1] introduced positive-measure overlap statistics, proved finite-atomic formulas and admissibility results, and explicitly asked in Question 6.8 whether zero-entropy or countable-atomic systems can have infinite normalized mean or variance. The present construction uses **one orbit of every positive length**, a power-law distribution of orbit masses, and a fixed two-symbol generator to answer the question constructively. Finite permutation formulas in [1] do not establish the infinite result: finite-support truncations have finite saturation times and the limits in refinement depth and orbit cutoff do not commute. Classical first-return/Kac identities concern individual-point recurrence or conditional first returns and do not imply the minimum positive-overlap time of partition atoms. Distinct recent topological cylinder-penetration studies use uniform counts of words rather than a fixed atomic invariant probability; their statements do not imply these weighted thresholds.

## Limitations

The system is nonatomic only in the limit of orbit size; each actual point has positive mass. It is not ergodic, compact, or mixing. Assertions of global infinite invariants follow from one admissible generator; no global upper bounds are asserted when \(s>2\) or \(s>3\). The published priority comparison is limited to the inspected sources, and a historical equivalent construction cannot be excluded without further independent literature review. The finite checker cannot prove infinite sums or assertions over all real \(s>1\). No independent mathematical audit has been performed.

## References

[1] D. N. Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems*, arXiv:2611.13416v1, first publicly posted 2026-11-10, especially Sections 5.1–5.9 and Question 6.8. https://arxiv.org/abs/2611.13416
