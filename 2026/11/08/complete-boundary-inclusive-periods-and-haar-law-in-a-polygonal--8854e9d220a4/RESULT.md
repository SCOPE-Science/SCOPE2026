# Complete boundary-inclusive periods and Haar law in a polygonal symplectic torus map

## Finding

For the explicit two-segment toral McMillan–Hénon map below, with a specified half-open representative and force at the switching seam, the **entire least-period spectrum** is
\[
\{1,2,3,5,7,10\}.
\]
The period-one set comprises exactly three points; period two comprises exactly one orbit; period five comprises exactly one orbit; period ten consists of all but the midpoints on five specified open edges; period seven covers seven open triangular faces and seven additional open edges; and period three covers the eighth open triangular face except for its unique fixed point. For normalized Haar area \(\lambda\),
\[
\lambda\{P=3\}=\frac18,\qquad
\lambda\{P=7\}=\frac78,\qquad
\lambda\{P\notin\{3,7\}\}=0,
\quad\mathbb E_\lambda P=\frac{13}{2}.
\]
These statements specify every point of the torus, including all discontinuity and partition boundaries; they are distinct from a claim only about almost-everywhere periods.

## Assumptions and scope

Represent the two-dimensional torus \(\mathbb T^2=(\mathbb R/2\mathbb Z)^2\) by the half-open fundamental square \(S=[0,2)^2\), with arithmetic reductions \([u]_2\in[0,2)\). Define
\[
f(v)=\begin{cases}0,&0\le v<1,\\1-v,&1\le v<2,\end{cases}
\qquad F(x,y)=\bigl(y,[-x+f(y)]_2\bigr).
\]
In particular \(f(0)=f(1)=0\); the lower branch includes \(0\), and the upper branch includes \(1\). The map \(F\) is invertible, with \(F^{-1}(x,y)=([-y+f(x)]_2,x)\), and preserves normalized two-dimensional Lebesgue/Haar area because its affine matrices have determinant one and their domains fit bijectively. Least period \(P(z)\) is the minimum positive \(n\) with \(F^n(z)=z\).

A complete disjoint stratification is obtained by eight open triangular faces, twelve open edges and four vertices. Label faces by the following strict conditions (all coordinates in \((0,2)\)):

| Face | Open interior |
| --- | --- |
| \(T_0\) | \(0<y<x<1\) |
| \(T_1\) | \(0<x<1<y<2-x\) |
| \(T_2\) | \(1<x<2,\;1<y<3-x\) |
| \(T_3\) | \(1<x<2,\;0<y<2-x\) |
| \(T_4\) | \(0<x<y<1\) |
| \(T_5\) | \(0<x<1,\;2-x<y<2\) |
| \(T_6\) | \(1<x<2,\;2-x<y<1\) |
| \(T_7\) | \(1<x<2,\;3-x<y<2\) |

For \(i,j\in\{0,1\}\), define open edge parameterizations for \(0<t<1\):
\[
H_{ij}(t)=(i+t,j),\qquad V_{ij}(t)=(i,j+t),
\]
\[
D_{00}(t)=(t,t),\quad D_{01}(t)=(t,2-t),\quad
D_{10}(t)=(1+t,1-t),\quad D_{11}(t)=(1+t,2-t).
\]
The four vertices are \((0,0),(0,1),(1,0),(1,1)\). Taken together these open strata and vertices partition \(S\) without overlap. All face areas are \(1/2\), so their total area is four.

## Proof

**Face dynamics.** On \(T_0,T_3,T_4,T_6\), the affine representative is \((x,y)\mapsto(y,2-x)\). On \(T_1,T_2,T_5\), it is \((x,y)\mapsto(y,3-x-y)\); on \(T_7\), it is \((x,y)\mapsto(y,5-x-y)\). Strict inequalities of the defining triangles verify that these expressions select the correct force and modular branch at every interior point. Applying them to the three vertices of each triangle gives exact open-set image relations
\[
T_0\longrightarrow T_1\longrightarrow T_2\longrightarrow T_3
\longrightarrow T_4\longrightarrow T_5\longrightarrow T_6\longrightarrow T_0,
\qquad F(T_7)=T_7.
\]
Affine composition over the seven successive maps is the identity on \(T_0\), and the third iterate of the \(T_7\) affine formula is the identity on \(T_7\). For example, the seven successive images of \((x,y)\in T_0\) are
\[
\begin{aligned}
&(y,2-x),\\
&(2-x,1+x-y),\\
&(1+x-y,y),\\
&(y,1-x+y),\\
&(1-x+y,2-y),\\
&(2-y,x),\\
&(x,y).
\end{aligned}
\]
Consequently points in the first seven faces have *least* period seven, since the distinct faces preclude an earlier return. The single affine map on \(T_7\) is \((x,y)\mapsto(y,5-x-y)\); its third power is identity and its unique fixed point is \((5/3,5/3)\). All other \(T_7\) points have least period three.

**Edge dynamics and orientations.** Evaluate the same piecewise rule on the twelve parametric open edges. The resulting exact transitions split into the two disjoint cycles
\[
H_{00}\to V_{01}\to D_{11}\to H_{10}\to V_{00}\to H_{00}
\]
and
\[
H_{01}\to V_{11}\to D_{10}\to D_{00}\to D_{01}
\to H_{11}\to V_{10}\to H_{01}.
\]
Every arrow maps all \(t\in(0,1)\) to all of the next edge, using either \(t\) or \(1-t\). The parameter-orientation signs in the displayed order are, respectively, \((-1,+1,-1,-1,+1)\) and \((-1,+1,-1,+1,-1,-1,+1)\). Thus the first five-edge circuit changes \(t\) to \(1-t\); its unique fixed parameter \(t=1/2\) gives a single primitive five-cycle, while all other parameters have primitive period ten. The second seven-edge circuit preserves \(t\), and every point on these seven edges has primitive period seven. Since all edges in each circuit are distinct, no shorter returns are possible.

**Vertices and exhaustion.** Direct substitution yields fixed vertices \((0,0),(1,1)\) and the two-cycle \((1,0)\leftrightarrow(0,1)\). The face/edge/vertex partition is exhaustive, so the preceding list is the **global** spectrum and pointwise stratification. In particular, the isolated interior fixed point raises the number of fixed points to three.

**Area law.** The boundary strata have zero two-dimensional Haar area. Since precisely one of the eight equal-area open triangles is the period-three face and seven are period-seven faces, division by the torus area four gives probabilities \(1/8\) and \(7/8\). The mean follows from \(3/8+49/8=13/2\). The exceptional fixed point in \(T_7\) has zero area.

## Verification

The standalone program `checker.py` uses rational arithmetic to check each of the eight **entire** face-to-face affine images by vertex-and-branch inequalities, the exact seven- and three-fold affine return identities, and each of the twelve **entire** edge-to-edge affine images by symbolic one-variable endpoints and branch bounds. It independently checks the orientation products, all four vertex iterates, representative face/edge points and a \(64\times64\) rational grid. It is reproducible with `python3 checker.py` and uses only Python's standard library. The finite grid is diagnostic only, not an argument that untested points have the asserted periods; the analytical exhaustive partition supplies that proof.

## Relationship to prior work

Zolkin, Kharkov and Nagaitsev introduced the polygon-tessellating symplectic torus map and described the \(3\)- and \(7\)-cycle behavior for its two-segment example (arXiv:2311.17616, Section III). Those generic cycles are prior art. The additional conclusion here is a *complete, convention-specific* boundary and measure classification: a period-five orbit, a continuum of period-ten orbits on five open seams, vertex periods, and the exact normalized area weights. These additional statements are not claimed as consequences of the authors' generic period statement. Their earlier general methods for piecewise-affine symplectic maps (arXiv:2201.13133) are also credited. Both relevant papers were examined in accessible full-text forms; equivalent boundary calculations elsewhere cannot be excluded.

## Limitations

All boundary claims depend on the specified half-open fundamental domain and the values of the force on seams; another prescribed completion on discontinuity sets may change the zero-area period spectrum. The analysis concerns this exact map only, not a planar unwrapping or nearby force parameters. The exact quantitative area result concerns normalized Haar measure, and no claim is made about uniqueness within all possible descriptions of polygonal dynamical systems. Independent audit has not been performed.

## References

1. T. Zolkin, Y. Kharkov, and S. Nagaitsev, *Integrable symplectic maps with a polygon tessellation*, arXiv:2311.17616, first posted 2023-11-29; *Physical Review Research* **6**, 023324 (2024), DOI: 10.1103/PhysRevResearch.6.023324.
2. T. Zolkin, Y. Kharkov, and S. Nagaitsev, *Machine-assisted discovery of integrable symplectic mappings*, arXiv:2201.13133 (2022).
