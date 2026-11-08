# Exact chip-mass polynomial and Gaussian law for primitive two-cycles on finite rings

## Finding
For every integer \(n\ge3\), consider synchronous parallel chip-firing on the labelled, simple cycle \(C_n\). A configuration is an \(n\)-tuple of nonnegative integers. A vertex fires one chip to each of its two neighbours if and only if it has at least two chips, and all firings occur simultaneously. Write \(F\) for the update map and \(|x|=\sum_i x_i\) for the conserved chip count. Let
\[
H_n(z)=\sum_{\substack{x\in\mathbb Z_{\ge0}^{n}\\F^2x=x,\ Fx\ne x}}z^{|x|}.
\]
Then the following two exact forms agree, as integer polynomials:
\[
\boxed{H_n(z)=2\sum_{\substack{0\le r\le\lfloor n/2\rfloor\\r\equiv n\pmod2}}
\frac{n}{n-r}\binom{n-r}{r}z^{n+r}(1+z)^{n-2r}.}
\tag{1}
\]
Define \(\lambda_\pm(z)=\frac{z}{2}\bigl(1+z\pm\sqrt{1+6z+z^2}\bigr)\). Equivalently,
\[
\boxed{H_n(z)=\lambda_+(z)^n+\lambda_-(z)^n+(-z)^n+(-z^2)^n.}
\tag{2}
\]
The radical cancels between the first two terms. For even \(n\), the positive coefficients have precisely exponents \(n,n+1,\dots,2n\), with endpoint coefficients both \(2\). For odd \(n\), they have precisely exponents \(n+1,\dots,2n-1\), with endpoint coefficients both \(2n\). There are no other primitive two-cycle chip totals. The exact total number of primitive-two configurations is
\[
\boxed{H_n(1)=(1+\sqrt2)^n+(1-\sqrt2)^n+2(-1)^n,}
\]
and half this number is the number of distinct temporal two-cycle orbits.

If \(X_n\) is sampled uniformly from these initially primitive-two configurations and \(M_n=|X_n|\), then \(\mathbb E[M_n]=3n/2\) exactly and
\[
\boxed{\frac{M_n-3n/2}{\sqrt n}\ \Longrightarrow\ \mathcal N\!\left(0,\frac{\sqrt2}{8}\right)}
\qquad(n\to\infty).
\tag{3}
\]
Here the second argument of \(\mathcal N\) is the *variance*, not the standard deviation. This is a limit conditional on uniform sampling from the initially periodic primitive-two class, not on uniformly sampled arbitrary initial states or on eventual attraction basins.

## Assumptions and scope
The ring is labelled and undirected, and \(n\ge3\) so the two incident neighbours of a vertex are distinct. All site counts are unbounded nonnegative integers, and the firing threshold is exactly two. No dissipative sink, asynchronous update, or stochastic transition is present. Only configurations *already on a least-period-two orbit at time zero* are enumerated. Period-one states, transient precursors, and periodic orbits of larger length are deliberately excluded. Formula (1) is valid for every \(n\ge3\), including odd rings.

## Proof
**1. Universal firing-frequency reduction.** Put \(s_i(t)={\bf1}_{\{x_i(t)\ge2\}}\) and \(k_i(t)=s_{i-1}(t)+s_{i+1}(t)\), indexing modulo \(n\). The update is \(x_i(t+1)=x_i(t)-2s_i(t)+k_i(t)\). If \(F^2x=x\), then the vector \(s(0)+s(1)\) is annihilated by the cycle Laplacian. Connectedness implies this integer vector is constant, with common value in \(\{0,1,2\}\). If it is zero, no vertex ever fires and \(Fx=x\); if it is two, every vertex fires and again \(Fx=x\). Thus every primitive two-cycle has \(s_i(1)=1-s_i(0)\) at *every* vertex. Conversely, if the firing indicators complement after one update, then the two-step update is zero at each site because every site and each neighbour fires once in the two steps. The next firing indicators are again the original ones, giving a genuine two-cycle.

**2. Exact local feasibility.** Fix \(s=s(0)\in\{0,1\}^n\) and let \(k_i=s_{i-1}+s_{i+1}\). The feasible initial chip counts with the required complementary next firing indicator are exactly:
\[
\begin{array}{c|ccc}
 &k_i=0&k_i=1&k_i=2\\\hline
s_i=0&\varnothing&\{1\}&\{0,1\}\\
s_i=1&\{2,3\}&\{2\}&\varnothing
\end{array}
\]
These inequalities follow directly from \(s_i={\bf1}_{\{x_i\ge2\}}\) and \(1-s_i={\bf1}_{\{x_i-2s_i+k_i\ge2\}}\). In particular all primitive-two configurations have chip counts at most three. The forbidden local patterns are precisely three consecutive equal firing bits, so a phase word \(s\) is feasible if and only if it has no cyclic \(000\) or \(111\) triple.

**3. A matching and parity encoding.** Mark an edge whenever its endpoints carry equal firing bits. Since triples of equal bits are forbidden, marked edges form a matching. Let \(r\) be the number of marks. Exactly \(n-r\) edges change the firing bit, which must be even around a ring. Hence \(r\equiv n\pmod2\). Conversely, every matching of size \(r\) satisfying that parity condition determines exactly two firing words, interchanged by bit complementation. The number of size-\(r\) matchings of \(C_n\) is
\[
\frac{n}{n-r}\binom{n-r}{r};
\]
this follows by counting arrangements of \(r\) nonadjacent selected cyclic edges, including the case \(r=0\).

Every marked edge has two distinct incident vertices, each with one equal and one unequal neighbour, thus an initial chip count forced to \(1\) or \(2\). All other \(n-2r\) sites have two choices: either \(0,1\) if waiting with two firing neighbours, or \(2,3\) if firing with two waiting neighbours. To calculate their total-chip weights without dependence on the number of firing sites, note that conservation gives \(2|x|=\sum_i(x_i(0)+x_i(1))\). At each of the \(2r\) forced sites this two-time sum is exactly \(3\). At each remaining site it is either \(2\) or \(4\), independently according to its lower or upper initial chip choice. Thus \(|x|=n+r+h\), where \(h\in\{0,\dots,n-2r\}\) counts upper choices, and the weight polynomial for either firing word is \(z^{n+r}(1+z)^{n-2r}\). Multiplying by two firing words and the matching count gives (1), with neither omissions nor overcounting.

**4. Transfer polynomial and closed form.** Let \(I_n(a,w)=\sum_r\frac{n}{n-r}\binom{n-r}{r}a^{n-2r}w^r\) be the matching polynomial of the cyclic edge set with vertex fugacity \(a\) and marked-edge weight \(w\). For \(n\ge3\), its standard two-state cyclic transfer gives \(I_n(a,w)=\alpha_+^n+\alpha_-^n\), where \(\alpha_\pm=(a\pm\sqrt{a^2+4w})/2\). Filtering \(r\equiv n\pmod2\) yields
\[
H_n(z)=z^n\bigl(I_n(1+z,z)+(-1)^nI_n(1+z,-z)\bigr).
\]
In the second term, \((1+z)^2-4z=(1-z)^2\), so the two transfer roots are \(1\) and \(z\). Substituting the first term's roots yields (2).

**5. Sharp bands, exact orbit number, and symmetric mean.** The smallest permitted \(r\) is zero if \(n\) is even and one if \(n\) is odd. The corresponding positive summand in (1) has support on *every integer* between its extremal powers, with strictly positive coefficients. Every larger \(r\) contributes only within a narrower interval \([n+r,2n-r]\). The endpoint counts follow from \(r=0\) or from \(\frac{n}{n-1}\binom{n-1}{1}=n\) for \(r=1\). Evaluation of (2) at \(z=1\) proves the Pell–Lucas expression. Every primitive-two orbit has exactly two configurations, yielding half the count as orbits. The sum (1) is palindromic about exponent \(3n/2\): each summand is fixed by \(z\mapsto 1/z\) after multiplying by \(z^{3n}\). This proves \(\mathbb E[M_n]=3n/2\) exactly.

**6. Gaussian chip-mass fluctuations.** For real \(t\) near zero, the positive dominant root has analytic logarithm
\[
\log\lambda_+(e^t)=\frac{3t}{2}+\operatorname{arsinh}\bigl(\cosh(t/2)\bigr).
\]
The other three terms in (2) are exponentially smaller uniformly for sufficiently small \(|t|\), since at \(t=0\) their moduli are less than \(1+\sqrt2\). Therefore the logarithm of the chip-mass moment-generating function is
\[
\log\frac{H_n(e^t)}{H_n(1)}
=n\left[\frac{3t}{2}+\operatorname{arsinh}(\cosh(t/2))-\operatorname{arsinh}(1)\right]+o(1)
\]
locally uniformly in \(t\). The analytic bracket has first derivative \(3/2\), second derivative \(1/(4\sqrt2)=\sqrt2/8\), and third and higher terms \(O(t^3)\). Taking \(t=u/\sqrt n\), subtracting the exact centering \(3n/2\), and using convergence of moment-generating functions proves (3). The lattice nature and parity-dependent finite-size support are retained; no unrestricted local limit theorem is claimed.

## Verification
Two standalone Python 3 standard-library programs are included. `check_direct.py` enumerates every initial state with site counts in \(\{0,1,2,3\}\) for \(3\le n\le9\) (349,504 total labelled states), performs two explicit chip-firing updates, and checks the full mass histogram against formula (1). The proof above establishes why no initially primitive-two state lies outside the enumerated cube. `check_polynomials.py` independently computes the quadratic-root power-sum recurrence of (2), comparing its integer coefficients to the matching formula for all \(3\le n\le150\); it also checks support, endpoints, palindromy and the Pell–Lucas total. Captured outputs are supplied. These finite tests are corroboration, not the proof of the all-size result or the central limit theorem.

## Relationship to prior work
Dall'Asta (2006) analyses the exact microscopic dynamics of the one-dimensional deterministic fixed-energy sandpile, and in particular describes two-site building blocks \(20,21,30,31\) and their reverses for the period-two regime, and the bulk energy-density interval \([1,2]\). The present result *does not claim* the identification of this two-cycle phase is new. Its additional statements are an exact mass-refined polynomial for every labelled finite ring including odd-size boundary defects, a closed Pell–Lucas period-two orbit census, and a conditional Gaussian fluctuation law. Dall'Asta's explicit enumeration elsewhere in the paper is for period populations *at the critical energy endpoints*, not this all-mass primitive-two polynomial. Jiang (2010) treats attainable periods of parallel chip-firing on complete bipartite graphs and general structural aspects, not this energy-resolved ring enumeration. Jiang, Scully and Zhang (2012 preprint, 2015 publication) prove a general restriction on temporal firing patterns and explain ring gliders, rather than counting the precise chip-mass distribution here. The ring count can be derived using Dall'Asta's known block description with additional counting; no assertion is made that the underlying microscopic patterns are previously unknown.

## Limitations
The claim concerns initially primitive-two configurations, not basins of attraction or all periodic states. The Gaussian limit is for the uniform measure on that class only. Finite experiments do not certify the infinite-size theorem. While targeted prior-art searches and the inspected main sources did not locate the mass-polynomial/Pell–Lucas/conditional-CLT package, an older unindexed counting formula or an equivalent unpublished enumeration may exist. The result is a new enumerative refinement of known one-dimensional periodic-state structure, not a new dynamical universality class.

## References
1. L. Dall'Asta, *Exact solution of the one-dimensional deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0601267, first posted January 12, 2006, especially the period-two building-block description and the separate critical-energy count.
2. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, first posted March 4, 2010.
3. T.-Y. Jiang, Z. Scully, Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786, first posted November 29, 2012; published in SIAM J. Discrete Math. 29 (2015), 615–630.
