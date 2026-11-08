# Odd generalized Petersen Ising antiferromagnets have Fibonacci ground-state multiplicities

## Finding
For every **odd integer** \(n\ge5\), the zero-field, uniform-coupling antiferromagnetic Ising model on the generalized Petersen graph \(GP(n,2)\) has exact ground-state energy
\[
 E_{\min}=-(2n-1)J,
\]
and the following number of **labelled spin configurations** attaining that energy:
\[
 \boxed{\Omega_n=\begin{cases}
 2nF_{(n-1)/2}, & n\equiv1\pmod4,\\
 2nF_{(n+1)/2}, & n\equiv3\pmod4.
 \end{cases}}
\]
Here \(F_0=0\), \(F_1=1\), and \(F_{m+2}=F_{m+1}+F_m\) are Fibonacci numbers. Spin-reversed configurations count separately. Equivalently, the graph has maximum cut size \((5n-1)/2\) and \(\Omega_n/2\) distinct maximum cuts when cuts are identified under complementation. The ground-state residual entropy per spin satisfies
\[
 \lim_{\substack{n\to\infty\\n\text{ odd}}}
 \frac{\log \Omega_n}{2n}=\frac14\log\left(\frac{1+\sqrt5}{2}\right).
\]
For \(n=5,7,9,11,13\), respectively, the exact degeneracies are \(10,42,54,176,208\). The smallest case is the Petersen graph.

## Assumptions and scope
The graph has distinct vertices \(u_i,v_i\), for \(i\in\mathbb Z/n\mathbb Z\), and precisely the \(3n\) undirected edges
\[
 E_n=\{\{u_i,u_{i+1}\},\{u_i,v_i\},\{v_i,v_{i+2}\}:i\in\mathbb Z/n\mathbb Z\}.
\]
All \(2n\) spins \(\sigma_w\in\{-1,+1\}\) are independent Ising variables, \(J>0\) is uniform, no field is present, and
\[
 H_n(\sigma)=J\sum_{\{a,b\}\in E_n}\sigma_a\sigma_b.
\]
An edge is *frustrated* precisely when its spins are equal. Write \(f(\sigma)\) for the number of such edges. Thus \(H_n/J=2f(\sigma)-3n\). All assertions concern exact finite-system, zero-temperature ground states, not thermal phase transitions. Odd \(n\) is a natural topological class: both outer and inner rims are single odd cycles because \(\gcd(n,2)=1\).

## Proof
**1. A pentagonal lower bound.** For each index \(i\), the five edges along
\[
 u_i\;u_{i+1}\;u_{i+2}\;v_{i+2}\;v_i\;u_i
\]
form a five-cycle. Every spin assignment frustrates an odd number of the edges on any odd cycle, hence at least one. Each outer-rim edge occurs in two of these \(n\) cycles, each spoke in two, and each inner-rim edge in one. Summing over the \(n\) pentagons therefore gives \(n\le2f(\sigma)\). For odd \(n\), this implies \(f(\sigma)\ge(n+1)/2\), or \(H_n(\sigma)\ge-(2n-1)J\).

**2. Exact finite-memory spin transfer.** Let \(\mathcal S=\{-1,+1\}^3\). Label a transfer state by \(s=(a,b,c)\), representing \((\sigma_{u_{i-1}},\sigma_{v_{i-1}},\sigma_{v_{i-2}})\), and its successor by \(s'=(u,v,d)\), representing \((\sigma_{u_i},\sigma_{v_i},\sigma_{v_{i-1}})\). Define the \(8\times8\) matrix \(T(x)\), for an indeterminate \(x\), by
\[
 T(x)_{(a,b,c),(u,v,d)}=
 \begin{cases}
 x^{(3+au+cv+uv)/2},&d=b,\\
 0,&d\ne b.
 \end{cases}
\]
The exponent is an integer in \(\{0,1,2,3\}\): it is exactly the number of frustrated bonds introduced at index \(i\). The compatibility condition \(d=b\) ensures consistent propagation of the prior inner spin. Every periodic sequence of \(n\) states, counted as a closed transfer walk, corresponds bijectively to one spin configuration on \(GP(n,2)\). Consequently,
\[
 Z_n(x):=\sum_{\sigma\in\{-1,+1\}^{2n}}x^{f(\sigma)}
 =\operatorname{tr}(T(x)^n).
\]
This identity uses no large-size approximation.

**3. Two coefficients of an exact determinant.** Put \(M(y)=y^{-1}T(y^2)\) and
\[
 D(t,y)=\det(I_8-tM(y)).
\]
A direct expansion of the stated eight-state matrix, in the formal ring \(\mathbb Z[t][[y]]\), gives
\[
 D(t,y)=\underbrace{(1-3t^4+t^8)}_{D_0(t)}
 -2y(t^3+t^5)+O(y^2).
\]
The determinant has **no negative powers of \(y\)**; this can be verified by expanding its eight-by-eight characteristic polynomial. The exact algebraic calculation is reproducible in the accompanying source checker, which constructs the matrix from the definition and tests these coefficients symbolically. In fact, its \(y^2\)-coefficient is \(-(t^2+6t^4+t^6)\), providing an additional internal check.

The formal matrix identity
\[
 -\log D(t,y)=\sum_{m\ge1}\frac{t^m}{m}\operatorname{tr}(M(y)^m)
\]
follows from \(\det(I-tM)=\exp(\operatorname{tr}\log(I-tM))\) over the rational formal-power-series ring. Thus, for an odd integer \(n\), since \(\log D_0(t)\) has powers only divisible by four, the coefficient of \(y\) in \(\operatorname{tr}(M(y)^n)\) is
\[
 [y]\operatorname{tr}(M(y)^n)
 =2n[t^n]\frac{t^3+t^5}{1-3t^4+t^8}.
\]
By the bound in Step 1,
\[
 \operatorname{tr}(M(y)^n)=y^{-n}Z_n(y^2)
\]
has no negative powers of \(y\) for odd \(n\); its coefficient of \(y\) is exactly the number of assignments with \(f=(n+1)/2\). The zero-power coefficient vanishes because \(n\) is odd.

**4. Fibonacci coefficient extraction.** The elementary identity
\[
 \frac1{1-3q+q^2}=\sum_{k\ge0}F_{2k+2}q^k
\]
follows from the recurrence \(F_{2k+4}=3F_{2k+2}-F_{2k}\) and the two initial terms \(1,3\). If \(n=4k+5\), only the \(t^5\) term contributes and yields \(2nF_{2k+2}=2nF_{(n-1)/2}\). If \(n=4k+3\), with \(k\ge1\), only \(t^3\) contributes and yields \(2nF_{2k+2}=2nF_{(n+1)/2}\). These integers are strictly positive. Thus the lower bound is attained, and the coefficient counts **all and only** its minimizers, proving the energy and both degeneracy formulas.

**5. Residual entropy.** Binet's formula gives \(F_m\sim \varphi^m/\sqrt5\), with \(\varphi=(1+\sqrt5)/2\). The Fibonacci index is \(n/2+O(1)\), and the prefactor \(2n\) has sublinear logarithm. Dividing by the \(2n\) spin sites gives the displayed entropy limit.

## Verification
The standalone file `verify.py` constructs the exact eight-state polynomial transfer matrix and independently verifies the first three determinant coefficients in \(y\) using symbolic arithmetic. It compares the theorem with exact min-plus transfer calculations for 28 odd graph sizes through \(n=81\). A separate brute-force enumeration directly constructs graph edges and checks all spin assignments for \(n=5,7,9\), without using transfer-state recurrence. To reproduce, run `python3 verify.py` with Python 3 and SymPy installed. The expected terminal line begins with `VERIFY_OK` and reports counts of symbolic and independent checks. Finite computations check the proof and do not replace the all-\(n\) symbolic argument.

## Relationship to prior work
The dodecahedral Ising analysis of Strečka, Karľová and Madaras treats \(GP(10,2)\) as one regular polyhedron and establishes its finite zero-field degeneracy; it does not address the odd-index family. Jacobsen and Salas calculate Potts/Ising transfer functions for generalized Petersen graphs of the form \(G(mk,k)\), a family that for \(k=2\) has an **even** first index; its general transfer framework is credited, rather than represented as new. Kuhl's theorem identifies \(P(m,2)\) by its Tutte polynomial but does not provide a closed formula for the odd-family Ising ground-state degeneracy. Work on maximum frustration over all signings of generalized Petersen graphs asks a different optimization question from fixing all couplings antiferromagnetic and counting ground states. The new statement is restricted to the odd-index family and specifically asserts the complete two-congruence Fibonacci ground-state counts, plus the sharp energy and residual entropy. Equivalent statements may be expressed as the number of maximum cuts or lowest-degree coefficients of an Ising partition polynomial.

## Limitations
The proof requires odd \(n\ge5\), identical positive nearest-neighbor couplings, zero field, and classical two-state spins. It neither determines field-dependent magnetization plateaux nor any positive-temperature partition function or critical singularity. An unindexed earlier maximum-cut count, Tutte coefficient formula, or special-purpose transfer-matrix evaluation could affect historical priority. The checker relies on SymPy for symbolic evaluation; the proof itself does not rely on unverified numerical extrapolation.

## References
1. J. Strečka, K. Karľová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449 (first public 2015-02-16), https://arxiv.org/abs/1502.04449 .
2. J. L. Jacobsen and J. Salas, *A generalized Beraha conjecture for non-planar graphs*, arXiv:1303.5210 (2013), https://arxiv.org/html/1303.5210v2 .
3. J. S. Kuhl, *The Tutte polynomial and the generalized Petersen graph*, Australasian Journal of Combinatorics 40 (2008), 87–97, https://www.researchgate.net/publication/267081866_The_Tutte_polynomial_and_the_generalized_Petersen_graph .
4. *Maximum Frustration in Signed Generalized Petersen Graphs*, arXiv:1905.05548 (2019), https://arxiv.org/html/1905.05548v1 .
