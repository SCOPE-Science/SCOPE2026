# Sharp run-length criterion for clustered disease-free opinion equilibria

## Finding

In the coupled opinion--vaccination--infection mean-field update of Roy et al. [1], a connected chain of four-person complete communities has a family of disease-free, completely polarized opinion equilibria. For every number \(m\geq1\) of communities, the local stability of a prescribed community opinion pattern is determined **exactly** by the longest consecutive run of anti-vaccine communities; the overall fraction vaccinated does not determine stability.

Specifically, write \(r_0=0\) and, for integers \(\ell\geq1\),
\[
 t_\ell=2\cos\!\left(\frac{\pi}{\ell+1}\right),\qquad
 r_\ell=\frac{2+t_\ell+\sqrt{(2-t_\ell)^2+12}}{2}.
\]
Let \(\sigma\in\{-1,+1\}^{m}\), and let \(L(\sigma)\) be the length of the longest contiguous run of \(-1\) symbols, with \(L=0\) for the all-positive word. At the equilibrium defined below, the infection-free state is locally exponentially attracting when
\[
 \lambda r_{L(\sigma)}<\alpha,
\]
and it is Lyapunov unstable whenever
\[
 \lambda r_{L(\sigma)}>\alpha.
\]
Equality is not classified. In particular, if \(\lambda r_\ell\neq\alpha\) for every \(1\leq\ell\leq m\), put \(q=\max\{0\leq\ell\leq m:\lambda r_\ell<\alpha\}\). Exactly the community-label words avoiding \(q+1\) consecutive negative labels produce locally exponentially attracting equilibria. Their number \(a_m\) is determined by
\[
 a_0=1,\quad a_n=2^n\ (1\leq n\leq q),\quad
 a_n=\sum_{j=1}^{q+1}a_{n-j}\ (n\geq q+1).
\]
In the last formula the recurrence is applied only through the required index \(m\); for \(q=0\) it gives \(a_m=1\).

For four communities, the two patterns \((-1,+1,-1,+1)\) and \((-1,-1,+1,+1)\) have identical average vaccinated fraction \(1/3\) when \(\phi=1/2\), yet the first is locally exponentially attracting and the second is unstable for \(\alpha=1/2\), \(\lambda=4/25\), and any fixed \(\epsilon>0\), \(\omega\geq0\). Exactly eight of the sixteen polarized community equilibria are attracting for these parameters.

## Assumptions and scope

The deterministic microscopic mean-field equations are the uncloaked equations (1)--(3), (6)--(8) of [1], with explicit clipping of opinions:
\[
\begin{aligned}
 O_i^{+}&=\Pi_{[-1,1]}\!\left(O_i+\frac{\epsilon}{d_i}\sum_j A_{ij}O_j+\frac{\omega}{d_i}\sum_j A_{ij}I_j\right),\\
 \gamma_i&=\frac{1+O_i}{2},\qquad q_i=1-\prod_j(1-\lambda A_{ij}I_j),\\
 I_i^{+}&=(1-\alpha)I_i+(1-I_i-V_i)(1-\gamma_i)q_i,\\
 V_i^{+}&=(1-\phi)V_i+(1-I_i-V_i)\gamma_i.
\end{aligned}
\]
Here \(A\) is a loopless undirected adjacency matrix, \(d_i=\sum_jA_{ij}>0\), and the physically admissible region is \(-1\leq O_i\leq1\), \(0\leq I_i,V_i\), \(I_i+V_i\leq1\). Parameters satisfy \(\epsilon>0\), \(0\leq\omega<\infty\), \(0<\alpha\leq1\), \(0<\phi<1\), and \(0\leq\lambda\leq1\). All stability assertions concern these discrete-time deterministic mean-field equations, not the original finite-population stochastic simulation.

For \(m\geq1\), take vertex-disjoint copies \(C_j\) of \(K_4\), \(1\leq j\leq m\). Designate one vertex \(p_j\) per copy and add only the edges \(p_jp_{j+1}\) for \(1\leq j<m\). Denote the resulting connected graph by \(G_m\). Given \(\sigma\), assign opinion \(O_i=\sigma_j\) to each vertex of \(C_j\), set \(I_i=0\), and set \(V_i=1/(1+\phi)\) on positive communities and \(V_i=0\) on negative communities. Call this candidate state \(E_\sigma\). No claim is made that these are all equilibria or all attracting equilibria of the unrestricted model.

## Proof

**1. Exactly pinned equilibria.** A nondesignated vertex has three neighbors within its clique, hence the sum of the neighbors' opinions has its own sign and magnitude three. A designated vertex has the same three internal neighbors and at most two external neighbors; even if both external opinions oppose its clique, the signed neighbor sum is at least \(3-2=1\). Thus
\[
\sigma_j\sum_k A_{ik}\sigma_{c(k)}\geq1
\]
for every vertex \(i\in C_j\), where \(c(k)\) is the community of \(k\). Since \(\epsilon>0\), each preclipped opinion update lies strictly outside \([-1,1]\) at its own endpoint. Every \(O_i\) is consequently fixed by clipping, and there exists a full relative neighborhood of \(E_\sigma\) whose image has **all opinions pinned** to those of \(E_\sigma\) after one update, even for finite \(\omega\geq0\).

At \(I_i=0\), the infection pressure is \(q_i=0\). The vaccination fixed-point equation becomes \(\phi V_i=(1-V_i)\gamma_i\). For \(\gamma_i=1\) this gives \(V_i=1/(1+\phi)\); for \(\gamma_i=0\) it gives \(V_i=0\). Therefore all \(E_\sigma\) are equilibria.

**2. Local epidemic criterion.** Let \(P\) be the set of vertices in positive communities and \(M\) the set in negative communities. In the pinned neighborhood, the linearized infection update, ordered by \((I_P,I_M)\), is
\[
 \begin{pmatrix} I_P^{+}\\ I_M^{+}\end{pmatrix}
 =\begin{pmatrix}(1-\alpha)\operatorname{Id}&0\\
 \lambda A_{MP}&(1-\alpha)\operatorname{Id}+\lambda A_{MM}
 \end{pmatrix}
 \begin{pmatrix} I_P\\ I_M\end{pmatrix}+O(\|(I,V)-(I^*,V^*)\|^2).
\]
The linearized vaccination variables contribute diagonal multipliers \(-\phi\) on \(P\) and \(1-\phi\) on \(M\), with possible subdiagonal couplings from infection, while the opinion derivative vanishes because of strict clipping. Thus the full linear spectrum consists of these vaccination multipliers, \(1-\alpha\) on \(P\), and the eigenvalues of \((1-\alpha)\operatorname{Id}+\lambda A_{MM}\).

Because \(A_{MM}\) is real symmetric, all of its eigenvalues lie in \([-\rho(A_{MM}),\rho(A_{MM})]\). If \(\lambda\rho(A_{MM})<\alpha\), each infection multiplier lies strictly between \(1-2\alpha\) and \(1\), and its modulus is strictly below one (also for \(\alpha=1\)). The entire Jacobian is a contraction in a suitable equivalent norm. The smooth map on the pinned neighborhood therefore has a locally exponentially attracting fixed point. Conversely, if \(\lambda\rho(A_{MM})>\alpha\), the Perron eigenvalue \(1-\alpha+\lambda\rho(A_{MM})\) exceeds one. A nonnegative Perron infection perturbation is physically admissible for sufficiently small amplitude, so the equilibrium is Lyapunov unstable. The borderline eigenvalue one is not addressed by this linear test.

**3. Exact block spectral radius.** Each maximal negative run of length \(\ell\) produces a separate connected component \(H_\ell\) of the induced graph on \(M\): \(\ell\) copies of \(K_4\) joined in a path through designated vertices. For \(\ell\geq1\), the strictly positive Perron vector has, by symmetry, one value \(u_j\) at the designated vertex and a common value \(v_j\) at the three nondesignated vertices of its \(j\)-th clique. Writing its Perron eigenvalue as \(r>2\), the satellite equations yield
\[
 (r-2)v_j=u_j.
\]
The designated-vertex equations become
\[
 \left(r-\frac3{r-2}\right)u_j=u_{j-1}+u_{j+1},\qquad u_0=u_{\ell+1}=0.
\]
The positive vector \((u_j)\) is therefore the Perron eigenvector of the \(\ell\)-vertex path, whose largest adjacency eigenvalue is \(t_\ell=2\cos(\pi/(\ell+1))\). Hence \(r-3/(r-2)=t_\ell\). Solving its larger-root quadratic gives the formula for \(r_\ell\) in the Finding. This is the Perron root because the constructed eigenvector is strictly positive. The numbers \(t_\ell\), and therefore \(r_\ell\), increase strictly with \(\ell\). The spectral radius of the disjoint union of the maximal negative runs is thus exactly \(r_{L(\sigma)}\), with the zero-dimensional case assigned \(r_0=0\).

**4. Enumeration.** Away from the stated equalities, step 2 and step 3 show that a pattern is attracting precisely when it has no run of \(q+1\) negative communities. Write \(a_n\) for the number of such binary words of length \(n\). For \(n\leq q\) every word qualifies, giving \(a_n=2^n\). For larger \(n\), partition admissible words by the length \(0,1,\ldots,q\) of the final negative run, preceded by a positive label unless this run is the whole word. The standard end-of-word decomposition gives \(a_n=\sum_{j=1}^{q+1}a_{n-j}\), using \(a_0=1\). If \(q=0\), only the all-positive word is admissible.

**5. Equal-coverage instability reversal.** For \(m=4\), the patterns \((-1,+1,-1,+1)\) and \((-1,-1,+1,+1)\) both contain two positive cliques and therefore both have overall equilibrium vaccinated fraction \(\tfrac12/(1+\phi)\), equal to \(1/3\) at \(\phi=1/2\). But their longest negative runs have lengths one and two. With \(\alpha=1/2\) and \(\lambda=4/25\),
\[
 \lambda r_1=\frac{12}{25}<\frac12<\frac{2(3+\sqrt{13})}{25}=\lambda r_2.
\]
The right-hand strict inequality follows from \(\sqrt{13}>13/4\). Hence the first equilibrium is exponentially attracting and the second unstable. At these parameters \(q=1\), and the binary-word recurrence gives \(a_4=8\).

## Verification

Run `python verify.py` with Python 3 standard library. It constructs the exact graph, verifies the rational pinned equilibrium and signed-neighborhood inequalities for every community-label word through five communities, computes independent numerical Perron radii of the induced negative graphs for every word through seven communities, compares with the analytic closed form, enumerates forbidden-run words versus their recurrence, and checks the four-community separation using exact rational arithmetic and a radical inequality. Expected final output begins `VERIFY_OK:`. These finite computations test the derivation, but the proof above, not enumeration, establishes the unrestricted theorem.

## Relationship to prior work

Roy et al. [1], equations (1)--(3) and (6)--(8), provide the model, its numerical behavior on heterogeneous graphs and a critical calculation around the entirely anti-vaccine state. Their published analysis does not yield the classification of partially vaccinated, polarized community corners, the run-length spectral law, or the equal-coverage reversal proved here. The general possibility of exponentially many stable opinion partitions is established independently in majority dynamics [2, Section 6.2] and is **not** claimed as a discovery here. Spectral-radius epidemic thresholds under heterogeneous vaccination are also known in much greater generality [3,4]. The contribution is their *model-specific combination*: a fully explicit family of opinion-pinned epidemic equilibria with exact counting and a sharp dependence on contiguous anti-vaccine clusters. The related but different two-layer alertness/opinion dynamics of [5] also admits multiple equilibria; its abstract does not establish the present formula or state-space identification.

## Limitations

The result classifies only the specified block-constant, disease-free equilibria on the chain of designated \(K_4\) communities; other equilibria, their basins, and nonlinear endemic dynamics are not classified. The eigenvalue equality \(\lambda r_{L}=\alpha\) is unproved. The result concerns the deterministic marginal-probability map and local behavior, not a stochastic infection-extinction guarantee or an empirical policy recommendation. A general matrix spectral theorem or majority-partition construction may recover individual ingredients; precise prior-work subsumption of the combined claim cannot be excluded without broader bibliographic verification.

## References

[1] A. Roy, U. Shekhar, S. Ghosh, T. Kapitaniak, and C. Hens, *Opinion-Driven Vaccination and Epidemic Dynamics on Heterogeneous Networks*, arXiv:2603.24403 (first public version 2026-03-25), later *Scientific Reports* 16 (2026), article 24951, DOI 10.1038/s41598-026-53331-8. https://arxiv.org/abs/2603.24403 ; https://www.nature.com/articles/s41598-026-53331-8

[2] I. Benjamini, G. Zakharov, and M. Zhukovskii, *Majority Dynamics on Finite Trees*, *Random Structures & Algorithms* 69 (2026), e70092, Section 6.2. https://doi.org/10.1002/rsa.70092

[3] J.-F. Delmas, D. Dronnier, and P.-A. Zitt, *Vaccinating According to the Maximal Endemic Equilibrium Achieves Herd Immunity*, *SIAM Journal on Applied Mathematics* (2025), DOI 10.1137/23M1558112. https://arxiv.org/abs/2211.15463

[4] J.-F. Delmas, D. Dronnier, and P.-A. Zitt, *The Effective Reproduction Number: Convexity, Concavity and Invariance*, *Journal of the European Mathematical Society*, DOI 10.4171/JEMS/1429. https://ems.press/journals/jems/articles/14297626

[5] S. Zhai, H. Li, F. Sun, and J. Kurths, *Coevolution of Epidemic Spreading and Opinion Dynamics in a Two-Layer Network with Media Influence*, *Physica A* 696 (2026), DOI 10.1016/j.physa.2026.131676. https://ideas.repec.org/a/eee/phsmap/v696y2026ics0378437126004127.html
