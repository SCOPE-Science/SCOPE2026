# Parity-split frozen-state polynomial for two-spin facilitation on cyclic ladders

## Finding
For every integer \(n\ge3\), the complete polynomial counting *fully frozen configurations* of the two-spin-facilitated Fredrickson–Andersen kinetic spin model on the cyclic two-leg ladder \(P_n=C_n\square K_2\) is
\[
B_n(z)=\begin{cases}F_{2n}(z),&n\text{ odd},\\F_n(z)^2,&n\text{ even},\end{cases}\qquad
F_m(z)=\sum_{k=0}^{\lfloor m/3\rfloor}
\frac{m}{m-2k}\binom{m-2k}{k}z^k\quad(m\ge3).
\]
The coefficient of \(z^k\) counts labeled fully frozen spin configurations with exactly \(k\) facilitating sites. The maximum number of facilitating sites is \(\lfloor2n/3\rfloor\) for odd \(n\), and \(2\lfloor n/3\rfloor\) for even \(n\). The latter is strictly one smaller than \(\lfloor2n/3\rfloor\) exactly when \(n\equiv2\pmod6\).

Writing \(\rho(z)\) for the unique positive root of \(\rho^3-\rho^2-z=0\) when \(z>0\), the frozen-state entropy per site is
\[
\lim_{n\to\infty}\frac{1}{2n}\log B_n(z)=\log\rho(z).
\]
In particular \(B_3(1),\ldots,B_9(1)=10,25,46,100,211,441,973\), and \(\rho(1)\approx1.465571231876768\).
For initially independent facilitating indicators of probability \(q\in(0,1)\), the probability that no spin can flip is exactly
\[
\Pr(\text{fully frozen})=(1-q)^{2n}B_n\!\left(\frac{q}{1-q}\right),
\]
with limiting logarithmic rate per site \(\log(1-q)+\log\rho(q/(1-q))<0\).

## Assumptions and scope
The vertex set is \(V(P_n)=\{(r,i):r\in\{0,1\},\ i\in\mathbb Z/n\mathbb Z\}\), with horizontal edges \((r,i)(r,i\pm1)\) and rung edges \((0,i)(1,i)\). Since \(n\ge3\), each site has exactly three distinct nearest neighbors. A facilitating spin is encoded by \(\xi_v=1\), which corresponds to an *empty* site in the usual occupied/empty convention of the FA model. At positive birth and death rates a spin at \(v\) may flip if and only if at least two *neighbors* of \(v\) have facilitating indicator one. The site \(v\)'s own state does not affect whether the flip is permitted. A *fully frozen* configuration is one in which no single spin flip is permitted anywhere, not a configuration with merely zero average current, nor every configuration in a nonergodic communicating class. The claimed census includes all \(2^{2n}\) labeled spin configurations, with no quotient by translation or reflection. A fugacity \(z\) weights each facilitating site; probability parameter \(q\) is the independent initial facilitating density and does not alter the kinetic constraint.

## Proof
**1. Translate facilitation to an open packing.** Let \(S=\{v:\xi_v=1\}\). The configuration is fully frozen if and only if \(|N(v)\cap S|\le1\) for every vertex \(v\). Equivalently no two distinct vertices in \(S\) share a common nearest neighbor. Define the conflict graph \(H_n\) on \(V(P_n)\), joining two distinct vertices precisely when they have a common neighbor in \(P_n\). Then the fully frozen sets are exactly the independent sets of \(H_n\), with their cardinalities preserved.

**2. Identify the conflict graph.** A direct enumeration of length-two walks in the three-regular prism shows that the conflicting vertices with a given \((r,i)\) are exactly the distinct members of
\[
\{(r,i+2),(r,i-2),(1-r,i+1),(1-r,i-1)\}.
\]
Define a permutation \(T(r,i)=(1-r,i+1)\). The four displayed vertices are precisely \(T^{\pm1}(r,i)\) and \(T^{\pm2}(r,i)\) (duplicates, if any, are harmless). Because \(T^2(r,i)=(r,i+2)\), the permutation \(T\) has one orbit of size \(2n\) if \(n\) is odd, and two orbits each of size \(n\) if \(n\) is even. Therefore \(H_n\cong C_{2n}^{\,2}\) when \(n\) is odd, whereas \(H_n\cong C_n^{\,2}\sqcup C_n^{\,2}\) when \(n\) is even. Here \(C_m^{\,2}\) is the graph in which cyclic positions at distance one or two are adjacent, and for \(m=3,4\) duplicated descriptions of an edge are counted only once.

**3. Count independent sets of a squared cycle.** For an independent set of size \(k\ge1\) in \(C_m^{\,2}\), successive selected positions have cyclic distances at least three. Writing those \(k\) positive distances as \(d_1,\dots,d_k\ge3\), their sum is \(m\). The number of ordered distance compositions is \(\binom{m-2k-1}{k-1}\). There are \(m\) choices of an initial selected position and each labeled independent set is obtained exactly \(k\) times, so the number with \(k\) selected vertices is
\[
\frac{m}{k}\binom{m-2k-1}{k-1}=
\frac{m}{m-2k}\binom{m-2k}{k}.
\]
This is nonzero precisely when \(3k\le m\). The empty set contributes the constant term one. Independence polynomials multiply over disjoint unions, proving the displayed formula for \(B_n(z)\), including its maximal powers and the parity-specific deficit.

**4. Entropy.** Introduce the nonnegative transfer matrix
\[
M(z)=\begin{pmatrix}1&z&0\\0&0&1\\1&0&0\end{pmatrix},\qquad
\det(\lambda I-M(z))=\lambda^3-\lambda^2-z.
\]
A closed walk of length \(m\) through its three memory states specifies a cyclic zero-one string with two zeroes separating any pair of ones; every selected vertex contributes weight \(z\). Thus \(F_m(z)=\operatorname{tr}(M(z)^m)\) for every \(m\ge3\). For \(z>0\) the matrix is irreducible and aperiodic (the first state has a self-loop), so its Perron eigenvalue \(\rho(z)>0\) is simple and strictly dominates the other eigenvalues in modulus. Consequently \(F_m(z)=\rho(z)^m(1+o(1))\), as \(m\to\infty\). The odd and even formulas both yield the stated entropy limit along their respective subsequences, hence along all \(n\). For \(q\in(0,1)\), multiplying the Bernoulli weights of every fully frozen configuration gives the displayed probability. Finally \(\rho(z)<1+z\), since \((1+z)^3-(1+z)^2-z=z((1+z)^2-1)>0\) and the cubic has a unique root exceeding one. With \(z=q/(1-q)\) this proves strictly negative logarithmic probability rate.

## Verification
The attached standalone standard-library script `verify_frozen_ladder.py` independently enumerates all binary configurations of the prism for \(3\le n\le9\), directly evaluates the local two-facilitator constraint, and compares the entire activity-resolved polynomial to the formula. It separately enumerates independent sets of squared cycles for \(3\le m\le13\). It also constructs the actual common-neighbor conflict graphs and checks their proposed cyclic-square decompositions for every \(3\le n\le50\). All checks passed. Symbolic characteristic-polynomial and trace checks for the transfer matrix were independently carried out for orders three through eight. These finite checks support the theorem but are not substitutes for the all-size proof above.

## Relationship to prior work
Cancrini, Martinelli, Roberto, and Toninelli (2006) precisely define facilitated-spin kinetic constraints and study relaxation and correlation scales of FA1f and FA2f, mainly on infinite-dimensional square and cubic lattices; their main statements do not enumerate fully frozen microstates of finite cylindrical ladders. Brešar, Klavžar, and Rall (2023) prove an **extremal** open-packing-number formula for bipartite prisms, which applies to \(n\) even, but does not imply this full coefficient-by-coefficient polynomial, the odd-base case, or the Bernoulli frozen-state probabilities. The independent-set polynomial of a squared cycle is a standard combinatorial subproblem; the new content claimed here is the complete physical freezing classification, its nontrivial parity-dependent conflict-graph decomposition, and the resulting exact finite-volume census and asymptotic probability for FA2f on the specified geometry. No claim is made that generic cycle-independent-set counting or the terminology of open packing is new.

## Limitations
The result describes fully immobile microstates only: it does not classify all disconnected dynamical sectors, transient lifetimes, bootstrap closure, spectral gaps, or finite-time persistence. It assumes nonzero spin-flip rates whenever the constraint allows a move. It does not cover ladders with open ends, additional diagonal bonds, more than two legs, nor ring sizes below three. The novelty assessment is bibliographic rather than exhaustive; unlocated prior work on open-packing polynomials for cylindrical ladders remains a possible overlap risk. Independent scientific validation has not been performed.

## References
1. N. Cancrini, F. Martinelli, C. Roberto, C. Toninelli, *Relaxation times of kinetically constrained spin models with glassy dynamics*, arXiv:cond-mat/0603745v1 (first posted 2006-03-28), https://arxiv.org/abs/cond-mat/0603745.
2. B. Brešar, S. Klavžar, D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1 (2023), https://arxiv.org/abs/2309.04963.
3. J. A. Fredrickson, H. C. Andersen, *Kinetic Ising Model of the Glass Transition*, Physical Review Letters **53** (1984), 1244–1247, https://doi.org/10.1103/PhysRevLett.53.1244.
