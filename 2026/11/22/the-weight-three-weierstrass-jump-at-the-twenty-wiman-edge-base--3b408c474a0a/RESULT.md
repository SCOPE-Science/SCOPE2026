# The weight-three Weierstrass jump at the twenty Wiman–Edge base points

## Finding

Let \(C_\varphi\) be any smooth complex member of the Wiman–Edge pencil of genus-six curves on the quintic del Pezzo surface \(S\). The twenty base points \(\Delta\) of the pencil are all canonically ordinary unless \(4\varphi^2=105\). Precisely at those two smooth parameter values, every point of \(\Delta\) has canonical vanishing sequence
\[
(0,1,2,3,5,7),
\]
canonical gap sequence \((1,2,3,4,6,8)\), and Weierstrass weight three. They therefore contribute \(20\cdot3=60\) to the total canonical ramification weight \(6(6^2-1)=210\). The two exceptional parameters correspond to one geometric isomorphism class, as odd permutations of five letters exchange \(\varphi\) with \(-\varphi\). This is a classification **on the distinguished twenty-point base locus**, not a classification of all Weierstrass points of each curve.

## Assumptions and scope

Work over \(\mathbb C\). Write \(x=\sigma\), \(y=\tau\) on an affine chart of \(\mathbb P^1\times\mathbb P^1\), and use the explicitly normalized Wiman–Edge pencil from Candelas–de la Ossa–van Geemen–van Straten:
\[
\begin{aligned}
G={}&3x^2y^2-\tfrac12xy(1+x)(1+y)(1+xy)\\
&+(1-x+x^2)(1-y+y^2)(1-xy+x^2y^2),\\
H={}&xy(1-x)(1-y)(1-xy),\\
F_\varphi={}&G+\varphi H.
\end{aligned}
\]
Its three fixed ordinary nodes on \(\mathbb P^1\times\mathbb P^1\) are resolved by blowing up \((1,1),(0,\infty),(\infty,0)\); the blowup is \(S\), with \(C_\varphi\in|-2K_S|\). Smoothness is equivalent to excluding \(\varphi=\infty\), \(4\varphi^2=-3\), and \(4\varphi^2=125\). In particular, the points \(4\varphi^2=105\) are smooth fibers. The twenty base points form one transitive \(A_5\)-orbit. One representative is \((x,y)=(1,u)\), where \(u^2-u+1=0\). On this affine chart, every fiber is smooth at this point.

The canonical vanishing sequence \((a_0,\ldots,a_5)\) at a point means that the six-dimensional space of canonical sections admits a basis vanishing to these orders. Its Weierstrass weight is \(\sum_{i=0}^5(a_i-i)\). These are ordinary characteristic-zero canonical notions; there is no assertion about positive-characteristic Hasse orders.

## Proof

**Canonical sections.** Since \(C_\varphi\sim-2K_S\), adjunction gives \(K_{C_\varphi}=(-K_S)|_{C_\varphi}\). The anticanonical restriction map is an isomorphism on global sections: its kernel is \(H^0(S,K_S)=0\), and the obstruction is \(H^1(S,K_S)=0\) for the rational del Pezzo surface. Thus \(h^0(K_{C_\varphi})=6\). In the affine \((x,y)\)-trivialization, the following six sections of \(-K_S\) are linearly independent, and all satisfy the conditions of passing through the three blowup centers:
\[
(z_0,z_1,z_2,z_3,z_4,z_5)=
(x^2y^2-1,\,xy^2-1,\,x^2y-1,\,xy-1,\,y-1,\,x-1).
\]
They hence restrict to a canonical basis. Changing the local trivialization multiplies all six functions by a common unit, which does not alter their vanishing sequence.

**Exact local jets.** Fix \(P=(1,u)\) with \(u^2-u+1=0\). For \(2F_\varphi\), the \(y\)-partial derivative at \(P\) is \(4-2u\), with inverse \((1+u)/6\). Therefore \(t=x-1\) is a uniformizer, and there is a unique formal series \(y(t)=u+\sum_{j\ge1}b_jt^j\) solving \(2F_\varphi(1+t,y(t))=0\). Its coefficients lie in \(\mathbb Q[u,\varphi]/(u^2-u+1)\), and recursion is exact: if the coefficients before order \(n\) are fixed, then
\[
b_n=-\frac{1+u}{6}\,[t^n]\left(2F_\varphi(1+t,u+\textstyle\sum_{j<n}b_jt^j)\right).
\]
Let \(J=(J_{ij})\) be the six-by-six matrix of coefficients \(J_{ij}=[t^j]z_i(1+t,y(t))\), with row indices \(i=0,\ldots,5\), column indices \(j=0,\ldots,5\). Exact rational elimination in the quotient ring gives
\[
\det J=\frac{(4\varphi^2-105)(4\varphi^2+3)^3}{62208}.
\]
The \((4\varphi^2+3)\)-factor corresponds to excluded singular fibers. On every smooth fiber outside \(4\varphi^2=105\) the determinant is nonzero, proving canonical vanishing sequence \((0,1,2,3,4,5)\).

**Order seven at the exceptional fiber.** Reduce the coefficients by \(\varphi^2=105/4\). Every five-by-five minor from columns \(0,1,2,3,4\) vanishes, while the four-by-four minor with rows and columns \(0,1,2,3\) is
\[
4\varphi u-2\varphi-3u+27.
\]
It is nonzero: its field norm from \(\mathbb Q(u)\) equals \(3(4\varphi^2-6\varphi+219)\), nonzero at \(\varphi^2=105/4\). A five-by-five minor from rows \(0,1,2,3,4\) and columns \(0,1,2,3,5\) is
\[
-27\varphi u-\tfrac{81}{2}u+81,
\]
whose norm is \(729(4\varphi^2+27)/4\), again nonzero. Every six-by-six minor using columns in \(\{0,1,\ldots,6\}\) vanishes at \(\varphi^2=105/4\). But the six-by-six minor with columns \((0,1,2,3,5,7)\) equals \(-486\varphi\), nonzero on that locus. The rank jumps in the six-dimensional jet filtration therefore occur exactly at orders \(0,1,2,3,5,7\). This establishes the claimed gaps and weight three at \(P\).

**Entire base locus.** The \(A_5\)-action on every member preserves the canonical linear series and is transitive on the twenty base points. Hence the identical vanishing sequences hold at all of \(\Delta\). The odd part of \(S_5\) exchanges \(C_\varphi\) with \(C_{-\varphi}\), identifying the two smooth exceptional fibers as unmarked curves.

## Verification

The accompanying standalone `verify_wiman.py` uses exact rational arithmetic in \(\mathbb Q[u,\varphi]/(u^2-u+1)\), constructs the formal solution through degree seven, verifies the displayed six-by-six determinant identity symbolically, checks all six exceptional five-by-five minors with orders at most four, checks all seven exceptional six-by-six minors with orders at most six, and verifies the three displayed nonzero minors through order seven. It prints `WIMAN_BASEPOINT_CANONICAL_RAMIFICATION_VERIFIED_OK` only if all assertions hold. Python and SymPy are required; no floating-point approximations are used. The finite jet calculation is exhaustive for the *specified* canonical order claims because the nonzero and vanishing minors establish the exact successive ranks; no inference from finite sampling to an infinite family is made.

## Relationship to prior work

Candelas–de la Ossa–van Geemen–van Straten give the exact \(G,H\) model, identify the twenty persistent van Geemen points and the excluded singular parameters. Dolgachev–Farb–Looijenga prove that the twenty base points form the distinguished orbit, and develop the global geometry of the pencil. Inoue–Kato and Edge describe its classical construction. These structural statements do not determine the canonical jet filtration at the base points; the new contribution is the exact exceptional Weierstrass condition and the full vanishing sequence on this intrinsic orbit. An earlier computation in the 1981 Edge papers is possible and was not ruled out by complete full-text comparison.

## Limitations

The result describes only the twenty distinguished base points of smooth complex fibers. It does not calculate the remaining canonical ramification divisor (of degree \(150\) in the exceptional fibers, counted with multiplicity), the Weierstrass semigroups beyond the canonical gap sequence, or the behavior of singular fibers. Historical originality remains subject to independent review; the 1981 Edge paper was identifiable but its entire text was not accessible for close comparison. The explicit proof and symbolic verifier establish the mathematics within the stated model and hypotheses, not independent certification.

## References

- P. Candelas, X. de la Ossa, B. van Geemen, D. van Straten, *Lines on the Dwork Pencil of Quintic Threefolds* (first arXiv version 21 June 2012), https://arxiv.org/abs/1206.4961, especially §§2.2, 3.3–3.4, and 5.
- I. Dolgachev, B. Farb, E. Looijenga, *Geometry of the Wiman–Edge Pencil, I: Algebro-geometric aspects*, European J. Math. 4 (2018), 879–930, https://doi.org/10.1007/s40879-018-0231-3, especially Lemma 3.1 and §3.5.
- N. Inoue, F. Kato, *On the Geometry of Wiman's Sextic* (2005 preprint), https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf.
- W. L. Edge, *A Pencil of Specialized Canonical Curves*, Math. Proc. Cambridge Philos. Soc. 90 (1981), 239–249, https://doi.org/10.1017/S0305004100058692 (abstract and bibliographic information examined; full text not accessed).
