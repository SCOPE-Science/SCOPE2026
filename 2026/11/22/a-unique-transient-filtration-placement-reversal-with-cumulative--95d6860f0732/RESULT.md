# A unique transient filtration-placement reversal with cumulative dominance in a three-room path

## Finding

Consider three equal-volume, well-mixed rooms arranged as a path, with equal bidirectional exchange rate \(k>0\), uniform background loss \(v\geq0\), and one identical, permanently operated local filter of additional first-order loss \(p>0\). A unit pollutant impulse begins in room 1. Let \(f_1(t)\) be the subsequent concentration in room 3 if the filter is in room 1, and \(f_2(t)\) the same concentration if the filter is in room 2. For **every** choice of these parameters there exists a **unique** time \(t_*>0\) such that

\[
  f_1(t)<f_2(t)\quad(0<t<t_*),\qquad
  f_1(t_*)=f_2(t_*),\qquad
  f_1(t)>f_2(t)\quad(t>t_*).
\]

Despite this late instantaneous reversal, the cumulative exposure in room 3 satisfies the *opposite, all-horizon strict comparison*

\[
  \int_0^T f_1(t)\,dt<\int_0^T f_2(t)\,dt
  \qquad\text{for every }T>0.
\]

Hence a constant source activated in room 1 instead of an impulse always produces a smaller room-3 concentration when the filter is in room 1, at every finite observation time. At infinite horizon the impulse cumulative doses tie precisely when \(v=0\), and placement at the emitter is strictly better when \(v>0\). The three-room path is *minimal* for an instantaneous placement reversal within this homogeneous symmetric path model: a two-room path has identical source-to-target impulse responses for filter placements at either endpoint.

## Assumptions and scope

Let \(e_j\) be the standard basis of \(\mathbb R^3\). With unit initial mass scaled to unit concentration in room 1 and equal chamber volumes, write

\[
L_3=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},\qquad
M_j=vI_3+kL_3+p e_je_j^{\mathsf T},\qquad
C^{(j)}(t)=e^{-M_jt}e_1,
\]

for \(j=1,2\) and \(f_j(t)=e_3^{\mathsf T}C^{(j)}(t)\). The flow between adjacent rooms is balanced, and the filter changes only its room's local pollutant loss, **not** the airflow or inter-room exchange. The model is linear, time homogeneous, and source-free after the impulse; there are no adsorption/desorption reservoirs, nonlinear aerosol transport, or unequal volumes. Time and the rate constants use reciprocal consistent units. Strict comparisons refer to positive times; both response functions vanish at \(t=0\).

## Proof

**Step 1: exact Green-function comparison.** For \(s>0\) write \(D_j(s)=\det(sI_3+M_j)\). The end-to-end inverse entry of either tridiagonal matrix has numerator \(k^2\), so its impulse Laplace transform is

\[
 \widehat f_j(s)=\frac{k^2}{D_j(s)}.
\]

Expanding the determinant (or using the determinant lemma) gives the exact identity

\[
 D_1(s)-D_2(s)=pk(s+v).
\]

Consequently, for \(\Delta(t)=f_2(t)-f_1(t)\),

\[
 \widehat\Delta(s)=\frac{pk^3(s+v)}{D_1(s)D_2(s)}.
 \tag{1}
\]

**Step 2: positive strictly log-concave reference kernel.** For each \(j\), the symmetric matrix \(M_j-vI_3=kL_3+pe_je_j^{\mathsf T}\) is positive definite. Indeed its quadratic form is

\[
 k\big((x_1-x_2)^2+(x_2-x_3)^2\big)+px_j^2,
\]

which can vanish only for \(x=0\). Let \(\lambda_1,\ldots,\lambda_6\) be the eigenvalues of \(M_1\) and \(M_2\), counted with multiplicity. They are all strictly larger than \(v\), and

\[
D_1(s)D_2(s)=\prod_{r=1}^6(s+\lambda_r).
\]

Put \(g_r(t)=e^{-\lambda_rt}\mathbf 1_{\{t\ge0\}}\), and let \(h=g_1*g_2*\cdots*g_6\), convolution on the real line. Each \(g_r\) is log-concave on its convex support; by the classical Prékopa convolution theorem, \(h\) is log-concave. It is strictly positive and real analytic on \((0,\infty)\). Furthermore

\[
  h(t)=\frac{t^5}{5!}+O(t^6)\quad(t\downarrow0),
\]

and if \(a=\min_r\lambda_r>v\), with multiplicity \(m\), then

\[
  h(t)=c\,t^{m-1}e^{-at}(1+o(1))\quad(t\longrightarrow\infty),\quad c>0.
\]

The latter follows from the positive product Laplace transform by the leading pole (or by convolution of the slowest exponentials with faster integrable kernels). Therefore \(q(t)=h'(t)/h(t)\) has limits \(+\infty\) and \(-a<-v\) at the two ends. Since \(\log h\) is concave, \(q\) is nonincreasing. It is actually **strictly decreasing**: if it were equal at two distinct times it would be constant on their intervening interval; analyticity of \(\log h\) would make it affine throughout \((0,\infty)\), contradicting its \(5\log t\) behavior near zero.

**Step 3: one and only one sign change.** As \(h(0)=0\), inverse Laplace transformation of (1) yields exactly

\[
\Delta(t)=pk^3\big(h'(t)+vh(t)\big)
          =pk^3h(t)\big(q(t)+v\big).
\tag{2}
\]

By Step 2 the continuous, strictly decreasing \(q\) crosses \(-v\) at precisely one positive time. Formula (2) proves all three asserted instantaneous comparisons and the uniqueness of the reversal.

**Step 4: strict cumulative dominance and its limiting boundary.** Integrating (2) and using \(h(0)=0\) gives the exact *deficit certificate*

\[
 \int_0^T\big(f_2(t)-f_1(t)\big)dt
   =pk^3\left(h(T)+v\int_0^Th(t)dt\right)>0
 \qquad(T>0).
 \tag{3}
\]

For a unit step source switched on in room 1, linear convolution makes the difference of room-3 concentrations precisely the left-hand side of (3), establishing the continuous-source assertion. Taking \(T\to\infty\) in (3), since \(h(T)\to0\), yields

\[
 \int_0^\infty\big(f_2(t)-f_1(t)\big)dt
 =\frac{pk^3v}{D_1(0)D_2(0)},
\]

which vanishes exactly at \(v=0\), and otherwise is positive.

**Step 5: sharp two-room obstruction.** On the two-room path let \(L_2=\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\) and \(N_j=vI_2+kL_2+pe_je_j^{\mathsf T}\) for \(j=1,2\). Reflection exchanges the two local-filter placements and both transition matrices are symmetric; equivalently, their end-to-end resolvents both equal \(k/\det(sI_2+N_1)\), because the two determinants agree. Thus their impulse responses coincide for every positive time. With one room there is no distinct placement; three rooms are minimal.

## Verification

The self-contained checker `verify.py` (dependencies in `requirements.txt`) reconstructs both three-room determinants symbolically, checks (1), the exact end-to-end Green functions, two-room equality, the integrated-dose identity, and an independent matrix-exponential reconstruction of the normalized case \(v=k=p=1\). In this case,

\[
 D_1(s)=s^3+8s^2+19s+13,\quad
 D_2(s)=(s+2)(s^2+6s+6),
\]

and the unique crossing is numerically \(t_*\approx6.8878699336050795\). The computed differences have signs \(\Delta(1)>0\) and \(\Delta(8)<0\). The exactly integrated all-time difference is \(1/156\). **The finite computational checks are supplementary**; the infinite-family, all-time result follows from Steps 1–5 and the standard log-concavity theorem.

## Relationship to prior work

Mao et al. (2023) measure differences between particle control strategies and use cumulative exposure as an evaluation criterion. Novoselac and Siegel (2009) explicitly compare portable air-cleaner placement in a multizone residence with CFD and particle tracking, including impulsive contamination and time-varying response; this establishes that placement and its time dependence are prior knowledge. Parker et al. (2014) provide the state-space framework for multizone contaminant transport and exposure, but their analyzed model deliberately neglects indoor filtration. The Prékopa log-concavity theorem, matrix resolvents, and finite exponential convolutions are established mathematics. None of these inspected works states the simultaneous universal *unique instantaneous reversal*, strict *all-horizon cumulative dominance*, and *sharp two-room obstruction* for the homogeneous symmetric three-room filtration model. This is a comparison of the particular mathematical implications, not a claim that all literature has been exhausted.

## Limitations

The result is conditional on symmetric, equal-rate transport, equal well-mixed volumes, identical background losses, fixed filtration efficiency, and unchanged airflow upon filter placement. Real portable cleaners alter flow patterns and have particle-size-dependent performance; asymmetric ventilation, heterogeneous rooms, time-varying rates, or nonlinear particle processes may invalidate the crossing and ordering conclusions. The result does not optimize filter cost, total exposure across all rooms, infection probability, or exposure from an arbitrary source history. Historical priority is subject to further specialized literature review. No independent external audit has been performed.

## References

1. Mao, Y., Xie, H., Liang, J., He, J. & Ren, J. (2023). *Experimental study on the control effects of different strategies on particle transportation in a conference room: Mechanical ventilation, baffle, portable air cleaner, and desk air cleaner.* Atmospheric Pollution Research 14(4), 101716. Published online 2023-03-09. https://doi.org/10.1016/j.apr.2023.101716
2. Novoselac, A. & Siegel, J. A. (2009). *Impact of placement of portable air cleaning devices in multizone residential environments.* Building and Environment 44, 2348–2356. https://doi.org/10.1016/j.buildenv.2009.03.023
3. Parker, S. T., Coffey, C., Gravesen, J., Kirkpatrick, J., Ratcliffe, K., Lingard, B. & Nally, J. (2014). *Contaminant ingress into multizone buildings: An analytical state-space approach.* Building Simulation 7, 57–71. https://doi.org/10.1007/s12273-013-0136-5
4. Prékopa, A. (1980). *Logarithmic concave measures and related topics.* In: Stochastic Programming (Proc. International Conference, Oxford 1974), pp. 63–82. Academic Press. Classical convolution log-concavity theorem.
