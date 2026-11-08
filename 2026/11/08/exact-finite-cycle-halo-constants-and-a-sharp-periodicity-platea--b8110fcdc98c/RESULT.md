# Exact finite-cycle halo constants and a sharp periodicity plateau

## Finding
For an integer \(N\ge2\) let \(T\colon\mathbb Z/N\mathbb Z\to\mathbb Z/N\mathbb Z\) be the cyclic permutation \(T(j)=j+1\), with uniform probability measure. For a nonempty \(E\subset\mathbb Z/N\mathbb Z\), \(0<\alpha<1\), and each phase \(j\), set
\[
 M_E(j)=\sup_{L\ge1}\frac1L\sum_{q=0}^{L-1}\mathbf1_E(T^qj),\qquad H_\alpha(E)=\{j:M_E(j)>\alpha\}.
\]
The optimal restricted weak-type (halo) constant has the following **exact formula for every** \(N\) and \(\alpha\):
\[
 \boxed{C_N(\alpha):=\max_{\emptyset\ne E\subset\mathbb Z/N\mathbb Z}\frac{|H_\alpha(E)|}{|E|}=\max_{1\le k\le N}\frac{\min\{N,\lceil k/\alpha\rceil-1\}}{k}.}
\]
More precisely, among every \(k\)-point set, the maximum halo size is \(\min\{N,\lceil k/\alpha\rceil-1\}\), **attained by any block of \(k\) consecutive phases**. The exact endpoint matters because the maximal-function inequality is strict.

These constants have a sharp finite-period plateau and a discontinuity:
\[
 \boxed{C_N(\alpha)=1\quad\Longleftrightarrow\quad\frac{N-1}{N}\le\alpha<1.}
\]
On \((\frac{N-2}{N-1},\frac{N-1}{N})\), \(C_N(\alpha)=N/(N-1)\), but at the right endpoint it equals \(1\). Finally, for every fixed \(\alpha\in(0,1)\), \(C_N(\alpha)\) is nondecreasing in \(N\) and
\[
 \boxed{\lim_{N\to\infty} C_N(\alpha)=1/\alpha.}
\]
For an arbitrary finite, full-support probability-preserving permutation \(T\), its sharp constant is the maximum of \(C_N(\alpha)\) over its cycle lengths \(N\) (with the convention \(C_1(\alpha)=1\)). Thus the finite cyclic formula classifies every finite measure-preserving permutation, not just ergodic ones.

## Assumptions and scope
The averaging starts at the tested phase and proceeds only in forward integer time. It uses all lengths \(L\ge1\), strict threshold \(>\alpha\), exact arithmetic, and the discrete normalized counting measure. There is no stopping-time cutoff, no two-sided or centered averaging, no ball basis, and no continuous-time interpolation. The subset \(E\) is arbitrary except for nonemptiness. The assertion concerns the complete deterministic finite permutation with \(N\ge2\), and is not a statement about infinite lattice actions.

## Proof
**Upper bound at fixed cardinality.** Write \(k=|E|\), \(a_j=\mathbf1_E(j)-\alpha\), and extend \(a_j\) periodically to integers. If \(k/N>\alpha\), the average over every complete period exceeds \(\alpha\), so \(H_\alpha(E)\) consists of all \(N\) phases, and \(N<k/\alpha\).

Suppose \(k/N\le\alpha\). The period sum \(s=k-N\alpha\) is nonpositive. Define \(S_0=0\), \(S_m=\sum_{j=0}^{m-1}a_j\) for \(m\ge1\). Choose \(m_0\in\{0,\dots,N-1\}\) maximizing \(S_m\) over that range. For \(q\ge0\), periodicity gives \(S_{qN+r}=qs+S_r\le S_{m_0}\) for every \(0\le r<N\). In particular no forward sum based at \(m_0\) is positive, hence \(m_0\notin H_\alpha(E)\).

Split the halo into nonempty maximal consecutive cyclic blocks \([a,b]\), each followed by a phase \(b+1\notin H_\alpha(E)\), and unroll indices along the cycle. By the definition of the complement, \(S_q\le S_{b+1}\) for all \(q>b+1\). Since \(b\) belongs to the halo, some forward partial sum from \(b\) is positive; hence \(S_b<S_{b+1}\). Inducting backwards from \(b\) to \(a\), the same argument shows \(S_j<S_{b+1}\) for every \(a\le j\le b\): if all later partial sums are at most \(S_{b+1}\), membership of \(j\) forces this strict inequality. Consequently
\[
 \sum_{j=a}^b(\mathbf1_E(j)-\alpha)=S_{b+1}-S_a>0.
\]
Summing over disjoint halo blocks yields \(0<k-\alpha|H_\alpha(E)|\), because \(E\subset H_\alpha(E)\) by the length-one average. Thus \(|H_\alpha(E)|<k/\alpha\). Since this is an integer, it is at most \(\lceil k/\alpha\rceil-1\). The same inequality holds in the previous case, and \(|H_\alpha(E)|\le N\) always.

**Attainment.** Set \(E=\{0,\dots,k-1\}\) cyclically. When \(k/N>\alpha\), every phase belongs to the halo. Otherwise each outside phase lies \(j\) steps before the first point of \(E\), for a unique integer \(1\le j\le N-k\). Its largest average among the first \(N\) lengths equals \(k/(j+k)\): there are first \(j\) zeros, then \(k\) ones, then zeros. For a longer length \(L=qN+r\) the average is a convex combination of \(k/N\le\alpha\) and the initial \(r\)-step average, so longer lengths cannot create a new strict exceedance. The outside phase is therefore in the halo exactly when \(j<k(1/\alpha-1)\). Including the \(k\) phases of \(E\), this gives
\[
 |H_\alpha(E)|=k+\min\{N-k,\lceil k/\alpha-k\rceil-1\}=\min\{N,\lceil k/\alpha\rceil-1\}.
\]
Maximizing over \(k\) proves the exact formula.

**Endpoint and limit.** For \(k<N\), any average beginning outside \(E\) that exceeds the global density must have a first partial interval containing at least one zero, and at most \(k\) ones, hence ratio at most \(k/(k+1)\le(N-1)/N\). Equivalently, the exact formula directly gives \(|H_\alpha(E)|=k\) whenever \(\alpha\ge(N-1)/N\). Immediately below this threshold, only the case \(k=N-1\) can gain one extra halo phase, giving the displayed jump. Increasing \(N\) increases each fixed-\(k\) numerator in the formula and adds new choices, hence \(C_N\) is nondecreasing. The universal bound gives \(C_N(\alpha)<1/\alpha\); for large \(N\), choose \(k_N=\lfloor\alpha N\rfloor-1\ge1\). Then \(k_N<\alpha N\) and
\[
 C_N(\alpha)\ge\frac{\lceil k_N/\alpha\rceil-1}{k_N}\ge\frac1\alpha-\frac1{k_N}\longrightarrow\frac1\alpha.
\]
For a finite invariant permutation, the halo decomposes across its cycles, and the ratio of the total halo measure to the total initial-set measure is an initial-set-mass-weighted average of the corresponding cyclic ratios. Concentrating \(E\) on a maximizing positive-mass cycle attains their maximum.

## Verification
Run the standalone exact-arithmetic program `python3 verify.py`. It checks the predicted sharp halo size against direct enumeration of **every nonempty subset** for all cycle lengths \(2\le N\le10\), at every rational threshold arising from an average of length at most \(N\) and at each interval midpoint. It separately confirms consecutive-block attainment for each cardinality, the critical plateau and jump, and asymptotic bounds for much larger cycles. In particular \(C_{10}(3/5)=8/5\), attained by five consecutive marked phases with eight halo phases. The computer census is finite support only; the proof above establishes the all-size, all-real-threshold theorem.

## Relationship to prior work
Huang, *Solyanik estimates for ergodic flows* (first posted October 30, 2026, arXiv:2610.41151v1), proves that a **nontrivial continuous-time measure-preserving flow** has one-sided Tauberian constant \(1/\alpha\). That theorem does not cover one-sided **discrete-time finite cycles**; their exact constants are generally smaller and can jump. Huang, *Sharp Solyanik estimates for discrete and ergodic Hardy–Littlewood maximal operators* (arXiv:2610.41156v1), establishes general discrete and ergodic estimates and exhibits a bounded-period plateau for a different, uncentered ball basis. The 2015 Hagelstein–Parissis paper *Solyanik estimates in ergodic theory* (arXiv:1503.02900v1) recalls the classical one-sided maximal ergodic inequality and develops multi-parameter geometric-basis estimates. These furnish context and an upper bound, not the all-threshold sharp finite-cycle formula above. The issue of historical priority beyond the inspected material remains open.

## Limitations
The finite-cycle claim makes no assertion for noninvertible maps, infinite or continuous-time actions, alternative centered/two-sided averaging bases, or weighted observables. The formula is an exact deterministic invariant, not an estimate of stochastic sampling. The proof establishes one family of extremizers at each cardinality, not a complete classification of all maximizing sets. The direct computer checks do not establish the infinite statement independently.

## References
- K. Huang, *Solyanik estimates for ergodic flows*, arXiv:2610.41151v1, October 30, 2026, https://arxiv.org/html/2610.41151v1.
- K. Huang, *Sharp Solyanik estimates for discrete and ergodic Hardy–Littlewood maximal operators*, arXiv:2610.41156v1, October 30, 2026, https://arxiv.org/html/2610.41156v1.
- P. Hagelstein and I. Parissis, *Solyanik estimates in ergodic theory*, arXiv:1503.02900v1, March 10, 2015, https://arxiv.org/pdf/1503.02900.
