# Eulerian necklace clocks and uniform basins for sequential Rule 170

## Finding
Let \(n\ge3\), let \(\pi\) be any permutation of the sites of an indexed binary ring, and let \(F_\pi\) be one full in-place sequential sweep of elementary Rule 170 (the site about to be updated copies its currently visible clockwise neighbor). Write \(t_i\) for the visit rank of site \(i\), and define
\[
S_\pi=\{i\in\mathbb Z/n\mathbb Z:t_{i-1}<t_i\},\qquad k=|S_\pi|.
\]
Then \(1\le k\le n-1\), and **every** initial state becomes periodic after at most one sweep. The exact recurrent core has \(2^k\) states and is conjugate to the cyclic rotation of \(k\) independent bits, indexed by the cyclically ordered sites in \(S_\pi\). Consequently the sharp one-sweep transient shell has \(2^n-2^k\) states.

Define the classical primitive binary-word count
\[
A_p=\sum_{d\mid p}\mu(p/d)2^d.
\]
For any \(p\ge1\), the number of primitive temporal period-\(p\) recurrent *states* equals \(A_p\) when \(p\mid k\), and zero otherwise. Thus the primitive temporal-orbit count is \(A_p/p\). Every recurrent state has exactly \(2^{n-k}\) immediate preimages, so **every individual period-\(p\) orbit has the same basin size** \(p2^{n-k}\); the number of initial states ultimately attaining period \(p\) is \(2^{n-k}A_p\) if \(p\mid k\), and zero otherwise.

Writing \(\left\langle{m\atop j}\right\rangle\) for an Eulerian number counting permutations of \(m\) elements with \(j\) ordinary ascents, the number of labelled full-sweep schedules with given \(k\) is precisely
\[
\boxed{n\left\langle{n-1\atop k-1}\right\rangle.}
\]
In particular exactly \(n\) of the \(n!\) sequential update permutations force all initial configurations to become fixed after one sweep. More generally, the **exact joint schedule/initial-state period census** is
\[
\boxed{\#\{(\pi,x):|S_\pi|=k,\;\operatorname{per}(x)=p\}
=n\left\langle{n-1\atop k-1}\right\rangle 2^{n-k}A_p\,\mathbf1_{p\mid k}.}
\]
For a uniformly random update permutation, independent of a uniformly random initial configuration, the eventual period \(P_n\) satisfies
\[
\boxed{\frac{P_n-n/2}{\sqrt{n/12}}\ \Longrightarrow\ \mathcal N(0,1),}
\]
indeed \(\Pr(P_n\ne |S_\pi|)\to0\) exponentially fast. All periods count **full sequential sweeps**, not individual site updates.

## Assumptions and scope
Sites are \(\mathbb Z/n\mathbb Z\), with binary labels; at a visit to site \(i\), its current bit is replaced by the *current* bit at site \(i+1\), while other bits remain untouched. Exactly one visit per site occurs in the fixed permutation \(\pi\), repeated on every subsequent sweep. The transition is neither parallel Rule 170 nor sequential Rule 150. The attraction basin of an orbit includes its recurrent phases and all preperiodic ancestors. Spatial rotations are not identified, except that binary necklaces naturally parameterize temporal orbits within the recurrent core.

## Proof
**Copy-source lemma.** Track not binary values but their source-site labels throughout one sweep. Suppose site \(i\) has been visited: it copies source at \(i+1\). If site \(i+1\) has not yet been visited, that source is \(i+1\); otherwise continue to \(i+2\), and so forth. The chain terminates exactly at the first clockwise site \(s\) for which its predecessor is visited *earlier* than \(s\), i.e. \(s\in S_\pi\). Such an \(s\) must exist: a strict cyclic increase of all \(n\) visit ranks is impossible. This proves that after the sweep
\[
 F_\pi(x)_i=x_{\operatorname{next}_{S_\pi}(i)},
\]
where \(\operatorname{next}_{S_\pi}(i)\) is the first member of \(S_\pi\) encountered strictly clockwise from \(i\), including \(i\) itself only after a complete turn. The same argument shows \(S_\pi\) cannot be empty or all sites: both situations would force a cyclic chain of strict inequalities.

**Rotation and basins.** Write the members of \(S_\pi\) in clockwise order as \(s_1,\ldots,s_k\). The displayed formula makes the output constant on each clockwise block \(s_j,s_j+1,\ldots,s_{j+1}-1\), taking the freely chosen input bit at \(s_{j+1}\). Exactly \(k\) source coordinates are used, and each can be assigned independently: hence the image consists of exactly \(2^k\) block-constant words. On this image, the value at site \(s_j\) after the next sweep is the previous value at site \(s_{j+1}\). Therefore the image is invariant, and the restriction of \(F_\pi\) to it is the invertible length-\(k\) binary rotation. Thus the image is precisely the periodic set, all remaining \(2^n-2^k\) states enter it in one sweep, and the one-sweep map is uniform-to-one on its image with multiplicity \(2^{n-k}\).

**Primitive periods.** The set of binary length-\(k\) words fixed by rotation by \(p\) has cardinality \(2^{\gcd(k,p)}\). Divisor Möbius inversion yields \(A_p=\sum_{d\mid p}\mu(p/d)2^d\) exactly when \(p\mid k\); dividing by \(p\) gives temporal orbits. Each orbit contains \(p\) distinct image states, each with a disjoint fiber of \(2^{n-k}\) initial words; this establishes the individual basin size and all initial-period counts. In particular a primitive length-\(k\) binary word exists for any \(k\ge2\) (one single one, the rest zero), so each schedule actually realizes temporal period \(k\).

**Eulerian frequency.** Let \(t_0,\ldots,t_{n-1}\) be the visit ranks arranged in spatial cyclic order. The number \(k\) is the number of cyclic ascents \(t_{i-1}<t_i\). Every cycle of cyclic shifts of such an ordering has exactly \(n\) distinct rooted representatives, and one representative has its maximum rank at the final position. In that representative the cyclic-ascent count equals one plus the ordinary ascent count of the preceding \(n-1\) entries. There are \(\left\langle{n-1\atop k-1}\right\rangle\) such representatives. Multiplication by \(n\) gives the schedule frequency and the exact joint census. In particular \(k=1\) occurs in \(n\) schedules.

**Random scheduling.** Cyclic ascents of a uniformly random rank permutation have the same distribution as cyclic comparisons of independent continuous random variables. Each comparison has mean \(1/2\), variance \(1/4\); nonadjacent comparisons are independent, and each adjacent pair has covariance \(-1/12\). Thus \(\mathbb E k=n/2\), \(\operatorname{Var}k=n/12\), and the bounded one-dependent central limit theorem yields \((k-n/2)/\sqrt{n/12}\Rightarrow\mathcal N(0,1)\). Conditional on \(k\), a uniform initial configuration induces a *uniform* binary core word. If its least rotation period is a proper divisor of \(k\), that period is at most \(k/2\); a union bound over proper divisors gives \(\Pr(P_n\ne k\mid k)\le k2^{-k/2}\). A standard bounded-differences or one-dependent concentration bound gives \(\Pr(k<n/4)\le e^{-cn}\) for some absolute \(c>0\). Consequently \(\Pr(P_n\ne k)\le e^{-c'n}\) for some \(c'>0\), and the period central limit theorem follows by Slutsky's theorem.

## Verification
`verification/verify_formula.py` independently tracks actual symbolic copy-sources through **every** permutation for ring sizes \(3\) through \(8\), compares against the clockwise next-ascent rule, counts all Eulerian schedule classes, and verifies primitive necklace identities through length \(24\). `verification/check_exhaustive.py` independently simulates the actual bitwise asynchronous update for **every** initial state under **every** scan order on rings of sizes \(3\) through \(7\); it computes cycle entrance and least period from the resulting functional graph and compares every count. Both programs use only the Python standard library. Their run outputs are included, but the all-\(n\) claims follow from the analytic copy-source proof, not finite tests.

## Relationship to prior work
Macauley, McCammond and Mortveit (2007) study order independence of periodic points under asynchronous cellular automata and classify rules with schedule-independent periodic sets; Rule 170 is outside that class. De Oliveira et al. (2020) examine ECA sensitivity to update schedules, explicitly including Rule 170 and proving that different block schedules produce different maps, rather than an exact full-permutation recurrent census. Donoso-Leiva et al. (2025) exhibit an update order that makes Rule 170 converge to consensus, but do not count all such orders or the other necklace clocks and basins. Published results on sequential Rule 150 provide Eulerian scan classes and exact invertible dynamics, whereas Rule 170 has a collapsing \(2^k\)-state core and equal per-orbit basins. A published bi-threshold cycle model also rotates binary necklaces after one sweep, but has a fixed scan and distinctly **nonuniform**, run-dependent basin sizes. These claims do not imply the exact Rule 170 theorem, although the use of Eulerian numbers, Möbius inversion and rotation combinatorics is classical.

## Limitations
The theorem assumes precisely one visit to every site in each repeated scan, and the binary copy-right local rule. It does not cover arbitrary block-parallel schedules, stochastic changes of order between sweeps or other elementary rules. The Gaussian statement concerns the distribution over *scan orders*, not randomness in a fixed scan beyond its initial bits. A relevant 2025 study of general (a)synchronism was not available in full via accessible preprint, open-access and institutional routes, leaving historical-priority uncertainty about possible related maximal-period observations. No independent mathematical audit has been performed.

## References
- M. Macauley, J. McCammond, H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, first public version July 16, 2007, https://arxiv.org/abs/0707.2360 ; full text https://web.math.ucsb.edu/~mccammon/papers/wolfram.pdf .
- P. P. B. de Oliveira, E. Formenti, K. Perrot, S. Riva, E. L. P. Ruivo, *Non-maximal sensitivity to synchronism in periodic elementary cellular automata: exact asymptotic measures*, first version April 15, 2020, https://arxiv.org/abs/2004.07128 .
- I. Donoso-Leiva, E. Goles, M. Ríos-Wilson, S. Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, September 9, 2025, https://arxiv.org/abs/2509.07797 .
- *Impact of (a)Synchronism on ECA: Towards a New Classification*, 2025, https://arxiv.org/abs/2505.10645 (full text not obtained).
- *Scan-order phase diagram and exact Rule 150 cycle census on binary rings*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-scan-order-phase-diagram-and-exact-rule-150-cycle-census-on-bina--a8edc73752da .
- *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binary-necklace-attractors-and-triangular-run-basins-for-sequent--e79a108b9794 .
