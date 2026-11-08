# Strict factorial finite-cycle excess in balanced one-attempt antagonistic adsorption

## Finding
Let \(n\ge3\) and consider the simple undirected cycle \(C_n\). Independently assign to each vertex a proposal type \(A\) or \(B\), each with probability \(1/2\), and a continuous uniform arrival time. In increasing time order, accept each proposal exactly when none of its *already accepted* neighbors has the opposite type. Every vertex makes precisely one attempt; rejected vertices make no later attempts. Let \(\rho_n\) denote the expected fraction of occupied vertices at the terminal time.

Define \(r_0=0\) and, for integers \(m\ge1\),
\[
r_m=1+\frac2m\sum_{j=0}^{m-2}r_j,
\]
where an empty sum is zero. The complete finite-size expectation is
\[
\rho_n=\sum_{m=1}^{n-2}\frac{r_m}{2^{m+1}}+
\begin{cases}
2^{1-n}r_n,&n\ \mathrm{odd},\\[2pt]
2^{1-n}\left(r_{n-1}+\frac{1+r_{n-3}}n\right),&n\ \mathrm{even}.
\end{cases}
\tag{1}
\]
For every integer \(n\ge3\),
\[
\boxed{\rho_n>1-e^{-1}.}
\tag{2}
\]
The excess has two different, sharp, factorial scales:
\[
\boxed{\lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}n\,n!\bigl(\rho_n-(1-e^{-1})\bigr)=1,\qquad
\lim_{\substack{n\to\infty\\n\ \mathrm{even}}}n!\bigl(\rho_n-(1-e^{-1})\bigr)=\frac12.}
\tag{3}
\]
Thus even cycles have an excess asymptotic to \(1/(2n!)\), whereas odd cycles have the smaller excess asymptotic to \(1/(n\,n!)\). The infinite-line terminal coverage \(1-e^{-1}\) itself was previously known.

## Assumptions and scope
All random types and arrival times are mutually independent. The finite graph is a *simple* cycle (including the triangle at \(n=3\)), no holding or repeated depositions occur, and the coverage is the total number of accepted vertices divided by \(n\), averaged over both types and arrival orders. Only the balanced probabilities \(1/2,1/2\) and full terminal time are asserted in this theorem. A random greedy independent set on a graph means processing its vertices in uniform random order and accepting a vertex exactly when no previously accepted vertex is adjacent to it.

## Proof
**1. Conflict graph.** Fix the proposed species \(Y_v\) of every vertex. Form a graph \(H\) on the same vertices by retaining precisely the cycle edges \(uv\) for which \(Y_u\ne Y_v\). Given these species, the one-attempt adsorption algorithm is *identical*, for every arrival ordering, to the random-order greedy maximal independent set algorithm on \(H\). This equivalence follows because equal-type neighbors never block an arrival, while opposite-type previously accepted neighbors are exactly the retained edges of \(H\). The connected components of \(H\) are alternating-color paths, except that a perfectly alternating coloring on an even cycle gives \(H=C_n\).

**2. Greedy occupancy of a path.** Write \(r_m\) for the mean number accepted by random-order greedy selection on a path of \(m\) vertices. Conditional on the first chosen vertex, its two neighbors become ineligible and the remaining eligible vertices comprise independent left and right subpaths. Averaging the first position gives the recurrence stated above. With \(R(z)=\sum_{m\ge0}r_mz^m\), formal power series manipulation yields
\[
zR'(z)=\frac{z}{(1-z)^2}+\frac{2z^2}{1-z}R(z),
\qquad
R(z)=\frac{1-e^{-2z}}{2(1-z)^2}.
\tag{4}
\]
The formula follows by an integrating factor and \(R(0)=0\), hence is valid analytically for \(|z|<1\).

**3. Exact components on the cycle.** Fix a candidate starting position for a component of \(m\) consecutive vertices, where \(1\le m\le n-2\). Its two boundary edges must be between equal types and its \(m-1\) internal edges between opposite types. There are precisely two compatible species assignments on the \(m+2\) distinct involved sites; this event has probability \(2^{-(m+1)}\). By cyclic translation invariance, the expected number of such path components is \(n/2^{m+1}\).

The wraparound cases are different. If \(n\) is odd, a coloring with exactly one equal-type edge gives a spanning path of order \(n\): there are \(n\) choices of the equal edge and two alternating assignments for each, so its probability is \(n2^{1-n}\); a completely alternating full cycle is impossible. If \(n\) is even, a spanning path with exactly one equal edge is impossible; a path component of order \(n-1\) starts at any fixed position with probability \(2^{1-n}\). A fully alternating coloring occurs with probability \(2^{1-n}\), resulting in the conflict graph \(C_n\). The first greedy choice on \(C_n\) removes its two neighbors from future selection, leaving a path of order \(n-3\), so the mean greedily selected count on that full cycle is \(1+r_{n-3}\). All remaining components have the ordinary lengths counted above. Summing conditional expected accepted vertices over components and dividing by \(n\) proves equation (1), including \(n=3,4\).

**4. Exact comparison with the infinite-line density.** By equation (4),
\[
\rho_\infty:=\sum_{m\ge1}\frac{r_m}{2^{m+1}}=\frac12R(1/2)=1-e^{-1}.
\tag{5}
\]
The series is absolutely convergent because \(0\le r_m\le m\). To expose the extremely small difference, let
\[
a=\frac{1-e^{-2}}2,\qquad b=\frac{1-3e^{-2}}2,
\qquad B_j=\frac1{j!}\int_0^1 t^j(1-t)e^{-2(1-t)}\,dt\quad(j\ge0).
\tag{6}
\]
Expanding equation (4) at \(z=1\) and using the elementary identity
\[
\frac{e^x-1-x}{x^2}=\int_0^1(1-t)e^{tx}\,dt
\]
provides the **exact**, not asymptotic, decomposition for every \(m\ge0\):
\[
r_m=am+b+(-1)^{m+1}2^{m+1}B_m.
\tag{7}
\]
Indeed, \(R(z)=a(1-z)^{-2}-e^{-2}(1-z)^{-1}-\frac{e^{-2}}{2(1-z)^2}\bigl(e^{2(1-z)}-1-2(1-z)\bigr)\), and the integral identity evaluates each Taylor coefficient of the last term. Note that \(1+b-3a=0\). Moreover \(B_j>0\), and \(B_{j+1}<B_j/(j+1)\) follows immediately from the defining integral; in particular the alternating series below have strictly decreasing positive terms.

For odd \(n\), subtract the tail of (5) from (1). The linear part \(am+b\) cancels because \(\sum_{m\ge n-1}2^{-(m+1)}(am+b)=2^{1-n}(an+b)\). Inserting (7) yields
\[
\rho_n-\rho_\infty
=B_{n-1}+3B_n+\bigl(B_{n+1}-B_{n+2}+B_{n+3}-\cdots\bigr)>0.
\tag{8}
\]
For even \(n\), the same linear part cancels because \(1+b-3a=0\), and equation (7) gives
\[
\rho_n-\rho_\infty
=\frac{B_{n-3}}{2n}+B_{n-1}+\bigl(B_n-B_{n+1}+B_{n+2}-\cdots\bigr)>0.
\tag{9}
\]
Both signs are strict since each displayed alternating parenthesis is positive by the alternating-series test. This proves (2).

**5. Two sharp scales.** Since the weight \(t^j(1-t)\) concentrates near \(t=1\), a beta-integral estimate gives
\[
B_j=\frac{1+O(j^{-1})}{j!(j+1)(j+2)}\qquad(j\to\infty).
\tag{10}
\]
For an elementary uniform justification, use \(1-2(1-t)\le e^{-2(1-t)}\le1\) in (6) and the exact integrals of \(t^j(1-t)\) and \(t^j(1-t)^2\). Equation (8) is \(B_{n-1}+O(B_n)\), and (9) is \(B_{n-3}/(2n)+O(B_{n-1})\); successive \(B_j\) shrink by at least a factorial factor. Finally,
\[
B_{n-1}\sim\frac1{(n-1)!n(n+1)}\sim\frac1{n\,n!},
\qquad
\frac{B_{n-3}}{2n}\sim\frac1{2n!}.
\]
These estimates prove equation (3). No numerical extrapolation is used in this argument.

## Verification
An independent finite-state calculation enumerates all \(2^n\) equally likely species assignments and, for each resulting conflict graph, computes exact greedy expected occupancy by the first-vertex recurrence on vertex subsets. It agrees with equation (1) for every \(3\le n\le10\). Exact rational alternating-Taylor enclosures verify \(\rho_n>1-e^{-1}\) for \(3\le n\le31\), and separate checks evaluate elementary rational bounds for the integral kernels. The standalone source `check_one_shot_cycle.py` reproduces 61 grouped exact-rational assertions with Python's standard library. These finite checks are corroborative; the proof of the all-size inequalities and asymptotic limits is analytic in steps 1–5.

## Relationship to prior work
Do Amaral and dos Santos (2023, arXiv:2306.09786) introduced precisely the one-deposition-per-site antagonistic model on the infinite integer line and computed its expected species densities at every time; equation (5) agrees with their balanced terminal density. That source does not give equation (1) or compare finite periodic systems with the infinite-line limit. Classical path greedy occupancy and the limit \((1-e^{-2})/2\) are longstanding, and Krivelevich, Mészáros, Michaeli and Shikhelman (2024, first posted 2023) develop general local-limit methods for greedy maximal independent sets. These results justify context and first-order limits but do not state the cycle-dependent correction in (8)–(10). Gerin (2015) treats a related one-dimensional parking problem, not this two-species one-attempt finite cycle. The contribution here is the conflict-component reduction combined with **strict positive finite-cycle excess at every size and two explicit parity-dependent factorial constants**. Repeated-attempt two-species adsorption, in which rejected sites may receive another species later, is a different process and its finite-cycle laws are not equivalent.

## Limitations
Only terminal expected *total* occupied fraction for the balanced, one-attempt model on a simple cycle is determined. Equations (2)–(3) are not asserted for biased proposal probabilities, for repeated attempts, for higher-dimensional lattices, or for fluctuations/distributional observables. The novelty comparison is based on accessible published texts and records, not a guarantee of exhaustive historical priority. No independent mathematical validation has been performed.

## References
- C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786 (first posted 2023-06-16), https://arxiv.org/abs/2306.09786 , DOI: 10.1088/1751-8121/ad02cd.
- M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, first online 2023-12-18, https://doi.org/10.1002/rsa.21200 .
- L. Gerin, *The Page–Rényi Parking Process*, Electronic Journal of Combinatorics 22(4) (2015), #P4.4, https://doi.org/10.37236/5150 .
