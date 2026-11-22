# Logarithmic repeated-edge fluctuations and finite repeated-hyperedge tails in growing uniform hypergraphs

## Finding
Fix an integer \(k\ge2\), and let \(0<p<1\), \(q=1-p\). Start with \(k\) labelled isolated vertices. At each integer time, independently add one new vertex with probability \(p\); otherwise sample a uniformly random unordered \(k\)-subset of the currently present vertices. Sampling is **with replacement across time**: a previously sampled hyperedge may be sampled again. Let \(D_n^{(k)}\) count the repeat attempts among the first \(n\) operations (the newly sampled hyperedge matches at least one earlier sample).

Then an exact rank dichotomy holds:

1. When \(k=2\), with \(c_p=2(1-p)^2/p^2\),
\[
 \frac{D_n^{(2)}}{\log n}\longrightarrow c_p \quad\text{almost surely},
 \qquad
 \frac{D_n^{(2)}-c_p\log n}{\sqrt{c_p\log n}}
 \Longrightarrow N(0,1).
\]
2. For every fixed \(k\ge3\), the total number of repetitions \(D_\infty^{(k)}=\lim_{n\to\infty}D_n^{(k)}\) is finite almost surely, and in fact has finite expectation.
3. For \(k=2\), let \(G_n^{\mathrm{multi}}\) retain every sampled edge as a separate parallel edge, and let \(G_n^{\mathrm{simple}}\) collapse parallel edges. Their first graph Betti numbers satisfy, **at every finite time**,
\[
 \beta_1(G_n^{\mathrm{multi}})-\beta_1(G_n^{\mathrm{simple}})=D_n^{(2)}.
\]
Consequently, the discrepancy between their cycle ranks grows logarithmically with the strong law and Gaussian fluctuations displayed above. The claims hold throughout the parameter range \(0<p<1\), without requiring a particular percolation phase.

## Assumptions and scope
Let \(\mathcal F_t\) denote the complete history after \(t\) operations. Write \(B_t\) for the number of vertex-creation operations, \(E_t=t-B_t\) for the number of hyperedge-selection operations, and \(D_t=D_t^{(k)}\). The number of available vertices after \(t\) operations is \(V_t=k+B_t\). The number of distinct selected hyperedges is exactly \(E_t-D_t\), even if the same hyperedge has been sampled more than twice. No self-loops are allowed: all sampled \(k\) vertices are distinct. Birth/sampling decisions and random hyperedge selections are independent at each operation, conditional on the current vertex set. The assertion is for each fixed \(p\) and fixed integer \(k\); no uniformity as \(p\to0\) or as \(k\) grows is claimed.

## Proof
**Step 1: exact conditional repeat intensity.** Put \(X_t=D_t-D_{t-1}\), for \(t\ge1\). Every earlier selected hyperedge is contained in the currently available vertex set, and the next selection is uniform over its \(\binom{V_{t-1}}k\) subsets. Hence, without independence assumptions on distinct-edge indicators,
\[
 a_t:=\mathbb E[X_t\mid\mathcal F_{t-1}]
 =q\frac{E_{t-1}-D_{t-1}}{\binom{k+B_{t-1}}k}.
\]
The compensator \(A_n=\sum_{t=1}^n a_t\) yields a martingale \(M_n=D_n-A_n\) with increments bounded in absolute value by one, and predictable quadratic variation
\[
 \langle M\rangle_n=\sum_{t=1}^n a_t(1-a_t).
\]

**Step 2: concentration of vertex births.** Since \(B_t\) is a binomial random walk with parameter \(p\), Hoeffding's inequality and Borel–Cantelli imply that, almost surely, for all sufficiently large \(t\),
\[
 B_t=pt+O(t^{2/3}),\qquad E_t=qt+O(t^{2/3}).
\]
For \(k\ge2\), these estimates imply \(a_t=O(t^{1-k})\) almost surely because \(E_t-D_t\le t\). In addition, a binomial lower-tail estimate on \(B_{t-1}\) gives the deterministic expectation bound \(\mathbb E[a_t]=O(t^{1-k})+O(e^{-\eta t})\) for some \(\eta>0\), with constants depending on \(p,k\). When \(k\ge3\), summing this bound proves \(\mathbb E D_\infty<\infty\), hence \(D_\infty<\infty\) almost surely.

**Step 3: almost-sure graph-case growth.** Take \(k=2\). From the previous step, \(a_t\le C/t\) eventually almost surely for a deterministic \(C\). Therefore \(A_n=O(\log n)\) almost surely. More precisely, the martingale series \(\sum_{t\ge2}(X_t-a_t)/\log(t+1)\) has almost surely finite total predictable quadratic variation, since \(\sum_{t\ge2}a_t/\log^2(t+1)<\infty\). Localization and the martingale convergence theorem give almost-sure convergence of that series; Kronecker's lemma then gives \(M_n/\log n\to0\) almost surely. Thus \(D_n=O(\log n)\) almost surely.

Now insert the estimates \(B_{t-1}=pt+O(t^{2/3})\), \(E_{t-1}=qt+O(t^{2/3})\) and \(D_{t-1}=O(\log t)\) into the **exact** formula from Step 1. Since \(\binom{2+B_{t-1}}2=(p^2/2)t^2(1+O(t^{-1/3}))\),
\[
 a_t=\frac{2q^2}{p^2t}+O(t^{-4/3})+O(\log t/t^2)
 \quad\text{almost surely}.
\]
Both error series are summable; therefore \(A_n-c_p\log n\) converges almost surely to a finite random limit. Together with \(M_n/\log n\to0\), this proves the strong law.

**Step 4: central limit theorem.** As \(a_t=O(1/t)\) almost surely, \(\sum_t a_t^2<\infty\). Consequently,
\[
 \langle M\rangle_n=A_n-\sum_{t\le n}a_t^2
 =c_p\log n+O(1)\quad\text{almost surely}.
\]
The bounded martingale increments satisfy the conditional Lindeberg condition at scale \(\sqrt{c_p\log n}\). The martingale central limit theorem gives \(M_n/\sqrt{c_p\log n}\Longrightarrow N(0,1)\). The almost-sure boundedness of \(A_n-c_p\log n\) and Slutsky's theorem yield the stated central limit theorem for \(D_n\).

**Step 5: cycle rank.** The two graph representations have identical vertices and identical connected components. The multigraph has \(E_n\) edges counted with multiplicity, whereas the simple graph has \(E_n-D_n\) distinct edges. The Euler/cycle-rank identity \(\beta_1=|E|-|V|+\#\mathrm{components}\) gives the exact difference \(D_n\), independently of the percolation regime.

## Verification
Run `python checker.py` using Python 3 and no external dependencies. The script performs 542 exact rational conditional-probability checks for ranks \(2\), \(3\), \(4\) and small finite histories, plus nine seeded finite-run simulations used as diagnostics. The conditional-probability checks test Step 1 by enumerating every available \(k\)-subset, including histories with repeated samples. These computations do **not** replace the almost-sure convergence or central-limit arguments in Steps 2–4. The mathematical proof invokes standard binomial concentration, localized martingale convergence, Kronecker's lemma, and the bounded-increment martingale central limit theorem; the proof above states their verification hypotheses explicitly.

## Relationship to prior work
Krapivsky, *Randomly growing uniform hypergraphs* (2026), introduces the vertex-birth versus uniform-hyperedge-selection process and analyzes percolation, cluster distributions, and topological invariants, chiefly at extensive scales. It does not state the logarithmic repeat-attempt law, the martingale fluctuation law, or the rank dichotomy above. Callaway et al., *Are randomly grown graphs really random?* (2001), study an earlier growing graph with random edge addition and infinite-order percolation, without this quantified count of sampled-edge repetitions. The deterministic cycle-rank identity is classical; the probabilistic growth and fluctuation assertions are the additional part. Related occupancy and martingale techniques are classical; priority beyond the inspected literature remains open.

## Limitations
The logarithmic and finite-repeat dichotomy applies to **repeated sampled hyperedges**, not to all cycle-generating edges or to the number of noncontractible simplicial subcomplexes. Only the graph case has the stated exact Betti-number interpretation; higher-dimensional homology cannot be inferred from repeated-face counts alone. The model samples a random \(k\)-subset even when it is already present; a process that forbids repeat attempts is a different model. Numerical experiments are finite diagnostics, and the normal limit is an asymptotic mathematical result, not a finite-sample exact normal distribution. The earlier literature is extensive, and unindexed or inaccessible prior derivations of this particular logarithmic CLT remain a priority risk.

## References
1. P. L. Krapivsky, *Randomly growing uniform hypergraphs*, arXiv:2611.14824v1 (first public 2026-11-10), https://arxiv.org/abs/2611.14824 .
2. D. S. Callaway, J. E. Hopcroft, J. M. Kleinberg, M. E. J. Newman, and S. H. Strogatz, *Are randomly grown graphs really random?*, arXiv:cond-mat/0104546, *Physical Review E* **64**, 041902 (2001), https://arxiv.org/abs/cond-mat/0104546 .
3. P. Hall and C. C. Heyde, *Martingale Limit Theory and Its Application*, Academic Press (1980), martingale convergence and central limit theorems.
