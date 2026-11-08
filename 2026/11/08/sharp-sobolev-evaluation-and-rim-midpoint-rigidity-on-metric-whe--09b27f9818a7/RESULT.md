# Sharp Sobolev evaluation and rim-midpoint rigidity on metric wheels

## Finding

For each integer \(m\ge3\), let \(W_m=K_1\vee C_m\) be the wheel with one hub and \(m\) cyclic rim vertices. Regard each of its \(2m\) edges as a unit interval, with unnormalized arclength \(ds\). On the real space of continuous edgewise-\(H^1\) functions with \(\int_{W_m}f\,ds=0\), define the optimal *squared* evaluation constant \(\mathcal K_m\) by
\[
\|f\|_{L^\infty(W_m)}^2\le\mathcal K_m\int_{W_m}|f'|^2\,ds.
\]
Put \(\rho=(3-\sqrt5)/2\) and
\[
u_m=\frac{1+\rho^m}{\sqrt5(1-\rho^m)}.
\]
Then the exact sharp constant is
\[
\boxed{\mathcal K_m=\frac{5u_m}{4}-\frac{49}{48m}}
=\frac{\sqrt5}{4}\frac{1+\rho^m}{1-\rho^m}-\frac{49}{48m}.
\]
For every \(m\ge4\), its maximizers among *all points of the metric graph* are precisely the \(m\) midpoints of the rim edges; every spoke and every vertex is strictly suboptimal. For \(m=3\), the graph is \(K_4\), and precisely its six edge midpoints maximize evaluation. Every nonzero function attaining the inequality is a nonzero real scalar multiple of the centered Kirchhoff Green representer of evaluation at one of the specified points.

Writing \(\mathcal S_m\) for the maximum squared evaluation norm over all spoke points, the strict separation for \(m\ge4\) has the explicit form
\[
\mathcal K_m-\mathcal S_m=\frac{F_m}{4a_m}>\frac{37}{20736},\qquad
a_m=1-u_m-\frac1{2m},
\]
\[
F_m=-5u_m^2+\left(5+\frac4m\right)u_m-1-\frac{5}{2m}-\frac3{4m^2}.
\]
Thus \(\mathcal K_m=\sqrt5/4-49/(48m)+O(\rho^m)\). In particular, the sharp squared constants converge to the nonzero finite limit \(\sqrt5/4\) as the wheel grows. For example, \(\mathcal K_3=41/144\), \(\mathcal K_4=21/64\), and \(\mathcal K_5=961/2640\).

## Assumptions and scope

All edge lengths equal one. Functions are real, continuous at graph vertices, and belong to the usual \(H^1\) space on each edge. The measure is ordinary, *unnormalized* arclength; the same sharp constant results from the normalized mean-zero equation since the mean-zero condition is unchanged, but the displayed energy is unnormalized. The hub is indexed by \(0\), and the cyclic rim vertices by \(1,\ldots,m\). Evaluation means a point of the entire geometric realization, not merely a vertex.

## Proof

**1. The exact evaluation-diagonal identity.** Let \(G\) be any connected unit-edge metric graph with \(E\) edges and combinatorial Laplacian \(L\), and put \(\pi_v=\deg(v)/(2E)\). Every admissible function can be written uniquely as a piecewise-linear interpolation of vertex values \(F_v\), plus functions \(h_e\in H^1_0(0,1)\) on the edges. These two pieces are orthogonal for the derivative-energy form. Since the arclength mean of the interpolation equals \(\sum_v\pi_vF_v\), the evaluation functional on the mean-zero quotient has vertex coefficient
\[
c_t=(1-t)e_a+te_b-\pi
\]
at a point a fraction \(t\in[0,1]\) along the edge \(ab\), and on the edge-Dirichlet components has coefficient \(h\mapsto h_{ab}(t)-E^{-1}\sum_e\int_0^1h_e\). The Dirichlet interval Green kernel \(D(s,t)=\min(s,t)-st\) satisfies
\[
D(t,t)=t(1-t),\quad\int_0^1D(s,t)\,ds=\frac{t(1-t)}2,
\quad\int_0^1\!\int_0^1D(s,t)\,ds\,dt=\frac1{12}.
\]
Taking squared dual norms in the energy Hilbert space therefore gives the identity
\[
q_{ab}(t):=\|\delta_{x_t}\|_{(H^1/\mathbb R)^*}^2
=c_t^TL^+c_t+\left(1-\frac1E\right)t(1-t)+\frac1{12E}.
\]
Here \(L^+\) is the inverse of \(L\) on the zero-sum vertex space. Equivalently, put \(H_v=(e_v-\pi)^TL^+(e_v-\pi)\) and let \(R_{ab}=(e_a-e_b)^TL^+(e_a-e_b)\). Expanding the quadratic gives
\[
\boxed{q_{ab}(t)=(1-t)H_a+tH_b+\left(1-\frac1E-R_{ab}\right)t(1-t)+\frac1{12E}.}\tag{1}
\]
This identity also applies at vertices by taking \(t=0\) or \(1\).

**2. Wheel modes and their resolvent.** For \(W_m\), \(E=2m\); the arclength-mean weights are \(\pi_0=1/4\) and \(\pi_j=3/(4m)\) at rim vertices. The graph Laplacian separates into a hub-versus-uniform-rim eigenmode of eigenvalue \(m+1\), and \(m-1\) nonconstant rim Fourier modes of eigenvalues
\[
\lambda_j=3-2\cos(2\pi j/m),\qquad1\le j<m.
\]
Define the cyclic Green diagonal
\[
u_m=\frac1m\sum_{j=0}^{m-1}\frac1{3-2\cos(2\pi j/m)}.
\]
The inverse of the cyclic matrix \(3I-A(C_m)\) has displacement-\(d\) entry
\[
\frac{\rho^d+\rho^{m-d}}{\sqrt5(1-\rho^m)},
\]
as follows by substituting the geometric recurrence \(3g_d-g_{d-1}-g_{d+1}=\mathbf1_{d=0}\) with cyclic indices; hence its diagonal equals the stated closed form \(u_m\). Resolving the degree-weighted vertex coefficients into the hub mode and zero-sum rim modes gives
\[
H_{\mathrm{hub}}=\frac9{16m},\qquad
H_{\mathrm{rim}}=u_m-\frac{15}{16m}.
\]
Similarly, the two edge-orbit effective resistances are
\[
R_{\mathrm{spoke}}=u_m,\qquad R_{\mathrm{rim}}=1-u_m.
\]
These resistance identities agree with established formulas for wheel vertices; they are not claimed as new.

**3. Exact edge profiles and localization.** Substitution in (1), with spoke parameter \(t\) directed from hub to rim, yields
\[
q_{\mathrm{spoke}}(t)=\frac9{16m}+\left(u_m-\frac3{2m}\right)t
+\left(1-u_m-\frac1{2m}\right)t(1-t)+\frac1{24m}.
\]
For each rim edge (either orientation),
\[
q_{\mathrm{rim}}(t)=u_m-\frac{15}{16m}
+\left(u_m-\frac1{2m}\right)t(1-t)+\frac1{24m}.
\]
Both are strictly concave on their edges because \(u_m>1/\sqrt5>4/9\) and \(u_m\le1/2\). Thus every rim edge has its unique maximum at \(t=1/2\), with value \(5u_m/4-49/(48m)\). The spoke maximum occurs at the interior point
\[
t_{\mathrm{spoke}}=\frac{1-2/m}{2(1-u_m-1/(2m))};
\]
its inclusion in \((0,1)\) follows from \(m\ge3\) and \(u_m\le1/2\). Its exact value is
\[
\mathcal S_m=\frac{H_{\mathrm{hub}}+H_{\mathrm{rim}}}{2}
+\frac{a_m}{4}+\frac{(u_m-3/(2m))^2}{4a_m}+\frac1{24m}.
\]
An exact subtraction gives \(4a_m(\mathcal K_m-\mathcal S_m)=F_m\), where \(F_m\) is displayed in the finding. When \(m=3\), \(u_m=1/2\) and \(F_m=0\); the graph is \(K_4\), so all six edge midpoints are equivalent and maximizing. When \(m\ge4\), the closed form shows \(4/9<u_m\le u_4=7/15<1/2\) and \(0<1/m\le1/4\). Regard
\[
F(u,x)=-5u^2+5u-1+x\left(4u-\frac52\right)-\frac34x^2.
\]
On the rectangle \(4/9\le u\le1/2\), \(0\le x\le1/4\), the function is nondecreasing in \(u\) and strictly decreasing in \(x\), because its partial derivatives are \(5-10u+4x\ge0\) and \(4u-5/2-3x/2<0\). Therefore
\[
F_m=F(u_m,1/m)>F(4/9,1/4)=\frac{37}{5184}>0.
\]
Since \(0<a_m<1\), we have \(\mathcal K_m-\mathcal S_m>37/20736\). Strict edgewise concavity then excludes all other points. No unexamined boundary cases remain.

**4. Equality functions and limit.** In the mean-zero energy Hilbert space, let \(g_x\) be the unique centered continuous Kirchhoff solution of \(-g_x''=\delta_x-ds/(2m)\) in the distributional graph sense. It represents evaluation: \(f(x)=\int f'g_x'\,ds\) and \(\int|g_x'|^2\,ds=q(x)=g_x(x)\). Hilbert-space Cauchy--Schwarz gives equality exactly for nonzero scalar multiples of \(g_x\), at the previously classified maximizing points. Finally \(\rho^m\to0\) gives the exact limiting and correction formulas in the finding.

## Verification

The included `verify_wheel_h1.py` runs independent exact-rational checks with Python and SymPy. For each tested wheel and edge point, it subdivides the observed edge, solves the mean-zero Kirchhoff Poisson boundary-value problem (including the constant arclength source on *every* segment), integrates its solution exactly, and compares evaluation with the claimed quadratic profile. The program tests \(m=3,\ldots,11\) on both edge orbits and multiple interior and endpoint coordinates, including the spoke stationary point; it also checks the competing maxima. Its 99 exact evaluations are consistency evidence only. The proof above treats every integer \(m\ge3\) analytically.

## Relationship to prior work

Baker and Faber (arXiv:math/0407428, first posted 2004-07-25) establish metric-graph Laplacians, electrical networks and the combinatorial/metric interface. Cinkir (arXiv:0902.3401, first posted 2009-02-19) gives general Laplacian-pseudoinverse formulas for the *canonical-measure tau constant*, a different invariant. Bapat and Gupta (2010, DOI:10.1007/s13226-010-0004-2) determine wheel and fan **vertex effective resistances**, including the same wheel unit-edge resistances used in step 2. These formulas are antecedents, not novel claims. Their inspected statements do not give the sharp unnormalized-arclength mean-zero Sobolev evaluation constant, its all-points norming set, or the strict rim/spoke separation proved here. Generic resistance identities imply an algorithmic path to the result, but proving the all-wheel strict comparison requires the explicit cyclic resolvent and inequality in step 3.

## Limitations

The scope is the real mean-zero first-order energy on unweighted, equilateral wheels, not arbitrary spoke lengths, nonuniform densities, other vertex conditions or higher-order spaces. Sharpness and equality are mathematical results proved above; the standalone finite checks are not substitutes for the infinite-family proof. Prior vertex resistances are acknowledged; an unindexed equivalent Sobolev theorem could affect bibliographic priority.

## References

1. Matthew Baker and Xander Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first submitted July 25, 2004. https://arxiv.org/abs/math/0407428
2. Zubeyir Cinkir, *The tau constant and the discrete Laplacian matrix of a metrized graph*, arXiv:0902.3401, first submitted February 19, 2009. https://arxiv.org/abs/0902.3401
3. R. B. Bapat and Somit Gupta, *Resistance distance in wheels and fans*, Indian Journal of Pure and Applied Mathematics 41 (2010), 1–13, DOI:10.1007/s13226-010-0004-2. https://doi.org/10.1007/s13226-010-0004-2
