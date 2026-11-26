# Singularities and dual class of the nonextendable Galois-point septic

## Finding

Let \(C\subset\mathbb P^2_{\mathbb C}\) be the image of
\[
\nu:\mathbb P^1\longrightarrow\mathbb P^2,\qquad
[u:v]\longmapsto [u(v^6-u^6):u^5(u^2+v^2):v^5(u^2+v^2)].
\]
This is the degree-seven curve used in Abouelsaad's nonextendibility example for a cyclic order-five Galois point. Its **complete** geometric singularity basket is
\[
\boxed{13A_1+A_4},
\]
meaning thirteen distinct ordinary nodes and one unibranch plane cusp analytically equivalent to \(y^2=x^5\). More precisely, the cusp is \(Q=[-1:1:0]\); one node is \(P=[1:0:0]\), the inner Galois point of the source; and twelve further nodes are specified explicitly below. The projective dual has degree
\[
\boxed{\deg(C^\vee)=11}.
\]

## Assumptions and scope

The base field is \(\mathbb C\); all singularities and tangent lines are geometric. The normalizing coordinate is \(t=v/u\) on \(u\neq0\), so
\[
\nu(t)=[t^6-1:1+t^2:t^5(1+t^2)].
\]
Write \(f(t)=(t^6-1)/(t^2+1)\). Choose a primitive fifth root \(\zeta\) of unity, and for \(k\in\{1,2,3,4\}\) set \(a=\zeta^{2k}\) and
\[
T_a(w)=a(1+a)w^3+(1+a+a^2)w^2+1.
\]
For each such \(k\), take the three roots \(w\) of \(T_a\) and the two choices \(t\) with \(t^2=w\). Each \(\{t,\zeta^k t\}\) gives one ordered presentation of an ordinary node. In total these twenty-four presentations pair into twelve distinct nodes. No assertion is made about positive characteristic.

## Proof

**1. Normalization and degree.** The three degree-seven binary forms have no common zero: at \(u=0\), the third is \(v^7\); at \(v=0\), the second is \(u^7\); and \(u^2+v^2=0\) with \(uv\neq0\) gives \(u(v^6-u^6)=-2u^7\neq0\). Thus \(\nu\) is a morphism. Away from \(t=0,\infty\) and \(t^2=-1\), projection from \(P\) gives \(Z/Y=t^5\). A second point in the same fiber has parameter \(\zeta^k t\), but equality of \(X/Y=f(t)\) is not an identity for any nontrivial fifth root, by the displayed cubic calculation below. Therefore \(\nu\) is generically injective, hence birational to its image; the image has degree seven and \(\nu\) is its normalization.

**2. The unibranch cusp.** Near \(t=0\), use \(Y\neq0\) with \(x=X/Y=f(t)\) and \(y=Z/Y=t^5\). The rational function \((w^3-1)/(w+1)\) has value \(-1\) and derivative \(1\) at \(w=0\). Hence a local analytic target coordinate is \(w=t^2\), with the other coordinate \(y=t^5\). The local equation is \(y^2=w^5\): this is the \(A_4\) cusp, with multiplicity \(2\), Milnor number \(4\) and delta invariant \(2\).

**3. The distinguished node.** The two points \(t=i,-i\) both map to \(P=[1:0:0]\). Their branches are immersed and have different tangent ratios \(d(Z/X)/d(Y/X)=i,-i\). An independently checked implicit equation has quadratic part \(X^5(Y^2+Z^2)\) at \(P\), confirming that its tangent cone consists of two distinct lines. Thus \(P\) is an ordinary node. The point \(t=\infty\) maps to \([0:0:1]\), where \(X/Z\) is a uniformizer, so this point is smooth. No other parameter has the same image as \(0\), \(\infty\) or \(\pm i\), except the indicated pair \(\{i,-i\}\).

**4. Twelve further nodes.** If \(t\neq0,\infty\) and \(1+t^2\neq0\), a distinct parameter with the same image must be \(s=\zeta^k t\) for a unique \(k\in\{1,2,3,4\}\), because \(Z/Y=s^5=t^5\). With \(a=\zeta^{2k}\), \(w=t^2\), direct subtraction gives
\[
f(t)-f(\zeta^k t)=
\frac{(1-a)wT_a(w)}{(w+1)(aw+1)}.
\]
The values \(T_a(0)=1\) and \(T_a(-1)=T_a(-a^{-1})=2\) exclude degenerate and pole parameters. Exact arithmetic in \(\mathbb Q(\zeta)\) proves that each cubic \(T_a\) has three simple roots and that distinct \(T_a,T_b\) share none. A compact certificate is:
\[
\bigl|N_{\mathbb Q(\zeta)/\mathbb Q}(\operatorname{disc}T_a)\bigr|=674041,
\qquad
\bigl|N_{\mathbb Q(\zeta)/\mathbb Q}(\operatorname{Res}(T_a,T_b))\bigr|=2000
\quad(a\neq b).
\]
Both norms are nonzero. There are \(4\cdot3\cdot2=24\) directed distinct parameter coincidences; reversing the pair divides this count by two, giving **twelve distinct double-image points**. The nonzero derivative of the difference along the common local coordinate \(t^5\) follows from the simplicity of each root \(T_a\), so the two branches have distinct tangents: every such point is an ordinary node. No image has three branches, since that would make two distinct cubics share a root.

**5. Exhaustion and dual degree.** For any nonzero finite \(t\) with \(t^2\neq-1\), the projected coordinate \(t^5\) is étale, so \(\nu\) is immersed. The two remaining charts were handled in steps 2 and 3, and \(\infty\) is smooth. Thus there are no other singularities. The delta sum is \(13\cdot1+2=15=(7-1)(7-2)/2\), providing an independent arithmetic-genus check. The Plücker class formula, using local Milnor and multiplicity data, yields
\[
\deg(C^\vee)=7(7-1)-13(1+2-1)-(4+2-1)=11.
\]
As a second exact description, differentiation of the displayed parametrization gives the tangent-line map in affine parameter \(t\), after removing its common factor:
\[
[5t^3(t^2+1)^2:\;-t^3(t^8-t^6-7t^2-5):\;-2(2t^6+3t^4+1)].
\]
The homogeneous completion has degree eleven, agreeing with the Plücker calculation.

## Verification

Run `python3 septic_check.py` with Python's standard library. The checker performs exact fraction arithmetic in the cyclotomic field via the relation \(\zeta^4+\zeta^3+\zeta^2+\zeta+1=0\); constructs the four coincidence cubics; obtains four discriminant norms \(674041\) and all six pairwise-resultant norms \(2000\); checks the exceptional denominator values, an implicit septic equation with nodal tangent cone at the Galois point, projective tangent cross-products and genus/class arithmetic. Its successful output is:

`VERIFY_OK degree=7 nodes=13 cusp=A4 dual_degree=11 discriminant_norms=4x674041 pair_resultant_norms=6x2000`

The proof also explicitly covers the local analytic charts and noncoincidence conditions; the finite computation is not being substituted for those geometric arguments.

## Relationship to prior work

Abouelsaad, *Galois points and Cremona transformations*, arXiv:2302.00324v1, Lemma 5.2 and Theorem C, supplies exactly this septic parametrization, identifies the order-five inner Galois point and proves nonextendibility of its Galois action. The source establishes birationality and excludes singularities of multiplicity at least three, but does not give the complete analytic singularity basket, the twelve ordinary-node coincidences, or the dual degree. One incidental sentence in its multiplicity argument calls \(P\) smooth; the explicit normalization has two distinct branches over \(P\), and the checked implicit equation has tangent cone \(Y^2+Z^2\) in the chart \(X=1\), showing that \(P\) is in fact nodal. This refines that local description without challenging the published nonextendibility conclusion. The later open-access journal version has the same relevant construction and focuses on Cremona extendibility. Miura's related article arXiv:2302.00870 treats order-three extensions, not this order-five septic's singularities. The twelve-node cubic coincidence proof and complete \(13A_1+A_4\) basket refine the exact source without claiming the source's nonextendibility theorem as new.

## Limitations

The result is for this specific complex septic; it does not classify all rational septics, all Galois-point curves, or behavior in positive characteristic. The exact coincidence polynomials are computed over the characteristic-zero cyclotomic field, and the Plücker formula is applied in characteristic zero. The computations do not constitute an independent external mathematical audit. A differently indexed treatment of this exact curve's singularities remains a bibliographic risk.

## References

1. Ahmed Abouelsaad, *Galois points and Cremona transformations*, arXiv:2302.00324v1 (public 2023-02-01), especially Theorem C and Lemma 5.2; open version: https://arxiv.org/pdf/2302.00324.
2. Ahmed Abouelsaad, *Galois points and Cremona transformations*, *Glasgow Mathematical Journal* **66** (2024), 471–478, doi:10.1017/S0017089524000090; open-access version: https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/galois-points-and-cremona-transformations/1A2EC8196A391E1DE5AADA0F853B3F51.
3. Kei Miura, *Extendable birational transformations belonging to Galois points*, arXiv:2302.00870v1 (2023-02-02), https://arxiv.org/pdf/2302.00870.
