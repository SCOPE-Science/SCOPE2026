# A unique household-assortativity crossover under opposing transmission traits

## Finding

For every real susceptibility–infectivity contrast \(r>1\), between-household transmission multiplier \(\sigma>0\), and within-household transmission intensity \(\tau>0\), compare two populations with the same numbers of two individual types: one groups like types into two-person households and the other pairs unlike types. Under the SIR model specified below, their household reproduction numbers are exactly
\[
R_{\mathrm{same}}=\sigma r(2-e^{-r\tau}),\qquad
R_{\mathrm{mixed}}=\sigma\left[r+\frac{(1-e^{-r^2\tau})+r^2(1-e^{-\tau})}{2}\right].
\]
There is exactly one critical intensity \(\tau_c(r)>0\) such that
\[
R_{\mathrm{same}}>R_{\mathrm{mixed}}\quad(0<\tau<\tau_c(r)),\qquad
R_{\mathrm{same}}<R_{\mathrm{mixed}}\quad(\tau>\tau_c(r)).
\]
The unique crossing satisfies \(\tau_c(r)=-\log x_c(r)\), where \(x_c(r)\in(0,1)\) is the unique interior root of
\[
x^{r^2}-2rx^r+r^2x-(r-1)^2=0.
\]
The ordering reversal is universal for this naturally anti-correlated two-type family, not a selected numerical parameter anomaly. It can also reverse which household arrangement permits a major epidemic, as proved by exact rational witnesses below.

## Assumptions and scope

Each type constitutes half the individuals in a closed population with an even number of two-person households. Let the types be \(A,B\) with per-infective global activity \((b_A,b_B)=(r,1)\) and per-susceptible susceptibility \((k_A,k_B)=(1,r)\). All infectious periods equal one unit. A type-\(i\) infective makes independent Poisson contacts with any specified type-\(j\) individual in the population at rate \(\sigma b_i k_j/N\), and with its single household partner at rate \(\tau b_i k_j\). Contacts and infectious periods follow the household SIR specification of Ball and Critcher (2026); individuals are infected at most once. The comparison is between (i) equal numbers of \(AA\) and \(BB\) households and (ii) all \(AB\) households, with the type fractions, activity, susceptibility, global rate multiplier, and local rate multiplier held fixed. The household reproduction numbers are those of the large-household-count branching-process limit; they determine whether a major outbreak has positive limiting probability.

## Proof

Let \(x=e^{-\tau}\in(0,1)\). For a single directed local contact from type \(i\) to type \(j\), the probability of infecting the susceptible partner is \(1-e^{-\tau b_i k_j}\). The four possible exponents \(b_i k_j\), in row/column order \(A,B\), are \(r,r^2,1,r\).

In the normalized proportionate-global-mixing notation of Ball and Critcher's formula (4.1), the susceptibility factors are \(\kappa_A=2/(r+1)\), \(\kappa_B=2r/(r+1)\), and the global infectivity factors are \(\beta_A=\sigma r(r+1)/2\), \(\beta_B=\sigma(r+1)/2\). Since both types have population fraction \(1/2\), a typical *newly seeded household* is seeded by type \(A\) with probability \(P_A=1/(r+1)\) and by type \(B\) with probability \(P_B=r/(r+1)\). In particular, these are not the unweighted population frequencies.

For a homogeneous \(AA\) or \(BB\) household, the index infection generates one additional household infection with probability \(1-x^r\). The mean outgoing global contact rate summed over seeded household members, weighted by the seed distribution, is therefore
\[
R_{\mathrm{same}}=(P_A\beta_A+P_B\beta_B)(2-x^r)=\sigma r(2-x^r).
\]
For a mixed \(AB\) household, an \(A\) seed transmits locally to \(B\) with probability \(1-x^{r^2}\), whereas a \(B\) seed transmits to \(A\) with probability \(1-x\). Since \(P_A\beta_B=\sigma/2\) and \(P_B\beta_A=\sigma r^2/2\), the expected household offspring count is
\[
R_{\mathrm{mixed}}=\sigma r+\frac{\sigma}{2}\left[(1-x^{r^2})+r^2(1-x)\right].
\]
Consequently
\[
\frac{2}{\sigma}(R_{\mathrm{same}}-R_{\mathrm{mixed}})=F_r(x):=x^{r^2}-2rx^r+r^2x-(r-1)^2.
\]
Here \(F_r(0)=-(r-1)^2<0\), \(F_r(1)=0\), and
\[
F_r'(x)=r^2\left[1-2x^{r-1}+x^{r^2-1}\right]
=r^2 h_r(x^{r-1}),\quad h_r(y)=1-2y+y^{r+1}.
\]
The function \(h_r\) is strictly convex on \((0,1)\); it satisfies \(h_r(0)=1\), \(h_r(1)=0\), \(h_r'(0)=-2\), and \(h_r'(1)=r-1>0\). It is therefore negative just to the left of one, has exactly one root \(y_0\in(0,1)\), and is positive before that root and negative after it. Thus \(F_r\) first increases and then decreases strictly on \((0,1)\). Its maximum is strictly positive, because it decreases to \(F_r(1)=0\). Starting from a strictly negative value at zero, it consequently crosses zero exactly once at a point \(x_c(r)\in(0,1)\). Since \(x=e^{-\tau}\) decreases strictly, the asserted unique switch follows. The endpoint zero \(x=1\) corresponds to \(\tau=0\), excluded from the strict comparison. As \(\tau\to\infty\), the same-minus-mixed difference tends to \(-\sigma(r-1)^2/2\); at small positive \(\tau\) it is \(\sigma r^2(r-1)^2\tau^2/4+O(\tau^3)\).

For exact epidemic-threshold witnesses set \(r=4\), giving
\[
R_{\mathrm{same}}/\sigma=8-4x^4,\quad
R_{\mathrm{mixed}}/\sigma=\frac{25}{2}-8x-\frac{x^{16}}{2},\quad
F_4(x)=x^{16}-8x^4+16x-9.
\]
At \(x=3/4\) and \(\sigma=2/13\), direct rational arithmetic gives
\[
R_{\mathrm{same}}=\frac{431}{416}>1,
\qquad R_{\mathrm{mixed}}=1-\frac{(3/4)^{16}}{13}<1.
\]
At \(x=1/2\) and \(\sigma=1/8\), the opposite strict inequality is
\[
R_{\mathrm{same}}=\frac{31}{32}<1,
\qquad R_{\mathrm{mixed}}=\frac{17}{16}-2^{-20}>1.
\]
The branching-process threshold in Ball and Critcher, Sect. 4.2.1, therefore gives opposite major-outbreak possibility verdicts for the paired populations in each exact case. The two witness comparisons use separately specified global multipliers; the unique ranking crossover theorem itself holds at every *fixed* positive global multiplier.

## Verification

Run `python3 verification.py` in a Python 3 environment. The standard-library checker verifies the exact degree-sixteen factorization, rational threshold inequalities, symbolic witness identities, a rational bracket for the unique positive crossing, and supplementary numerical consistency tests for several contrasts. The general uniqueness proof is the convexity argument above; finite numerical checks do not establish it. For \(r=4\), the crossing is approximately \(x_c=0.6537751279\), or \(\tau_c=0.4249918278\).

## Relationship to prior work

Ball and Critcher (2026), Sect. 4.2.1, established the household reproduction formula and the large-population outbreak threshold, which are used as premises rather than claimed as new. The new contribution is a sharp, uniform-in-contrast comparison between two exact household pairings, with the unique switch and two opposite strict outbreak-threshold witnesses. Ball, Martin, Neal and Sirl (2026) consider a discrete-time household epidemic rather than this type-heterogeneous continuous-time comparison. Ball, Critcher, Neal and Sirl (2023) study household structure and herd immunity, not the present fixed-type household-pairing crossover. Earlier general household SIR results, including Ball and Lyne (2001), establish broad model frameworks; they may imply the starting reproduction formula but do not supply the convexity comparison as inspected here. A related 2026 published mathematical result on household matching was read in full. It fixes two distinct infectivity rates, equal global susceptibilities, and four local transmission probabilities while varying the fraction of mixed pairs; it proves that the household reproduction number can rise as major-outbreak probability falls. It neither varies a common within-household intensity nor gives the present universal, one-crossing pair-ranking theorem. The broader historical literature still leaves a priority risk.

## Limitations

The statement concerns the household-based reproduction quantity \(R_*\) and the existence of a possible major outbreak in the many-household limit. The numerical ordering of \(R_*\) alone does **not** establish an ordering of major-outbreak probabilities, attack rates, epidemic peaks, or individual-based reproduction numbers. It assumes deterministic infectious duration, Poisson contacts, fixed equal type frequencies, strict two-person households and the precise opposed activity/susceptibility pattern. It makes no empirical treatment or household policy recommendation. The claim is analytically checked and has not undergone independent scientific audit; prior-literature priority is not certified.

## References

1. F. Ball and L. Critcher, *Multitype SIR epidemics among a population partitioned into households with proportionate global mixing*, Journal of Mathematical Biology **92**, article 77 (published 26 April 2026), https://doi.org/10.1007/s00285-026-02359-5, especially Sect. 2 and Eq. (4.1).
2. F. Ball, N. Martin, P. Neal and D. Sirl, *Discrete-Time Household Epidemic Models*, Methodology and Computing in Applied Probability **28**, article 21 (2026), https://doi.org/10.1007/s11009-026-10253-2.
3. F. Ball, L. Critcher, P. Neal and D. Sirl, *The impact of household structure on disease-induced herd immunity*, Journal of Mathematical Biology **87**, article 83 (2023), https://doi.org/10.1007/s00285-023-02010-7.
4. F. Ball and O. Lyne, *Stochastic multitype SIR epidemics among a population partitioned into households*, Advances in Applied Probability (2001), https://doi.org/10.1017/S000186780001065X.
