# Exact second moments and lognormal-scale fluctuations of limited-permutation output spheres

## Finding

Let \(q\ge2\) be a fixed integer and let \(X=(X_1,\ldots,X_n)\) consist of independent uniformly random symbols from an alphabet of size \(q\), with \(n\ge1\). Let \(B_n(X)\) be the number of distinct strings obtained by applying any set of **pairwise disjoint adjacent swaps**, including the empty set. Put \(N=n-1\), \(p=(q-1)/q\), and \(a=1-p=1/q\). For Fibonacci numbers \(F_1=F_2=1\), \(F_{j+2}=F_{j+1}+F_j\), define

\[
\mu_q=a^2\sum_{t=0}^{\infty}p^t\log F_{t+2},\qquad
\sigma_q^2=a^2\sum_{t=0}^{\infty}p^t\bigl(\log F_{t+2}-\mu_q(t+1)\bigr)^2.
\]

These series converge absolutely and \(\mu_q,\sigma_q^2>0\). As \(n\to\infty\),

\[
\frac{\log B_n(X)}{n-1}\longrightarrow\mu_q\quad\text{almost surely},\qquad
\frac{\log B_n(X)-\mu_q(n-1)}{\sqrt{n-1}}\Longrightarrow\mathcal N(0,\sigma_q^2).
\]

There is also an **exact finite-length second-moment evaluator**, with no large-length assumption. Set \(m_0=1\), \(m_1=1+p\), and \(m_N=m_{N-1}+p m_{N-2}\) for \(N\ge2\). Set

\[
M_p=\begin{pmatrix}1&2&1\\p&p&0\\p&0&0\end{pmatrix},\qquad e=(1,0,0)^{\mathsf T},\qquad h=(1,2,1)^{\mathsf T}.
\]

Then, for every \(n\ge1\),

\[
\mathbb E B_n=m_{n-1},\qquad \mathbb E B_n^2=h^{\mathsf T}M_p^{n-1}e,\qquad
\operatorname{Var}(B_n)=h^{\mathsf T}M_p^{n-1}e-m_{n-1}^{2}.
\]

Let \(\lambda_q=(1+\sqrt{1+4p})/2\), and let \(\rho_q\) be the Perron eigenvalue of \(M_p\), equivalently the largest positive zero of

\[
P_p(z)=z^3-(1+p)z^2-2pz+p^2.
\]

For every fixed \(q\ge2\), **strict exponential relative-variance inflation** holds: \(\rho_q>\lambda_q^2\), and there exists \(C_q>0\) such that

\[
\frac{\operatorname{Var}(B_n)}{(\mathbb E B_n)^2}
\sim C_q\left(\frac{\rho_q}{\lambda_q^2}\right)^{n-1}.
\]

## Assumptions and scope

The output sphere contains **all** allowable disjoint adjacent swaps, not exactly one swap, not a sequence of potentially overlapping swaps, and not permutations of a fixed window. Equal adjacent symbols yield no new output. Every alphabet symbol has probability \(1/q\), independently across coordinates. Probabilities and limits are with respect to the random input center. Logarithms are natural, and the alphabet size \(q\) is fixed in the asymptotic statements.

## Proof

**1. Independent transition indicators.** For \(1\le i\le N\), let \(D_i=\mathbf 1\{X_i\ne X_{i+1}\}\). For any fixed transition pattern with \(k\) ones, there are exactly \(q(q-1)^k\) corresponding input strings: choose the first symbol arbitrarily, each zero forces equality, and each one allows \(q-1\) options. Thus

\[
\Pr\{(D_1,\ldots,D_N)=d\}=p^k a^{N-k},
\]

so the indicators are independent Bernoulli variables of parameter \(p\).

**2. Distinct outputs and transition-run products.** Disjoint effective swap sets are subsets of \(\{i:D_i=1\}\) containing no two consecutive indices. These sets yield distinct outputs: at the earliest site in the symmetric difference, the two resulting strings have distinct symbols in the earliest affected position. The number of such subsets for a run of \(t\) active sites is \(F_{t+2}\), by the standard path independent-set recurrence, and separate active runs multiply. Hence

\[
B_n(X)=\prod_{\text{maximal runs of ones of lengths }t}F_{t+2}.
\]

This deterministic formula is the established Fibonacci ball-volume identity, not a novelty claim here.

**3. Regenerative form and exact constants.** Extend the transition process to an infinite independent Bernoulli sequence. Let \(T_j\) be the number of consecutive ones before the \(j\)-th zero, so \(\Pr\{T_j=t\}=a p^t\). The complete cycles have lengths \(L_j=T_j+1\), rewards \(R_j=\log F_{T_j+2}\), and are independent and identically distributed. Their expected length is \(\mathbb E L_j=1/a\), while \(\mathbb E R_j=a\sum_{t\ge0}p^t\log F_{t+2}\). Thus reward per site is \(\mathbb E R_j/\mathbb E L_j=\mu_q\). Write \(K_N\) for the number of zeros in the first \(N\) indicators and \(U_N\) for the number of ones after its last zero (with \(U_N=N\) if none); then exactly

\[
\log B_n=\sum_{j=1}^{K_N}R_j+\log F_{U_N+2},\qquad
N=\sum_{j=1}^{K_N}L_j+U_N.
\]

The incomplete tail obeys \(\Pr\{U_N\ge u\}\le p^u\) for every \(1\le u\le N\). Since \(\log F_{t+2}=O(t+1)\), its contribution to the centered sum is \(O_{\mathbb P}(1)\) and is almost surely \(o(N)\). Also \(K_N/N\to a\) almost surely, by the ordinary Bernoulli strong law. The renewal reward strong law proves the almost-sure formula.

**4. Gaussian fluctuations.** Let \(Y_j=R_j-\mu_q L_j\). Its expectation vanishes and its variance is

\[
\mathbb E Y_j^2=a\sum_{t=0}^{\infty}p^t\bigl(\log F_{t+2}-\mu_q(t+1)\bigr)^2.
\]

The summands have exponential tails and therefore all moments are finite. The ordinary iid central limit theorem for \(\sum_{j\le\lfloor aN\rfloor}Y_j\), combined with the random-index (Anscombe) lemma because \(K_N/N\to a\), gives variance per site \(a\mathbb E Y_j^2=\sigma_q^2\). The incomplete-tail term is negligible after division by \(\sqrt N\). Since \(\Pr\{T_j=0\}=a>0\) and \(Y_j=-\mu_q\ne0\) on that event, \(\sigma_q^2>0\). Also \(\mu_q>0\) because \(\Pr\{T_j\ge1\}>0\) and \(F_{t+2}>1\) there.

**5. Exact first moment.** The sphere counts independent sets of a path of \(N\) Bernoulli-active sites. If the last site is omitted, the expected count is \(m_{N-1}\); if included, the preceding site must be omitted, contributing \(p m_{N-2}\). This yields the displayed recurrence and initial values. This average is also implied by the published enumerator for effective swap sets; it is not presented as a new result.

**6. Exact second moment.** Square the count and interpret it as ordered pairs \((S,T)\) of independent sets of the active sites. Process the sites from left to right and record whether the preceding site was used by neither set, by the first set only (or symmetrically by the second only), or by both sets. Let the four corresponding weighted sums be \((u,v,v,w)\), initialized at \((1,0,0,0)\). A new site unused by both has combined weight \(u+2v+w\); used only by the first has expected weight \(p(u+v)\); and used by both has expected weight \(pu\). Thus \((u',v',w')^{\mathsf T}=M_p(u,v,w)^{\mathsf T}\), proving the exact matrix formula. In these transitions, a site used by at least one set requires one Bernoulli success, not a separate success for each set. All expectations are consequently exact.

**7. Strict exponential dispersion.** The nonnegative matrix \(M_p\) has a strictly positive square for \(0<p<1\). Perron–Frobenius theory implies \(h^{\mathsf T}M_p^N e\sim c_2\rho_q^N\) with \(c_2>0\). The first-moment recurrence likewise gives \(m_N\sim c_1\lambda_q^N\) with \(c_1>0\). Direct determinant expansion gives \(\det(zI-M_p)=P_p(z)\). Using \(\lambda_q^2=\lambda_q+p\) yields the exact sign identity

\[
P_p(\lambda_q^2)=\lambda_q p(p-1)<0.
\]

Since \(P_p(z)\to+\infty\) as \(z\to\infty\), it has a real positive root strictly exceeding \(\lambda_q^2\). Its spectral radius \(\rho_q\) is at least that root. Hence \(\rho_q>\lambda_q^2\), and subtracting \(m_N^2\) from the second-moment asymptotic proves the final expression with \(C_q=c_2/c_1^2>0\).

## Verification

The standalone file `check_lpc.py` enumerates every possible string of length \(1\) through \(12\) for alphabet size \(2\), length \(1\) through \(9\) for alphabet size \(3\), and length \(1\) through \(7\) for alphabet size \(4\). For each input it constructs the output set directly, independently counts effective-swap matchings by a recurrence, and compares exact rational first and second moments with the transfer matrix. The \(59{,}557\) source instances passed. Additional exact rational calculations checked positive finite-length variances for selected longer lengths. These finite computations are sanity checks, **not** proofs of the infinite statements; steps 1–7 supply those proofs.

## Relationship to prior work

Kovačević, Kiah and Goyal (2025 initial release; updated 2026) study precisely the pairwise disjoint adjacent-transposition channel and derive a complete finite enumeration of average spheres (Proposition 6 and Remark 2); the first-moment recurrence above is included only to compare scales. The established Fibonacci run formula was explicitly stated by Langberg, Schwartz and Yaakobi (2017) and restated in Ben Shimon and Zabokritskiy (2026, Lemma 8). The present claim concerns **source-random logarithmic fluctuations, its explicit regenerative constants, the exact second moment, and the strict exponential divergence of relative variance**, none of which is supplied by those cited formulas alone. General central-limit results for disordered monomer–dimer systems give related probabilistic context and reduce any claim of novelty for a CLT in that broader model; this theorem instead gives channel-specific constants and an independent finite-moment identity with an explicit spectral separation.

## Limitations

Only the uniformly independent source and the full radius-one limited-permutation output sphere are treated. The results do not give an optimal correcting code, an error exponent for arbitrary source laws, or distributional limits when the alphabet size varies with length. Existing general disordered-matching theorems may overlap with the qualitative central-limit assertion; historical priority of every specialized formula is not independently certified.

## References

1. M. Kovačević, H. M. Kiah and K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, first public preprint September 8, 2025, arXiv:2509.06692, Proposition 6 and Remark 2. https://arxiv.org/abs/2509.06692
2. N. Ben Shimon and A. L. Zabokritskiy, *A q-ary Local Criterion for the Radius-One Limited Permutation Channel and Almost-Optimal Binary Block-Concatenation Codes*, first public preprint June 25, 2026, arXiv:2606.26905, Lemma 8, pp. 18–19. https://arxiv.org/abs/2606.26905
3. M. Langberg, M. Schwartz and E. Yaakobi, *Coding for the ℓ-infinity-Limited Permutation Channel*, IEEE Transactions on Information Theory 63 (2017), 7676–7686, Theorem 10 (as cited and restated in reference 2). DOI:10.1109/TIT.2017.2762676.
4. N. Ben Shimon and A. L. Zabokritskiy, *Extinction Depth and q-ary Error-Correcting Codes for the Limited Permutation Channel*, arXiv:2607.19566 (2026), related finite-state correction and covering work. https://arxiv.org/abs/2607.19566
5. W.-K. Lam and A. Sen, *Central limit theorem in disordered Monomer–Dimer model*, first published August 7, 2024 (journal issue 2025), Random Structures & Algorithms, DOI:10.1002/rsa.21256, broader related fluctuation theory. https://doi.org/10.1002/rsa.21256
