# Geometric vacancy chains and a Poisson extreme in discrete dimer parking

## Finding
Take \(n\ge2\) initially empty sites on a path and process every adjacent bond in an independent continuous-priority order. Accept a dimer exactly when both endpoints are empty. Let \(V_i\) indicate whether site \(i\) is *vacant in the final jammed configuration*. Define the classical one-endpoint probability
\[
a_m=\sum_{j=0}^{m-1}\frac{(-1)^j}{j!},\qquad m\ge1.
\]
The following *all-order geometric vacancy-chain law* is exact, including boundaries: for every integer \(k\ge0\) and \(1\le s\le n-3k\),
\[
\boxed{\Pr(V_s=V_{s+3}=\cdots=V_{s+3k}=1)=3^{-k}a_s a_{n-s-3k+1}.}\tag{1}
\]
In particular, on the infinite line the joint probability for \(k+1\) designated vacancies spaced three sites apart is \(e^{-2}3^{-k}\).

A pair of vacancies at distance three encloses an accepted dimer, and its four-site segment is an augmenting path for the jammed matching. Thus a chain with \(k\) links is a cluster of \(k\) *overlapping* local augmentation opportunities; these are not asserted to be simultaneously executable.

Let \(L_n\) be the largest \(k\ge1\) for which a chain occurs, or zero if no such chain exists. Then
\[
\boxed{\frac{L_n}{\log_3 n}\xrightarrow{\mathbb P}1.}\tag{2}
\]
For \(4\le s\le n-3k\), let \(B_{s,k}\) denote a chain from \(s\) to \(s+3k\) with \(V_{s-3}=0\), and set \(N_{n,k}=\sum_s\mathbf1_{B_{s,k}}\). These mark the left ends of long vacancy chains. Their exact probabilities are
\[
\Pr(B_{s,k})=3^{-k}\bigl(a_s-\tfrac13a_{s-3}\bigr)a_{n-s-3k+1}.
\tag{3}
\]
For every integer sequence \(k=k_n\ge1\) such that \(n3^{-k_n}\to\tau\in(0,\infty)\),
\[
\boxed{N_{n,k_n}\xrightarrow{\mathrm d}\operatorname{Poisson}\bigl(\tfrac23e^{-2}\tau\bigr),\quad
\Pr(L_n<k_n)\longrightarrow\exp\bigl(-\tfrac23e^{-2}\tau\bigr).}\tag{4}
\]
The factor \(2/3\) is a nontrivial extremal-clustering correction to the raw vacancy-chain count. The limits are *lattice limits along subsequences*: no unqualified continuously centered limiting distribution is asserted.

## Assumptions and scope
The graph is the open path with vertex set \(\{1,\ldots,n\}\), and its \(n-1\) edges have independent continuous identically distributed priorities. The process is the random-order greedy maximal matching, also called discrete Page–Rényi dimer parking. The vacancy indicator is measured only at the terminal jammed state. \(\log_3 n=(\log n)/(\log3)\). The theorem refers to consecutive vacancies at the *exact spacing three*, not arbitrary unoccupied-site gaps. Statements (1) and (3) hold for all admissible finite indices; statements (2) and (4) are asymptotic as \(n\to\infty\).

## Proof
**Endpoint probabilities.** Write \(a_m\) for the probability that the first site is vacant after dimer parking on a path of \(m\) sites, and set \(a_0=0\). The first attempted bond splits the remaining process into two independent shorter paths, giving \((m-1)a_m=\sum_{j=0}^{m-2}a_j\) for \(m\ge2\), with \(a_1=1\). Subtraction of successive recurrences proves \(a_m=\sum_{j=0}^{m-1}(-1)^j/j!\), and the alternating-series remainder gives \(a_m=e^{-1}+O(1/m!)\), uniformly for positive integer \(m\).

**Exact geometric-chain factorization.** Fix \(s,k\). The condition that sites \(s,s+3,\ldots,s+3k\) are all vacant forces the interior dimers on the bonds starting at \(s+1,s+4,\ldots,s+3k-2\). For each forced bond, its clock must be earlier than the clocks of its two adjacent bonds; otherwise one of those neighboring bonds would occupy a required-vacant site (the neighboring bond adjacent to the required vacancy cannot ultimately be accepted, so it must be blocked by this forced dimer). Conversely these local three-clock minima guarantee acceptance of all \(k\) forced dimers, and leave only the independent question whether the two designated outer sites remain vacant in their left and right subpaths. The \(k\) disjoint three-clock groups have independent minima, each of probability \(1/3\). Conditional on these minima, the clocks strictly outside those groups are independent and retain their original laws. The remaining endpoint-vacancy probabilities are \(a_s\) and \(a_{n-s-3k+1}\), proving (1). The case \(k=0\) follows from the same separation at a single required vacancy.

**Canonical starts and the mean.** The event \(B_{s,k}\) is the event in (1) minus the event that the chain also extends to \(s-3\). Subtract (1) with parameters \((s-3,k+1)\) to obtain (3). Summability of \(|a_m-e^{-1}|\le1/m!\) shows that, uniformly as \(k=o(n)\),
\[
\mathbb EN_{n,k}=3^{-k}\bigl[\tfrac23e^{-2}(n-3k)+O(1)\bigr].\tag{5}
\]
In particular, the mean converges to \(\lambda=\tfrac23e^{-2}\tau\) along the sequence in (4).

**Poisson approximation.** We give the localization and rare-dependence argument. The acceptance of an edge can be altered by deleting priorities outside distance \(w\) only if there exists a path of strictly decreasing priorities over at least \(w\) consecutive edges. There are at most two directions on a path, and each given decreasing path of length \(w\) has probability \(1/w!\). Consequently, coupling the true parking configuration to parking calculated inside a window extending \(w\) bonds beyond the sites used by a given \(B_{s,k}\) makes that event's indicator disagree with probability at most \(C/w!\) for an absolute constant \(C\). Put \(w=\lceil(\log n)^2\rceil\). The probability that *any* of the \(O(n)\) indicators differs is \(O(n/w!)=o(1)\).

The windowed event indicators have a dependency graph whose maximum degree is \(D=O(k+w)\). Their probabilities are at most \(3^{-k}+O(w!^{-1})\). If two candidate starts are at distance at most \(3k+3\), their true canonical-start events are mutually exclusive: two required vacancies would be too close or the later start would have an earlier vacancy at its predecessor. If the starts are farther apart, their necessary collections of \(k\) disjoint three-clock local minima are disjoint, so their joint probability is at most \(3^{-2k}\). The corresponding windowed pair probabilities differ by at most \(O(w!^{-1})\). Therefore both dependency-graph Chen–Stein sums satisfy
\[
b_1+b_2=O\bigl(nD3^{-2k}+nD/w!\bigr)=o(1)
\]
when \(n3^{-k}\to\tau\in(0,\infty)\), since \(k=O(\log n)\). The elementary dependency-graph Poisson bound (or the standard Chen–Stein inequality) now gives \(d_{\mathrm{TV}}(\mathcal L(N_{n,k}),\operatorname{Poisson}(\mathbb EN_{n,k}))\to0\). Combining with (5) proves the first assertion of (4). Every chain of length at least \(k\) either has a canonical left start counted by \(N_{n,k}\), or extends back to a first vacancy at one of sites \(1,2,3\). By (1), the latter event has probability at most \(3\cdot3^{-k}=o(1)\). Hence \(\{L_n<k\}\) and \(\{N_{n,k}=0\}\) differ with probability \(o(1)\), proving the remaining assertion of (4).

**Logarithmic maximal-chain length.** For every \(k\), (1) and \(0\le a_m\le1\) yield \(\Pr(L_n\ge k)\le n3^{-k}\), which tends to zero for \(k\ge(1+\varepsilon)\log_3n\). For the other tail, divide the path into \(\lfloor n/(3k+8)\rfloor\) nonoverlapping blocks. Within each block, demand \(k\) interior dimers and two outer protective dimers, all with strictly earlier clocks than their two neighboring bonds. These are \(k+2\) disjoint three-clock tests, hence an event of probability \(3^{-(k+2)}\), and they force a chain of \(k\) vacancy links insulated from the outside. The block events are independent. If \(k\le(1-\varepsilon)\log_3n\), the chance that none occurs is at most \(\exp[-\lfloor n/(3k+8)\rfloor3^{-(k+2)}]\to0\). Together with the upper bound this proves (2). \(\square\)

## Verification
The bundled `verify.py` enumerates all \((n-1)!\) priority permutations for every path size \(2\le n\le9\) and checks (1) and (3) exactly using rational arithmetic. It also checks the endpoint recursion independently and verifies finite small-case inequalities and the explicit canonical-start count. Execute `python3 verify.py` using standard Python 3. Enumeration confirms finite samples only; the limiting Poisson and logarithmic laws follow from the arguments above, not from tests or simulation.

## Relationship to prior work
The model and its end-vacancy recursion are classical. Gerin's paper, *The Page–Rényi parking process* (arXiv:1411.8002), explicitly gives the infinite-line probability \(e^{-2}/3\) for two vacancies separated by three sites: this **two-point special case is prior art** and is not included in the novelty claim. Gerin also develops local influence/stabilization tools. The new assertion is the entire finite all-order chain law plus the rare *canonical-start* Poisson extreme with its \(2/3\) clustering factor; no novelty is claimed for the local-minimum mechanism, endpoint law, or generic Chen–Stein methodology. Penrose and Sudbury (arXiv:math/0503519) study dimer RSA, exact evolution and normal approximations but no chain-extreme statement was found in the sections inspected. Published finite-endpoint covariance, global-count covariance, and late-successful-arrival Poisson results concern different observables and do not imply (4) directly.

## Limitations
The results apply to homogeneous random priorities and nearest-neighbor dimers on paths. They do not establish analogous laws for rings, longer rods, nonuniform rates or simultaneous augmentation of overlapping local paths. The asymptotic extreme law is valid along lattice subsequences, not as an unconditional continuously centered convergence. The classic Page (1959) paper and some broader lattice multisite-correlation literature were not available in full; these remain genuine historical-priority risks. No independent mathematical audit has been performed.

## References
1. L. Gerin, *The Page–Rényi parking process*, arXiv:1411.8002 (first public version 2014-11-28), https://arxiv.org/abs/1411.8002 ; *Electronic Journal of Combinatorics* 22 (2015), P4.4.
2. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519 (first public 2005-03-24), https://arxiv.org/abs/math/0503519 .
3. E. S. Page, *The distribution of vacancies on a line*, *J. Roy. Stat. Soc. B* 21 (1959), 364–374, https://doi.org/10.1111/j.2517-6161.1959.tb00343.x .
4. R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: The Chen–Stein method*, *Ann. Probab.* 17 (1989), 9–25.
