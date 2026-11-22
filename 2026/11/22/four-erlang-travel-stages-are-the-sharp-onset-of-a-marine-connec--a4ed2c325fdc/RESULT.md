# Four Erlang travel stages are the sharp onset of a marine-connectivity spacing reversal

## Finding

Consider two point-site habitat populations on a circular, strictly one-way dispersal corridor. If larval travel distance has the distribution of the sum of \(k\) independent equal-rate exponential stages, wrapping the density around the corridor and using its point-site values as a positive linear recruitment kernel produces the following exact layout law. For \(k=1\), the complete two-site recruitment spectrum is spacing-independent. For \(k=2\) and \(k=3\), antipodal placement uniquely maximizes the Perron recruitment multiplier at every positive travel rate and for all positive site qualities. **Four stages are the first number capable of reversing this rule**: the four-stage kernel has a sharp dimensionless rate boundary at which the best layout changes from antipodal to coincident (or arbitrarily near-coincident if sites must be distinct). A second, different boundary changes whether two off-center local minima exist.

Write \(q=e^{-\alpha L}\), where \(L>0\) is the ring circumference and \(\alpha>0\) is the common exponential-stage rate. For four stages set
\[
q_\mathrm{G}=7-4\sqrt3,\qquad q_\mathrm{M}=5-2\sqrt6,
\qquad 0<q_\mathrm{G}<q_\mathrm{M}<1.
\]
Then the global maximizers on the closed, coincident-site-allowed layout space are precisely antipodal layouts for \(0<q<q_\mathrm{G}\), both antipodal and coincident layouts for \(q=q_\mathrm{G}\), and coincident layouts for \(q_\mathrm{G}<q<1\). The minimizing layouts for \(0<q<q_\mathrm{M}\) consist of two mirror-image non-antipodal separations determined by \(z(1-z)=2q/(1-q)^2\); for \(q\ge q_\mathrm{M}\), antipodal placement is the unique minimum. At the first boundary, the minimum occurs at \(z(1-z)=1/6\).

For physically distinct point sites, the domain is \(0<z<1\); when coincidence is the closed-space optimum, it is only a strict supremum as \(z\to0\) or \(z\to1\). At \(q=q_\mathrm{G}\), the antipodal maximum remains attained. The scale-equivalent threshold \(\alpha L=-\log(7-4\sqrt3)\approx2.633915794\) separates the two global regimes. There is no biological claim that two reserves should literally be collapsed into one; the theorem concerns point-sampled low-density recruitment.

## Assumptions and scope

Fix \(L>0\), \(\alpha>0\), and an integer \(k\in\{1,2,3,4\}\). Put two labeled demographic point sites at positions \(0\) and \(d\) clockwise around a circle, and let \(z=d/L\in(0,1)\). Define the wrapped Erlang-\(k\) point kernel by
\[
K_k(d)=\sum_{n=0}^{\infty}\frac{\alpha^k}{(k-1)!}(d+nL)^{k-1}e^{-\alpha(d+nL)},\qquad 0<d<L.
\]
At \(d=0\), use the same series to define the self-transfer coefficient \(K_k(0)\). For \(k\ge2\) the kernel has a continuous extension at the identified circle endpoint, so the coincidence limit is well defined. For \(k=1\), the non-coincident off-diagonal product alone is used in the spacing-invariance statement, avoiding its directional jump at the origin.

Let receiving strengths \(u_1,u_2>0\) and source outputs \(v_1,v_2>0\) be fixed independently of spacing, with \(w_i=u_iv_i>0\). The positive two-by-two recruitment matrix is \(M_{ij}(d)=u_i v_j K_k((x_i-x_j)\bmod L)\) for distinct sites, with diagonal \(u_i v_i K_k(0)\). Its Perron root \(\rho(M)\) is a linear low-density recruitment multiplier; it is not asserted to be a stochastic survival probability or a measured ecosystem-growth rate. The continuum of positive site strengths is allowed, and all statements are global over the stated placement domain. Coincident layout is a mathematical limit of two labeled populations, not a claim about finite-width reserves.

## Proof

**1. Separation only affects the reciprocal recruitment product.** The diagonal entries are \(w_1K_k(0)\) and \(w_2K_k(0)\), independent of \(d\). The cross-product of off-diagonal entries is \(w_1w_2K_k(d)K_k(L-d)\). Therefore the positive Perron eigenvalue equals
\[
\rho_k(d)=\frac{K_k(0)(w_1+w_2)+\sqrt{K_k(0)^2(w_1-w_2)^2+4w_1w_2K_k(d)K_k(L-d)}}2.
\]
It is strictly increasing as a function of the positive kernel cross-product. This reduces the ranking of all layouts, even for unequal site qualities, to one scalar polynomial in \(z\).

**2. Exact stage polynomials.** Set \(q=e^{-\alpha L}\) and \(s_j(q)=\sum_{n\ge0}n^j q^n\) for \(j=0,1,2,3\). With \(P_m(z)=\sum_{j=0}^m\binom mj z^{m-j}s_j(q)\), geometric summation gives
\[
K_k(Lz)=\frac{\alpha^kL^{k-1}}{(k-1)!}e^{-\alpha Lz}P_{k-1}(z),\quad
K_k(Lz)K_k(L(1-z))=\frac{\alpha^{2k}L^{2k-2}}{((k-1)!)^2}\,q\,P_{k-1}(z)P_{k-1}(1-z).
\]
The needed sums are
\[
s_0=\frac1{1-q},\quad s_1=\frac q{(1-q)^2},\quad s_2=\frac{q(1+q)}{(1-q)^3},\quad s_3=\frac{q(1+4q+q^2)}{(1-q)^4}.
\]
Put \(t=z(1-z)\in(0,1/4]\). Expanding the polynomials and collecting symmetric powers gives, exactly,
\[
\begin{aligned}
P_0(z)P_0(1-z)&=(1-q)^{-2},\\
P_1(z)P_1(1-z)&=\frac q{(1-q)^4}+\frac t{(1-q)^2},\\
P_2(z)P_2(1-z)&=\frac{q(1+q)^2}{(1-q)^6}+\frac{t^2}{(1-q)^2},\\
P_3(z)P_3(1-z)&=\frac{q(q^2+4q+1)^2}{(1-q)^8}-\frac{3q t^2}{(1-q)^4}+\frac{t^3}{(1-q)^2}.
\end{aligned}
\]
These are identities of rational functions in \(q\) and polynomials in \(z\); the reproducibility file checks their exact-rational specializations independently but the displayed finite algebra proves them without numerical extrapolation. Since \(t\) uniquely peaks at the antipode \(z=1/2\), stages two and three strictly prefer that location, while stage one is indifferent.

**3. Four-stage global and local phase diagram.** Ignore the spacing-independent positive multiplier and write the last line as \(F_q(t)\). Its derivative is
\[
F'_q(t)=\frac{3t}{(1-q)^4}\left((1-q)^2t-2q\right).
\]
Thus \(F_q\) first decreases and then increases on positive \(t\), if its single positive turning point \(t_*=2q/(1-q)^2\) lies in \((0,1/4)\); otherwise it decreases throughout \((0,1/4)\). Hence a global maximum can only lie at \(t=0\) (coincidence) or \(t=1/4\) (antipode). Their exact difference is
\[
F_q(1/4)-F_q(0)=\frac{1-14q+q^2}{64(1-q)^4}.
\]
For \(0<q<1\) its sign changes exactly once, at \(q_\mathrm{G}=7-4\sqrt3\). This proves every asserted global maximizer and the equality case. The turning point satisfies \(t_*<1/4\) exactly when \((1-q)^2>8q\), or \(q<q_\mathrm{M}=5-2\sqrt6\). If present, it is a strict minimum in the \(t\) variable and produces exactly the two mirror-image minimizing separations \(z=(1\pm\sqrt{1-4t_*})/2\). Otherwise \(F_q\) decreases up to \(t=1/4\), making antipodal placement its unique minimum. At \(q_\mathrm{G}\), \((1-q)^2=12q\), so \(t_*=1/6\). Strictness and boundary cases follow directly from these derivative signs.

**4. Exact finite-separation witness.** At \(q=1/2\), equivalently \(\alpha L=\log2\), the four-stage polynomial is
\[
P_3(z)=2z^3+6z^2+18z+26,
\quad P_3(z)P_3(1-z)=1352-24t^2+4t^3.
\]
It is strictly decreasing in \(t\) for \(0<t\le1/4\). At the *distinct* configurations \(z=1/10\) and \(z=1/2\) its exact values differ by
\[
P_3(1/10)P_3(9/10)-P_3(1/2)^2=\frac{19469}{15625}>0.
\]
Thus a genuinely separated, strongly clustered pair has a strictly larger invasion multiplier than an antipodal pair for every \(w_1,w_2>0\). This avoids relying on the coincidence boundary for the reversal. Together with the universal stage-one, -two, and -three statements, it proves minimality of the four-stage obstruction.

## Verification

Run `python3 VERIFY.py` using Python 3 with only its standard library. The checker tests all four identities using `fractions.Fraction` over seven rational wrapping parameters and 36 rational site positions, independently checks the four-stage rational witness and threshold identities, compares the stage polynomials with truncated direct winding sums, and tests spectral rankings with unequal site strengths and all phase regimes. The displayed output is `PASS: 1659 deterministic assertions; four exact factorizations; sharp stage-four transition`. No finite sample establishes the universal claim; the rational-function identities and derivative argument above do that. The checker file is included with this result.

## Relationship to prior work

Shanks, Grantham and Carr (2003), whose full freely available paper was inspected (methods, quantitative dispersal compilation, and reserve-layout discussion), motivate reserve design from measured propagule dispersal distances and habitat spacing, but do not state this stage-indexed spectral layout phase diagram. Hastings and Botsford (2006), in the inspected full open article, give a general low-density patch-connectivity persistence criterion and show why reciprocal recruitment pathways matter; they do not specialize to wrapped Erlang kernels or derive a four-stage spacing transition. Artzy-Randrup and Stone (2010), in the inspected full open article, analyze connectivity eigenvalues and dispersal cycles, not the present four-stage point-kernel spacing law. Kaplan and Botsford (2005), whose complete nine-page open paper was inspected, study variable reserve spacing through numerical population simulations with a two-sided Laplacian dispersal kernel and age structure, not the present directed, wrapped Erlang-stage spectral classification. The accessible opening and abstract of D'Aloia and colleagues (2015) support the ecological relevance of measured dispersal kernels, but describe an approximately exponential spatial profile rather than stage-indexed spectral extrema. Its complete text could not be reopened in this check.

Two closest published mathematical comparisons are **Spacing-blind recruitment spectra characterize exponential transport, while two stages favor opposite sites** (published-finding corpus record `2026/11/2/SCOPE-spacing-blind-recruitment-spectra-characterize-exponential-trans--692440d5c26c`) and **Memoryless dispersal is the only gap-neutral exponential mixture: a sharp two-reserve spacing law** (record `2026/11/2/SCOPE-memoryless-dispersal-is-the-only-gap-neutral-exponential-mixture--a041b2e80341`). The first full result proves the exponential point-site invariance and the **two-stage** antipodal preference, but its stated theorem and proof stop at stage two; neither the stage-three rigidity nor the four-stage global/local phase boundaries are implied by its two-stage formula. The second full result treats *finite-width reserves* with **positive mixtures of exponential rates**, a log-convex class. Erlang four-stage travel distances are convolutions of sequential exponential stages and are not positive rate mixtures; neither its Hölder argument nor its theorem covers this kernel. These are related baselines, not priority support for the new four-stage result. The polynomial identities use standard geometric-series and Perron-eigenvalue tools; those tools are not claimed as novel independently.

## Limitations

This is an exact result only for two point-sampled, possibly unequal-strength demographic sites on a closed circle with clockwise-only travel and equal-rate, integer-stage Erlang *distance* laws. It does not extend automatically to two finite-width reserves, nonuniform currents, bidirectional diffusion, density dependence, larval mortality beyond that represented by the kernel, or field-estimated competency distributions. The coincidence layout is a mathematical closure convention; distinct populations co-located in space may not be biologically meaningful. For strictly distinct sites the clustering regime has a supremum but no attained global maximum without a minimum-spacing constraint. A higher Perron multiplier is a statement about the defined linear model, not a validated conservation-management prescription. Results for \(k\ge5\) are not claimed. Broader historical kernel-design and integral-operator literature may contain equivalent or stronger formulations; originality is a provisional literature-based conclusion, not a proof of uniqueness or independent certification.

## References

1. A. L. Shanks, B. A. Grantham and M. H. Carr, *Propagule dispersal distance and the size and spacing of marine reserves*, Ecological Applications 13 (2003), 159–169, first published 2003-02-01, https://doi.org/10.1890/1051-0761(2003)013[0159:PDDATS]2.0.CO;2.
2. A. Hastings and L. W. Botsford, *Persistence of spatial populations depends on returning home*, PNAS 103 (2006), 6067–6072, https://doi.org/10.1073/pnas.0506651103, full open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1458697/.
3. Y. Artzy-Randrup and L. Stone, *Connectivity, Cycles, and Persistence Thresholds in Metapopulation Networks*, PLOS Computational Biology 6 (2010), e1000876, https://doi.org/10.1371/journal.pcbi.1000876, full open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2916855/.
4. D. M. Kaplan and L. W. Botsford, *Effects of variability in spacing of coastal marine reserves on fisheries yield and sustainability*, Canadian Journal of Fisheries and Aquatic Sciences 62 (2005), https://doi.org/10.1139/F04-243, abstract: https://escholarship.org/uc/item/75p6q8t0.
5. C. C. D'Aloia et al., *Patterns, causes, and consequences of marine larval dispersal*, PNAS 112 (2015), 13940–13945, https://pmc.ncbi.nlm.nih.gov/articles/PMC4653176/.
6. *Spacing-blind recruitment spectra characterize exponential transport, while two stages favor opposite sites*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-spacing-blind-recruitment-spectra-characterize-exponential-trans--692440d5c26c.
7. *Memoryless dispersal is the only gap-neutral exponential mixture: a sharp two-reserve spacing law*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-memoryless-dispersal-is-the-only-gap-neutral-exponential-mixture--a041b2e80341.
