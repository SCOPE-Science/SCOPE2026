# Sharp positive two-cycle obstruction in a coupled-logistic predator–prey map

## Finding
Consider the coupled-logistic recurrence
\[
F(x,y)=\bigl(ax(1-x)-cxy,\;by(1-y)+dxy\bigr),
\qquad a,b,c,d>0.
\]
If \(a\le3\) and \(b+d\le3\), then **every strictly positive solution of \(F^2(x,y)=(x,y)\) is a fixed point of \(F\)**. Equivalently, this entire parameter region has no strictly positive orbit of least period two, whether or not the entire positive quadrant is forward invariant.

Both coordinate thresholds are sharp in the following uniform sense. For every sufficiently small \(\delta>0\), arbitrarily small strictly positive couplings \(c=d=t\) produce a hyperbolically attracting, strictly positive primitive two-cycle when either
\[
(a,b)=(3+\delta,2),\qquad b+d<3,
\]
or
\[
(a,b)=(2,3+\delta),\qquad a<3.
\]
In both cases the cycle lies strictly inside \((0,1)^2\). Thus neither numerical threshold \(3\) can be raised while retaining the other bound and retaining a universal exclusion theorem.

## Assumptions and scope
The state space is the strictly positive quadrant, not necessarily a globally invariant compact rectangle. Parameters \(a,b,c,d\) are arbitrary positive real numbers; the exclusion requires both \(a\le3\) and \(b+d\le3\). A positive primitive two-cycle means two distinct states \((x_0,y_0),(x_1,y_1)\), each with positive coordinates, satisfying \(F(x_0,y_0)=(x_1,y_1)\) and \(F(x_1,y_1)=(x_0,y_0)\). Fixed points are not excluded. No assertion is made about periods three or higher, global convergence, or orbits that leave the positive quadrant.

## Proof
Suppose a positive two-step orbit exists. Positivity of its first component implies
\[
0<x_i<1,\qquad i=0,1.
\]
Put
\[
S_x=x_0+x_1,\quad S_y=y_0+y_1,\qquad
R_x=x_0^{-1}+x_1^{-1},\quad R_y=y_0^{-1}+y_1^{-1}.
\]
Dividing the two prey recurrence equations by their positive initial prey coordinates and adding yields the exact identity
\[
\frac{x_1}{x_0}+\frac{x_0}{x_1}
=2a-aS_x-cS_y.
\]
The left-hand side is at least \(2\), while \(cS_y>0\). Therefore \(a>1\) and
\[
0<S_x<\frac{2(a-1)}a.
\]
Arithmetic–harmonic mean gives \(R_x\ge4/S_x\), hence for \(a\le3\),
\[
R_x>\frac{2a}{a-1}\ge a.
\tag{1}
\]

Likewise, dividing and adding the predator equations gives
\[
\frac{y_1}{y_0}+\frac{y_0}{y_1}=2b-bS_y+dS_x.
\]
Since \(S_x<2\), positivity requires \(b+d>1\) and
\[
0<S_y<\frac{2(b+d-1)}b.
\]
Therefore, whenever \(b+d\le3\),
\[
R_y\ge\frac4{S_y}>
\frac{2b}{b+d-1}\ge b.
\tag{2}
\]
Subtracting instead of adding the normalized prey and predator equations, and writing \(\Delta_x=x_1-x_0\), \(\Delta_y=y_1-y_0\), gives exactly
\[
(R_x-a)\Delta_x=c\Delta_y,
\qquad (R_y-b)\Delta_y=-d\Delta_x.
\tag{3}
\]
The determinant of this homogeneous two-by-two system is
\[
(R_x-a)(R_y-b)+cd>0
\]
by (1), (2), and \(c,d>0\). Thus \(\Delta_x=\Delta_y=0\), proving exclusion of primitive positive two-cycles, including both weak parameter boundaries.

For sharpness, consider the scalar logistic map \(f_r(u)=ru(1-u)\). For each \(3<r<1+\sqrt6\), it has a strictly positive primitive two-cycle
\[
u_\pm(r)=\frac{r+1\pm\sqrt{(r-3)(r+1)}}{2r},
\qquad 0<u_-(r)<u_+(r)<1,
\]
with two-step multiplier
\[
\lambda_r=f_r'(u_-(r))f_r'(u_+(r))=4+2r-r^2\in(-1,1).
\]
At the decoupled endpoint \(c=d=0\), for \((a,b)=(r,2)\) the coupled map has the primitive two-cycle \((u_-(r),1/2)\leftrightarrow(u_+(r),1/2)\). The two eigenvalues of the derivative of its second iterate are \(\lambda_r\) and \(0\), neither equal to \(1\). The implicit-function theorem applied to \(F^2-\mathrm{id}\) therefore continues this distinct cycle to all sufficiently small \(c=d=t>0\). Continuity preserves coordinates in \((0,1)\) and both Floquet multipliers inside the unit disk. Here \(b+d=2+t<3\).

Similarly, when \((a,b)=(2,r)\), the decoupled cycle \((1/2,u_-(r))\leftrightarrow(1/2,u_+(r))\) has second-iterate eigenvalues \(0\) and \(\lambda_r\), so it continues to a positive attracting two-cycle for small \(c=d=t>0\). Here \(a=2<3\) and \(b+d=r+t>3\). Taking \(r=3+\delta\) and then \(t\downarrow0\) establishes sharpness arbitrarily close to either boundary. \(\square\)

## Verification
A standalone Python checker in `checker.py` verifies with exact symbolic algebra the four normalized add/subtract identities used in the proof, the exact logistic two-cycle formulas, and the multiplier \(\lambda_{16/5}=4/25\). At \(a=16/5,b=2,c=d=10^{-4}\) and at \(a=2,b=16/5,c=d=10^{-4}\), it independently solves the coupled two-cycle equations to high precision and checks positive distinct orbit coordinates and strictly attracting two-step multipliers. These numerical examples illustrate the implicit-function construction; they are not substitutes for its proof.

Reproduce using `python checker.py` with Python, SymPy and mpmath installed. The determinant argument applies to all real positive parameters in the stated rectangle; it does not rely on a finite parameter enumeration.

## Relationship to prior work
The coupled-logistic predator–prey map has been investigated since the numerical work of Satoh and Aihara (1990), whose published coordinates exchange the prey and predator names. The accessible full text of Al-Kaff et al. (2024), particularly its model equation, local stability analysis, Theorem 11 on a **local** flip bifurcation, and numerical bifurcation sections, addresses a different question: whether local bifurcations arise around equilibria. These results do not imply the present all-positive-state two-cycle exclusion or its uniform sharpness. The related 2018 analysis by Elsadany, Yousef and Elsonbaty emphasizes local bifurcations; its full text was not available for comparison. Local stability of a fixed point alone cannot rule out a disconnected primitive two-cycle elsewhere, so a global amplitude argument is needed here.

A published exclusion theorem for a separate linear-response plankton map does not cover this coupled-logistic map: its predator update is linear in predator density, whereas the present predator has the strictly quadratic self-limiting term \(-by^2\). Likewise, planar Ricker competition cycle-census results concern exponential, mutually competitive maps rather than a quadratic predator–prey pair of opposite interaction signs.

## Limitations
The conclusion is only a period-two nonexistence result; it neither establishes global attraction nor excludes higher-period, quasiperiodic or chaotic motions. The parameter condition is a sharp **coordinatewise universal sufficient region**, not a necessary-and-sufficient criterion for every fixed quadruple of parameters. The sharpness examples use small couplings, though they remain strictly positive. Previous work on coupled logistic maps extends back to 1990; equivalently formulated results in inaccessible or unindexed manuscripts cannot be ruled out from search alone. No independent mathematical audit has been performed.

## References
1. Al-Kaff, M. O., El-Metwally, H. A., Elsadany, A.-E. A., and Elabbasy, E. M., “Exploring chaos and bifurcation in a discrete prey–predator based on coupled logistic map,” *Scientific Reports* **14**, 16118 (first public online 2024-07-12), https://doi.org/10.1038/s41598-024-62439-8 ; complete lawful open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11245555/ .
2. Satoh, K. and Aihara, T., “Numerical Study on a Coupled-Logistic Map as a Simple Model for a Predator-Prey System,” *Journal of the Physical Society of Japan* **59**, 1184–1198 (1990), https://doi.org/10.1143/JPSJ.59.1184 .
3. Elsadany, A. A., Yousef, A. M., and Elsonbaty, A., “Further analytical bifurcation analysis and applications of coupled logistic maps,” *Applied Mathematics and Computation* **338**, 314–336 (2018), https://doi.org/10.1016/j.amc.2018.06.008 .
4. Yao, X.-Y., Li, X.-F., Jiang, J., and Leung, A. Y. T., “Codimension-one and -two bifurcation analysis of a two-dimensional coupled logistic map,” *Chaos, Solitons & Fractals* **164**, 112651 (2022), https://doi.org/10.1016/j.chaos.2022.112651 .
