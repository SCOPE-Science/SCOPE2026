# The canonical-curve double cover and nonliftable symmetries of maximal-order \(K^2=p_g=1\) surfaces

## Finding

Let \(r\in\mathbb C^\times\setminus\{\pm1\}\), and let \(X_r\) be the smooth surface in \(\mathbb P(1,2,2,3,3)\) defined by
\[
 z_3^2+r x_0^6+x_1^3-r^2x_2^3=0,\qquad
 z_4^2+x_0^6+x_1^3-x_2^3=0.
\]
Its unique canonical divisor \(D_r=\{x_0=0\}\) is a smooth genus-two curve isomorphic to
\[
 C_s:\quad y^2=(t^3-1)(t^3-s),\qquad s=r^2.
\]
Two such canonical curves are isomorphic if and only if \(s'=s\) or \(s'=s^{-1}\). The published surface-isomorphism classification identifies exactly \(r\) and \(r^{-1}\). Thus, with explicit surface-moduli coordinate \(v=r+r^{-1}\) and canonical-curve coordinate \(u=s+s^{-1}\), the forgetful map is
\[
 u=v^2-2,\qquad v\in\mathbb C\setminus\{\pm2\},\quad u\in\mathbb C\setminus\{2\}.
\]
It is generically two-to-one, identifying the distinct surfaces \(X_r\) and \(X_{-r}\), and its only critical point in these parameter domains is \(v=0\) (equivalently \(r^2=-1\)). This statement concerns explicit coarse parameter lines; it does not assert a smooth stack-theoretic branching statement.

For every parameter, the restriction of automorphisms has image of order twelve and kernel \(\mathbb Z/6\mathbb Z\):
\[
1\longrightarrow\mathbb Z/6\mathbb Z\longrightarrow
 \operatorname{Aut}(X_r)\longrightarrow H_r\longrightarrow1,
 \qquad |H_r|=12.
\]
Its full target satisfies the complete jump spectrum
\[
|\operatorname{Aut}(D_r)|=
\begin{cases}
48,&r^4+52r^2+1=0;\\
24,&r^2=-1;\\
12,&\text{otherwise}.
\end{cases}
\]
Consequently every automorphism of \(D_r\) extends to \(X_r\) for general \(r\), whereas the index of extendable automorphisms is four at the Bolza locus and two at the sixfold-symmetric locus.

## Assumptions and scope

The base field is \(\mathbb C\), all surfaces and curves are considered up to complex isomorphism, and \(r\neq0,\pm1\). The surface equations, smoothness, the equality \(p_g=K^2=1\), the full surface automorphism order \(72\), and \(X_r\simeq X_{r'}\) precisely when \(r'=r\) or \(r'=r^{-1}\), are inputs from Duque Franco--Liendo--Montero, Theorem A. No independent extension of that surface classification is asserted. The unique canonical divisor exists because \(h^0(K_{X_r})=1\) and the canonical ring is generated in degree one by \(x_0\).

## Proof

**Canonical curve and its six branch points.** On \(x_0=0\), write \(t=x_1/x_2\) and \(w=z_3/z_4\). As rational functions on the weighted curve, these satisfy
\[
w^2=\frac{t^3-r^2}{t^3-1}.
\]
The simultaneous sign change in the weight-three coordinates is the residual weight-two projective scaling, so the generic fiber over \(t\) consists of two, not four, points. Setting \(y=w(t^3-1)\) gives the displayed hyperelliptic equation. For \(r^2\neq0,1\), its six roots are distinct. The resulting complete smooth model has genus two; the original weighted divisor is itself smooth: in every chart \(x_1\neq0\) or \(x_2\neq0\), the two equations give an unramified local coordinate except for simple branching at one of the two nonoverlapping cubic root sets, while the two points over \(t=\infty\) are unramified. Thus the model identifies the divisor, not merely its normalization.

**Complete isomorphism invariant.** Put \(s=r^2\) and fix \(a\in\mathbb C\) with \(a^3=s\). The hyperelliptic branch locus in \(\mathbb P^1\) is \(B_s=\mu_3\cup a\mu_3\), invariant under \(t\mapsto\omega t\) and \(t\mapsto a/t\), with \(\omega^3=1\) primitive. Its stabilizer contains a dihedral group of order six. By the classification of finite subgroups of \(\operatorname{PGL}_2(\mathbb C)\), a finite subgroup containing this dihedral group and preserving only six points can be this dihedral group, a dihedral group of order twelve, or the octahedral group \(S_4\): \(A_4\) has no subgroup isomorphic to \(S_3\), \(A_5\) has no orbit of size at most six on \(\mathbb P^1\), and larger dihedral groups also have no suitable six-point orbit. The order-twelve reduced dihedral case occurs exactly when the two triples form a regular hexagon, equivalently \(s=-1\).

For the octahedral case, its unique six-point orbit is projectively \(\{0,\infty,\pm1,\pm i\}\). An order-three element is \(R(z)=(i-z)/(z+i)\), cycling \(0,1,i\) and \(\infty,-1,-i\). Its fixed points are \(\alpha=(\sqrt3-1)(1+i)/2\) and \(\beta=-(\sqrt3+1)(1+i)/2\). The coordinate \(h(z)=(z-\alpha)/(z-\beta)\) conjugates \(R\) to multiplication by a primitive cube root. Explicitly \(h(0)=\sqrt3-2\) and \(h(-1)=(-1+i\sqrt3)/2\). Hence the ratio of the cubes of the two triplet radii is
\[
 s=\left(\frac{h(-1)}{h(0)}\right)^3
 =-(2+\sqrt3)^3=-26-15\sqrt3,
\]
or its inverse \(-26+15\sqrt3\). Thus the octahedral case occurs exactly at \(s^2+52s+1=0\). Conversely, the displayed projective transformation realizes this configuration, proving sufficiency.

Every isomorphism of genus-two curves descends to a projective equivalence of their six-point branch sets. In the generic dihedral case its unique order-three rotation subgroup is intrinsic, so the projective equivalence must normalize \(t\mapsto\omega t\) and has the form \(t\mapsto ct\) or \(t\mapsto c/t\). This gives \(s'=s\) or \(s'=s^{-1}\). At the hexagonal case \(s=-1\), group order distinguishes it from other parameters. At the octahedral case all order-three subgroups of \(S_4\) are conjugate, so the same normalizer argument applies after composing with a target automorphism. Thus the isomorphism criterion holds at every allowed parameter. The reduced stabilizer sizes are \(6,12,24\); each projective symmetry admits two lifts to the hyperelliptic curve, so the full automorphism orders are \(12,24,48\).

**Surface automorphism restriction.** There are \(36\) diagonal automorphisms
\[
 x_0\mapsto x_0,\quad x_1\mapsto\omega^a x_1,\quad
 x_2\mapsto\omega^b x_2,\quad z_3\mapsto\epsilon z_3,\quad z_4\mapsto\delta z_4,
\]
where \(a,b\in\{0,1,2\}\) and \(\epsilon,\delta\in\{\pm1\}\). Choose constants \(A,B,C,D\in\mathbb C^\times\) with \(A^3=-r\), \(B^3=-r^{-1}\), \(C^2=r\), \(D^2=r^{-1}\). Exchanging the pairs by
\[
 (x_0,x_1,x_2,z_3,z_4)\longmapsto
 (x_0,A x_2,B x_1,Cz_4,Dz_3)
\]
pulls the first defining equation back to \(r\) times the second and the second to \(r^{-1}\) times the first. It is not diagonal, so these maps generate a subgroup of order \(72\), and by the published automorphism bound they exhaust \(\operatorname{Aut}(X_r)\).

On the canonical curve the diagonal maps induce \((t,w)\mapsto(\omega^{a-b}t,(\epsilon/\delta)w)\), giving six distinct transformations, while the exchange induces \((t,w)\mapsto(k/t,r/w)\) for a choice of \(k^3=s\) and signs. Together they generate the hyperelliptic involution and the full order-twelve lift of the reduced dihedral group. Exactly six diagonal automorphisms act trivially (\(a=b\), \(\epsilon=\delta\)); they form \(\mu_3\times\mu_2\simeq\mu_6\), and no exchange acts trivially. This proves the kernel, image, and exceptional nonextension indices.

Finally the known surface-isomorphism criterion gives the parameter \(v=r+r^{-1}\), while the established canonical-curve criterion gives \(u=s+s^{-1}=r^2+r^{-2}\). The identity \(u=v^2-2\) completes the claimed degree-two map and identifies its sole critical point.

## Verification

The accompanying Python 3 standard-library script `verify.py` checks the exchange pullbacks coefficientwise over rational sample parameters, the identity \(u=v^2-2\), and the exact quadratic equation for both octahedral branch parameters. It also reconstructs all \(120\) possible ordered three-image Möbius transformations of each six-point set and numerically obtains reduced stabilizer sizes \(6,12,24,24\) at \(s=4,-1,-26+15\sqrt3,-26-15\sqrt3\). Its last line is `VERIFY_OK`. These finite complex-number diagnostics are *not* the proof of the uniform stabilizer classification, which is the group-theoretic argument above; nor are they a replacement for the published surface automorphism classification.

## Relationship to prior work

Duque Franco--Liendo--Montero prove the surface automorphism bound and classify the explicit \(72\)-automorphism surfaces and their isomorphisms. Cardona--Quer classify the classical genus-two dihedral-automorphism locus and associated elliptic quotients. The present statement does not claim those results. Its subject is the specific *restriction and information loss* map from the new surface family to its unique canonical curves, with a complete fiber and nonliftable-automorphism jump classification. No exact such surface-to-canonical-curve statement was found in the inspected material. Combining the two existing classifications narrows the originality margin, and broader uninspected Catanese literature remains a historical-priority risk.

## Limitations

The result concerns only the explicit smooth \(72\)-automorphism family over \(\mathbb C\). It neither classifies canonical curves of arbitrary \((K^2,p_g)=(1,1)\) surfaces nor settles stack-level ramification or derived/period-theoretic Torelli questions. The older source's general genus-two classification already covers the unadorned dihedral curve family; novelty is asserted only for the surface-to-curve relationship and the liftability classification. Independent mathematical validation has not been performed.

## References

1. J. Duque Franco, A. Liendo, P. Montero, *Automorphisms and Hodge isometries of surfaces with \(K^2=p_g=1\)*, arXiv:2610.33364v1, October 23, 2026. https://arxiv.org/abs/2610.33364
2. G. Cardona and J. Quer, *Curves of genus 2 with group of automorphisms isomorphic to \(D_8\) or \(D_{12}\)*, arXiv:math/0203165v1, March 17, 2002. https://arxiv.org/abs/math/0203165
