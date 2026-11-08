# Sharp fifth-period window for the isosceles farthest-projection map

## Finding
Let \(h>0\). On the union of the three complete lines supporting the triangle with vertices \((-1,0)\), \((1,0)\), and \((0,h)\), apply the farthest-perpendicular-projection rule of Everett: at a point on a line, project orthogonally to each of the other two lines, take the projection at the **larger** Euclidean distance, and leave the point fixed in case of a tie. Count primitive period-five orbits up to cyclic rotation.

Put \(u=h^2\), and define
\[
\begin{aligned}
P(u)&=u^5-12u^4-10u^3-20u^2-15u-8,\\
R(u)&=u^6-22u^5-u^4-52u^3-17u^2-22u-15.
\end{aligned}
\]
Each polynomial has exactly one positive real zero; denote them by \(\alpha\) and \(\beta\), respectively. They satisfy
\[
12<\alpha<13<16<22<\beta<23,
\quad \alpha=12.9024576276\ldots,\quad \beta=22.1527603955\ldots.
\]
The **complete fifth-period census** is
\[
N_5(h)=\begin{cases}
2,&\alpha<h^2<\beta,\\
0,&\text{otherwise}.
\end{cases}
\]
In the nonempty window \(\sqrt\alpha<h<\sqrt\beta\) (approximately \(3.591999113<h<4.706671903\)), the two orbits are mirror images across the vertical symmetry axis and are both locally attracting. There are no period-five orbits at either endpoint: the formal affine cycles violate the strict farthest-projection rule there because of ties.

## Assumptions and scope
All three supporting lines are **complete**, not truncated to segments. Let \(L_0\) be the horizontal base, \(L_1\) the line through \((-1,0)\) and \((0,h)\), and \(L_2\) the line through \((1,0)\) and \((0,h)\). Let \(\pi_j\) denote orthogonal projection to \(L_j\). A nonfixed step from \(L_i\) to \(L_j\) is permissible only if its squared jump distance exceeds the squared jump distance to the remaining line. If these distances are equal, the map fixes the current point instead. A primitive period-five orbit is a set of five distinct points cyclically permuted by the map; the count identifies cyclic shifts, not mirror images.

No assertion is made about primitive periods other than five, global basins, or the map on a differently defined triangle-boundary truncation.

## Proof
**1. Finite enumeration of line words.** A nonfixed iteration is an orthogonal projection from one of the three lines onto another. A primitive five-cycle admits a cyclic word of five line labels with neighboring labels distinct, including the last and first. Up to cyclic rotation, there are precisely six words, grouped into three reflection pairs:
\[
\begin{array}{c|c}
\text{type}&\text{words}\\ \hline
\mathrm{I}&(0,1,0,1,2),\ (0,2,0,2,1)\\
\mathrm{II}&(0,1,0,2,1),\ (0,1,2,0,2)\\
\mathrm{III}&(0,1,2,1,2),\ (0,2,1,2,1).
\end{array}
\]
This enumeration includes all possible periodic points lying at a line intersection: choose the line onto which the preceding orthogonal projection landed. A cycle cannot have a stationary tie step.

For a proposed cyclic word \(w=(w_0,\ldots,w_4)\), compose the five affine orthogonal projections in the indicated order, starting and ending on \(L_{w_0}\). The composition has a unique fixed point, because its one-dimensional derivative has modulus strictly below one. Thus each word yields at most one putative cycle. At its points \(p_i\), define the five *choice gaps*
\[
G_i=\|p_i-\pi_{w_{i+1}}(p_i)\|^2-\|p_i-\pi_k(p_i)\|^2,
\]
where \(k\) is the third label and indices are taken modulo five. The word is realized by the actual map **if and only if** every \(G_i>0\).

**2. Elimination of types I and II.** For type I, the gap after its first step, at the point on \(L_1\), is
\[
G_1=-\frac{4h^2(h^8+h^6+2h^4+h^2+3)}{(h^2+1)(h^2-h+2)^2(h^2+h+2)^2}<0.
\]
The reflected case has the same obstruction. For the type-II representative \((0,1,0,2,1)\), the first gap is
\[
G_0=-\frac{4h^4(h^2-1)}{(h^2+1)(h^2-h+2)(h^2+h+2)}.
\]
Strict positivity forces \(h<1\). But its fourth gap is
\[
G_3=\frac{4h^2(h^3-2h^2+2h-2)(h^3+2h^2+2h+2)}{(h^2-h+2)^2(h^2+h+2)^2}<0
\]
when \(0<h<1\): the first cubic factor is increasing on the positive axis, since its derivative has negative discriminant and positive leading coefficient, and its value at \(h=1\) is \(-1\). The reflected word has identical gap obstructions at shifted indices. Thus neither type I nor type II can occur.

**3. Complete analysis of type III.** For the representative \((0,1,2,1,2)\) define
\[
\begin{aligned}
Z(u)&=u^3+5u^2+3u+7,\\
A(u)&=u^5+4u^4+10u^3+4u^2+5u-8,\\
B(u)&=u^5-3u^4-10u^3-22u^2-15u-15.
\end{aligned}
\]
Its unique affine fixed point on \(L_0\) is \(p_0=((u-1)^3/Z(u),0)\). Define the other four points by
\[
p_1=\pi_1(p_0),\quad p_2=\pi_2(p_1),\quad p_3=\pi_1(p_2),\quad p_4=\pi_2(p_3).
\]
The projection \(\pi_0(p_4)=p_0\) holds identically. Direct substitution into the Euclidean squared-distance formula gives, in the order of the five steps,
\[
(G_0,G_1,G_2,G_3,G_4)=
\left(
\frac{4u(u-1)^3}{(u+1)Z},\ 
\frac{4uA}{Z^2},\ 
\frac{4uB}{Z^2},\ 
\frac{4uP}{Z^2},\ 
-\frac{4uR}{(u+1)Z^2}
\right).
\]
Every denominator is strictly positive. The polynomial \(P\) has one positive real root by Descartes' rule of signs and \(P(12)<0<P(13)\); hence \(P(u)>0\) exactly when \(u>\alpha\). Similarly \(R\) has one positive root, \(R(22)<0<R(23)\), and \(R(u)<0\) exactly when \(0<u<\beta\). Since \(P(16)>0>R(16)\), \(\alpha<16<\beta\).

For \(u>\alpha>1\), one has \(A(u)>0\), as \(A(1)=16\) and \(A\) is strictly increasing for positive \(u\). Also
\[
B(u)-P(u)=(u^2-1)(9u^2+7)>0.
\]
Consequently all five gaps are positive **exactly** for \(\alpha<u<\beta\). The reflected type-III word has all the same gaps and a distinct base point \(p_0=(-(u-1)^3/Z(u),0)\). Those are therefore the only two primitive five-cycles. Their five points are distinct because the trajectory is nonfixed and a nonconstant orbit of prime period five cannot have a smaller period.

**4. Stability.** Both fifth-return maps are affine near their base points, since all five inequalities are strict. Their exact derivative along the base is
\[
\mu_5=-\frac{(u-1)^3}{(u+1)^4}.
\]
For \(u>\alpha>1\), its modulus is strictly below one. Thus both cycles are locally attracting. At \(u=\alpha\) the fourth gap vanishes; at \(u=\beta\) the fifth gap vanishes. The tie convention therefore excludes both boundary candidates. The other four words were excluded uniformly, completing all parameter and boundary cases.

## Verification
A self-contained symbolic checker is supplied as `checker.py`; execute `python checker.py` with Python 3 and SymPy. It builds all three orthogonal-projector matrices from the vertices, independently enumerates all six cyclic words, solves their affine return equations, verifies the required gap factorizations, proves the stated sign-isolation and multiplier identities symbolically, and checks 12 exact-rational triangle heights. The checker was run successfully on the packaged contents. The infinite-parameter conclusion rests on the algebraic sign proof above, **not** on finite samples. The exact root definitions, not printed decimal approximations, specify the thresholds.

## Relationship to prior work
Everett's *A Piecewise Contractive Map on Triangles* defines this farthest-perpendicular-projection map, proves qualitative convergence, and discusses period changes for isosceles triangles. The publisher records online availability on 7 January 2021; the author's freely accessible arXiv manuscript was posted on 26 August 2024. The inspected manuscript's sections 2–4 describe trapping intervals and bifurcations but do not provide the explicit primitive-period-five census or the degree-five and degree-six endpoint polynomials here.

Existing exact classifications for primitive periods three and four in this family are separate results. In particular, the right-isosceles period-four orbit and the sharp isosceles period-three/four classifications do **not** imply the fifth-period window; the relevant fifth-return line words are different. An indexed published three-cycle classification likewise does not cover fifth periods. Wang–Zhang's triangular iterated-function-system paper concerns transformations of triangle moduli, not the farthest orthogonal projection of points among three fixed supporting lines. The result claims only the precise fifth-period classification, not a new general convergence theorem.

## Limitations
The statement is restricted to Euclidean isosceles triangles with half-base normalized to one, the complete supporting-line phase space, and the rule that equidistant choices fix the point. It does not determine higher-period orbits or global basin measures. Although source comparison covered the author's full accessible manuscript, publisher metadata, relevant published records, and nearby previously recorded exact results, equivalent formulae in unindexed literature remain a residual publication-priority risk. No independent audit has been performed.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* **18** (2020 issue), 183–192; publisher reports first online publication 7 January 2021, DOI `10.1080/1726037X.2020.1847765`. Author manuscript: `https://arxiv.org/html/2408.16019` (26 August 2024).
2. Jiajun Wang and Ying Zhang, *A geometric iterated function system on triangles*, `arXiv:1605.01794` (6 May 2016), distinct triangle-moduli dynamical system.
3. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published mathematical record `2944d54e59d8` (11 October 2026), concerning primitive period three, not period five.
