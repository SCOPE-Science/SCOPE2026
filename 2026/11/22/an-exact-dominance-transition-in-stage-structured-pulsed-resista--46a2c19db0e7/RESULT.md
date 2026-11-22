# An exact dominance transition in stage-structured pulsed resistance fixation

## Finding

Consider a deterministic, periodically treated stage-structured population with a resistant allele and a susceptible allele at one locus. Let \(q_i(t)=1-y_i(t)\) be the susceptible allele fraction in stage \(i\). For any number of communicating stages, positive resistant-allele frequencies and nontrivial treatment selection, the speed of fixation has a sharp distinction controlled by heterozygote dominance.

At complete dominance of resistance, \(h=0\), define \(M=D e^{\tau A}\), let \(\lambda=\rho(M)\), and choose positive right/left Perron vectors \(v,\ell\) with \(\ell^Tv=1\). Put

\[
S=\sum_{i=1}^{n}\ell_i v_i s_i>0.
\]

Then, at each stage and regardless of initial allele frequencies,

\[
\boxed{\lim_{k\to\infty} kq_i(k\tau^+)=\frac1S.}
\]

At all times (including times between disturbances), \(\lim_{t\to\infty}t q_i(t)=\tau/S\). In contrast, for every fixed \(0<h\le1\), define \(M_h=\operatorname{diag}(1-hs_i)M\). Then

\[
\boxed{\lim_{k\to\infty}\frac{\log q_i(k\tau^+)}{k}=\log\!\left(\frac{\rho(M_h)}{\rho(M)}\right)<0.}
\]

The continuous-time logarithmic rate is this quantity divided by \(\tau\). Both conclusions hold irrespective of whether \(\rho(M)\) is below, equal to or above one.

## Assumptions and scope

There are \(n\ge2\) stages, with a real irreducible Metzler matrix \(A\) (nonnegative off-diagonal entries, strongly connected directed interaction graph), a treatment period \(\tau>0\), and a strictly positive transition matrix \(E=e^{\tau A}\). In stage \(i\), let \(0<d_i\le1\), \(0\le s_i<1\), with \(s_j>0\) for at least one stage \(j\), and let the common dominance parameter be \(h\in[0,1]\). The three genotype treatment-survival probabilities (susceptible homozygote, heterozygote, resistant homozygote) are respectively

\[
\delta_i^{11}=d_i(1-s_i),\qquad\delta_i^{12}=d_i(1-hs_i),\qquad\delta_i^{22}=d_i.
\]

Hardy–Weinberg genotype proportions are assumed at the instant of each pulse. Between pulses, stage densities evolve by \(x'=Ax\) and each allelic density follows the same linear stage transport, without genotype-dependent demographic rates. Initially \(x_i(0^+)>0\) and \(0<y_i(0^+)<1\) for every stage. Put \(D=\operatorname{diag}(d_i)\); all vectors are column vectors and all limits are for deterministic, infinite-population allele frequencies. The classification is a continuous-frequency limit, not a statement about random finite-population fixation times.

## Proof

**1. Allele-density map.** Write \(z_i=x_i y_i\) for resistant alleles and \(w_i=x_i(1-y_i)\) for susceptible alleles. Between pulses, \(z'=Az\), \(w'=Aw\), since transport and reproduction are genotype-independent. With \(Z=Ez\), \(W=Ew\), \(Q_i=W_i/(W_i+Z_i)\), direct substitution of Hardy–Weinberg genotype frequencies in the marginal survival law gives the exact pulse update

\[
\begin{aligned}
z_i^+&=d_iZ_i(1-hs_iQ_i),\\
w_i^+&=d_iW_i\bigl(1-hs_i-(1-h)s_iQ_i\bigr).
\end{aligned}
\tag{1}
\]

For a stage receiving a pulse, its allele fraction obeys \(0<Q_i^+\le Q_i<1\), strictly when \(s_i>0\). This follows from comparing the allele-weighted marginal survivals of susceptible and resistant alleles; the exact decrement is

\[
Q_i-Q_i^+=\frac{s_iQ_i(1-Q_i)[h(1-Q_i)+(1-h)Q_i]}{1-2hs_iQ_i+(2h-1)s_iQ_i^2}.
\tag{2}
\]

The denominator is the mean pulse survival divided by \(d_i\), so it is strictly positive.

**2. All susceptible fractions vanish.** The stage density map is \(x^+=B(Q)Ex\), with \(B(Q)\) diagonal and its entries in \([d_i(1-s_i),d_i]\). Since \(E\) is strictly positive, at every pulse after the first, the normalized stage densities lie in a common compact subset of the positive simplex. Consequently the between-pulse allele averages \((Ew)_i/(Ex)_i\) assign every preceding stage a mixing weight bounded below by one fixed \(\alpha>0\). If \(Q_k^{\max}\) and \(Q_k^{\min}\) denote maximum and minimum susceptible fractions just after pulse \(k\), positivity of mixing and nonincrease at pulses imply

\[
Q_{k+1}^{\max}\le Q_k^{\max}-\alpha(Q_k^{\max}-Q_k^{\min}).
\]

Hence \(Q_k^{\max}\) decreases to some limit and the stagewise spread tends to zero. If the limit were in \((0,1)\), a selected stage with \(s_j>0\) would incur a strictly positive decrement in (2), contradicting the common limit. The limit cannot equal one because all initial resistant fractions are strictly positive and the maximal susceptible fraction never increases. Therefore \(q_i(k\tau^+)\to0\) for every stage. Convex mixing extends this limit to all times.

**3. Exponential regime \(h>0\).** In (1), the two evolving allele-density vectors are products of strictly positive matrices asymptotic to \(M=D E\) and \(M_h=\operatorname{diag}(1-hs_i)D E\), respectively. For a fixed \(\epsilon>0\), all sufficiently late matrices lie entrywise between \((1-\epsilon)M\) and \((1+\epsilon)M\) (for resistant alleles), and between \((1-\epsilon)M_h\) and \((1+\epsilon)M_h\) (for susceptible alleles). Perron–Frobenius comparison, followed by \(\epsilon\downarrow0\), yields the respective componentwise log-growth exponents \(\log\rho(M)\) and \(\log\rho(M_h)\). Subtracting gives the stated limit for \(\log(w_i/(z_i+w_i))/k\). Because \(M_h\le M\), with a strict inequality in at least one positive row, \(\rho(M_h)<\rho(M)\).

**4. Algebraic regime \(h=0\).** Equation (1) makes the resistant allele density exactly linear: \(z_{k+1}=Mz_k\). Normalize by \(\lambda^k\): \(Z_k=\lambda^{-k}z_k\to a v\), where \(a=\ell^Tz_0>0\). Set \(W_k=\lambda^{-k}w_k\). As \(w_k\le x_k\le M^k x_0\) componentwise and \(q_i(k\tau^+)\to0\), we have \(W_k\to0\). The susceptible update becomes exactly

\[
W_{k+1}=\lambda^{-1}\left(MW_k-D\operatorname{diag}(s_i)\frac{(EW_k)^{\circ2}}{E(Z_k+W_k)}\right),
\tag{3}
\]

where squaring and division are componentwise. Let \(b_k=\ell^TW_k>0\) and \(u_k=W_k/b_k\). From (3), \(u_{k+1}=\lambda^{-1}Mu_k+o(1)\); all \(u_k\) lie in the compact positive normalized simplex \(\ell^T u_k=1\). The matrix \(M/\lambda\) has a simple eigenvalue one, while all other eigenvalues have modulus below one. Iterating the asymptotically unforced recurrence gives \(u_k\to v\). Multiplication of (3) by \(\ell^T\) now gives

\[
\begin{aligned}
b_k-b_{k+1}&=\lambda^{-1}\sum_i\ell_i d_i s_i\frac{(EW_k)_i^2}{(E(Z_k+W_k))_i}\\
&=\left(\frac Sa+o(1)\right)b_k^2,
\end{aligned}
\tag{4}
\]

where the equality \(d_i(Ev)_i=\lambda v_i\) identifies the coefficient. It follows that \(1/b_{k+1}-1/b_k\to S/a\), and Cesàro averaging yields \(kb_k\to a/S\). Since \(w_{k,i}/z_{k,i}=W_{k,i}/Z_{k,i}\sim b_k/a\), every stage satisfies \(k q_i(k\tau^+)\to1/S\). For times between successive pulses, the susceptible fractions are positive convex averages of the end-of-pulse fractions and hence have the same leading order; replacing \(k\tau\) by \(t\) gives \(t q_i(t)\to\tau/S\). Replacing \(A\) with \(A+cI\) multiplies both \(M\) and \(M_h\) by \(e^{c\tau}\) but leaves \(v\), \(\ell\), \(S\), and the Perron eigenvalue ratio unchanged. Thus baseline demographic growth can cross the ecological persistence threshold without changing either allele-fixation law. This completes the proof.

## Verification

A standalone Python standard-library checker (`verify.py`) verifies the Hardy–Weinberg marginal-survival identities exactly on rational inputs and checks the predicted two-stage algebraic coefficient and exponential rate by explicit matrix iteration. For \(A=\begin{psmallmatrix}-2&2\\1&-1\end{psmallmatrix}\), \(\tau=1\), \(D=\operatorname{diag}(0.9,0.7)\) and \(s=(0.5,0.25)\), it computes \(S\approx0.349461035386\), hence \(1/S\approx2.86154935384\). After 30,000 pulses with \(h=0\), the two values of \(kq_i\) are approximately \(2.86248655\) and \(2.86255867\). At \(h=0.3\), the limiting log-rate is approximately \(-0.110656383926\) per pulse, consistent with finite-iteration data. These computations corroborate but do not replace the analytical proof.

## Relationship to prior work

D'Ovidio Long, Adjei and Patel (2026) formulate the periodically pulsed stage-structured genotype-survival model and prove asymptotic convergence to full resistance (Theorem 5), together with extinction/growth criteria for population density (Theorems 6–7). Their inspected theorem statements and analysis do not give the critical inverse-pulse coefficient or the dominance-dependent exact logarithmic decay rate established here. The new statement concerns a stronger observable, not merely the already-known limit of the allele fraction.

Classical diploid selection already exhibits slow fixation when favorable resistance is completely dominant; no claim is made to have discovered that unstructured phenomenon. Engen, Lande and Sæther (2009) develop reproductive-value-weighted allele descriptions in stochastic age structure, and de Vries and Caswell (2019) study stage-structured evolutionary demography. The present exact coefficient \(S\) for *periodic pulsed, stage-specific genotype survival*, obtained without weak-selection or fixed-population assumptions, is the point of distinction. Earlier general periodic projection-matrix work characterizes ecological Perron multipliers rather than the same genotype-frequency rates.

## Limitations

The result presumes infinite-population deterministic frequencies, strictly positive initial frequencies of both alleles in every stage, irreducible linear stage transport, genotype-independent vital rates between pulses, Hardy–Weinberg genotype fractions at each pulse, fixed treatment parameters, and at least one positively selected stage. It is not a stochastic fixation-time theorem and does not account for mutation, resistance costs, density feedback or time-varying dose parameters. For \(h=0\), the inverse-time coefficient is asymptotic, not a uniform finite-time error bound. The exponential and algebraic regimes need not have a uniform crossover approximation as \(h\downarrow0\). An independent historical-priority assessment has not been performed.

## References

1. A. D'Ovidio Long, A. Adjei, S. Patel, *On the formulation and analysis of a stage-structured eco-evolutionary model with pulsed disturbances*, arXiv:2609.10581v1 (first public 2026-09-05), https://arxiv.org/abs/2609.10581.
2. S. Patel and P. De Leenheer, *On the spectral radius properties of a key matrix in periodic impulse control*, arXiv:2310.07616, https://arxiv.org/abs/2310.07616.
3. S. Engen, R. Lande and B.-E. Sæther, *Reproductive Value and Fluctuating Selection in an Age-Structured Population*, Genetics 183 (2009), 629–637, https://pmc.ncbi.nlm.nih.gov/articles/PMC2766322/.
4. C. de Vries and H. Caswell, *Stage-Structured Evolutionary Demography: Linking Life Histories, Population Genetics, and Ecological Dynamics* (2019), https://doi.org/10.1086/701857.
5. P. D. Taylor, *Allele-Frequency Change in a Class-Structured Population*, American Naturalist 135 (1990), 95–106, https://doi.org/10.1086/285034; full-text class-weighting analysis and its first-order rare-allele limit were inspected.
