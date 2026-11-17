# Thirteen points uniquely maximize total-variation amplification in quartic Savitzky–Golay smoothing

## Finding
For each integer \(m\ge2\), let \(T_m\) be the bilateral unweighted Savitzky–Golay center smoother: at each integer \(j\), fit a real polynomial of degree at most four to the \(2m+1\) samples at \(j-m,\ldots,j+m\), by ordinary least squares, and output its central fitted value. The degree-five center smoother agrees with \(T_m\) by symmetry.

For any real, bounded, bi-infinite sequence of finite adjacent total variation, define
\[
V(x)=\sum_{j\in\mathbb Z}|x_{j+1}-x_j|.
\]
The sharp operator amplification is the finite-impulse-response \(\ell^1\) mass
\[
G_m=\sup_{V(x)>0}\frac{V(T_mx)}{V(x)}
=\sum_{k=-m}^{m}|h_{m,k}|,
\]
where the exact weights are
\[
h_{m,k}=
\frac{15\bigl(63k^4-(70m^2+70m-105)k^2+15m^4+30m^3-35m^2-50m+12\bigr)}
{4(2m-3)(2m-1)(2m+1)(2m+3)(2m+5)}.
\]
**The unique globally worst window is the thirteen-point window** \(m=6\), with
\[
\boxed{G_m\le G_6=\frac{3763}{2431}=1.547922665569724\ldots,\qquad G_m=G_6\iff m=6.}
\]
Every \(G_m\) is attained by a one-jump (Heaviside) input, so the maximum is an exact stability statement, not merely an upper estimate. The corresponding largest negative kernel mass is \(666/2431\).

Despite the strict finite global maximum, the gain stays above one at large window lengths. With
\[
K(u)=\frac{225-1050u^2+945u^4}{128},\qquad
u_\pm=\sqrt{\frac{35\pm2\sqrt{70}}{63}},
\]
and \(J(u)=(225u-350u^3+189u^5)/128\),
\[
\lim_{m\to\infty}G_m
=\int_{-1}^1|K(u)|\,du
=1+4\bigl(J(\nu_-)-J(\nu_+)\bigr)
=1.504091623350886\ldots.
\]

## Assumptions and scope
The filter is translation invariant on the full integer lattice; the fitted data window is equally spaced, symmetric, unweighted and has odd length at least five. All input and output samples are real. Variation is unanchored adjacent \(\ell^1\) variation on \(\mathbb Z\). Bounded finite-variation inputs include finite-support steps and sequences with distinct one-sided limits. Constants are in the nullspace of this seminorm and are fixed by \(T_m\).

The statement compares the *entire family* of quartic/fifth-degree center filters, not a selected set of conventional coefficient tables. No finite-interval boundary treatment, irregular spacing, noncentral SG derivative, stochastic noise model or weighted least-squares variant is included.

## Proof
**1. Exact least-squares kernel.** Put \(S_{2r}=\sum_{k=-m}^{m}k^{2r}\). Symmetry decouples odd monomials from the even span \(\{1,k^2,k^4\}\). The Gram matrix of this even subspace is
\[
A_m=\begin{pmatrix}S_0&S_2&S_4\\S_2&S_4&S_6\\S_4&S_6&S_8\end{pmatrix}.
\]
The fitted intercept functional is represented by \((1,k^2,k^4)A_m^{-1}(1,0,0)^{\mathsf T}\). Expanding the first column by cofactors gives the numerator
\[
(S_4S_8-S_6^2)+(S_4S_6-S_2S_8)k^2+(S_2S_6-S_4^2)k^4
\]
over \(\det A_m\). Faulhaber's formulas for the even power sums simplify this expression to the displayed \(h_{m,k}\). In particular \(\sum h_{m,k}=1\) and \(\sum k^rh_{m,k}=0\) for \(1\le r\le4\). The degree-five fit has the same intercept because its extra odd column is orthogonal to the even subspace.

**2. The variation norm and sharp jump.** Write \((\Delta x)_j=x_{j+1}-x_j\). Since \(T_m\) is a finite convolution, \(\Delta T_mx=T_m\Delta x\). The convolution triangle inequality yields \(V(T_mx)\le(\sum|h_{m,k}|)V(x)\). For \(x_j=\mathbf 1_{\{j\ge0\}}\), \(\Delta x\) is one Kronecker impulse, so equality holds. Thus the kernel absolute sum is the exact norm and every window has a one-jump norming input.

**3. Exact finite-window certificate.** Define
\[
P_m=(2m-3)(2m-1)(2m+1)(2m+3)(2m+5),\quad
B_m=-70m^2-70m+105,\quad
C_m=15m^4+30m^3-35m^2-50m+12.
\]
Then the integer-only formula
\[
G_m=\frac{15}{4P_m}\left(|C_m|+2\sum_{k=1}^{m}|63k^4+B_mk^2+C_m|\right)
\]
requires no root approximation. The included standalone `verify.py` exhaustively compares integers \(15( |C_m|+2\sum|\cdots|)\cdot2431\) with \(4P_m\cdot3763\) for every \(2\le m\le1999\). Every inequality is strict except the exact equality \(m=6\). This is an exhaustive finite interval, **not** the whole proof; the remaining infinite tail is bounded independently below.

**4. Analytic infinite tail.** For \(|u|\le1\), write \(F_m(u)=m h_{m,mu}\), interpreting the polynomial formula for real \(mu\). The coefficients of \(1,u^2,u^4\) converge respectively to \(225/128,-1050/128,945/128\), hence \(F_m\to K\) uniformly. To make this quantitative, set \(P_m=m^5p(1/m)\), where
\[
p(t)=(2-3t)(2-t)(2+t)(2+3t)(2+5t)>31\quad(0<t\le1/2000).
\]
After substituting \(t=1/m\), the absolute differences of the three coefficients from their limits are at most
\[
\frac{15}{128m}\frac{240+80t+1400t^2+114t^3+675t^4}{p(t)}<\frac1m,
\]
\[
\frac{525}{64m}\frac{48+32t+200t^2+18t^3+45t^4}{p(t)}<\frac{13}{m},
\]
\[
\frac{945}{128m}\frac{80+80t+200t^2+18t^3+45t^4}{p(t)}<\frac{20}{m}.
\]
Here \(p(t)>31\) follows from \((2-3t)^5>31\), and the strict right inequalities follow by substituting the largest permitted \(t=1/2000\) in the positive-coefficient bounds. Consequently
\[
\sup_{|u|\le1}|F_m(u)-K(u)|<34/m\quad(m\ge2000).
\]
The polynomial \(K\) has critical values \(K(0)=225/128\), \(K(\pm\sqrt5/3)=-25/48\), and \(K(\pm1)=15/16\). Thus \(\operatorname{Var}_{[-1,1]}(|K|)\le\operatorname{Var}_{[-1,1]}K=1435/192\). The bounded-variation Riemann-sum estimate, including the duplicated right endpoint, gives
\[
\left|\frac1m\sum_{k=-m}^{m}|K(k/m)|-\int_{-1}^1|K(u)|\,du\right|\le\frac{1435/192+15/16}{m}<\frac9m.
\]
Combining the two inequalities yields
\[
G_m<G_\infty+\frac{(2m+1)34}{m^2}+\frac9m<G_\infty+\frac{78}{m},\qquad m\ge2000.
\]

**5. Exact continuum bound and separation.** The two positive zeros of \(K\), ordered \(\nu_-<\nu_+\), satisfy
\[
0.538469<\nu_-<0.538470,\qquad0.906179<\nu_+<0.906180.
\]
These rational intervals follow by testing the signs of \(63u^4-70u^2+15\) at their rational endpoints and using its monotonicity on either side of \(\sqrt5/3\). On \([0,1]\), \(|J'|=|K|<18\). Evaluating \(J\) at the two rational midpoints, with conservative error \(18\cdot10^{-6}\) for their difference, proves by exact rational arithmetic that \(G_\infty<301/200=1.505\). The checked inequality
\[
\frac{301}{200}+\frac{78}{2000}<\frac{3763}{2431}
\]
therefore proves \(G_m<G_6\) for **all** \(m\ge2000\). Together with step 3 this proves the all-window sharpness and uniqueness. Since \(m h_{m,k}\to K(k/m)\) uniformly and the Riemann sums converge, the integral expression for \(G_\infty\) follows; its explicit form comes from integrating the two negative lobes of \(K\).

## Verification
Run `python3 verify.py` with the Python 3 standard library. It reconstructs the even least-squares Gram-cofactor formula and polynomial reproduction on 29 independent sample windows, evaluates **all** windows \(2\le m\le1999\) using exact integers, validates both positive-root brackets and the strict continuum upper bound in rational arithmetic, checks the quantitative coefficient-error bounds used for the tail, and verifies that discrete single jumps attain the precise norm on representative windows.

The finite checker is supplementary to, and explicitly combined with, the analytic tail proof. The claim does not infer an infinite property from finite enumeration alone. The decimal approximations have no role in any strict comparison.

## Relationship to prior work
Savitzky and Golay introduced the least-squares center-convolution construction in 1964; their filter definition and classical coefficient tables are prior art. Schmid, Rath and Diebold (2022) discuss frequency-domain limitations and filtering artifacts for SG kernels, including degree-four and higher center filters, but do not establish this worst-window, infinite-family total-variation optimization. A published earlier sharp result for degree-two/degree-three SG centers shows **seven** points are uniquely worst under the analogous negative-mass invariant; its full statement explicitly excludes higher polynomial degrees. Its quadratic kernel formula and \(29/21\) maximum do not imply the quartic result here, because the quartic kernel changes sign twice in the positive half-window, and its unique maximizer has thirteen points.

The new contribution is not the elementary identity between a convolution's variation gain and its kernel \(\ell^1\) norm. It is the **exact global comparison over all quartic window lengths**, the unexpected finite optimal extremal window, and a rigorously separated continuum limit. The known coefficients, polynomial reproduction, and generic convolution inequality are not claimed as discoveries.

## Limitations
Only equally spaced unweighted bilateral center smoothing is covered. Boundary rules and finite signals can change operator norms. The data model is worst-case deterministic variation, not mean-square noise reduction. A historical all-window quartic kernel-negative-mass calculation in unindexed signal-processing literature remains possible; the original 1964 paper was verified bibliographically but its publisher-restricted PDF was not inspected in full.

## References
1. A. Savitzky and M. J. E. Golay, *Smoothing and Differentiation of Data by Simplified Least Squares Procedures*, Analytical Chemistry 36 (1964), 1627–1639, DOI: 10.1021/ac60214a047 (July 1, 1964 issue).
2. M. Schmid, D. Rath, and U. Diebold, *Why and How Savitzky–Golay Filters Should Be Replaced*, ACS Measurement Science Au 2 (2022), 185–196, DOI: 10.1021/acsmeasuresciau.1c00054, freely readable at https://pmc.ncbi.nlm.nih.gov/articles/PMC9026279/ .
3. *Seven points maximize the positivity defect of quadratic Savitzky–Golay smoothing* (2026), public text: https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-seven-points-maximize-the-positivity-defect-of-quadratic-savitzk--401e21174d7a/RESULT.md .
