# Exact variance and a Gaussian law for permutation-averaged exponential pair contrasts

## Finding
For every even integer \(N\ge2\), take independent \(\operatorname{Exp}(\lambda)\) observations \(Z_1,\ldots,Z_N\), where \(\lambda>0\) is arbitrary. Independently generate \(B\ge1\) uniform random perfect matchings of the observations, sampling matchings independently with replacement. For one matching \(M\), form
\[
R_M=\frac2N\sum_{\{i,j\}\in M}h(Z_i,Z_j),\qquad h(x,y)=\frac{|x-y|}{x+y},
\]
and let \(A_{N,B}\) be the mean of the \(B\) resulting values. This is exactly the zero-threshold version of the repeated-pairing statistic in Karagrigoriou, Mavrogiannis, Papasotiriou and Vonta (2023), without the tail-exceedance indicators.

Put \(q(x)=\mathbb E[h(x,Y)]\), for \(Y\sim\operatorname{Exp}(1)\), and
\[
\zeta=\int_0^\infty e^{-x}\left(q(x)-\tfrac12\right)^2\,dx=0.0158672827997\ldots.
\]
Then, **for every finite even \(N\) and every positive integer \(B\)**,
\[
\boxed{\mathbb E A_{N,B}=\tfrac12,\qquad
\operatorname{Var}(A_{N,B})=V_N+\frac{1}{B}\left(\frac1{6N}-V_N\right),\qquad
V_N=\frac{4(N-2)\zeta+1/6}{N(N-1)}.}
\]
In particular, averaging \(50\) independently sampled matchings removes **exactly \(98\%\)** of the removable (matching-induced) variance for any \(N\ge4\), while the irreducible sampling variance remains positive.

For fixed \(B\), as even \(N\to\infty\),
\[
\boxed{\sqrt N(A_{N,B}-\tfrac12)\ \xrightarrow{\mathcal D}\
\mathcal N\!\left(0,\;4\zeta+\frac1B(\tfrac16-4\zeta)\right).}
\]
If \(B=B_N\to\infty\) at an arbitrary rate, the same central limit theorem holds with variance \(4\zeta\). The asymptotic variance of the complete-pair average is \(0.38081478719\ldots\) times the variance of one random pairing, and at \(B=50\) that fraction is \(0.39319849145\ldots\). Treating the \(50\) repetitions as statistically independent would underestimate their true asymptotic variance by a factor \(19.65992457\ldots\); this conditional statement is not a claim about how the published procedure is actually calibrated.

## Assumptions and scope
The data are iid with a common exponential law of arbitrary positive rate; no unknown rate needs estimating because the kernel is scale invariant. All \(B\) perfect matchings are independently sampled with replacement from the \((N-1)!!\) possible matchings and are independent of the data. \(N\) is even; the statistic uses the entire sample, corresponding to the published procedure's exploratory threshold \(d=0\). The theorem is **not** asserted for positive or data-dependent tail thresholds, for dependent observations, or for matchings selected adaptively by their scores.

## Proof
**(1) One-pair law.** If \(X,Y\) are independent exponential observations of the same rate, \(X/(X+Y)\) is uniform on \((0,1)\) and independent of \(X+Y\). Hence \(h(X,Y)=|2X/(X+Y)-1|\) is also uniform on \((0,1)\), with mean \(1/2\) and variance \(1/12\). Disjoint pairs in a single matching are independent. Thus \(\mathbb E R_M=1/2\) and \(\operatorname{Var}(R_M)=1/(6N)\).

**(2) Exact projection and strict nondegeneracy.** With \(E_1(t)=\int_t^\infty e^{-s}s^{-1}\,ds\), direct integration on \((0,x)\) and \((x,\infty)\) gives, for \(x>0\),
\[
q(x)=-1+2e^{-x}+2xe^x\big[E_1(x)-2E_1(2x)\big].
\]
Set \(g(x)=q(x)-1/2\) and \(r(x,y)=h(x,y)-1/2-g(x)-g(y)\). Then \(\mathbb E[g(X)]=0\), \(\mathbb E[r(X,Y)\mid X]=\mathbb E[r(X,Y)\mid Y]=0\), and
\[
\operatorname{Var}(h(X,Y))=2\zeta+\operatorname{Var}(r(X,Y))=\tfrac1{12}.
\]
Here \(\zeta>0\), because \(q(x)\to1\) as \(x\downarrow0\) whereas \(\mathbb E q(X)=1/2\). Also \(\operatorname{Var}(r)>0\): otherwise \(h(x,y)\) would be the sum of one-coordinate functions almost everywhere and, by continuity on the positive quadrant, everywhere; evaluating \(h(x,x)=0\) would force the kernel to be constant, contradicting \(h(x,y)>0\) for \(x\ne y\). Therefore \(0<\zeta<1/24\).

**(3) The full-matching conditional mean.** Given the observations, any unordered pair is included in a uniformly selected matching with probability \(1/(N-1)\). Consequently
\[
U_N:=\mathbb E[R_M\mid Z_1,\ldots,Z_N]
=\frac{2}{N(N-1)}\sum_{i<j}h(Z_i,Z_j).
\]
For different unordered pairs, their centered kernel values have covariance \(\zeta\) if they share exactly one index, and covariance zero if disjoint. Counting the \(\binom N2\) diagonal terms and the \(2(N-2)\) ordered, single-index overlaps per edge gives
\[
\operatorname{Var}(U_N)=\frac{4(N-2)\zeta+1/6}{N(N-1)}=V_N.
\]
Given the observations, the \(B\) matching statistics are independent and identically distributed. Total variance therefore yields
\[
\operatorname{Var}(A_{N,B})=\operatorname{Var}(U_N)+\frac1B\mathbb E\operatorname{Var}(R_M\mid Z_1,\ldots,Z_N)
=V_N+\frac{1}{B}(\tfrac1{6N}-V_N).
\]
Since \(\frac1{6N}-V_N=(N-2)(\frac16-4\zeta)/[N(N-1)]>0\) for \(N\ge4\), the fraction of removable variance eliminated by \(B\) matchings is exactly \(1-1/B\).

**(4) Fixed number of matchings: central limit theorem.** Condition on the independently sampled matchings and retain every matched pair as a tagged edge of a multigraph on \(N\) vertices. There are \(NB/2\) tagged edges, and every vertex has degree \(B\). Centered edge variables are uniformly bounded and have a dependency graph with maximum degree at most \(2(B-1)\). For each pair of matchings let \(K\) be their number of common edges. Their conditional covariance is exactly
\[
\operatorname{Cov}(R_{M_b},R_{M_c}\mid M_b,M_c)
=\frac4{N^2}\left[(N-2K)\zeta+\frac K{12}\right].
\]
For independent uniform matchings, \(\mathbb EK=N/[2(N-1)]\), hence \(K/N\to0\) in probability. With \(B\) fixed, the conditional variance of \(\sqrt N A_{N,B}\) therefore tends in probability to \(4\zeta+(1/B)(1/6-4\zeta)>0\). Every joint cumulant of fixed order \(r\ge3\) of the unscaled tagged-edge sum is \(O(N)\): a nonzero joint cumulant requires a connected \(r\)-tuple in a uniformly bounded-degree dependency graph, and edge variables are bounded. After division by \(N^{r/2}\), these cumulants vanish. The conditional method of moments gives the stated Gaussian law, and averaging over matchings removes the conditioning.

**(5) Growing number of matchings.** The standard nondegenerate degree-two U-statistic projection yields \(\sqrt N(U_N-1/2)\Rightarrow\mathcal N(0,4\zeta)\). For every \(B_N\to\infty\), the exact identity implies
\[
N\,\mathbb E[(A_{N,B_N}-U_N)^2]
=\frac N{B_N}(\tfrac1{6N}-V_N)\le\frac1{6B_N}\longrightarrow0.
\]
Slutsky's theorem completes the assertion with no restriction on the rate of growth of \(B_N\).

## Verification
Run the accompanying source file `verify.py` with Python 3, NumPy and SciPy. It verifies the special-function formula by independent quadratures, computes the numerical constant, checks all-perfect-matching means for samples of sizes \(2,4,6\), the exact variance and variance-savings algebra, and independently simulates several small-sample variances with seeded exponential draws and fresh random matchings. It passed \(54\) assertions at preparation. Numerical evaluations corroborate constants but do not substitute for the exact argument above.

## Relationship to prior work
Karagrigoriou et al. (2023), equations (10)–(13), define the same pair kernel and average \(B=50\) random permutations; their figures explicitly include the \(d=0\) baseline. They supply fixed-threshold asymptotics for single pair collections and simulations but not the stated exact \(B\)-matching variance, its numeric irreducible floor, or the fixed-\(B\) dependent-pairing normal law. Papasotiriou's publicly deposited 2021 thesis describes the same exponentiality-test research program, with simulated distributions and critical values in the relevant sections; the inspected material does not state the formula here. Classical Hoeffding projection theory, U-statistics and bounded-degree dependency-graph methods provide general tools, credited as such; the contribution claimed here is their quantitative application to the particular permutation-averaged normalized-ratio statistic, not invention of those tools.

## Limitations
This is a zero-threshold baseline calibration theorem, **not** a result for the positive, typically high-quantile thresholds recommended for tail detection. The number \(19.6599\ldots\) describes what would happen **if** the correlated permutations were treated as independent; it does not establish that the published simulation-based critical values use that shortcut. The numerical constant is given as a convergent special-function integral rather than a proven elementary closed form. Historical priority of synonymous pairwise-ratio U-statistics and the 2022 edited-volume precursor could not be exhaustively excluded; the thesis and full 2023 paper were materially inspected. No independent mathematical audit has been performed.

## References
1. Karagrigoriou, A., Mavrogiannis, I., Papasotiriou, G., and Vonta, I. (2023), *An Exponentiality Test of Fit Based on a Tail Characterization against Heavy and Light-Tailed Alternatives*, Risks 11(10), 169, doi:10.3390/risks11100169, https://www.mdpi.com/2227-9091/11/10/169 (Sections 3.1–3.4).
2. Papasotiriou, G. (2021), *Non Parametric Test for the Exponential Distribution*, master's thesis, National Technical University of Athens, public repository item posted 2021-09-28, https://dspace.lib.ntua.gr/xmlui/handle/123456789/53900 (Chapter 2).
3. Karagrigoriou, A., Papasotiriou, G., and Vonta, I. (2022), *Goodness of fit exponentiality test against light and heavy tail alternatives*, in *Statistical Modeling of Reliability Structures and Industrial Processes*, pp. 25–38 (precursor bibliographically identified but full text unavailable).
4. Hoeffding, W. (1948), *A Class of Statistics with Asymptotically Normal Distribution*, Annals of Mathematical Statistics 19, 293–325 (general U-statistic methods).
