# Two-seed parity reversal and factorial screening in one-dimensional dimer adsorption

## Finding
Consider irreversible random sequential dimer adsorption on the labelled cycle \(C_n\) with \(n\ge4\). Each bond proposes one dimer at an independent continuous arrival priority; it is accepted if both endpoints are vacant. Let \(M_n\) be the final number of dimers for identically distributed priorities.

**One-bond invariance.** Give bond \(e_0\) any independent arrival distribution with zero tie probability against the other \(n-1\) iid continuous priorities. The **entire probability law** of the terminal number of accepted dimers remains that of \(M_n\). In fact the same law holds conditional on every possible rank of \(e_0\), including ranks one and \(n\).

**Two-bond response.** For any disjoint \(e_0,e_d\), \(2\le d\le n-2\), force those two bonds to precede all others, leaving the other priorities in uniformly random order; the two seeds are necessarily accepted. Define \(F_0=F_1=0\), and for \(m\ge2\) set
\[
F_m=\sum_{k=1}^{m-1}\frac{(-1)^{k-1}2^{k-1}(m-k)}{k!}.
\]
Then the expected number of terminal dimers is \(2+F_{d-2}+F_{n-d-2}\), while the homogeneous mean is \(1+F_{n-2}\). In particular the exact, signed change is
\[
\Delta_{n,d}=1+F_{d-2}+F_{n-d-2}-F_{n-2}.
\]
Writing \(a=(1-e^{-2})/2\), \(\delta_m=F_m-am+e^{-2}\), one also has the exact finite-size identity
\[
\Delta_{n,d}=\delta_{d-2}+\delta_{n-d-2}-\delta_{n-2}.
\]
For fixed \(d\), as \(n\to\infty\), the response converges to \(\delta_{d-2}\), where
\[
\delta_0=e^{-2},\qquad
\delta_m=\frac{(-1)^m 2^m}{(m-1)!}\int_0^1x(1-x)^{m-1}e^{-2x}\,dx\quad(m\ge1).
\]
Consequently \((-1)^d\delta_{d-2}>0\) for every integer \(d\ge2\). For \(d\ge3\) the sharp elementary bounds are
\[
e^{-2}\frac{2^{d-2}}{(d-1)!}<(-1)^d\delta_{d-2}<\frac{2^{d-2}}{(d-1)!},
\]
and the ratio of the middle quantity to \(2^{d-2}/(d-1)!\) tends to one as \(d\to\infty\). Two pre-seeded dimers therefore have an alternating, factorially screened influence on the expected jammed count, whereas an individually controlled bond has no effect on its distribution.

## Assumptions and scope
A bond \(e_j\) joins sites \(j\) and \(j+1\pmod n\). Each bond is proposed once; rejected proposals never return. All unspecified bond priorities are iid atomless, and only their relative ordering matters. The one-bond statement requires independence from all other bond priorities and excludes ties. In the two-seed statement the two selected bonds are disjoint, and their mutual order is irrelevant. The response is an expected dimer **count**, not the occupied-vertex fraction. The limits take \(n\to\infty\) at fixed integer \(d\), and then \(d\to\infty\) when asserting factorial screening.

## Proof
**1. Exact open-path mean.** Let \(F_m\) be the expected greedy dimer count on the path with \(m\) vertices and uniformly randomly ordered edges. The first proposed edge is uniform among \(m-1\) edges. It is accepted and divides the remaining unoccupied vertices into paths with \(j\) and \(m-2-j\) vertices. Therefore
\[
(m-1)F_m=(m-1)+2\sum_{j=0}^{m-2}F_j\qquad(m\ge2),
\]
with \(F_0=F_1=0\). The generating function \(G(z)=\sum_{m\ge0}F_m z^m\) consequently satisfies \(G(z)=z(1-e^{-2z})/[2(1-z)^2]\); solving the recurrence, or comparing coefficients of this identity, gives the stated finite sum. This homogeneous open-path mean is classical background, not the asserted new result.

**2. One-bond invariance.** Condition on the rank \(r\) of a chosen bond among the \(n\) priorities. The remaining \(n-1\) bond orderings are uniformly permuted, independently of \(r\). For the homogeneous model, choose the rank-\(r\) bond uniformly among all \(n\) edges and uniformly order the others. This creates a uniform permutation of all \(n\) bond labels; hence its terminal-count law equals the unrestricted homogeneous law. Every edge has the same rank-conditioned law by rotational symmetry of \(C_n\); the fixed chosen edge therefore also has the unrestricted law at every rank. Mixtures over ranks cover arbitrary independent tie-free changes to its arrival law.

**3. Two first arrivals split the cycle.** Two disjoint seeded bonds occupy four vertices and isolate the remaining unoccupied sites into two disjoint open paths of lengths \(d-2\) and \(n-d-2\). The relative priorities remaining on each path are uniform, and no unused edge crossing an occupied vertex can be accepted. Hence the conditional mean equals \(2+F_{d-2}+F_{n-d-2}\). A single first bond cuts the remaining cycle into one open path of length \(n-2\), giving \(\mathbb EM_n=1+F_{n-2}\). Their difference yields the exact formula.

**4. Alternating factorial tail.** Define \(a=(1-e^{-2})/2\). The infinite series identities \(a=\sum_{k\ge1}(-1)^{k-1}2^{k-1}/k!\) and \(e^{-2}=\sum_{k\ge1}(-1)^{k-1}2^{k-1}/(k-1)!\) imply
\[
\delta_m=\sum_{j\ge1}\frac{(-1)^{m+j-1}2^{m+j-1}j}{(m+j)!},\qquad m\ge1.
\]
Expand \(e^{-2x}\) in its absolutely convergent power series and use \(\int_0^1x^{j+1}(1-x)^{m-1}\,dx=(j+1)!(m-1)!/(m+j+1)!\). Term-by-term integration gives the displayed integral formula. Since its integrand is positive, \(\delta_m\) has sign \((-1)^m\). Moreover \(e^{-2}<e^{-2x}<1\) for almost every \(0<x<1\), and \(\int_0^1x(1-x)^{m-1}\,dx=1/[m(m+1)]\), proving the strict two-sided bounds.

For large \(m\), normalizing \(x(1-x)^{m-1}\) gives a \(\mathrm{Beta}(2,m)\) distribution, whose mass concentrates at zero. Bounded convergence then gives \(\mathbb E[e^{-2X}]\to1\), yielding the sharp factorial asymptotic. The same bounds show \(\delta_m\to0\), so \(\Delta_{n,d}\to\delta_{d-2}\) as claimed. No experimental extrapolation is needed.

## Verification
Run `python3 verification_pair_impurities.py` using Python 3 standard library only. Direct enumeration checked 409104 priority-order evaluations on cycles of lengths four to nine, 33 rank-law comparisons, and 21 exact two-seed comparisons. The program also checked open-path recurrences and 16 alternating integral/bound instances numerically. The infinite-volume statements follow from the explicit integral proof, not those finite computations.

## Relationship to prior work
Bartelt (1991) studies the homogeneous finite-line dimer adsorption problem and boundary effects, motivating and covering the standard \(F_m\) calculation. Ziff (1994) studies information about a tagged deposited dimer; Bonnier, Boyer and Viot (1994) study unconditioned pair correlations of deposited objects. Lee (1997) develops impurity-density kinetics for random and RSA-generated impurities; its inspected manuscript treats ensemble initial conditions rather than two position-fixed, first-arriving dimers. The present claim concerns an exact **controlled pair response** with its alternating sign and factorial spatial screening, not a new homogeneous density formula or an unconditioned pair correlation.

## Limitations
There is no claim about stochastic dynamics when previously rejected dimers retry, adsorption with desorption, arbitrary inhomogeneity at multiple bonds, or a universal sign for finite \(n\). Single-bond invariance concerns the terminal count distribution, not all spatial observables. The pair result concerns forced earliest arrivals, not infinitesimal derivatives of two arrival rates. Older literature that formulates the same conditional two-seed response differently could affect the originality assessment; independent audit has not been performed.

## References
- M. C. Bartelt, “Random sequential filling of a finite line,” *Phys. Rev. A* **43** (1991), 3149–3152, DOI `10.1103/PhysRevA.43.3149`.
- R. M. Ziff, “Traces of the arrival history in the jammed state of random sequential adsorption,” *J. Phys. A* **27** (1994), DOI `10.1088/0305-4470/27/18/003`.
- B. Bonnier, D. Boyer and P. Viot, “Pair correlation function in random sequential adsorption processes,” *J. Phys. A* **27** (1994), 3671, DOI `10.1088/0305-4470/27/11/017`.
- J. W. Lee, “Effects of Impurities in Random Sequential Adsorption on a One-Dimensional Substrate,” preprint `arXiv:cond-mat/9701167`, first posted January 22, 1997; *Phys. Rev. E* **55** (1997), 3731, DOI `10.1103/PhysRevE.55.3731`.
