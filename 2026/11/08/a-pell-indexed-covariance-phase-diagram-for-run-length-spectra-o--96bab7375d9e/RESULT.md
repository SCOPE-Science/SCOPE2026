# A Pell-indexed covariance phase diagram for run-length spectra of fixed-composition binary words

## Finding
For fixed **distinct positive integers** \(r<s\), choose a binary word \(W^{(N)}\) of length \(N\) uniformly among those containing exactly \(a_N\) ones and \(N-a_N\) zeros. Let \(X_{N,r}\) count occurrences of the **fully bounded** pattern \(0\,1^r\,0\), entirely within the word; thus runs touching an endpoint are excluded. If \(a_N/N\to p\in(0,1)\), then
\[
\lim_{N\to\infty}\frac{\operatorname{Cov}(X_{N,r},X_{N,s})}{N}
=-p^{r+s-1}(1-p)^3 F_{r,s}(p),
\]
where
\[
 F_{r,s}(p)=(r+1)(s+1)p^2-(2rs+r+s-1)p+rs.
\]
Write \(\Delta_{r,s}=r^2+s^2-6rs-2(r+s)+1\). If \(\Delta_{r,s}<0\), the limiting covariance density is strictly negative for every \(p\in(0,1)\). If \(\Delta_{r,s}=0\), it is negative except for one tangency where it is zero. If \(\Delta_{r,s}>0\), it is positive precisely on the **nonempty** interval
\[
\frac{2rs+r+s-1-\sqrt{\Delta_{r,s}}}{2(r+1)(s+1)}
<p<
\frac{2rs+r+s-1+\sqrt{\Delta_{r,s}}}{2(r+1)(s+1)},
\]
and negative outside the closed interval. Equivalently, a positive-covariance density is possible precisely when
\[
 s>3r+1+\sqrt{8r(r+1)}.
\]
All positive integer pairs \((r,s)\) at the tangency boundary satisfy
\[
(2r+1)^2-2z^2=1,\qquad s=3r+1+2z,
\]
with the positive Pell solutions \((2r+1)+z\sqrt2=(3+2\sqrt2)^j\), \(j\ge1\). The first pairs are \((1,8),(8,49),(49,288)\). In particular, \((r,s)=(1,9)\) is the first pair with \(r=1\) allowing positive covariance density, exactly for \(3/5<p<3/4\).

At the first tangency, \((r,s)=(1,8)\), \(p=2/3\), an additional cancellation is exact: whenever \(N\ge15\) is divisible by \(3\), put \(a_N=2N/3\). Then
\[
\operatorname{Cov}(X_{N,1},X_{N,8})
=-\frac{256N(N-3)^2(2N-21)(2N-15)(2N-9)(2N-3)}{177147(N-10)(N-8)(N-7)(N-5)(N-4)(N-2)(N-1)^2}
=-\frac{4096}{177147N}+O(N^{-2}).
\]
More generally, along integer sequences satisfying \(\sqrt N(a_N/N-2/3)\to\lambda\in\mathbb R\),
\[
\operatorname{Cov}(X_{N,1},X_{N,8})\to
-18\left(\frac23\right)^8\left(\frac13\right)^3\lambda^2.
\]
These last limits concern *fixed* run lengths. No growing-run-length limit is claimed.

## Assumptions and scope
A fully bounded \(r\)-run is an occurrence of exactly \(r\) consecutive ones with a zero immediately before and immediately after, all positions lying within \(1,\dots,N\). Set \((x)_k=x(x-1)\cdots(x-k+1)\), \((x)_0=1\), with \((x)_k=0\) for nonnegative integral \(x<k\). The exact formulas below hold for \(N\ge r+s+4\), \(0\le a_N\le N\), \(r<s\). All asymptotic statements take \(r,s\) fixed and \(a_N/N\to p\in(0,1)\). For the displayed exact rational identity at \((1,8)\), additionally \(N\ge15\) is a multiple of three.

## Proof
Write \(b=N-a_N\) and \(P_N(o,z)=(a_N)_o(b)_z/(N)_{o+z}\), the probability that \(o\) specified sites are ones and \(z\) other specified sites are zeros. There are \(N-r-1\) possible interior starts, giving
\[
\mathbb E X_{N,r}=(N-r-1)P_N(r,2).
\]
For distinct \(r,s\), two pattern windows can occur simultaneously only if their prescribed sites are disjoint or if they share precisely a boundary zero. Any other overlap assigns a zero and a one to the same site. Writing \(h=N-r-s-2\), a direct count of ordered window placements gives \(h(h-1)\) disjoint pairs and \(2h\) single-boundary-zero pairs. Consequently
\[
\mathbb E[X_{N,r}X_{N,s}]
=h(h-1)P_N(r+s,4)+2hP_N(r+s,3).
\tag{1}
\]
This is a finite exact identity, not a probabilistic approximation.

For \(p_N=a_N/N\) in any compact subset of \((0,1)\) and fixed nonnegative \(o,z\), multiplication of the finite falling factorials yields uniformly
\[
P_N(o,z)=p_N^o(1-p_N)^z
\left(1+\frac{d_{o,z}(p_N)}{N}+O(N^{-2})\right),
\]
\[
d_{o,z}(p)=\frac12\left[(o+z)(o+z-1)-\frac{o(o-1)}p-\frac{z(z-1)}{1-p}\right].
\]
Substitute in (1) and subtract the product of the two means. The \(N^2\) terms cancel. Dividing by \(N\) and simplifying the remaining coefficient gives
\[
-p_N^{r+s-1}(1-p_N)^3 F_{r,s}(p_N)+O(N^{-1}).
\]
(The \(O(N^{-1})\) applies after division by \(N\).) This proves the covariance-density formula without a central limit theorem.

The quadratic \(F_{r,s}\) has positive leading coefficient, \(F_{r,s}(0)=rs>0\), \(F_{r,s}(1)=2>0\), and vertex \(p_*=(2rs+r+s-1)/(2(r+1)(s+1))\in(0,1)\). Its discriminant is \(\Delta_{r,s}\). Thus two distinct interior zeros exist exactly when \(\Delta_{r,s}>0\), and the covariance sign is reversed between them. For \(s\ge r\),
\[
\Delta_{r,s}=(s-3r-1)^2-8r(r+1),
\]
while \(\Delta_{r,r}<0\); hence the positive-discriminant range among \(s>r\) is exactly the strict upper inequality stated in the finding.

At equality, \(z=s-3r-1>0\) satisfies \(z^2=8r(r+1)\). Since \(z\) is even, write \(z=2u\) and \(x=2r+1\); then \(x^2-2u^2=1\). Conversely every nontrivial positive Pell solution yields a pair of distinct positive integers \((r,s)\). Pell's positive solutions are the stated powers of \(3+2\sqrt2\). For \((r,s)=(1,9)\), \(F=20(p-3/5)(p-3/4)\).

For \((r,s)=(1,8)\), \(F=18(p-2/3)^2\). Substitute \(a_N=2N/3\) into the *exact* two moment identities, cancel factorial products and factor the resulting rational function; the displayed rational identity follows. Its numerator and denominator have degrees seven and eight, giving the displayed \(N^{-1}\) coefficient. Finally, the same finite rational identities have a uniform expansion
\[
\operatorname{Cov}(X_{N,1},X_{N,8})=Nf(p_N)+g(p_N)+O(N^{-1}),
\]
for analytic functions \(f,g\) near \(2/3\), with \(f(p)=-18p^8(1-p)^3(p-2/3)^2\). The exact factorization at \(p_N=2/3\) forces \(g(2/3)=0\). Substituting \(p_N=2/3+\lambda N^{-1/2}+o(N^{-1/2})\) and using continuity of \(g\) proves the critical-window limit.

## Verification
The accompanying standard-library script `verify.py` independently enumerates every fixed-weight binary word in its checked finite ranges, compares exact means and mixed moments with the window formulas, tests the tangency rational identity at 56 successive admissible lengths, and checks the discriminant/Pell classification in many integer cases. Its completed run reported **2,440 exact checks passed**. The script is supplementary: the all-\(N\) and asymptotic results follow from the explicit combinatorial and algebraic proof above, not from exhaustive finite sampling.

## Relationship to prior work
Inoue and Aki (2005) analyze joint distributions of success runs of multiple prescribed lengths, including their Type IV (exact-length) scheme, for Bernoulli sequences. Their 2006 online paper develops the joint conditional generating function when symbol totals are fixed; its Theorem 4.2 directly covers the **general distributional framework** and consequently determines finite run moments in principle. These distributional frameworks and the finite mixed-moment reduction are not claimed as first discoveries. The present contribution is the *explicit universal asymptotic sign phase*, the arithmetic characterization of all degenerate boundary length pairs, and the extra cancellation at the first exceptional pair. Theorem 4.2 does not state these sign classifications or critical-window limits in the inspected section. Mytalas and Zazanis (2012 preprint, 2013 journal) give a covariance/CLT framework for unconditioned Bernoulli and Markov run statistics, not the same fixed-composition phase diagram. See the assessment report for the strongest potential implication and source-access risks.

## Limitations
The sign classification is for the limit of covariance divided by \(N\), not an assertion that the finite covariance always has the limiting sign. At roots where that limit vanishes, finite-size signs may depend on higher terms; only the stated first Pell pair is treated at the exact center and square-root window. Endpoint-touching runs and circular runs are different observables. The broad earlier conditional joint generating function formally determines all finite moments, so mathematical priority for a specialized consequence requires independent literature assessment; no independence or external certification is asserted. The critical-window statement does not claim a central limit theorem.

## References
1. K. Inoue and S. Aki, *Joint distributions of numbers of success runs of specified lengths in linear and circular sequences*, Annals of the Institute of Statistical Mathematics **57** (2005), 353–368. https://www.ism.ac.jp/editsec/aism/pdf/057_2_0353.pdf; DOI: 10.1007/BF02507029.
2. K. Inoue and S. Aki, *Joint distributions of numbers of runs of specified lengths in a sequence of Markov dependent multistate trials*, Annals of the Institute of Statistical Mathematics **59** (2007), 577–595; published online **17 June 2006**. https://www.ism.ac.jp/editsec/aism/pdf/059_3_0577.pdf; DOI: 10.1007/s10463-006-0056-6.
3. G. C. Mytalas and M. A. Zazanis, *Central Limit Theorem approximations for the number of runs in Markov-dependent binary sequences*, Journal of Statistical Planning and Inference **143** (2013), 321–333. https://doi.org/10.1016/j.jspi.2012.07.014.
4. E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics **12** (2005), R57. https://doi.org/10.37236/1954.
