# Periodic habitat clustering strictly rescues a marginal coloniser in hierarchical metacommunities

## Finding

Consider a superior competitor and an inferior, globally dispersing coloniser in the two-species patch-occupancy model of Planas-Sitjà, Iritani and Cronin. When the superior competitor's effective colonisation rate varies periodically and nontrivially at fixed arithmetic mean, the inferior coloniser's invasion exponent is **strictly larger** than under constant colonisation at that same mean. This holds for every nonconstant positive periodic waveform and every forcing frequency, provided the superior competitor persists. At the constant-environment invasion boundary, any such variation creates a unique attracting positive periodic coexistence state.

Specifically, if \(K\in(0,1)\) is habitable patch capacity, \(\mu>0\) is the mortality rate, \(\ell>0\) is the inferior species' constant effective colonisation rate, and \(b(t)>0\) is the superior competitor's continuous \(T\)-periodic colonisation rate, the occupancy equations are

\[
\dot M=M\{b(t)(K-M)-\mu\},\qquad
\dot L=L\{\ell(K-M-L)-b(t)M-\mu\}.
\]

Write \(\overline b=T^{-1}\int_0^T b(t)\,dt\). Assume \(K\overline b>\mu\). There is a unique positive periodic resident orbit \(M_*(t)\in(0,K)\). Its associated inferior-coloniser invasion exponent is \(\Lambda_{\mathrm{per}}\). The constant-colonisation comparator has \(M_0=K-\mu/\overline b\) and exponent \(\Lambda_{\mathrm{const}}=\ell\mu/\overline b-K\overline b\). Writing \(Y(t)=K-M_*(t)\) and \(\langle f\rangle=T^{-1}\int_0^T f(t)\,dt\), the exact identity is

\[
\boxed{\Lambda_{\mathrm{per}}-\Lambda_{\mathrm{const}}
=\ell\bigl(\langle Y\rangle-\langle Y^{-1}\rangle^{-1}\bigr)>0}
\]

for every nonconstant \(b(t)\). Equality holds exactly for constant \(b\). Whenever \(\Lambda_{\mathrm{per}}>0\), there is a unique strictly positive \(T\)-periodic coexistence state that attracts every initial state with \(M>0\), \(L>0\), and \(M+L\le K\). In particular, \(\Lambda_{\mathrm{const}}=0\) implies positive periodic coexistence for every nonconstant seasonal modulation.

## Assumptions and scope

The model is deterministic, continuous time, with strict competitive replacement by the superior species and no environmental feedback from the populations. The landscape's habitable fraction \(K=1-H\) is fixed. The inferior coloniser has global dispersal \(d_L=1\), so the source paper's landing factor \(\lambda_L=K\) and \(\ell=c_LK\) remain constant even as habitat autocorrelation \(A(t)\in[0,1]\) varies. The superior species has fixed dispersal parameter \(d_M\in[0,1)\), effective rate

\[
b(t)=c_M\{K+(K^{d_M}-K)e^{A(t)-1}\}.
\]

The analysis applies more generally to any strictly positive continuous periodic \(b(t)\). Only the mean-persistence inequality \(K\overline b>\mu\) is imposed; no slow- or fast-forcing approximation is used. The admissible physical state space is \(M\ge0\), \(L\ge0\), \(M+L\le K\). The coloniser's invasion exponent is the period-average instantaneous per-capita growth rate computed along the resident orbit, not an equilibrium payoff.

## Proof

**Resident existence and uniqueness.** Set \(Z=K/M-1\) for positive resident occupancy. Direct differentiation of the superior competitor's equation gives the linear equation

\[
\dot Z=\mu-[Kb(t)-\mu]Z.
\]

Its homogeneous time-\(T\) multiplier is \(\exp[-T(K\overline b-\mu)]\in(0,1)\). The inhomogeneous forcing is positive, hence the unique fixed point of the period map is strictly positive. Thus \(Z_*(t)>0\) and \(M_*(t)=K/(1+Z_*(t))\in(0,K)\) is the unique positive periodic orbit; all positive resident solutions converge to it exponentially. If \(M_*\) were constant, its equation would force \(b(t)\) to be constant.

**Exact invasion identity.** Along the resident orbit, direct differentiation gives

\[
\frac{d}{dt}\log\frac{M_*}{K-M_*}=K\biggl[b(t)-\frac{\mu}{K-M_*}\biggr].
\]

Integrating over a period yields \(\overline b=\mu\langle Y^{-1}\rangle\). Similarly, integrating \(\dot{\log M_*}=b(t)(K-M_*)-\mu\) yields \(\langle bM_*\rangle=K\overline b-\mu\). Therefore

\[
\begin{aligned}
\Lambda_{\mathrm{per}}
&=\bigl\langle\ell(K-M_*)-b(t)M_*-\mu\bigr\rangle\\
&=\ell\langle Y\rangle-K\overline b.
\end{aligned}
\]

The constant-rate orbit has \(Y_0=\mu/\overline b=\langle Y^{-1}\rangle^{-1}\). Subtracting the constant-rate invasion exponent proves the boxed formula. The strict arithmetic-mean/harmonic-mean inequality for the positive, nonconstant function \(Y\) proves strict improvement. This is a periodwise identity, not a numerical or small-amplitude approximation.

**Positive coexistence.** The resident equation is independent of \(L\). When \(M=M_*\), the inferior species obeys \(\dot L=L[a(t)-\ell L]\), where \(a(t)=\ell(K-M_*)-b(t)M_*-\mu\) has mean \(\Lambda_{\mathrm{per}}\). If this mean is positive, the reciprocal \(V=1/L\) solves \(\dot V=-a(t)V+\ell\), whose homogeneous period multiplier is \(e^{-T\Lambda_{\mathrm{per}}}<1\). The positive forcing yields a unique positive periodic \(L_*\), globally attracting positive solutions along the periodic resident. For general initially positive \(M\), the resident's exponential convergence makes the coefficient of this reciprocal equation an exponentially decaying perturbation of the periodic coefficient. Variation of constants and the negative mean exponent then imply \(L(t)-L_*(t)\to0\). The physical region remains invariant: at \(M+L=K\), \(\dot M+\dot L=-\mu K\), and the coordinate axes are invariant.

**A fully admissible exact family and a quantitative onset.** Take

\[
K=\frac12,\quad c_L=1,\quad d_L=1,\quad c_M=\frac25,\quad d_M=0,\quad \mu=\frac9{100},
\]

and, for \(0<|\eta|<\frac12-e^{-1}\), set

\[
A_\eta(t)=1+\log\bigl(\tfrac12+\eta\cos(t/10)\bigr).
\]

Then \(A_\eta(t)\in[0,1]\), \(\ell=1/2\), \(b_\eta(t)=3/10+(\eta/5)\cos(t/10)\), and \(T=20\pi\). The constant comparator has resident occupancy \(M_0=1/5\) and is exactly at the inferior species' invasion threshold: \(\Lambda_{\mathrm{const}}=0\). By the strict identity, every nonzero admissible \(\eta\) yields globally attracting positive periodic coexistence. A second-order regular perturbation of the resident equation gives the exact near-onset law

\[
\Lambda_\eta=\frac3{340}\eta^2+O(\eta^3)\quad\text{as }\eta\to0.
\]

Indeed, putting \(b=b_0+\varepsilon\cos(\omega t)\), \(M_0=K-\mu/b_0\), \(\gamma=b_0M_0\), and \(M_*=M_0+\varepsilon u+\varepsilon^2v+O(\varepsilon^3)\), the first-order Fourier coefficients of \(u\) are

\[
u_c=\frac{M_0(\mu/b_0)\gamma}{\gamma^2+\omega^2},\qquad
u_s=\frac{M_0(\mu/b_0)\omega}{\gamma^2+\omega^2}.
\]

The averaged resident identity forces \(\langle v\rangle=-u_c/(2b_0)\), so the invasion increase to second order in \(\varepsilon\) is \(\ell u_c\varepsilon^2/(2b_0)\). In the stated example \(\gamma=3/50\), \(\omega=1/10\), \(\varepsilon=\eta/5\), and \(u_c=9/34\), giving \(3\eta^2/340\). Smooth dependence of a stable periodic orbit on the forcing amplitude justifies the expansion.

## Verification

The standalone `check.py` uses exact rational arithmetic for the critical comparator, the first-order Fourier coefficients and the onset constant. Separately, it solves the resident's exact linear reciprocal equation and reconstructs the positive periodic orbit for two admissible nonzero amplitudes. Period quadrature checks the integral identities, the strict positive invasion exponent, and the quadratic approximation. Tests of finitely many amplitudes verify the implementation only; the universal waveform and all-amplitude claims rely on the analytical proof above.

## Relationship to prior work

Planas-Sitjà, Iritani and Cronin (2026) define the same hierarchical metacommunity equations and landing factor, but solve stationary coexistence at fixed habitat autocorrelation. The present result permits temporally changing autocorrelation while keeping habitat area, mortality and the inferior coloniser's global dispersal fixed.

Peniston and collaborators (2024) explain that periodic colonisation variation can lower the *single-species* time-mean occupancy in Levins-type metapopulations. That general occupancy penalty is already known and is not claimed as new. The contribution here is the exact **two-species invasion identity**, its strict waveform-independent sign, and the resulting new coexistence phase of the specific landscape-dependent competitive replacement system at a static invasion boundary. Burkart, Willeke and Frey (2023) establish environmentally facilitated coexistence for a distinct periodically forced chemostat resource-competition model, not this exact hierarchical patch occupancy equation or its all-waveform invasion identity. Cai (2022) studies adaptive evolution under stochastic mortality/ownership rather than the stated deterministic periodic autocorrelation forcing.

## Limitations

The theorem requires the inferior coloniser's effective rate to remain constant, as when its dispersal is global; allowing seasonal variation in both species' effective colonisation rates changes the exact cancellation and need not preserve the sign. It concerns a deterministic spatially implicit patch-occupancy approximation, not a fully spatial stochastic lattice or empirical evidence. For mean invasion exponents strictly negative, periodicity may improve the exponent without making it positive. There is no claim of independent verification, of a new general Jensen inequality, or of uniqueness of this mechanism in ecological models. The bibliographic search does not establish absolute historical priority.

## References

1. I. Planas-Sitjà, R. Iritani, A. L. Cronin, *Disentangling the interactive effects of anthropogenic disturbances on biodiversity*, arXiv:2603.29116v1, publicly released 31 March 2026, https://arxiv.org/html/2603.29116v1 ; Ecography (2026), DOI:10.1002/ecog.08812.
2. J. H. Peniston et al., *Ecological and evolutionary consequences of temporal variation in dispersal*, Ecography 2024, e06699, https://doi.org/10.1111/ecog.06699 .
3. T. Burkart, J. Willeke, E. Frey, *Periodic temporal environmental variations induce coexistence in resource competition models*, Physical Review E 108 (2023), 034404, https://doi.org/10.1103/PhysRevE.108.034404 ; arXiv:2202.11635.
4. Y. Cai, *Evolutionary coexistence in a metacommunity: Competition-colonization trade-off, ownership effects, environmental fluctuations*, Journal of Theoretical Biology 533 (2022), 110944, https://doi.org/10.1016/j.jtbi.2021.110944 .
