# Exact adjacent-digit law for a composite-base automatic number-theory sequence

## Finding
For every integer \(n\ge1\), put
\[
A_n=(2n-1)(16^n-4),\qquad d_n=\left(A_n/15^{\nu_{15}(A_n)}\right)\bmod15,
\]
where \(\nu_{15}(m)=\min(\nu_3(m),\nu_5(m))\) and \(d_n\) is the representative in \(\{0,1,\ldots,14\}\). Define
\[
R=\{3,6,9,12\},\quad E=\{2,5,8,11,14\},\qquad q(j)=\begin{cases}3/37&j\in R,\\5/37&j\in E,\\0&\text{otherwise}.\end{cases}
\]
For any residues \(i,j\in\{0,\ldots,14\}\), the exact limiting frequency of their ordered adjacency is
\[
\pi_{i,j}=\frac15\left(\mathbf 1_{(i,j)\in\{(12,6),(9,3),(3,12)\}}+\mathbf 1_{i=6}q(j)+q(i)\mathbf 1_{j=9}\right).
\]
In fact,
\[
\#\{1\le n\le N:(d_n,d_{n+1})=(i,j)\}=\pi_{i,j}N+O((1+\log N)^2)
\]
with an absolute implied constant. Exactly twenty ordered pairs ever occur, and all twenty have positive limiting frequencies. The one-site limiting law is \(8/37\) for each member of \(R\), \(1/37\) for each member of \(E\), and zero otherwise.

## Assumptions and scope
Indices are positive integers, not arbitrary integers or negative indices. The last nonzero digit is taken in positional base \(15\), so entire factors of \(15\) are stripped before reduction modulo \(15\). Limiting frequencies use consecutive indices \(1\le n\le N\), with \(N\to\infty\). All arithmetic formulas are exact; the asymptotic assertion has a logarithmic-squared counting error. The underlying strictly automatic sequence and pointwise digit framework were introduced in the cited earlier paper; only the complete adjacency distribution, support classification, and quantitative counts are asserted here.

## Proof
Write \(t=2n-1\), \(a=\nu_3(t)\), \(b=\nu_5(t)\), and \(u=t/5^b\). Since \(16^n-4=4(4^t-1)\), the lifting-the-exponent identity gives \(\nu_3(A_n)=2a+1\) and \(\nu_5(A_n)=b\). Furthermore,
\[
(4^t-1)/(3t)\equiv1\pmod3,\qquad (16^n-4)\equiv2\pmod5.
\]
After division by \(15^{\min(2a+1,b)}\), the resulting digit satisfies
\[
d_n\equiv 2u\,3^{-b}\pmod5\quad\text{if }b\le2a+1.
\]
For \(b<2a+1\), it is \(0\pmod3\); for \(b=2a+1\), it is \(2\pmod3\) (the exponent \(2a+1\) is odd). For \(b>2a+1\), it is simultaneously \(2\pmod3\) and \(0\pmod5\), hence \(d_n=5\). These cases prove the exact digit classification by the Chinese remainder theorem. In particular, if \(5\nmid t\) then
\[
(t\bmod5,d_n)=(1,12),(2,9),(3,6),(4,3).
\]

For a uniformly sampled residue in a growing interval, the \(3\)-adic and \(5\)-adic valuations of \(t\) are independent by the Chinese remainder theorem. Conditional on \(5\mid t\), their exact distributions are
\[
\Pr(a=r)=\frac2{3^{r+1}},\qquad \Pr(b=s\mid b\ge1)=\frac4{5^s}\quad(r\ge0,s\ge1).
\]
In consequence,
\[
\Pr(b\ge2a+1\mid b\ge1)=\sum_{r\ge0}\frac2{3^{r+1}5^{2r}}=\frac{25}{37}.
\]
Conditionally, the equality event has probability \(20/37\), the strict excess event \(5/37\), and the strict deficit event \(12/37\). In each fixed valuation stratum, \(u\bmod5\) is uniform on the four units; hence the strict deficit gives each of \(R\) conditional probability \(3/37\), the equality gives each of \(E\setminus\{5\}\) probability \(5/37\), and the excess gives \(5\) probability \(5/37\). This proves \(q\).

Successive indices correspond to \(t\mapsto t+2\). Partition the indices into the five equally frequent residue classes of \(t\pmod5\). Classes \(1,2,4\) give the deterministic pairs \((12,6),(9,3),(3,12)\). Class \(3\) gives \((6,d_{n+1})\), with the next digit distributed according to \(q\) because \(5\mid t+2\). Class \(0\) gives \((d_n,9)\) with the first digit distributed as \(q\). Combining these mutually exclusive cases yields the displayed \(\pi_{i,j}\). The two nine-edge stars share exactly one edge, \((6,9)\), so the support has \(3+9+9-1=20\) pairs; positivity proves these are all attained. Summing over the second coordinate gives the one-site frequencies.

For the error, each event fixing \(a,b\) and the final unit residue is a union of at most eight progressions modulo \(3^{a+1}5^{b+1}\), hence its count up to \(N\) differs from its density times \(N\) by an absolute constant. On \(t=2n-1\le2N+1\), only \(O(1+\log N)\) values of each valuation occur. Summing over the \(O((1+\log N)^2)\) valuation strata proves the error. The excluded tails of the limiting valuation distribution beyond \(2N+1\) contribute \(O(1)\) to the expected counts. The adjacent-pair classes are combinations of these single-digit events and fixed congruence classes, so the same bound applies.

## Verification
The supplied standalone Python 3 program `verify.py` checks \(300\) digits by directly constructing \(A_n\), independently evaluates \(200000\) consecutive digit pairs using the valuation/CRT identity, verifies all \(20\) predicted pairs and all rational masses, and verifies that every observed pair belongs to the predicted support. The largest absolute numerical count deviation in this trial was below two. Exact rational identities are tested using `fractions.Fraction`; the finite loop is corroboration and does not replace the preceding proof.

## Relationship to prior work
Sobolewski's paper first introduced precisely this base-\(15\) last-nonzero-digit sequence in Example 5.3 and showed that it is strictly \(75\)-automatic, giving a pointwise digit formula. That pointwise formula is a starting point, not a newly claimed result. Neither its main classification nor the inspected example supplies the exact \(20\)-pair adjacency language, rational transition frequencies, or logarithmic-squared discrepancy bound. Work on factorial last nonzero digits addresses a different sequence. An independent database search found related transition laws for other automatic arithmetic words but no statement covering this specific sequence. The comparisons do not establish absolute uniqueness; other unindexed treatments could contain an equivalent pair law.

## Limitations
The theorem concerns only adjacent pairs, not all longer blocks, spectral measures, mixing, or an independent construction of a minimal automaton. It establishes limiting frequencies with a uniform quantitative bound, not exact counts at every arbitrary finite cutoff. A subsequent literature discovery of a complete adjacent-pair law would affect the novelty assessment; the existence of a pointwise digit formula by itself is acknowledged and is not being claimed as new.

## References
- B. Sobolewski, *On k-regularity of sequences of valuations and last non-zero digits*, arXiv:2202.09922 (first public version 20 February 2022); *Ramanujan Journal* **61** (2023), 1151–1195, Example 5.3, https://doi.org/10.1007/s11139-023-00710-8.
- B. Sobolewski, *On the last nonzero digits of n! in a given base*, arXiv:1809.06947 (2018), *Acta Arithmetica* **191** (2019), 173–189, https://arxiv.org/abs/1809.06947 (distinct motivating example).
