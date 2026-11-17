# An occupation-resolved stationary zeta and Gaussian law for Critters on two-row tori

## Finding
For the original complementing Critters block automaton on every labelled torus \(\mathbb Z_2\times\mathbb Z_{2m}\), \(m\ge2\), let \(F_m(u)=\sum_{x:T(x)=x}u^{K(x)}\), where \(T\) is one even-plus-odd pair of block updates and \(K(x)\) is the number of occupied cells. Put
\[
Q(z,u)=1-(1+u^2+u^4)z+(u^4-u^2-u^6)z^2-u^6z^3.
\]
Then the complete occupied-site distribution is determined by
\[
\boxed{F_m(u)=[z^m]\left(-z\frac{\partial}{\partial z}\log[(1-u^2z)^5Q(z,u)]\right)}\qquad(m\ge2).
\]
In particular \(F_m(1)=5+\sum_{j=1}^3\lambda_j^m\), where the \(\lambda_j\) are the roots, with multiplicity, of \(X^3-3X^2-X-1\). The unique positive dominant root \(\lambda=3.382975767906\ldots\) gives \(F_m(1)\sim\lambda^m\) and spatial entropy \(\log\lambda/4\) per physical site. The exact reciprocal identity is \(F_m(u)=u^{4m}F_m(u^{-1})\); hence a uniformly chosen stationary configuration has exact mean occupation \(2m\).

Furthermore, if \(K_m\) is its number of occupied cells, then
\[
\frac{K_m-2m}{\sqrt m}\ \Longrightarrow\ \mathcal N(0,\sigma^2),\quad
\sigma^2=\frac{8(\lambda+1)}{3\lambda^2-6\lambda-1}=2.689824935959\ldots.
\]
The variance also satisfies \(\operatorname{Var}(K_m)=\sigma^2m+O(1)\). This is a distribution over **fixed configurations**, not over all initial configurations or evolving trajectories.

## Assumptions and scope
Index a \(2\times2\) block by its integer \(a\in\{0,\ldots,15\}\) with bits \(a_0,a_1,a_2,a_3\) at upper-left, upper-right, lower-left, lower-right respectively, \(a=\sum_{j=0}^3 2^ja_j\). Let \(f(a)\) be the following permutation: for occupancy \(0,1,4\), complement all four bits; for occupancy two with adjacent occupied cells, leave the block unchanged; for the two diagonally occupied blocks \(a=6,9\), complement all bits (interchange diagonals); for occupancy three, complement then rotate the resulting block by half a turn (exchange bit positions \(0\leftrightarrow3\), \(1\leftrightarrow2\)). This is the original *complementing*, rather than the alternating nonstrobing, Critters convention. For all sixteen blocks \(|f(a)|=4-|a|\).

First apply \(f\) simultaneously to the disjoint blocks whose left column is even and upper row is \(0\). Then shift the blocking by one site in both torus coordinates and apply \(f\) to the odd blocks, taking upper row \(1\) and left column odd. Their composition \(T\) is one full two-phase update. Both coordinates have periodic boundary conditions; each spatial coordinate and time phase is labelled. We require \(m\ge2\) to avoid a two-column degenerate quotient. No spatial rotation or translation or temporal identification is used in the count.

## Proof
Define the \(m\) original even-block words \(a^{(0)},\ldots,a^{(m-1)}\), each with four bits, and indices modulo \(m\). After the even update these are \(b^{(i)}=f(a^{(i)})\). The odd block straddling adjacent even blocks \(i,i+1\) contains, in its vertical row-\(1\)-then-row-\(0\) order, the four bits
\[
X(a,b)=(f(a)_3,f(b)_2,f(a)_1,f(b)_0).
\]
For a fixed configuration to return to itself after the odd phase, the desired odd output must be
\[
Y(a,b)=(a_3,b_2,a_1,b_0).
\]
Consequently, with component-tuple notation as above, define the explicit binary \(16\times16\) matrix \(M\) by \(M_{a,b}=1\) exactly when \(f(X(a,b))=Y(a,b)\), and \(M_{a,b}=0\) otherwise. Define \(W(u)_{a,b}=u^{|a|}M_{a,b}\). Since each original bit appears in precisely one even block and one odd block, the simultaneous fixed-point equations are **exactly** the \(m\) local edge constraints \(M_{a^{(i)},a^{(i+1)}}=1\). Therefore
\[
F_m(u)=\operatorname{tr}W(u)^m.
\]
A finite sixteen-state symbolic determinant calculation, reproduced algebraically by the included `verify_transfer.py`, yields the **polynomial identity**
\[
\det(I-zW(u))=(1-u^2z)^5Q(z,u).
\]
The standard formal trace-determinant identity \(-z\partial_z\log\det(I-zW)=\sum_{m\ge1}z^m\operatorname{tr}(W^m)\) proves the coefficient formula for every \(m\ge2\), without extrapolating from finite enumeration.

At \(u=1\), the characteristic factorization is \((1-z)^5(1-3z-z^2-z^3)\); the other eight eigenvalues vanish. The cubic has a unique real positive root \(\lambda>3\) and two roots of modulus less than one (directly by its discriminant or complex roots), giving the exact unweighted count and leading term. In the directed graph of \(M\), the unique spectrally dominant strongly connected component comprises states \(\{0,1,2,4,6,8,9,15\}\). It is primitive (it is strongly connected and contains a one-step loop). All other cyclic components are one-vertex loops with eigenvalue \(u^2\); transient components do not affect the trace. Therefore for positive \(u\) near one, \(W(u)\) has a simple dominant eigenvalue \(\lambda(u)\), analytic in \(u\) and strictly separated in modulus from the others, satisfying
\[
\lambda(u)^3-(1+u^2+u^4)\lambda(u)^2+(u^4-u^2-u^6)\lambda(u)-u^6=0.
\]
The coefficient identity with \(u\) replaced by \(u^{-1}\) and \(z\) by \(u^4z\), together with invariance of its determinant, proves occupation reciprocity for every coefficient. In particular \(\mathbb E K_m=2m\) exactly.

Write \(\psi(t)=\log\lambda(e^t)-\log\lambda(1)\). Implicit differentiation of the cubic at \(u=1\) gives \(\psi'(0)=2\) and \(\psi''(0)=8(\lambda+1)/(3\lambda^2-6\lambda-1)>0\). The simple primitive Perron component gives uniformly for complex \(t\) near zero
\[
\mathbb E e^{tK_m}=\frac{\operatorname{tr}W(e^t)^m}{\operatorname{tr}W(1)^m}
=e^{m\psi(t)}(1+O(\theta^m)),\quad 0<\theta<1.
\]
Taking \(t=is/\sqrt m\), subtracting the exact mean and expanding \(\psi\) to quadratic order proves convergence of characteristic functions to \(e^{-\sigma^2s^2/2}\). Differentiating the locally uniform analytic expansion proves the variance statement. No finite cutoff is used as a substitute for these all-length arguments.

## Verification
The standalone Python program `verify_transfer.py` reconstructs all sixteen block images, verifies their bijectivity and occupancy complement, constructs all 256 candidate directed edges, and symbolically recomputes the exact weighted determinant using SymPy. It checks that the matrix has 30 directed edges and independently evaluates its unweighted traces at \(m=2,3,4,5,6,7\), obtaining respectively \(16,44,136,448,1504,5076\). It computes the displayed numerical values from the characteristic cubic.

The separately implemented C++17 program `verify_direct.cpp` evolves **all** \(2^{4m}\) original binary configurations directly through both global block phases for \(m=2,3,4,5\). Its complete occupation histograms are saved in `direct_output.txt`. Both program outputs were reproduced for this package; exact outputs appear in `transfer_output.txt` and `direct_output.txt`. Exhaustive checks at those lengths are consistency checks, not the infinite proof.

## Relationship to prior work
Margolus, *Crystalline Computation* (first publicly posted 1998-11-10, arXiv:comp-gas/9811002), §4, explicitly gives the original two-phase, complementing Critters rule, reversible block permutation, occupation complementation, and diagonal parity. It illustrates gliders and universality, not the above width-two fixed-configuration occupation enumerator. Marotta, *Living in Critters' World* (2005), §1.1 and §§2–3, studies oscillators, barriers, collisions and diffusion in the alternate nonstrobing realization, and specifically distinguishes this convention from the book's complementing rule in footnote 1. Neither inspected work states this all-width labelled stationary zeta or the Gaussian occupation law; methods and dynamical observables differ. Records on parity automata and majority/cyclic-dominance frozen states were also compared; their local rules, phase structure and stationary populations are different, not stronger instances of this result. A description of a reversible block rule alone does not mathematically imply a cubic fixed-point determinant without the distinct two-row classification performed here.

## Limitations
The theorem applies only to original Critters under the fixed phase and labelled periodic width-two geometry, and only to states fixed by a **full even-plus-odd update**. No claims about general widths, higher temporal periods, mixing or long-term orbit distributions are made. The weight is the number of occupied bits at the designated even-phase observation time; despite temporal occupation complementation at each halfstep, it is conserved across full steps. An earlier 1987 print treatment is known but its relevant entire archival text was not accessible for an exhaustive historical-priority inspection. Historical uniqueness in unpublished or poorly indexed treatments is not established. No independent mathematical audit has been performed.

## References
- Norman Margolus, *Crystalline Computation*, arXiv:comp-gas/9811002, first submitted 1998-11-10, §4. https://arxiv.org/abs/comp-gas/9811002
- Sebastian M. Marotta, *Living in Critters' World*, Revista Ciências Exatas e Naturais 7(1) (2005), pp. 9–35. https://revistas.unicentro.br/index.php/RECEN/article/download/385/537
- Tommaso Toffoli and Norman Margolus, *Cellular Automata Machines: A New Environment for Modeling* (1987). Earlier book-based rule source; not represented as fully inspected.
