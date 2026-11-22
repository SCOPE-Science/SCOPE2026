# Four-strain pairwise immune-history aliasing with opposite initial infection growth

## Finding

In the history-based multi-strain susceptible–infectious model, **four is the smallest total number of strains for which complete one- and two-strain immune-history marginals can conceal opposite initial growth signs of a fourth strain**. This holds even if all eight susceptible-history classes are strictly positive, the two populations have identical totals and identical seeded fourth-strain infections, and each previous strain acts through an independent multiplicative susceptibility reduction.

For a new strain numbered \(4\), let \(J\subseteq\{1,2,3\}\) be the set of previous infections among susceptible hosts. Suppose its relative susceptibility is \(\sigma_J^{4}=c^{|J|}\), where \(0<c<1\). Conditional on the total susceptible mass \(s>0\), suppose every previous-strain exposure has frequency \(1/2\) and every *pairwise* co-exposure has frequency \(1/4\). These data permit precisely the one-parameter family

\[
p_t(J)=\begin{cases}t,&|J|\text{ odd},\\[2pt]1/4-t,&|J|\text{ even},\end{cases}\qquad 0\le t\le1/4.
\]

The exact average susceptibility and its **sharp identifiable interval** are

\[
H(t)=\sum_{J}c^{|J|}p_t(J)
=\frac{1+3c^2}{4}-(1-c)^3t,
\qquad
\frac{3c+c^3}{4}\le H\le\frac{1+3c^2}{4}.
\]

Every value in this interval is attained with the *same* one- and two-strain marginals, and the interval width is \((1-c)^3/4>0\).

In particular, set \(c=1/2\), \(s=63/64\), \(\beta_4=4096/1701\), \(\gamma=\mu=1/2\), and initial aggregate fourth-strain infection \(I_4=1/64\). Place the latter entirely in \(I_{\varnothing}^{4}\), set other infectious classes to zero, and assign the susceptible classes \(S_J=s\,p_t(J)\). At the two strictly interior history distributions \(t=1/16\) and \(t=3/16\), all eight susceptible-history classes have positive mass and all observed first- and second-order history marginals agree. Nevertheless, the respective initial fourth-strain per-capita growth rates are exactly

\[
\left.\frac{d}{du}\log I_4(u)\right|_{u=0}
=\begin{cases}+1/54,&t=1/16,\\-1/54,&t=3/16.\end{cases}
\]

Here \(u\) is the time variable. The signs are strictly robust under small compatible perturbations of the two states and parameters.

## Assumptions and scope

Use the history-based ODE of Ilahi, Hall and House (2026), adapted from earlier multi-strain frameworks. For every infecting strain \(i\) and history \(J\) not containing \(i\), let

\[
\Lambda^{i}=\beta_i\sum_{J:i\notin J}I_J^{i},
\qquad
\dot I_J^{i}=\sigma_J^{i}\Lambda^{i}S_J-(\gamma+\mu)I_J^{i}.
\]

The susceptible-history variables and infection compartments are nonnegative, and \(\sigma_\varnothing^{i}=1\). The other susceptible equations are those of the cited model. For the explicit construction choose constant birth flow \(b=\mu=1/2\), so total mass initially equals the demographic equilibrium value \(1\). Parameters for strains \(1,2,3\) may be any positive admissible values: there are no active infections of those strains at the comparison instant. Define the pooled fourth-strain infectious mass \(I_4=\sum_{J\subseteq\{1,2,3\}}I_J^4\).

The comparison fixes all first-order and second-order *susceptible* infection-history margins, as well as total susceptibility and the pooled fourth-strain infectious mass. It is a comparison of **instantaneous** dynamics at admissible initial states, not a claim that the specified immunity-history states are equilibria, dynamically reachable from a fully naive state, or suitable clinical predictions.

## Proof

**1. Exact aggregate growth equation.** Summing the infectious equations for the target strain gives, with \(I_4>0\),

\[
\frac{d}{du}\log I_4
=\beta_4\sum_{J\subseteq\{1,2,3\}}\sigma_J^4S_J-(\gamma+\mu)
=\beta_4sH-(\gamma+\mu).
\]

This is an exact ODE identity, not a reproduction-number approximation.

**2. All history distributions under the fixed marginals.** Put \(X_j=\mathbf1_{\{j\in J\}}\) and let \(p(J)\) be the conditional history distribution. The constraints \(\Pr(X_j=1)=1/2\) and \(\Pr(X_j=X_k=1)=1/4\), for distinct \(j,k\in\{1,2,3\}\), together with normalization leave exactly one free number \(t=\Pr(X_1=X_2=X_3=1)\). Inclusion–exclusion yields \(p(111)=t\), each one-exposure history has probability \(t\), and each two-exposure history and the empty history have probability \(1/4-t\). Their nonnegativity is equivalent to \(0\le t\le1/4\). Hence the parameterization is complete and proves sharpness of its endpoints.

**3. Quantitative susceptibility aliasing.** Each history with \(j\) previous strains has susceptibility \(c^j\), so

\[
H(t)=(1/4-t)+3ct+3c^2(1/4-t)+c^3t
=(1+3c^2)/4+(c-1)^3t.
\]

Since \(0<c<1\), the slope is strictly negative. The endpoint values and interval width follow, with no untested optimization steps.

**4. Opposite growth at strictly positive compartments.** At \(c=1/2\), the two interior values give \(H(1/16)=55/128\) and \(H(3/16)=53/128\). The demographic and transmission choices satisfy \(\beta_4s=64/27\) and \(\gamma+\mu=1\); thus the exact growth rates are respectively \((64/27)(55/128)-1=1/54\) and \((64/27)(53/128)-1=-1/54\). Because \(t\in(0,1/4)\), every susceptible-history class has positive mass. The inequalities are strict and the relevant model expressions are continuous, so the opposite signs survive sufficiently small perturbations. (Preserving exactly the same pairwise marginals under perturbations is achieved by varying \(t\) within the displayed family.)

**5. Minimality in number of strains.** For at most three total strains, any chosen target strain has at most two other strains in its susceptible histories. Normalization, their single-history marginals, and their pairwise co-exposure (when present) determine all \(2^m\) probabilities by inclusion–exclusion for \(m\le2\). The exact growth formula is therefore unique for any specified cross-immunity kernel and fixed infectious seeding; no pairwise-history alias of its sign can occur. Four strains suffice by Step 4.

**6. General information-order criterion.** For any \(m\ge1\) previous strains and any history response \(\sigma:2^{[m]}\to\mathbb R\), there is a unique expansion \(\sigma(J)=\sum_{A\subseteq J}c_A\), where \(c_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}\sigma(B)\). Thus the expected response under *every* history distribution is determined by all inclusion moments \(M_A=\Pr(A\subseteq J)\) with \(|A|\le k\) if and only if every coefficient \(c_A\) with \(|A|>k\) vanishes. Sufficiency follows from \(\mathbb E\sigma=\sum_Ac_AM_A\). For necessity, if \(c_A\ne0\) at \(|A|>k\), take the uniform even- and odd-parity distributions on subsets of \(A\), with all strains outside \(A\) absent. All inclusion moments of order less than \(|A|\) agree, while their expectations differ by \(\pm c_A/2^{|A|-1}\). This proves the criterion for arbitrary response kernels. In the multiplicative case \(c_A=(c-1)^{|A|}\), so every order up to \(m\) can matter despite mechanistically separable single-exposure protection. The familiar Boolean Möbius identity is used as a proof tool, not claimed as a new algebraic discovery.

## Verification

Run the embedded standalone `verify.py` using Python 3. It performs exact rational (not floating-point) checks of the eight history probabilities, all one- and two-strain marginals, the susceptibility identity and its endpoints for several protection factors and grid points, the strictly positive opposite-growth example, the Boolean coefficients through seven previous strains, and finite parity-trade moment cancellation through six. The delivered script prints `PASS: exact rational checks: 4005` when successful. These computations corroborate finite formulas; the all-size statements are justified by Steps 1–6, not by finite tests.

## Relationship to prior work

Ilahi, Hall and House (2026) specify the full history-based ODE and improve its numerical implementation without asserting a sharp pairwise-information threshold or the present four-strain opposite-growth construction. Kucharski, Andreasen and Gog (2015) discuss information lost through history-based model reductions, not this exact interval of compatible fourth-strain growth. Gog and Grenfell (2002) analyze a status-based reduced-transmission model with different state variables and assumptions. McLeod, Bank and Gandon (2024; 2023 preprint) explicitly discuss third-order *pathogen-genotype* linkage disequilibrium being invisible to pairwise genomic structure; that is a related higher-order-information warning but does not characterize the *host-history* susceptible sum of this ODE, its sharp interval, or the opposite-growth example. General Boolean inversion is classical and not asserted to be original. The claimed new result is the biologically specified, minimal four-strain information limit and its exact ODE sign reversal.

## Limitations

The conclusion is about **initial per-capita growth**, not a long-term invasion exponent, final epidemic size, endemic persistence, or infection prevention efficacy. States with past-exposure classes need not be generated by a specified historical epidemic from naive initial conditions. The stipulated identical pairwise history information presumes pairwise co-exposure data, not merely separate marginal seroprevalences. Cross-immunity is multiplicative for the example and the standard ODE model assumes homogeneous mass-action transmission. The endpoint distributions attaining the global range have four empty history classes, but strictly positive interior distributions already reverse growth. Broad historical priority beyond the inspected and retrieved literature is not independently certified.

## References

1. F. Ilahi, I. Hall, T. House, *A Robust Numerical Framework for Multi-Strain Epidemics*, arXiv:2610.15796v1 (first public 11 October 2026), https://arxiv.org/abs/2610.15796, HTML https://arxiv.t3mt.com/html/2610.15796v1.
2. A. J. Kucharski, V. Andreasen, J. R. Gog, *Capturing the dynamics of pathogens with many strains*, Journal of Mathematical Biology 72 (2016), first online March 2015, https://doi.org/10.1007/s00285-015-0873-4.
3. J. R. Gog, B. T. Grenfell, *Dynamics and selection of many-strain pathogens*, PNAS 99 (2002), https://doi.org/10.1073/pnas.252512799.
4. D. V. McLeod, C. Bank, S. Gandon, *A multilocus perspective on the evolutionary dynamics of multistrain pathogens*, PNAS 121 (2024), https://doi.org/10.1073/pnas.2401578121; preprint https://doi.org/10.1101/2023.10.27.564465.
