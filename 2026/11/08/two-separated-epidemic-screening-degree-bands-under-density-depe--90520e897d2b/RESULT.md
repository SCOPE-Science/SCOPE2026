# Two separated epidemic-screening degree bands under density-dependent migration

## Finding

A degree-based SIS metapopulation can have **two separated sets of degree classes passing the same sufficient early-invasion screen**, with a class failing the screen between them. This occurs even in an uncorrelated scale-free degree distribution, with mass-action contacts and identical power-law movement of susceptible and infected individuals. The phenomenon is about a rigorous sufficient screening inequality, not two independent epidemic thresholds.

Here is a sharp general turning-point criterion. Fix integers \(1\le k_0<K\), a degree exponent \(\gamma>2\), a movement exponent \(\alpha\ge0\), and \(a,b,\mu>0\). Put
\[
 d=\gamma-1,\quad s=\frac1{1+\alpha},\quad t=\frac{\alpha}{1+\alpha},\quad c=\Bigl(\sum_{j=k_0}^K j^{-d}\Bigr)^{-1}.
\]
The continuous interpolation of the degree-specific sufficient-invasion score is
\[
 R(u)=\frac{a u^s}{\mu+b u^t(1-cu^{-d})},\qquad k_0\le u\le K.
\]
For \(0\le\alpha\le1\), \(R\) has no strict interior local maximum. For \(\alpha>1\), define
\[
 H=1-\alpha+d(1+\alpha),\qquad
 G(u)=(\alpha-1)u^t+cH u^{t-d},\qquad
 u_c=\left(\frac{cH(d-t)}{(\alpha-1)t}\right)^{1/d}.
\]
**Exactly two strict interior turning points**, a local minimum followed by a local maximum, occur if and only if
\[
 k_0<u_c<K,\qquad G(u_c)<\frac\mu b<\min\{G(k_0),G(K)\}.
\]
There can never be more than two. Thus the two separated screening bands have a sharp, explicitly testable structural prerequisite; removing the same-degree return term \(cu^{-d}\) makes two turning points impossible.

For the concrete finite set of degrees \(k=3,4,\ldots,20\), take \(\gamma=3\), \(\alpha=2\), \(b=1\), \(\mu=5\), and \(a=1250/281\). Then the **exact** degree classes satisfying \(R(k)>1\) are
\[
 \boxed{\{3\}\ \cup\ \{5,6,\ldots,13\}.}
\]
The classes \(4\) and \(14,15,\ldots,20\) fail this particular sufficient screen. Every one of the eighteen inequalities is strict and is certified by rational arithmetic; no floating-point classification is needed.

## Assumptions and scope

The underlying reference is the heterogeneous mean-field SIS metapopulation of Ripoll, Avinyó, Pellicer and Saldaña (2015), not an individual-contact simulation. Its degree law here is the truncated discrete scale-free distribution
\[
 p(k)=\frac{k^{-\gamma}}{\sum_{j=k_0}^K j^{-\gamma}},\quad k_0\le k\le K,
\]
with the uncorrelated annealed mixing rule \(P(k'\mid k)=k'p(k')/\langle k\rangle\). Consequently
\[
 P(k\mid k)=c k^{-d}.
\]
The model uses mass-action contact number \(C(\rho)=c_0\rho\), susceptible movement \(D_S(\rho)=D_S^0(\rho/\rho_0)^\alpha\), and infected movement \(D_I(\rho)=D_I^0(\rho/\rho_0)^\alpha\), all with positive coefficients. Write \(\mu\) for recovery plus demographic turnover, as in the source's early-invasion block. The disease-free population profile is
\[
 \rho_k^*=\rho_0\frac{k^s}{L},\qquad L=\sum_{j=k_0}^K p(j)j^s.
\]
The constants above are \(a=\beta c_0\rho_0/L\) and \(b=D_I^0/L^\alpha\). The score \(R(k)\) is exactly the left side of the source's sufficient condition (9); \(R(k)>1\) means that the corresponding infected-block diagonal is positive and therefore guarantees a positive spectral growth bound for the complete degree-based linearization. It is not an exact patch-level reproduction number.

In the exhibited example all normalized constants are realized, for instance, by \(\rho_0=1\), \(\beta=1\), \(c_0=(1250/281)L\), \(D_S^0=D_I^0=L^2\), recovery rate \(4\), and demographic turnover rate \(1\). The smooth variable \(u\) is used only to classify the scores of supported integer degree classes.

## Proof

For \(u\ge k_0\), the denominator of \(R(u)\) is positive: \(cu^{-d}\le ck_0^{-d}<1\), since \(K>k_0\). Direct differentiation, using \(s=1/(1+\alpha)\), gives
\[
 \operatorname{sgn}R'(u)=\operatorname{sgn}\left(\mu+b(1-\alpha)u^t-bc[1-\alpha+d(1+\alpha)]u^{t-d}\right).
\]
If \(0\le\alpha\le1\), the expression in parentheses is strictly increasing in \(u\): its nonconstant positive-power term is nondecreasing, and its negative \(u^{t-d}\) term strictly increases because \(t<d\). Thus any zero changes the sign from negative to positive, producing only a minimum.

If \(\alpha>1\), the sign is that of \(\mu/b-G(u)\). Moreover,
\[
 u^{d-t+1}G'(u)=(\alpha-1)t u^d-cH(d-t).
\]
Since \(\alpha>1\), \(t>0\), \(d>1\), and \(H>0\), this has the unique positive zero \(u_c\), with \(G\) strictly decreasing before and increasing after it. It follows that two strict interior roots of \(\mu/b-G\) exist precisely under the displayed endpoint/minimum inequalities. Their derivative-sign pattern is negative, positive, negative, establishing first a minimum and then a maximum. The same argument proves the upper bound of two turning points and the necessity of the criterion.

For the concrete example, \(d=2\), \(t=2/3\), and
\[
 c=\left(\sum_{j=3}^{20}\frac1{j^2}\right)^{-1}
 =\frac{10838475198270720}{3751881733704241}.
\]
Hence \(G(u)=u^{2/3}+5cu^{-4/3}\) has its minimum at \(u_c=\sqrt{10c}\); the stationary-point equation becomes the cubic
\[
 x^3-5x^2+5c=0,\qquad x=u^{2/3}.
\]
Exact rational interval comparisons yield \(G(3)>5>G(4)\), \(G(8)<5<G(9)\), and \(3<u_c<8\). Therefore the two distinct stationary points lie in \((3,4)\) and \((8,9)\). The finite degree screening result follows by the exact inequalities certified in the accompanying checker: \(R(3)>1\), \(R(4)<1\), \(R(k)>1\) for every integer \(5\le k\le13\), and \(R(k)<1\) for every integer \(14\le k\le20\).

Because a positive diagonal term of an irreducible Metzler infected Jacobian block implies positive spectral bound, any of the passing classes suffices for the source's early-invasion instability implication. The statement does not infer an actual outbreak probability or independent local invasion within any one class.

## Verification

Run `python3 checker.py` using only the Python standard library. The checker computes the exact rational degree-law normalizer, reconstructs the same-degree mixing probabilities, tests the analytic turning-point sign landmarks, and certifies all eighteen threshold inequalities with outward rational intervals for cube roots. Each \(k^{1/3}\) is enclosed using integer cube roots at a denominator of \(10^{12}\); the denominator \(5+t^2-c/t^4\) is increasing in \(t>0\), so its interval bounds are rigorous. The verifier reports 48 passed exact assertions. These finite certificates support the particular eighteen-class witness; the general classification is proved analytically above.

## Relationship to prior work

Ripoll, Avinyó, Pellicer and Saldaña (2015), equation (9), supply the exact degree-specific sufficient-invasion score and show numerically that its maximum can occur at a smallest or intermediate connectivity. Their figure 3 illustrates monotone and single-peaked profiles, not the sharp two-turning-point criterion or two disconnected sets of integer degree classes passing the same threshold. The earlier Avinyó–Pellicer–Ripoll–Saldaña conference chapter gives the analogous sufficient score and discusses an intermediate maximum but not a minimum followed by a maximum. Juher and Mañosa (2014) prove the diagonal spectral sufficient condition for constant migration, but do not develop the density-dependent power-law two-turning mechanism. The present contribution is a structural classification and exact counterexample to the expectation that the sufficient-screening degree profile has only one high-risk band; it is **not** a new epidemic model, a newly derived base invasion inequality, or an exact epidemiological threshold.

## Limitations

The two bands are bands of a **sufficient** instability test, not necessarily bands of observed outbreaks or exact local basic reproduction numbers. The degree distribution and mixing are degree-based annealed assumptions; the result does not assert realizability by every simple finite network with those counts. The real-variable turning-point criterion is an interpolation of supported discrete degree scores, and a continuous local extremum need not coincide with an integer. The exact finite witness avoids that ambiguity by checking every degree. Historical priority is not independently certified; an equivalent analytical consequence of earlier formulas might have appeared elsewhere.

## References

1. J. Ripoll, A. Avinyó, M. Pellicer and J. Saldaña, *Impact of density-dependent migration flows on epidemic outbreaks in heterogeneous metapopulations*, arXiv:1504.05884 (first public version 2015-04-22), *Physical Review E* **92**, 022809 (2015). https://arxiv.org/abs/1504.05884 .
2. A. Avinyó, M. Pellicer, J. Ripoll and J. Saldaña, *Density-Dependent Diffusion and Epidemics on Heterogeneous Metapopulations*, in *Extended Abstracts Spring 2014*, *Trends in Mathematics* **4**, pp. 143–148 (2015). https://www.maia.ub.es/~gerard/2014/HSND-2014%20%2845-48%28.pdf .
3. D. Juher and V. Mañosa, *Spectral Properties of the Connectivity Matrix and the SIS-epidemic Threshold for Mid-size Metapopulations*, *Mathematical Modelling of Natural Phenomena* **9** (2014), 108–120. https://doi.org/10.1051/mmnp/20149207 .
