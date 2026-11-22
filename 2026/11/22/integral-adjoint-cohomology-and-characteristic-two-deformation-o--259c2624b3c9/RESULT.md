# Integral adjoint cohomology and characteristic-two deformation of a six-dimensional toral \(\mathfrak{sl}_2\) extension

## Finding

Let \(L_{\mathbb Z}\) be the six-dimensional Lie ring over \(\mathbb Z\) defined below, and let \(L_k=L_{\mathbb Z}\otimes_{\mathbb Z}k\) for a field \(k\). Its Chevalley–Eilenberg cohomology with **adjoint coefficients** is completely determined:

\[
H^j(L_{\mathbb Z},L_{\mathbb Z})\cong
\begin{cases}
0,&j=0,\;\text{or }j>6,\\
(\mathbb Z/2\mathbb Z)^{a_j},&1\le j\le6,
\end{cases}\qquad
(a_1,a_2,a_3,a_4,a_5,a_6)=(1,3,6,9,8,3).
\]

Consequently, for **every** field \(k\) with \(\operatorname{char} k\ne2\), all adjoint cohomology vanishes in every degree. For **every** field \(k\) of characteristic two, the adjoint Betti numbers in degrees \(0,1,\ldots,6\) are
\[
\bigl(\dim_k H^j(L_k,L_k)\bigr)_{j=0}^{6}=(1,4,9,15,17,11,3).
\]

This jump includes an integrable, nontrivial second-cohomology direction: in characteristic two, the alternating cochain \(\phi(x,y)=h+t\), vanishing on the other basis pairs, produces the Lie algebra family with \([x,y]_{\lambda}=\lambda(h+t)\). Each nonzero member has four-dimensional derived algebra, whereas \(L_k\) has three-dimensional derived algebra.

## Assumptions and scope

The underlying free \(\mathbb Z\)-module has ordered basis \((e,f,h,t,x,y)\). The only nonzero basis brackets, other than those forced by skew-symmetry and bilinearity, are
\[
[h,e]=2e,\quad [h,f]=-2f,\quad [e,f]=h,\qquad
[h,x]=x,\quad[h,y]=-y,\quad[e,y]=x,\quad[f,x]=y,\quad[t,x]=x,\quad[t,y]=y.
\]

All diagonal brackets are zero, also after reduction modulo two; therefore the Lie bracket is alternating. Direct inspection of triples gives Jacobi over \(\mathbb Z\), so base change to any field is valid. In characteristic zero this is the toral extension of \(\mathfrak{sl}_2\) by its defining two-dimensional module, with \(t\) acting as the identity. The cohomology is ordinary alternating Chevalley–Eilenberg cohomology, **not** restricted Lie cohomology.

## Proof

For \(0\le j\le6\), form the integral cochain groups
\[
C^j=\operatorname{Hom}_{\mathbb Z}(\Lambda^j L_{\mathbb Z},L_{\mathbb Z}),\qquad
\operatorname{rank}_{\mathbb Z} C^j=6\binom 6j.
\]
Their ranks are \((6,36,90,120,90,36,6)\). On a cochain \(F\) of degree \(j\), take the standard differential
\[
(dF)(u_0,\ldots,u_j)=
\sum_{i=0}^{j}(-1)^i[u_i,F(u_0,\ldots,\widehat{u_i},\ldots,u_j)]
+\sum_{0\le i<l\le j}(-1)^{i+l}
F([u_i,u_l],u_0,\ldots,\widehat{u_i},\ldots,\widehat{u_l},\ldots,u_j).
\]
Use the lexicographically ordered subsets of the fixed six-element basis for each exterior power, followed by the output-basis coordinate. This fixes **every** matrix entry as an integer. Exact elementary \(\mathbb Z\)-unimodular row and column operations, implemented in the bundled `checks/verify.py`, give the following complete Smith diagonals for \(d^j:C^j\to C^{j+1}\):

| \(j\) | Units \(1\) | Factors \(2\) | Rank |
|---|---:|---:|---:|
| 0 | 5 | 1 | 6 |
| 1 | 27 | 3 | 30 |
| 2 | 54 | 6 | 60 |
| 3 | 51 | 9 | 60 |
| 4 | 22 | 8 | 30 |
| 5 | 3 | 3 | 6 |

The algorithm admits only pivots \(1\) and \(2\), checks divisibility before quotient operations, and asserts that the unreduced rectangular block is identically zero. Thus these are Smith decompositions over \(\mathbb Z\), not estimates from finite-field experiments. It separately checks all compositions \(d^{j+1}d^j=0\) with exact integer arithmetic.

Writing \(r_j\) for the displayed rank of \(d^j\), one has \(r_{j-1}+r_j=\operatorname{rank}C^j\) for every \(j\), with the boundary conventions \(r_{-1}=r_6=0\). Hence rational cohomology is zero. Since the image of each integral differential is free abelian, the exact sequence \(0\to H^j\to\operatorname{coker}d^{j-1}\to\operatorname{im}d^j\to0\) identifies \(H^j\) with the torsion subgroup of \(\operatorname{coker}d^{j-1}\), proving the displayed integral cohomology groups.

Base change to a field preserves this complex of free abelian groups. The Smith factors are all units unless the characteristic is two. In characteristic two, the ranks of the differentials become \((5,27,54,51,22,3)\); taking kernel minus image dimensions gives \((1,4,9,15,17,11,3)\). In other characteristics, the ranks remain \((6,30,60,60,30,6)\) and all cohomology vanishes. No assumption that \(k\) is finite or algebraically closed is needed.

Finally, in characteristic two \(c=h+t\) is central: \([h+t,e]=2e=0\), \([h+t,f]=-2f=0\), and the actions of \(h\) and \(t\) on \(x,y\) cancel. Set \(\phi(x,y)=c\) and zero on every other independent wedge. The cochain differential satisfies \(d\phi=0\); this follows by direct substitution and is also checked against the integer differential modulo two. For any one-cochain \(G\), the \(t\)-coordinate of \((dG)(x,y)\) is zero because \([x,y]=0\) and every bracket with \(x\) or \(y\) is in \(\operatorname{span}(x,y)\). The \(t\)-coordinate of \(\phi(x,y)\) is one, so \([\phi]\ne0\) in \(H^2\). As \(c\) is central and \(\phi(c,-)=0\), the quadratic Jacobi obstruction vanishes. Thus \([\ ,\ ]+\lambda\phi\) is a Lie bracket for every \(\lambda\in k\). Its derived space is \(\operatorname{span}(h,x,y,h+t)\) if \(\lambda\ne0\), versus \(\operatorname{span}(h,x,y)\) for \(\lambda=0\), proving non-isomorphism to the undeformed algebra.

## Verification

Run `python3 checks/verify.py` with Python 3 and no third-party dependencies. The certificate reconstructs the bracket, verifies the Jacobi identity over the integers, constructs the six integral cochain matrices from the displayed sign convention, checks consecutive compositions vanish, and computes each exact Smith diagonal by invertible integer operations. It compares all six diagonal multiplicities and both predicted cohomology vectors against literal expected values, checks the explicit characteristic-two cocycle is closed and not exact, and directly checks Jacobi and derived-space dimensions for the two deformation types over \(\mathbb F_2\). Successful execution prints `TORAL_SL2_INTEGRAL_ADJOINT_COHOMOLOGY_OK`. The integral Smith calculations, rather than sampling finite fields, certify the conclusions for arbitrary fields.

## Relationship to prior work

Fernández and Tirao's 2026 paper defines this toral-extension construction and proves in characteristic zero that an irreducible module gives vanishing adjoint \(H^0,H^1,H^2\) (Proposition 3.1); its full-torus result, Proposition 3.4, in fact proves **all-degree characteristic-zero acyclicity**. That stronger coverage is acknowledged here and is not claimed as new. Their results are stated only over \(\mathbb C\) and do not imply integral Smith factors, a unique bad prime, or characteristic-two Betti dimensions. The present claim is exactly those integral and modular refinements, with a nontrivial integrable deformation. Campoamor-Stursberg's low-dimensional contraction study concerns real non-solvable Lie algebras, not the integral adjoint complex. Ibrayeva–Ibraev–Turbayev calculate modular deformations of the three-dimensional \(\mathfrak{sl}_2\) itself, not the six-dimensional toral extension.

## Limitations

This is the full adjoint cohomology of one canonical integral six-dimensional Lie ring and its base changes, not a classification over all semisimple modules. The characteristic-two cohomology is the **ordinary** Lie cohomology, without a restricted structure. The explicit one-parameter deformation witnesses nonrigidity but does not classify every characteristic-two deformation or all nine second-cohomology directions. Priority remains conditional on literature coverage; accessible primary sources and mathematical research indexes were compared, but unindexed precedent is possible. The calculations have not been independently audited.

## References

1. E. Fernández and P. Tirao, *Rigid Lie Algebras from Semisimple Lie Algebras and Their Symplectic Modules*, arXiv:2611.10747v1, first publicly posted 2026-11-07, https://arxiv.org/abs/2611.10747 ; relevant Propositions 3.1 and 3.4.
2. R. Campoamor-Stursberg, *Non-solvable contractions of simple Lie algebras in low dimension* (2006), https://web.ma.utexas.edu/mp_arc/c/06/06-370.pdf .
3. A. A. Ibrayeva, Sh. Sh. Ibraev, and B. E. Turbayev, *Deformations of the three-dimensional Lie algebra sl(2)* (2020), https://doi.org/10.31489/2020m1/44-51 .
