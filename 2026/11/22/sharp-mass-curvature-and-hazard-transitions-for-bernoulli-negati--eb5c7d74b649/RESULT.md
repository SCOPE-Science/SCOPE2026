# Sharp mass-curvature and hazard transitions for Bernoulli–negative-binomial counts

## Finding

Let \(X=B+N\), where \(B\sim\mathrm{Bernoulli}(p)\) and \(N\sim\mathrm{NB}(\nu,q)\) are independent, with \(0<p,q<1\), \(\nu>0\), and \(\Pr(N=k)=(\nu)_k q^k(1-q)^\nu/k!\). Set \(r=p/(1-p)\), and let \(m_k=\Pr(X=k)\). Define the discrete hazard \(h_k=m_k/\Pr(X\ge k)\). Then:

1. If \(\nu\ge1\), the masses are log-concave at every interior index and the hazards are nondecreasing at every index. At \(\nu=1\), \(h_0<h_1=h_2=\cdots=1-q\); for \(\nu>1\) the hazards strictly increase.
2. If \(0<\nu<1\), the masses are strictly log-convex at every index \(k\ge2\). The entire sequence is log-convex exactly when
   \[
   r\le L_\nu(q):=\frac q2\bigl(\sqrt{\nu(2-\nu)}-\nu\bigr).
   \]
   Above this sharp boundary, the first interior triple is strictly log-concave and every later interior triple is strictly log-convex.
3. If \(0<\nu<1\), the hazard sequence is nonincreasing exactly when
   \[
   r\le D_\nu(q):=\frac{\sqrt{\nu^2q^2+4[1-(1-q)^\nu-\nu q]}-\nu q}{2}.
   \]
   It is strictly decreasing for \(r<D_\nu(q)\), has \(h_0=h_1>h_2>\cdots\) at equality, and has exactly one peak at index \(1\) for \(r>D_\nu(q)\): \(h_0<h_1>h_2>h_3>\cdots\).
4. The two exact boundaries are separated strictly: \(0<L_\nu(q)<D_\nu(q)\) for all \(0<\nu,q<1\). Thus there are decreasing-failure-rate distributions in this family that are **not log-convex**.

For instance, \(\nu=q=1/2\), \(p=1/11\), hence \(r=1/10\), lies strictly between the two thresholds. The masses have a strictly log-concave first triple and strictly log-convex subsequent triples, whereas the entire hazard sequence is strictly decreasing.

## Assumptions and scope

All conclusions are for the full-support, zero-based parameterization displayed above, with finite real parameters \(0<p,q<1\) and \(\nu>0\). The rising and falling hazard statements compare \(h_k\) and \(h_{k+1}\) for **every** integer \(k\ge0\); mass curvature compares \(m_k^2\) and \(m_{k-1}m_{k+1}\) for every \(k\ge1\). In particular, strict log-convexity means \(m_k^2<m_{k-1}m_{k+1}\). Neither asymptotic truncation nor a finite count cutoff is assumed.

The generating function is
\[
G(z)=(1-p+pz)\left(\frac{1-q}{1-qz}\right)^\nu.
\]
The parameter domain and convolution agree with the NB–shifted-NB family introduced in the original 2023 article; the new claims concern exact mass and failure-rate shape boundaries, not its construction.

## Proof

**1. Exact masses and neighboring ratios.** Put \(M_k=q(\nu+k-1)+rk\) for \(k\ge1\). Direct convolution gives
\[
m_0=\frac{(1-q)^\nu}{1+r},\quad
m_k=\frac{(1-q)^\nu}{1+r}\frac{(\nu)_{k-1}q^{k-1}}{k!}M_k\quad(k\ge1).
\]
All masses are positive. Writing \(R_k=m_{k+1}/m_k\), we obtain
\[
R_0=\nu q+r,\qquad
R_k=\frac{q(\nu+k-1)M_{k+1}}{(k+1)M_k}\quad(k\ge1).
\]
Their first difference is
\[
R_1-R_0=-\frac{\nu(\nu-1)q^2+2\nu qr+2r^2}{2(\nu q+r)}.
\]
For each integer \(k\ge1\), algebraic subtraction gives the all-index identity
\[
R_{k+1}-R_k=\frac{q(1-\nu)S_k}{(k+1)(k+2)M_kM_{k+1}},
\]
where, with \(t=k-1\ge0\),
\[
\begin{split}
S_k={}&(q+r)^2t^2+
\bigl[q^2(2\nu+1)+2qr(\nu+3)+5r^2\bigr]t\\
&+q^2\nu(\nu+1)+4qr(\nu+1)+6r^2.
\end{split}
\]
Every coefficient is strictly positive, so \(S_k>0\) for all admissible parameters and \(k\ge1\). This establishes that the tail ratios are strictly increasing if \(\nu<1\), constant if \(\nu=1\), and strictly decreasing if \(\nu>1\), **at every index**.

**2. Sharp mass-curvature boundary.** The masses are log-concave at interior index \(k\) exactly when \(R_k\le R_{k-1}\), and log-convex when the reverse inequality holds. For \(\nu\ge1\), the preceding identities yield \(R_0>R_1\ge R_2\ge\cdots\), proving the first mass-curvature assertion. If \(0<\nu<1\), the ratios \(R_1<R_2<\cdots\) give strict log-convexity at every interior index \(k\ge2\). The remaining condition \(R_0\le R_1\) is equivalent to
\[
2r^2+2\nu qr-\nu(1-\nu)q^2\le0,
\]
whose unique positive boundary is \(L_\nu(q)\). At equality the first triple has zero log-curvature; the strict alternatives follow directly.

**3. From mass ratios to hazards.** Since the masses sum to one and are positive,
\[
\frac{1}{h_k}=1+\sum_{j\ge1}\prod_{i=0}^{j-1}R_{k+i}.
\]
The series is finite for every fixed \(k\), because it equals \(\Pr(X\ge k)/m_k\). If all successive \(R_{k+i}\) increase with \(k\), each nonconstant product increases, hence \(h_k\) decreases; if they decrease, \(h_k\) increases. The tail-ratio identity therefore proves strict decreasing hazards for \(k\ge1\) when \(\nu<1\), strict increasing hazards at \(k\ge1\) when \(\nu>1\), and equality for \(k\ge1\) when \(\nu=1\). When \(\nu\ge1\), \(R_0>R_1\) gives \(h_0<h_1\), completing this case.

For \(\nu<1\), the only undecided hazard comparison is between indices \(0\) and \(1\). Because \(\Pr(X\ge0)=1\) and \(\Pr(X\ge1)=1-m_0\),
\[
h_0\ge h_1\iff m_0(1-m_0)\ge m_1
\iff r^2+\nu qr\le1-(1-q)^\nu-\nu q.
\]
Strict concavity of \(x\mapsto x^\nu\) on the positive half-line ensures that the rightmost quantity is strictly positive for \(0<\nu,q<1\). The quadratic in \(r\) is strictly increasing for \(r\ge0\), and its unique positive root is \(D_\nu(q)\). This proves every hazard case and shows the boundary is necessary as well as sufficient.

**4. Strict separation of the boundaries.** At \(r=L_\nu(q)\), one has \(R_0=R_1<R_2<R_3<\cdots\). Comparing each product in the two reciprocal-hazard series at indices \(0\) and \(1\) gives \(1/h_1>1/h_0\), strictly from terms of length at least two. Thus \(h_0>h_1\) at \(r=L_\nu(q)\). As the sign of \(h_0-h_1\) changes only at the unique positive root \(D_\nu(q)\), it follows that \(L_\nu(q)<D_\nu(q)\). Positivity of \(L_\nu(q)\) is immediate from \(0<\nu<1\).

**5. Exact example.** With \(\nu=q=1/2\) and \(r=1/10\), the numerator \(\nu(\nu-1)q^2+2\nu qr+2r^2\) of the first ratio difference is \(3/400>0\), so \(R_1<R_0\) while all later ratios increase. Also
\[
r^2+\nu qr=\frac7{200}
<\frac34-\frac1{\sqrt2}=1-(1-q)^\nu-\nu q.
\]
The strict inequality is certified by \(143/200>1/\sqrt2\), since \(143^2=20449>20000\). Therefore \(h_0>h_1>h_2>\cdots\). This is a fully exact witness of decreasing hazards without log-convex masses.

## Verification

Run `python verify.py` with Python and SymPy available. The script independently simplifies the two mass-ratio identities to zero, checks exact coefficient formulas, verifies the rational witness and both thresholds, and makes additional finite-index rational cross-checks. Its finite-index checks corroborate but do not replace the universally quantified algebra and hazard comparison in the proof. The checker returns an explicit `PASS` message on success.

## Relationship to prior work

Ong, Sim, Liu and Srivastava (2023, Section 2.6) introduced the NB–shifted-NB count family and asserted log-concavity, strong unimodality and increasing failure rate throughout its stated domain \(\nu>0\). Their log-concavity argument invokes closure under convolution for log-concave factors, but the negative-binomial factor is log-concave only for \(\nu\ge1\). The results above identify the sharp actual regimes on the whole domain. The original probability law, convolution representation, and the general connection between mass ratios and failure-rate ageing are not claimed as new.

Letac, Malouche and Maurer (2002) studied the **same Bernoulli-plus-negative-binomial convolution** via positivity of coefficients of arbitrary real convolution powers and Jørgensen sets; their material was compared at the level of the underlying generating function. Its target is not the first-hazard boundary or all-index mass-curvature/hazard classification established here. Ben Salah (2021/2022) studied generalized real convolution powers of Bernoulli plus infinitely divisible factors, again a different invariant. Generic convolution closure statements do not supply the two explicit shape-transition thresholds for this family.

## Limitations

These are analytical statements about the infinite-support distribution, not estimates from observational data. They do not classify every named ageing order (such as IFRA), nor extend to the boundary values \(p=0\) or \(p=1\), which are excluded from the hypotheses. Historical priority remains subject to independent literature review, including inaccessible older papers, even though the mathematical implication comparisons with the closest located work found no covering theorem. No independent external mathematical audit has been performed.

## References

1. S. H. Ong, S. Z. Sim, S. Liu and H. M. Srivastava, *A Family of Finite Mixture Distributions for Modelling Dispersion in Count Data*, Stats 6 (2023), 942–955, first publicly published 18 September 2023, https://doi.org/10.3390/stats6030059. Specifically Sections 2.2 and 2.6.
2. G. Letac, D. Malouche and S. Maurer, *The Real Powers of the Convolution of a Negative Binomial Distribution and a Bernoulli Distribution*, Proc. Amer. Math. Soc. 130 (2002), 2107–2114, https://doi.org/10.1090/S0002-9939-02-05352-2.
3. N. Ben Salah, *Generalized Convolution Product of an Infinitely Divisible Distribution and a Bernoulli Distribution*, Commun. Stat. Theory Methods 51 (2022), 7297–7304, first online 1 February 2021, https://doi.org/10.1080/03610926.2021.1879863.
4. J. Keilson and H. Gerber, *Some Results for Discrete Unimodality*, J. Amer. Statist. Assoc. 66 (1971), 386–389, as cited for the classical log-concavity criterion in reference 1.
