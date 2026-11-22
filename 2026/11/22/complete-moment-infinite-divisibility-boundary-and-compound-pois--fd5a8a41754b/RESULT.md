# Complete moment-infinite-divisibility boundary and compound-Poisson measures for geometrically regular shifts

## Finding
For a real number \(p>1\) and parameters \(-1<N,D<1\), let \(W_{p,N,D}\) be the positive unilateral weighted shift on \(\ell^2(\mathbb N_0)\) with weights
\[
\alpha_n=\sqrt{\frac{p^n+N}{p^n+D}},\qquad n\ge0.
\]
A shift is *moment infinitely divisible* (MID) if, for every real \(s>0\), the shift with weights \(\alpha_n^s\) is subnormal. Then, **with no exceptional base \(p\)**,
\[
\boxed{W_{p,N,D}\text{ is MID}\ \Longleftrightarrow\ N=D\ \text{or}\ -1<N<0,\ N<D\le -N.}
\]
In particular, the region \(N<0\), \(D>-N\) consists of non-MID shifts, including its subnormal portion; thus the MID exclusion in the third sector of the geometrically regular parameter diagram is exact.

On the nontrivial MID region, write \(q=p^{-1}\) and
\[
c_k=\frac{(-1)^{k-1}(D^k-N^k)}{k},\quad
b_k=\frac{c_k}{1-q^k},\quad
B=\sum_{k=1}^{\infty}b_k,\qquad k\ge1.
\]
These coefficients satisfy \(c_k\ge0\), \(b_k\ge0\), and \(B<\infty\). For each \(s>0\), take independent Poisson random variables \(P_{k,s}\) of respective means \(s b_k\), and set \(J_s=\sum_{k\ge1}kP_{k,s}\). Then \(J_s<\infty\) almost surely, and the **unique Berger probability measure** of the Schur-\(s\)-power shift is
\[
\boxed{\mu_s=\operatorname{Law}(q^{J_s}),\qquad
\mu_s(\{q^m\})=e^{-sB}[z^m]\exp\!\left(s\sum_{k=1}^{\infty}b_k z^k\right),\quad m\ge0.}
\]
In particular, the atom at \(1\) has mass \(e^{-sB}\). On the boundary \(D=-N>0\), precisely the even-indexed Poisson intensities vanish. In the trivial case \(D=N\), all Schur powers have Berger measure \(\delta_1\).

## Assumptions and scope
The Hilbert space is complex \(\ell^2(\mathbb N_0)\), and every shift weight is strictly positive. The base \(p\) is arbitrary real greater than one, not restricted to an integer. All parameter inequalities are strict except the stated boundary \(D=-N\). The Berger measure of a subnormal contractive unilateral shift means the unique probability measure \(\mu\) on \([0,1]\) whose moments are \(\gamma_n=\prod_{j=0}^{n-1}\alpha_j^2\), with \(\gamma_0=1\). The Schur-\(s\)-power shift has moments \(\gamma_n^s\), not \(\gamma_{sn}\). The notation \([z^m]\) means coefficient extraction from the indicated absolutely convergent power series.

## Proof
**1. Exclude the expanding half-square.** Set \(q=p^{-1}\). If \(N>D\), then \(\alpha_n^2=(1+Nq^n)/(1+Dq^n)>1\) and these weights strictly decrease to one, since the rational function \((1+Nt)/(1+Dt)\) is strictly increasing in \(t\), whereas \(q^n\) decreases. Every subnormal unilateral weighted shift is hyponormal and hence has nondecreasing positive weights. Consequently such a shift is not subnormal and cannot be MID. If \(N=D\), all weights are one, yielding the stated trivial case. Henceforth assume \(N<D\), so \(0<\alpha_n<1\).

**2. Obtain the logarithmic Hausdorff criterion from MID.** Define the forward difference \(\Delta f_n=f_{n+1}-f_n\) and
\[
h_n=-\log \alpha_n^2=\log(1+Dq^n)-\log(1+Nq^n)>0.
\]
If the shift is MID, every \(\gamma_n^s\) is a Hausdorff moment sequence because its subnormal representing measure is supported on \([0,1]\). Thus \((-1)^m\Delta^m\gamma_n^s\ge0\) for all integers \(m,n\ge0\). For fixed \(m\ge1\), let \(s\downarrow0\), using \(\gamma_j^s=1+s\log\gamma_j+O(s^2)\) at each of the finitely many needed indices. Since \(\Delta\log\gamma_n=-h_n\), we obtain
\[
(-1)^r\Delta^r h_n\ge0\qquad(n,r\ge0).
\]
Therefore \(h\) is completely monotone. By the Hausdorff moment theorem, there exists a **finite positive** Borel measure \(\nu_+\) on \([0,1]\) with \(h_n=\int t^n\,d\nu_+(t)\) for all \(n\ge0\).

**3. Identify its unique signed atomic representation.** As \(|N|,|D|<1\), the ordinary logarithmic power series converges absolutely and uniformly over all \(n\ge0\), giving
\[
h_n=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}(D^k-N^k)}{k}q^{kn}
=\int_{[0,1]}t^n\,d\nu(t),
\qquad \nu=\sum_{k=1}^{\infty}c_k\delta_{q^k}.
\]
The signed measure \(\nu\) is finite because, with \(\rho=\max(|N|,|D|)<1\), one has \(|c_k|\le2\rho^k/k\). Polynomials are dense in \(C([0,1])\), so two finite signed Borel measures with identical monomial moments coincide. Hence \(\nu=\nu_+\) and every distinct atomic mass \(c_k\) must be nonnegative.

**4. Obtain the exact parameter boundary.** The first two coefficients are \(c_1=D-N>0\) and \(c_2=(N^2-D^2)/2\). Their nonnegativity forces \(|D|\le|N|\). Together with \(D>N\), this is equivalent to \(N<0\) and \(N<D\le -N\). Conversely, in that region, for every odd \(k\), \(D^k-N^k>0\) by monotonicity of odd powers, while for every even \(k\), \(D^k-N^k\le0\) because \(|D|\le|N|\). Thus **all** \(c_k\ge0\). This proves the necessary region and the positivity needed for sufficiency.

**5. Construct every powered Berger measure.** Put \(b_k=c_k/(1-q^k)\). Since \(1-q^k\ge1-q>0\), the series \(B=\sum b_k\) converges. Using \(\gamma_n=\prod_{j=0}^{n-1}\alpha_j^2\) and a justified exchange of absolutely convergent series,
\[
\log\gamma_n=-\sum_{j=0}^{n-1}h_j
=-\sum_{k=1}^{\infty}b_k(1-q^{kn}).
\]
The Poisson collection has finite total mean \(sB\), so only finitely many \(P_{k,s}\) are nonzero almost surely and \(J_s\) is finite. Its probability generating function is
\[
\mathbb E[z^{J_s}]=\exp\!\left(s\sum_{k\ge1}b_k(z^k-1)\right),\qquad |z|\le1.
\]
Consequently \(\mathbb E[(q^{J_s})^n]=\exp[-s\sum b_k(1-q^{kn})]=\gamma_n^s\) for all \(n\ge0\). This is a probability measure on \([0,1]\) representing the moments of the Schur-\(s\)-power shift, so those shifts are subnormal by the Berger moment criterion. Hausdorff determinacy gives uniqueness. Coefficient extraction yields the claimed mass formula; \(P_{k,s}=0\) simultaneously for all \(k\) with probability \(e^{-sB}\), proving the atom at one. If \(D=-N>0\), then \(c_{2j}=0\) and \(c_{2j-1}=2D^{2j-1}/(2j-1)>0\). The proof is complete.

## Verification
The independent algebraic points to verify are the sign of \(c_2\), the absolutely convergent logarithm expansion, the Hausdorff uniqueness argument, and the compound-Poisson probability generating function. They are established directly above for the entire continuous parameter region. The accompanying standalone `check.py` checks rational examples in the allowed and forbidden sectors, coefficient signs, exact finite-difference obstructions for a forbidden example, and agreement of truncated Poisson moments with direct shift moments. These finite computations do **not** certify the universal quantifiers or replace the proof.

## Relationship to prior work
Benhida, Curto and Exner introduced this family, proved MID in Sectors I and II, and conjectured in their Conjecture 1.3(2) that Sector III beyond its Sector II boundary has no MID shifts. Their existing sufficient results already cover the *positive* half of the parameter classification, not its necessity. Their 2019/2020 sequence criteria supply a **general** MID/log-complete-alternation equivalence; the present argument instead identifies the unique discrete logarithmic Hausdorff measure, extracts an exact all-parameter necessity condition and constructs the representing measures of **every** fractional Schur power. The 2024 follow-up concentrates on safe quotients and partial zones, not the complete single-shift MID region; the 2025 signed-Berger-charge study addresses the ordinary moments and related classes, not the explicit Poisson measures of every Schur power. These distinctions concern the statements and their logical coverage, not merely titles or terminology.

## Limitations
Only moment infinite divisibility and the resulting powered Berger laws are classified; the theorem does **not** classify ordinary subnormality, complete hyperexpansivity, safe quotients, or all higher hyponormality strata. The base and parameter ranges are essential to the analytic series and the measure support. The proof is self-contained apart from standard weighted-shift/Berger and Hausdorff moment facts. Independent validation and historical priority beyond inspected sources are not established; an unindexed equivalent characterization remains possible.

## References
1. C. Benhida, R. E. Curto and G. R. Exner, *Geometrically regular weighted shifts*, arXiv:2309.05888 (first public 12 September 2023), especially Theorem 1.2, Conjecture 1.3 and Section 2.1. https://arxiv.org/abs/2309.05888
2. C. Benhida, R. E. Curto and G. R. Exner, *Moment infinitely divisible weighted shifts*, arXiv:1710.10683 (2017), on the general logarithmic-complete-alternation criterion. https://arxiv.org/abs/1710.10683
3. C. Benhida, R. E. Curto and G. R. Exner, *Moment Infinite Divisibility of Weighted Shifts: Sequence Conditions*, arXiv:2009.07797 (2020), especially Theorems 3.1 and 3.4. https://arxiv.org/abs/2009.07797
4. C. Benhida, R. E. Curto and G. R. Exner, *MID and subnormal safe quotients for geometrically regular weighted shifts*, J. Math. Anal. Appl. 538 (2024), 128443; arXiv:2312.06390. https://arxiv.org/abs/2312.06390
5. C. Benhida, R. E. Curto and G. R. Exner, *Signed Representing Measures (Berger-Type Charges) in Subnormality and Related Properties of Weighted Shifts*, Results in Mathematics 81 (2026), article 17, online 15 December 2025. https://doi.org/10.1007/s00025-025-02574-4
