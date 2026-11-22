# A sharp drift threshold for initial vacancy-hazard acceleration in finite exclusion rings

## Finding

Fix a homogeneous asymmetric simple exclusion process on the cycle of \(L\ge4\) sites with \(N\) particles, \(1\le N\le L-1\), positive clockwise hopping rate \(p\) and counterclockwise rate \(q\). Sample the stationary path at **events** where the observed site \(0\) changes from occupied to empty. If \(S(t)\) is the probability that the newly empty site remains unoccupied through the following \(t\) time units, define its elapsed-spell hazard by \(h(t)=-\frac{d}{dt}\log S(t)\).

Set
\[
\alpha=\frac{N-1}{L-2},\qquad
\beta=\frac{(N-1)(N-2)}{(L-2)(L-3)}.
\]
The exact initial hazard and initial hazard slope are
\[
\boxed{h(0)=\frac{2pq+(p^2+q^2)\alpha}{p+q},\qquad
h'(0)=h(0)^2-2pq(1+\alpha)-(p-q)^2\beta.}
\]
Equivalently,
\[
\boxed{h'(0)=\frac{L-N-1}{(L-3)(L-2)^2(p+q)^2}
\left[(N-1)(p^4+q^4)-2(L-2)(L-3)pq(p^2+q^2)
-2(2L-5)(N-1)p^2q^2\right].}
\]
For \(2\le N\le L-2\) there is **one and only one** bias-magnitude threshold. Define
\[
 z_* = \frac{(L-2)(L-3)+\sqrt{(L-2)^2(L-3)^2+4(L-2)(N-1)^2}}{N-1},
\quad r_* =\frac{z_*+\sqrt{z_*^2-4}}2.
\]
Then \(r_*>1\), and, with \(r=p/q\),
\[
\boxed{h'(0)>0\ \Longleftrightarrow\ r>r_*\ \text{or}\ r<1/r_*;\qquad
h'(0)=0\ \Longleftrightarrow\ r\in\{r_*,1/r_*\}.}
\]
The slope is strictly negative for all remaining positive ratios in the interior sector. For \(N=1\) the slope is strictly negative for every positive pair of rates; for \(N=L-1\) it is exactly zero, because only one empty configuration is possible. At fixed density \(N/L\to\rho\in(0,1)\), the threshold diverges linearly,
\[
\boxed{r_*/L\longrightarrow 2/\rho.}
\]
Thus a site-occupancy record can reveal broken detailed balance without tracking particle currents: an **initially increasing** stationary vacancy-spell hazard is impossible for any finite reversible stationary continuous-time chain, but appears here beyond a sharp driving threshold.

## Assumptions and scope

The model is a finite irreducible continuous-time exclusion chain with fixed particle number and independent exponential jump clocks. A jump from \(j\) to \(j+1\pmod L\) has rate \(p\) when its destination is empty; the reverse has rate \(q\) when allowed. Rates are positive, with no births, deaths, partial observations in addition to the indicated probe, or external reservoirs. The stationary distribution on all \(\binom LN\) configurations is uniform. The initial law is the **stationary departure-Palm law** for a newly created vacancy at site \(0\), not the uniform distribution conditional on vacancy at an arbitrary instant. The claim refers to \(h'(0)\) and does **not** imply monotonicity of \(h(t)\) for all \(t\).

## Proof

**1. Stationarity and Palm entrance.** Each configuration has the same number of clockwise \(10\) bonds and counterclockwise \(01\) bonds on the cycle. Thus incoming and outgoing total rates agree under the uniform fixed-\(N\) law; positive jump rates make it the unique invariant distribution. Condition on probe site \(0\) being empty and let \(\mathbb E_B\) denote the uniform law on those \(\binom{L-1}{N}\) configurations. Write \(X=n_1\), \(Y=n_{L-1}\), \(U=n_2\), \(V=n_{L-2}\). The rate at which an occupied-probe configuration enters an empty-probe configuration \(x\), summed over all its occupied precursors, is proportional to
\[
a(x)=pX+qY.\]
The rate at which this empty-probe configuration exits to an occupied-probe configuration is
\[
c(x)=qX+pY.\]
Consequently the entrance-Palm measure \(\nu\) on empty-probe configurations satisfies \(\nu(x)=a(x)\mathbb P_B(x)/\mathbb E_B[a]\).

**2. Killed generator and hazard derivatives.** Let \(G\) be the complete row generator, \(B\) the empty-probe configurations, and \(G_B\) the subgenerator obtained by restricting \(G\) to \(B\), retaining the original negative diagonal. Then \(G_B\mathbf 1=-c\) and
\[
 S(t)=\nu e^{tG_B}\mathbf1,\qquad
 h(0)=\nu c,\qquad
 h'(0)=\nu G_Bc+(\nu c)^2.
\]
Write \(G_B=G_{\mathrm{int}}-\operatorname{diag}(c)\), where \(G_{\mathrm{int}}\) has only transitions that keep the probe empty and is a conservative generator on \(B\). Direct examination of the two neighboring bonds gives, for \(L\ge4\),
\[
 G_{\mathrm{int}}X=qU-pX+(p-q)XU,\qquad
 G_{\mathrm{int}}Y=pV-qY+(q-p)VY.
\]
This also applies to \(L=4\), for which \(U=V\); no term requires them to be distinct.

**3. Hypergeometric contraction.** For any \(m\) distinct nonprobe sites,
\[
\mathbb E_B[n_{i_1}\cdots n_{i_m}]=\frac{(N)_m}{(L-1)_m}=:\mu_m.
\]
Set \(\mu_1=\mu\). Expanding the previous displayed identities and using only products of up to three **distinct** nonprobe occupations yields
\[
 \mathbb E_B[a]=(p+q)\mu,
\]
\[
\mathbb E_B[ac]=2pq\mu+(p^2+q^2)\mu_2,
\]
\[
\mathbb E_B[aG_{\mathrm{int}}c]=-pq(p+q)\mu
 +(p^3+q^3)\mu_2-(p-q)^2(p+q)\mu_3,
\]
\[
\mathbb E_B[ac^2]=(p+q)\{pq\mu+(p^2+pq+q^2)\mu_2\}.
\]
Subtract the last equation from the preceding one, divide by \(\mathbb E_B[a]\), and note \(\mu_2/\mu=\alpha\) and \(\mu_3/\mu=\beta\). This proves both hazard formulas; polynomial factorization gives the second version. No finite-state sampling is used to establish the general identity.

**4. Sign and unique threshold.** If \(2\le N\le L-2\), the exterior factor in the second formula is positive. Let \(z=p/q+q/p\ge2\). Divide its quartic bracket by \(p^2q^2\). The sign equals the sign of
\[
 F(z)=(N-1)[z^2-4(L-2)]-2(L-2)(L-3)z.
\]
This upward quadratic has exactly one positive root \(z_*\). Moreover \(F(2)<0\) for \(L\ge4\). The increasing branch \(r\mapsto r+r^{-1}\) on \([1,\infty)\) gives the unique \(r_*>1\), with reciprocal counterpart. If \(N=1\), the quartic bracket reduces to \(-2(L-2)(L-3)pq(p^2+q^2)<0\). If \(N=L-1\), the prefactor vanishes and the empty-probe sector has one state. As \(N/L\to\rho\in(0,1)\), expansion of the explicit quadratic root gives \(z_*\sim2L/\rho\), hence \(r_*/L\to2/\rho\).

**5. Relation to reversibility.** For any finite reversible irreducible stationary Markov chain, the killed generator of a subset is self-adjoint in the stationary weighted inner product. The entrance-Palm distribution into that subset is proportional to \(-G_B\mathbf 1\) under this inner product. A spectral decomposition then writes the spell survival as a positive mixture \(S(t)=\sum_jw_je^{-\lambda_jt}\), with \(w_j\ge0\), \(\sum_jw_j=1\), and \(\lambda_j>0\). Therefore \(h'(t)=-\operatorname{Var}_{w(t)}(\lambda_j)\le0\) for all \(t\). The positive initial slopes in the theorem consequently give a rigorously one-sided, coarse-observation witness of nonreversibility.

## Verification

The included `check_hazard.py` uses only the Python standard library. It independently enumerates complete transition generators, obtains the entrance distribution by **summing actual occupied-to-vacant transition rates** (not the asserted Palm formula), constructs the killed subgenerator, computes the first two survival derivatives using exact `Fraction` arithmetic, and verifies the derived expressions and the sign polynomial. Running `python3 check_hazard.py` checks every nonempty, nonfull particle sector on rings of lengths \(4\) through \(8\) for six distinct rational rate pairs (150 exact checks). The finite checks test independent representations but do not replace the proof for all \(L,N,p,q\).

## Relationship to prior work

Iadecola [1] studies information-theoretic local Markov memory of **symmetric discrete-time** exclusion and global charge inference. That motivates using a site record as an observable, but neither its symmetric generator nor its conditional mutual information formula implies the biased **continuous-time departure-Palm first-exit hazard** or its exact threshold. Iyer et al. [2] study **tagged-particle trapping times in percolation side branches**, including restricted-generator survival calculations under directional driving; their state space and first-passage event differ from the vacancy of a fixed site on a homogeneous cyclic ring. Chatterjee, Ramola, and Dhar [3] study disordered branch waiting times with symmetric exclusion; there is no driven regular-cycle site-spell threshold there. Tracy and Widom [4] provide exact stationary-ASEP one-time correlations and current laws on the infinite line, but these do not directly state the present **whole-spell Palm survival derivative on a finite fixed-charge ring**. The general reversible spectral-mixture argument above is standard and not claimed as new. The claim of contribution is the explicit finite-ring asymmetric threshold, including particle-number boundaries and its density-scale law.

## Limitations

The derivative is a local-in-spell-age quantity; global hazard monotonicity, complete survival laws, higher-dimensional lattices, open boundaries, site disorder, and partially observed charging protocols are not classified. The positive slope is sufficient but not necessary for broken detailed balance, and a negative slope does not establish reversibility. The theorem does not assert experimental detectability at finite sample sizes. Published work could contain equivalent waiting-time calculations under other terminology; that remains an originality risk requiring independent specialist literature review. The derived classifications assume strictly positive clockwise and counterclockwise rates; totally one-way dynamics is addressed only by limits, not by an equality case.

## References

1. T. Iadecola, *Local Markov Order and Global Inference in Many-Body Dynamics*, arXiv:2607.06689 (first public 2026-07-07), https://arxiv.org/abs/2607.06689.
2. C. Iyer, M. Barma, H. Singh, D. Dhar, *Asymmetric Simple Exclusion Process on the Percolation Cluster: Waiting Time Distribution in Side Branches*, arXiv:2312.15508 (first public 2023-12-24), https://arxiv.org/abs/2312.15508.
3. A. Chatterjee, K. Ramola, D. Dhar, *Continuously varying exponents in the distribution of waiting times in the symmetric exclusion process on a percolation cluster*, arXiv:2609.32314 (2026-09-26), https://arxiv.org/abs/2609.32314.
4. C. A. Tracy, H. Widom, *Formulas for ASEP with Two-Sided Bernoulli Initial Condition*, J. Stat. Phys. **140** (2010), 619–634, DOI 10.1007/s10955-010-0013-x. Literature comparison to [4] is limited to its accessible abstract.
