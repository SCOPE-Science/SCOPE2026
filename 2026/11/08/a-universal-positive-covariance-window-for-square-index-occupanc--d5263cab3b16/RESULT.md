# A universal positive covariance window for square-index occupancy counts

## Finding

Throw \(N\) distinguishable balls independently and uniformly into \(m\) labeled boxes. Write \(X_{m,r}\) for the number of boxes containing exactly \(r\) balls. Fix an integer \(j\ge 1\) and put
\[
r=j^2,\qquad s=(j+1)^2,\qquad a=j(j+1).
\]
For every real \(z\) and every integer sequence \(N=N_m\) satisfying
\[
\frac{N_m}{m}=a+\frac{z}{\sqrt m}+o(m^{-1/2}),
\]
we have the *unscaled* covariance limit
\[
\boxed{\displaystyle
\lim_{m\to\infty}\operatorname{Cov}(X_{m,r},X_{m,s})
=\frac{e^{-2a}a^{r+s}}{r!s!}\left(1-\frac{z^2}{a}\right).}
\tag{1}
\]
Consequently, at every fixed \(j\), the covariance is eventually strictly positive whenever \(|z|<\sqrt a\), and eventually strictly negative whenever \(|z|>\sqrt a\). No assertion is made about the sign on the boundary \(|z|=\sqrt a\).

In particular, at the *exactly integral* central load \(N=am\), the covariance tends to a strictly positive constant, even though the standard order-\(m\) covariance coefficient vanishes. For \(j=1\), the two occupancy frequencies are one-balls and four-balls, and
\[
\lim_{m\to\infty}\operatorname{Cov}(X_{m,1},X_{m,4})\big|_{N=2m}=\frac43e^{-4}.
\tag{2}
\]
The positive window is asymptotically \(N=am+z\sqrt m\) with \(|z|<\sqrt a\). Outside the window, when \(N/m\to\alpha\ne a\) for a fixed \(\alpha>0\), the covariance is eventually negative and of order \(m\). The window is nontrivial because the natural standard deviations of the individual occupancy counts are of order \(\sqrt m\), whereas their covariance here is only of order one.

## Assumptions and scope

All boxes have equal selection probability \(1/m\). The index \(j\ge1\) is fixed, not growing with \(m\), and the number \(N_m\) of balls is deterministic and integral. The asymptotic parameter is \(m\to\infty\). The claim is about covariance, not stochastic independence or conditional association; a zero limiting covariance does not imply independence. Counts of empty boxes, nonuniform allocation, or growing frequency indices are not included in (1).

For context, for any two fixed *distinct* positive integers \(r<s\), the ordinary order-\(m\) mixed-covariance coefficient is determined by
\[
F_{r,s}(\alpha)=\alpha+1-r-s+\frac{rs}{\alpha}.
\]
Its global minimum over \(\alpha>0\) is \(1-(\sqrt s-\sqrt r)^2\). The *double-zero*, or tangency, case is precisely \((r,s)=(j^2,(j+1)^2)\) for integers \(j\ge1\). This observation identifies the natural family to which the higher-order limit (1) applies; the generic first-order covariance formula is classical background, not asserted as a separate novel result.

## Proof

**Exact occupancy moments.** For fixed \(m\ge3\), \(N\ge r+s\), and \(r\ne s\), let
\[
P_t=\binom Nt m^{-t}(1-m^{-1})^{N-t},
\qquad
Q_{r,s}=\frac{(N)_{r+s}}{r!s!m^{r+s}}(1-2m^{-1})^{N-r-s},
\]
where \((N)_k=N(N-1)\cdots(N-k+1)\). For a specified box, \(P_t\) is the probability of exactly \(t\) balls. For two distinct specified boxes, \(Q_{r,s}\) is the probability of their occupancies being \(r,s\). Summing their indicators gives the exact identity
\[
\operatorname{Cov}(X_{m,r},X_{m,s})
=m(m-1)Q_{r,s}-m^2P_rP_s
=m^2P_rP_s(R-1),
\tag{3}
\]
where
\[
R=(1-m^{-1})\frac{(N)_{r+s}}{(N)_r(N)_s}
\frac{(1-2m^{-1})^{N-r-s}}{(1-m^{-1})^{2N-r-s}}.
\tag{4}
\]
The same moment identity, with the joint probability set to zero if \(N<r+s\), is valid for all admissible finite \(m,N\).

**Uniform expansion.** Write \(\alpha=N/m\) and restrict \(\alpha\) to any fixed compact subinterval of \((0,\infty)\). Since \(r,s\) are fixed, expanding the logarithm of (4) as a finite product and the two elementary log-power terms yields uniformly
\[
\log R=-\frac{F_{r,s}(\alpha)}m
+\frac{G_{r,s}(\alpha)}{m^2}+O(m^{-3}),
\tag{5}
\]
with
\[
\begin{aligned}
F_{r,s}(\alpha)&=\alpha+1-r-s+\frac{rs}{\alpha},\\
G_{r,s}(\alpha)&=-2\alpha+\frac{3(r+s)-1}{2}
-\frac{rs(r+s-1)}{2\alpha^2}.
\end{aligned}
\tag{6}
\]
For reproducibility, the finite-product portion of \(\log R\) is
\[
\sum_{h=0}^{s-1}\log\frac{N-r-h}{N-h}
=-\frac{rs}{\alpha m}-\frac{rs(r+s-1)}{2\alpha^2m^2}+O(m^{-3}),
\]
and the remaining portion is
\[
(N-r-s)\log(1-2/m)-(2N-r-s-1)\log(1-1/m)
=\frac{r+s-1-\alpha}{m}
+\frac{-2\alpha+[3(r+s)-1]/2}{m^2}+O(m^{-3}).
\]
These expansions follow term by term from \(\log(1-u)=-u-u^2/2-u^3/3+O(u^4)\); uniformity holds because \(r,s\) are fixed and \(\alpha\) stays bounded away from zero.

**Critical cancellation.** For \(r=j^2\), \(s=(j+1)^2\), and \(a=j(j+1)\), we have \(r+s=2a+1\) and \(rs=a^2\). Thus (6) becomes
\[
F_{r,s}(\alpha)=\frac{(\alpha-a)^2}{\alpha},
\qquad G_{r,s}(a)=1.
\tag{7}
\]
Under the stated scaling, \(F_{r,s}(\alpha)={z^2}/{(am)}+o(m^{-1})\). Equations (5)–(7) imply
\[
\log R=\frac{1-z^2/a}{m^2}+o(m^{-2}),
\qquad
m^2(R-1)\longrightarrow 1-\frac{z^2}{a}.
\]
At the same time,
\[
P_rP_s\longrightarrow \frac{e^{-2a}a^{r+s}}{r!s!}>0.
\]
Substituting into the exact identity (3) proves (1) and the strict eventual signs away from the two boundary values. For any fixed \(\alpha\ne a\), (5) instead gives \(m^{-1}\operatorname{Cov}(X_{m,r},X_{m,s})\to-e^{-2\alpha}\alpha^{r+s}F_{r,s}(\alpha)/(r!s!)<0\), proving the outer statement.

**Completeness of the tangency family.** Differentiation gives \(F'_{r,s}(\alpha)=1-rs/\alpha^2\); its unique minimum is at \(\alpha=\sqrt{rs}\), with value \(1-(\sqrt s-\sqrt r)^2\). A double zero therefore requires \(\sqrt s-\sqrt r=1\). Since \(r,s\) are positive integers, this forces \(\sqrt r=(s-r-1)/2\) to be rational, hence an integer \(j\); then \(s=(j+1)^2\). Conversely, these square-index pairs satisfy the condition. This proves the family is exhaustive.

## Verification

The standalone `verify.py` implements (3) independently of the logarithmic expansion. It exhaustively enumerates all allocations for \(2\le m\le4\), \(0\le N\le8\), and every pair of distinct occupancy counts with indices in \(\{0,\dots,N\}\), checking exact rational covariance against the moment formula. It also verifies the critical polynomial identities for \(1\le j\le100\) exactly and checks numerical convergence for selected \(j\) and scaling parameters using 95-digit decimal arithmetic.

Executed command: `python3 verify.py`. Output: `PASS: 720 exhaustive exact covariance assertions; 300 exact critical-polynomial assertions; 14 asymptotic diagnostic assertions; total 1034.` Finite enumeration and numerical diagnostics corroborate the argument but do not replace the uniform Taylor proof of the all-\(m\) limit.

## Relationship to prior work

The underlying occupancy mixed moments are classical. Békéssy's 1963 treatment develops a multivariate occupancy generating function and gives univariate moments; later Kolchin–Sevast'yanov–Chistyakov-type results yield the leading fixed-density covariance. Barbour–Gnedin (2008) analyzes the joint behavior of occupancy-frequency counts in an *infinite-box* framework, with a Poissonized mixed-covariance formula and the classification of possible limiting correlation structures. Sagitov (2026) restates the general first-order fixed-density covariance and supplies explicit bounds for higher-order remainder terms, but the inspected theorem does not identify an exact second-order limit at a zero of the leading term.

The new assertion here is narrowly the *universal order-one covariance limit across every square-index tangency, including its explicit square-root critical window*. It is not a claim to have discovered the classical exact moments or the first-order covariance matrix. A published general expansion with an explicit *coefficient* for the relevant order could implicitly subsume this specialization; available comparisons found no such identified statement, but no exhaustive literature-priority certification is claimed.

## Limitations

The \(o(1)\) in (1) is proved only for fixed \(j,z\), not uniformly as these parameters grow. The sign at \(|z|=\sqrt a\) is deliberately left undetermined. No independent scientific audit, general central limit theorem, or stochastic independence conclusion is claimed. Earlier general generating-function treatments can encode these finite moments without explicitly stating this critical-window consequence.

## References

1. A. Békéssy, “On Classical Occupancy Problems I,” *Publ. Math. Inst. Hung. Acad. Sci.* 8 (1963), 59–71. Open-access scan: https://real.mtak.hu/201424/1/cut_MATKUTINT_8_1_-_2_1963_pp59_-_71.pdf .
2. B. A. Sevast'yanov and V. P. Chistyakov, “Asymptotic Normality in the Classical Ball Problem,” *Theory Probab. Appl.* 9 (1964), 198–211, https://doi.org/10.1137/1109034 .
3. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387v1, first public 2008-09-25; later *Electronic Journal of Probability* 14 (2009), 365–384. https://arxiv.org/html/0809.4387v1 .
4. S. Sagitov, “The Multinomial Allocation Model and the Random Box Load,” arXiv:2604.15152v2 (2026), https://arxiv.org/html/2604.15152v2 .
