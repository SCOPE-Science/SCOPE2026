# Mean-persistence reserve spacing is never shorter than tail-persistence spacing

## Finding

Consider a symmetric two-reserve continuous-time occupancy process started with both reserves occupied, with the absorbing state of zero occupied reserves. Local extinctions occur independently in each occupied reserve at rate \(e>0\). When exactly one reserve is occupied, recolonization of the empty reserve occurs at rate
\[
c(d)=c_0e^{-a d},\qquad c_0>0,
\]
where \(d\geq0\) is reserve separation. An independent common catastrophe removes all currently occupied reserves at rate
\[
z(d)=z_0e^{-b d},\qquad z_0>0.
\]
Assume the catastrophe hazard decays faster with separation than recolonization: \(0<a<b\). Write \(\tau_d\) for time to total extinction, \(M(d)=\mathbb E_2\tau_d\) for its mean from two occupied reserves, and
\[
\Lambda(d)=-\lim_{t\to\infty}t^{-1}\log\mathbb P_2(\tau_d>t)
\]
for its asymptotic survival-decay rate. The limit exists at every finite \(d\). Let \(d_M\) maximize \(M\) and let \(d_T\) minimize \(\Lambda\), each over \(d\geq0\).

**Theorem (three sharp placement regimes).** Both optimizers exist, are unique, and satisfy
\[
\boxed{0\leq d_T\leq d_M<\infty.}
\]
The inequality is strict whenever \(d_M>0\). Put
\[
U=c_0+3e,\quad\Delta_0=\sqrt{U^2-8e^2},\quad
\ell_0=\frac{U-\Delta_0}{2},
\qquad z_T=\frac{a c_0\ell_0}{b\Delta_0}.
\]
Let \(z_M\) be the unique positive solution of
\[
\boxed{b z_M[(c_0+3e+z_M)^2-2e^2]=2a e^2 c_0.}
\]
Then \(0<z_M<z_T\), and the complete classification in the catastrophe amplitude \(z_0\) is:

- \(0<z_0\leq z_M\): \(d_T=d_M=0\).
- \(z_M<z_0\leq z_T\): \(d_T=0<d_M\).
- \(z_0>z_T\): \(0<d_T<d_M\).

All inequalities are exact; at either parameter boundary the corresponding objective still has a unique optimizer at zero. Thus an open parameter regime makes an initial-state mean-lifetime objective recommend strictly *greater* separation than a long-horizon, quasi-stationary survival objective.

## Assumptions and scope

The occupancy count is the continuous-time Markov chain on \(\{2,1,0\}\). Occupied reserves have individual, independent exponential local-extinction clocks at rate \(e\). In state 2, either local event moves the process to state 1, giving a total rate \(2e\); in state 1, a local event moves it to state 0 at rate \(e\). Recolonization is possible only in state 1, at rate \(c(d)\), and moves the chain to state 2. An independent common-catastrophe clock of rate \(z(d)\) sends either positive state directly to state 0. State 0 is absorbing. All clocks are independent of the past given the state, and the process starts from state 2.

This is a deliberately specified continuous-time common-shock analogue of the distance-dependent connectivity/catastrophe trade-off, **not** the discrete-time transition process of Wagner, Ross and Possingham. The catastrophe clock has a state-independent rate and kills all occupied reserves; the source paper also allows catastrophes removing only one reserve, so its formulas are not silently imported into this model. The rates and exponential kernels are assumptions rather than estimated field parameters.

The transient generator in state order \((2,1)\) is
\[
Q(d)=\begin{pmatrix}-(2e+z)&2e\\c&-(e+c+z)\end{pmatrix},
\]
where \(c=c(d)\), \(z=z(d)\). Since \(e,c,z>0\) at every finite separation, the transient class is irreducible and is killed almost surely. The overall time unit is arbitrary; the spacing unit is determined by \(a,b\).

## Proof

**1. Two exact objectives.** Write \(N=c+3e+z\) and \(D=2e^2+zN\). The backward equations for the means \(m_2,m_1\) are
\[
(2e+z)m_2=1+2e m_1,\qquad(e+c+z)m_1=1+c m_2.
\]
Their unique solution gives
\[
\boxed{M(d)=m_2=\frac{c+3e+z}{2e^2+z(c+3e+z)}=\frac ND.}
\]
For the tail, \(-Q=zI+\begin{psmallmatrix}2e&-2e\\-c&e+c\end{psmallmatrix}\). Let \(U=c+3e\) and \(\Delta=\sqrt{U^2-8e^2}>0\). The two eigenvalues of \(-Q\) are \(z+(U\pm\Delta)/2\). Irreducibility and strictly positive survival coefficients from state 2 imply the slow eigenvalue gives the logarithmic survival rate:
\[
\boxed{\Lambda(d)=z+\ell(c),\qquad \ell(c)=\frac{U-\Delta}{2}=\frac{4e^2}{U+\Delta}.}
\]
The last rationalized identity also shows \(\ell(c)>0\) and makes the derivative stable to evaluate.

**2. Derivatives and uniqueness.** Direct differentiation, using \(c'=-ac\), \(z'=-bz\), gives
\[
M'(d)=\frac{bz(N^2-2e^2)-2ae^2c}{D^2},
\quad
\Lambda'(d)=-bz+ac\frac{\ell(c)}{\Delta}.
\]
The factor \(N^2-2e^2\) is strictly positive because \(N>3e\). The sign of \(M'\) is the sign of
\[
H_M(d)=b\frac{z}{c}(N^2-2e^2)-2ae^2.
\]
For \(b>a\), the ratio \(z/c=(z_0/c_0)e^{-(b-a)d}\) decreases strictly, as does \(N=c+3e+z\). Therefore \(H_M\) decreases strictly from its initial value to \(-2ae^2\). It follows that \(M\) either decreases strictly after zero or first increases and then decreases, with exactly one maximizer. The sign of \(\Lambda'\) is the sign of
\[
H_T(d)=\frac ab\frac c z\frac{\ell(c)}\Delta-1.
\]
Here \(c/z\) increases strictly with \(d\); so does \(\ell(c)/\Delta=(U/\Delta-1)/2\), because \(U\) decreases and \(U/\sqrt{U^2-8e^2}\) strictly decreases as \(U\) increases. Moreover \(H_T(d)\to+\infty\) as \(d\to\infty\), because \(c/z\to\infty\) and \(\ell(c)/\Delta\to1\). Hence \(\Lambda\) either increases strictly after zero or first decreases and then increases, with exactly one minimizer. Both are attained at finite separation.

**3. Pointwise ordering of the marginal thresholds.** For every \(c>0\), \(z\geq0\), write \(U=c+3e\), \(N=U+z\), \(\Delta=\sqrt{U^2-8e^2}\). Then
\[
\boxed{\frac{\ell(c)}\Delta>\frac{2e^2}{N^2-2e^2}.}
\]
Indeed, using \(\ell(c)=4e^2/(U+\Delta)\), cross-multiplication reduces the claimed strict inequality to \(2(N^2-2e^2)>\Delta(U+\Delta)\). Its left-minus-right side satisfies
\[
2(N^2-2e^2)-\Delta(U+\Delta)
\geq U(U-\Delta)+4e^2>0,
\]
since \(N\geq U>\Delta\). No limiting or numerical argument is involved.

At any positive-separation zero of \(\Lambda'\), one has \(z/c=(a/b)\ell/\Delta\); the displayed strict inequality forces \(M'>0\) there. If \(d_T>0\), this means the unique maximizer of \(M\) must lie strictly to the right of \(d_T\). If \(d_T=0\), the same ordering is immediate. In fact, if \(M'(0)>0\) and \(\Lambda'(0)=0\), strictness again gives \(d_M>0=d_T\). This proves the optimizer ordering, including its strictness condition.

**4. Exact amplitude boundaries.** At separation zero, \(\Lambda'(0)=0\) if and only if
\[
z_0=z_T=\frac{a c_0\ell_0}{b\Delta_0}.
\]
Because \(\Lambda'(0)=-bz_0+a c_0\ell_0/\Delta_0\), smaller catastrophe amplitude gives \(\Lambda'(0)>0\), hence \(d_T=0\), and larger amplitude gives \(d_T>0\). Similarly \(M'(0)=0\) exactly when the displayed defining equation for \(z_M\) holds. Its left side increases continuously and strictly from zero to infinity as \(z_M\) increases, so the root exists uniquely. The pointwise strict inequality at \(z_0=z_T\) implies \(M'(0)>0\), while at \(z_0=0\) the derivative is negative. Therefore \(0<z_M<z_T\). Combining the derivative signs and uniqueness completes all three regimes and the boundary cases.

## Verification

`verify.py` independently reconstructs the two transient backward equations over exact-rational parameter grids; symbolically checks the generator determinant, eigenvalue polynomial, mean formula, and derivatives; and performs deterministic, bounded numerical stress tests of the objective ordering and critical-point formulas. It has no external dataset and prints its exact assertion count. For example, at \(e=c_0=a=1\), \(b=2\), the boundaries reduce to
\[
z_M^3+8z_M^2+14z_M-1=0,\quad z_M\approx0.06870782333,
\qquad z_T=\frac{\sqrt2-1}{4}\approx0.10355339059.
\]
With \(z_0=0.03\), both optimal distances are zero. With \(z_0=0.08\), \(d_T=0\) and \(d_M\approx0.097682567728\). With \(z_0=0.3\), \(d_T\approx0.602594205566\) and \(d_M\approx1.045481687293\). These computations illustrate rather than prove the theorem: the proof applies for all positive parameters with \(b>a\).

## Relationship to prior work

Wagner, Ross and Possingham (arXiv:math/0309255, earliest public version September 16, 2003) introduce the competing distance dependence of colonization and spatially correlated catastrophes and optimize a quasi-stationary eigenvalue in a *discrete-time* two-reserve model. Their Section 5 additionally treats local extinction and external recruitment using stationary occupancy with ongoing imports. This result does not claim that modeling idea, the Markov formulation, or quasi-stationary optimization as new; it proves a different continuous-time common-catastrophe model's universal *ordering between two different optimal separations*, plus three exact amplitude regimes. The source's printed transition matrices include single-reserve catastrophes, unlike this model.

McCarthy, Thompson and Possingham (2004 online) compare reserve-number decisions based on mean time and extinction risk, and Blowes and Connolly (2012) compare long-run growth and quasi-extinction criteria in stochastic spatial populations. Those studies motivate the distinction between persistence objectives but involve different state descriptions or optimization variables; no implication from their accessible statements establishes this two-reserve mean-versus-tail ordering. Grimm and Wissel (2004) clarify why quasi-stationary persistence need not equal initial-condition persistence. The full McCarthy and Blowes articles were not inspected here; they remain explicit historical-priority risks. Mathematical originality has not undergone independent review.

## Limitations

The theorem concerns exactly two identical patches with local extinction, a state-independent *systemwide fatal catastrophe clock*, and exponential separation effects with faster catastrophe decay \(b>a\). Other catastrophe geometries, state-dependent shock intensities, \(b\leq a\), heterogeneous patches, external recruitment after global extinction, nonlinear dispersal kernels, multiple reserves, and finite-deadline survival objectives are not classified. Here \(M\) is the mean from the specified fully occupied initial state; \(1/\Lambda\) is the intrinsic late-survival time scale, not that same initial-state mean. Neither optimal distance should be interpreted as an empirical reserve-management prescription without calibrated rates and model validation. No independence, originality, or biological relevance beyond the assumptions has been externally certified.

## References

- Wagner, L. D., Ross, J. V. and Possingham, H. P. *Catastrophe Management and Inter-Reserve Distance for Marine Reserve Networks*. arXiv:math/0309255 (first public version 2003-09-16); *Ecological Modelling* **201** (2007), 82–88. https://arxiv.org/abs/math/0309255 ; https://doi.org/10.1016/j.ecolmodel.2006.07.030.
- McCarthy, M. A., Thompson, C. J. and Possingham, H. P. *Theory for Designing Nature Reserves for Single Species*. *The American Naturalist* **165** (2005), 250–257; published online 2004-12-22. https://doi.org/10.1086/427297.
- Blowes, S. A. and Connolly, S. R. *Risk spreading, connectivity, and optimal reserve spacing*. *Ecological Applications* **22** (2012), 311–321. https://doi.org/10.1890/11-0952.1.
- Grimm, V. and Wissel, C. *The intrinsic mean time to extinction: a unifying approach to analysing persistence and viability of populations*. *Oikos* **105** (2004), 501–511. https://doi.org/10.1111/j.0030-1299.2004.12606.x.
