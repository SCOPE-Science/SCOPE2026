# Exact crystalline endpoints and fractional-density laws on a triangular maximal hard-core strip

## Finding
Consider the maximal hard-core gas on the width-two oriented triangular-ladder graph described below. The number of occupied sites in any maximal independent set on a periodic strip of \(n\ge4\) rungs lies between the exact bounds
\[
\left\lceil\frac{2n}{5}\right\rceil \le |I|\le \left\lfloor\frac{2n}{3}\right\rfloor.
\]
Both bounds are attained for **every** such \(n\). If \(5\mid n\), exactly five configurations attain the lower bound; they are the translates of the five-column pattern \((A,0,B,0,0)\). If \(3\mid n\), exactly three attain the upper bound; they are the translates of \((A,B,0)\).

For activity \(z>0\), the finite-volume partition polynomial satisfies a fixed order-five recurrence, and the infinite-strip pressure is analytic for all positive activities. Its Perron root \(\Lambda(z)\), and mean occupancy \(\theta(z)\) *per rung*, have fractional-power endpoint laws:
\[
\begin{aligned}
\Lambda(z)&=z^{2/5}\left(1+\tfrac25z^{1/5}+O(z^{2/5})\right),
&\theta(z)&=\tfrac25+\tfrac{2}{25}z^{1/5}+O(z^{2/5})&& (z\downarrow0),\\
\Lambda(z)&=z^{2/3}\left(1+\tfrac23z^{-1/3}+O(z^{-2/3})\right),
&\theta(z)&=\tfrac23-\tfrac29z^{-1/3}+O(z^{-2/3})&&(z\to\infty).
\end{aligned}
\]
Thus the finite-width model has two distinct commensurate low- and high-activity crystalline patterns but **no** positive-activity phase transition. The pressure per site is \(\tfrac12\log\Lambda(z)\); the mean density per site is \(\theta(z)/2\).

## Assumptions and scope
For each integer \(n\ge4\), let \(G_n\) have vertices \((i,U)\) and \((i,L)\), indexed by \(i\in\mathbb Z/n\mathbb Z\). Its undirected edges are the vertical rungs \(\{(i,U),(i,L)\}\), the horizontal upper/lower edges \(\{(i,U),(i+1,U)\}\), \(\{(i,L),(i+1,L)\}\), and the oriented diagonals \(\{(i,L),(i+1,U)\}\). Only this one diagonal orientation is present; there are **not** two diagonals in every cell. An independent set is maximal exactly when every unoccupied vertex has an occupied neighbor. We sum \(z^{|I|}\) over maximal independent sets \(I\), writing \(Z_n(z)\) for the partition polynomial. Column states are \(0\) (empty), \(A\) (upper occupied) and \(B\) (lower occupied). The graph is a finite-width periodic strip, not the full two-dimensional triangular lattice and not a transverse periodic cylinder.

## Proof
**1. Exact local transfer.** Independence permits the consecutive-column transitions \(0\to0,A,B\), \(A\to0,B\), and \(B\to0\). For a triple \((a,b,c)\) with \(b=0\), maximality at the central column requires both
\[
(a\ne0\ \text{or}\ c=A),\qquad(a=B\ \text{or}\ c\ne0).
\]
If \(b\ne0\), its one unoccupied vertex is dominated through the rung. This condition enforces maximality at every vertex of a periodic configuration. Use the pair states \((00,0A,0B,A0,AB,B0)\) in that order, and give a transition \((a,b)\to(b,c)\) weight \(z\) when \(c\in\{A,B\}\), otherwise weight \(1\). The resulting transfer is
\[
T(z)=\begin{pmatrix}
0&z&0&0&0&0\\
0&0&0&1&z&0\\
0&0&0&0&0&1\\
0&z&z&0&0&0\\
0&0&0&0&0&1\\
1&z&z&0&0&0
\end{pmatrix}.
\]
Every periodic configuration corresponds bijectively to one closed walk of length \(n\), weighted by exactly its occupied-column count. Consequently
\[
Z_n(z)=\operatorname{tr}T(z)^n,
\quad\det(tI-T)=t\bigl(t^5-2zt^3-z^2t^2-z^2t-z^2\bigr).
\]
The characteristic identity (obtained by direct determinant expansion) gives the exact recurrence, for integers \(n\ge1\),
\[
Z_{n+5}=2zZ_{n+3}+z^2Z_{n+2}+z^2Z_{n+1}+z^2Z_n.
\]
For example \(Z_4=12z^2\), \(Z_5=5z^2+10z^3\), and \(Z_6=28z^3+3z^4\).

**2. Sharp global occupation bounds.** Label every allowed directed pair-state edge by \(w=1\) if its new column is occupied and \(w=0\) otherwise. In the fixed state order above, define the integer potentials
\[
h_-=(-4,-1,0,-3,0,-2),\qquad h_+=(0,-1,-1,0,-2,0).
\]
Inspection of the ten allowed edges verifies the two inequalities
\[
5w-2+h_-(u)-h_-(v)\ge0,\qquad 2-3w+h_+(u)-h_+(v)\ge0.
\]
Summing over any length-\(n\) closed walk telescopes the potential and yields \(5|I|-2n\ge0\) and \(2n-3|I|\ge0\). Equality in the first edge inequality is possible on just one directed cycle (other equality edges are noncyclic), namely
\[
00\to0A\to A0\to0B\to B0\to00,
\]
and equality in the second is possible on just one directed cycle, namely
\[
0A\to AB\to B0\to0A.
\]
These unique equality cycles yield respectively five and three cyclic translates in periods divisible by their lengths.

For completeness, all the integer-rounded bounds are attained, not merely the divisible cases. Three closed walks based at \(0A\) have (length, occupancy) pairs \((2,1)\), \((3,2)\), \((5,2)\), corresponding respectively to \(0A\to A0\to0A\), \(0A\to AB\to B0\to0A\), and the preceding five-cycle. Concatenating these cycles gives length \(n\) with minimum occupancy \(\lceil2n/5\rceil\): use five-cycles for multiples of five; for residues \(2,3,4\) add respectively one two-cycle, one three-cycle, or two two-cycles; for residue \(1\), replace one five-cycle by three two-cycles. (The last operation requires \(n\ge6\), automatically true here.) For the upper bound, use three-cycles for multiples of three, add a two-cycle for residue two, and replace one three-cycle by two two-cycles for residue one. This works for every \(n\ge4\), proving both formulas.

**3. Perron root and endpoint laws.** The transfer digraph is strongly connected and has closed walks of lengths two and three, hence its nonnegative matrix is primitive for each \(z>0\). Its Perron eigenvalue \(\Lambda(z)\) is strictly positive, simple, larger in modulus than every other eigenvalue, and analytic in positive \(z\). Therefore \(\lim_{n\to\infty}\tfrac1n\log Z_n(z)=\log\Lambda(z)\), and thermodynamic differentiation gives \(\theta(z)=z\Lambda'(z)/\Lambda(z)\).

For small activity put \(z=s^5\), \(\Lambda=s^2 y\). The nonzero eigenvalue equation becomes
\[
y^5-1-2sy^3-s^2y-s^4y^2=0.
\]
At \((s,y)=(0,1)\) the derivative with respect to \(y\) is \(5\), so the analytic implicit-function theorem gives \(y=1+2s/5+O(s^2)\). For large activity put \(s=z^{-1/3}\), \(\Lambda=z^{2/3}y\). This yields
\[
y^5-y^2-2sy^3-s^2y-s^4=0,
\]
whose derivative with respect to \(y\) at \((0,1)\) is \(3\), giving \(y=1+2s/3+O(s^2)\). The positive Perron root is the positive branch in both limits (its power exponent is also trapped between the proven occupation bounds). Differentiating the resulting convergent fractional-power expansions proves the stated occupancy laws. Analyticity forbids a positive-activity singularity on the fixed-width strip.

## Verification
Run `python3 verify.py` using the accompanying standard-library checker. It independently enumerates all \(2^{2n}\) candidate vertex subsets for \(4\le n\le8\), checks graph-theoretic independence and maximality, and compares the full counting polynomial with a pair-state transfer computation. It checks both potential inequalities on every allowed edge, the endpoint counts, and the characteristic matrix identity at four positive integer activities. Separately, symbolic exact-arithmetic expansion of the displayed six-by-six determinant gives the stated polynomial. The finite tests are consistency checks, not substitutes for the all-size proof or the two analytic limits.

## Relationship to prior work
Wang, Barg and Kashyap introduce and analyze the maximal hard-core gas on the **full triangular lattice**, obtaining coexistence and crystalline phase information. Their general model, its maximality constraint and associated physical motivation are prior. Barg, He and Wang subsequently discuss a general framework for crystallization of maximal hard-core models on periodic graphs. The present result isolates a distinct, explicitly defined **two-row periodic strip** and derives its exact complete occupation endpoints, the weighted order-five transfer recurrence and fractional-density endpoint coefficients. None of those precise finite-strip statements was located in the inspected primary text or in targeted independent-domination and transfer-matrix searches. Generic transfer-matrix and Perron–Frobenius methods are classical and are not claimed as inventions.

## Limitations
This is a two-row, one-direction-diagonal periodic strip; it does not prove any full two-dimensional triangular-lattice phase boundary or a macroscopic phase transition. The end-pattern uniqueness claims apply only when the corresponding period divides \(n\); for other periods the proof establishes only extremal occupation numbers. The term \(O(\cdot)\) refers to the indicated one-sided activity limit. A previously unindexed explicit ladder generating polynomial or a stronger independent-domination theorem could cover part of these formulas; bibliographic novelty remains subject to independent verification.

## References
1. G. Wang, A. Barg and N. Kashyap, *The maximal hard-core model on the triangular lattice*, arXiv:2602.18310, first submitted 2026-02-20. https://arxiv.org/abs/2602.18310 ; full text https://arxiv.org/html/2602.18310.
2. A. Barg, Q. He and G. Wang, *A general framework for crystallization in maximal hard-core models*, arXiv:2610.11042, first submitted 2026-10-08. https://arxiv.org/abs/2610.11042.
3. L. Dall'Asta, P. Pin and A. Ramezanpour, *Statistical mechanics of maximal independent sets*, Physical Review E 80, 061136 (2009). https://doi.org/10.1103/PhysRevE.80.061136.
