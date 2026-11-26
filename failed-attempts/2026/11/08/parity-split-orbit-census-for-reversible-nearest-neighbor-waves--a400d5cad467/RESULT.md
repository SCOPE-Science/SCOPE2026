# Parity-split orbit census for reversible nearest-neighbor waves on binary rings

## Finding

Let \(n\ge 3\), let \(Q=2^f\) with integer \(f\ge1\), and let \(F_n\) act on pairs of cyclic rows over \(\mathbb F_Q\) by
\[
F_n(u,v)=(Su+S^{-1}u+v,\;u),
\]
where \(S\) rotates the \(n\) labelled sites by one position. Let \(t\ge1\), \(d=\gcd(n,t)\), and let \(N_n(t)\) be the number of paired-row states fixed by \(F_n^t\). Then
\[
\boxed{N_n(t)=Q^{2d-\mathbf 1_{\{n\text{ odd},\ t\text{ odd}\}}}.}
\]
The complete similarity classification underlying this count is as follows. Let \(R_n\) be the cyclic coordinate shift on \(\mathbb F_Q^n\). When \(n\) is even, \(F_n\) is similar over \(\mathbb F_Q\) to \(R_n\oplus R_n\). When \(n\) is odd, write \(W_n=\{w\in\mathbb F_Q^n:\sum_i w_i=0\}\); then \(F_n\) is similar to
\[
J_2(1)\oplus(R_n|_{W_n})\oplus(R_n|_{W_n}).
\]
Here \(J_2(1)\) is a single nontrivial size-two Jordan block at eigenvalue one.

In particular, **all states are periodic from the first instant**, and the exact permutation order and maximum attainable primitive period are both
\[
\boxed{L_n=\begin{cases}n,&n\text{ even},\\2n,&n\text{ odd}.\end{cases}}
\]
For each positive divisor \(\ell\mid L_n\), the number of labelled states of primitive period \(\ell\) and the number of primitive cycles of that period are exactly
\[
P_n(\ell)=\sum_{e\mid\ell}\mu(\ell/e)\,Q^{2\gcd(n,e)-\mathbf 1_{\{n,e\text{ odd}\}}},
\qquad O_n(\ell)=P_n(\ell)/\ell.
\]
All other primitive-period populations vanish. A further exact odd-circumference law holds: for every odd \(n\ge3\) and every divisor \(\ell\mid n\),
\[
\boxed{P_n(2\ell)=(Q-1)P_n(\ell).}
\]
Thus for binary fields, each odd-ring primitive-period population is exactly matched by the population at double that period; this is a statement about **states**, not numbers of cycles.

## Assumptions and scope

The ring is labelled, with indices interpreted modulo \(n\), and uses the simultaneous local rule
\[
u_i(k+1)=u_{i-1}(k)+u_{i+1}(k)+u_i(k-1)
\]
with addition in characteristic two. The state is the ordered pair of the current and preceding rows. The condition \(n\ge3\) ensures the two neighboring sites of each vertex are distinct. No assumption on the configuration, the field extension degree, or the time exponent is imposed beyond those stated. Statements count labelled configurations: rotations of a row are not identified. The primitive-period count is defined in the usual temporal, not spatial, sense.

## Proof

**1. Reversibility and the shift algebra.** Put \(A=S+S^{-1}\). The block matrix of the map is
\[
T=\begin{pmatrix}A&I\\I&0\end{pmatrix},\qquad
T^{-1}=\begin{pmatrix}0&I\\I&A\end{pmatrix}.
\]
Consequently there are no transient states. The shift satisfies \(S^n=I\), and \(T\) commutes with the diagonal action of \(S\).

**2. Odd circumferences: explicit traveling-wave coordinates.** Because \(n\) is odd, the constant vector \(\mathbf1\) is complementary to \(W_n=\ker(\sum_i\cdot_i)\), and both summands are \(S\)-stable. The operator \(A\) is invertible on \(W_n\): over an algebraic closure, all roots \(\zeta\) of \(x^n-1\) are simple, and \(\zeta+\zeta^{-1}=0\) in characteristic two only for \(\zeta=1\), absent from \(W_n\).

For \(a,b\in W_n\) define
\[
(u,v)=(a+b,\;S^{-1}a+Sb).
\]
This is an invertible change of coordinates because its determinant is \(A|_{W_n}\). Direct substitution gives
\[
T(u,v)=(Sa+S^{-1}b,\;a+b),
\]
which is the image corresponding to \((Sa,S^{-1}b)\). The cyclic inverse shift is similar to the forward shift, so the restriction to \(W_n\oplus W_n\) is similar to two copies of \(S|_{W_n}\). On the two-dimensional constant-row subspace, \(A=0\), and \(T(u,v)=(v,u)\), the characteristic-two transposition, whose only Jordan block is \(J_2(1)\). This proves the odd case of the similarity claim.

**3. Even circumferences: local Jordan structure.** Write \(n=hm\), where \(h=2^a\ge2\) and \(m\) is odd. Work temporarily over an algebraic closure \(K\) of \(\mathbb F_Q\). The coordinate-shift module decomposes as
\[
K[x]/(x^n-1)\cong\prod_{\zeta^m=1} K[\epsilon]/(\epsilon^h),
\qquad x\mapsto\zeta+\epsilon.
\]
On the factor corresponding to \(\zeta\), the two-row update is the matrix \(T_\zeta=\left(\begin{smallmatrix}x+x^{-1}&1\\1&0\end{smallmatrix}\right)\). Its characteristic polynomial in a commuting indeterminate \(z\) is
\[
\det(zI-T_\zeta)=(z+x)(z+x^{-1}).
\]
If \(\zeta\ne1\), the two factors are coprime in the local ring, so the module splits into a one-row component on which the update multiplies by \(x\) and one on which it multiplies by \(x^{-1}\). Each contributes a single Jordan block of size \(h\), respectively at eigenvalues \(\zeta\) and \(\zeta^{-1}\). Since both \(\zeta\) and \(\zeta^{-1}\) occur among the shift roots, each nonunit eigenvalue occurs in exactly two length-\(h\) blocks, matching two coordinate shifts.

For \(\zeta=1\), write \(x=1+\epsilon\). The identity
\[
A=x+x^{-1}=\epsilon^2/(1+\epsilon)
\]
holds in \(K[\epsilon]/(\epsilon^h)\). The matrix identity \((T_1+I)^2=AT_1\) implies \((T_1+I)^h=0\), because \(h\) is even and \(A^{h/2}=0\). Moreover, the fixed-vector equations are \(u=v\) and \(Au=0\). Multiplication by \(A\) has kernel dimension exactly two in the length-\(h\) local ring. Thus \(T_1\) has exactly two Jordan blocks, each of size at most \(h\); their total dimension is \(2h\), forcing both blocks to have size \(h\). These coincide with the two length-\(h\) unit-root blocks in \(S\oplus S\).

We have matched every elementary divisor of \(T\) and \(S\oplus S\) after scalar extension. Rational canonical form (or elementary-divisor descent) gives similarity already over \(\mathbb F_Q\). This proves the even case without assuming semisimplicity in even circumference.

**4. Fixed-space dimensions.** A coordinate shift on \(n\) sites has a \(d=\gcd(n,t)\)-dimensional space fixed by its \(t\)-th power, because its permutation has \(d\) coordinate cycles. The even-circumference similarity therefore gives \(\dim\ker(T^t-I)=2d\).

When \(n\) is odd, all \(d\) coordinate cycles of \(S^t\) have odd length \(n/d\). Their fixed-space intersection with \(W_n\) imposes exactly one independent sum-zero condition, hence has dimension \(d-1\). On \(J_2(1)\), the fixed-space dimension of the \(t\)-th power is one if \(t\) is odd and two if \(t\) is even. Summing the three contributions gives \(2(d-1)+1=2d-1\) for odd \(t\), and \(2(d-1)+2=2d\) for even \(t\). A \(k\)-dimensional vector space over \(\mathbb F_Q\) has \(Q^k\) elements, proving the boxed fixed-point formula.

**5. Exact order and primitive periods.** In the even case \(T\) is similar to two coordinate rotations; a coordinate impulse has primitive period \(n\), and the order is exactly \(n\). In the odd case the two copies of \(S|_{W_n}\) have order \(n\) (their nonconstant eigenvalues include roots of order whose least common multiple is \(n\)), and \(J_2(1)\) has order two. Because \(n\) is odd, a direct sum of an \(n\)-periodic vector and a nonfixed vector in \(J_2(1)\) has primitive period \(2n\). Hence the permutation order and maximum primitive period are both \(2n\). The standard divisor identity \(N_n(t)=\sum_{\ell\mid t}P_n(\ell)\), followed by Möbius inversion, gives the population formula.

For odd \(n\) and \(\ell\mid n\), all divisors \(e\mid\ell\) are odd; the fixed-point formula yields \(N_n(2e)=Q N_n(e)\). Applying Möbius inversion at \(\ell\) and \(2\ell\) and separating odd and even divisors gives \(P_n(2\ell)=\sum_{e\mid\ell}\mu(\ell/e)(N_n(2e)-N_n(e))=(Q-1)P_n(\ell)\).

## Verification

The proof is exact in every \(n\), field size \(Q\), and time \(t\). Three independently structured reproducibility programs accompany this result:

- `check_matrix.py` constructs the linear map on binary basis vectors and checks the exact nullity of \(T^t-I\) for all \(3\le n\le35\) and \(1\le t\le2n\): 1,254 comparisons.
- `check_enumeration.py` independently represents states as pairs of tuples and **exhaustively classifies all 87,360** labelled binary states over ring lengths \(3\le n\le8\), with 66 separate fixed-point comparisons and exact observed maximum periods.
- `check_orbits.py` uses independent integer Möbius inversion for \(3\le n\le60\), field sizes \(Q\in\{2,4\}\), and performs 682 divisor/primitive-population consistency comparisons, checking nonnegative integral orbit counts and attainment of the predicted maximum period.

The corresponding `*.out` files record successful execution. Finite checks do not replace the algebraic proof; extension-field validity follows from the similarity and vector-space arguments.

## Relationship to prior work

Reversible second-order cellular automata and matrix-valued generating techniques are classical. Macfarlane (2004), equations (1)–(3), studies specific one-dimensional reversible rules, including a left/right/center symmetric rule with an additional current-site term, and focuses on single-seed weights \(N(t)\) on unbounded lines; the complete paper's introduction, model definitions, sections on the three rules, concluding remarks, and appendix do not provide the present cyclic Rule-90R paired-state orbit census. Schiff (2007), Chapter 3, explicitly identifies the *same* Rule-90R local equation with periodic boundaries and demonstrates reversibility, but provides an illustrative spacetime evolution, not the even/odd-circumference similarity classification, fixed-point formula, primitive-period populations, or odd-period doubling relation.

Toffoli, Capobianco and Mentrasti (2004) provide a general reversible second-order cellular-automaton-to-lattice-gas equivalence, not an inspected closed formula for this cyclic orbit invariant. Prior algebraic descriptions of reversible rules and first-order cellular automata are acknowledged as general infrastructure, not claimed discoveries. The proposed contribution is specifically the all-circumference similarity split and the resulting exact temporal census, not reversibility itself or the local update rule.

## Limitations

This result is restricted to the stated linear second-order update, periodic spatial boundary, and finite fields of characteristic two. It does not classify nonlinear reversible rules, open-boundary systems, or trajectories distinguished by spatial-rotation equivalence. The connection to generic second-order lattice-gas reductions remains a source of potential indirect prior implication. Historical uniqueness is not mathematically certified by the literature searches, and the complete Toffoli–Capobianco–Mentrasti article was not accessible in the examined sources. No independent review has been performed.

## References

1. A. J. Macfarlane, “Linear reversible second-order cellular automata and their first-order matrix equivalents,” *Journal of Physics A* **37** (2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006. Public source date: 2004-10-28. Full text: https://citeseerx.ist.psu.edu/document?doi=f3921158b9871d8db8d16cde33822fabde049a6b&repid=rep1&type=pdf.
2. J. L. Schiff, *Cellular Automata: A Discrete View of the World*, Wiley, 2007, Chapter 3.7 and Figure 3.22. ISBN 9780470168790. https://www.wiley.com/en-us/Cellular%2BAutomata%3A%2BA%2BDiscrete%2BView%2Bof%2Bthe%2BWorld-p-9780470168790.
3. T. Toffoli, S. Capobianco and P. Mentrasti, “How to turn a second-order cellular automaton into a lattice gas: a new inversion scheme,” *Theoretical Computer Science* **325** (2004), 329–344. DOI: 10.1016/j.tcs.2004.06.012. Comparison based on abstract and accessible bibliographic description only.
