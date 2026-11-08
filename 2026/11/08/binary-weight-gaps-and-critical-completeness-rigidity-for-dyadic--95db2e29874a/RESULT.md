# Binary-weight gaps and critical completeness rigidity for dyadic floor rays

## Finding
For every real \(\alpha>0\), let \(a_j=\lfloor 2^j\alpha\rfloor\) (\(j\ge1\)), \(S_n=\sum_{j=1}^n a_j\), and let \(\mathcal P_\alpha\) be the set of all finite sums of terms indexed by distinct positive integers. Terms equal to zero are allowed, and equal values at distinct indices are separately indexed. Call the ray *complete* if \(\mathcal P_\alpha\) contains all sufficiently large nonnegative integers and *fully complete* if \(\mathcal P_\alpha=\mathbb Z_{\ge0}\).

**Theorem.** For \(0<\alpha<1\), choose the standard binary expansion \(\alpha=\sum_{i\ge1}b_i2^{-i}\), with eventually-zero digits for dyadic rationals, and put \(w_m=\sum_{i=1}^m b_i\). For every integer \(n\ge1\),
\[
 a_{n+1}-S_n-1=w_{n+1}-1.
\]
The interval of integers \(G_n=\{S_n+1,\ldots,a_{n+1}-1\}\), interpreted as empty if its upper endpoint is below its lower endpoint, consists entirely of integers absent from \(\mathcal P_\alpha\), and its size is exactly \((w_{n+1}-1)_+\). These intervals are pairwise disjoint. For **all** \(\alpha>0\),
\[
 \mathcal P_\alpha\text{ is complete}\quad\Longleftrightarrow\quad
 \mathcal P_\alpha=\mathbb Z_{\ge0}
 \quad\Longleftrightarrow\quad \alpha=2^{-k}\text{ for some integer }k\ge1.
\]

For uniformly sampled \(\alpha\in(0,1)\), at every integer \(n\ge1\) the signed gap defect \(a_{n+1}-S_n-1\) has the distribution \(\mathrm{Binomial}(n+1,1/2)-1\). In particular, the nonnegative gap length \(L_n=|G_n|\) has the exact law
\[
 \Pr(L_n=0)=\frac{n+2}{2^{n+1}},\qquad
 \Pr(L_n=\ell)=\frac{\binom{n+1}{\ell+1}}{2^{n+1}}
 \quad(1\le\ell\le n),
\]
and
\[
 \mathbb E\sum_{n=1}^{N}L_n
 =\frac{N(N-1)}4+\frac12(1-2^{-N})
 \qquad (N\ge1).
\]

More generally, for any fixed \(0<\alpha<1\) whose binary digit-one frequency exists and is \(\delta>0\), the number of integers \(\le X\) lying in the union of the **canonical intervals** \(G_n\) is
\[
 \frac{\delta}{2}(\log_2 X)^2+o_\alpha((\log X)^2)
 \qquad(X\to\infty).
\]
In particular this is \((1/4+o(1))(\log_2 X)^2\) for Lebesgue-almost every \(\alpha\in(0,1)\). Consequently, the total number of *all* nonrepresentable integers up to \(X\) is at least this quantity, not necessarily asymptotic to it. For the rational scalings \(\alpha=1/7\) and \(\alpha=3/7\), the corresponding canonical counts are respectively asymptotic to \((1/6)(\log_2 X)^2\) and \((1/3)(\log_2 X)^2\).

## Assumptions and scope
Only ordinary nonnegative subset sums with coefficients zero or one are considered. The exact binary identities and probability laws use \(0<\alpha<1\); completeness rigidity holds for all positive scalings. The binary expansion convention excludes the ambiguous eventually-one expansion for dyadic rationals. The canonical gap count is a lower bound, not an assertion that all missing integers occur in these intervals. The parameter \(\alpha\) is random only for the stated distributional conclusions.

## Proof
Write \(a_j=\sum_{i=1}^j b_i2^{j-i}\). Summing in the other order yields
\[
 S_n=\sum_{i=1}^n b_i(2^{n+1-i}-1),\qquad
 a_{n+1}=\sum_{i=1}^{n+1}b_i2^{n+1-i}.
\]
Their difference is \(a_{n+1}-S_n=\sum_{i=1}^{n+1}b_i=w_{n+1}\). Since the sequence \(a_j\) is nondecreasing, an integer strictly between \(S_n\) and \(a_{n+1}\) cannot be represented: a sum of earlier terms is at most \(S_n\), and any sum using a later term is at least \(a_{n+1}\). For different indices the intervals are disjoint because \(S_{n+1}=S_n+a_{n+1}\ge a_{n+1}\).

If \(\alpha\in(0,1)\) has at least two nonzero binary digits, the second occurs at some finite position. Thereafter \(w_{n+1}\ge2\), so every sufficiently large canonical interval is nonempty, providing infinitely many distinct missing integers. If it has exactly one nonzero digit, \(\alpha=2^{-k}\), with \(k\ge1\), and the positive terms form the sequence \(1,2,4,8,\ldots\); their distinct subset sums give every nonnegative integer. There is no expansion with zero nonzero digits for \(\alpha>0\). For \(\alpha\ge1\), set \(S_0=0\) and \(d_n=a_{n+1}-S_n-1\) for \(n\ge0\). Then \(d_0=\lfloor2\alpha\rfloor-1\ge1\), while
\[
 d_{n+1}-d_n=a_{n+2}-2a_{n+1}\in\{0,1\}.
\]
Thus every canonical gap from index zero onward is nonempty, again giving infinitely many missing integers. This proves both completeness equivalences.

For uniformly distributed \(\alpha\in(0,1)\), the first \(m\) binary digits are independent fair bits: every dyadic cylinder of length \(m\) has measure \(2^{-m}\). Hence \(w_{n+1}\) has the stated binomial law. The expectation follows from \((w_{n+1}-1)_+=w_{n+1}-1+\mathbf1_{\{w_{n+1}=0\}}\) and summing its expectation over \(n\le N\).

Suppose \(w_n/n\to\delta>0\). Then \(L_n=\delta n+o(n)\), so \(\sum_{n\le N}L_n=\delta N^2/2+o(N^2)\). All the intervals with \(a_{n+1}\le X\) are contained in \([1,X]\), and their terminal index satisfies \(N_X=\log_2 X+O_\alpha(1)\), since \(a_{n+1}=\lfloor2^{n+1}\alpha\rfloor\). At most one further interval intersects \([1,X]\); its length is at most \(n=O(\log X)\). Hence the canonical union has the claimed asymptotic. For Lebesgue-almost every scaling the binary digits have limiting one-frequency \(1/2\) by the strong law of large numbers. The binary expansions \(1/7=0.\overline{001}_2\) and \(3/7=0.\overline{011}_2\) have respective frequencies \(1/3\) and \(2/3\), giving the stated rational examples.

## Verification
The standalone `verify.py` checks 47,101 exact rational floor/popcount identities, 8,188 dyadic-cylinder representatives for the binomial multiplicity formula through eleven digits, and 140 absent integers against direct finite subset sums. It also tests the rational frequencies for \(1/7\) and \(3/7\). Execute with `python3 verify.py`. These finite computations test local arithmetic and cases but the unrestricted theorem follows from the displayed proof and the classical binary strong law.

## Relationship to prior work
Wu and Ma (arXiv:2610.38288, first posted 28 October 2026) prove that whenever a strictly increasing positive sequence satisfies the growth bound \(s_{n+1}\le2s_n\), at least one scaling yields all subset sums. Their Lemma 2.1 uses Brown's classical criterion. Applied to \(s_n=2^n\), their existence theorem does not identify the full scaling locus, give the exact prefix popcount identity, or supply the binomial gap law and canonical-hole asymptotics. Graham's 1971 survey discusses completeness of rounded geometric rays of ratio less than two and explicitly poses an open problem for two combined dyadic floor rays. The present result treats a **single** ray at the critical ratio two, and does not resolve the two-ray problem. The 2022 Ma--Chen theorem gives positive-measure results under strict subcritical growth hypotheses and is not a statement about this endpoint distribution.

## Limitations
The canonical gaps need not exhaust all nonrepresentable integers. The quadratic logarithmic asymptotic concerns precisely their union, and only gives a lower bound for the full complement. The theorem does not address a union of two or more dyadic rays, nor does it classify scaled geometric sequences with bases other than two. The endpoint rigidity and quantitative laws were compared to accessible published statements, but a previously implicit specialization of classical completeness criteria remains a historical-priority risk. Historical priority remains to be assessed beyond the inspected sources.

## References
1. B.-L. Wu and W.-X. Ma, *A note on a problem of Ma and Chen*, arXiv:2610.38288 (2026), first posted 28 October 2026, https://arxiv.org/abs/2610.38288.
2. R. L. Graham, *On sums of integers taken from a fixed sequence*, Proceedings of the Washington State University Conference on Number Theory (1971), 22--40, https://mathweb.ucsd.edu/~ronspubs/71_08_integer_sums.pdf.
3. W.-X. Ma and Y.-G. Chen, *Hegyvári's theorem on complete sequences, II*, Acta Arith. 203 (2022), 307--318, https://doi.org/10.4064/aa210811-30-3.
4. J. L. Brown, Jr., *Note on complete sequences of integers*, Amer. Math. Monthly 68 (1961), 557--560, https://doi.org/10.2307/2311150.
