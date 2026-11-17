# Bounded reset discrepancy and identifiable stationary risk law in a discontinuous hysteresis map

## Finding

Consider the two-dimensional risk-reset map in the cited model,
\[
F_{a,b}(x,s)=(x',s'),\qquad x'=-a x+(b+a)s,\qquad
s'=\begin{cases}s+x'-x,&|s+x'-x|\leq1,\\0,&|s+x'-x|>1.\end{cases}
\]
For every \(0<a<1\), \(b>1\), and \(a(b+1)>1\), define
\[
c=(1+a)b+a,\quad \ell=\log(1/a),\quad h=\log c,\quad K=h+2\ell,\quad
\nu_0=\frac{a}{1+a},\quad q_0=\frac1{1+a},\quad U=\frac{c}{1+a}.
\]
There is an explicitly specified, non-atomic, \(F_{a,b}\)-invariant probability \(\mathcal M_{a,b}\), supported on four straight rays (two signed section pieces and two signed intermediate pieces), with **signed risk-coordinate marginal**
\[
\boxed{(s)_*\mathcal M_{a,b}=\frac{h+\ell}{K}\,\delta_0
+\frac{\mathbf 1_{\{a<|t|<1\}}}{2K|t|}\,dt.}
\]
Here \(dt\) is Lebesgue measure on the risk coordinate. Equivalently, the reset-state frequency is \((h+\ell)/K\), and conditional on a nonzero risk, its magnitude is log-uniform on \((a,1)\), with equiprobable signs. In particular,
\[
\mathbb E_{\mathcal M}|s|=\frac{1-a}{K},\qquad
\mathbb E_{\mathcal M}s=0,\qquad
\mathbb E_{\mathcal M}s^2=\frac{1-a^2}{2K}.
\]
**Uniform reset-count discrepancy in actual time.** Fix either sign and an initial section point \((\sigma x,0)\) with \(\nu_0<x<U\) whose return orbit never lands exactly on a branch boundary. For every integer \(n\geq1\), with \(Z_n=\sum_{t=0}^{n-1}\mathbf1_{\{s_t=0\}}\), the original two-dimensional orbit satisfies the *non-asymptotic* bound
\[
\boxed{\left|Z_n-n\frac{h+\ell}{K}\right|<1.}
\]
The bound holds whether the induced rotation number is rational or irrational: the observed reset density is exactly controlled even when the full stationary risk law is not a typical-orbit limit. This is stronger than almost-sure frequency convergence and rules out growing reset-count fluctuations on the invariant two-level core.

The **one-coordinate stationary marginal determines both original parameters**. Namely, writing \(p_0=\Pr_{\mathcal M}(s=0)\), the lower endpoint \(a\) of the support of the nonzero risk magnitude gives the first parameter, and
\[
\boxed{K=\frac{\log(1/a)}{1-p_0},\qquad
b=\frac{\exp(K-2\log(1/a))-a}{1+a}.}
\]
If \(h/(h+\ell)\) is irrational, \(\mathcal M_{a,b}\) is ergodic. For almost every signed section point \((x,0)\) with \(a/(1+a)<|x|<c/(1+a)\), the empirical distribution of the risk variable converges weakly to this law in **original iteration time**, not just in return time. No statement of uniqueness among all invariant probabilities is made: the map also has an equilibrium segment.

For the exact example \(a=1/2\), \(b=5/3\), the return rotation has irrational ratio \(\log3/\log6\) and the formula reduces to
\[
(s)_*\mathcal M=\frac{\log6}{\log12}\delta_0
+\frac{\mathbf1_{\{1/2<|t|<1\}}}{2\log12\,|t|}\,dt.
\]

## Assumptions and scope

The phase space is \(\mathbb R\times[-1,1]\). The map uses **reset to zero** when the tentative risk leaves \([-1,1]\), not the continuous saturation-at-\(\pm1\) stop operator. The parameter region \(a(b+1)>1\) is precisely the two-branch return regime of the cited discontinuous model, expressed in the positive parameter \(a=-\lambda\), with \(b=\beta\). All equalities of measures ignore finite or countable boundary sets of measure zero. The result concerns the explicitly constructed non-equilibrium invariant probability, rather than every initial point or every invariant measure.

## Proof

**1. Return-time geometry.** On the risk-zero section, start from \((\sigma x,0)\) with \(\sigma\in\{+1,-1\}\) and \(\nu_0\leq x\leq U\). Direct substitution gives, when \(\nu_0\leq x\leq q_0\),
\[
F_{a,b}(\sigma x,0)=(-\sigma ax,-\sigma(1+a)x),\qquad
F_{a,b}^{2}(\sigma x,0)=(-\sigma cx,0).
\]
The first tentative risk is within \([-1,1]\), while the second is strictly outside it, except for inconsequential boundary conventions. For \(q_0<x\leq U\), the first tentative risk lies outside \([-1,1]\), hence
\[
F_{a,b}(\sigma x,0)=(-\sigma ax,0).
\]
Thus the section return time is two on the lower interval and one on the upper. Every return reverses the sign. The absolute return map is
\[
T(x)=\begin{cases}cx,&\nu_0\leq x\leq q_0,\\ax,&q_0<x\leq U.\end{cases}
\]
The identities \(cq_0=U\), \(c\nu_0=aU\), and \(aq_0=\nu_0\) show that the branch images \([aU,U]\) and \((\nu_0,aU]\) tile the section up to endpoints.

**2. Logarithmic base measure.** Put \(y=\log x\). The two branches translate \(y\) by \(h=\log c\) and \(-\ell=\log a\), respectively, on a circle of length \(H=h+\ell\). The resulting map is rotation by \(h\) modulo \(H\). Hence the probability \(dx/(Hx)\) on \([\nu_0,U]\) is invariant under the absolute return map. The sign-reversing extension has invariant probability \(\frac12\sum_{\sigma=\pm1}\delta_\sigma\otimes dx/(Hx)\). It is ergodic if \(h/H\notin\mathbb Q\): its square restricts to the irrational rotation by \(2h\) on each sheet, and one return interchanges the sheets.

**3. Lift to actual iteration time.** The average number of original iterations per section return is
\[
\bar r=\frac{2\ell+h}{H}=\frac K H.
\]
For a bounded Borel test function \(\varphi\), define the stationary probability directly by
\[
\int\varphi\,d\mathcal M_{a,b}=
\frac1{2K}\sum_{\sigma=\pm1}\left[
\int_{\nu_0}^{U}\varphi(\sigma x,0)\frac{dx}{x}
+\int_{\nu_0}^{q_0}\varphi(-\sigma ax,-\sigma(1+a)x)\frac{dx}{x}
\right].
\]
Its total mass is \((H+\ell)/K=1\). This is an explicit two-level return tower. For invariance, apply \(F_{a,b}\) to each integrand: the lower base segment becomes the intermediate segment; the upper base and the intermediate segment become signed base segments with absolute coordinates \(ax\in(\nu_0,aU]\) and \(cx\in[aU,U]\), respectively. These two image ranges partition the full base interval, and the substitutions preserve \(dx/x\). Hence \((F_{a,b})_*\mathcal M_{a,b}=\mathcal M_{a,b}\).

**4. Risk law and identification.** The base segment contributes an atom of mass \(H/K\) at risk zero. On intermediate segments, \(|s|=(1+a)x\); therefore \(|s|\) ranges through \((a,1)\) and \(dx/x=d|s|/|s|\). The two sign sheets give precisely the stated density \(1/(2K|s|)\). Integrating \(|s|\) and \(s^2\) yields the moments. The nonzero support begins at \(a\), and the atom has weight \(p_0=1-\ell/K\); solving these two identities recovers \(K\), \(c=\exp(K-2\ell)\), and \(b=(c-a)/(1+a)\).

**5. Exact bounded reset discrepancy.** Normalize logarithmic section coordinates by \(u=(\log x-\log\nu_0)/H\in[0,1)\), put \(\theta=h/H\in(0,1)\), and write \(u_j=\{u_0+j\theta\}\). Away from branch boundaries, the one-step return branch occurs precisely when \(u_j\geq1-\theta=\ell/H\); its indicator is \(v_j=\lfloor u_j+\theta\rfloor\). Since \(u_{j+1}=u_j+\theta-v_j\), telescoping gives \(\sum_{j=0}^{m-1}v_j=\lfloor u_0+m\theta\rfloor\). The physical time of the \(m\)-th return to risk zero is consequently
\[
\tau_m=\sum_{j=0}^{m-1}(2-v_j)=2m-\lfloor u_0+m\theta\rfloor
=m\frac{K}{H}+u_m-u_0.
\]
At an original-time index \(n=\tau_m\), exactly \(m\) earlier iterates have risk zero, and \(|m-nH/K|=|u_m-u_0|H/K<1\). The only possible index strictly between consecutive return times is \(n=\tau_m+1\), when the current roof has height two. Then exactly \(m+1\) earlier iterates have risk zero, and
\[
Z_n-n\frac H K=1-\frac{1+u_m-u_0}{K/H}.
\]
Since \(0<1+u_m-u_0<2\) and \(1<K/H<2\), this difference belongs to \((-1,1)\). Every integer time is one of these two cases, proving the uniform estimate without an irrationality assumption.

**6. Original-time typicality.** If \(h/H\) is irrational, the sign-reversing return system in step 2 is ergodic. Birkhoff's theorem for the return map and the return-time ratio formula (or the corresponding finite-height tower) give, for \(\mathcal M_{a,b}\)-almost every orbit, its empirical law in actual iterations. For section points this holds for \(dx/x\)-almost all \(x\), and hence for Lebesgue-almost all \(x\) in the stated interval. For \(a=1/2\) and \(b=5/3\), \(c=3\), \(H=\log6\). The ratio \(\log3/\log6\) is irrational: otherwise positive integers would satisfy \(3^m=6^n\), contradicting the prime factor \(2\).

## Verification

The standalone `check.py` included with this result checks the section-return branch identities exactly using rational arithmetic for four parameter pairs and over one thousand rational test inputs per pair. It independently tests normalization, the moment and parameter-inversion identities, the bound on full-time reset-count discrepancy, stationary-integral invariance against three polynomial observables, and original-map time averages for the explicit irrational-rotation example (150,000 iterations). The checker was run from its actual packaged location. Finite computations are checks, not the continuum proof.

## Relationship to prior work

Kryzhevich, Avrutin, Begun, Rachinskii and Tajbakhsh (2021, arXiv:2104.11825) introduced and studied the discontinuous risk-reset map. In their Section 8, formulas for the return thresholds and branch slopes, together with a logarithmic conjugacy to an interval translation, yield the two-branch circle-rotation regime. Their Theorem 3 establishes existence of a non-atomic invariant measure but does not state the **bounded original-time reset-count discrepancy**, the **physical-iteration-time marginal of risk**, its explicit atom-plus-logarithmic density, or recovery of both parameters from this one observable. The present computation uses their geometry but explicitly incorporates variable return times and the sign-reversing lift. The general idea of lifting invariant measures along induced maps is classical; that method is not claimed as novel. Arnold and coauthors (2016, arXiv:1605.00584) analyze a distinct continuous saturation-at-\(\pm1\) stop operator, not the zero-reset system treated here.

## Limitations

The exact reset-count bound concerns section orbits on the specified two-level core, excluding boundary hits; the risk-distribution formula is a law for one explicitly specified invariant measure on a two-level invariant set; it does not claim global attraction, uniqueness of invariant probability, or identifiability from arbitrary invariant measures. For rational return-rotation ratios, the constructed probability is still invariant, but its pathwise ergodic conclusion does not follow and periodic-orbit measures may differ. The zero-reset discontinuity and endpoints are interpreted modulo null sets. A general-purpose inducing principle underlies the proof, and an unlocated prior calculation of the same specific risk distribution remains a publication-priority risk. Independent external validation is not included.

## References

1. S. Kryzhevich, V. Avrutin, N. Begun, D. Rachinskii and K. Tajbakhsh, *Dynamics of Systems with a Discontinuous Hysteresis Operator and Interval Translation Maps*, Axioms **10** (2021), 80; arXiv:2104.11825v1 (public April 23, 2021), https://arxiv.org/abs/2104.11825, https://doi.org/10.3390/axioms10020080. Especially Sections 7–8 and Theorem 3.
2. M. Arnold, N. Begun, P. Gurevich, E. Kwame, H. Lamba and D. Rachinskii, *Dynamics of Discrete Time Systems with a Hysteresis Stop Operator*, SIAM Journal on Applied Dynamical Systems **16** (2017), 91–119; arXiv:1605.00584, https://arxiv.org/abs/1605.00584. Different continuous saturation model.
