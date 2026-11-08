# Gaussian pass-count fluctuations in resampled record filtering

## Finding

For every integer \(n\ge 1\), start with \(n\) independent observations from any atomless distribution. In a pass, retain all strict left-to-right records, remove those records from further processing, and **replace the remaining nonrecords** by independent observations from the original distribution. Repeat until no observations remain. Let \(D_n\) count passes, with \(D_0=0\). Write
\[
H_m=\sum_{j=1}^m\frac1j,\qquad A_n=\sum_{m=1}^n\frac1{H_m}.
\]
Then, as \(n\to\infty\),
\[
\boxed{\frac{D_n-A_n}{\sqrt n/\log n}\ \Longrightarrow\ N(0,1).}
\]
Moreover \(0\le A_n-\mathbb ED_n=O(\log n)\), so the same central limit theorem holds after centering at \(\mathbb ED_n\). The deterministic center satisfies
\[
A_n=\frac n{\log n}+\frac{(1-\gamma)n}{(\log n)^2}+O\!\left(\frac n{(\log n)^3}\right),
\]
where \(\gamma\) is the Euler--Mascheroni constant. In particular \(D_n/(n/\log n)\to1\) in probability. The exact \(A_n\), not any fixed truncation of its logarithmic expansion, provides a center accurate on the Gaussian scale.

## Assumptions and scope

Each pass is freshly and independently resampled, conditional only on the number of surviving nonrecords. The initial sampling distribution is atomless, with no moment or density assumption. This is **not** the non-resampling filtering algorithm, whose number of passes equals a longest decreasing subsequence statistic and has a different scale. All limits hold along positive integers with no adjustable parameters; logarithms are natural. The claimed Gaussian convergence is weak convergence, not an assertion of convergence of variances or a finite-sample normal approximation rate.

## Proof

**1. Exact decrement law.** If \(m\ge1\) items enter a pass, their upper-record count \(R_m\) has the law
\[
R_m\stackrel d=\sum_{j=1}^m B_j,\qquad B_j\ \text{independent},\quad\Pr(B_j=1)=1/j.
\]
Indeed, the relative rank at each successive insertion is uniform on its available ranks, independently over insertions. Consequently
\[
\mathbb ER_m=H_m,\qquad v_m:=\operatorname{Var}(R_m)=H_m-\sum_{j=1}^m j^{-2},
\]
and the current list length follows the strictly descending Markov chain \(M_{t+1}=M_t-R_{M_t}\), started at \(M_0=n\), absorbed at zero after \(D_n\) steps. New copies of \(R_m\) are sampled independently at each step. As sums of independent bounded Bernoulli variables, these counts satisfy \(\mathbb E R_m^4\le C H_m^4\), \(\mathbb E(R_m-H_m)^4\le C H_m^2\) for an absolute constant \(C\).

**2. Harmonic potential and controlled drift debt.** Define \(A(0)=0\) and \(A(m)=\sum_{k=1}^m H_k^{-1}\). For every \(1\le r\le m\), put
\[
\delta(m,r):=A(m)-A(m-r)-r/H_m
=\sum_{j=0}^{r-1}\left(H_{m-j}^{-1}-H_m^{-1}\right)\ge0.
\]
For \(r\le m/2\), since \(H_m-H_{m-j}\le2j/m\) and \(H_{m-j}\ge H_{\lceil m/2\rceil}\ge H_m/2\),
\[
0\le\delta(m,r)\le C\frac{r^2}{mH_m^2}.
\]
For \(r>m/2\), \(\delta(m,r)\le A(m)\le m\). The fourth moment of \(R_m\) gives \(\Pr(R_m>m/2)\le C H_m^4/m^4\). Using \(\sup_{m\ge1}H_m^4/m^2<\infty\) and \(\mathbb ER_m^2\le2H_m^2\), we obtain the uniform bound
\[
0\le\mathbb E\delta(m,R_m)\le C/m.
\]
Because the positive states \(M_t\) are all distinct, the total drift debt \(U_n=\sum_{t<D_n}\delta(M_t,R_{M_t})\) satisfies
\[
0\le \mathbb EU_n\le C\sum_{m=1}^n\frac1m=O(\log n).
\]
Define martingale differences \(Y_t=(R_{M_t}-H_{M_t})/H_{M_t}\) until absorption, and zero thereafter. Telescoping the potential gives the **exact path identity**
\[
D_n-A_n=-\sum_{t<D_n}Y_t-U_n.
\]
Thus \(U_n/(\sqrt n/\log n)\to0\) in \(L^1\) and probability, and, on taking expectations, \(0\le A_n-\mathbb ED_n=O(\log n)\).

**3. Predictable quadratic variation.** The martingale has predictable quadratic variation
\[
Q_n=\sum_{t<D_n}\frac{v_{M_t}}{H_{M_t}^2}.
\]
Fix \(\varepsilon\in(0,1)\). Stop first when the state is at most \(\varepsilon n\), and call the number of steps \(T_\varepsilon\). Uniformly over \(\varepsilon n\le m\le n\),
\[
H_m=\log n+O_\varepsilon(1),\qquad v_m=\log n+O_\varepsilon(1).
\]
The cumulative centered decrement up to that stopping time has variance at most \(nH_n=O(n\log n)\), since there are at most \(n\) decrements. The crossing overshoot is \(o_{\mathsf P}(n)\): for example, a union bound over at most \(n\) steps and the uniform fourth-moment estimate gives \(\Pr(\max R_{M_t}>n^{1/3})\le Cn(\log n)^4/n^{4/3}\to0\). Comparing total depletion with its conditional mean therefore yields
\[
\frac{T_\varepsilon\log n}{n}\ \xrightarrow{\mathsf P}\ 1-\varepsilon,
\qquad
\frac{\log^2n}{n}\sum_{t<T_\varepsilon}\frac{v_{M_t}}{H_{M_t}^2}\ \xrightarrow{\mathsf P}\ 1-\varepsilon.
\]
For the remaining states \(n^{1/3}\le m\le\varepsilon n\), conditional drift is at least \(H_{\lceil n^{1/3}\rceil}\ge(\log n)/3\). The total decrease in that region cannot exceed \(\varepsilon n\), so its expected number of visits is at most \(3\varepsilon n/\log n\). Since \(v_m/H_m^2\le 1/H_m\le3/\log n\), the expected contribution of that region to \(Q_n\) is at most \(9\varepsilon n/\log^2n\). Below \(n^{1/3}\) there are at most \(n^{1/3}\) visits, and each contribution is at most one. First let \(n\to\infty\), then \(\varepsilon\downarrow0\). Nonnegativity gives
\[
\boxed{Q_n/(n/\log^2n)\ \xrightarrow{\mathsf P}\ 1.}
\]

**4. Lindeberg condition and conclusion.** With \(b_n=\sqrt n/\log n\), the fourth-centered-moment bound from Step 1 gives \(\mathbb E(Y_t^4\mid\mathcal F_t)\le C\) on each visited state. There are at most \(n\) steps. For each \(\eta>0\),
\[
\frac1{b_n^2}\sum_{t<D_n}\mathbb E\!\left[Y_t^2\,\mathbf1_{\{|Y_t|>\eta b_n\}}\mid\mathcal F_t\right]
\le \frac{Cn}{\eta^2b_n^4}=O\!\left(\frac{\log^4n}{n}\right)\to0.
\]
The triangular-array martingale central limit theorem applied to Step 3 and this conditional Lindeberg condition gives \(\sum_{t<D_n}Y_t/b_n\Longrightarrow N(0,1)\). Combine with the exact path identity and the negligible drift debt. The usual asymptotic for harmonic numbers, followed by summation or integral comparison, gives the displayed expansion for \(A_n\). The CLT implies the first-order probability limit because \(b_n=o(n/\log n)\). This completes the proof.

## Verification

The standalone `verify_rds.py` uses exact rational Stirling-number transition probabilities and, independently, enumerates all permutations through size seven. It verifies conditional record-count moments, mean and second-moment absorbing recursions, the nonnegative potential correction, and the potential/mean-debt identity through size thirteen. Its recorded execution produced `PASS: 146 exact rational / permutation assertions`. An additional exploratory simulation at sizes \(1000\), \(3000\) and \(12000\) gave standardized empirical standard deviations approximately \(0.944\), \(0.967\) and \(0.977\), respectively, using 3000 sample paths per size. Neither finite method proves the asymptotic theorem; the proof above is the evidence for the infinite claim.

Run the checker with `python3 verify_rds.py`; it uses only the Python standard library and no external data. The simulation is described for contextual stress testing and is not required for verification.

## Relationship to prior work

Zariski and Kratter, *Recursive Record Filtering and Longest Decreasing Subsequences* (first publicly available 2026-04-26, arXiv:2604.23825), define this resampling model and give the exact Stirling-number recurrence for its expectation (their Theorem 3); their asymptotic Tracy--Widom statements concern **non-resampling** filtering instead. The present claim is a Gaussian limit with an explicit fluctuation scale and an accurate deterministic center for the resampled model, neither supplied by that recurrence alone.

Alsmeyer, Kabluchko and Marynych, *A leader-election procedure using records* (arXiv:1512.04750; *Annals of Probability* 2017), independently **retain** the records at each round; the size chain is then \(m\mapsto R_m\), rather than the present \(m\mapsto m-R_m\). Its iterated-logarithm-scale duration is not an absorption-time law for this model.

Chern, Jiu and Simonelli, *A central limit theorem for a card shuffling problem* (arXiv:2309.08841), prove a Gaussian limit for a merging process with a different decrement law and a linear number of rounds. Their general recurrence theorems concern that process's transition coefficients, not the Stirling record-removal decrement. Standard martingale central limit theorems provide a method but do not by themselves furnish the harmonic-potential comparison and occupation-time estimates here.

## Limitations

The theorem is specific to independent fresh resampling at each pass and atomless observations. It does not cover the non-resampling algorithm, data-dependent resampling, ties, nonidentical observations or a quantitative Berry--Esseen rate. The exact finite checker is not a proof of limiting normality. Historical priority relative to general stochastic-depletion central limit theorems may require further independent review, even though no directly covering statement was located in the listed full-text and targeted comparisons.

## References

1. J. Zariski and K. Kratter, *Recursive Record Filtering and Longest Decreasing Subsequences*, arXiv:2604.23825 (first posted 2026-04-26), https://arxiv.org/abs/2604.23825.
2. G. Alsmeyer, Z. Kabluchko and A. Marynych, *A leader-election procedure using records*, *Annals of Probability* 45 (2017), 4348--4388, arXiv:1512.04750, https://arxiv.org/abs/1512.04750.
3. S. Chern, L. Jiu and I. Simonelli, *A central limit theorem for a card shuffling problem*, arXiv:2309.08841 (2023), https://arxiv.org/abs/2309.08841.
4. P. Hall and C. C. Heyde, *Martingale Limit Theory and Its Application*, Academic Press (1980), for the standard martingale central limit theorem used in Step 4.
