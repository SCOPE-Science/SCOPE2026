# Universal spacing extrema for three weighted rungs of a circular ladder

## Finding

Let \(n\ge5\). On the simple prism \(G_n=C_n\square K_2\), give all rail edges conductance one and exactly three selected rungs a common conductance \(t>0\); the other rungs also have unit conductance. Let \(\tau_n(S;t)\) be the weighted spanning-tree sum, i.e., the sum over spanning trees of products of their edge conductances, where \(S\subset\mathbb Z/n\mathbb Z\) is the three-element set of special rung indices. Write the three positive cyclic gaps of \(S\) as \((x,y,z)\), with \(x+y+z=n\).

For every \(t>0\) other than \(t=1\), the following statements hold **simultaneously**:

* The **largest** value of \(\tau_n(S;t)\) occurs exactly when the gaps differ by at most one, i.e., their multiset is \(\{\lfloor n/3\rfloor,\lfloor(n+1)/3\rfloor,\lfloor(n+2)/3\rfloor\}\).
* The **smallest** value occurs exactly when their multiset is \(\{1,1,n-2\}\), i.e., three consecutive rungs.

Each equality description includes all rotations and reflections; there are no further optimizers. At \(t=1\), every placement has the same spanning-tree sum. Thus the optimal placement is **unchanged when a positive conductance contrast switches from strengthening to weakening the three rungs**.

More precisely, if \(x+1<y\), then replacing the gaps \((x,y,z)\) by \((x+1,y-1,z)\) strictly increases the weighted tree sum whenever \(t\ne1\). This local inequality has the explicit all-parameter positive certificate in the proof below.

For instance, at \(n=9,t=2\), the balanced placement \((3,3,3)\) has \(\tau=2{,}480{,}040\), whereas the consecutive-rung placement \((1,1,7)\) has \(\tau=2{,}432{,}232\).

## Assumptions and scope

The graph has \(2n\) vertices \((j,\varepsilon)\), where \(j\in\mathbb Z/n\mathbb Z\) and \(\varepsilon\in\{0,1\}\); each layer forms a unit-conductance cycle and the rung \((j,0)(j,1)\) has conductance \(t\) for \(j\in S\), and one otherwise. The graph is undirected, finite, connected and simple. The result is a statement about the **weighted sum of all spanning trees**, not the weight of a single minimum spanning tree or the probability of surviving random bond deletion at arbitrary heterogeneous failure probabilities. The parameter \(t\) is any positive real number, with no asymptotic restriction. Only the three selected rungs may differ from unit weight.

## Proof

**1. Reduction to a one-dimensional massive cyclic Green kernel.** Let \(L_C\) denote the Laplacian of the unit-weight cycle on \(n\) indices, and let \(D=\operatorname{diag}(w_0,\ldots,w_{n-1})\) list the rung conductances. In the two-layer ordering, the weighted Laplacian is
\[
\mathcal L=\begin{pmatrix}L_C+D&-D\\-D&L_C+D\end{pmatrix}.
\]
The orthogonal symmetric/antisymmetric layer decomposition makes this matrix the direct sum of \(L_C\) and \(L_C+2D\). The nonzero eigenvalues of \(L_C\) have product \(n^2\); the latter block is positive definite. The matrix-tree theorem therefore gives the **exact identity**
\[
\tau_n(S;t)=\frac n2\det(L_C+2D).
\]
Set \(u=t-1\) (so \(u>-1\)), \(B=L_C+2I\), and \(E_S=\sum_{j\in S}e_je_j^{\mathsf T}\). Then \(L_C+2D=B+2uE_S\), and the rank-three determinant lemma yields
\[
\frac{\tau_n(S;t)}{\tau_n(S;1)}=\det(I_3+uK_S),\qquad K=2B^{-1}.
\]
Here \(K_S\) is the principal submatrix on the three selected rung indices. The unweighted denominator is independent of \(S\), and, using the cycle spectrum, equals
\[
\tau_n(S;1)=n\bigl(T_n(2)-1\bigr),
\]
where \(T_n\) is the Chebyshev polynomial of the first kind.

**2. Exact periodic Green kernel.** Define
\[
q=2-\sqrt3\in(0,1),\qquad c=\frac{1}{\sqrt3(1-q^n)}>0,
\qquad g(d)=c(q^d+q^{n-d})\quad(0\le d\le n).
\]
The relation \(q+q^{-1}=4\) verifies directly that \((4I-A(C_n))g=2e_0\), with periodic indices. Consequently \(K_{ij}=g(d)\) for \(d\equiv j-i\pmod n\). Write \(a=g(0)\), \(b_x=g(x)\), \(b_y=g(y)\), and \(b_z=g(z)\). Directly expanding the symmetric three-by-three determinant gives the exact ratio
\[
P(x,y,z;t):=\frac{\tau_n(S;t)}{\tau_n(S;1)}
=(1+ua)^3-u^2(1+ua)(b_x^2+b_y^2+b_z^2)+2u^3b_xb_yb_z.
\]
This is a degree-three polynomial in \(u\), and thus includes the three-rung interaction term that is absent in one- or two-rung comparisons.

**3. Strict discrete gap-balancing identity.** Consider positive integers \(x,y,z\) satisfying \(x+y+z=n\) and \(x+1<y\). Put \(A=q^x\), \(D_0=q^y\), and \(C=q^z\), so \(q^n=AD_0C\). From the Green kernel,
\[
b_x=c(A+D_0C),\qquad b_y=c(D_0+AC),\qquad b_z=c(C+AD_0).
\]
After replacing \((x,y,z)\) by \((x+1,y-1,z)\), the first two bracketed quantities become \(qA+D_0C/q\) and \(D_0/q+qAC\). Elementary expansion, with \(H=(1-q^2)(q^2A^2-D_0^2)/q^2\), gives
\[
\begin{aligned}
(b_x^2+b_y^2)_{\rm old}-(b_x^2+b_y^2)_{\rm new}&=c^2H(1+C^2),\\
(b_xb_y)_{\rm old}-(b_xb_y)_{\rm new}& =c^2H C.
\end{aligned}
\]
The latter identity is multiplied by the unchanged \(b_z=c(C+AD_0)\) when taking the threefold product. Substitution into the exact ratio, followed by the identity
\[
(1+AD_0C)(1+C^2)-2C(AD_0+C)=(1-C^2)(1-AD_0C),
\]
and the equality \(c(1-q^n)=1/\sqrt3\), gives
\[
\boxed{\begin{aligned}
&P(x+1,y-1,z;t)-P(x,y,z;t)\\
&=\frac{u^2c^2(1-q^2)}{q^2}
\bigl(q^{2x+2}-q^{2y}\bigr)
\left(1+q^{2z}+\frac{u}{\sqrt3}(1-q^{2z})\right).
\end{aligned}}
\]
Every factor on the right is strictly positive when \(t\ne1\). Indeed, \(y\ge x+2\) makes \(q^{2x+2}>q^{2y}\); and since \(u>-1\), the final parenthesis is strictly greater than \(1-1/\sqrt3>0\). At \(t=1\), its prefactor \(u^2\) vanishes.

**4. Global extremizers and uniqueness.** Any positive integer triple summing to \(n\) whose gaps do not differ by at most one has two gaps differing by at least two. Balancing those gaps strictly increases \(P\) for \(t\ne1\). Repeating must terminate at the unique multiset of nearly equal gaps. Conversely, from any gap triple other than \(\{1,1,n-2\}\), a reverse balancing operation moves one unit from a gap of size at least two to a (weakly) larger gap, strictly decreasing \(P\). Repetition reaches \(\{1,1,n-2\}\). Rotational and reflectional symmetry identify all arrangements with the same gap multiset. Thus the claimed maxima and minima are exhaustive for every \(n\ge5\), with equality only for the respective specified multisets. The argument does not distinguish \(u>0\) from \(-1<u<0\).

## Verification

The standalone standard-library program `verify.py` checks the rank-three determinant formula against full exact-rational matrix-tree cofactors for all three-rung placements on sizes \(5\le n\le9\) at three rational contrasts; it also exhaustively compares the gap optimizers for all \(5\le n\le17\) at four rational contrasts, verifies cyclic invariance of the Green kernel and tests all applicable local balancing inequalities. It reports `VERIFY_OK 14694 exact rational tests`.

The companion `verify_symbolic.py` uses SymPy to expand and verify, exactly as polynomial identities, both finite-difference factors and the final factorization before inserting the positive range of parameters. It reports `SYMBOLIC_VERIFY_OK`. Neither finite test set alone is a proof for all integers and real parameters; the all-size, all-parameter proof is the exact factorization and positivity argument above.

## Relationship to prior work

Kirchhoff's matrix-tree theorem and the Burton–Pemantle transfer-current framework give the underlying determinant identities; they do not themselves rank positions of three fixed-contrast rung defects. Martin and Reiner's 2003 weighted-tree work develops factorization methods for products of complete graphs rather than this discrete placement problem. Kassel and Wu (2013) study transfer-current correlations and scaling limits, not fixed-number spacing extrema on prisms. Khosoussi and collaborators (2016) establish general spanning-tree design methods and approximation principles, not this explicit all-contrast integer-gap classification. Klenke (2017) analyzes rung determinantal processes on infinite straight ladders, rather than three marked rungs on finite cyclic ladders. Azimi and Farrokhi (2023) determine circular-ladder resistance matrices and the unweighted tree count, but their checked circular-ladder section does not supply the constrained three-rung placement optimum. A published exact budget allocation result for prisms treats **freely variable** edge conductances and proves a uniform global optimizer; that unconstrained optimum cannot be substituted for any of the admissible binary three-rung assignments and does not give this ordering.

The new assertion is specifically the strict, all-size, all-contrast three-rung balancing law, including both sharp extremal patterns. General determinantal structure, the resolvent formula, and unweighted tree counts are background, not claimed as new.

## Limitations

The result requires exactly three special rungs of identical conductance, with all rails and all other rungs at unit conductance. It does not classify arbitrary numbers of special rungs, unequal defect strengths, wider ladder strips, or arbitrary graph topologies. A general result on discrete point-impurity rearrangements may imply this classification even if it did not appear in the sources inspected; historical priority therefore remains provisional. No independent mathematical audit has been performed.

## References

1. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, arXiv:math/0302213v1, first posted 2003-02-18. https://arxiv.org/abs/math/0302213 .
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946v1, first posted 2013-12-10. https://arxiv.org/abs/1312.2946 .
3. K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116v1, first posted 2016-04-05. https://arxiv.org/abs/1604.01116 .
4. A. Klenke, *The random spanning tree on ladder-like graphs*, arXiv:1704.00182v1, first posted 2017-04-01. https://arxiv.org/abs/1704.00182 .
5. A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497v1, first posted 2023-06-18. https://arxiv.org/abs/2306.10497 .
6. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings Via Transfer-Impedances*, *Annals of Probability* 21 (1993), 1329–1371, DOI:10.1214/aop/1176989121.
