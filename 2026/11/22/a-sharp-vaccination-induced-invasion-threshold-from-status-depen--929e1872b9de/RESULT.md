# A sharp vaccination-induced invasion threshold from status-dependent travel

## Finding

For the resident–traveller SVIRS framework of Arino and van den Driessche, **birth vaccination is guaranteed not to increase the vaccination reproduction number whenever susceptible and vaccinated residents have the same mobility generator**, with all other parameters fixed. This holds for any finite number of residence patches, heterogeneous vaccine efficacy and contacts, arbitrary fixed infectious mobility, and independent nonnegative ongoing-vaccination rates.

When those two mobility generators differ, the conclusion can reverse even though the vaccine strictly reduces susceptibility. An explicit two-residence, two-destination model with all directed travel rates and all transmission coefficients strictly positive, vaccine efficacy exactly one half, and no immunity waning or ongoing vaccination has one and only one vaccination-at-birth threshold \(t_*\in(0,1)\):

\[
\mathcal R_v(t)<1\quad (0\le t<t_*),\qquad
\mathcal R_v(t_*)=1,\qquad
\mathcal R_v(t)>1\quad(t_*<t<1).
\]

Here \(t_*\) is the unique root in \((0,1)\) of

\[
P(t)=2448016069t^3-1215675371t^2-6337116745t+2889002747,
\]

with \(9/20<t_*<23/50\) (numerically \(t_*\approx0.452391194675\)). Thus introducing vaccination at birth can change a linearly stable disease-free equilibrium into an unstable one in this *status-dependent travel* model, notwithstanding a 50% reduction in susceptibility per vaccinated individual. This is a mathematical model counterexample, not an empirical claim that vaccination causes outbreaks.

## Assumptions and scope

Let residence and current physical location both range over \(\{1,2}\}\). The ordering of state vectors is \((11,12,21,22)\) (residence first, location second). The source's movement generators act on column population vectors; define

\[
M(a,b)=\begin{pmatrix}-a&b\\a&-b\end{pmatrix}.
\]

The birth rate is \(b_{11}=b_{22}=1\) (other birth entries zero); death and recovery rates in all four subpopulations are \(d=\gamma=1\). No susceptible-to-vaccinated conversion after birth (\(\Phi=0\)); no vaccine waning; vaccine relative susceptibility \(\pi_{ij}=1/2\). Birth vaccination has \(p_{11}=t\in[0,1)\) and \(p_{22}=0\). All movement rates are strictly positive in both directions:

\[
M_1^S=M(1/10,2),\qquad
M_1^V=M_1^I=M_2^S=M_2^V=M_2^I=M(2,1/10).
\]

Recovered mobility can be \(M(2,1/10)\) for both residence groups; it does not change the disease-free threshold. At every residence–infector–location triple take \(\beta_{ikj}=1/20\), except \(\beta_{112}=16\). Here \(i\) is the susceptible recipient's residence, \(k\) the infective individual's residence, and \(j\) the physical transmission location. Every transmission coefficient is positive; the resident–traveller next-generation matrix is nonnegative and irreducible for \(0\le t<1\).

The general monotonicity result concerns the same SVIRS model for any finite \(n\), with nonnegative birth vaccinations \(P_i\), nonnegative ongoing-vaccination matrices \(\Phi_i\), fixed death, recovery, transmission and movement parameters, fixed \(0\le\pi_{ij}\le1\), and **\(M_i^S=M_i^V\)** for each resident group. No assumption about equality with infected mobility \(M_i^I\) is needed. Comparisons raise arbitrary components of \(P\) and/or \(\Phi\), remaining within their admissible parameter ranges.

## Proof

**Monotonicity with equal susceptible/vaccinated mobility.** Let \(M_i=M_i^S=M_i^V\) and \(D_i=\operatorname{diag}(d_{ij})\). The disease-free populations satisfy

\[
N_i^*=(D_i-M_i)^{-1}b_i,\quad
S_i^*=(D_i+\Phi_i-M_i)^{-1}(I-P_i)b_i,\quad V_i^*=N_i^*-S_i^*.
\]

The first expression is independent of vaccination. For larger \(P_i'\ge P_i\) and \(\Phi_i'\ge\Phi_i\), write \(A_i'=D_i+\Phi_i'-M_i\). Comparing the two susceptible equations gives

\[
A_i'(S_i^*-S_i^{*\prime})=(P_i'-P_i)b_i+(\Phi_i'-\Phi_i)S_i^*\ge0.
\]

The inverse of each \(A_i'\) is nonnegative, hence \(S_i^{*\prime}\le S_i^*\) entrywise. Each effective susceptible count is \(S_{ij}^*+\pi_{ij}V_{ij}^*=\pi_{ij}N_{ij}^*+(1-\pi_{ij})S_{ij}^*\). It does not increase. Physical-location denominators \(N_j^{p*}=\sum_iN_{ij}^*\) and the infectious transition matrix \(W\) do not change. Thus \(F'\le F\), so Perron monotonicity gives \(\rho(F'W^{-1})\le\rho(FW^{-1})\).

**Exact two-patch disease-free state.** Direct inversion of the two mobility–death matrices yields

\[
S_1^*=\frac{1-t}{31}\binom{30}{1},\qquad
V_1^*=\frac{t}{31}\binom{11}{20},\qquad
S_2^*=\frac1{31}\binom{1}{30},\quad V_2^*=0.
\]

Consequently, \(N_1^{p*}=(31-19t)/31\), \(N_2^{p*}=(31+19t)/31\) and

\[
W=\operatorname{diag}(B,B),\qquad B=\begin{pmatrix}4&-1/10\\-2&21/10\end{pmatrix},\quad
B^{-1}=\begin{pmatrix}21/82&1/82\\10/41&20/41\end{pmatrix}.
\]

Writing \(a(t)=(60-49t)/(40(31-19t))\), \(c(t)=1/[20(31-19t)]\), \(d(t)=3/[2(31+19t)]\), and \(q(t)=(1+9t)/(31+19t)\), the infection matrix is

\[
F(t)=\begin{pmatrix}
 a&0&a&0\\
 0&16q&0&q/20\\
 c&0&c&0\\
 0&d&0&d
\end{pmatrix}.
\]

**Exact threshold and uniqueness.** Replace the exceptional coefficient 16 temporarily by \(\varepsilon=1/20\) and call the resulting infection matrix \(F_0(t)\). Every row of \(F_0\) has at most two positive entries, each at most \(1/20\). The largest row sum of \(W^{-1}\) is \(30/41\); therefore \(\lVert F_0W^{-1}\rVert_\infty\le3/41<1\) for every \(0\le t<1\). Thus \(A(t)=W-F_0(t)\) is a nonsingular \(M\)-matrix with \(A^{-1}\ge0\) and \(\det A>0\).

The exceptional contact changes one entry: \(W-F=A-(319/20)q(t)e_2e_2^T\), with \(e_2=(0,1,0,0)^T\). The determinant lemma and the rank-one nonnegative perturbation criterion show

\[
\mathcal R_v(t)\lessgtr1\quad\Longleftrightarrow\quad
1-\frac{319}{20}q(t)(A^{-1})_{22}\gtrless0
\quad\Longleftrightarrow\quad\det(W-F(t))\gtrless0.
\]

An exact determinant expansion (reproduced in \(verify.py\)) gives

\[
\det(W-F(t))=\frac{P(t)}{2000(31-19t)(31+19t)^2}.
\]

The denominator is positive throughout the admissible domain. The derivative

\[
P'(t)=7344048207t^2-2431350742t-6337116745
\]

is strictly negative on \([0,1]\): it is convex as a function of \(t\), with negative values at both endpoints, \(P'(0)=-6337116745\), \(P'(1)=-1424419280\). Also \(P(9/20)=113611307281/8000>0\) and \(P(23/50)=-5628471513927/125000<0\). There is therefore precisely one simple zero in \((0,1)\), with the asserted strict threshold on both sides. At the zero the positive irreducible next-generation matrix has Perron root exactly one. This completes the classification.

## Verification

The included \(verify.py\) reconstructs \(S_i^*,V_i^*\), \(F\) and \(W\) directly from the stated rates using exact rational arithmetic and checks the full rational-function identity for the determinant, the hotspot coefficient, the strict derivative signs and rational interval bounds. Run: `python verify.py` (requires Python 3 and SymPy). The proof itself uses exact algebra and the standard nonnegative matrix rank-one threshold lemma, not numerical sampling. The decimal root is illustrative only.

## Relationship to prior work

Arino and van den Driessche (2026) supply the resident–traveller SVIRS model, its disease-free equilibrium equations and next-generation operator; these are assumed, not newly claimed. Their reported numerical investigation keeps susceptible and vaccinated mobility equal (though infected movement may differ) and does not establish the mobility-status monotonicity boundary or the exact counterexample above. The general possibility that changes in vaccinated people's contacts or travel can offset protection is recognized in prior vaccination-behavior literature; that qualitative idea is not new. The contribution assessed here is the theorem for this specific resident–traveller system and its exact all-positive two-patch, one-crossover certificate.

Lachiany and Stone (2012) analyze an earlier mover–stayer vaccination model, and Lachiany (2016) studies a different SIS vaccination diffusion model; no claim is made that mobility/vaccination interaction in general was first observed here. The complete 2012 article was not accessible for a full-text priority comparison; this residual limitation remains material.

## Limitations

The counterexample deliberately ties vaccination status to substantially different movement habits; holding habits fixed makes vaccination non-increasing in the model's reproduction number. It does not support withholding vaccination or imply empirical vaccine harm. It proves a linearized reproduction-number crossover, not a global nonlinear disease-outcome classification derived here. No measurements, fitting, stochastic extinction rates, or independent expert validation are provided. The exact cubic pertains to the specified witness, not arbitrary parameters. Prior-literature originality is bounded by accessible source material.

## References

1. J. Arino and P. van den Driessche, *A resident-traveller model for global aspects of vaccination*, arXiv:2611.01555v1, 1 November 2026, https://arxiv.org/html/2611.01555v1 (Sections 3.1–3.3; numerical setup in Section 4).
2. M. Lachiany and L. Stone, *A Vaccination Model for a Multi-City System*, Bulletin of Mathematical Biology 74 (2012), 2474–2487, https://doi.org/10.1007/s11538-012-9762-9.
3. M. Lachiany, *Modeling vaccination in a heterogeneous metapopulation system*, Physica A 458 (2016), 43–51, https://doi.org/10.1016/j.physa.2016.03.049.
4. *Impact of Immediate and Preferential Relaxation of Social and Travel Restrictions for Vaccinated People on the Spreading Dynamics of COVID-19: a Model-Based Analysis*, medRxiv (2021), https://www.medrxiv.org/content/10.1101/2021.01.19.21250100v1.full.
5. *The minimal COVID-19 vaccination coverage and efficacy to compensate for a potential increase of transmission contacts*, BMC Public Health (2022), https://pmc.ncbi.nlm.nih.gov/articles/PMC9235129/.
