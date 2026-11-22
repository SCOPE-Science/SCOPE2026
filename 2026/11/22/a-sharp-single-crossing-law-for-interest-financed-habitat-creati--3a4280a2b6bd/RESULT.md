# A sharp single-crossing law for interest-financed habitat creation under colonization and extinction

## Finding

Fix a terminal census time \(H>0\), a baseline colonization rate \(a>0\), a local extinction rate \(\mu>0\), and a nonnegative investment appreciation rate \(r\geq0\). A single initially absent habitat patch may be created once at a deterministic date \(s\in[0,H]\). Waiting increases its post-creation colonization rate to \(q(s)=a e^{rs}\), held constant after creation. Its occupancy immediately upon creation is zero. Thereafter, independent exponential transitions from empty to occupied have rate \(q(s)\), and occupied to empty have rate \(\mu\). The objective is the occupancy probability at census \(H\).

Define for \(q>0\) and \(t\geq0\)
\[
\mathcal B(q,\mu,t)=t+\frac{\mu\bigl(e^{(q+\mu)t}-1-(q+\mu)t\bigr)}{(q+\mu)^2},
\qquad r_c=\frac{1}{\mathcal B(a,\mu,H)}.
\]
Then the globally optimal creation date is **unique** for every admissible parameter choice. If \(0\leq r\leq r_c\), it is exactly \(s_*=0\). If \(r>r_c\), it is the unique \(s_*\in(0,H)\) satisfying
\[
 r\mathcal B\bigl(a e^{rs_*},\mu,H-s_*\bigr)=1.
\]
In particular, \(0<r_c<1/H\). The critical appreciation rate is strictly decreasing separately in \(a\), \(\mu\), and \(H\) (other inputs held fixed). Hence local extinction can make delayed creation optimal even when \(rH<1\); with zero extinction the corresponding immediate-versus-delay threshold is \(rH=1\).

## Assumptions and scope

The patch does not exist before \(s\), and is empty when created. The landscape supplying colonists is externally maintained; no feedback, finite-source depletion, or effect of the target patch on colonization is included. Investment before \(s\) appreciates exponentially and translates linearly into the single post-creation colonization rate \(a e^{rs}\). After creation the rate is fixed, not continuously reinvested. Local extinction is memoryless with a constant rate and is followed by possible recolonization. One creation date is chosen in advance, no reallocation or subsequent intervention is permitted. All times are continuous, and the objective is a single terminal occupancy probability, not mean persistence, regional occupancy, cost-adjusted value, or cumulative occupancy.

## Proof

**Step 1: Exact terminal probability.** For a chosen \(s\), put \(q=a e^{rs}\), \(t=H-s\), and \(y=q+\mu\). The Kolmogorov equation for occupied probability \(P(u)\) after construction is
\[
 P'(u)=q(1-P(u))-\mu P(u),\qquad P(0)=0.
\]
Its solution is \(P(u)=\frac{q}{q+\mu}(1-e^{-(q+\mu)u})\), so
\[
 F(s):=\Pr\{\text{occupied at }H\}
 =\frac{q}{y}(1-e^{-yt}).
\]
In particular, \(F(0)>0\), \(F(H)=0\), and \(F\) is continuously differentiable on \([0,H]\).

**Step 2: Derivative and threshold.** Differentiating the two-argument function \(P(q,t)\) gives
\[
 P_q=\frac{\mu}{y^2}(1-e^{-yt})+\frac{qt}{y}e^{-yt},
\qquad P_t=q e^{-yt}.
\]
Since \(q'(s)=rq\), \(t'(s)=-1\), it follows that
\[
 F'(s)=q e^{-yt}\left[r\left(\frac{\mu(e^{yt}-1)}{y^2}+\frac{qt}{y}\right)-1\right]
 =q e^{-yt}\bigl(r\mathcal B(q,\mu,t)-1\bigr).
\]
Thus the derivative's sign is that of \(G(s)=r\mathcal B(ae^{rs},\mu,H-s)-1\), with \(G(H)=-1\) and \(G(0)=r/r_c-1\).

**Step 3: Every interior root crosses strictly downward.** For \(q,\mu,t>0\), differentiation yields
\[
 \mathcal B_t=\frac{q+\mu e^{yt}}{y},\qquad
 \mathcal B_q=\frac{\mu\bigl((yt-2)e^{yt}+2+yt\bigr)}{y^3}.
\]
Set \(x=yt\), \(\theta=q/y\) and \(\phi=\mu/y\), so \(\theta,\phi>0\) and \(\theta+\phi=1\). Direct expansion gives the exact identity
\[
 \mathcal B_t\mathcal B-q\mathcal B_q
 =\frac{\phi^2e^x(e^x-1)+\theta\phi[3(e^x-1)-x]+\theta^2x}{y}>0.
\]
The strict positivity follows from \(x>0\), \(e^x-1>x\), and positive coefficients. At any interior root \(G(s)=0\), substitute \(r=1/\mathcal B\) into the chain rule to obtain
\[
 G'(s)=r\bigl(rq\mathcal B_q-\mathcal B_t\bigr)
 =-\frac{r}{\mathcal B}(\mathcal B_t\mathcal B-q\mathcal B_q)<0.
\]
Consequently **every** interior zero crosses from positive to negative. There cannot be two distinct zeros: after a downward crossing, a later downward crossing would require an intervening zero where the sign crosses upward or otherwise fails to cross downward, contradicting the established strict derivative at every zero. When \(G(0)\leq0\), \(G(s)<0\) for all \(s>0\): this includes equality, since the same identity makes the derivative at \(s=0\) strictly negative for \(r=r_c>0\). Thus \(F\) is strictly decreasing after an initial endpoint maximum. When \(G(0)>0\), continuity and \(G(H)=-1\) imply one root in \((0,H)\), and the signs on either side make it the unique global maximum.

**Step 4: Critical-rate comparisons.** The exact integral identity
\[
 \mathcal B(q,\mu,t)=t+\mu\int_0^t(t-u)e^{(q+\mu)u}\,du
\]
holds for every \(t\geq0\). For strictly positive \(q,\mu,t\), the integral is positive, giving \(\mathcal B>t\) and hence \(r_c<1/H\). The integral is strictly increasing with \(q\), \(\mu\), and \(t>0\); in the \(\mu\) case both its prefactor and integrand increase. Thus \(r_c\) decreases in \(a\), \(\mu\), and \(H\). At \(\mu=0\), the limiting formula becomes \(\mathcal B=t\); therefore \(r_c=1/H\), and direct maximization of \(a e^{rs}(H-s)\) gives \(s_*=\max\{0,H-1/r\}\) for \(r>0\). This last boundary case is stated only as a comparison; the principal classification assumes \(\mu>0\).

## Verification

The proof needs no numerical root enumeration. A standalone standard-library checker, `check.py`, verifies the exact determinant identity independently of the derivative implementation on multiple positive parameter sets; tests the sign-predicted optimizer against a dense grid; and compares the closed-form occupancy formula with a separately integrated Kolmogorov ODE. Run `python check.py` in the directory containing the two files. Finite tests are supplementary and are not treated as evidence for the universal quantifiers.

For a concrete example choose \(a=\mu=H=r=1\). Then the threshold is exactly \(r_c=4/(e^2+1)=0.4768116880\ldots\). The unique maximizer satisfies \(s_*=0.3640459757\ldots\), with \(F(s_*)=0.4649368812\ldots\) versus \(F(0)=(1-e^{-2})/2=0.4323323584\ldots\). Here \(rH=1\) but delayed creation is strictly better because \(\mu>0\).

## Relationship to prior work

Westphal, Pickett, Getz and Possingham (2003) formulate discrete-time stochastic landscape reconstruction with state-dependent decisions, and Thomson and collaborators (2009) analyze spatially structured multi-species revegetation schedules. Neither inspected formulation gives this single-patch, one-time investment/colonization-rate objective or its universal one-crossing threshold. Iacona, Possingham and Bode (2017) prove an analytic timing formula for conservation spending, but for a deterministic species-area/extinction-debt objective, not a recolonizing two-state patch with fixed terminal occupancy. Southwell, Heard and McCarthy (2017 online; 2018 journal) treat interest-financed delayed habitat compensation in a spatially explicit metapopulation by stochastic dynamic programming; the accessible abstract is closely relevant, but a primary full-text comparison was unavailable and priority over their model is not established. This result is an exact theorem for the explicitly restricted two-state model, not a claim of general superiority over spatial conservation optimization methods.

## Limitations

The exogenous constant source, linear link between investment and colonization, fixed post-creation transition rates, lack of extinction before creation, and single terminal reward are strong idealizations. No result is claimed for extinction rates that depend on patch area, coupled multi-patch recolonization, time-varying hazards, a stochastic investment process, or feedback between creation and source survival. Later intervention is not categorically recommended in practice. Historical priority remains provisional because the full primary paper of Southwell and colleagues could not be examined and because broad investment-timing and finite-horizon Markov decision theory may cover special cases.

## References

- Westphal, M. I., M. Pickett, W. M. Getz, and H. P. Possingham (2003). “The Use of Stochastic Dynamic Programming in Optimal Landscape Reconstruction for Metapopulations.” *Ecological Applications* 13(2), 543–555. DOI: 10.1890/1051-0761(2003)013[0543:TUOSDP]2.0.CO;2. First public online date: 2003-04-01.
- Thomson, J. R., A. J. Moilanen, P. A. Vesk, A. F. Bennett, and R. Mac Nally (2009). “Where and When to Revegetate: A Quantitative Method for Scheduling Landscape Reconstruction.” *Ecological Applications* 19(4), 817–828. DOI: 10.1890/08-0915.1. First online: 2009-06-01; full open manuscript: https://scispace.com/pdf/where-and-when-to-revegetate-a-quantitative-method-for-1ypjlxiftw.pdf.
- Iacona, G. D., H. P. Possingham, and M. Bode (2017). “Waiting Can Be an Optimal Conservation Strategy, Even in a Crisis Discipline.” *PNAS* 114(39), 10497–10502. DOI: 10.1073/pnas.1702111114; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5625895/.
- Southwell, D. M., G. W. Heard, and M. A. McCarthy (2018). “Optimal Timing of Biodiversity Offsetting for Metapopulations.” *Ecological Applications* 28(2), 508–521. DOI: 10.1002/eap.1666. First public online: 2017-12-20; primary full text not accessible in this examination.
