# A sharp reliability-driven reversal of three-row Kaczmarz sweep order

## Finding
Consider a consistent three-equation system in two unknowns with unit row normals
\[
a_0=\frac{(1,-3)}{\sqrt{10}},\qquad a_1=(1,0),\qquad a_2=\frac{(1,3)}{\sqrt{10}}.
\]
Each of the three distinct row updates is attempted exactly once, in a prescribed permutation. An attempted exact Kaczmarz projection is independently delivered with probability \(p\); a missing update acts as the identity. For an initial error \(e\), let \(e_\pi\) be the resulting error after the three attempts, and define the worst-case squared one-sweep factor
\[
F_\pi(p)=\max_{\|e\|_2=1}\mathbb E\|e_\pi\|_2^2,\qquad 0\le p\le1.
\]
There is exactly one number \(p_*\in(7/8,9/10)\), the unique root in \((0,1)\) of
\[
Q(p)=12231p^5-38171p^4-48500p^3+423000p^2-600000p+250000,
\]
with \(p_*=0.882380124514663\ldots\), at which the optimal order changes:

- For \(0<p<p_*\), exactly the two orders \((1,0,2)\) and \((1,2,0)\) are optimal (central row first).
- At \(p=p_*\), these tie with exactly the two orders \((0,1,2)\) and \((2,1,0)\) (central row between flanking rows).
- For \(p_*<p\le1\), exactly the last two orders are optimal.

The remaining orders \((0,2,1)\) and \((2,0,1)\), which place the central row last, are strictly suboptimal for every \(0<p\le1\). At \(p=0\) all six orders tie. In particular the best deterministic order at perfect delivery is not best when updates are sufficiently unreliable. This is an exact one-sweep mean-square minimax result, not an assertion about long-run or samplewise optimality.

## Assumptions and scope
The row equations \(a_i^{\mathsf T}x=b_i\) are jointly consistent, so the unique solution \(x_*\) exists because the rows span \(\mathbb R^2\). One Kaczmarz update on row \(i\) transforms the error \(e=x-x_*\) by \(P_i e\), where \(P_i=I_2-a_i a_i^{\mathsf T}\). For each attempted row, independently of all others, the error multiplier is \(P_i\) with probability \(p\) and \(I_2\) otherwise. No relaxation, noise in a delivered reading, adaptive ordering or repeated attempts are allowed. A sweep always incurs three attempted updates at equal cost; the result compares the six fixed permutations at that equal budget. The expectation is over exactly the three independent delivery indicators, not over initial errors or right-hand sides.

## Proof
**1. Exact expected energy matrix.** For a deterministic symmetric matrix \(H\), define the positive linear map
\[
\mathcal T_i(H)=(1-p)H+pP_iHP_i.
\]
If the attempted order is \(\pi=(i,j,k)\), conditioning successively on the independent deliveries shows
\[
\mathbb E\|e_\pi\|_2^2=e^{\mathsf T}M_\pi e,
\qquad M_\pi=\mathcal T_i\bigl(\mathcal T_j(\mathcal T_k(I_2))\bigr).
\]
Thus \(F_\pi(p)=\lambda_{\max}(M_\pi)\). Every \(M_\pi\) is positive semidefinite since it is a convex sum of matrices of the form \(X^{\mathsf T}X\). The three projectors are explicitly
\[
P_0=\frac1{10}\begin{pmatrix}9&3\\3&1\end{pmatrix},\quad
P_1=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
P_2=\frac1{10}\begin{pmatrix}9&-3\\-3&1\end{pmatrix}.
\]
Reflection of the second coordinate exchanges rows \(0\) and \(2\). Therefore the six permutations divide into three spectral classes, each of size two, represented by \(C=(0,1,2)\), \(L=(0,2,1)\), and \(E=(1,0,2)\).

**2. Polynomial matrices.** Direct exact multiplication yields, for \(0\le p\le1\),
\[
M_C=\frac1{1000}\begin{pmatrix}
143p^3+66p^2-1200p+1000&3p^2(74-73p)\\
3p^2(74-73p)&27p^3+774p^2-1800p+1000
\end{pmatrix},
\]
\[
M_L=\frac1{1250}\begin{pmatrix}
127p^3+195p^2-1500p+1250&24p^2(10-9p)\\
24p^2(10-9p)&153p^3+855p^2-2250p+1250
\end{pmatrix},
\]
\[
M_E=\frac1{125}\begin{pmatrix}
28p^3-3p^2-150p+125&24p^2(1-p)\\
24p^2(1-p)&108p^2-225p+125
\end{pmatrix}.
\]
These formulas and every spectral identity below are independently recomputed by the bundled exact-rational script.

**3. The central-last class cannot win.** The class traces obey \(\operatorname{tr}M_L=\operatorname{tr}M_E\), whereas
\[
\det M_L-\det M_E
=\frac{54p^3(p-2)(p-1)(36p-100)}{100000}<0
\qquad(0<p<1).
\]
For positive semidefinite real \(2\times2\) matrices of the same trace, smaller determinant means larger largest eigenvalue. Hence \(F_L(p)>F_E(p)\) for \(0<p<1\). At \(p=1\) both classes have factor \(8/125\), but \(F_C(1)=1/100\), so neither central-last order is optimal there either.

**4. Algebraic crossing of the two possible winners.** Set \(T_J=\operatorname{tr}M_J\), \(D_J=\det M_J\) for \(J\in\{C,E\}\). Their traces and the exact difference are
\[
T_C=\frac{17p^3+84p^2-300p+200}{100},\qquad
T_E=\frac{(4p-5)(7p^2+35p-50)}{125},\qquad
T_C-T_E=-\frac{54p^3}{1000}.
\]
For \(0<p\le1\), a common eigenvalue of \(M_C\) and \(M_E\) must therefore equal
\[
\xi(p)=\frac{D_E-D_C}{T_E-T_C}
=\frac{(p-1)(67p^2+600p-1000)}{500}.
\]
Substitution in the characteristic polynomial of \(M_C\) gives the exact factorization
\[
\xi(p)^2-T_C\xi(p)+D_C=-\frac{(p-1)Q(p)}{250000}.
\]
Thus a crossing of the two *largest* eigenvalues inside \((0,1)\) requires \(Q(p)=0\). Under the substitution \(p=t/(1+t)\), \(0<p<1\) is equivalent to \(t>0\), and
\[
(1+t)^5Q\!\left(\frac{t}{1+t}\right)
=-1440t^5-16171t^4+120500t^3+523000t^2+650000t+250000.
\]
This polynomial has exactly one sign change in descending coefficient order, so Descartes' rule permits at most one positive root. Exact rational substitution gives \(Q(7/8)>0\) and \(Q(9/10)<0\), proving that such a root exists and is unique.

To ensure it is a crossing of the **largest** eigenvalues, the candidate common eigenvalue must lie above both half-traces. Their exact differences are
\[
\xi-\frac{T_C}{2}=\frac{49p^3+646p^2-1700p+1000}{1000},\qquad
\xi-\frac{T_E}{2}=\frac{11p^3+323p^2-850p+500}{500}.
\]
On \([7/8,9/10]\) both right-hand sides are strictly positive: their derivatives are increasing and negative at \(9/10\), and their values at \(9/10\) are positive. Hence the unique root really equates the two upper eigenvalues. The other zero \(p=1\) from the characteristic factor is extraneous: there \(\xi(1)=0\), while the largest eigenvalues are \(1/100\) and \(8/125\).

**5. Orientation and endpoints.** At \(p=1/2\),
\[
F_C(1/2)=\frac{117+\sqrt{565}}{320}
>\frac{369+\sqrt{3385}}{1000}=F_E(1/2),
\]
using \(\sqrt{565}>23\) and \(\sqrt{3385}<59\). At \(p=1\), \(F_C(1)=1/100<8/125=F_E(1)\). Both functions are continuous. Since they cross exactly once inside \((0,1)\), the exact order classification follows. At \(p=0\) every map equals the identity.

## Verification
The standalone `verify.py` (Python 3 and SymPy) rebuilds the projectors, enumerates all six permutations, and matches every expected-energy matrix both by three nested conditional maps and by direct enumeration of all eight delivery masks. It checks the determinant/traces, crossover polynomial, Descartes transformed polynomial, isolating bracket, eigenvalue branches, endpoint formulas, and supplementary exact-rational tests at seven delivery probabilities. Run `python verify.py`; the recorded output is in `verification_output.txt`. The finite-mask enumeration verifies polynomial identities, not uniqueness by itself. The Descartes argument and the eigenvalue-branch argument prove the continuum claim.

## Relationship to prior work
Keinert and Weber [1] study randomized distributed Kaczmarz on tree networks and give general spectral convergence estimates; their control distribution differs from a fixed row permutation with independent per-attempt Bernoulli delivery. Dax [2] studies cyclic row-order and shuffle effects in tomography but does not develop the exact delivery-reliability ordering phase of this three-row instance. Two closely related public benchmark studies [3,4] consider respectively cyclic versus reshuffling of an equiangular tight three-line frame and greedy sample-size selection for a symmetric planar three-row frame. Both change the sampling model and objective: neither asserts an erasure-dependent minimax ordering crossover for three preselected one-time updates. The exact claim is therefore not a consequence of those statements. A more general order-selection theorem in older projection-product literature might nevertheless imply this instance; historical priority requires independent confirmation.

## Limitations
Only this concrete three-row planar system, exactly one sweep, independent identically distributed erasures, and worst-case expected squared Euclidean error are considered. No statement is made about multiple-sweep convergence, randomly correlated losses, other row geometries, nonzero relaxation, communication overhead, or noisy successfully delivered updates. The one-step model gives an analytically sharp ordering benchmark, not a universal practical scheduling rule. The mathematical analysis and script are not independent certification.

## References
[1] F. Keinert and E. S. Weber, *A Randomized Distributed Kaczmarz Algorithm and Anomaly Detection*, Axioms 11(3), 106, published 2022-02-26, https://doi.org/10.3390/axioms11030106 .

[2] A. Dax, *Kaczmarz Anomaly in Tomography Problems*, AppliedMath 2(2), 196–211, published 2022-04-25, https://doi.org/10.3390/appliedmath2020012 .

[3] *Sharp cyclic–reshuffling rate reversal for a three-line tight Kaczmarz frame*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-cyclic-reshuffling-rate-reversal-for-a-three-line-tight-ka--9dbaf46096e3 .

[4] *Exact residual-budget-optimal sampling sizes for symmetric three-row Kaczmarz–Motzkin*, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-residual-budget-optimal-sampling-sizes-for-symmetric-three--efae258a460c .
