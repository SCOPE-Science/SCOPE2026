# Parabolic stochastic dynamics: full path-measure classes and a critical rare-visit window

## Finding

The qualitative convergence of a nonlinear stochastic operator does not by itself determine the support or equivalence class of the path laws generated from its iterates. The following complete model calculation resolves these distinctions for a natural parabolic family. In particular, it supplies positive, distinct choices of Markov-row seeds for which the associated measures are **equivalent even though the usual summability condition fails**.

**Theorem.** For every \(\gamma>0\), define on the two-state simplex
\[
S^1=\{(1-s,s):0\le s\le1\},\qquad
h_\gamma(s)=\begin{cases}(s^{-\gamma}+1)^{-1/\gamma},&s>0,\\0,&s=0,\end{cases}
\qquad W_\gamma(1-s,s)=(1-h_\gamma(s),h_\gamma(s)).
\]
This is an \(F\)-stochastic operator in the terminology of Souissi--Mukhamedov, and every orbit tends to \((1,0)\). Let \(s_0,s_1\in(0,1]\), let \(\pi_0,\pi_1>0\) sum to one, and define the associated nonhomogeneous Markov law \(\mathbb P_{\gamma,s,\pi}\) on \(\{0,1\}^{\mathbb N_0}\) by \(\Pr(Z_0=i)=\pi_i\) and
\[
\Pr(Z_n=1\mid Z_{n-1}=i)
=\bigl(n+s_i^{-\gamma}\bigr)^{-1/\gamma},
\quad n\ge1,\ i\in\{0,1\}.
\]

(i) Let \(\mathbb Q_{\gamma,\pi}\) be the product law with the same initial distribution and independent coordinates satisfying
\[
\mathbb Q_{\gamma,\pi}(B_n=1)=(n+1)^{-1/\gamma},\quad n\ge1.
\]
Then \(\mathbb P_{\gamma,s,\pi}\sim\mathbb Q_{\gamma,\pi}\). Moreover these laws admit a coupling under which \(Z_n=B_n\) for all sufficiently large \(n\), almost surely. Both assertions hold regardless of whether the tail probability series converges.

(ii) Given any two such laws (with possibly different positive row seeds and full-support initial distributions) having exponents \(\gamma,\delta>0\), their **complete equivalence--singularity classification** is
\[
\mathbb P_{\gamma,s,\pi}\sim\mathbb P_{\delta,t,\rho}
\quad\Longleftrightarrow\quad
\gamma=\delta\ \text{or}\ (\gamma<1\ \text{and}\ \delta<1).
\]
Otherwise the two path measures are mutually singular. Thus there is one equivalence class for all \(0<\gamma<1\), and a distinct equivalence class for each \(\gamma\ge1\).

(iii) With \(K_N=\sum_{n=1}^N\mathbf1_{\{Z_n=1\}}\) and
\[
\mu_\gamma(N)=\sum_{n=1}^N(n+1)^{-1/\gamma},
\]
if \(0<\gamma<1\) then \(K_\infty<\infty\) almost surely; if \(\gamma\ge1\) then
\[
\frac{K_N}{\mu_\gamma(N)}\longrightarrow1\quad\text{almost surely},
\qquad
\frac{K_N-\mu_\gamma(N)}{\sqrt{\mu_\gamma(N)}}
\ \Longrightarrow\ \mathcal N(0,1).
\]
Here \(\mu_1(N)\sim\log N\), and for \(\gamma>1\), \(\mu_\gamma(N)\sim N^{1-1/\gamma}/(1-1/\gamma)\).

(iv) Fix \(u\in\mathbb R\), and in the \(N\)-th finite-time experiment replace \(\gamma\) by \(\gamma_N=1+u/\log N>0\), keeping the row seeds and initial distribution fixed. Then, as \(N\to\infty\),
\[
\frac{K_N-\ell(u)\log N}{\sqrt{\log N}}
\ \Longrightarrow\ \mathcal N(0,\ell(u)),
\qquad
\ell(u)=\begin{cases}(e^u-1)/u,&u\ne0,\\1,&u=0.\end{cases}
\]
The law of large numbers \(K_N/\log N\to\ell(u)\) holds in probability. This is the explicit logarithmic-width crossover between finite rare-state occupancy and power-law-divergent occupancy.

## Assumptions and scope

All path measures use the two-state transition convention in the cited papers: the \(i\)-th row of the step-\(n\) transition matrix is \(W_\gamma^{\circ n}(1-s_i,s_i)\), for \(n\ge1\). The two seeds may coincide; for the nontrivial nonsummable equivalence counterexample they can be chosen distinct, for example \(s_0=1/2\), \(s_1=2/3\), and compared with a different pair such as \(t_0=1/3\), \(t_1=1\), all with strictly positive initial state probabilities. The statements are for fixed finite \(\gamma\in(0,\infty)\) except in the triangular critical experiment in part (iv), where \(\gamma_N\) varies with the observation horizon. No independence is assumed for the original Markov coordinates.

The deterministic map is an \(F\)-stochastic operator: take \(f(s)=\varphi(s)=g(s)=h_\gamma(s)\), extending \(h_\gamma\) continuously to the nonnegative half-line for \(\varphi\). Then \(\varphi(s)>0\) for \(s>0\), \(f\le\varphi\), and
\[
\varphi(W_\gamma(1-s,s))=h_\gamma(h_\gamma(s))
=g(1-(W_\gamma(1-s,s))_0).
\]
The function \(g\) is continuous and increasing on \([0,1]\), and its iterates tend to zero. The source condition \(\sum_{n\ge1}g^{\circ n}(x)<\infty\) holds exactly when \(\gamma<1\) for every fixed \(x>0\).

## Proof

**Step 1: Exact parabolic iterates.** For \(s>0\),
\[
h_\gamma(s)^{-\gamma}=s^{-\gamma}+1.
\]
Induction gives \(h_\gamma^{\circ n}(s)=(s^{-\gamma}+n)^{-1/\gamma}\); the same formula at \(s=0\) follows by continuity. This supplies the transition probabilities stated in the theorem, as well as convergence to \((1,0)\).

**Step 2: Finite-defect Bernoulli coupling.** Put \(\alpha=1/\gamma\), \(a_i=s_i^{-\gamma}\ge1\), and \(b_n=(n+1)^{-\alpha}\). On a probability space with independent uniforms \(U_1,U_2,\ldots\), start \(Z_0=B_0\) with distribution \(\pi\) and set
\[
Z_n=\mathbf1_{\{U_n\le(n+a_{Z_{n-1}})^{-\alpha}\}},
\qquad B_n=\mathbf1_{\{U_n\le b_n\}}.
\]
The marginal path laws are \(\mathbb P\) and \(\mathbb Q\). By the mean-value theorem applied to \(x\mapsto x^{-\alpha}\), uniformly in the previous state,
\[
0\le b_n-(n+a_i)^{-\alpha}
\le \alpha(a_i-1)(n+1)^{-1-\alpha}.
\]
Consequently,
\[
\sum_{n\ge1}\Pr(Z_n\ne B_n)
\le\alpha\max_i(a_i-1)\sum_{n\ge1}(n+1)^{-1-\alpha}<\infty.
\]
The first Borel--Cantelli lemma implies almost-sure eventual coordinate agreement. In particular \(K_N-\sum_{n=1}^NB_n\) eventually becomes a finite, random integer, not merely a lower-order error in probability.

**Step 3: Mutual absolute continuity, stronger than eventual agreement.** The coupling alone does not establish equivalence of path laws, so verify it separately. All transition entries are strictly between zero and one. For the finite-coordinate likelihood \(L_N=d\mathbb P|_{\mathcal F_N}/d\mathbb Q|_{\mathcal F_N}\), conditional on \(Z_{n-1}=i\) under \(\mathbb Q\), the second moment of the step likelihood equals
\[
\frac{p_{i,n}^2}{b_n}+\frac{(1-p_{i,n})^2}{1-b_n}
=1+\frac{(p_{i,n}-b_n)^2}{b_n(1-b_n)},
\qquad p_{i,n}=(n+a_i)^{-\alpha}.
\]
The coupling estimate shows \(p_{i,n}-b_n=O(n^{-1-\alpha})\) uniformly in \(i\). Because \(b_n\asymp n^{-\alpha}\) and \(1-b_n\) is bounded below by the positive constant \(1-2^{-\alpha}\), the fraction is \(O(n^{-2-\alpha})\). Iterated conditional expectation yields
\[
\sup_N\mathbb E_{\mathbb Q}L_N^2
\le\prod_{n\ge1}\left(1+\sup_i\frac{(p_{i,n}-b_n)^2}{b_n(1-b_n)}\right)<\infty.
\]
Uniform \(L^2\)-integrability of this likelihood martingale gives \(\mathbb P\ll\mathbb Q\). Interchanging the laws produces the analogous bound with denominator \(p_{i,n}(1-p_{i,n})\), also \(O(n^{-2-\alpha})\) because \(p_{i,n}\asymp b_n\), and yields \(\mathbb Q\ll\mathbb P\). The initial distributions agree here; replacing one strictly positive initial distribution by another affects only a finite likelihood factor. This proves part (i).

**Step 4: Entire phase diagram.** If \(\gamma<1\), then \(\alpha>1\) and \(\sum_n b_n<\infty\). The Bernoulli product law puts probability one on the **countable** set of binary sequences with only finitely many ones; moreover each such sequence has positive mass, since all one-step probabilities lie strictly between zero and one and \(\prod_n(1-b_n)>0\). Thus all product laws with \(\gamma<1\), regardless of exponent, are equivalent. Via Step 3, the corresponding Markov measures are equivalent as well.

If \(\gamma\ge1\), the independent reference counting process \(S_N=\sum_{n=1}^NB_n\) satisfies \(S_N/\mu_\gamma(N)\to1\) almost surely, proved in Step 5. The coupling transfers the same law to \(K_N\). If \(\gamma>\delta\) with \(\gamma\ge1\), then \(\mu_\delta(N)/\mu_\gamma(N)\to0\): this also holds when \(\delta<1\), because then the numerator stays bounded. Hence the measurable path event
\[
\lim_{N\to\infty}K_N/\mu_\gamma(N)=1
\]
has probability one under the \(\gamma\)-law and zero under the \(\delta\)-law. This proves mutual singularity in every case not covered by equality of exponents or by the common summable regime. When the exponents agree, each Markov law is equivalent to the corresponding independent reference by Step 3, proving the converse.

**Step 5: Occupation laws.** For \(\gamma<1\), the first Borel--Cantelli lemma gives \(S_\infty<\infty\) almost surely; Step 2 transfers this to \(K_\infty\). For \(\gamma\ge1\), write \(X_n=B_n-b_n\). Independence and
\[
\sum_{n\ge2}\frac{\operatorname{Var}(X_n)}{\mu_\gamma(n)^2}
\le\sum_{n\ge2}\frac{\mu_\gamma(n)-\mu_\gamma(n-1)}{\mu_\gamma(n)^2}<\infty
\]
(the latter is bounded by a telescoping series with denominators \(\mu_\gamma(n-1)\mu_\gamma(n)\)) imply by Kolmogorov convergence and Kronecker's lemma that \(S_N/\mu_\gamma(N)\to1\) almost surely. Moreover \(\sum_{n\le N}b_n(1-b_n)\sim\mu_\gamma(N)\to\infty\), since \(b_n\to0\). The bounded independent centered increments satisfy Lindeberg's condition, hence \((S_N-\mu_\gamma(N))/\sqrt{\mu_\gamma(N)}\Rightarrow\mathcal N(0,1)\). Step 2 transfers both claims. Integral comparison gives the displayed growth of \(\mu_\gamma\).

**Step 6: Uniform logarithmic critical window.** Fix \(u\in\mathbb R\) and let \(\gamma_N=1+u/\log N\) (positive for all sufficiently large \(N\)), \(\alpha_N=1/\gamma_N\). By integral comparison, uniformly along this sequence,
\[
\mu_{\gamma_N}(N)
=\int_1^N t^{-\alpha_N}\,dt+O_u(1)
=\ell(u)\log N+O_u(1).
\]
The last equality follows from \((1-\alpha_N)\log N=u+O_u(1/\log N)\), with the value at \(u=0\) understood continuously. Also \(\sum_{n\le N}(n+1)^{-2\alpha_N}=O_u(1)\), so the independent triangular-array variance is \(\ell(u)\log N+O_u(1)\). Lindeberg--Feller gives the normal limit with variance \(\ell(u)\) after normalization by \(\sqrt{\log N}\). Finally the bound in Step 2 is uniform for \(\gamma_N\) in a compact neighborhood of one, so the expected number of coupling discrepancies up to \(N\) stays bounded independently of \(N\). Markov's inequality makes their normalized contribution \(o_{\Pr}(1)\). Slutsky's theorem proves part (iv), and the weak law follows from the same estimates.

## Verification

The accompanying standalone `checker.py` uses only the Python standard library. Run `python checker.py` from the directory containing the file. It verifies exact rational iteration for \(\gamma=1\), the finite-defect coupling inequality, the conditional likelihood \(\chi^2\) identity, and numerical finite-horizon mean/variance consistency in the crossover window. Its successful completion prints `PARABOLIC_MARKOV_PATH_CHECK_OK`.

These tests are finite sanity checks. The almost-sure claims, path-measure equivalence, mutual singularity, and central limit theorems are proved analytically in Steps 2--6 and are not inferred from the program.

## Relationship to prior work

Souissi--Mukhamedov (2024), Sections 3--4, introduces \(F\)-stochastic operators, their regularity, and the transition-matrix construction used here. Jamilov--Mukhamedov--Mukhamedova--Souissi (2024), Section 4, gives a sufficient summability condition for equivalent Markov measures, recalls a general Hellinger-type equivalence--singularity criterion, and explicitly raises the issue of whether nonsummability forces singularity. Those foundations and the classical Bernoulli product, Borel--Cantelli, martingale-likelihood, and triangular-array limit tools are prior work. The present claim is the explicit parabolic-operator model, the **complete path-law phase diagram**, the stronger eventual-coordinate coupling, and the sharp \(1/\log N\) rare-occupation crossover for its own Markov construction. This does not settle the general nonsummability question for arbitrary \(F\)-stochastic operators.

## Limitations

All row seeds are strictly positive and all initial probabilities have full support. Zero seeds lead to zero transition probabilities and may change equivalence classes; they are excluded. The statement concerns the specified nonhomogeneous Markov-chain construction rather than arbitrary stochastic models, and the critical window concerns a triangular family of laws, not a single path observed with a changing parameter. Comparisons with broader, possibly unpublished or unindexed literature may reveal equivalent formulations; there is no independent mathematical audit in this package.

## References

1. A. Souissi and F. Mukhamedov, “Nonlinear Stochastic Operators and Associated Inhomogeneous Entangled Quantum Markov Chains,” *Journal of Nonlinear Mathematical Physics* **31**, article 11 (first public 2024-02-26), DOI: 10.1007/s44198-024-00172-6. Full text: https://link.springer.com/article/10.1007/s44198-024-00172-6 .
2. U. Jamilov, F. Mukhamedov, F. Mukhamedova, and A. Souissi, “Dynamics of nonlinear stochastic operators and associated Markov measures,” *Mathematical Methods in the Applied Sciences* **47** (2024), 13300–13312 (first public 2024-05-16), DOI: 10.1002/mma.10191. Full text: https://onlinelibrary.wiley.com/doi/full/10.1002/mma.10191 .
3. S. Kakutani, “On equivalence of infinite product measures,” *Annals of Mathematics* **49** (1948), 214–224. Only its classical criterion as discussed in reference 2 is used as literature context; the present likelihood proof is self-contained.
