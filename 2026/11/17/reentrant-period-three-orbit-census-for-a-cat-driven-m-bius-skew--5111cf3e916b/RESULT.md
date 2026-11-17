# Reentrant period-three orbit census for a cat-driven Möbius skew map

## Finding

Consider the three-torus map of Chigarev, Kazakov and Pikovsky, on the symmetric slice \(c=\alpha=0\),
\[
(t,s,x)\longmapsto \left(2t+s,\ t+s,\ x+\mu\sin(2\pi t)-\frac1\pi\arctan\frac{\varepsilon\sin(2\pi x)}{1+\varepsilon\cos(2\pi x)}\right)\pmod1,
\]
for \(0<\varepsilon<1\) and \(0\le\mu\le\tfrac12\). Let \(d=1-\varepsilon^2\), and define
\[
q_{\pm}=\frac{\pm d^{3/2}-2\varepsilon^2}{1+\varepsilon^2},\qquad
\mu_{\pm}=\frac{1}{2\pi}\arccos q_{\pm}.
\]
Then \(0<\mu_+<\mu_-<1/2\). Let \(N_3(\mu;\varepsilon)\) be the **number of distinct primitive period-three orbits** of the full three-torus map, with cyclic time shifts counted once. The following complete, exact census holds:
\[
N_3(\mu;\varepsilon)=
\begin{cases}
10,&0\le\mu<\mu_+\text{ or }\mu_-<\mu\le\frac12,\\
8,&\mu=\mu_+\text{ or }\mu=\mu_-,\\
6,&\mu_+<\mu<\mu_-.
\end{cases}
\]
Equivalently, the number of **points of least period three** is three times this value. All isolated primitive period-three points are fiber-hyperbolic away from the two thresholds; at either threshold precisely two primitive period-three orbits are fiber-parabolic and the other six remain fiber-hyperbolic. In particular, increasing \(\mu\) first destroys four primitive period-three orbits across an open elliptic interval, then restores them: this is an exact reentrant finite-period phenomenon.

## Assumptions and scope

The coordinates are in \(\mathbb T^3=(\mathbb R/\mathbb Z)^3\). The parameter \(\varepsilon\) is real and strictly between zero and one. The parameters \(c=\alpha=0\) and \(0\le\mu\le1/2\) are essential to this statement. "Period three" always means **least** period three for the entire map. The fiber classification refers to the derivative in the circle coordinate and does not replace the base Anosov multipliers. There is no assertion about other least periods or the generic invariant measures.

## Proof

**1. Exhaustive base orbit list.** Write \(A=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)\). Direct multiplication gives
\[
A^3=\begin{pmatrix}13&8\\8&5\end{pmatrix},\qquad
\det(A^3-I)=-16,\qquad \det(A-I)=-1.
\]
Thus exactly sixteen base points are fixed by the third iterate: one fixed point and fifteen points forming five primitive three-cycles. For example, the complete five orbits, written with coordinates in \([0,1)^2\), are
\[
\begin{aligned}
&(0,\tfrac14)\to(\tfrac14,\tfrac14)\to(\tfrac34,\tfrac12),\\
&(0,\tfrac34)\to(\tfrac34,\tfrac34)\to(\tfrac14,\tfrac12),\\
&(0,\tfrac12)\to(\tfrac12,\tfrac12)\to(\tfrac12,0),\\
&(\tfrac14,0)\to(\tfrac12,\tfrac14)\to(\tfrac14,\tfrac34),\\
&(\tfrac12,\tfrac34)\to(\tfrac34,\tfrac14)\to(\tfrac34,0).
\end{aligned}
\]
The successive values of \(\sin(2\pi t)\) are, up to cyclic permutation, respectively \((0,1,-1)\), \((0,-1,1)\), \((0,0,0)\), \((1,0,1)\), and \((-1,0,-1)\). All five are distinct, and fifteen points exhaust the determinant count.

**2. Möbius return and exact traces.** With \(z=e^{2\pi i x}\), the one-step fiber map driven by forcing shift \(\delta\) is \(R_{\delta}\circ H_{\varepsilon}\), where
\[
H_{\varepsilon}(z)=\frac{z+\varepsilon}{1+\varepsilon z},\qquad R_{\delta}(z)=e^{2\pi i\delta}z.
\]
An associated determinant-one matrix is
\[
M_{\delta}=\frac1{\sqrt d}\begin{pmatrix}
e^{i\pi\delta}&\varepsilon e^{i\pi\delta}\\
\varepsilon e^{-i\pi\delta}&e^{-i\pi\delta}
\end{pmatrix}.
\]
Multiply the three matrices in chronological order, rightmost first, on each of the five base cycles. The three possible real traces are exactly
\[
\begin{aligned}
\tau_0&=\frac{2(1+3\varepsilon^2)}{d^{3/2}} &&\text{(one zero-forcing cycle)},\\
\tau_{\rm opp}&=\frac{2(1+\varepsilon^2+2\varepsilon^2\cos(2\pi\mu))}{d^{3/2}} &&\text{(two opposite-sign cycles)},\\
\tau_{\rm same}&=\frac{2((1+\varepsilon^2)\cos(2\pi\mu)+2\varepsilon^2)}{d^{3/2}} &&\text{(two same-sign cycles)}.
\end{aligned}
\]
These can also be checked by exact expansion of the Laurent polynomials in \(\varepsilon\) and \(e^{i\pi\mu}\), without numerical matrix evaluation.

**3. Classification and sharp transitions.** Since \(0<d<1\), \(\tau_0>2\) and \(\tau_{\rm opp}\ge2/\sqrt d>2\). Thus each of those three base cycles carries precisely two fiber fixed points after three steps. For the remaining two base cycles, \(\tau_{\rm same}\) strictly decreases with \(\mu\in(0,1/2)\). Its endpoint values are \(\tau_{\rm same}(0)=\tau_0>2\) and \(\tau_{\rm same}(1/2)=-2/\sqrt d<-2\). Therefore there are exactly two interior threshold crossings \(\tau_{\rm same}=+2\) and \(\tau_{\rm same}=-2\), given by the stated \(\mu_+\) and \(\mu_-\). The inequalities \(-1<q_-<q_+<1\) follow from \(0<d<1\) and \(d^{3/2}<d\).

For a determinant-one circle Möbius map, \(|\tau|>2\) gives two distinct fiber fixed points, \(|\tau|<2\) gives none, and \(|\tau|=2\) gives one unless its projective action is the identity. The same-sign monodromy is **not** the identity at either threshold. Indeed, for the forcing itinerary \((\mu,0,\mu)\), its unnormalized upper-right matrix entry equals
\[
\varepsilon\bigl((1+\varepsilon^2)e^{2\pi i\mu}+2\bigr).
\]
This is nonzero for every real \(\mu\), because \(1+\varepsilon^2<2\). The negative-sign cycle has the conjugate nonzero entry. Consequently each threshold cycle has exactly one (genuinely parabolic) fiber fixed point, not an identity circle of them.

**4. No extra least-period-three points.** The only base fixed point is \((0,0)\); over it the fiber map is \(H_{\varepsilon}\), which has precisely two hyperbolic fixed points and no other points fixed by its third iterate. It contributes no primitive three-cycle. Each of the five primitive base cycles contributes either two, one, or zero primitive three-cycles depending on the above trace class. Adding the three permanently hyperbolic base contributions and the two variable contributions gives \(6+4=10\), \(6+2=8\), or \(6\) respectively. Hyperbolic and parabolic statements follow from the same classification. This exhausts all period-three orbits because every such orbit projects to an \(A^3\)-fixed base point.

## Verification

The standalone standard-library Python script `verify.py` exhaustively lists the sixteen rational base points fixed by the third iterate and checks the five cyclic forcing itineraries. It multiplies all three Möbius matrices **as exact two-variable integer Laurent polynomials**, verifying all three trace formulas and the nonzero parabolic upper-right entry. It additionally checks sample parameter inequalities and threshold ordering numerically only as diagnostics. Executing `python3 verify.py` produces `CAT_DRIVEN_PERIOD_THREE_EXACT_CENSUS_OK`. The script is a finite consistency checker; the proof above supplies the all-parameter assertion.

## Relationship to prior work

Chigarev, Kazakov and Pikovsky (2023), specifically their equation (1), Sections II and IV, and Appendix A, introduced this Anosov-driven Möbius skew diffeomorphism, described the Möbius composition principle and investigated periodic-driver bifurcations numerically, including plots involving periods up to seven. These general principles are not new. The inspected original text does **not** state the symmetric slice's complete primitive-period-three count, both exact transition thresholds, a reentrant open elliptic interval, or the genuine-parabolic endpoint count. The 2021 related article by the same authors addresses statistical singularities in other Anosov–Möbius settings and does not establish this census.

The publicly available finding *Arithmetic isolation of identity resonances in a cat-driven Möbius map* (2026) studies the same \(c=\alpha=0\) slice but explicitly only **least period two**. In that case isolated forcing resonances replace two fixed points by an identity circle, whereas the present period-three transition has a **nonidentity parabolic** boundary and an open parameter interval without any fiber fixed points over two base cycles. Neither period-two identity resonance nor general group classification implies the specific five-itinerary census or thresholds without additional computation. An earlier unpublished equivalent calculation remains possible.

## Limitations

The claim is restricted to the symmetric \(c=\alpha=0\) slice and the parameter interval \(0\le\mu\le1/2\), with fixed \(0<\varepsilon<1\). It makes no generic bifurcation assertion under perturbing \(c\) or \(\alpha\). It counts primitive period-three orbits, not other periodic or chaotic invariant objects. The novelty comparison is best-knowledge, not proof of priority; unindexed equivalent calculations could exist. No independent mathematical audit has been carried out.

## References

1. V. Chigarev, A. Kazakov and A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1, first public 2023-05-29; *Chaos* 33, 063113 (2023), DOI: 10.1063/5.0144672. Original HTML text: https://ar5iv.labs.arxiv.org/html/2305.18172 .
2. V. Chigarev, A. Kazakov and A. Pikovsky, *Mutual singularities of overlapping attractor and repeller*, *Chaos* 31, 083127 (2021), DOI: 10.1063/5.0056891.
3. *Arithmetic isolation of identity resonances in a cat-driven Möbius map*, published result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-arithmetic-isolation-of-identity-resonances-in-a-cat-driven-m-bi--a1ced3096486 .
4. Mathematics Subject Classification 2020, class 37C25, American Mathematical Society.
