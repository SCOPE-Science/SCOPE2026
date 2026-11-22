# Marked Poisson–Gamma limits for low-degree chords with random circular endpoints

## Finding
For each integer \(n\ge2\), sample \(2n\) independent uniform angular points on a circle of circumference one, then independently match them uniformly into \(n\) chords. Let \(d(c)\) be the crossing degree of chord \(c\), \(a(c)\in(0,1/2]\) the shorter arc fraction between its endpoints, and \(u(c)\in\mathbb T=\mathbb R/\mathbb Z\) the midpoint of that shorter arc. Ties have probability zero. For a fixed nonnegative integer \(K\), define
\[
\Xi_{n,j}=\sum_{c:\,d(c)=j}\delta_{(u(c),\,n a(c))},\qquad 0\le j\le K.
\]
**Theorem.** In the weak topology of finite point measures on \(\mathbb T\times[0,\infty)\), jointly over \(0\le j\le K\),
\[
(\Xi_{n,0},\ldots,\Xi_{n,K})\ \Longrightarrow\ (\Pi_0,\ldots,\Pi_K),
\qquad
\mathbb E\Pi_j(du,dy)=du\,\frac{2^{j+1}}{j!}y^je^{-2y}\,dy,
\]
where the \(\Pi_j\) are independent Poisson point processes and \(du\) is normalized Haar measure on the circle. Each degree class therefore has an independent \(\operatorname{Poisson}(1)\) number of points; conditional on the count, locations are independent uniform angles and marks are independent \(\operatorname{Gamma}(j+1,\text{rate }2)\) random variables. The class size, angular location, and arc-mark conclusions are simultaneous consequences of the same theorem.

Put \(M_{n,j}=\max\{na(c):d(c)=j\}\), with the maximum defined as zero for an empty class. For every \(t\ge0\),
\[
\lim_{n\to\infty}\Pr(M_{n,j}\le t)
=\exp\left[-e^{-2t}\sum_{r=0}^{j}\frac{(2t)^r}{r!}\right].
\]
At \(t=0\) the limiting cdf has an atom of size \(e^{-1}\), corresponding to an empty class. The limit describes the physical lengths and positions of rare low-degree chords, not just their numbers.

## Assumptions and scope
All endpoint angles are independent \(\operatorname{Uniform}(\mathbb T)\) variables. Their circular order induces a uniform perfect matching of \(N=2n\) endpoint labels, independent of their random circular spacings. The process concerns all crossings of straight chords inside the disk; crossing and degree are determined by alternating cyclic endpoint order. Fix \(K\) before letting \(n\to\infty\). Every measure \(\Xi_{n,j}\) is finite. Weak convergence is for finite measures, not merely vague convergence on bounded mark intervals; tightness of the entire marked mass is established below. The shape/rate convention is explicit: the \(\operatorname{Gamma}(j+1,2)\) density is \(2^{j+1}y^je^{-2y}/j!\) for \(y>0\).

For a chord \(c\), its *combinatorial length* \(\ell(c)\) is the smaller of the two counts of other endpoint labels lying strictly between its endpoints around the circle. This integer differs from its physical arc length and must not be conflated with it. For fixed \(j\) and all sufficiently large \(n\), the \(N\) candidate edges of combinatorial length \(j\) are precisely \(e_{i,j}=\{i,i+j+1\}\) with indices taken modulo \(N\); each occurs in the uniform matching with probability \(1/(N-1)\).

## Proof
**1. Independent matching and Dirichlet spacings.** Order the independent angular endpoints around the circle and choose a uniformly random origin angle \(U\). The successive normalized gaps \((G_i)_{i=1}^{N}\) have the Dirichlet distribution with every parameter one, independent of the perfect matching and of \(U\). Equivalently, let \(E_1,\ldots,E_N\) be independent rate-one exponential variables, \(S_N=\sum_{i=1}^N E_i\), and set \(G_i=E_i/S_N\). The angular location of endpoint \(i\) is \(\theta_i=U+\sum_{h<i}G_h\pmod1\). Almost surely, \(S_N/N\to1\) and \(\max_{1\le i\le N}|\sum_{h<i}G_h-i/N|\to0\); the latter follows from uniform control of the centered partial sums and normalization. These statements may equally be viewed as consequences of uniform order-statistic convergence.

**2. Exact candidate probabilities.** For each fixed \(j\le K\), candidate chord \(e_{i,j}\) spans \(j+1\) consecutive gaps. If \(m\) distinct prescribed candidate chords have pairwise disjoint endpoints, the exact probability that all occur is
\[
q_{N,m}=\prod_{h=0}^{m-1}\frac1{N-2h-1}.
\]
If two prescribed candidates share an endpoint, simultaneous occurrence has probability zero. A candidate has at most \(O_K(1)\) other candidates sharing one endpoint, so among all ordered arrays of \(m\) candidate chords of lengths at most \(K\), only \(O_{K,m}(N^{m-1})\) are incompatible. The same bound applies to arrays whose starting indices are closer than \(K+2\), ensuring disjoint sets of exponential gap variables. Since \(q_{N,m}=N^{-m}(1+O_m(N^{-1}))\), the total contribution of these exceptional arrays to any bounded factorial-moment test vanishes.

**3. Full marked Poisson convergence for combinatorial length.** Temporarily define \(\widetilde\Xi_{n,j}\) by marking every *present* candidate \(e_{i,j}\) with \(\theta_i\) and
\[
W_{i,j}=n\sum_{h=0}^{j}G_{i+h}
=\frac{n}{S_N}\sum_{h=0}^{j}E_{i+h},
\]
where cyclic indices are understood. Fix any finite array of types \(j_s\le K\), and test functions \(f_s\) that are bounded, continuous, and compactly supported on \(\mathbb T\times[0,\infty)\). Expand the corresponding mixed factorial moments as sums over ordered distinct candidate chords. The exceptional overlapping-index arrays from Step 2 have total contribution \(o(1)\). For the other arrays, the sums \(\sum_{h=0}^{j_s}E_{i_s+h}\) use disjoint exponential variables and are exactly independent Gamma variables with shape \(j_s+1\), rate one. Because \(n/S_N\to1/2\), their scaled limits have rate two. Uniformly in the endpoint index, \(\theta_{i_s}=U+i_s/N+o_p(1)\). Hence, averaging the bounded test functions over all \(m\)-tuples of starting indices produces a Riemann sum tending to
\[
\prod_{s=1}^{m}\int_{\mathbb T}\int_0^{\infty}
 f_s(u,y)\,du\,\frac{2^{j_s+1}}{j_s!}y^{j_s}e^{-2y}\,dy.
\]
A common random rotation \(U\) causes no dependence in this integral: the integration variables \(i_s/N\) are asymptotically independent uniform points, and translation of each by \(U\) preserves product Haar measure. The prescribed-matching factor \(q_{N,m}\) cancels the \(N^m\) candidate-index scale. Thus every fixed joint factorial moment measure converges to that of independent Poisson processes with the displayed intensities. The moments are uniformly bounded for each fixed order by the same candidate counting; the Poisson factorial moments uniquely determine the limit. Finite-dimensional process convergence follows for all continuity sets and hence for finite point measures with marks restricted to compact intervals.

To pass from compactly supported marks to full finite measures, use the exact expectation of the number of present length-\(j\) candidates whose marks exceed \(T\):
\[
\mathbb E\widetilde\Xi_{n,j}(\mathbb T\times(T,\infty))
=\frac{N}{N-1}\Pr\bigl(nB_{j+1,N-j-1}>T\bigr),
\]
where \(B_{a,b}\) is beta distributed. This quantity converges for each fixed \(T\) to the Gamma tail \(e^{-2T}\sum_{r=0}^{j}(2T)^r/r!\); letting \(T\to\infty\) makes the limit zero. Markov's inequality therefore gives the required tail tightness. The exact expected total number of candidates is \(N/(N-1)\), so total masses are tight as well. Consequently \((\widetilde\Xi_{n,j})_{j\le K}\) converges jointly to the asserted finite Poisson processes.

**4. Replace combinatorial length by crossing degree.** A chord of combinatorial length \(\ell\) has degree at most \(\ell\). For \(j\le K\), condition on a given candidate chord of length \(j\). If no two of the \(j\) interior endpoints are matched to each other, all \(j\) must be matched across the chord and its degree equals \(j\). The probability of an interior pair is bounded by \(\binom j2/(N-3)\) (for sufficiently large \(N\)), and the expected number of present length-\(j\) candidates is \(N/(N-1)\). Summing over the fixed finite set \(j\le K\), with probability \(1-O_K(N^{-1})\), every such chord has degree equal to its length.

The converse exclusion of low-degree chords with large combinatorial length requires a global argument, not a finite local check. Acan's Theorem 4.1 proves that for any \(k\) with \(k^2=o(n)\), the *induced subdiagram of chords of combinatorial length at least \(k\)* has minimum crossing degree at least \(k\), with probability tending to one. His proof bounds the expected number of violating chords by \(O(k^2/n)\). Apply this independently established theorem with \(k=K+1\) fixed. With probability tending to one, no chord of combinatorial length \(\ge K+1\) can have whole-diagram degree \(\le K\), since its degree in the full diagram is at least its degree in that subdiagram. Combining the two estimates, all chords of degrees \(0,\ldots,K\) are exactly the corresponding short combinatorial-length chords with probability tending to one.

For fixed \(j\), the \(j+1\) consecutive gaps summed by each present candidate tend to zero in probability, and their expected number is uniformly bounded; the probability any such candidate spans a physical arc of length at least \(1/2\) tends to zero by the preceding beta estimate. Therefore its chosen arc is indeed the shorter *physical* arc. Its midpoint differs from \(\theta_i\) by half its arc length, an amount \(o_p(1)\) on the circle. The probability of a mismatch of degree class, orientation, or an appreciable location shift tends to zero. The marked convergence in Step 3 thus transfers to the original \(\Xi_{n,j}\).

**5. Extreme marks.** A Gamma random variable with integer shape \(j+1\) and rate two exceeds \(t\ge0\) with probability \(e^{-2t}\sum_{r=0}^{j}(2t)^r/r!\). The number of marks larger than \(t\) in \(\Pi_j\) is Poisson with that mean, and its void probability gives the claimed cdf. Gamma marks have no atom at positive \(t\), so the convergence holds for every \(t>0\); at \(t=0\), convergence also follows from convergence of total point counts and the vanishing chance of a zero-length chord. This proves the corollary.

## Verification
The supplied Python 3 standard-library file `check_chords.py` exhaustively enumerates uniform perfect matchings up through six chords. It independently checks the exact expected numbers of combinatorial-length classes, joint factorial moments for the first three classes, and the finite occurrence of degree/length mismatches. It also tests the beta moment formulas exactly and performs seeded simulations at 300 chords to check the predicted class means, scaled-arc means and rotational uniformity. A fresh run reported **85 exact grouped checks and 9 seeded grouped checks**, all passing. The exact beta law provides an independent distributional check for each candidate, but the computational checks do not establish the infinite point-process theorem; Steps 1–5 establish it mathematically.

## Relationship to prior work
H. Acan, *On a uniformly random chord diagram and its intersection graph* (arXiv:1501.01489v1, January 7, 2015), Theorems 4.1 and 4.2, proves the low-degree core exclusion and independent Poisson limits for the **counts** of fixed short combinatorial lengths. Those theorems are used and credited, not claimed anew. Flajolet and Noy, *Analytic Combinatorics of Chord Diagrams* (INRIA RR-3914, March 2000), establishes unmarked random-chord structural limits. A published study titled *Gaussian–Poisson decoupling for local chords and global crossings* establishes joint limits of finite combinatorial-length counts and the normalized crossing statistic, but assumes fixed cyclic endpoint sites and does not state a physical circular-arc mark or continuous angular-location limit. *Spatial Poisson limits for near-diametral chords and independent Gaussian crossings* treats rare chords almost antipodal in **combinatorial** separation, not rare low-crossing-degree chords nor independent uniform physical-gap marks. A marked Poisson theorem for the low-degree classes with the explicit Gamma law and continuous physical localization is not implied solely by these unmarked count, crossing, or near-diametral statements. The factorial-moment proof here supplies the missing continuous-spacing argument.

## Limitations
The degree cutoff \(K\) is fixed. No convergence rate, growing-degree law, central-limit independence, or nonuniform endpoint-density extension is established. The global degree-to-length identification invokes Acan's published minimum-degree theorem, whose hypotheses hold here; the present proof does not claim a new proof of that theorem. General marked-point-process theorems or earlier unlocated work may contain an implication of the same result; absence from the inspected works is not a uniqueness guarantee. Independent mathematical validation remains outstanding.

## References
1. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, first posted 2015-01-07, especially Section 4, Theorems 4.1–4.2. https://arxiv.org/pdf/1501.01489
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914, March 2000, particularly the random-chord component and crossing results. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
3. *Gaussian–Poisson decoupling for local chords and global crossings*, publicly accessible scientific result, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-gaussian-poisson-decoupling-for-local-chords-and-global-crossing--30537820a0d6
4. *Spatial Poisson limits for near-diametral chords and independent Gaussian crossings*, publicly accessible scientific result, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-spatial-poisson-limits-for-near-diametral-chords-and-independent--8fd313fa5d9e
