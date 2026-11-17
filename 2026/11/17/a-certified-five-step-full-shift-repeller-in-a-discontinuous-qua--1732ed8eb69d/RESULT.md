# A certified five-step full-shift repeller in a discontinuous quadratic population map

## Finding
For the two-species, state-dependent quadratic stochastic operator of Abdurakhimova and Rozikov with coefficient triple \((a,b,c)=(1,0,c)\), for **every** \(c\in[0,1]\), there is a compact forward-invariant set \(S\subset(0,2/3)\) such that the scalar population map is continuous on \(S\) and
\[
h_{\mathrm{top}}(f_{1,0,c}|_S)\geq\frac{\log2}{5}>0.
\]
More precisely, a compact Cantor set \(K\subset [527/2500,7/25]\) is invariant under the fifth iterate, and \(f_{1,0,c}^{5}|_K\) is topologically conjugate to the one-sided full shift on two symbols. The construction has a strict rational covering and expanding certificate and persists for all \((a,b)\) sufficiently near \((1,0)\) **within** the admissible unit parameter square, uniformly over \(c\in[0,1]\). No assertion is made about entropy of the globally discontinuous map or positive Lebesgue measure of the repeller.

## Assumptions and scope
For \(x\in[0,1]\), let
\[
f_{a,b,c}(x)=x^2+2p_{a,b,c}(x)x(1-x),\qquad
p_{a,b,c}(x)=
\begin{cases}
a,&0\le x\le 1/3,\\
b,&1/3<x<2/3,\\
c,&2/3\le x\le1.
\end{cases}
\]
These are the first-coordinate population updates in equation (2.1)-(2.2) of the cited source. Fix \(a=1\), \(b=0\) and any \(c\in[0,1]\). On the first two regions the branches are the strictly increasing quadratics
\[
L(x)=2x-x^2\quad(0\le x\le1/3),\qquad R(x)=x^2\quad(1/3<x<2/3).
\]
Set
\[
J=[527/2500,7/25],\quad I_A=[527/2500,6/25],\quad
I_B=[1221/5000,7/25].
\]
The intervals \(I_A\) and \(I_B\) are disjoint subsets of \(J\), and \(I_A\) lies strictly to the left of \(I_B\). The words \(A=LRLLR\) and \(B=LRLRL\) specify the successive actual branches for five iterations.

## Proof
**1. Exact admissibility and covering.** Because both \(L\) and \(R\) are increasing on \([0,2/3]\), interval propagation is exactly endpoint propagation, not a floating-point enclosure. Iterating the two rational starting intervals produces the following outward-decimal displays of rational endpoint bounds (every branch condition and comparison is evaluated exactly in `CHECK.py`):

| Time | \(I_A\) image | Branch | \(I_B\) image | Branch |
|---|---|---|---|---|
| 0 | [0.210800, 0.240000] | L | [0.244200, 0.280000] | L |
| 1 | [0.377163, 0.422400] | R | [0.428766, 0.481600] | R |
| 2 | [0.142252, 0.178422] | L | [0.183840, 0.231939] | L |
| 3 | [0.264268, 0.325010] | L | [0.333883, 0.410082] | R |
| 4 | [0.458699, 0.544388] | R | [0.111478, 0.168167] | L |
| 5 | [0.210405, 0.296358] | — | [0.210529, 0.308054] | — |

In the table, all nontrivial decimal bounds are rounded outward, not treated as equalities. Exact rational comparisons give
\[
f^5(527/2500)<527/2500,\quad f^5(6/25)>7/25
\]
on \(I_A\), and
\[
f^5(1221/5000)<527/2500,\quad f^5(7/25)>7/25
\]
on \(I_B\). Every intermediate image stays strictly on its displayed branch and strictly below \(2/3\). In particular, the close branch switch at the fourth entry of \(B\) is rigorous: its lower endpoint is greater than \(1/3\). Thus the two genuine five-step restrictions \(F_A=f^5|_{I_A}\) and \(F_B=f^5|_{I_B}\) are increasing smooth maps, each satisfying \(F_i(I_i)\supset J\).

**2. Strict expansion.** On a propagated interval \([\ell,u]\), the minimum branch derivative is \(2(1-u)\) for \(L\) and \(2\ell\) for \(R\). Multiplying these exact rational lower bounds along the respective five-step words shows
\[
\inf_{I_A}(f^5)'>23/10>2,
\qquad
\inf_{I_B}(f^5)'>21/10>2.
\]
The inequalities are exact fraction comparisons in `CHECK.py`; they do not extrapolate from sampled orbits.

**3. Full-shift invariant set.** Each restriction \(F_i\) has a well-defined inverse branch \(g_i:J\to I_i\subset J\), with Lipschitz constant strictly less than \(1/2\). Since their images lie in disjoint intervals, the nested inverse construction
\[
K=\bigcap_{n\ge1}\bigcup_{\omega\in\{A,B\}^n}
(g_{\omega_1}\circ\cdots\circ g_{\omega_n})(J)
\]
is a nonempty compact Cantor set. The diameters of cylinders decay at least geometrically, so each infinite symbol sequence codes a **unique** point. Disjoint branch images make the coding injective; compactness makes it a homeomorphism. Applying \(f^5\) deletes the first symbol. Consequently \(f^5|_K\) is conjugate to the full one-sided shift, with entropy \(\log2\).

**4. An invariant continuous subsystem of the original map.** Define
\[
S=K\cup f(K)\cup f^2(K)\cup f^3(K)\cup f^4(K).
\]
The five-step invariance gives \(f(S)\subset S\). Every set in this union lies inside a finite union of the strict branch intervals from Step 1, disjoint from both discontinuity locations \(1/3\) and \(2/3\). Therefore \(f|_S\) is continuous, \(S\) is compact, and the usual entropy iterate identity applies:
\[
5h_{\mathrm{top}}(f|_S)=h_{\mathrm{top}}(f^5|_S)
\ge h_{\mathrm{top}}(f^5|_K)=\log2.
\]
It follows, in particular, that arbitrarily large primitive periods and uncountably many non-eventually-periodic bounded orbits occur in this continuous invariant subsystem.

**5. Persistence.** For coefficients \(a,b\) near \(1,0\), the polynomial branches, their iterated endpoint images and their derivatives depend continuously on \((a,b)\). All branch-separation, covering and derivative inequalities above are strict, hence survive on a sufficiently small admissible parameter neighborhood. The same construction then applies with the same two intervals and words, independently of \(c\), since none of the five-stage image intervals reaches the third region.

## Verification
Run `python CHECK.py` using the Python standard library. It propagates both rational intervals using `fractions.Fraction`, tests **every** branch inequality and disjointness, computes both five-step image bounds, and multiplies rational lower derivative bounds. A successful execution prints `TWO_DISCONTINUITY_QSO_HORSESHOE_OK exact_branches=2 period=5`. The checker supports the exact finite certificate; the infinite Cantor conjugacy and entropy bound follow from the proof above, not from finite orbit enumeration.

## Relationship to prior work
Abdurakhimova and Rozikov introduced this precise state-dependent two-species quadratic stochastic map and established fixed-point, periodic-point and absorbing/trapping-region conclusions across parameter cases. In particular, their final parameter classification gives a trapping interval in the regime with \(a>1/2\) and \(b<1/2\), but the inspected source results do not supply two full expanding five-step branches, an invariant full shift or a positive-entropy compact continuous subsystem. The construction here is **inside** that known trapping region, not a replacement for the original result. Standard inverse-branch Cantor coding and entropy iterate identities are background tools, not claimed as new. A previously established fixed-itinerary uniqueness theorem for related quadratic compositions identifies at most one periodic point per prescribed word and does not settle which words occur or prove full-shift existence. General horseshoe results for unrelated piecewise-affine maps do not imply the explicit nonlinear rational covering certificate here.

## Limitations
The theorem supplies a compact repelling subsystem; it does not prove a positive-measure chaotic attractor, typical chaotic population behavior, a globally defined entropy for the discontinuous map, a sharp minimal return length, or an exact global entropy. The derivative threshold and five-step intervals are sufficient certificates, not optimal ones. The robustness neighborhood is existential and no numerical radius is claimed. Publication-priority uncertainty remains if an equivalent same-model horseshoe exists in uninspected literature. This proof and its arithmetic checks have not been independently audited.

## References
1. Sh. B. Abdurakhimova and U. A. Rozikov, *Dynamical system of a quadratic stochastic operator with two discontinuity points*, arXiv:2103.14834v1, publicly posted 2021-03-27. https://arxiv.org/abs/2103.14834 ; full PDF https://arxiv.org/pdf/2103.14834 .
2. Sh. B. Abdurakhimova and U. A. Rozikov, *Dynamical System of a Quadratic Stochastic Operator with Two Discontinuity Points*, Mathematical Notes **111** (2022), 676–687, DOI:10.1134/S0001434622050029; original Russian edition DOI:10.4213/mzm13510. https://www.mathnet.ru/eng/mzm13510 .
