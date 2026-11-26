# A sharp positive-time peak criterion for two nonlinear groundwater stores

## Finding

After recharge ends, let two independent nonlinear stores have total discharge
\[
Q(t)=A(t+a)^{-p}+B(t+b)^{-p},\qquad t\ge0,\quad p>1,\quad A,B>0,\quad 0<a<b.
\]
Write \(\beta(t)=d\log(-Q'(t))/d\log Q(t)=Q(t)Q''(t)/Q'(t)^2\), the instantaneous recession exponent, and \(r_0=a/b\). Let \(r_*\in(0,p/(p+2))\) be the unique solution of
\[
A[p-(p+2)r_*]=B r_*^{p+1}[p+2-pr_*]. \tag{1}
\]
If \(r_0<r_*\), the exponent increases strictly up to its unique maximum at \(t_*=(br_*-a)/(1-r_*)>0\) and then decreases strictly. If \(r_0\ge r_*\), the maximum on \([0,\infty)\) is at zero, and the exponent decreases strictly for positive time; its endpoint tangent is horizontal precisely at \(r_0=r_*\). Equivalently, a positive-time maximum exists exactly when
\[
r_0<\frac{p}{p+2}\quad\text{and}\quad \frac AB>\frac{r_0^{p+1}(p+2-pr_0)}{p-(p+2)r_0}. \tag{2}
\]
The offset contrast \(b/a>(p+2)/p\) is sharp for the *possibility* of an interior peak, with amplitudes allowed to vary. This temporal classification is separate from the classical amplitude envelope for peak height discussed below.

## Assumptions and scope

The stores have no input, evapotranspiration or exchange for \(t\ge0\). Amplitudes carry the units needed to express discharge, and offsets share the time unit. Each store with parameters \(A_i,a_i\) has finite remaining storage
\[
S_i(t)=\int_t^\infty A_i(u+a_i)^{-p}\,du=\frac{A_i}{p-1}(t+a_i)^{1-p},
\qquad -S_i'=Q_i.
\]
This gives \(S_i=A_i^{1/p}Q_i^{(p-1)/p}/(p-1)\); \(p=2\) corresponds to a quadratic discharge–storage law. The local exponent is not a finite-window regression slope. Equal individual powers, distinct positive offsets and nonzero amplitudes are assumed.

## Proof

Put \(u=(t+a)^{-1}\), \(v=(t+b)^{-1}\) and \(r=v/u\). Then \(r=(t+a)/(t+b)\) increases strictly from \(r_0\) to one. By differentiation \(-Q'=p(Au^{p+1}+Bv^{p+1})\) and \(Q''=p(p+1)(Au^{p+2}+Bv^{p+2})\). The difference of \((Au^p+Bv^p)(Au^{p+2}+Bv^{p+2})\) and \((Au^{p+1}+Bv^{p+1})^2\) is \(ABu^pv^p(u-v)^2\), so
\[
\beta(t)=\frac{p+1}{p}\left[1+\frac{ABr^p(1-r)^2}{(A+Br^{p+1})^2}\right]. \tag{3}
\]
In particular the two-store value is strictly above the one-store value \((p+1)/p\) at each finite time and tends to it as \(r\uparrow1\).

Differentiating the excess term in brackets with respect to \(r\) gives the strictly positive multiplier \(ABr^{p-1}(1-r)/(A+Br^{p+1})^3\) times
\[
H(r)=A[p-(p+2)r]-Br^{p+1}[p+2-pr]. \tag{4}
\]
On \((0,p/(p+2))\), the first term decreases from \(Ap\) to zero. The function \(r^{p+1}(p+2-pr)\) has derivative \((p+2)r^p[p+1-pr]>0\) on \((0,1)\), so \(H\) is strictly decreasing and is negative at \(p/(p+2)\). On \([p/(p+2),1)\) the first term is nonpositive and the subtracted term is strictly positive. Thus \(H\) has exactly the root (1), with sign positive before and negative after. Because \(r'(t)>0\), the monotonicity, endpoint tangent and peak time follow. The inequality \(H(r_0)>0\) is precisely (2); when \(r_0<p/(p+2)\) the rational-power expression on the right of (2) is finite and some positive amplitude ratio exceeds it. When \(r_0\ge p/(p+2)\) no such peak is possible.

For example, with \(p=2\), \((a,b,A,B)=(1,4,5,27)\) gives \(r_*=1/3\) by (1), \(t_*=1/2\), and \(\beta(t_*)=16/9\) by (3).

## Classical pointwise bounds and their consequence

The pointwise elevation over \((p+1)/p\) in (3) is also a strict Cauchy–Schwarz inequality. For the upper envelope set \(Y_1=u\), \(Y_2=v\) and assign probabilities proportional to \(AY_1^{p+1},BY_2^{p+1}\). Under these probabilities,
\[
\frac{p}{p+1}\beta=\mathbb{E}[Y]\mathbb{E}[1/Y]\le \frac{(u+v)^2}{4uv}=\frac{(1+r)^2}{4r}.
\]
This is the classical Kantorovich inequality [1]; here the maximum is attained precisely at equal endpoint probabilities, or \(Br^{p+1}=A\). Equivalently, (3) has an amplitude factor \(x/(1+x)^2\le1/4\) with \(x=Br^{p+1}/A\). For \(p=2\), the envelope is greater than two exactly at \(r<1/3\). As \(r(t)\) strictly increases, some positive amplitudes and some positive time yield \(\beta>2\) if and only if \(b/a>3\). For example, \((a,b,A,B)=(1,4,27,1000)\) attains the envelope at \(r=3/10\), \(t=2/7\), giving \(169/80\). This threefold contrast is a consequence of the classical envelope, not an independent novelty claim and not a consequence of the temporal peak criterion.

## Verification

The included rational-arithmetic checker tests the identities for the exponent and derivative sign and the two numerical examples, along with pointwise envelope bounds. The proof covers all real \(p>1\); finite tests do not do so.

## Relationship to prior work

Single-store nonlinear recession and superposition-induced changes of estimated slopes are established in hydrology [2–4]. Jachens et al. [3] explicitly obtain larger and varying fitted slopes after superposing antecedent recessions; this does not give the exact sign and unique turning point of the instantaneous exponent of two equal-power terms. Analogous indexed results exist for sums of exponential discharges [5] and the time-reversed inverse-time problem [6]. The latter's two-mode exponent and root equation agree with the boundary algebra at \(p=1\), which does not give a store with finite remaining integral here. Neither the classical pointwise inequalities nor the inspected qualitative hydrologic superposition results determine the monotonicity and exact amplitude–offset criterion in the stated finite-storage model.

## Limitations

The theorem requires independent stores, a common power, no recharge over the observation interval and exact differential slopes. It does not infer the number of stores from noisy field data or identify parameters from finite-window regressions. Bibliographic priority is not inferred from a shared publication date for analogous indexed results.

## References

1. M. Newman (1959), *Kantorovich’s Inequality*, J. Res. Natl. Bur. Standards B 64B(1), Eq. (1), [open PDF](https://nvlpubs.nist.gov/nistpubs/jres/64B/jresv64Bn1p33_A1b.pdf).
2. H. Wittenberg (1999), *Baseflow recession and recharge as nonlinear storage processes*, Hydrological Processes 13, 715–726, [DOI](https://doi.org/10.1002/(SICI)1099-1085(19990415)13:5%3C715::AID-HYP775%3E3.0.CO;2-N).
3. E. R. Jachens, D. E. Rupp, C. Roques and J. S. Selker (2020), *Recession analysis revisited: impacts of climate on parameter estimation*, Hydrol. Earth Syst. Sci. 24, 1159–1170, [DOI](https://doi.org/10.5194/hess-24-1159-2020), §3.2.2.
4. H. K. McMillan et al. (2011), *Hydrological field data from a modeller's perspective: Part 1. Diagnostic tests for model structure*, Hydrol. Process. 25, 511–522, [author manuscript](https://www.hilandtom.com/hilarymcmillan/McMillanClark_ModelStructure_1_Proof.pdf).
5. *Arbitrarily many separated recession-exponent peaks from positive linear reservoirs*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-arbitrarily-many-separated-recession-exponent-peaks-from-positiv--0c7b5b64c16a).
6. *Superposed inverse-time creep modes create false acceleration exponents and late failure forecasts*, [Resultary](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-superposed-inverse-time-creep-modes-create-false-acceleration-ex--3c3c5bc7cc44).
