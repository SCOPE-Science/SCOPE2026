# Complete ternary two-sum fibers and additive energy of connected-noncrossing-graph nondivisibility indices

## Finding

Let \(N_n\) count connected noncrossing graphs with vertex labels \(1,\ldots,n\) placed in circular order. For every integer \(r\ge1\), write
\[
S_r=\{n\in\mathbb Z:1\le n<3^r,\ 3\nmid N_n\},\qquad
R_r(t)=\#\{(a,b)\in S_r^2:a+b\equiv t\pmod{3^r}\}.
\]
The ordered pair in the definition of \(R_r\) is significant: \((a,b)\) and \((b,a)\) are separately counted when different. Let \(H_j(r)=\#\{t\in\mathbb Z/3^r\mathbb Z:R_r(t)=j\}\). Then, for every \(r\ge2\), every \(R_r(t)\) lies in \(\{0,1,2,3,4,5,6\}\), and the **complete** multiplicity histogram is
\[
\begin{aligned}
H_1(r)&=1,&H_2(r)&=2,\\
H_3(r)&=1+r+\binom r2,&
H_4(r)&=3\binom r3+r^2+r-4,\\
H_5(r)&=r-2,&
H_6(r)&=\binom r4+\binom r3+\binom{r-2}2,\\
H_0(r)&=3^r-\sum_{j=1}^{6}H_j(r).
\end{aligned}
\]
Here binomial coefficients with a smaller upper index than lower index are zero. At \(r=1\), instead \((H_0,H_1,H_2)=(0,2,1)\), and all higher multiplicities vanish.

Precisely the targets of ternary digit sum at most four are representable:
\[
S_r+S_r=\{t\bmod3^r: s_3(t)\le4\},
\qquad
|S_r+S_r|=1+2r+4\binom r2+4\binom r3+\binom r4.
\]
In particular, \(R_r(t)\le6\), and for \(r\ge3\) the upper bound six is attained at precisely \(H_6(r)\) residues. The total ordered additive energy is exactly
\[
E_r:=\sum_{t\bmod3^r}R_r(t)^2
=\#\{(a,b,c,d)\in S_r^4:a+b\equiv c+d\pmod{3^r}\}
=\frac{3r^4+10r^3+26r^2-51r+24}{2}.
\]
Thus \(E_r\sim \tfrac32r^4\), while \(|S_r|=r(r+3)/2\) and \(|S_r+S_r|\sim r^4/24\).

## Assumptions and scope

All sums are taken in the cyclic group \(\mathbb Z/3^r\mathbb Z\), not as ordinary integer sums. The index set excludes \(n=0\), for which \(N_n\) is not used. The established Deutsch--Sagan congruence, proved by Eu--Liu--Yeh and independently by Gessel, says
\[
N_n\not\equiv0\pmod3\quad\Longleftrightarrow\quad s_3(n)\in\{1,2\}\qquad(n\ge1).
\]
In fact it states that \(N_n\equiv1\pmod3\) for a power of three or twice one, and \(N_n\equiv2\pmod3\) for a sum of two distinct powers of three. Consequently
\[
S_r=\{3^i,2\cdot3^i:0\le i<r\}\ \cup\ \{3^i+3^j:0\le i<j<r\}.
\]
No conjectural property of the graph counts or their higher-prime-power congruences is needed.

## Proof

**1. Exact support.** The ordinary base-three digit sum is subadditive under addition because carrying replaces three units at one position by one unit at the next. Discarding the final carry at modulus \(3^r\) cannot increase digit sum. Every member of \(S_r\) has digit sum one or two, hence every pair sum has digit sum at most four. Conversely, a target whose digit sum is in \(\{2,3,4\}\) can have its digit units partitioned into two nonempty groups, each with one or two units, giving an ordinary carry-free sum of two members of \(S_r\). To represent zero, use \(3^{r-1}+2\cdot3^{r-1}\). To represent \(3^i\) for \(i<r-1\), use \((3^{r-1}+3^i)+2\cdot3^{r-1}\); to represent \(3^{r-1}\), use \(2\cdot3^{r-1}+2\cdot3^{r-1}\). These are all congruences modulo \(3^r\), and cover every digit sum zero or one. Enumeration of the four possible digit-sum levels proves the displayed support cardinality.

**2. An exact finite-state machine for every fiber.** For digits \(a_i,b_i,t_i\in\{0,1,2\}\), write the usual addition carry relation
\[
a_i+b_i+c_i=t_i+3c_{i+1},\qquad c_i\in\{0,1\},\quad c_0=0.\]
Track both partial digit sums in the truncated coefficient ring \(\mathbb Z[X,Y]/(X^3,Y^3)\). Relative to carries \(c_i=0,1\), the three digit transitions, with row indicating incoming carry, are
\[
M_0=\begin{pmatrix}1&XY^2+X^2Y\\0&X^2+XY+Y^2\end{pmatrix},\quad
M_1=\begin{pmatrix}X+Y&X^2Y^2\\1&XY^2+X^2Y\end{pmatrix},\quad
M_2=\begin{pmatrix}X^2+XY+Y^2&0\\X+Y&X^2Y^2\end{pmatrix}.
\]
For \(t=\sum_{i=0}^{r-1}t_i3^i\), multiply \((1,0)M_{t_0}\cdots M_{t_{r-1}}\), sum both carry coordinates (because the outgoing carry is ignored modulo \(3^r\)), and sum coefficients of \(X^aY^b\) for \(1\le a,b\le2\). This number is exactly \(R_r(t)\): truncation rejects digit sums greater than two, and the coefficient extraction rejects zero digit sums. Every pair of admitted inputs has a unique path through the standard carry equations.

Enumerating states as *exact 18-dimensional integer coefficient vectors* under all three transitions reaches precisely 18 states, numbered from the initial vector as state zero. The following complete transition table gives the output fiber value and the next state on digits 0, 1, and 2. It is a finite, exactly reproducible certificate rather than an extrapolation from sample moduli.

| State | Fiber | Digit 0 | Digit 1 | Digit 2 |
|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 2 | 3 |
| 1 | 2 | 1 | 4 | 5 |
| 2 | 1 | 6 | 7 | 8 |
| 3 | 1 | 3 | 8 | 9 |
| 4 | 3 | 10 | 11 | 8 |
| 5 | 3 | 5 | 8 | 9 |
| 6 | 2 | 6 | 12 | 8 |
| 7 | 3 | 7 | 13 | 14 |
| 8 | 4 | 8 | 14 | 15 |
| 9 | 3 | 9 | 15 | 15 |
| 10 | 4 | 10 | 16 | 8 |
| 11 | 5 | 11 | 13 | 14 |
| 12 | 4 | 12 | 13 | 14 |
| 13 | 6 | 13 | 17 | 15 |
| 14 | 4 | 14 | 15 | 15 |
| 15 | 0 | 15 | 15 | 15 |
| 16 | 6 | 16 | 13 | 14 |
| 17 | 6 | 17 | 15 | 15 |

Let \(T\) be the \(18\times18\) integer matrix whose row for a state counts its three successors, with repeated successors counted repeatedly. Direct integer matrix multiplication, certified by `fiber_certificate.py`, establishes the exact identity
\[
T^2(T-3I)(T-I)^5=0.
\]
The vector of state populations after \(r\) digits is the initial row vector times \(T^r\). Therefore every multiplicity count \(H_j(r)\) satisfies the homogeneous recurrence given by \(z^2(z-3)(z-1)^5\) in the shift operator. The displayed formulas are, for \(r\ge2\), polynomials of degree at most four plus (only for \(H_0\)) a term \(3^r\); their exceptional values at \(r=0,1\) are annihilated by the factor \(z^2\). Both families satisfy the same order-eight recurrence, and the exact certificate verifies their agreement at depths \(r=0,\ldots,7\). Induction by that recurrence proves the histogram for **all** \(r\ge1\). Since no automaton state has fiber greater than six, the bound is global.

**3. Energy.** Summing \(j^2H_j(r)\) and simplifying the binomial polynomials yields exactly the stated quartic energy formula, including \(r=1\). This counts cyclic additive quadruples, not just ordinary-integer collisions.

## Verification

Run `python fiber_certificate.py` and `python independent_energy_check.py` with Python 3; both files are self-contained and need only the standard library. The first reconstructs every reachable symbolic carry state from its 18 coefficients, checks the entire transition table, performs the complete 18-by-18 integer annihilator multiplication, and checks histograms through depth 17. The second independently counts pairs and energies for depths up to 10 and computes cyclic additive energy from a separate four-input carry model through depth 17. Its rational-generating-function argument is corroborative; the all-depth result does not depend on any unverified numerical extrapolation. The first eight depths together with the matrix identity supply the finite-to-infinite certificate. At depths \(r=1,2,3,4\), direct energies are \(6,77,309,822\).

## Relationship to prior work

Deutsch and Sagan's 2004 congruence study conjectured the exact ternary nondivisibility pattern; Eu, Liu, and Yeh proved it; Gessel's 2014 short proof derives it directly from the mod-three graph generating function. Those results establish **membership in** \(S_r\), rather than ordered cyclic pair-sum fibers, the complete histogram, or energy. Krattenthaler and Müller's 2025 paper develops stronger prime-power congruences for the original graph-count values; these do not imply the new additive-index fiber formulas without a separate carry analysis. Green's 2025 digital Waring paper gives general additive-energy **bounds** for sets with few nonzero centered digits, but not this exact ternary digit-sum-weight-two residue histogram or quartic cyclic energy. Related exact digital-sum energy formulas for different binary sets do not imply this theorem, because the digit restrictions and carries differ.

## Limitations

This is an exact all-depth statement for ordered two-sums of the **indices** with \(3\nmid N_n\), not about sums of the graph-count values themselves. It covers the bound two on ternary digit sum and does not assert a comparable fixed bound for larger digit-sum thresholds or another prime. The originality comparison has the normal limitation that an older formula or more general finite-state result might implicitly subsume the classification; published-priority independence is not certified, and no independent mathematical audit has been performed. The 2005/2006 Eu--Liu--Yeh primary publication was checked at the abstract/bibliographic level; the fully accessible Gessel proof supplies the required original congruence premise independently.

## References

1. E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326v1, first public version 19 July 2004. https://arxiv.org/abs/math/0407326
2. S.-P. Eu, S.-C. Liu and Y.-N. Yeh, *On the Congruences of Some Combinatorial Numbers*, Studies in Applied Mathematics 116 (2006), 135–144, DOI:10.1111/j.1467-9590.2006.00337.x. https://doi.org/10.1111/j.1467-9590.2006.00337.x
3. I. M. Gessel, *A short proof of the Deutsch–Sagan congruence for connected non crossing graphs*, arXiv:1403.7656v1, 29 March 2014. https://arxiv.org/abs/1403.7656
4. C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(p^k\) behaviour of recursive sequences*, Aequationes mathematicae 99 (2025), 2505–2547, DOI:10.1007/s00010-025-01195-0. https://doi.org/10.1007/s00010-025-01195-0
5. B. Green, *Waring's problem with restricted digits*, Compositio Mathematica 161 (2025), 341–364, DOI:10.1112/S0010437X24007723. https://doi.org/10.1112/S0010437X24007723
