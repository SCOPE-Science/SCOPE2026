# The three Frobenius spectra of the Hesse cyclic cubic-surface pencil

## Finding
Let \(q\) be an odd prime power of characteristic different from \(3\), and let \(t\in\mathbb F_q\) satisfy \(t^3+27\ne0\). Consider the smooth cubic surface
\[
S_t:\quad X^3+Y^3+Z^3+W^3+tXYZ=0\quad\subset\mathbb P^3_{\mathbb F_q}.
\]
Put \(c_t=-(1+t^3/27)\in\mathbb F_q^\times\). All \(27\) geometric lines are defined over an extension of degree at most three (quadratic or cubic), and their fields of definition are specified below. More precisely, the complete Frobenius cycle type on these lines, the number \(r_t\) of \(\mathbb F_q\)-rational lines, and the degree-seven middle-cohomology factor \(D_t(T)=\det(1-qT\operatorname{Fr}_q\mid\operatorname{Pic}(S_{t,\overline{\mathbb F}_q})\otimes\mathbb Q_\ell)\) are:

| Arithmetic condition | Frobenius cycles on the \(27\) lines | \(r_t\) | \(D_t(T)\) |
| --- | --- | --- | --- |
| \(q\equiv1\pmod3\), \(c_t\) a cube | \(1^{27}\) | \(27\) | \((1-qT)^7\) |
| \(q\equiv1\pmod3\), \(c_t\) a noncube | \(3^9\) | \(0\) | \((1-qT)(1+qT+q^2T^2)^3\) |
| \(q\equiv2\pmod3\) | \(1^3 2^{12}\) | \(3\) | \((1-qT)^4(1+qT)^3\) |

Thus the complete Hasse--Weil zeta function for every such surface is
\[
Z(S_t,T)=\frac{1}{(1-T)(1-q^2T)D_t(T)}.
\]
Equivalently, for every integer \(n\ge1\),
\[
\#S_t(\mathbb F_{q^n})=q^{2n}+1+q^n\,\tau_t(n),
\]
where \(\tau_t(n)\) is respectively \(7\) in the first case; \(7\) if \(3\mid n\) and \(-2\) otherwise in the second; and \(7\) if \(n\) is even and \(1\) if \(n\) is odd in the third.

The explicit finite-field dichotomy is nonconstant already in characteristic seven: among the four smooth members with \(t\in\mathbb F_7\), \(t=0\) has \(27\) rational lines and \(99\) rational points, while \(t\in\{3,5,6\}\) has no rational lines and has \(36\) rational points. In characteristic thirteen the corresponding frequencies are one split member and nine line-free members.

## Assumptions and scope
The family is coefficient-marked: distinct values of \(t\) need not give geometrically distinct cubic surfaces. The field is always a finite field of odd characteristic at least five. The condition \(t^3+27\ne0\) is exactly the smoothness condition. The term rational line means a geometric line which is defined over the stated field; no assumption that every rational point lies on a rational line is made. The character of Frobenius is taken on the geometric rank-seven Picard group, not on the permutation representation of dimension \(27\). Counts over every extension are asserted, not just experimental counts at the first few extensions.

## Proof
**Smoothness and the nine flexes.** Write \(f_t=X^3+Y^3+Z^3+tXYZ\). On the surface, vanishing of the \(W\)-derivative forces \(W=0\), while the other derivatives are exactly those of \(f_t\). If one of \(X,Y,Z\) vanishes at a critical point, the three partial derivatives force all three to vanish. Otherwise their product gives \(t^3=-27\). Conversely when this equality holds, the gradient equations have nonzero projective solutions over the algebraic closure. Hence the claimed smoothness criterion. If the surface is smooth, the branch cubic \(f_t=0\) is a smooth plane cubic. Its nine flexes are precisely the coordinate permutations of \([0:1:-\rho]\), for \(\rho^3=1\). They are distinct because the characteristic is not three, and these are all flexes since a smooth plane cubic has nine geometric flexes, counted with their usual multiplicity, in this characteristic.

**All geometric lines and their fields.** At \(P=[0:1:-\rho]\), the flex tangent is
\[
\ell_{t,\rho}:\quad -t\rho X+3Y+3\rho^2Z=0.
\]
Substituting \(Y=(t\rho/3)X-\rho^2Z\) gives the exact polynomial identity
\[
f_t\bigl(X,(t\rho/3)X-\rho^2Z,Z\bigr)=(1+t^3/27)X^3.
\]
Consequently the inverse image of this flex tangent on \(S_t\) is the union of the three distinct lines
\[
\ell_{t,\rho}=0,\qquad W=\eta X,\qquad \eta^3=c_t,
\]
with the same expressions after the three coordinate permutations. These nine flex tangents produce \(9\cdot3=27\) distinct geometric lines. A smooth cubic surface in characteristic at least five has exactly \(27\) geometric lines, so this list is exhaustive.

If \(q\equiv1\pmod3\), all nine flexes and their tangents are defined over \(\mathbb F_q\). If \(c_t\) is a cube, every choice of \(\eta\) is rational, giving \(27\) fixed lines. Otherwise the three roots form one Frobenius three-cycle over each flex, giving nine three-cycles. If \(q\equiv2\pmod3\), only \(\rho=1\) is rational; three flexes and their tangents are fixed, while the six remaining flexes form three conjugate pairs. The cube map is bijective on \(\mathbb F_q\), so over each fixed flex one of its three lines is fixed and the other two are exchanged. Over each pair of nonrational flexes, all six lines are paired. This yields exactly three fixed lines and twelve transpositions. In this case every \(c_t\in\mathbb F_q^\times\) becomes a cube in \(\mathbb F_{q^2}\), so all \(27\) lines split over that extension.

**Picard Frobenius and the zeta function.** The divisor classes of the \(27\) geometric lines generate the geometric Picard group of a smooth cubic surface, a rank-seven lattice. Thus splitting of all lines makes Frobenius trivial on this lattice. In the first case the Picard characteristic polynomial is \((U-1)^7\). In the second case, Frobenius on every line agrees with one fixed nontrivial generator of the cubic deck group \(W\mapsto\zeta W\). Its fixed locus on the surface is the smooth genus-one curve \(W=0\). The tame Lefschetz fixed-point formula gives trace \(-2\) on degree-two étale cohomology, since that fixed curve has Euler characteristic zero and the degree-zero and degree-four traces are each one. The deck transformation has order three, so the eigenvalues on the rank-seven Picard group are one copy of \(1\) and three copies each of \(\zeta\) and \(\zeta^2\); this gives the second polynomial.

In the third case, Frobenius squared is the identity on the Picard group because all lines split over the quadratic extension. On rational points, the projection \([X:Y:Z:W]\mapsto[X:Y:Z]\) is a bijection \(S_t(\mathbb F_q)\to\mathbb P^2(\mathbb F_q)\): the cube map is bijective, so for each projective base point there is exactly one compatible \(W\). Hence \(\#S_t(\mathbb F_q)=q^2+q+1\), which by the étale trace formula gives Picard Frobenius trace \(1\). With seven eigenvalues in \(\{1,-1\}\), their multiplicities must be four positive and three negative, giving the third polynomial. For a smooth cubic surface, \(H^1=H^3=0\), \(H^0\) and \(H^4\) are Tate, and \(H^2\) is generated by divisors. Its cohomological zeta formula gives the displayed \(Z(S_t,T)\). Taking logarithms yields the point counts for all positive extension degrees.

## Verification
The standalone pure-Python file `verify_hesse.py` enumerates all projective rational points independently of the cohomological argument for every smooth parameter over the prime fields of sizes \(5,7,11,13,19,31\), compares the results against the proposed three-way formula, and checks the displayed tangent-restriction identity for all nine rational flexes in characteristics \(7,13,19,31\). Independently it constructs quadratic field extensions and computes point counts directly over \(\mathbb F_{25}\) and \(\mathbb F_{49}\), including the nonsplit case in characteristic seven. The program prints `HESSE_CUBIC_SURFACE_FROBENIUS_VERIFIED` on success. Finite checks support the proof but do not replace its all-fields argument.

## Relationship to prior work
Medrano Martín del Campo (2019) establishes the geometric correspondence between the nine flexes of a smooth branch cubic and the twenty-seven lines of its cyclic cubic surface, and computes the complex monodromy group. The present direct flex calculation specializes that geometric mechanism to the Hesse normal form and adds an explicit cubic residue criterion and all-extension arithmetic zeta factors in positive characteristic. Brundu, Logar, and Polli (2022) classify symmetric cubic surfaces and their line and Eckardt configurations over characteristic zero; this provides the symmetry context, not the finite-field arithmetic trichotomy. McKean (2021) proves general restrictions on rational line counts and shows which counts can occur over fields, but these do not determine the parameterwise answer for this Hesse pencil. A published result on the \(45\) tritangent planes of cyclic cubic surfaces determines their geometric Hesse-incidence structure, not the Frobenius arithmetic of the present pencil. Two published finite-field analyses of the Fermat cubic concern only the subfamily member \(t=0\); that known special member is not asserted to be new. The main contribution is the uniform parameter-dependent classification of the entire pencil, including its nonsplit fibers and zeta functions.

## Limitations
No claim is made about uniqueness of isomorphism classes among different marked parameters or about the moduli of all cubic surfaces. The characteristic-three family is excluded because the covering model is inseparable and singular; characteristic two is also omitted from the stated uniform theorem. The coarse three-way Frobenius classification does not identify the full set of rational points lying on geometric lines. Earlier unindexed treatments of Hesse and cyclic cubic surfaces might encode the cubic character criterion or the same zeta factors; absolute historical priority requires an independent literature audit.

## References
1. A. Medrano Martín del Campo, *Monodromy of the family of cubic surfaces branching over smooth cubic curves*, arXiv:1910.09593, first public 2019-10-21, especially Proposition 2.1 and Section 3. https://arxiv.org/abs/1910.09593
2. M. Brundu, A. Logar, F. Polli, *Construction of Symmetric Cubic Surfaces*, arXiv:2207.04493, first public 2022-07-10. https://arxiv.org/abs/2207.04493
3. S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217, first public 2021-01-20. https://arxiv.org/abs/2101.08217
4. *The 45 tritangents of a cyclic cubic surface lie over the Hesse affine plane*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-the-45-tritangents-of-a-cyclic-cubic-surface-lie-over-the-hesse--c910adbbd32c
