# Exact factorial screening of a pinned color in antagonistic adsorption

## Finding
Consider the one-attempt antagonistic two-color random sequential adsorption process on the infinite integer lattice. Each site other than the origin independently attempts a single irreversible deposition at a uniformly distributed time in \([0,1]\), proposing \(A\) with probability \(\alpha\in(0,1)\), or \(B\) with probability \(\beta=1-\alpha\). An attempt is accepted precisely when no already occupied nearest neighbor has the opposite color. Compare two processes with *identical* proposal times and marks away from the origin: the origin is preoccupied by \(A\) in the plus process and by \(B\) in the minus process, both at time zero. It makes no later attempt.

For \(d\ge1\), define the color-\(A\) response
\[
R_d^A(t)=\Pr\{\eta_d^+(t)=A\}-\Pr\{\eta_d^-(t)=A\},\qquad 0\le t\le1.
\]
Put \(\gamma=\sqrt{\alpha\beta}\) and
\[
h_A(u)=\cosh(\gamma u)-\frac{\beta}{\gamma}\sinh(\gamma u).
\]
The *complete spatial response kernel* is
\[
\boxed{R_d^A(t)=\frac{\alpha^{\lceil d/2\rceil}\beta^{\lfloor d/2\rfloor}}{(d-1)!}
\int_0^t u^{d-1}h_A(u)\,du.}
\tag{1}
\]
For every \(0<\alpha<1\), \(0<t\le1\), and integer \(d\ge1\), the response is strictly positive. Its factorial tail has the sharp constant
\[
\boxed{\lim_{d\to\infty}\frac{d!\,R_d^A(t)}{\alpha^{\lceil d/2\rceil}\beta^{\lfloor d/2\rfloor}t^d}=h_A(t)>0.}
\tag{2}
\]
The entire spatial generating function, with an arbitrary complex variable \(z\), is
\[
\boxed{\mathcal R_A(z,t):=\sum_{d\ge1}R_d^A(t)z^d
=z\int_0^t h_A(u)\bigl[\alpha\cosh(\gamma zu)+\gamma\sinh(\gamma zu)\bigr]du.}
\tag{3}
\]
In particular, at equal proposal probabilities, \(\alpha=\beta=1/2\),
\[
R_d^A(t)=\frac{1}{2^d(d-1)!}\int_0^t u^{d-1}e^{-u/2}\,du,
\quad \mathcal R_A(z,t)=\frac{z\bigl(e^{(z-1)t/2}-1\bigr)}{z-1},
\quad\boxed{\sum_{d\ge1}R_d^A(t)=\frac t2.}
\tag{4}
\]
The apparent singularity at \(z=1\) is removable. By reflection the same responses occur on the negative half-line. Consequently, including the forced origin, the sum over all sites of the change in expected \(A\)-occupation is exactly \(1+t\) in the balanced process. The corresponding \(B\)-occupation change is its negative.

## Assumptions and scope
Each site outside zero has one independent uniform attempt time and one independent proposed color, never changed after a failed attempt. The two coupled processes use the same realization of these variables. The origin is already occupied at time zero and is not subject to an additional attempt. All statements are infinite-volume probabilities, not finite-ring limits or conditional laws given an ordinary root proposal. The time interval is \([0,1]\), with fixed \(0<\alpha<1\). The strict inequalities and large-distance limits require \(t>0\). Both left and right halves are independent conditional on the prescribed origin color.

Infinite-volume decisions are almost surely well defined. To determine a site's state, explore earlier arrivals along nearest-neighbor paths. A dependency chain of length \(m\) needs strictly descending independent times; the probability of such an event is at most \(2^m/(m+1)!\). This tends to zero and is summable, so finite-path truncations converge for any fixed observation site and time. For the difference of the two coupled evolutions, an influence can travel only along the unique path away from the origin, requiring strictly increasing attempt times.

## Proof
**1. Vacant-boundary cavity.** Run the unseeded model on a half-line whose endpoint has only one neighbor, and let \(a(u)\) and \(b(u)\) be the probabilities that the endpoint is occupied by \(A\) and \(B\) by time \(u\). Before the endpoint proposes, its neighbor evolves with the endpoint held vacant; it therefore has the law of another endpoint of the half-line. Conditioning on the attempted mark and time gives the exact Volterra equations
\[
a'(u)=\alpha[1-b(u)],\qquad b'(u)=\beta[1-a(u)],\qquad a(0)=b(0)=0.
\]
Their unique solution is
\[
a(u)=1-\cosh(\gamma u)+\frac{\alpha}{\gamma}\sinh(\gamma u),\qquad
b(u)=1-\cosh(\gamma u)+\frac{\beta}{\gamma}\sinh(\gamma u).
\]
Thus \(1-b(u)=h_A(u)\). Moreover \(b(u)\le\beta u\) because the endpoint must have proposed \(B\) by \(u\); hence \(h_A(u)\ge1-\beta u>0\) for \(u\in[0,1]\).

**2. A single causal disagreement path.** Couple the two seeded evolutions using identical arrival data. At site one, their outcomes differ only if it proposes: a proposed \(A\) is allowed next to the plus origin but blocked by the minus origin, and a proposed \(B\) has the reverse behavior (provided the other neighbor has not already blocked the proposal). At subsequent sites, a disagreement can propagate to the right only if the next site's attempt occurs strictly later and proposes the *opposite* color to the one occupying its preceding neighbor in the currently unblocked copy. Otherwise both copies give the same outcome and cannot later disagree at that site, because attempts occur only once.

Therefore, for a difference at site \(d\), its marks on sites \(1,\ldots,d\) must alternate, its arrival times must obey \(0<u_1<\cdots<u_d\le t\), and the last proposed color must be that measured. When the last mark is \(A\), the unique alternating word has \(\lceil d/2\rceil\) occurrences of \(A\) and \(\lfloor d/2\rfloor\) of \(B\). On this event, site \(d\) becomes \(A\) in the plus evolution and remains vacant in the minus evolution precisely when the exterior neighbor \(d+1\) has not already accepted \(B\) by time \(u_d\). Before \(u_d\), site \(d\) is vacant in both copies, so this exterior event is independent of the path arrival data and has probability \(h_A(u_d)\) by step 1. No alternative branch can change \(A\)-occupation in the opposite direction.

The factor for alternating proposed colors is \(\alpha^{\lceil d/2\rceil}\beta^{\lfloor d/2\rfloor}\). The Lebesgue volume of the ordered region \(0<u_1<\cdots<u_{d-1}<u_d=u\) is \(u^{d-1}/(d-1)!\). Multiplying these independent factors and integrating the final attempt time proves (1). Reflection gives the left-half statement, and exchanging the colors shows the \(B\) response has the opposite sign.

**3. Positivity and the sharp tail.** The integrand in (1) is positive on \((0,t]\). For fixed \(t>0\), the probability measures \(d\,u^{d-1}du/t^d\) on \([0,t]\) concentrate at \(u=t\). By bounded continuity of \(h_A\),
\[
\frac d{t^d}\int_0^t u^{d-1}h_A(u)du\longrightarrow h_A(t).
\]
Equation (2) follows immediately, without extrapolating from finite-distance checks.

**4. Summing the spatial response.** The bound \(0\le h_A\le1\) gives absolute, locally uniform convergence of the series in (3) for every complex \(z\). Splitting odd and even distances yields the integrand
\[
\sum_{d\ge1}\frac{\alpha^{\lceil d/2\rceil}\beta^{\lfloor d/2\rfloor}z^du^{d-1}}{(d-1)!}
=\alpha z\cosh(\gamma zu)+\gamma z\sinh(\gamma zu).
\]
Interchanging integration and summation proves (3). With \(\alpha=\beta=1/2\), we have \(\gamma=1/2\) and \(h_A(u)=e^{-u/2}\). Thus the integrand of (3) is \(ze^{(z-1)u/2}/2\), which integrates to (4). At \(z=1\) the continuous value equals \(t/2\); the seeded origin contributes one additional unit to the full-line \(A\)-occupation difference. Symmetry under exchanging \(A\) and \(B\) proves the opposite \(B\)-occupation difference.

## Verification
The standalone standard-library program `verify_seed_response.py` enumerates every active-site subset, ordering and proposed-color assignment for paths of one through seven unforced sites adjoining a prescribed origin, with both opposite preseedings. It computes finite-path expectation differences without using the infinite-volume formula and compares them in exact rational arithmetic at three biases \(\alpha\in\{1/3,1/2,2/3\}\) and three observation times \(t\in\{1/3,1/2,1\}\). The independent comparator uses only finite-half-line polynomial recurrences, which follow by conditioning on the endpoint's attempt:
\[
a_m'(t)=\alpha[1-b_{m-1}(t)],\quad b_m'(t)=\beta[1-a_{m-1}(t)],\quad a_0=b_0=0.
\]
For a path with \(n\) sites away from the seeded origin, the finite version of (1) replaces \(h_A(u)\) by \(1-b_{n-d}(u)\). The program checks **252 exact equalities across 1,146,655 marked-order cases** and separately tests the balanced generating-function sum with a certified factorial tail bound. It passed these checks when run from the packaged program's actual source. These exhaustive *finite-path* computations do not prove (1) in infinite volume or (2) for unbounded distance; steps 1–4 supply those proofs.

For illustration at balanced bias and terminal time, the first four response probabilities on either half-line are approximately \(0.3934693403\), \(0.0902040104\), \(0.0143876780\), and \(0.0017516226\); their complete sum, including all farther sites, is exactly \(1/2\).

## Relationship to prior work
Do Amaral and dos Santos [1] introduce precisely this one-attempt two-color antagonistic adsorption process and derive its unperturbed one-site densities for every time and bias; their calculation contains the cavity principle used in step 1. The one-neighbor response \(R_1^A\) follows directly from that same cavity law and is not claimed separately as new. The claim here instead concerns **a forced color swap at a preoccupied root** and gives the full, all-distance causal response, exact factorial coefficient and total susceptibility identity. None of these is a marginal density or a conditional ordinary-root event.

The prior exact all-size same-color cluster law [4] uses the same one-sided cavity probabilities and determines unperturbed contiguous cylinder probabilities, but does not condition on or intervene at an initially occupied root. Its cylinder probabilities do not specify the joint coupling of the two *different seeded histories*. The published distance-two covariance calculation [5] concerns unperturbed two-site occupations, not the response at distance \(d\) to an intervened root color. The finite-cycle excess [6] considers an unseeded periodic system and an average density, and therefore does not cover a pinned-site response. A localized dimer rate-defect theorem [7] also exhibits factorial screening, but changes the clock rate on one dimer edge in a different adsorption model; its alternating-sign effect and edge observable do not imply the strictly positive color-specific response here.

Do Amaral and dos Santos [2] study one-species nearest-neighbor *exclusion of any occupied neighbor*; that mechanism is not two-color opposite-type exclusion. Martins, Dickman and Ziff [3] investigate a two-color process with **repeated** proposals after rejection and focus on two-dimensional percolation, with a one-dimensional saturation discussion. General deposition and annihilation results by Penrose and Sudbury [8] provide useful graphical-construction context for one-species models but do not supply this two-color pinned response. Originality is a best-knowledge comparison; an unindexed response theorem could limit publication priority.

## Limitations
The result requires the one-attempt rule, uniform independent proposal times, nearest-neighbor exclusion of opposite colors only, and one permanently preoccupied site at time zero. It does not describe repeated attempts, spatially dependent attempted colors, multiple pinned sites, finite periodic systems, or time-dependent interventions. The sharp tail holds as distance grows for fixed positive time and bias and is not claimed uniform when the bias approaches zero or one. Independent mathematical validation and exhaustive historical-priority verification have not been performed.

## References
[1] C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786 (first public 2023-06-16), https://arxiv.org/abs/2306.09786.

[2] C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, arXiv:2210.05627 (first public 2022-10-11), https://arxiv.org/abs/2210.05627.

[3] P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622 (first public 2022-11-09), https://arxiv.org/abs/2211.04622.

[4] *Exact geometric tails for same-species clusters in one-shot antagonistic adsorption*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-geometric-tails-for-same-species-clusters-in-one-shot-anta--04ec1f49bc46.

[5] *Exact second-neighbor correlation in one-shot antagonistic adsorption*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-second-neighbor-correlation-in-one-shot-antagonistic-adsor--b16701b2c768.

[6] *Strict factorial finite-cycle excess in balanced one-attempt antagonistic adsorption*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-strict-factorial-finite-cycle-excess-in-balanced-one-attempt-ant--f5f37a6bc0ec.

[7] *Alternating factorial screening of one anomalous dimer-adsorption bond*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-alternating-factorial-screening-of-one-anomalous-dimer-adsorptio--62931be7f8b0.

[8] M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519 (first public 2005-03-24), https://arxiv.org/abs/math/0503519.
