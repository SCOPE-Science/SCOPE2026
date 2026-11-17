# Global convergence and exact winner selection in a symmetric mutation–competition flow

## Finding
For all \(c>0\), \(\mu>0\), and \(x(0)\in[0,\infty)^3\setminus\{0\}\), the flow
\[
\dot x_i=x_i\left(1-x_i-c\sum_{j\ne i}x_j\right)+\mu\sum_{j\ne i}(x_j-x_i),\qquad i=1,2,3,
\]
converges to a single positive equilibrium. No nonconstant periodic orbit or non-equilibrium compact recurrent motion exists in the positive octant.

For \(0<c\le1\) all such trajectories converge to the equal-population equilibrium \(e=(1/(1+2c),1/(1+2c),1/(1+2c))\). For \(c>1\) and
\[
0<\mu<\mu_*(c):=\frac{c-1}{3(1+2c)},
\]
if one initial coordinate is strictly larger than each of the others, it selects the unique equilibrium where that same coordinate is strictly largest and the other two are equal. Explicitly the smaller value \(r\) is the unique root in \((0,r_0)\), with \(r_0=(1-3\mu)/(c+2)\), of
\[
P(r)=(c^2-1)r^2+(c-1)(2\mu-1)r+\mu(1-3\mu)=0,
\]
and the larger one is \(s=1-(c+1)r-3\mu\). The winner is chosen by the initial largest coordinate, not by its magnitude or by the ordering of the two smaller coordinates.

## Assumptions and scope
All parameters are strictly positive and all initial states are nonnegative and nonzero. The equations use unrescaled, original time. Statements about recurrent sets concern the closed nonnegative octant, excluding the equilibrium at the origin. A tied initial maximum is covered by global convergence but not by the winner-selection assertion. No basin formula is claimed outside the stated strict parameter strip.

## Proof
**1. Positive persistence and compactness.** Put \(S=x_1+x_2+x_3\), \(Q=x_1^2+x_2^2+x_3^2\). Summation cancels mutation and gives
\[
S'=S-cS^2+(c-1)Q,\qquad S^2/3\le Q\le S^2.
\]
With \(k_-:=\min\{1,(1+2c)/3\}\) and \(k_+:=\max\{1,(1+2c)/3\}\),
\[
S-k_+S^2\le S'\le S-k_-S^2.
\]
Logistic comparison gives a uniform eventual positive lower bound and finite upper bound on \(S\). Whenever \(x_i=0\) but \(S>0\), its derivative equals \(\mu S>0\), so every coordinate becomes strictly positive immediately. For large time, with \(M\) an upper bound for \(S\) and \(m>0\) a lower bound, \(x_i'\ge\mu m-[\max\{1,c\}M+3\mu]x_i\). Comparison supplies an eventual positive coordinate-wise lower bound. Thus each positive omega limit is a compact subset of the interior and every solution exists for all forward time.

**2. Persistent order and a monotone shape ratio.** For all distinct indices \(i,j,k\), subtraction yields the exact identity
\[
(x_i-x_j)'=(x_i-x_j)[1-x_i-x_j-cx_k-3\mu].
\]
Every strict ordering and equality between coordinates is preserved. When the three coordinates are strictly ordered, write them \(a>b>d\), and set \(R=(a-b)/(b-d)\). Direct subtraction of the two logarithmic gap equations gives
\[
\frac{d}{dt}\log R=(c-1)(a-d).
\]
For \(c\ne1\), either the monotone \(R\) tends to a positive finite limit, or tends to the appropriate endpoint (\(\infty\) when \(c>1\), \(0\) when \(c<1\)). In the finite-limit case, \(\int_0^\infty(a-d)dt<\infty\). Since the vector field and its derivative are bounded on the compact positively invariant tail, \(a-d\) is uniformly continuous, hence tends to zero. The equation for \(S\) then differs by \(o(1)\) from \(S'=S-(1+2c)S^2/3\), forcing \(S\to3/(1+2c)\) and \(x\to e\). For the endpoint case, boundedness forces \(b-d\to0\) when \(c>1\) and \(a-b\to0\) when \(c<1\). Thus the omega limit is wholly contained in one invariant coordinate-equality plane. If any pair began equal, that plane was invariant from the start.

At \(c=1\), \(S'=S-S^2\) and all differences satisfy \((x_i-x_j)'=(1-S-3\mu)(x_i-x_j)\). Therefore \(S\to1\), the differences tend to zero and \(x\to e\).

**3. Convergence on every equality plane, including omega limits arriving from outside.** Relabel so that \(x_1=x_2=r>0\), \(x_3=s>0\). The induced plane system is
\[
\dot r=r[1-(1+c)r-cs]+\mu(s-r),\qquad
\dot s=s(1-s-2cr)+2\mu(r-s).
\]
For the Dulac factor \(B(r,s)=1/(rs)\), an exact differentiation gives
\[
\partial_r(B\dot r)+\partial_s(B\dot s)
=-\frac{1+c}{s}-\frac1r-\frac\mu{r^2}-\frac{2\mu}{s^2}<0.
\]
The Bendixson–Dulac/Green argument excludes all interior periodic orbits and all closed separatrix polygons. The equilibrium set in this plane is finite: at any positive equilibrium all three coordinates solve the same quadratic
\[
(c-1)t^2+(1-cS-3\mu)t+\mu S=0.
\]
For \(c\ne1\), at most two distinct positive values occur, and when \(s\ne r\) the gap equation implies \(s=1-(c+1)r-3\mu\). Substitution into either equilibrium equation reduces exactly to \(P(r)=0\), a nonzero quadratic. When \(c=1\), the common equation has only one positive root. Hence there are finitely many positive equilibria on any equality plane.

For clarity about the three-dimensional-to-planar reduction: the omega limit of any precompact forward trajectory is compact, connected, invariant and internally chain transitive. Once this set lies in a coordinate-equality plane, it is an internally chain-transitive set for the restricted planar flow. The standard planar Poincaré–Bendixson classification, together with finiteness of equilibria and absence of periodic or polycyclic recurrent circuits, forces this set to consist of one equilibrium. Therefore even trajectories approaching the plane from outside converge to a single equilibrium.

**4. Universal equalization when \(c<1\).** For \(0<c<1\), the common quadratic in step 3 has negative leading coefficient and positive constant term, so it has exactly one positive root. Every positive equilibrium must have three equal coordinates, namely \(e\). With step 3 this proves the global claim for \(c\le1\).

**5. Exact basin selection when \(c>1\) and \(0<\mu<\mu_*(c)\).** The equal-population equilibrium has transverse eigenvalue \(\lambda=(c-1)/(1+2c)-3\mu>0\). A trajectory with unequal coordinates cannot tend to \(e\): the difference identity would then give eventually strictly positive logarithmic growth rate for a nonzero difference, contradicting convergence to zero. For an initially unique maximum, the ordering identity and the monotone ratio in step 2 imply that any omega limit away from \(e\) has the two smaller coordinates equal; the same holds immediately if these two initially tie. Thus the limit has the form \((s,r,r)\) up to permutation, with \(s>r>0\), and \(s=1-(c+1)r-3\mu\), so \(0<r<r_0\). Since \(\mu<\mu_*<1/6\),
\[
P(0)=\mu(1-3\mu)>0,
\qquad
P(r_0)=\frac{(1-3\mu)[3(2c+1)\mu-(c-1)]}{(c+2)^2}<0.
\]
The upward quadratic \(P\) therefore has exactly one root in \((0,r_0)\). This proves existence, uniqueness and the initial-maximum basin selection, with no unproved numerical extrapolation.

## Verification
The accompanying `CHECK.py` is a self-contained Python standard-library rational-arithmetic test of the sum and gap identities, the strict Dulac sign, the reduced equilibrium polynomial, and the strict subcritical endpoint signs over a finite grid of rational parameters and points. Run `python CHECK.py`; the expected output is `MUTATION_SYMMETRY_EXACT_FRACTION_CHECKS_OK`. The proof above, rather than this finite diagnostic, establishes the global and parameter-uniform conclusions. The critical convergence step uses the classical planar chain-transitivity/Poincaré–Bendixson lemma and is not an exhaustive computer certificate.

## Relationship to prior work
Jaramillo, Mrad and Stepien introduced this exact all-to-all mutation model (equation (6)), analyzed the equal-competition degenerate case using cylindrical coordinates, derived formulas for additional equilibria (their equation (33)), and presented numerical convergence observations. The new result is an all-rate global-convergence theorem and an exact initial-largest-species basin criterion; the source's equilibrium formulas, its observed dynamics and its stability diagrams are not claimed as discoveries here.

Coville and Fabre establish global attraction under type-independent competition, which does not encompass the bistable \(c>1\) regime: here the per-type competition explicitly depends on \(x_i\), and the low-mutation family has multiple positive equilibria. Prior unmutated May–Leonard integrability results also do not imply the strictly positive mutation conclusion. A broader unpublished Lyapunov result could still overlap; publication priority requires independent review.

## Limitations
No exact basin classification is proved for a tied maximum, and outside the strict winner regime only convergence, not the number or basin of every equilibrium, is asserted. The proof does not give rates, nor does it extend to \(\alpha\ne\beta\), asymmetric mutations, or negative initial populations. No independent audit has been conducted.

## References
1. G. Jaramillo, L. Mrad, T. L. Stepien, *Dynamics of a linearly-perturbed May–Leonard competition model*, arXiv:2210.04342 (initial public version 2022-10-09), full open preprint https://arxiv.org/html/2210.04342v2; original equations (6), sections IV.4–IV.6, equation (33).
2. J. Coville and F. Fabre, *Convergence to the Equilibrium in a Lotka–Volterra Ode Competition System with Mutations*, arXiv:1301.6237, 2013, https://arxiv.org/abs/1301.6237.
3. Classical Bendixson–Dulac criterion and planar Poincaré–Bendixson theory; the last convergence argument uses standard internal chain transitivity of omega limits.
