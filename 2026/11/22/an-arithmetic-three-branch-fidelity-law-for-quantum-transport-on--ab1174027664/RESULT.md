# An arithmetic three-branch fidelity law for quantum transport on friendship graphs

## Finding
Let \(F_m\) be the simple friendship graph formed by \(m\ge2\) triangles sharing exactly one common hub, with no other overlaps. Choose the two non-hub vertices \(u,v\) of one triangle and let \(A_m\) denote the unweighted adjacency matrix. Evolve a single excitation with \(U_m(t)=\exp(-itA_m)\), in units where every edge hopping amplitude is one. Define its optimal partner-transfer probability as
\[
P_m^*=\sup_{t\in\mathbb R}|\langle v|U_m(t)|u\rangle|^2.
\]
For every fixed \(m\ge2\), this partner pair has neither perfect nor pretty good state transfer: \(P_m^*<1\). Nevertheless \(P_m^*\to1\) as \(m\to\infty\), and its sharp leading infidelity has **three arithmetic branches**. Write \(s_m=\sqrt{8m+1}\), and set
\[
 c_{\mathrm{irr}}=1-1/\sqrt2.
\]
For \(\alpha\in\{\pi/4,3\pi/4\}\), let \(u_\alpha\) be the unique real solution of
\[
 u_\alpha=-\sqrt2\sin(\alpha+u_\alpha/2)
\]
and define
\[
 c_\alpha=1+u_\alpha^2/8-\cos(\alpha+u_\alpha/2)/\sqrt2.
\]
Then the following three assertions hold, with limits taken within the indicated infinite subsequences:
\[
\begin{aligned}
\lim_{\substack{m\to\infty\\s_m\notin\mathbb Z}}m(1-P_m^*)&=c_{\mathrm{irr}}=0.292893218813\ldots,\\
\lim_{\substack{m\to\infty\\s_m\equiv1,7\pmod8}}m(1-P_m^*)&=c_{\pi/4}=0.419296833428\ldots,\\
\lim_{\substack{m\to\infty\\s_m\equiv3,5\pmod8}}m(1-P_m^*)&=c_{3\pi/4}=1.305301344447\ldots.
\end{aligned}
\]
Here a congruence on \(s_m\) requires that it be an integer. Equivalently, the integer-frequency cases have triangular \(m=k(k+1)/2\), with \(k\ge2\). Thus integral spectral resonances cause two different order-\(m^{-1}\) transport penalties, both strictly exceeding the generic penalty. The same graph family approaches unit-fidelity transfer as its size grows, even though no finite member permits arbitrarily accurate transfer.

## Assumptions and scope
The vertices are one hub \(h\), and disjoint peripheral pairs \((u_j,v_j)\), for \(1\le j\le m\). Edges join \(h\) to every peripheral vertex and join \(u_j\) to \(v_j\). There are no loops, onsite potentials, dissipation or time-dependent couplings. Time is any real number; by unitarity \(t\ge0\) has the same supremum. A supremum need not be attained when \(s_m\) is irrational. The result concerns transfer within a single triangle, not between different triangles, and is not a claim about many-particle or open-system dynamics.

## Proof
**1. Exact invariant-space reduction.** Introduce normalized pair states \(p_j=(|u_j\rangle+|v_j\rangle)/\sqrt2\) and antisymmetric states \(d_j=(|u_j\rangle-|v_j\rangle)/\sqrt2\). Each \(d_j\) has eigenvalue \(-1\). Every combination \(\sum_j a_jp_j\) with \(\sum_j a_j=0\) has eigenvalue \(+1\), and the remaining span of \(|h\rangle\) and \(p=m^{-1/2}\sum_jp_j\) has adjacency matrix
\[
 B_m=\begin{pmatrix}0&\sqrt{2m}\\\sqrt{2m}&1\end{pmatrix}.
\]
Its distinct eigenvalues are \(\lambda_\pm=(1\pm s_m)/2\), and the diagonal time-evolution amplitude at \(p\) is
\[
 f_m(t)=e^{-it/2}\left[\cos\left(\frac{s_mt}{2}\right)-\frac{i}{s_m}\sin\left(\frac{s_mt}{2}\right)\right].
\]
The hub-to-pair normalization and the projection of \(p_1\) onto the \(+1\) eigenspace yield the exact identity
\[
 a_m(t):=\langle v_1|U_m(t)|u_1\rangle
 =\frac{(m-1)e^{-it}+f_m(t)-m e^{it}}{2m}.
\tag{1}
\]

**2. No finite member has pretty good transfer.** For \(m\ge2\), the input vertex has nonzero spectral projections in all four eigenvalues \(-1,+1,\lambda_+,\lambda_-\). The two states \(u_1,v_1\) have identical projections in the \(+1,\lambda_+,\lambda_-\) sectors and opposite projections in the \(-1\) sector. If unit fidelity could be approached, the unitary eigenphases on these sectors would have to approach one common phase \(\gamma\) in the three symmetric sectors and \(-\gamma\) in the antisymmetric sector. Thus
\[
 e^{-it}\sim\gamma,\qquad e^{it}\sim-\gamma,\qquad
 e^{-it\lambda_+}\sim\gamma,\quad e^{-it\lambda_-}\sim\gamma.
\]
Since \(\lambda_++\lambda_-=1\), multiplying the last two relations gives \(e^{-it}\sim\gamma^2\). Combined with \(e^{-it}\sim\gamma\), this forces \(\gamma\sim1\), whereas the first two relations then force \(1\sim-1\). This contradiction applies also to any sequence of times, proving \(P_m^*<1\).

**3. Uniform localization of the optimizing time.** Put
\[
 W_m(t)=(m-1)e^{-it/2}-me^{3it/2},\qquad
 q_m(t)=\cos(s_mt/2)-\frac{i}{s_m}\sin(s_mt/2).
\]
Then \(2m a_m(t)=W_m(t)+q_m(t)\), with \(|q_m(t)|\le1\), and
\[
 |W_m(t)|^2=(2m-1)^2-4m(m-1)\cos^2t.
\tag{2}
\]
At \(t=\pi/2\), the reverse triangle inequality implies \(|a_m(t)|\ge1-1/m\). Therefore any sequence of times that is asymptotically optimal at order \(1/m\) must have \(\cos^2t=O(1/m)\), by (2) and the upper triangle inequality. Such times lie within \(O(m^{-1/2})\) of an odd multiple of \(\pi/2\). Near the center \(\pi/2\), the direction of \(W_m\) converges to \(e^{-i\pi/4}\), and near \(3\pi/2\) it converges to \(e^{-3i\pi/4}\). The elementary expansion \(|W+q|=|W|+\operatorname{Re}(\overline Wq/|W|)+O(1/|W|)\), uniform for \(|q|\le1\), will be used below.

**4. Nonsquare-frequency branch.** Suppose \(s_m\) is irrational. Since \(1\) and \(s_m\) are rationally independent, the orbit of \((t\bmod4\pi,s_mt/2\bmod2\pi)\) is dense in the two-torus. Hence the supremum of \(|a_m|\) is at least the value of its continuous two-phase extension at \(t=\pi/2\) and \(s_mt/2=0\), for which
\[
 P_m^*\ge1-\frac{1-1/\sqrt2}{m}+\frac{2-\sqrt2}{4m^2}.
\tag{3}
\]
Conversely, the optimization-time localization in Step 3 makes the real part of \(q_m\) dominate, because \(s_m\to\infty\), and its projection onto either limiting direction of \(W_m\) is at most \(1/\sqrt2+o(1)\). From (2), \(|W_m|\le2m-1\); thus \(|2m a_m|\le2m-1+1/\sqrt2+o(1)\), uniformly on any near-optimal sequence. This gives \(\liminf m(1-P_m^*)\ge1-1/\sqrt2\). Inequality (3) gives the reverse bound, proving the first limit.

**5. Integer-frequency branches.** If \(s_m=s\) is an integer, it is odd and \(m=(s^2-1)/8\) is triangular. All four eigenvalues are integers, so (1) is \(2\pi\)-periodic. By Step 3, an optimal time in \([0,2\pi]\) lies near \(t_1=\pi/2\) or \(t_2=3\pi/2\); write \(t=t_j+u/s\). Any sequence with bounded leading infidelity must have bounded \(u\). Uniformly for \(u\) in any fixed bounded interval,
\[
\begin{aligned}
|W_m(t)|&=2m-1-u^2/8+o(1),\\
\operatorname{Re}\frac{\overline{W_m(t)}q_m(t)}{|W_m(t)|}
&=\begin{cases}
\cos(s\pi/4+u/2)/\sqrt2+o(1),&j=1,\\
-\cos(3s\pi/4+u/2)/\sqrt2+o(1),&j=2.
\end{cases}
\end{aligned}
\tag{4}
\]
Consequently the leading infidelity is the minimum over the two centers and \(u\in\mathbb R\) of \(1+u^2/8\) minus the corresponding cosine term. For \(s\equiv1,7\pmod8\), the two center expressions reduce by reflecting \(u\) to the single objective \(1+u^2/8-\cos(\pi/4+u/2)/\sqrt2\). For \(s\equiv3,5\pmod8\), they similarly reduce to the objective with \(3\pi/4\). The function
\[
 g_\alpha(u)=\frac{\cos(\alpha+u/2)}{\sqrt2}-\frac{u^2}{8}
\]
is strictly concave on \(\mathbb R\), since
\[
 g_\alpha''(u)=-\frac14-\frac{\cos(\alpha+u/2)}{4\sqrt2}
\le-\frac{1-1/\sqrt2}{4}<0.
\]
It has exactly one maximizer, characterized by \(u=-\sqrt2\sin(\alpha+u/2)\), necessarily in \([-\sqrt2,\sqrt2]\). Equation (4), compactness of bounded near-optimal \(u\), and these unique maxima prove both remaining limits. This completes the proof.

## Verification
The standalone file `check_transport.py` constructs adjacency matrices independently and compares their exponential entries to (1) for 143 parameter-time pairs. It also checks both implicit variational constants, selected periodic triangular-family optimum values, and the analytic two-torus witness (3), for 168 assertions in total. Run `python check_transport.py` with NumPy and SciPy. These computations corroborate specific cases; the infinite-size statements and the exclusion of pretty good transfer are proved by the preceding arguments, not by numerical extrapolation.

## Relationship to prior work
Godsil's *State Transfer on Graphs* (first publicly posted 2011-02-24) develops the eigenprojection phase criteria and periodicity theory underlying the argument. Cameron and coauthors' *Universal State Transfer on Graphs* (first posted 2013-10-15) gives continuous-time transfer terminology and Kronecker-type mechanisms, rather than the present within-triangle optimal-fidelity asymptotics. Kimmerling's 2023 open dissertation concerns continuous-time quantum walks on windmills and primarily reports long-time average-mixing ranks; only its abstract and repository metadata were accessible here, not its 100-page full text. Its potential overlap with the exact graph requires independent checking. A published research-record result on heterogeneous clique-cored windmills establishes time-averaged mixing rank and spectral lower bounds; those claims do not imply a supremum over observation times or the arithmetic three-branch leading constants. No assertion of worldwide novelty follows merely from the unsuccessful searches.

## Limitations
The result applies only to the unweighted, single-particle adjacency Hamiltonian on friendship graphs and the two non-hub vertices in one triangle. It gives leading asymptotics of the **optimal over all times** fidelity, not a bound on the waiting time needed to approach the irrational-frequency supremum. In the nonsquare case, very long times may be necessary. No claim is made about decoherence, disorder, multi-excitation dynamics, or transport between different triangles. Existing work on windmill quantum walks was not fully accessible, so historical priority should be assessed independently before external dissemination.

## References
- C. Godsil, *State Transfer on Graphs*, arXiv:1102.4898, first public version 2011-02-24. https://arxiv.org/abs/1102.4898
- S. Cameron, S. Fehrenbach, L. Granger, O. Hennigh, S. Shrestha, C. Tamon, *Universal State Transfer on Graphs*, arXiv:1310.3885, first public version 2013-10-15. https://arxiv.org/abs/1310.3885
- P. R. Kimmerling, *Continuous-Time Quantum Walks on Windmill Graphs*, Washington State University dissertation (2023), DOI:10.7273/000006322. https://rex.libraries.wsu.edu/esploro/outputs/doctoral/Continuous-Time-Quantum-Walks-on-Windmill-Graphs/99901086723401842
- *Exact rank and uniform positive spectral gap for heterogeneous clique-cored windmills*, publicly indexed research record, 2026-10-12. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-rank-and-uniform-positive-spectral-gap-for-heterogeneous-c--1fc0e371735c
