# A Fibonacci consensus basin and exact relaxation shells in pinned majority dynamics

## Finding
Consider the synchronous three-site binary majority map on a cyclic ring of \(n\ge3\) indexed sites, with **site zero permanently pinned to zero** while every other site takes the majority of its previous, present, and next site values. Write \(\tau(x)\) for the first update at which the evolving configuration is fixed; pinned-zero initial states are counted once each, so there are \(2^{n-1}\) possible initial states.

For any integer \(t\ge0\), put \(L=2t+1\), define
\[
S_L^+(z)=\sum_{j=0}^{L}z^j,\qquad S_L^-(z)=\sum_{j=0}^{L}(-z)^j,
\]
and let \(A_n(t)\) count initial configurations with \(\tau(x)\le t\). Then **every finite-size, finite-time relaxation population** is determined by the exact formal generating function
\[
\boxed{\sum_{n\ge0}A_n(t)z^n=\frac12\left(\frac{S_L^+(z)}{1-zS_L^+(z)}+\frac{S_L^-(z)}{1-zS_L^-(z)}\right).}
\]
The length-zero coefficient is a formal convenience; physical assertions concern \(n\ge3\). The exact population first becoming fixed at step \(t\ge1\) is \(A_n(t)-A_n(t-1)\), while \(A_n(0)\) counts fixed starting states. **No nontrivial recurrent cycles occur.** The sharp maximum fixation time and the number of starts attaining it are
\[
\boxed{\max_x\tau(x)=\lfloor n/2\rfloor,\qquad
\#\{x:\tau(x)=\lfloor n/2\rfloor\}=\begin{cases}1&n\text{ even},\\2&n\text{ odd}.\end{cases}}
\]
In addition, the **complete basin of the all-zero fixed configuration**, not merely its one-step predecessors, has cardinality
\[
\boxed{B_n=F_{n+1}},
\]
where \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\) are Fibonacci numbers. In particular, for uniform independent initial opinions on the \(n-1\) unpinned sites, the precise probability that the pinned opinion ultimately becomes unanimous is
\[
\boxed{\Pr(\text{eventual all-zero})=\frac{F_{n+1}}{2^{n-1}}
\sim\frac{2\varphi}{\sqrt5}\left(\frac\varphi2\right)^n},\quad
\varphi=\frac{1+\sqrt5}{2}.
\]
For example, on \(n=8\), the numbers of starts fixing at times \(0,1,2,3,4\) are respectively \(27,77,20,3,1\); 34 of the 128 initial configurations eventually reach all zero. The Fibonacci basin and full time distribution are the asserted refinements of previously known fixed-boundary orbit-type and worst-case-time statements.

## Assumptions and scope
Sites are labelled \(0,1,\ldots,n-1\) modulo \(n\). Each \(x_i\in\{0,1\}\); the initial bit at site zero is zero and remains zero by an imposed boundary control. The other sites update simultaneously as
\[
(Fx)_i=\operatorname{maj}(x_{i-1},x_i,x_{i+1})\ (1\le i<n),\qquad (Fx)_0=0,
\]
where \(\operatorname{maj}\) is one precisely when at least two of the three arguments are one. No site or color symmetries are quotiented. The model is identical to Rule 232 on an open string of \(n-1\) dynamical cells with two fixed zero boundary values. The first-fixation time is \(\tau(x)=\min\{t\ge0:F^{t+1}x=F^tx\}\), not the time of the last individual bit flip. The generating function is over all lengths at a **fixed** threshold \(t\); the asymptotic probability is for \(n\to\infty\) with uniform unpinned bits.

## Proof
**Wall-word bijection and local update.** Set \(w_i=x_i\oplus x_{i+1\bmod n}\), with \(\oplus\) addition modulo two. Its binary Hamming weight is even because it telescopes around the cycle. Conversely, every even-weight length-\(n\) binary word \(w\) uniquely determines the configuration with \(x_0=0\), by successively taking \(x_{i+1}=x_i\oplus w_i\). Thus pinned configurations and even-weight wall strings are bijective, not two-to-one.

For an unpinned site, majority flips its central bit exactly when its two incident wall bits are both one. Hence the flip indicator at site \(i\ne0\) is \(w_{i-1}w_i\); by the pinning condition, the flip indicator at site zero is **zero**. Writing \(w'\) for walls after one simultaneous step gives
\[
\begin{aligned}
w'_0&=w_0(1\oplus w_1),\\
w'_i&=w_i(1\oplus w_{i-1}\oplus w_{i+1})\qquad (1\le i\le n-2),\\
w'_{n-1}&=w_{n-1}(1\oplus w_{n-2}).
\end{aligned}
\]
Equivalently, use the uniform middle formula with **virtual zero boundary walls** \(w_{-1}=w_n=0\). These two virtual zeros distinguish the pinned problem from the unpinned cyclic majority rule: the actual walls are a **linear word**, not a cyclic string, for purposes of erosion.

**Exact erosion and fixation time.** Each zero wall remains zero. Every maximal run of \(r\) consecutive one walls shrinks by one wall at each end at every iteration while its length is at least two; an isolated one wall stays fixed. The virtual zero boundaries ensure this is true even for runs touching the endpoints of the wall word. Thus a run of length \(r=2k\) vanishes after exactly \(k\) steps, while a run of length \(r=2k+1\) leaves exactly one stable central wall after \(k\) steps. A configuration is fixed exactly when no two adjacent actual walls are one, because these and only these pairs produce unpinned-site flips. Therefore
\[
\boxed{\tau(x)=\max_{\text{maximal linear one-runs }R\text{ in }w}\left\lfloor\frac{|R|}{2}\right\rfloor},
\]
with the maximum of the empty collection zero. Every orbit reaches a fixed configuration: no alternate periodic attractor survives.

**All-length time census.** The previous formula gives \(\tau(x)\le t\) precisely when every maximal one-run of its wall word has length at most \(L=2t+1\). Introduce a weight \(u\) for each one wall and a length variable \(z\). The generating polynomial for a permitted one-run is \(S_L(u,z)=\sum_{j=0}^{L}(uz)^j\). Every permitted finite word is uniquely decomposed as an initial permitted one-run followed by any number of pairs consisting of one zero and another permitted one-run. The resulting generating series is the exact identity
\[
G_L(u,z)=\frac{S_L(u,z)}{1-zS_L(u,z)}.
\]
Since each admissible pinned configuration corresponds to **one even-weight** wall string, parity extraction yields
\[
\sum_{n\ge0}A_n(t)z^n=\frac{G_L(1,z)+G_L(-1,z)}2.
\]
This is the displayed cumulative formula for every integer \(n,t\) and provides all exact first-entry shells by subtraction.

**Terminal layer.** All runs have length at most \(n\), so \(\tau\le\lfloor n/2\rfloor\). If \(n=2m\), a wall string with fixation time \(m\) must contain one-run length \(2m\), hence must be \(1^{2m}\), which has even weight and determines exactly one pinned configuration. If \(n=2m+1\), a wall string requiring time \(m\) must have a run of length at least \(2m\). Even weight excludes \(1^{2m+1}\); therefore its run has length exactly \(2m\) and the one zero must be at either endpoint. Exactly two such words exist. The final-time result follows and demonstrates sharpness.

**Entire consensus basin.** The final pinned configuration is all zero iff the terminal wall word has no surviving one. A run leaves a surviving wall iff its original length was odd. Thus precisely those initial wall words in which **every maximal one-run has even length** reach all zero. Every such word automatically has even total weight and therefore corresponds to exactly one allowed initial state. The admissible one-run generating series is \(S(z)=1+z^2+z^4+\cdots=1/(1-z^2)\), so the complete length generating function is
\[
\sum_{n\ge0}B_nz^n=\frac{S(z)}{1-zS(z)}=\frac1{1-z-z^2}.
\]
Its coefficients are exactly \(F_{n+1}\). There are \(2^{n-1}\) initial states, so the uniform probability formula follows. Finally Binet's formula \(F_{n+1}=(\varphi^{n+1}-(-\varphi)^{-n-1})/\sqrt5\) gives the displayed asymptotic. This proves every part of the finding. \(\square\)

## Verification
The standalone `verification/prove_run_enumerator.py` computes the exact coefficient recurrences of both rational series with integer arithmetic, independently enumerates even-weight binary wall strings for all lengths three through sixteen and every relevant time, and verifies Fibonacci consensus-basin counts and final-layer multiplicities; it exits with `ENUMERATOR_OK`. Independently, `verification/direct_dynamics.py` enumerates all pinned initial configurations for lengths three through fifteen, simulates the majority rule until fixation, compares observed first-fixation times and full histograms with the wall-run formula and cumulative wall counts, and counts all-zero basins. Its final line is `DYNAMICS_OK`. The finite exhaustive tests are reproducible checks, while the unrestricted assertions follow from the wall-word bijection and regular-language generating functions, not numerical extrapolation.

## Relationship to prior work
Inokuchi and Sato (2000) explicitly study the **same** Rule 232 automaton under fixed zero-zero boundary conditions, giving the qualitative fixed-point-only result, a recurrence for fixed-point numbers and sharp maximum transient lengths in Theorem 3.90 and nearby Lemma 3.88. Those assertions are acknowledged as prior, **not** new. They do not provide the complete time-resolved population at every \(n,t\), nor the full basin size of the all-zero fixed state. Tosic and Agha (2004) classify broad parallel/sequential majority configurations rather than the pinned system's exact per-time histogram or all-zero basin. Nakar and Ron (2022) investigate spatial structure on cyclic majority automata, not immutable-site controlled strings. The previously published complete relaxation census for **unpinned cyclic** Rule 232 uses a circular wall-word transfer trace and does not itself imply the present linear-wall generating function: the pin removes the all-one-wall two-cycle, changes the terminal layer, and leaves a unique initial-spin reconstruction rather than the unpinned two-to-one reconstruction. The classical local erosion mechanism itself is not claimed as novel. Fukś (1997) analyzes Rule 232 in a two-rule density-classification scheme, not the exact pinned-basin law.

## Limitations
This is a single pinned-zero site with synchronous three-site majority and no noise, weighted ties, sequential updates, or competing permanent opinions. The count \(F_{n+1}\) is for the entire all-zero basin, not the number of fixed configurations. The worst-case first-fixation time and qualitative absence of cycles are already covered by Inokuchi and Sato and are included to contextualize the **new** full transient distribution and basin formula. The proof does not address arbitrary locations of multiple pins or biased initial-state distributions. Exact priority against inaccessible monographs, unindexed sources, or equivalent run-avoidance formulas remains uncertain; there is no independent external scientific audit.

## References
- H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, first arXiv public version 1997-03-07, https://arxiv.org/abs/comp-gas/9703001.
- S. Inokuchi and T. Sato, *On Limit Cycles and Transient Lengths of Cellular Automata with Threshold Rules*, *Bulletin of Informatics and Cybernetics* **32** (2000), 23–60, especially Section 3.37, Lemma 3.88 and Theorem 3.90; https://doi.org/10.5109/13492 and https://www.researchgate.net/publication/31908320_ON_LIMIT_CYCLES_AND_TRANSIENT_LENGTHS_OF_CELLULAR_AUTOMATA_WITH_THRESHOD_RULES.
- P. T. Tosic and G. A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI (2004), https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
- Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv first public version 2022-05-18, https://arxiv.org/abs/2205.08972.
- *Exact stabilization-time distribution for the cyclic three-site majority automaton*, previously published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-stabilization-time-distribution-for-the-cyclic-three-site--ea6170529cae.
