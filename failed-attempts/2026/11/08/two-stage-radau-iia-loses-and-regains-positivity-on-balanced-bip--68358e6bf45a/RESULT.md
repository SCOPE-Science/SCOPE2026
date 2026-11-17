# Two-stage Radau IIA loses and regains positivity on balanced bipartite graphs

## Finding

Consider one step of the two-stage, third-order Radau IIA method for the continuous-time heat system \(u'=-Lu\) on the unweighted, connected complete bipartite graph \(K_{m,m}\). Its one-step matrix can be positive for both *small and sufficiently large* steps, but negative at an intermediate range.

For an integer \(m\ge 2\), define
\[
R(z)=\frac{1-z/3}{1+2z/3+z^2/6},\qquad
T_h=R(hL),\qquad x=mh,
\]
\[
P_m(x)=4x^4+(36-16m)x^3+(16m+36)x^2+72mx+72m.
\]
Every off-diagonal entry of \(T_h\) is strictly positive for \(h>0\), and the diagonal entries share the sign of \(P_m(x)\). Consequently:

- For \(2\le m\le5\), \(T_h\ge0\) entrywise for **all** \(h\ge0\).
- For \(m\ge6\), there are precisely two distinct roots \(3<\alpha_m<8<\beta_m\) of \(P_m\), and
\[
T_h\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad
0\le h\le\frac{\alpha_m}{m}\quad\text{or}\quad h\ge\frac{\beta_m}{m}.
\]
Every diagonal entry is strictly negative between these two intervals. At \(m=6\), \(\alpha_6=6\) and the other root is the unique positive root of \(x^3-9x^2-21x-18\), approximately \(11.0482227599\); the corresponding forbidden step band on \(K_{6,6}\) is \(1<h<1.84137046\ldots\).

In particular, the smallest balanced complete bipartite graph exhibiting this loss-and-recovery behavior is \(K_{6,6}\), with twelve vertices. The numerical map always preserves total mass; outside the forbidden band it also preserves coordinatewise nonnegativity of every initial vector.

## Assumptions and scope

The graph is simple, unweighted, and complete bipartite with equal part sizes \(m\ge2\). The Laplacian is the *combinatorial* Laplacian \(L=D-A\), not the normalized Laplacian. The time step is real and nonnegative. Matrix inequalities are entrywise. The result concerns the **end-of-step transition matrix** for the linear autonomous ODE, not the internal Radau stages, nonlinear problems, or all graphs. The stability function arises from the standard two-stage Radau IIA Butcher coefficients
\[
\mathsf A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad
b=\begin{pmatrix}3/4\\1/4\end{pmatrix}.
\]
Indeed \(1+zb^\top(I-z\mathsf A)^{-1}\mathbf1=(1+z/3)/(1-2z/3+z^2/6)\), which yields \(R\) upon substituting \(z=-hL\). For \(h\ge0\), the denominator is positive at each nonnegative Laplacian eigenvalue, so the matrix function is well-defined.

## Proof

**Spectral projectors.** Order the two parts consecutively. The Laplacian of \(K_{m,m}\) has eigenvalues \(0\), \(m\), and \(2m\) with respective orthogonal projectors
\[
\Pi_0=\frac1{2m}\begin{pmatrix}J&J\\J&J\end{pmatrix},\qquad
\Pi_m=\begin{pmatrix}I-J/m&0\\0&I-J/m\end{pmatrix},\qquad
\Pi_{2m}=\frac1{2m}\begin{pmatrix}J&-J\\-J&J\end{pmatrix},
\]
where \(I\) and \(J\) are the \(m\)-square identity and all-ones matrices. Thus
\[
T_h=\Pi_0+R(x)\Pi_m+R(2x)\Pi_{2m}.
\]
It is symmetric and has row sums \(R(0)=1\).

**All entry types.** With \(D(z)=z^2+4z+6>0\), we have \(R(z)=(6-2z)/D(z)\). A diagonal entry equals
\[
d_m(x)=\frac{1+R(2x)+(2m-2)R(x)}{2m}
=\frac{P_m(x)}{2mD(x)D(2x)}.
\]
Two distinct vertices in the same part have transition entry
\[
s_m(x)=\frac{1-2R(x)+R(2x)}{2m}
=\frac{4x^2(x^2+9x+9)}{2mD(x)D(2x)}>0
\quad(x>0).
\]
Vertices in opposite parts have entry \(c_m(x)=[1-R(2x)]/(2m)>0\) for \(x>0\), since \(D(z)-(6-2z)=z^2+6z>0\) for positive \(z\). Hence only the diagonal can obstruct nonnegativity.

**The small-side regime.** When \(0\le x\le3\), \(R(x)\ge0\), while \(1+R(2x)>0\) because \(D(z)+(6-2z)=z^2+2z+12>0\). Hence \(d_m(x)>0\) for every \(m\). For \(x>3\), \(R(x)<0\), and \(d_m(x)\) strictly decreases as \(m\) increases, because \(d_m(x)=R(x)+(1+R(2x)-2R(x))/(2m)\) and the bracket is positive; alternatively the numerator \(1+R(2x)+(2m-2)R(x)\) decreases in \(m\). The numerator at \(m=5\) is strictly positive: the exact identity
\[
\frac{P_5(x)}4=(x^2-6x-4)^2+x^3+x^2+42x+74>0
\qquad(x\ge0)
\]
proves all \(2\le m\le5\) safe (using the numerator comparison at \(x>3\)).

**Exactly one forbidden band for all larger sides.** For \(m\ge6\), \(P_m(0)=72m>0\), its leading term is \(4x^4\), and
\[
P_m(8)=P_6(8)-6520(m-6)=-2000-6520(m-6)<0.
\]
Thus there is a positive root on either side of \(8\). The signs of the coefficients in descending degree are \(+,-,+,+,+\) for \(m\ge6\). Descartes' rule allows at most two positive roots counting multiplicity; therefore these are the **only** positive roots, both simple, with negative sign strictly between. The argument for \(x\le3\) above places the smaller root beyond \(3\). At \(m=6\), the factorization is
\[
P_6(x)=4(x-6)(x^3-9x^2-21x-18),
\]
and the cubic has exactly one positive real root by its one sign change. This proves the exact nonnegativity set and sharp boundaries.

## Verification

The accompanying `verify.py` uses only Python's standard-library exact fractions. It constructs \(L\) independently and checks that the entrywise spectral formula satisfies the full matrix identity
\[
(I+2hL/3+h^2L^2/6)T_h=I-hL/3
\]
for 77 rational instances across seven sizes, checks mass conservation and symmetry, tests 9,680 individual entries against their formula/sign statements, and checks polynomial witnesses and the sum-of-squares identity. Running `python verify.py` produces `PASS: 77 exact-rational matrix cases; 9680 checked entries; polynomial and sign witnesses verified`.

These finite checks support reproduction only. The proof for **all** \(m\ge2\) and \(h\ge0\) is the symbolic projector, sign, sum-of-squares, and Descartes argument above.

## Relationship to prior work

Two-stage Radau IIA is a classical L-stable implicit Runge--Kutta method, not introduced here. The 1999 Radau survey by Hairer and Wanner describes its stiff-equation role. Horváth (2005) studies general Runge--Kutta positivity step thresholds; Horváth, Song and Terlaky (arXiv v1, 26 June 2014), especially Section 3.2 and Theorem 3.12, give a general sufficient rational-discretization invariance threshold based on absolute monotonicity. Their framework does not, in the inspected text, give this balanced-biclique quartic, the integer side-size cutoff \(m=6\), or the disconnected exact safe-step set. Generic first-threshold bounds need not determine later recovery. The new statement is this exact family-specific classification, not Radau stability, graph spectra, or the general positivity framework.

The directly related published research records checked included the separate \([2/2]\) Padé Markov-positivity barrier, the Crank--Nicolson resolvent-return law, and a backward-Euler-filtered Crank--Nicolson lattice result. Those concern different rational methods or graph classes and do not logically imply the present \([1/2]\) Radau IIA two-window theorem. The accessible previous records on graph diffusion involving \([0/2]\) Padé, Crank--Nicolson and explicit RK4 likewise do not supply this stability function and bipartite classification.

## Limitations

The conclusion is restricted to balanced complete bipartite combinatorial graph Laplacians. It does not assert an identical classification for unbalanced bipartite graphs, arbitrary weighted graphs, stagewise positivity, or nonlinear systems. The exact threshold formulas require solving a quartic; no radical simplification for general \(m\) is claimed. The literature comparison is not a proof of global publication priority: the full 2005 Horváth article was not available for inspection, although its abstract and the full 2014 successor were examined, and specialized unindexed results may exist. No independent mathematical review has been carried out.

## References

- Z. Horváth, Y. Song, T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755v1, publicly dated 2014-06-26, https://arxiv.org/abs/1406.6755 ; Discrete Contin. Dyn. Syst. 35 (2015), 2997--3013, https://doi.org/10.3934/dcds.2015.35.2997 . Section 3.2 and Theorem 3.12 inspected in accessible full-text HTML.
- Z. Horváth, *On the positivity step size threshold of Runge--Kutta methods*, Applied Numerical Mathematics 53 (2005), 341--356, https://doi.org/10.1016/j.apnum.2004.08.026 . Abstract available; full text not inspected.
- E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, Journal of Computational and Applied Mathematics 111 (1999), 93--111, https://doi.org/10.1016/S0377-0427(99)00134-X . Accessible overview and abstract reviewed.
