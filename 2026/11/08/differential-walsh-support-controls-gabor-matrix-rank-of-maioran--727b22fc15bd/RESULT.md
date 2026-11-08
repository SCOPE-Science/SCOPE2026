# Differential Walsh support controls Gabor matrix rank of Maiorana–McFarland graph windows

## Finding
Let \(m\ge1\), \(L=2^m\), \(D=L^2\), and let \(h:\mathbb F_2^m\to\mathbb F_2\) be arbitrary. On \(G=\mathbb F_2^m\times\mathbb F_2^m\times\mathbb F_2\) define
\[
 f_h(x,y)=x\cdot y+h(y),\qquad
 g_h(x,y,z)=\mathbf1_{\{z=f_h(x,y)\}}.
\]
Write \(D_vh(y)=h(y+v)+h(y)\), with addition in \(\mathbb F_2\), and let
\[
 s_v=\#\left\{\eta\in\mathbb F_2^m:
 \sum_{y\in\mathbb F_2^m}(-1)^{D_vh(y)+\eta\cdot y}\ne0\right\}.
\]
For all \(h\), the full complex-linear Gabor intensity-lifting operator associated with \(g_h\) has exact rank
\[
 \boxed{\operatorname{rank}_{\mathbb C}\mathcal L_{g_h}
 =D^2+4D-3+2L\sum_{v\ne0}(s_v-1).}
\]
The minimum is exactly \(D^2+4D-3\), attained precisely when the algebraic normal form of \(h\) has degree at most two. This holds even though every \(f_h\) is bent and hence has a flat ordinary Walsh spectrum. If \(m\ge3\) and \(h(y)=y_1y_2y_3\), then the exact rank is \(D^2+37D/4-3\), an increase of \(21D/4\). For example, the quadratic and cubic ranks are respectively \(4349\) and \(4685\) at \(m=3\).

## Assumptions and scope
All vector spaces, dot products, Boolean additions and Walsh characters are over \(\mathbb F_2\). The graph indicator is **unnormalized**: it has exactly \(D\) nonzero entries in an ambient vector space of dimension \(N=2D\). For a shift \(a\in G\) and a character \(\chi\in\widehat G\), write \((\pi(a,\chi)w)(t)=\chi(t)w(t+a)\). The intensity lifting map is
\[
 \mathcal L_{g_h}:M_N(\mathbb C)\longrightarrow\mathbb C^{N^2},
 \qquad \mathcal L_{g_h}(H)_{a,\chi}
 =\operatorname{tr}\!\left(H\,[\pi(a,\chi)g_h][\pi(a,\chi)g_h]^*\right).
\]
Its rank means **complex-linear rank on all matrices**, equivalently the complex dimension of the span of these projectors. The formula is not a claim about the injectivity of phaseless measurements on all complex signals, nor about the full singular-value distribution.

## Proof
**1. Weyl diagonalization of the projector orbit.** The \(N^2\) Weyl operators \(M_\chi T_a\), indexed by \((a,\chi)\in G\times\widehat G\), form an orthogonal basis of \(M_N(\mathbb C)\). Their conjugation action is diagonal on this basis. The full Gabor orbit of \(g_hg_h^*\) therefore has complex span equal to the sum of precisely those one-dimensional Weyl eigenspaces with nonzero projector coefficient. Up to a unit phase, that coefficient is the ambiguity number
\[
 A(a,\chi)=\sum_{t\in G}g_h(t)g_h(t+a)\chi(t).
\]
Consequently \(\operatorname{rank}_{\mathbb C}\mathcal L_{g_h}=\#\{(a,\chi):A(a,\chi)\ne0\}\). This equality follows from invertibility of the character table for the conjugation action and does not rely on numerical matrix rank.

**2. Explicit ambiguity counting.** Write a shift \(a=(u,v,b)\) and a modulation character \(\chi(x,y,z)=(-1)^{\alpha\cdot x+\beta\cdot y+cz}\), with all lower-case vectors in \(\mathbb F_2^m\) and \(b,c\in\mathbb F_2\). The overlap constraint for the two graph indicators is
\[
 x\cdot v=b+u\cdot y+u\cdot v+D_vh(y).
\]
There are three mutually exclusive cases, including both values of \(b\) in each indicated shift type.

If \(u=v=0\), only \(b=0\) contributes. The \(c=0\) ambiguity has just one nonzero frequency, while \(c=1\) has exactly \(D\). The total is \(D+1\).

If \(v=0\), \(u\ne0\), and \(b\) is fixed, the allowed \(y\) lie in the hyperplane \(u\cdot y=b\). For \(c=0\) the only possible \(\alpha\) is zero and the allowed \(\beta\) are \(0\) and \(u\), giving two nonzero coefficients. For \(c=1\), the nonvanishing condition is \(\alpha=y\) in that hyperplane, while \(\beta\) is free, giving \(D/2\) coefficients. Hence each of the \(2(L-1)\) shifts contributes \(D/2+2\).

If \(v\ne0\), the \(x\)-overlap is a hyperplane for every \(y\). For \(c=0\) the only possible \(\alpha\) are \(0\) and \(v\). The first gives one nonzero \(\beta\); the second is, up to a frequency shift and a nonzero scale, the Walsh transform of \((-1)^{D_vh}\), hence contributes exactly \(s_v\) nonzero \(\beta\). For \(c=1\), for each fixed \(\alpha\), only \(y=\alpha\) and \(y=\alpha+v\) survive the \(x\)-sum, and their sum is nonzero for exactly half of all \(\beta\). Thus \(c=1\) contributes \(L^2/2=D/2\) values. Each fixed \((u,v,b)\) therefore contributes \(D/2+1+s_v\).

Summing the disjoint cases gives
\[
 (D+1)+2(L-1)(D/2+2)
 +2L\sum_{v\ne0}(D/2+1+s_v)
 =D^2+4D-3+2L\sum_{v\ne0}(s_v-1).
\]
No nonzero Walsh transform has empty support, so \(s_v\ge1\) always.

**3. Rigidity of equality.** A Boolean function has exactly one nonzero Walsh coefficient if and only if its sign sequence is a signed linear character; equivalently it is affine. Hence the rank attains its minimum if and only if every nonzero derivative \(D_vh\) is affine. In the unique squarefree algebraic normal form, if \(h\) has degree at most two then every derivative is affine. Conversely, if its degree is \(d\ge3\), choose a coordinate occurring in a degree-\(d\) monomial. Differentiating in that coordinate yields at least one degree-\((d-1)\) monomial with no cancellation (distinct monomials containing the same coordinate give distinct differentiated monomials). That derivative is not affine, so its Walsh support exceeds one.

**4. Explicit genuinely nonlinear bent witness.** Let \(m\ge3\) and \(h(y)=y_1y_2y_3\). The derivative in direction \(v\) is affine if the first three coordinates of \(v\) vanish. Otherwise its degree-two polar form has rank \(2\), giving exactly \(4\) nonzero Walsh coefficients. There are \(7\cdot2^{m-3}\) such directions. Therefore the correction to the minimum is
\[
 2L\cdot7\cdot2^{m-3}\cdot(4-1)=\frac{21}{4}D,
\]
which yields the claimed cubic rank. Finally, \(f_h\) is bent for every \(h\): summing first over \(x\) in its Walsh transform forces \(y=\alpha\) and gives the coefficient \(L(-1)^{h(\alpha)+\alpha\cdot\beta}\), of constant magnitude \(L\).

## Verification
Run the complete standalone standard-library script `check.py` with Python 3. It uses integral Walsh–Hadamard transforms, computes the full ambiguity support independently of the closed formula, and exhausts all Boolean functions for \(m=1,2,3\). It also checks four explicit \(m=3,4\) cases and twelve seeded \(m=4\) samples. Output: `DIFFERENTIAL_WALSH_GABOR_CHECKS_OK cases= 292`. The infinite family and equality classification follow from the analytic proof, not the finite computations.

## Relationship to prior work
Maiorana–McFarland functions are classical bent functions; Canteaut–Daum–Dobbertin–Leander explicitly define them for arbitrary Boolean perturbation and record their bentness. Bojarovska–Flinth establishes the general Weyl-ambiguity approach to finite Gabor intensity lifting and phase retrieval. Those ingredients do not by themselves state the exact derivative-Walsh **rank correction**, its if-and-only-if algebraic-degree rigidity, or the cubic quantitative gap obtained here. The known quadratic-graph rank formula is recovered as the equality branch, not relabeled as new.

## Limitations
The ambient group is an elementary binary vector space, the perturbation is restricted to the identity-permutation Maiorana–McFarland class, and the window is a graph **indicator**. No assertion is made for arbitrary permutation representatives, arbitrary weights, general pure-state phase retrieval, or stability/conditioning. The full generality of prior historical results has not been independently checked; a stronger unlocated specialization might imply some part of the formula. Independent mathematical audit and validation have not been performed.

## References
Canteaut, Daum, Dobbertin, and Leander, *Finding nonnormal bent functions*, Discrete Applied Mathematics 154 (2006), 202–218; available online 2005-09-21. DOI: `10.1016/j.dam.2005.03.027`. Author full text: `https://www.rocq.inria.fr/secret/Anne.Canteaut/Publications/Canteaut_et_al06.pdf`.

Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first public version 2015-03-19. `https://arxiv.org/abs/1503.05800`.

Feichtinger, Kozek, and Luef, *Gabor analysis over finite Abelian groups*, arXiv:math/0703228, 2007. `https://arxiv.org/abs/math/0703228`.
