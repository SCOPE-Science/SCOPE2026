# A six-residue minimum-function census for total perfect Roman domination on cyclic prisms

## Finding
For every integer \(n\ge3\), let \(Y_n=C_n\square K_2\), with labelled vertices \((i,r)\), where \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\). A total perfect Roman dominating function (TPRDF) assigns labels \(0,1,2\) to vertices, requires every zero-labelled vertex to have **exactly one** two-labelled neighbor, and requires every positive-labelled vertex to have a positive-labelled neighbor. Write \(\gamma_{tR}^{p}(Y_n)\) for the minimum label sum and \(A_n\) for the number of minimizers (vertices and both rails are labelled, with no quotient by automorphisms).

For \(n=6k+r\), with \(r\in\{0,1,2,3,4,5\}\) and \(n\ge3\), the answer is

| \(r\) | \(\gamma_{tR}^{p}(Y_n)\) | \(A_n\) |
|---|---:|---:|
| \(0\) | \(8k\) | \(9\) |
| \(1\) | \(8k+2\) | \(5n\) |
| \(2\) | \(8k+4\) | \(\dfrac{n(n^3-2n^2+17n-52)}4\) |
| \(3\) | \(8k+4\) | \(3\) |
| \(4\) | \(8k+6\) | \(3n^2\) |
| \(5\) | \(8k+7\) | \(6n\) |

The exceptional parity effect is at \(n\equiv2\pmod6\): the natural cubic-regular-graph bound \(\lceil4n/3\rceil\) is missed by exactly one. At \(n\equiv5\pmod6\) the same bound is achieved. The minimum multiplicity changes from constant to linear, quadratic, and quartic by congruence class.

## Assumptions and scope
All graphs are finite, simple, undirected and unweighted. The cycle has at least three vertices; its two directions are distinct neighboring columns. The TPRDF definition includes the induced-positive-subgraph condition even at vertices labelled \(2\). The count \(A_n\) enumerates functions, not graph automorphism orbits.

## Proof
**Step 1: Exact transfer.** Put \(\Sigma=\{0,1,2\}^2\) (the nine column labels). For \(a,b,c\in\Sigma\), let \(\operatorname{Good}(a,b,c)\) mean that for each rail \(r\in\{0,1\}\): when \(b_r=0\), exactly one of \(a_r,c_r,b_{1-r}\) equals \(2\); when \(b_r>0\), at least one of these three values is positive. Define an \(81\)-state directed transfer on ordered pairs \((a,b)\in\Sigma^2\). Its transition \((a,b)\to(b,c)\) is allowed precisely when \(\operatorname{Good}(a,b,c)\), with weight \(u(b)=b_0+b_1\). Thus

\[
\mathcal P_n(z)=\sum_{f\text{ TPRDF on }Y_n} z^{\sum_v f(v)}
=\operatorname{tr}(M(z)^n)\qquad(n\ge3),
\]

where allowed transitions of \(M(z)\) carry \(z^{u(b)}\). The identity follows by reading the cyclic column sequence, checking each column once; it is a weight-preserving bijection, not an approximation.

**Step 2: Nonnegative reduced cost and the parity obstruction.** On every allowed transition \(e:s\to t\), assign initial integer cost \(c(e)=3u(b)-4\). Compute potentials \(h(s)\) as the shortest distances from an extra zero-cost source to all states. The attached `verify_prism_tpr.cpp` constructs these \(81\) potentials by Bellman--Ford and verifies that all \(468\) transitions have reduced cost

\[
\widetilde c(e)=c(e)+h(s)-h(t)\ge0.
\]

All potentials and reduced costs are integers, and the edge checks are exhaustive. Reduced costs telescope around any closed transfer walk; hence for a TPRDF of weight \(w\), its reduced cost is \(d=3w-4n\). In particular \(d\ge0\), proving \(w\ge\lceil4n/3\rceil\).

There are \(105\) reduced-cost-zero transitions. The zero-cost directed graph has exactly two cyclic strongly connected components, each a simple directed cycle, of lengths \(3\) and \(6\). For each reduced-cost-one transition, exhaustive reachability on state-residue pairs \((s,\ell\bmod6)\) finds the possible lengths of a zero-cost return path. Exactly six such transitions can close a walk; each has total closed length congruent to \(5\) modulo \(6\). Therefore a closed walk of reduced cost one cannot have length \(2\pmod6\). This sharpens the lower bound by one in precisely that residue class.

**Step 3: Exact low-cost closed-walk polynomials.** Let \(B(q)\) be the \(81\)-state matrix with allowed entry \(q^{\widetilde c(e)}\), and put

\[
H_{n,d}=[q^d]\operatorname{tr}(B(q)^n),\qquad
\Phi_d(t)=\sum_{n\ge1}H_{n,d}t^n.
\]

For all positive \(n\), the following four coefficient laws hold, where unspecified entries are zero:

- \(H_{n,0}=3\) when \(n\equiv3\pmod6\), and \(H_{n,0}=9\) when \(n\equiv0\pmod6\).
- \(H_{n,1}=6n\) when \(n\equiv5\pmod6\).
- \(H_{1,2}=3\); for \(n\ge2\), \(H_{n,2}=5n\) when \(n\equiv1\pmod6\) and \(H_{n,2}=3n^2\) when \(n\equiv4\pmod6\).
- \(H_{2,4}=7\); for \(n\ge3\), \(H_{n,4}=n(n^3-2n^2+17n-52)/4\) when \(n\equiv2\pmod6\), and \(H_{n,4}=n(12n^2+13n-71)/6\) when \(n\equiv5\pmod6\).

The formal values at lengths one and two are **transfer coefficients only**: they are included to make the generating-series certificate exact, not interpreted as simple cycle-prism graph invariants.

For completeness, the candidate rational series are explicit. With \(y=t^6\),

\[
\begin{aligned}
\Phi_0(t)&=\frac{3t^3+9t^6}{1-y},\\
\Phi_1(t)&=\frac{6t^5(5+y)}{(1-y)^2},\\
\Phi_2(t)&=\frac{5t(1+5y)}{(1-y)^2}
+\frac{12t^4(4+13y+y^2)}{(1-y)^3}-2t,\\
\Phi_4(t)&=\frac{9t^2(-1+109y+457y^2+275y^3+24y^4)}{(1-y)^5}\\
&\quad+\frac{t^5(245+1814y+545y^2-12y^3)}{(1-y)^4}+16t^2.
\end{aligned}
\]

These are equivalent to the residue-class laws by the elementary generating functions for polynomial sequences. Their products by \(D^{d+1}\), in order \(d=0,1,2,4\), are polynomials of degrees \(9,17,28,47\).

Here is the finite-to-infinite certificate for these identities. Let \(P(t,q)=\det(I-tB(q))\) and \(D(t)=P(t,0)\). The two zero-cost directed cycles and all other acyclic zero-cost components give

\[
D(t)=(1-t^3)(1-t^6).
\]

The formal trace identity is \(\sum_{n\ge1}\operatorname{tr}(B(q)^n)t^n=-t\partial_t\log P(t,q)\). Each coefficient \(P_j(t)=[q^j]P(t,q)\) has degree at most \(81\) in \(t\). Expanding \(\log(P/D)\) by powers of \(q\), then differentiating, proves that

\[
D(t)^{d+1}\Phi_d(t)\ \text{is a polynomial of degree at most}\ 81d+9.
\]

Each of the four proposed formulae has a rational size-generating function whose denominator divides \(D(t)^{d+1}\) and whose numerator, after multiplication by that denominator, has degree no greater than the same bound. Indeed the residue-class polynomials have degrees at most \(d\), so their generating functions have denominators dividing \((1-t^6)^{d+1}\), and the isolated length-one/two corrections are polynomials. Thus matching coefficients through degree \(333=81\cdot4+9\), including the formal lengths one and two, is sufficient to establish each identity for all orders. The attached exact-integer verifier computes **every coefficient** \(H_{n,d}\), for \(d=0,1,2,4\) and \(1\le n\le345\), from the nonnegative-cost transition matrix, and checks these explicit formulae. This finite calculation proves the rational identities for **every** positive \(n\), rather than merely extrapolating a numerical sequence.

**Step 4: Extracting the true minima.** As \(3w-4n\equiv-n\pmod3\), possible nonnegative reduced costs occur in the classes \(0,2,1\) when \(n\equiv0,1,2\pmod3\), respectively. The positive counts in Step 3 show that the smallest attainable costs are \(0\) for \(n\equiv0\pmod3\), \(2\) for \(n\equiv1\pmod3\), \(1\) for \(n\equiv5\pmod6\), and \(4\) for \(n\equiv2\pmod6\). In the last case, Step 2 rules out cost \(1\). Solve \(w=(4n+d)/3\) and use the corresponding \(H_{n,d}\) to obtain all six rows in the theorem.

## Verification
The two standalone sources are `verify_prism_tpr.cpp` and `independent_bruteforce.cpp`. Compile with any standards-compliant C++17 compiler using `c++ -O2 -std=c++17`. The first independently constructs the entire transfer and potential system, checks its zero-cost cycles and one-cost closure residue, and evaluates all \(81\) closed-walk starts at every length up to \(345\) using exact unsigned 128-bit integers. Its success message is `PRISM_TPR_VERIFIED_345`. The second uses direct ternary enumeration of labelled functions on the original graph (not the transfer) for \(3\le n\le7\), producing minima and counts \((4,3),(6,48),(7,30),(8,9),(10,35)\). No floating-point computations, heuristic search, or unproved extrapolation are used in the claim.

## Relationship to prior work
Almulhim (2023) introduced total perfect Roman domination and proved general bounds, complexity results and tree characterizations; its complete accessible text does not state the cyclic-prism weight or minimum-function census. Almulhim, Akwu and Al Subaiei (2022) studied **perfect Roman domination without the total condition** on Cartesian products and obtained bounds on grids and cylinders; the condition differs essentially. An exact published calculation for **open** two-row ladders has the same TPRDF definition but does not imply the cyclic case: joining the two ends changes each zero vertex's exact count of neighboring defenders and can change whether a positive vertex is isolated. The six-residue counts here are for cyclic ladders and are proved by a separate transfer certificate.

## Limitations
The theorem concerns ordinary labelled cyclic prisms \(C_n\square K_2\), with \(n\ge3\). It gives the minimum weight and its multiplicity, not a combinatorial classification of each minimizer or the entire all-weight polynomial in closed form (although the transfer computes the latter). The mathematical proof includes an explicitly reproducible finite exact certificate. Independent expert validation and exhaustive historical-priority clearance have not been performed.

## References
1. A. Almulhim, *Total Perfect Roman Domination*, Symmetry 15(9), 1676 (2023), DOI: 10.3390/sym15091676, https://www.mdpi.com/2073-8994/15/9/1676 (first public source used: 2023-08-31).
2. A. Almulhim, A. D. Akwu, and B. Al Subaiei, *The Perfect Roman Domination Number of the Cartesian Product of Some Graphs*, Journal of Mathematics 2022, 1957027 (published 2022-10-18), DOI: 10.1155/2022/1957027.
