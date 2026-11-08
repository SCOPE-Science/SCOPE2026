# Reentrant covariance phases of occupancy-frequency counts and sample collisions

## Finding

Fix integers \(m\ge2\) and \(n\ge2\). Assign \(n\) independently sampled balls uniformly to \(m\) labeled boxes. Write \(N_i\) for the occupancy of box \(i\), and define the frequency count and unordered pair-collision count
\[
F_r=\sum_{i=1}^{m}\mathbf1\{N_i=r\},\qquad
C=\sum_{i=1}^{m}\binom{N_i}{2},\qquad 0\le r\le n.
\]
Set
\[
p_r=\binom nr m^{-r}\left(1-\frac1m\right)^{n-r},\qquad
Q_{m,n}(r)=m^2r^2-m(2n+m-2)r+n(n-1).
\]
Then the complete frequency-versus-collision covariance profile is
\[
\boxed{\operatorname{Cov}(F_r,C)=\frac{p_r}{2(m-1)}Q_{m,n}(r).}
\tag{1}
\]
For any fixed \(m,n\), its sign is **positive in two outer frequency ranges and negative in one nonempty central interval**, with possible zero-covariance frequencies at the two boundaries. Precisely, with
\[
\rho_\pm=\frac{2n+m-2\pm\sqrt{(m-2)^2+4n(m-1)}}{2m},
\]
\(\operatorname{Cov}(F_r,C)<0\) exactly when \(\rho_-<r<\rho_+\), is zero exactly when \(r=\rho_-\) or \(r=\rho_+\), and is positive otherwise. Both endpoint frequencies \(r=0\) and \(r=n\) have strictly positive covariance. At least one integer frequency has negative covariance.

The singleton frequency has the especially sharp sign boundary
\[
\boxed{\operatorname{Cov}(F_1,C)=\frac{n(n-1)(n-2m)}{2m}
\left(1-\frac1m\right)^{n-1}.}
\tag{2}
\]
Hence \(F_1\) has negative covariance with collisions below \(n=2m\), zero at exactly \(n=2m\), and positive covariance above it. Put \(\widehat D=C/\binom n2\) and \(\widehat G=1-\widehat D\), the unbiased Simpson concentration and Gini--Simpson diversity statistics. If \(K=\sum_{r=1}^nF_r\) is observed richness, comparison with its established uniform-law covariance gives the exact contrast
\[
\boxed{\operatorname{Cov}(F_1,\widehat D)
=(n-2m)\operatorname{Cov}(K,\widehat G)
=\frac{n-2m}{m}\left(1-\frac1m\right)^{n-1}.}
\tag{3}
\]
Thus the singleton-based Good--Turing coverage statistic changes its covariance direction relative to diversity even though observed richness remains positively correlated with diversity.

For each fixed frequency \(r\ge2\) and box count \(m\ge2\), varying the sample size \(n\ge r\) gives a **reentrant** positive--negative--positive sequence (with possible zeros at the transitions): the two real transition sizes are
\[
\nu_\pm(m,r)=mr+\frac{1\pm\sqrt{1+4m(m-1)r}}2.
\tag{4}
\]
The covariance is negative exactly for integer \(n\) strictly between these roots, positive outside them, and zero at integral roots. As \(m\to\infty\) with \(n/m\to\lambda>0\) and fixed \(r\), the sign away from critical values is governed by \((\lambda-r)^2-r\); the two limiting sampling intensities are \(\lambda=r\pm\sqrt r\). There are infinitely many double-zero sample-size pairs: for \(m=3\), take any odd integer \(t\ge7\) not divisible by three, put \(r=(t^2-1)/24\), and use the two distinct admissible sizes \(n=3r+(1\pm t)/2\).

## Assumptions and scope

Balls are independent, and every box has probability exactly \(1/m\). The counts include the empty-box frequency \(F_0\) so that \(\sum_{r=0}^{n}F_r=m\) deterministically. The collision statistic counts **pairs** of balls rather than the number of multiply occupied boxes. All formulas are exact for integer \(m,n\ge2\), \(0\le r\le n\). The reentrant statement fixes an integer \(r\ge2\) as \(n\) varies, and the asymptotic statement holds only away from the displayed critical intensities.

## Proof

By symmetry and linearity,
\[
\operatorname{Cov}(F_r,C)=m\operatorname{Cov}(\mathbf1\{N_1=r\},C)
=mp_r\left(\mathbb E[C\mid N_1=r]-\mathbb EC\right).
\tag{5}
\]
The \(n-r\) other balls, conditional on \(N_1=r\), remain independent and uniform among the \(m-1\) other boxes. Therefore
\[
\mathbb E[C\mid N_1=r]=\binom r2+\frac{1}{m-1}\binom{n-r}{2},
\quad \mathbb EC=\frac1m\binom n2.
\tag{6}
\]
Here \(p_r>0\) is the binomial occupancy probability. Substitution of (6) into (5), followed by multiplication by \(2m(m-1)\), yields the exact quadratic (1).

The leading coefficient of \(Q_{m,n}\) is \(m^2>0\) and its discriminant in \(r\) is
\[
m^2\bigl((m-2)^2+4n(m-1)\bigr)>0.
\]
Thus its two roots are exactly \(\rho_\pm\) and the stated sign rule follows. At the endpoints,
\[
Q_{m,n}(0)=n(n-1)>0,\qquad
Q_{m,n}(n)=n(n-1)(m-1)^2>0.
\]
There must also be a negative *integer* frequency. Indeed, \(\sum_{r=0}^nF_r=m\) implies \(\sum_{r=0}^n\operatorname{Cov}(F_r,C)=0\), whereas the \(r=0\) summand is strictly positive. If all other summands were nonnegative, their sum could not be zero. Convexity of the quadratic then makes the negative-frequency indices one contiguous interval. Substitution \(r=1\) gives the factorization
\[
Q_{m,n}(1)=(n-1)(n-2m),
\]
which proves (2). Division by \(\binom n2\) proves the first equality in (3). The already-established richness-diversity covariance under the uniform law is
\[
\operatorname{Cov}(K,\widehat G)=m^{-1}(1-1/m)^{n-1},
\]
which proves the remaining equalities in (3).

For fixed \(m,r\), expand the same quadratic in sample size:
\[
Q_{m,n}(r)=n^2-(2mr+1)n+m^2r^2-m(m-2)r.
\tag{7}
\]
Its discriminant in \(n\) is \(1+4m(m-1)r\), giving the two roots (4). Because \(r\ge2\) and \(m\ge2\),
\[
Q_{m,r}(r)=r(r-1)(m-1)^2>0,
\qquad \nu_-(m,r)>r.
\]
The gap \(\nu_+-\nu_-=\sqrt{1+4m(m-1)r}\) is greater than four, so there is at least one integer sample size in the strictly negative interval. For sufficiently large \(n\), the positive leading term in (7) dominates. The resulting discrete phase order is therefore positive, then negative, then positive (allowing exact zeros at integral boundary sizes).

For fixed \(r\) and \(n/m\to\lambda\), divide \(Q_{m,n}(r)\) by \(m^2\) to obtain
\[
\lim_{m\to\infty}\frac{Q_{m,n}(r)}{m^2}
=\lambda^2-2\lambda r+r(r-1)=(\lambda-r)^2-r.
\]
This proves the limiting critical ratios away from zeros. Finally, any odd \(t\) coprime to three has \(t^2\equiv1\pmod{24}\), so \(r=(t^2-1)/24\) is a positive integer for \(t\ge7\). Setting \(m=3\) makes the discriminant in (4) equal to \(t^2\), and \(n=3r+(1\pm t)/2\) are integers. They satisfy \(n\ge r\) because \(4r+1\ge t\) for \(t\ge7\), and both annihilate (7). This proves the infinite double-zero family.

## Verification

The accompanying standalone `check_collision.py` recomputes the conditional-expectation formula using exact rational arithmetic and independently enumerates complete labeled allocations on a bounded grid (up to \(5^7\) allocation words where allowed). It checks the quadratic sign law, contiguous negative-frequency interval, singleton boundary, exact integer-root criterion and fixed-frequency reentrant pattern on additional bounded grids. It also checks the explicit infinite-family formula for finitely many integer parameters. The script returned **174,349 exact integer/rational assertions passed**. Enumeration is corroboration, not an infinite proof: the proof above supplies the all-parameter argument.

## Relationship to prior work

Gnedin, Hansen and Pitman (2007) define the occupancy frequency spectrum and provide general moment formulas and asymptotic regimes. Barbour and Gnedin (2008) study the joint normal approximation of occupancy frequency counts and their limiting covariance structures; Barbour (2009) studies one-dimensional translated-Poisson approximations. Those treatments establish the underlying occupancy setting, but the inspected sections do not present the exact covariance profile (1), its two sign ranges or the fixed-frequency reentrant and arithmetic orthogonality classifications.

Källberg, Leonenko and Seleznjev (2011) analyze pair-coincidence \(U\)-statistics as estimators of Rényi functionals, emphasizing asymptotic normality rather than their finite covariance with occupancy frequency counts.

A published finite-uniform occupancy result gives a **one-switch** sign law for covariance between richness and \(F_r\); another published categorical-sample result proves positive covariance of richness and Gini--Simpson diversity under arbitrary fixed iid category probabilities. These results concern different pairs of statistics. In particular, the latter proves the known richness factor used in (3), but neither yields an individual-frequency collision sign classification without additional joint covariance information. The contribution here is the exact *two-wing* sign structure, the strict singleton sampling threshold, the reentrant sample-size phase and the infinite integer zero family, not generic multinomial moment calculability.

## Limitations

The sign classification requires equal box probabilities; no heterogeneous-probability extension is claimed. A covariance sign does not imply stochastic monotonicity or independence, and zero covariance at boundary parameters does not mean independence. The fixed-frequency asymptotic sign statement excludes its critical values. Earlier general urn-moment identities may implicitly contain equation (1); historical priority of the qualitative classification has not been independently certified. This result does not assert novel raw binomial or multinomial moments.

## References

1. A. Gnedin, B. Hansen and J. Pitman, *Notes on the occupancy problem with infinitely many boxes: general asymptotics and power laws*, arXiv:math/0701718 (first submitted 2007-01-24), https://arxiv.org/pdf/math/0701718.
2. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387 (first submitted 2008-09-25), https://arxiv.org/pdf/0809.4387.
3. A. D. Barbour, *Univariate approximations in the infinite occupancy scheme*, arXiv:0902.0879 (first submitted 2009-02-05), https://arxiv.org/pdf/0902.0879.
4. D. Källberg, N. Leonenko and O. Seleznjev, *Statistical Inference for Rényi Entropy Functionals*, arXiv:1103.4977 (first submitted 2011-03-25), https://arxiv.org/pdf/1103.4977.
5. *A one-switch covariance law for occupancy richness and frequency counts*, publicly available research record `SCOPE-20261004-93dddb2be813`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813.
6. *Universal positive covariance of sample richness and unbiased Gini--Simpson diversity*, publicly available research record `SCOPE-20261004-e84114bd4ba0`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-universal-positive-covariance-of-sample-richness-and-unbiased-gi--e84114bd4ba0.
