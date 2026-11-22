# A noncurvilinear characteristic-three collision of four fixed points on the quintic del Pezzo surface

## Finding

Let \(S=\overline{M}_{0,5}\) be the smooth split degree-five del Pezzo surface over \(\operatorname{Spec}\mathbb Z\), with the natural permutation action on five markings. Let \(\sigma=(123)\) act on the first three markings. **The entire scheme-theoretic fixed locus, over the integers**, is the finite flat degree-four scheme

\[
\operatorname{Fix}_S(\sigma)\cong
\operatorname{Spec}\mathbb Z[u,v]/(v^2-v+1,\;u(u+2-v)).
\]

For every algebraically closed field \(k\) of characteristic different from \(3\), this is four reduced geometric points: two on the invariant boundary divisor \(D_{\{1,2,3\}|\{4,5\}}\) and two in \(M_{0,5}\). In characteristic \(3\), all four coalesce at a single boundary point and the fixed scheme has local algebra

\[
 k[u,w]/(w^2,\;u(u-w)),
\]

of length four, embedding dimension two, and Hilbert function \((1,2,1)\). Thus the wild fixed point is isolated and **noncurvilinear**. Its ambient tangent action is the identity, but the order-three automorphism is nontrivial; it cannot be formally linearized at that point.

## Assumptions and scope

All schemes and fixed loci are scheme-theoretic and over \(\mathbb Z\), with the action defined by permuting labels of stable five-pointed genus-zero curves. The fixed locus means the equalizer of the identity and the indicated permutation automorphism, not just the reduced set of fixed points. After excluding the other blow-up centers and normalization poles, the displayed exceptional-divisor coordinates are regular on an affine open of the integral smooth projective moduli surface containing the whole fixed locus. The claim holds in every residue characteristic, including \(2\) and \(3\).

## Proof

**1. Explicit action.** On the open locus of five distinct marks, choose the \(\operatorname{PGL}_2\)-normalization
\[
(p_1,p_2,p_3,p_4,p_5)=(1,x,y,0,\infty).
\]
Cyclically permuting the first three markings and then normalizing again gives
\[
(x,y)\longmapsto(y/x,1/x),
\]
which has order three. The standard integral presentation of \(\overline{M}_{0,5}\) as the blow-up of \(\mathbb P^1\times\mathbb P^1\) at \((0,0),(1,1),(\infty,\infty)\) identifies the exceptional divisor over \((1,1)\) with \(D_{\{1,2,3\}|\{4,5\}}\). In its affine blow-up chart, put
\[
 x=1+u,\qquad y=1+uv.
\]
The action extends as
\[
 u'=\frac{u(v-1)}{1+u},\qquad v'=\frac1{1-v}.
\]
Therefore, wherever the denominators are units, the fixed-point ideal is
\[
 I=(v^2-v+1,\;u(u+2-v)).
\]
Conversely the denominators *are* units in the proposed quotient: the first relation gives \(v(1-v)=1\), and the two relations give \((1+u)(1+vu)=1\). Multiplication by denominators thus creates no extraneous components.

**2. Exhausting all supports.** The boundary of \(\overline{M}_{0,5}\) is the union of divisors indexed by unordered two-element subsets of the five markings. The only boundary divisor stabilized by \((123)\) is \(D_{\{4,5\}}\). A stable five-pointed tree has at most three components. An order-three automorphism cannot nontrivially permute the vertices of such a tree, since a three-vertex tree is a path with automorphism group of order at most two. Hence any boundary fixed point lies on the sole invariant two-component boundary \(D_{\{4,5\}}\), and no deeper stratum is fixed. On that exceptional divisor \((u=0)\), the induced action on the exceptional coordinate is \(v\mapsto1/(1-v)\), whose fixed points satisfy \(v^2-v+1=0\); the point \(v=\infty\) is not fixed. For interior fixed points, the equations directly give \(x^3=1,\ y=x^2\), with \(x\ne1\) where distinct. In the blow-up chart they lie at \(u=v-2\) with \(v^2-v+1=0\). In characteristic three there are no geometric interior fixed points. Thus all geometric supports of the global fixed locus lie in this affine chart, so the displayed ideal gives the entire global equalizer scheme.

**3. Flat degree and tame fibers.** The relation \(v^2-v+1=0\) is monic in \(v\) and the second is monic in \(u\). Consequently the quotient is free of rank four over \(\mathbb Z\), with basis \(1,v,u,uv\). The quadratic in \(v\) has discriminant \(-3\). The two roots \(u=0\) and \(u=v-2\) are distinct away from characteristic three, since \(v=2\) and \(v^2-v+1=0\) would imply \(3=0\). Therefore all four points are reduced over every algebraically closed field of characteristic different from three.

**4. Wild special fiber.** In characteristic three, substitute \(w=v+1\). The equations become \(w^2=0\) and \(u(u-w)=0\). The maximal ideal \(\mathfrak m=(u,w)\) satisfies \(\mathfrak m^2=(uw)\ne0\), \(\mathfrak m^3=0\); the standard monomial basis is \(1,u,w,uw\). Thus its Hilbert function is \((1,2,1)\), and the tangent space of the fixed scheme has dimension two. In the ambient smooth surface, differentiating the transformation at \((u,v)=(0,-1)\) gives \(\operatorname{diag}(-2,1/4)\), which reduces to the identity in characteristic three. Nonetheless the formal expansion includes
\[
 u'-u=uw-u^2+O((u,w)^3),\qquad w'-w=-w^2+O((u,w)^3),
\]
so the action is not the identity on the completed local ring. Since a linearization with identity tangent action would be the identity, this wild action is not formally linearizable.

## Verification

The accompanying standalone `check_fixed.py` uses exact symbolic arithmetic in `sympy` to verify that the coordinate action has order three, that both blow-up transformations are correct, that the elimination identities hold exactly over the integers, that the quadratic discriminant is \(-3\), that the special-fiber equations and nilpotence conditions give length four and Hilbert function \((1,2,1)\), and that the tangent action reduces to the identity. It also checks the rational fixed-point support in characteristics \(3,5,7,11,13,17\). The general theorem is proved algebraically above; these finite-field checks are not substitutes for it. Running `python check_fixed.py` prints `M05_C3_INTEGRAL_FIXED_SCHEME_CHECKED` on success. Requires Python 3 and SymPy.

## Relationship to prior work

Boitrel's classification (arXiv:2304.05328, first public April 2023) gives degree-five del Pezzo geometric models and automorphism groups, including order-three permutation types, without supplying this integral four-point fixed scheme or the wild local intersection algebra. Dolgachev--Martin classify automorphism groups of del Pezzo surfaces in odd characteristic; the degree-five section does not compute this characteristic-three scheme-theoretic fixed locus. Bergvall--Gounelas address cohomology of marked degree-three and degree-four del Pezzo moduli and do not imply the result. Related fixed-locus cyclotomic collisions for order-five actions have different automorphism type and **curvilinear** special fibers; neither the length-four noncurvilinear algebra nor tangent-to-identity behavior follows from those computations.

## Limitations

This proves the fixed scheme for the specified standard three-cycle on the **split** degree-five del Pezzo surface, not for every arithmetic twist or every automorphism group scheme. It does not classify the characteristic-three quotient singularity. Novelty is conditional on the compared accessible literature; an older unindexed equivalent fixed-scheme computation could exist. No independent mathematical audit has been performed.

## References

- A. Boitrel, *Del Pezzo surfaces of degree 5 over perfect fields*, arXiv:2304.05328, https://arxiv.org/abs/2304.05328 (initial public posting 2023-04-11; consult the current version for the detailed classification).
- I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, *Journal of the London Mathematical Society* 109 (2024), e12905, https://doi.org/10.1112/jlms.12905.
- O. Bergvall and F. Gounelas, *Cohomology of moduli spaces of Del Pezzo surfaces*, *Mathematische Nachrichten* 296 (2023), 80--101, https://doi.org/10.1002/mana.202100311.
