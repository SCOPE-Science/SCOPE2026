# Directed-path amplification of final epidemic size by fatal removal at fixed infectious duration

## Finding

In a finite multigroup SIRD epidemic with source-population normalization, redirecting a fixed infectious exit rate from recovery toward death strictly increases the eventual fraction ever infected in **exactly** the groups reachable by a directed path of positive transmission rates from the affected source group. Neither the average infectious duration nor the next-generation reproduction threshold changes. The path criterion holds without an assumption of symmetry or irreducibility and distinguishes this mechanism from the classical fixed-population SIRD system, in which the same redistribution has no effect on infection dynamics.

For the model and assumptions below, put \(s_i=S_{i0}/N_{i0}\), \(q_i=\mu_i/k_i\), \(K_{ij}=\beta_{ij}/k_j\), and \(z_i=1-S_{i\infty}/N_{i0}\). Let \(h_i=\log(S_{i0}/S_{i\infty})\). Then the final-size vector \(h\) is uniquely determined by
\[
h_i=\sum_jK_{ij}\Phi_{q_j}(z_j),\qquad z_j=1-s_j e^{-h_j},\qquad
\Phi_q(z)=\int_0^z\frac{du}{1-qu}.
\]
The integral convention includes \(q=0\); for \(q>0\), \(\Phi_q(z)=-\log(1-qz)/q\).

Define the nonnegative matrix
\[
J_{ij}=K_{ij}\frac{1-z_j}{1-q_jz_j}
\]
and \(w_j=\int_0^{z_j}u(1-q_ju)^{-2}\,du>0\). At every admissible parameter point, \(\rho(J)<1\) and the **exact groupwise fatality sensitivity** is
\[
\boxed{\frac{\partial z_i}{\partial q_j}=(1-z_i)w_j\bigl[(I-J)^{-1}K\bigr]_{ij}.}
\]
For fixed \(i,j\), this derivative is strictly positive if and only if the directed graph with an edge \(j\to i\) whenever \(\beta_{ij}>0\) contains a directed positive-length path from \(j\) to \(i\). Otherwise it vanishes identically. Consequently, a strict increase in just one fatal-removal fraction produces strict increase in exactly the path-reachable groups' final infection fractions, while leaving other groups' final infection fractions unchanged. In a fully interacting model, **every** group is strictly affected by a change in **any** one group's fatal-removal fraction.

This is an exact comparative-statics statement about the specified deterministic equations, not an assertion that changing case fatality is a feasible clinical intervention or that its stochastic analog holds.

## Assumptions and scope

Fix an integer \(m\ge2\). For each group \(i=1,\ldots,m\), let \(S_i,I_i,R_i,D_i\) satisfy
\[
\dot S_i=-S_i\sum_j\beta_{ij}\frac{I_j}{N_j},\qquad
\dot I_i=S_i\sum_j\beta_{ij}\frac{I_j}{N_j}-k_iI_i,
\]
\[
\dot R_i=k_i(1-q_i)I_i,\qquad
\dot D_i=k_iq_i I_i,\qquad N_i=S_i+I_i+R_i.
\]
Here \(\beta_{ij}\ge0\), every row of \(\beta\) has at least one positive entry, \(k_i>0\), \(0\le q_i<1\), and initial states obey \(S_{i0}>0\), \(I_{i0}>0\), \(R_{i0}=D_{i0}=0\). In particular, \(N_{i0}=S_{i0}+I_{i0}\) and \(0<s_i<1\). Rates \(k_i\), \(\beta_{ij}\) and initial states are held fixed when comparing \(q\)-vectors. An edge \(j\to i\) means infection in source group \(j\) contributes directly to susceptible incidence in group \(i\). Paths must have positive length, so a source group influences its own final size through this mechanism if and only if its transmission network contains a directed cycle returning to it. The all-positive special case of \(\beta\) includes the original two-group model.

The disease-free next-generation matrix for the fully susceptible reference state with group sizes \(N_{i0}\) is \(\mathcal K_{ij}=\beta_{ij}N_{i0}/(k_jN_{j0})\). It is independent of \(q\). Likewise, the initially seeded effective reproduction matrix \(\beta_{ij}S_{i0}/(k_jN_{j0})\) is independent of \(q\). The expected duration of each infectious episode is exactly \(1/k_i\) for every \(q_i\).

## Proof

**1. Exact final-size reduction and positivity.** All compartments remain nonnegative, and \(S_i\) is decreasing. Each group's full population \(S_i+I_i+R_i+D_i=N_{i0}\) is conserved, while \(\dot N_i=-k_iq_iI_i\). For \(q_i<1\), since \(R_i(t)=(1-q_i)k_i\int_0^tI_i(v)\,dv\) and \(S_i\ge0\), the active population remains bounded below by a positive multiple of its initial size: \(N_i(t)\ge(1-q_i)N_{i0}\) follows from \(N_i(t)=N_{i0}-q_i k_i\int_0^t I_i\,dv\) and \(k_i\int_0^tI_i\,dv\le N_{i0}\). Hence \(S_i(t)\) never reaches zero and has a positive limiting value. Also \(k_i\int_0^\infty I_i(t)\,dt\le N_{i0}\). Bounded derivatives make \(I_i\) uniformly continuous, so \(I_i(t)\to0\).

Since \(R_{i0}=D_{i0}=0\), the number ever infected by time infinity, counting initial infectives, is \(N_{i0}-S_{i\infty}=k_i\int_0^\infty I_i(t)\,dt\). Thus \(N_{i\infty}=N_{i0}(1-q_iz_i)\). For \(q_i>0\), integrating \(\dot N_i/N_i=-k_iq_iI_i/N_i\) gives \(\int_0^\infty I_i/N_i\,dt=-\log(1-q_iz_i)/(k_iq_i)\). At \(q_i=0\), \(N_i=N_{i0}\) is constant and the same integral equals \(z_i/k_i\). Integrating \(\dot S_i/S_i=-\sum_j\beta_{ij}I_j/N_j\) gives the displayed final-size system for all \(0\le q_i<1\).

**2. Well-posedness and a strict spectral contraction at the physical fixed point.** Write \(g_{q,s}(h)=\Phi_q(1-se^{-h})\) and \(F_i(h)=\sum_jK_{ij}g_{q_j,s_j}(h_j)\) for \(h\ge0\). Direct differentiation gives
\[
\frac{d}{dh}g_{q,s}(h)=\frac{se^{-h}}{1-q(1-se^{-h})}>0,
\qquad
\frac{d^2}{dh^2}g_{q,s}(h)=-\frac{(1-q)se^{-h}}{[1-q(1-se^{-h})]^2}<0.
\]
Moreover \(g_{q,s}(0)=\Phi_q(1-s)>0\), and \(g_{q,s}\) is bounded by \(\Phi_q(1)<\infty\). Since each row of \(K\) has a positive entry, \(F(0)\gg0\). The increasing, continuous map \(F\) sends the nonnegative orthant into the compact order interval \([F(0),M]\), where \(M_i=\sum_jK_{ij}\Phi_{q_j}(1)>0\). Brouwer's theorem provides a fixed point \(h\gg0\).

For uniqueness, if \(h,v\gg0\) are distinct fixed points, exchange them if necessary and choose \(r=\max_i h_i/v_i>1\), attained at some coordinate. Concavity and \(F(0)\gg0\) imply \(F(rv)\le rF(v)-(r-1)F(0)\ll rv\), while monotonicity gives \(h=F(h)\le F(rv)\), contradicting equality at the maximizing coordinate. Thus the fixed point is unique and must be the physical final-size vector obtained in step 1. This generic positive-concave-map uniqueness principle is established in prior mathematical literature and is not claimed as new.

At its unique fixed point, \(J=DF(h)\). Strict concavity with a positive intercept gives \(g_{q,s}(h)>h g'_{q,s}(h)\) for \(h>0\). Therefore \(Jh\ll F(h)=h\). The standard positive-vector spectral bound yields \(\rho(J)<1\), including for reducible transmission graphs. Consequently \((I-J)^{-1}=\sum_{r=0}^\infty J^r\ge0\), and the implicit function theorem applies smoothly in every interior \(q\)-coordinate, extending one-sided to \(q=0\).

**3. Fatality derivative and exact graph support.** For \(0\le q<1\) and \(z>0\), differentiation under the integral sign gives
\[
\partial_q\Phi_q(z)=\int_0^z\frac{u\,du}{(1-qu)^2}>0.
\]
Differentiating \(h=F(h,q)\) with respect to one \(q_j\) while fixing all \(k_i\), \(\beta_{ij}\) and the initial states gives
\[
(I-J)\,\partial_{q_j}h=K_{:j}\,w_j.
\]
Since \(z_i=1-s_i e^{-h_i}\), one has \(\partial z_i/\partial h_i=1-z_i>0\), proving the boxed formula.

Because \(0<1-z_i\), \(w_j>0\), and the entries of \(J\) are positive exactly where the corresponding entries of \(K\) are positive, the entry \([J^rK]_{ij}\) is positive if and only if a positive-weight directed walk of length \(r+1\) runs from \(j\) to \(i\). The Neumann series has no cancellations, so the derivative is positive precisely for a positive-length directed path. No such path makes the derivative identically zero at every admissible parameter point. Integrating the derivative along an interval of values of \(q_j\) proves the corresponding finite-change classification. The invariant next-generation matrix and infectious duration follow immediately from their displayed definitions.

**4. Fixed-population contrast.** If the incidence denominator in the same equations is frozen at \(N_{j0}\), the differential equations for \((S,I)\) contain only \(k_i\), \(\beta_{ij}\), and the initial states, and **do not contain any \(q_i\)**. Hence in the fixed-population comparator every final infection fraction is exactly insensitive to the death-versus-recovery split. The strict path-dependent responses are specific to active-population normalization.

## Verification

An exact-rational input example uses two initially living groups with \(N_{10}=N_{20}=1\), \((s_1,s_2)=(49/50,97/100)\), \(k_1=k_2=1\), and
\[
K=\begin{pmatrix}5/4&4/5\\13/20&27/20\end{pmatrix}.
\]
At \((q_1,q_2)=(1/10,1/10)\), numerical solution gives \((z_1,z_2)\approx(0.83510923,0.82887977)\). Increasing only \(q_1\) to \(3/5\) gives \((z_1,z_2)\approx(0.90944400,0.88122095)\). The reproduction threshold remains \(\rho(K)\approx2.02284161\), the same before and after. Numerical values illustrate the already proved strict inequalities, not substitute for the proof.

The standalone `checker.py` evaluates the fixed-point equations, compares all four two-group numerical sensitivities with finite differences, tests a sparse three-group directed graph's predicted zero and positive sensitivities, and evaluates 200 further positive random systems (group counts two through six). Run with `python checker.py`; these finite tests are supplemental falsification checks only, not an infinite certificate.

## Relationship to prior work

Melo and Santos (2026) develop the active-population two-group SIRD model, derive its final-size equations, and prove monotonicity under larger transmission rates; their fixed-\(\gamma\) mortality plots alter the total infectious exit rate and therefore do **not** test a fixed infectious duration. The present classification instead varies the mortality/recovery **split** while holding the sum fixed, proving sharp effects across arbitrary directed group structures and an exact group-to-group sensitivity formula.

Diekmann, Heesterbeek and Britton's 2013 textbook already presents the **one-population** dependence of final size on infection survival probability at fixed reproduction number in Chapter 1, Exercise 1.26. That scalar mortality effect is explicitly not claimed as new. The published result *Parameter-unrestricted final-size uniqueness and certified geometric bracketing in active-population SIRD networks* already gives the multigroup uniqueness and iteration foundation; those statements are likewise credited. The potentially new claim is the exact full-parameter fatality sensitivity, its positive-length directed-path iff criterion, and its contrast with constant-denominator dynamics.

Classical multigroup SIR final-size work, including Magal, Seydi and Webb (2018), assumes constant population in the transmission normalization. Brauer and Watmough (2009) consider disease-death final-size inequalities in a broader age-of-infection setting, but the accessible material does not establish the exact fixed-exit, directed-path identity above. Brauer (2008) is relevant to heterogeneous treatment but was available only through bibliographic material and an abstract, not an inspected full text; priority uncertainty is explicitly retained.

## Limitations

The conclusion concerns total infections, **not** whether the combined burden of infections and deaths improves or worsens, since increasing the fatal share directly increases fatal outcomes. Changing \(q_i\) at fixed \(k_i\) is a controlled parameter comparison, not a recommended intervention; real clinical processes may change infectious duration, mixing, or transmission together with survival. All groups start with positive infectious seeds, each group receives some infectious input, and \(q_i<1\). The theorem does not claim the same derivative formula for individual-based stochastic epidemics, demographic turnover, population travel, pooled-population denominators or time-dependent controls. The novelty claim is bounded by the inspected literature; uninspected older treatment and matrix-epidemic texts may contain equivalent sensitivity formulas. No independent external scientific validation has been performed.

## References

1. A. M. V. D. L. Melo and M. C. Santos, *Final size of a structured SIRD model with active-population force of infection*, arXiv:2601.15388, first public version 2026-01-21. https://arxiv.org/abs/2601.15388 ; DOI:10.1016/j.cnsns.2026.110430.
2. O. Diekmann, H. Heesterbeek and T. Britton, *Mathematical Tools for Understanding Infectious Disease Dynamics*, Princeton University Press (2013), Chapter 1, Exercise 1.26; DOI:10.23943/princeton/9780691155395.001.0001.
3. *Parameter-unrestricted final-size uniqueness and certified geometric bracketing in active-population SIRD networks*, publicly indexed mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parameter-unrestricted-final-size-uniqueness-and-certified-geome--86fd5f29697c.
4. F. Brauer and J. Watmough, *Age of infection epidemic models with heterogeneous mixing*, Journal of Biological Dynamics 3 (2009), 324–330, DOI:10.1080/17513750802415822.
5. F. Brauer, *Epidemic models with heterogeneous mixing and treatment*, Bulletin of Mathematical Biology 70 (2008), 1869–1885, DOI:10.1007/s11538-008-9326-1 (abstract inspected; full text not inspected).
6. P. Magal, O. Seydi and G. Webb, *Final size of a multi-group SIR epidemic model: Irreducible and non-irreducible modes of transmission*, Mathematical Biosciences 301 (2018), 59–67, DOI:10.1016/j.mbs.2018.03.020.
