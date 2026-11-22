# All-prime arity valuation spectra and sharp periods for Fuss–Catalan numbers

## Finding
For every fixed integer \(n\ge2\), prime \(p\), and variable integer arity parameter \(t\ge0\), define the integral Fuss–Catalan number
\[
C_t(n)=\frac{1}{tn+1}\binom{(t+1)n}{n}.
\]
Put \(a=\nu_p(n)\) and define the **reduced carry column**
\[
m=\begin{cases}n/p^a,&a>0,\\ n-1,&a=0.\end{cases}
\]
Write \(m=\sum_{i=0}^{L-1}d_i p^i\) with \(0\le d_i<p\) and \(d_{L-1}>0\). For a formal indeterminate \(z\), define
\[
T_d(z)=\frac1p\begin{pmatrix}p-d&dz\\p-d-1&(d+1)z\end{pmatrix},\qquad
(A(z),B(z))=(1,0)T_{d_0}(z)\cdots T_{d_{L-1}}(z).
\]
Then for **every** \(v\ge0\), the natural density \(\mu_{p,n}(v)\) of arities \(t\ge0\) with \(\nu_p(C_t(n))=v\) exists, and the complete probability generating function is
\[
\boxed{\displaystyle\sum_{v\ge0}\mu_{p,n}(v)z^v=A(z)+\frac{p-1}{p-z}B(z).}\tag{1}
\]
In particular the law has an exactly geometric tail of ratio \(1/p\) after its \(L\)-th coefficient; its nondivisibility density and mean are respectively
\[
\boxed{\mu_{p,n}(0)=\prod_{i=0}^{L-1}\frac{p-d_i}{p},\qquad
\sum_{v\ge0}v\mu_{p,n}(v)=\frac{s_p(m)}{p-1},}\tag{2}
\]
where \(s_p(m)=\sum_i d_i\).

For **every** threshold \(k\ge1\), the integer sequence
\[
t\longmapsto\min\bigl(k,\nu_p(C_t(n))\bigr)
\]
has least positive period, starting at \(t=0\) (not merely an eventual period),
\[
\boxed{p^{L+k-1}.}\tag{3}
\]
Consequently the exact number of \(t\) in each complete period \(0\le t<p^{L+k-1}\) with valuation \(v<k\) is \(p^{L+k-1}\mu_{p,n}(v)\), and the number with valuation at least \(k\) is the remaining mass. Equations (1)–(3) are uniform in all the quantified integers and primes, not asymptotic in \(n\).

## Assumptions and scope
The \(p\)-adic valuation \(\nu_p(b)\) counts the power of a prime \(p\) dividing a positive integer \(b\). Here \(n\) and \(p\) are fixed while the integer arity parameter \(t\ge0\) varies. Natural density refers to the limit of \(N^{-1}\#\{0\le t<N:\nu_p(C_t(n))=v\}\) as \(N\to\infty\), for each fixed \(v\). The notation \(s_p\) is base-\(p\) digit sum. No distribution of the prime-free unit part of \(C_t(n)\) is asserted.

## Proof
**Step 1: reduce the Fuss–Catalan valuation to a fixed binomial column.** If \(a=\nu_p(n)>0\), then \(tn+1\) is a \(p\)-unit. Kummer's theorem and the fact that multiplying both summands by \(p^a\) merely appends \(a\) zero base-\(p\) digits give
\[
\nu_p(C_t(n))=\nu_p\binom{(t+1)n}{n}
=\nu_p\binom{(t+1)m}{m}
=\nu_p\binom{m+mt}{m}.
\]
If \(p\nmid n\), the exact factorial identity
\[
C_t(n)=\frac1n\binom{(t+1)n}{n-1}
\]
and \(\nu_p(n)=0\) give
\[
\nu_p(C_t(n))=\nu_p\binom{(t+1)n}{n-1}
=\nu_p\binom{(n-1)+(nt+1)}{n-1}.
\]
Thus in both cases \(\nu_p(C_t(n))=\nu_p\binom{m+u(t)}m\), where \(u(t)=mt\) if \(p\mid n\), and \(u(t)=nt+1\) otherwise. Crucially, the slope of \(u\) is coprime to \(p\) in either case. For every \(r\ge1\), this affine map is a permutation of the \(p^r\) input residue classes. Therefore all valuation statistics and least prime-power periods in \(t\) agree with those of the fixed-column binomial valuation \(V(u)=\nu_p\binom{m+u}{m}\).

**Step 2: exact carry transfer.** By Kummer, \(V(u)\) is the number of carries when adding \(m\) and \(u\) in base \(p\). Given an incoming carry \(c\in\{0,1\}\) and a fixed digit \(d\) of \(m\), a uniformly sampled digit of \(u\) creates an outgoing carry for exactly \(d+c\) of the \(p\) possibilities; the other \(p-d-c\) possibilities terminate it. Multiplication by \(z\) counts each outgoing carry. This gives exactly the transition matrix \(T_d(z)\) displayed above, with rows indexed by incoming state and columns by outgoing state. Starting in state zero and processing all \(L\) digits gives the two polynomials \(A(z)\) and \(B(z)\).

Above digit \(L-1\), the digits of \(m\) vanish. An existing carry terminates with probability \((p-1)/p\) and continues, contributing another carry, with probability \(1/p\). Its tail generating function therefore obeys \(H=(p-1)/p+(z/p)H\), whence \(H=(p-1)/(p-z)\). A vanished carry contributes weight one. Thus the generating function of the total number of carries is \(A+BH\), proving (1) as an identity of power series at zero.

For each fixed \(v\), the event of exactly \(v\) carries is determined by a finite prefix of digits: if a carry continues into the all-zero portion above digit \(L-1\), each additional step contributes a carry, so to decide \(V(u)=v\) it suffices to inspect the first \(L+v+1\) digits. Its density exists and equals its finite-digit probability. The exceptional infinite run of maximal digits has probability zero, so the probabilities sum to one. The affine permutation in Step 1 transfers these densities to arities. Since \(A\) and \(B\) have degree at most \(L\), (1) has an exact geometric coefficient tail for degrees strictly greater than \(L\).

**Step 3: nondivisibility and expectation.** There are zero carries if and only if each input digit \(u_i\) obeys \(u_i+d_i<p\), independently for all \(i<L\), giving the first part of (2). For every \(j\ge1\), the probability of a carry from the first \(j\) digits to digit \(j\) is exactly \((m\bmod p^j)/p^j\), as the first \(j\) digits of \(u\) are uniform. The expected total number of carries is the sum of these probabilities. Expanding \(m\) by digits and exchanging nonnegative sums gives
\[
\sum_{j\ge1}\frac{m\bmod p^j}{p^j}
=\sum_{i=0}^{L-1}d_i\sum_{j=i+1}^{\infty}p^{i-j}
=\frac{\sum_i d_i}{p-1}.
\]
This proves the second part of (2), including convergence of the expectation.

**Step 4: sharp threshold periods.** Fix \(k\ge1\). Every carry above position \(L-1\) must follow an unbroken chain beginning no later than position \(L-1\). Reaching an outgoing carry from digit \(L+k-2\) forces at least \(k\) carries. Consequently the first \(L+k-1\) digits of \(u\) determine \(\min(k,V(u))\); thus \(p^{L+k-1}\) is a period.

For sharpness, fix the lower \(L-1\) digits of \(u\) to zero, so no carry enters the top nonzero digit of \(m\). When \(k=1\), the threshold predicate depends nontrivially on the digit \(u_{L-1}\): exactly \(d_{L-1}\) of its \(p\) values start a carry. Thus translation by \(p^{L-1}\) cannot be a period. For \(k\ge2\), choose \(u_{L-1}=p-d_{L-1}\) to create a carry; set the next \(k-2\) digits, at positions \(L,\ldots,L+k-3\), equal to \(p-1\), thereby forcing exactly \(k-1\) outgoing carries before position \(L+k-2\). At this final digit, a carry continues precisely when \(u_{L+k-2}=p-1\). Hence the capped valuation is nonconstant as this digit ranges through \(0,\ldots,p-1\), so translation by \(p^{L+k-2}\) is not a period. Because any period of a sequence with a \(p\)-power period has a least period dividing that \(p\)-power, the least period in \(u\) is exactly \(p^{L+k-1}\). An affine change with unit slope multiplies a translation of \(t\) by a \(p\)-unit: at the decisive digit it permutes all \(p\) values nontrivially, so the same sharpness holds for \(t\). This establishes (3). Exact histogram formulas over the period then follow from density and periodicity. \(\square\)

## Verification
Run `python verify.py` using Python 3 with standard-library modules only. This independently computes exact integer Fuss–Catalan values and binomial coefficients, checks the valuation reductions for \(2\le n\le27\), \(0\le t<40\), and \(p\in\{2,3,5,7\}\), and compares full-period capped valuation histograms against exact rational carry-matrix probabilities wherever the period is at most 1500. It also checks sharpness of the periods and the expectation identity for all \(1\le m\le100\) at those four primes. Output:
```
VERIFY_OK assertions=59040 full_period_histograms=352 primes=2,3,5,7 mean_cases=400
```
These are finite tests only; the unrestricted results follow from the preceding proofs.

For example, with \(n=6\), \(p=2\), one obtains \(m=3\), \(L=2\), and
\[
\sum_{v\ge0}\mu_{2,6}(v)z^v
=\frac14+\frac{z/4+z^2/2}{2-z},
\]
with \(\mu_{2,6}(0)=1/4\), \(\mu_{2,6}(1)=1/8\), and \(\mu_{2,6}(v)=5/2^{v+2}\) for \(v\ge2\). The least period of the capped valuation at level \(k\) is \(2^{k+1}\).

## Relationship to prior work
Kummer's digit-carry theorem and the classical definition of Fuss–Catalan numbers are foundational, not claimed as new. Stănică's 2000 work studies divisibility of generalized Catalan numbers for special fixed arities as the size index varies; it does not give the all-prime distribution or period law across variable arities for arbitrary fixed size.

Barat–Grabner (author-hosted manuscript dated 2002-06-06) derives general binomial-row valuation asymptotics and digital-function machinery, but its Sections 3–4 count varying row-and-column pairs rather than an arbitrary fixed column sampled as the upper argument varies. Rowland (2011) records the Lu–Tsai theorem, which already gives the **upper bound** \(p^{L+k-1}\) for the period of the full binomial residue modulo \(p^k\). That fact does not by itself prove the **least period** for its coarser capped valuation, nor the complete arity distribution (1). Spiegelhofer–Wallner (initial public posting 2016-04-24), Section 2.4, gives a **known binary fixed-column density framework**. Therefore the \(p=2\) marginal density technique is not claimed as a new independent discovery; the result here is the complete fixed-size all-prime Fuss–Catalan arity theorem, including its precise normalization split, explicit uniform digit law, and sharp thresholds for every \(k\).

An existing published result on prime-power Pascal columns establishes all-prime valuation densities and sharp periods for that **special family of fixed columns**, not the arbitrary-digit reduced columns \(m\) here. Another published sparse-shift result gives the first interaction correction for separated nonzero digits, not the complete all-prime distribution or its periods. Prior classifications of ternary or five-ary Fuss–Catalan valuation spectra vary the **size** with arity held fixed; they do not imply the present variable-arity conclusions.

## Limitations
The claim concerns the valuation distribution in the arity parameter, not the residues of the prime-free parts, and does not assert statistical independence across distinct primes. The all-prime formula is built from classical Kummer carries and shares special cases with previously known binary fixed-column theory. Published or unindexed digit-automaton literature could contain an equivalent implicit formulation. The accessible introduction and main divisibility results of Stănică and relevant sections of the other highly relevant primary sources were inspected. Historical priority outside the inspected material remains unproved.

## References
- P. Stănică, *\(p^q\)-Catalan Numbers and Squarefree Binomial Coefficients*, arXiv:math/0010148, first posted 2000-10-15, https://arxiv.org/abs/math/0010148.
- G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, author-posted full paper (dated 2002-06-06), https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf.
- E. Rowland, *Two binomial coefficient conjectures*, arXiv:1102.1464, first posted 2011-02-07, https://arxiv.org/abs/1102.1464.
- L. Spiegelhofer and M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089, first posted 2016-04-24, https://arxiv.org/abs/1604.07089.
- E. Kummer, classical carry interpretation of binomial valuations (1852); discussed in the preceding references.
- *Prime-power Pascal columns: exact valuation densities and sharp threshold periods* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-prime-power-pascal-columns-exact-valuation-densities-and-sharp-t--4b2115180ea3.
- *First-interaction law for sparse shifts in odd-prime binomial valuations* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-first-interaction-law-for-sparse-shifts-in-odd-prime-binomial-va--5aa645fd919f.
