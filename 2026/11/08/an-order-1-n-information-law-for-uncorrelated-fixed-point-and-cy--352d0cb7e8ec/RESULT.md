# An order-\(1/n\) information law for uncorrelated fixed-point and cyclic-core counts

## Finding

Let \(f_n:[n]\to[n]\) be chosen uniformly from all \(n^n\) mappings, and write \(F_n=|\{v:f_n(v)=v\}|\) for the number of fixed points and \(C_n\) for the number of vertices belonging to directed cycles of its functional graph. Entropies and Kullback–Leibler divergences use natural logarithms (nats).

For **every integer \(n\ge 2\)**, these statistics are uncorrelated but not independent:
\[
\operatorname{Cov}(F_n,C_n)=0,\qquad I(F_n;C_n)>0.
\]
Their mutual information has the exact first-order decay
\[
\boxed{\lim_{n\to\infty}n I(F_n;C_n)=\mathcal J
=\sum_{m=1}^{\infty}m\,D_{\mathrm{KL}}(Q_m\|\operatorname{Pois}(1))
=3.692926238979770132438700\ldots,}
\]
where \(Q_m\) is the fixed-point-count distribution in a uniform permutation of \(m\) elements. In particular, \(I(F_n;C_n)=\mathcal J/n+o(n^{-1})\), and \(\mathcal J\) is strictly positive and finite. The summands admit a rapidly convergent explicit finite formula, with rigorous truncation bounds given below.

## Assumptions and scope

There are no restrictions on mapping images or graph components. Every map on the labeled set \([n]=\{1,\ldots,n\}\) has probability \(n^{-n}\), including maps with self-loops and multiple incoming edges. A cyclic vertex belongs to a directed orbit cycle of any positive length, so every map has at least one cyclic vertex. The statistic \(F_n\) counts cycles of length one. Information is between **the two aggregate integer counts**, not between the full labeled functional graph and a count.

For \(1\le m\le n\), define
\[
w_{n,m}=\Pr(C_n=m)=\frac{m(n)_m}{n^{m+1}},\qquad
Q_m(k)=\frac{1}{k!}\sum_{j=0}^{m-k}\frac{(-1)^j}{j!}\quad(0\le k\le m),
\]
where \((n)_m=n(n-1)\cdots(n-m+1)\), and put \(Q_m(k)=0\) for \(k>m\). Thus \(Q_m(k)\) is equivalently the number of permutations of \(m\) with exactly \(k\) fixed points divided by \(m!\). Let \(B_n=\operatorname{Bin}(n,1/n)\) and \(P=\operatorname{Pois}(1)\).

## Proof

**1. Conditional law.** Choosing the cyclic vertex set of size \(m\), a permutation on those vertices, and an oriented forest flowing into them yields \(\binom nm m!\,m n^{n-m-1}\) maps. Hence \(\Pr(C_n=m)=w_{n,m}\). Conditional on the cyclic set, its permutation is uniform and independent of the attached forest. Consequently,
\[
\Pr(F_n=k\mid C_n=m)=Q_m(k).
\]
Each map value \(f_n(v)\) is independent uniform on \([n]\), so the fixed-point indicators are independent Bernoulli with parameter \(1/n\); the unconditional law of \(F_n\) is \(B_n\). A uniform permutation of any nonempty size has mean exactly one fixed point, giving \(\mathbb E(F_n\mid C_n=m)=1\), \(\mathbb E F_n=1\), and therefore \(\operatorname{Cov}(F_n,C_n)=0\). But \(Q_1\) is concentrated at one, whereas \(B_n\) is not when \(n\ge2\); since \(w_{n,1}>0\), the variables are not independent.

**2. Exact information identity.** For any full-support reference probability \(P\), the KL chain rule gives
\[
I(F_n;C_n)=\sum_{m=1}^{n}w_{n,m}D_{\mathrm{KL}}(Q_m\|P)-D_{\mathrm{KL}}(B_n\|P).
\tag{1}
\]
Use the Poisson law \(P=\operatorname{Pois}(1)\). This identity is exact for each finite \(n\); it does not replace the actual marginal \(B_n\) with a Poisson law inside the mutual information.

**3. Summable control of the rencontres divergence.** Put \(d_m=D_{\mathrm{KL}}(Q_m\|P)\). For \(0\le k\le m\), the alternating-series remainder in the formula for \(Q_m\) gives
\[
|Q_m(k)-P(k)|\le\frac{1}{k!(m-k+1)!}.
\]
For \(k>m\), \(Q_m(k)=0\). Using \(D_{\mathrm{KL}}(Q_m\|P)\le\chi^2(Q_m\|P)\), summing the displayed bounds against \(P(k)^{-1}=e k!\), and bounding the Poisson tail, we obtain
\[
0\le d_m\le\frac{e2^{m+1}+1}{(m+1)!}.
\tag{2}
\]
Thus \(\sum_{m\ge1}m d_m\) converges absolutely. Since
\[
nw_{n,m}=m\frac{(n)_m}{n^m}\longrightarrow m\quad\text{for fixed \(m\)},
\qquad 0\le nw_{n,m}\le m,
\]
dominated convergence for series (extending \(w_{n,m}=0\) when \(m>n\)) yields
\[
\lim_{n\to\infty}n\sum_{m=1}^n w_{n,m}d_m=\sum_{m=1}^{\infty}m d_m.
\tag{3}
\]

**4. Negligible binomial-to-Poisson divergence.** Let \(X\sim B_n\). For \(0\le k\le n/2\), expansion of the exact likelihood ratio gives
\[
\log\frac{B_n(k)}{P(k)}
=1+(n-k)\log(1-1/n)+\sum_{i=0}^{k-1}\log(1-i/n)
=\frac{-k^2+3k-1}{2n}+O\!\left(\frac{1+k^3}{n^2}\right),
\tag{4}
\]
with a constant uniform in \(n\ge4\) and this range of \(k\). The binomial factorial moments satisfy \(\mathbb EX=1\), \(\mathbb E(X)_2=1-1/n\), and \(\sup_n\mathbb E X^3\le5\). Hence the expectation of the leading term in (4) is exactly \(1/(2n^2)\). For \(k>n/2\), the absolute log likelihood is at most \(O(n\log n)\), while \(\Pr(X\ge\lceil n/2\rceil)\le1/\lceil n/2\rceil!\) by the factorial-moment bound. Taking the expectation in (4) and controlling this negligible tail proves
\[
D_{\mathrm{KL}}(B_n\|P)=O(n^{-2}).
\tag{5}
\]
Combining (1), (3) and (5) proves the asserted limit and asymptotic order.

**5. Positivity and evaluation.** Since \(Q_1\) is the point mass at one, \(d_1=1\), so \(\mathcal J\ge1>0\). To evaluate it, compute the integers \(D_0=1\), \(D_1=0\), \(D_j=(j-1)(D_{j-1}+D_{j-2})\) for \(j\ge2\), and
\[
Q_m(k)=\frac{D_{m-k}}{k!(m-k)!},\qquad
d_m=\sum_{k=0}^m Q_m(k)\log(e\,k!\,Q_m(k)),
\]
with zero terms interpreted by continuity. Truncation after \(M\) terms has error at most
\[
\sum_{m>M}\frac{m(e2^{m+1}+1)}{(m+1)!}.
\]
For \(M=30\), this bound is below \(1.5\cdot10^{-24}\), giving the displayed numerical digits.

## Verification

The standalone standard-library checker `check.py` enumerates all mappings exactly for \(1\le n\le6\) and compares their complete joint count table with \(w_{n,m}Q_m(k)\). It also checks permutation factorial moments, the exact KL chain identity against direct finite mutual-information evaluation, and a high-precision summation with an explicit remainder bound. The delivered script passed 341 checks. Exact finite enumeration corroborates the conditional law but is not used as a proof for arbitrary size; the infinite limit follows from the displayed uniform bounds and dominated convergence.

## Relationship to prior work

The conditional uniform permutation on the cyclic set and the uniform rooted-forest representation are classical random-mapping facts, developed in particular by Flajolet–Odlyzko and explicitly used by Hansen–Jaworski. The rencontres distribution and its Poisson limit are classical permutation results. The present assertion concerns a different statistic: **the exact rate and universal coefficient of mutual information between the number of fixed points and the total number of cyclic vertices, despite identically zero covariance**. The proof depends on the low-probability small cyclic cores, rather than on the typical Rayleigh-scale core of size of order \(\sqrt n\).

## Limitations

The theorem concerns uniform random mappings only; no analogous coefficient is claimed for constrained mappings, permutations with nonuniform law, or other cycle-length counts. The asymptotic statement gives a first-order equivalent, not a complete higher-order expansion. The underlying conditional permutation distribution was already known. The priority of this particular information-theoretic asymptotic cannot be certified against every historical treatment of functional graphs; broad random-mapping generating-function theory may allow other derivations. No claim of computational certification or independent audit is made.

## References

1. J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria 94 (2010), 341–359, publisher-hosted full text: https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf .
2. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989 proceedings, LNCS 434 (1990), 329–354, DOI: https://doi.org/10.1007/3-540-46885-4_34 .
3. M. Soria, *Distribution of Image Points in Random Mappings*, Algorithms Seminar, November 10, 1996, https://algo.inria.fr/seminars/sem96-97/soria.html .
4. P. Diaconis, J. Fulman and R. Guralnick, *On fixed points of permutations*, arXiv:0708.2643, https://arxiv.org/abs/0708.2643 .
