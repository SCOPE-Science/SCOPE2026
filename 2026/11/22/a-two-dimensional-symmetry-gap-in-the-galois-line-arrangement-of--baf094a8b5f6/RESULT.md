# A two-dimensional symmetry gap in the Galois-line arrangement of a characteristic-two maximal curve

## Finding

Let \(k\) be an algebraic closure of \(\mathbb F_2\), let \(q=2^n\ge4\), let \(K=\mathbb F_{q^2}\subset k\), and let \(L_q(T)=\sum_{i=0}^{n-1}T^{2^i}\). Consider the smooth projective model \(C\) of \(L_q(x)=y^{q+1}\), embedded by \(\varphi=(x:y:1:y^2)\) in \(\mathbb P^3_k\). Denote its **unlabelled** set of all Galois lines by \(\mathcal G\). Higashine's classification (Reference 1) gives the following exhaustive families, in coordinates \([X:Y:Z:W]\):

\[
A_t=V(Z,X+tY+t^2W)\quad(t\in K),\qquad
B_c=V(Y+cZ,W+c^2Z)\quad(c\in k),\qquad
D_d=V(Z,Y+dW)\quad(d\in K).
\]

Thus \(\mathcal G=\{A_t:t\in K\}\cup\{B_c:c\in k\}\cup\{D_d:d\in K\}\). The **complete setwise projective stabilizer** of \(\mathcal G\) is the group of matrices

\[
\boxed{
M(a,b,u,v)=
\begin{pmatrix}
a^2&ab&u&b^2\\
0&a&v&0\\
0&0&a^2&0\\
0&0&v^2/a^2&1
\end{pmatrix}
\quad\text{with }a\in K^\times,\ b\in K,\ u,v\in k.
}
\]

Each matrix denotes its class in \(\operatorname{PGL}_4(k)\). In particular, as a reduced algebraic group, the stabilizer is

\[
\operatorname{Stab}_{\operatorname{PGL}_4(k)}(\mathcal G)
\simeq \mathbf G_a^2\rtimes\operatorname{AGL}_1(K),
\]

where the finite affine group acts via the displayed matrices with \(u=v=0\). Under the additional requirement that each line retain the **isomorphism type of its associated projection Galois group**, the same matrices occur with the sharper condition \(a^{q+1}=1\); this labelled stabilizer is \(\mathbf G_a^2\rtimes (K^+\rtimes\mu_{q+1})\).

The two-dimensional connected stabilizer acts nontrivially on the embedded curve. More precisely, for each \((s,t)\in k^2\) the projective curve

\[
C_{s,t}=\overline{\left\{[x:y:1:y^2]:
L_q(x)=y^{q+1}+ty^q+t^qy+t^{q+1}+s\right\}}
\]

is smooth, irreducible, and projectively equivalent to \(C\); the curves \(C_{s,t}\) are pairwise distinct **as embedded subsets of the fixed \(\mathbb P^3_k\)**, but their Galois-line sets and associated Galois-group isomorphism labels are identical. Thus even the complete labelled Galois-line configuration does not reconstruct this embedded curve.

## Assumptions and scope

Everything is over the algebraically closed characteristic-two field \(k\). The integer \(n\) ranges over all \(n\ge2\). The source curve is the nonsingular projective model of the affine equation; the closure in the definition of \(C_{s,t}\) is the projective scheme-theoretic closure of its image. We study **setwise stabilizers of geometric lines**, not automorphisms of the embedded curve or the potentially nonreduced stabilizer group scheme. The two finite families have parameters in \(K\); the third, \(B_c\), has parameter in all of \(k\). These different domains are essential.

## Proof

**1. Intrinsic recovery of the common point and plane.** Put \(P=[1:0:0:0]\) and \(H=V(Z)\). Every \(B_c\) and every \(D_d\) contains \(P\); no \(A_t\) contains it. Distinct \(B_c\)'s meet only at \(P\), and the other line families are finite. Hence \(P\) is the unique point incident with infinitely many lines of \(\mathcal G\), so every projective setwise symmetry fixes \(P\).

All \(A_t\) and \(D_d\) lie in \(H\), and no \(B_c\) lies in \(H\). If \(H'\ne H\) is a plane through \(P\), it contains no \(A_t\), at most one \(D_d\), and at most two \(B_c\): the latter direction vectors \([c:1:c^2]\) form a nonsingular conic in the projective plane of directions from \(P\), so a line cuts them in at most two points. A plane not through \(P\) contains no \(B_c\) or \(D_d\) and at most one \(A_t\). Therefore \(H\) is the unique plane containing at least four distinct Galois lines. Every setwise symmetry fixes \(H\), and on \(H\) it preserves separately the \(A_t\)'s (not through \(P\)) and the \(D_d\)'s (through \(P\)).

**2. Rigidity of the finite dual conic.** The lines \(A_t\subset H\) correspond, in the dual plane \(H^\vee\), to the \(q^2\) points \([1:t:t^2]\), \(t\in K\), lying on the smooth conic \(\Gamma:U_0U_2=U_1^2\). Since \(q^2\ge16>4\), Bezout's theorem forces any projectivity of the dual plane preserving this finite set to preserve \(\Gamma\). Its induced fractional-linear transformation preserves the finite set \(K\subset\mathbb P^1(k)\). A fractional-linear map carrying any three distinct \(K\)-points to \(K\)-points has coefficients in \(K\) up to scalar. It therefore preserves \(\mathbb P^1(K)\) and must fix the unique missing point \(\infty\). Consequently the induced map is \(t\mapsto at+b\), with \(a\in K^\times\) and \(b\in K\).

In the ordered coordinates \((X,Y,W)\) on \(H\), the unique projectivity realizing this dual-conic action is

\[
(X,Y,W)\longmapsto(a^2X+abY+b^2W,\ aY,\ W),
\]

because direct substitution gives
\[
X'+(at+b)Y'+(at+b)^2W'=a^2(X+tY+t^2W).
\]

**3. Exact extension off the plane.** Any projectivity of \(\mathbb P^3\) fixing \(H\) and restricting to the preceding map has, after choosing its unique scalar normalization, the form

\[
X'=a^2X+abY+b^2W+uZ,\quad Y'=aY+vZ,\quad Z'=\delta Z,\quad W'=W+wZ,
\]

where \(\delta\ne0\). A line \(B_c\) has points \([X:c:1:c^2]\), with arbitrary \(X\); its image must be \(B_{c'}\) with \(c'=(ac+v)/\delta\). The second defining equation of \(B_{c'}\) requires

\[
\frac{c^2+w}{\delta}=\left(\frac{ac+v}{\delta}\right)^2
\quad\text{for every }c\in k.
\]

Comparing coefficients of this polynomial identity yields \(\delta=a^2\) and \(w=v^2/a^2\). Thus the displayed \(M(a,b,u,v)\) are necessary. Conversely they send \(A_t\mapsto A_{at+b}\), \(D_d\mapsto D_{ad}\), and \(B_c\mapsto B_{c/a+v/a^2}\), so are sufficient. The kernel of the homomorphism induced on \(\{A_t\}\) is \(M(1,0,u,v)\), an additive \(\mathbf G_a^2\); the matrices \(M(a,b,0,0)\) split the quotient \(\operatorname{AGL}_1(K)\).

**4. Preservation of Galois-group labels.** Higashine's theorem states that \(A_t\) has cyclic Galois group of order \(q+1\); every \(B_c\), and \(D_0\), has elementary abelian Galois group of order \(q/2\); for nonzero \(d\), the group of \(D_d\) is elementary abelian of order \(q\) exactly if \(d^{q+1}=1\), and otherwise has a cyclic order-four factor. Since \(D_d\mapsto D_{ad}\), its group-type partition is preserved precisely when \(a^{q+1}=1\). No restriction on \(b,u,v\) is required. This proves the labelled formula.

**5. Failure of embedded reconstruction.** The connected subgroup \(U=\{M(1,0,u,v):u,v\in k\}\) acts on affine coordinates by \((x,y,y^2)\mapsto(x+u,y+v,(y+v)^2)\). Because \(L_q\) is additive, this translates \(C\) to \(C_{s,t}\) with \(s=L_q(u)\) and \(t=v\). The additive polynomial \(L_q\) has degree \(q/2\), nonzero formal derivative \(1\), and is surjective on \(k\), so every \((s,t)\) occurs and exactly \(q/2\) values of \(u\) give a fixed \(s\). If two displayed equations define the same embedded affine curve, the right sides must agree for every \(y\), because \(L_q\) is surjective and the fibers over each \(y\) are nonempty. Comparing coefficients of \(y^q\) forces the two \(t\)'s to agree, and comparing constants then forces the two \(s\)'s to agree. The projective closures are therefore pairwise distinct. The action of \(U\) fixes all \(A_t\) and all \(D_d\), while permuting all \(B_c\) by translation; their Galois-group labels are constant within this last family. Thus every \(C_{s,t}\) has the same labelled Galois-line set as \(C\), completing the proof.

## Verification

The standalone Python 3 program `CHECK.py` uses exact arithmetic in \(\mathbb F_{16}\) and \(\mathbb F_{64}\). It verifies the transformation identities for all three families at 720 selected matrices over the former field and 48 selected matrices over the latter, across all parameters in each field, and checks the kernel size of \(L_q\). Run `python3 CHECK.py` with no dependencies. The tests exercise 11,520 and 3,072 parameter cases respectively and passed. This finite verification is supplementary; the quantifiers for all \(n\ge2\), \(c\in k\) and all projective symmetries are covered by the proof above, not by enumeration.

## Relationship to prior work

Higashine's 2026 theorem (Reference 1) completely classifies the Galois lines and computes their projection Galois groups. Its Fact 6 classifies automorphisms of the **curve**, which form a finite group of order \(q^3(q+1)/2\). The present theorem instead classifies automorphisms of the **line configuration**, gives its connected two-dimensional subgroup, distinguishes labelled and unlabelled symmetry, and proves a two-parameter failure of ambient reconstruction. The conic-rigidity argument, extension calculation and reconstruction comparison are not the same as determining the individual Galois lines or the curve's automorphism group. Fukasawa's earlier work (References 2 and 3) studies other Galois-line configurations in related positive-characteristic curves, rather than the stated stabilizer of this explicit characteristic-two configuration.

## Limitations

No assertion is made that the distinct embedded curves \(C_{s,t}\) are abstractly nonisomorphic: they are all projectively equivalent. The stabilizer is computed on geometric \(k\)-points (equivalently its reduced algebraic-group structure); no claim about an infinitesimal nonreduced stabilizer scheme is made. The result requires \(q\ge4\), and concerns the entire Galois-line set including \(B_c\) for **all** \(c\in k\), not only rational lines. The priority comparison is confined to accessible indexed mathematical records and inspected sources; undiscovered prior formulations remain possible.

## References

1. Kazuki Higashine, *Galois lines for the maximal curve with the second largest genus in characteristic two*, arXiv:2611.08810v1, first submitted 2026-11-06, §§1–3, especially main theorem and Fact 6. https://arxiv.org/abs/2611.08810
2. Satoru Fukasawa, *Galois lines for the quotient curve of the Hermitian curve by an involution*, arXiv:2207.03759v1, 2022. https://arxiv.org/abs/2207.03759
3. Satoru Fukasawa, *Galois lines for the Artin–Schreier–Mumford curve*, arXiv:2005.10073v1, 2020. https://arxiv.org/abs/2005.10073
