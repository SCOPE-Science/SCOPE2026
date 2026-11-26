# Sharp finite-time switching bounds for two quarter-interval holes of the doubling map

## Finding
Let \(T(x)=2x\pmod 1\) act on \([0,1)\). At each integer time choose one of the equal-length holes \(H_0=[0,1/4)\) and \(H_1=[3/4,1)\). For a switching word \(\sigma=(\sigma_0,\ldots,\sigma_{n-1})\in\{0,1\}^n\), define
\[
S_n(\sigma)=\{x\in[0,1):T^t(x)\notin H_{\sigma_t}\ \text{for all }0\le t<n\}.
\]
Let \(F_0=0,F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\). Then, for every \(n\ge0\) and every schedule,
\[
\boxed{\frac{n+2}{2^{n+1}}\ \le\ \operatorname{Leb}(S_n(\sigma))\ \le\ \frac{F_{n+3}}{2^{n+1}}.}
\]
For every \(n\ge2\), equality on the left holds **only** for the two alternating words, and equality on the right holds **only** for the two constant words. For \(n=1\), both choices attain both bounds; the empty word is the sole schedule at \(n=0\).

For either infinite alternating schedule the infinite survivor set is **countably infinite** and has Hausdorff dimension zero; every surviving binary itinerary is eventually periodic of period two. For either constant schedule the infinite survivor set is the usual uncountable golden-mean-type subshift with Hausdorff dimension \(\log\varphi/\log2\), where \(\varphi=(1+\sqrt5)/2\). Consequently the two extremal schedules have escape rates \(\log2\) and \(\log(2/\varphi)\), respectively. Any infinite schedule for which a survival escape-rate limit exists has rate between these two values.

## Assumptions and scope
The map is the exact doubling map with Lebesgue initial distribution. The hole is checked at times \(t=0,\ldots,n-1\), **before** the next iterate; its location may be chosen arbitrarily at every step and its length is always \(1/4\). Binary expansions with two representations comprise a Lebesgue-null set and do not affect finite-time measures. No random-driving or periodicity assumption is imposed for the finite-time bounds. Assertions about infinite survivors specifically concern constant or alternating infinite schedules.

## Proof
For a point with binary itinerary \(x=0.b_0b_1b_2\ldots\), the condition \(T^t(x)\in H_0\) is equivalent, apart from dyadic endpoints, to the adjacent digit pair \((b_t,b_{t+1})=(0,0)\); likewise \(H_1\) corresponds to \((1,1)\). Thus admissible words of length \(n+1\) encode finite-time survivors, and each word has Lebesgue cylinder measure \(2^{-(n+1)}\).

Let \((a_t,b_t)\) count admissible digit strings of length \(t+1\) ending respectively in digit zero and digit one. Initially \((a_0,b_0)=(1,1)\). If the next hole is \(H_0\), appending a bit gives \((a_{t+1},b_{t+1})=(b_t,a_t+b_t)\); if it is \(H_1\), it gives \((a_{t+1},b_{t+1})=(a_t+b_t,a_t)\). These are exact integer recurrences, and the required cylinder count is \(C_n=a_n+b_n\).

For any \(t\ge1\), put \(u_t=\min(a_t,b_t)\) and \(v_t=\max(a_t,b_t)\). Both are positive and strictly unequal. The two choices for the *sorted* next pair are precisely
\[
(u_{t+1},v_{t+1})=(u_t,u_t+v_t)\quad\text{or}\quad(v_t,u_t+v_t).
\]
At time \(t=1\), the sorted pair is \((1,2)\) for either first choice.

For the lower bound, induction gives \(u_t\ge1\) and \(v_t\ge t+1\); hence \(C_t\ge t+2\). Equality for \(t\ge2\) forces \(u_t=1\). At each step after the first, this is possible only by choosing \((u_t,u_t+v_t)\), because \(v_t>u_t\). The required choice switches the forbidden digit at every step, hence the two and only two minimizers are alternating schedules. In an alternating schedule \((u_t,v_t)=(1,t+1)\), so equality is attained.

For the upper bound, induction from \((u_1,v_1)=(F_2,F_3)\) gives
\[
 u_t\le F_{t+1},\qquad v_t\le F_{t+2}.
\]
Indeed the next smaller entry is either \(u_t\) or \(v_t\), at most \(F_{t+2}\), while the larger is \(u_t+v_t\le F_{t+3}\). Thus \(C_t\le F_{t+3}\). For equality with \(t\ge2\), both entries must equal their respective Fibonacci bounds at the preceding step and the next smaller entry must be the former larger entry. Starting at \(t=1\), this is exactly the choice of the same forbidden digit at every step. Both constant schedules attain equality by the Fibonacci recurrence.

For an alternating schedule beginning with \(H_0\), the two transition matrices are
\[
 M_0=\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad M_1=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
 M_1M_0=\begin{pmatrix}1&2\\0&1\end{pmatrix}.
\]
Treat the last product as a directed two-step graph on the digit present at even times. It has one path from state zero to zero, one from one to one, two from one to zero, and no path from zero to one. Every infinite path therefore stays in its initial state forever or changes from one to zero exactly once and subsequently stays at zero. The possible change times are countable and yield only countably many infinite itineraries, each eventually periodic with two-step period. Both infinite never-changing paths exist, and arbitrary finite waiting times before the change yield infinitely many distinct survivors. The symmetric other alternation has the same conclusion. Dyadic expansions cannot give additional infinite survivors: an eventually all-zero expansion eventually lands in the hole \(H_0\) at every other time. The exact linear cylinder count implies Hausdorff dimension zero as well.

For a constant schedule, admissible binary words avoid a single repeated pair, giving the Fibonacci subshift. Its growth rate is \(\varphi\); its survivor set is an uncountable graph-directed Cantor set with Hausdorff dimension \(\log\varphi/\log2\) by equal-size cylinder coverings and the positive Perron eigenvector measure. The escape rates follow from the exact finite-time measures using \(F_{n+3}^{1/n}\to\varphi\). For a general switching schedule, taking logarithms in the finite-time inequalities bounds every subsequential escape-rate limit, without asserting that such a limit exists.

## Verification
The standalone \(\texttt{checker.py}\) enumerates all schedules through horizon fifteen, verifies the two unique extremizer classes and the sharp counts, and independently checks all admissible binary digit strings against the matrix recurrence for every schedule through horizon eight (511 independent comparisons). It also verifies the formulas along both extremal schedules through horizon one hundred and the exact two-step matrix product. Running `python3 checker.py` produced all PASS lines. These finite checks are independent sanity tests; the induction and directed-graph argument above prove the all-horizon and infinite-survivor claims.

## Relationship to prior work
Livorati, Georgiou, Dettmann and Leonel (arXiv:1312.7030, 2013) study a continuously oscillating or breathing hole in the doubling map, using Ulam calculations and hole-overlap approximations. Their model and claims do not supply an all-schedule finite-time optimum for switching between the two disjoint Markov cylinders. Atnip, Froyland, González-Tokman and Vaienti (arXiv:2103.04712v1, 2021) develop general thermodynamic formalism for random interval maps with holes; their main results concern existence, pressures and escape rates, not the exact global finite-horizon extremal classification here. Static forbidden-pair Fibonacci counts and the adjacency-matrix method are classical ingredients, not claimed as novel separately.

There is also an important equivalent formulation of the **alternating special case**: reflection \(R(x)=-x\pmod1\) commutes with \(T\), and \((R\circ T)^t=R^tT^t\). The alternating holes are \(R^tH_0\), so their survivors are the same as for the negative-doubling map with the fixed hole \(H_0\), up to endpoint convention. This reduction can recover the alternating-case count but does not alone establish optimality and uniqueness among *all* switching words. Priority of the complete switching optimum remains subject to further literature verification.

## Limitations
The result concerns precisely two dyadic quarter-interval holes; it does not classify optimal schedules for other hole positions, non-Markov hole sizes, other maps, or probabilistically chosen schedules. The finite-time bounds hold without assumptions on the schedule, whereas the countability assertions concern alternating infinite schedules only. The proof uses established symbolic-counting methods, and an earlier equivalent extremal theorem under different language cannot be ruled out from the accessed literature. This is a mathematical claim with reproducible finite tests, not an independently audited result.

## References
1. J. Atnip, G. Froyland, C. González-Tokman and S. Vaienti, *Thermodynamic Formalism for Random Interval Maps with Holes*, arXiv:2103.04712v1 (first submitted 2021-03-08), especially Introduction and Section 15.1. https://arxiv.org/abs/2103.04712
2. A. L. P. Livorati, O. Georgiou, C. P. Dettmann and E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030 (2013), *Physical Review E* 89 (2014), 052913, Sections II–IV. https://arxiv.org/abs/1312.7030
3. P. Glendinning and N. Sidorov, *The doubling map with asymmetrical holes*, *Ergodic Theory and Dynamical Systems*, online 2013, DOI: 10.1017/S0143385713000989 (static-hole survivor sets). https://doi.org/10.1017/S0143385713000989
