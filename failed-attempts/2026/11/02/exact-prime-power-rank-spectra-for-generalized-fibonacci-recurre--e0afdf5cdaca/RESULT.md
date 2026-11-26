# Exact prime-power rank spectra for generalized Fibonacci recurrences

## Finding

For every prime \(p\ge5\), integer \(k\ge1\), and residue \(s\in\mathbb Z/p^k\mathbb Z\), define the generalized Fibonacci sequence by \(U_0(s)=0\), \(U_1(s)=1\), and \(U_{n+2}(s)=sU_{n+1}(s)-U_n(s)\). Its *rank* \(r_{p^k}(s)\) is the least positive integer \(n\) for which \(U_n(s)\equiv0\pmod{p^k}\). Such a rank exists for every parameter.

Put \(A_-=(p-1)/2\), \(A_+=(p+1)/2\), and let \(\varphi\) denote Euler's totient. For any positive integer \(r\), **the number of parameters with rank exactly \(r\)** is

\[
\#\{s\bmod p^k:r_{p^k}(s)=r\}=
\begin{cases}
2p^{k-1},&r=p^k,\\
\varphi(r),&r=dp^j,\ 0\le j<k,\ d>1,\ d\mid A_-\ \text{or}\ d\mid A_+,\\
0,&\text{otherwise}.
\end{cases}
\]

The middle alternatives are disjoint because \(A_-\) and \(A_+\) are consecutive. In particular,
\[
\max_{s\bmod p^k}r_{p^k}(s)=p^k,
\qquad
r_{p^k}(s)=p^k\ \Longleftrightarrow\ s\equiv2\text{ or }-2\pmod p.
\]
The latter parameters have density \(2/p\) among all residue parameters.

## Assumptions and scope

The prime is odd and at least five; the recurrence parameter \(t=-1\) is fixed. The variable \(s\) ranges over **all** residue classes modulo \(p^k\). Counts refer to distinct parameters, not index multiplicities. The theorem is an unrestricted statement for every such prime, exponent, and rank, not an inference from a finite census. The primary subject is arithmetic of Lucas and generalized Fibonacci sequences (MSC2020 11B39).

## Proof

**1. The discriminant-zero parameters.** Let \(V_0(s)=2\), \(V_1(s)=s\), and \(V_{n+2}(s)=sV_{n+1}(s)-V_n(s)\). The integer-polynomial identity
\[
U_{mn}(s)=U_m(s)U_n(V_m(s))
\]
follows by introducing roots \(\alpha,\alpha^{-1}\) of \(X^2-sX+1\) in a splitting ring, writing \(U_n(s)=(\alpha^n-\alpha^{-n})/(\alpha-\alpha^{-1})\), and clearing denominators; hence the identity holds identically over \(\mathbb Z[s]\).

At \(s=2\), the identities \(U_n(2)=n\) and \(U'_n(2)=n(n^2-1)/6\) follow from the recurrence or its derivative. Since \(p\ge5\), \(U_p(2)=p\) and \(U'_p(2)\equiv0\pmod p\). The same statements at \(s=-2\) give \(U_p(-2)=p\) (as \(p\) is odd) and \(U'_p(-2)\equiv0\pmod p\). Taylor expansion of the integer polynomial \(U_p\) at \(\pm2\) therefore yields
\[
U_p(w)\equiv p\pmod{p^2}\quad\text{whenever}\quad w\equiv\pm2\pmod p.
\]
For every \(s\equiv2\varepsilon\pmod p\) with \(\varepsilon\in\{1,-1\}\), the recurrence gives \(U_n(s)\equiv\varepsilon^{n-1}n\pmod p\), and \(V_n(s)\equiv2\varepsilon^n\pmod p\). Thus if \(p\nmid n\), \(v_p(U_n(s))=0\); applying the composition identity repeatedly with multiplier \(p\) increases the valuation by exactly one at each step. Consequently
\[
v_p(U_n(s))=v_p(n)\quad(n\ge1).
\]
The least zero modulo \(p^k\) is therefore exactly \(p^k\). There are precisely \(2p^{k-1}\) such parameters.

**2. The two nonramified parameter groups.** Now suppose \(s^2-4\) is a unit modulo \(p\), so the polynomial \(X^2-sX+1\) has distinct roots \(\alpha,\alpha^{-1}\) in the appropriate étale quadratic extension of \(R=\mathbb Z/p^k\mathbb Z\). The root difference is a unit, so
\[
U_n(s)=0\pmod{p^k}\quad\Longleftrightarrow\quad\alpha^{2n}=1.
\]
Thus \(r_{p^k}(s)=\operatorname{ord}(\alpha^2)\).

If \(s^2-4\) is a nonzero quadratic residue modulo \(p\), both roots lie in \(R^\times\), a cyclic group of order \((p-1)p^{k-1}\). If it is a nonsquare, they lie in the norm-one subgroup \(T\) of the unramified quadratic extension \(R[\eta]\) (\(\eta^2=\delta\), with \(\delta\) a nonsquare unit). This group has order \((p+1)p^{k-1}\) and is cyclic: its reduction is the cyclic order-\(p+1\) norm-one group in \(\mathbb F_{p^2}\), while its principal norm-one kernel is cyclic of order \(p^{k-1}\), generated for \(k>1\) by \((1+p\eta)/(1-p\eta)\). The two factors have coprime orders, so their product is cyclic.

Write \(T_-\) for the split group and \(T_+\) for the nonsplit norm-one group. Their orders are \(2A_-p^{k-1}\) and \(2A_+p^{k-1}\). Squaring maps either group two-to-one onto a cyclic group of order \(A_\pm p^{k-1}\). A square \(\alpha^2\) of order \(r=dp^j\), where \(d\mid A_\pm\) and \(0\le j<k\), is associated to a nonramified trace if and only if \(d>1\); indeed \(d=1\) makes \(\alpha\equiv\pm1\pmod p\), and conversely. For each admissible \(r\), the cyclic image contains exactly \(\varphi(r)\) elements of order \(r\). Each has exactly two square roots \(\alpha\), and the trace \(s=\alpha+\alpha^{-1}\) identifies the pair \(\alpha\leftrightarrow\alpha^{-1}\). Distinct traces cannot produce the same root pair: the two simple roots of \(X^2-sX+1\) lift uniquely from their reductions by Hensel's lemma. It follows that precisely \(\varphi(r)\) distinct trace parameters have rank \(r\) in either case.

Since \(A_-\) and \(A_+\) are relatively prime, the two sets of nontrivial tame divisors cannot overlap. Adding both cases gives the stated middle line. As a consistency check, the total nonramified count is
\[
\sum_{\epsilon\in\{-,+\}}\ \sum_{\substack{d\mid A_\epsilon\\d>1}}\ \sum_{j=0}^{k-1}\varphi(dp^j)
=p^{k-1}\bigl((A_--1)+(A_+-1)\bigr)
=(p-2)p^{k-1}.
\]
Together with the \(2p^{k-1}\) ramified parameters, this accounts for every residue \(s\pmod{p^k}\).

**3. Sharp maximum.** Every nonramified rank is at most \(A_+p^{k-1}<p^k\), whereas both ramified classes attain \(p^k\). This proves the sharp threshold and its exact frequency. \(\square\)

## Verification

The accompanying standalone `verify.py` uses only integer arithmetic. It enumerates all residue parameters and first-zero ranks for \(21\) combinations of prime and exponent, and compares the entire observed multiplicity function with the totient formula. The tested primes are \(5,7,11,13,17,19,23,29\), with depths up to \(4\). All \(7{,}129\) parameter cases passed. In addition, the verifier checks that exactly the classes \(s\equiv\pm2\pmod p\) attain the maximum. Execute with `python3 verify.py` from this document's directory. This finite enumeration is supporting evidence; the preceding proof covers every prime and depth.

## Relationship to prior work

Soohyun Park, *Arithmetic properties of generalized Fibonacci sequences* (arXiv:1407.8086, first posted 2014-07-30), Theorem 19, interprets rank modulo \(p\) by the order of a characteristic root, and Theorem 20 proves the coarser general bound \(r(p^k)\le p^k+1\). Its concluding discussion expressly identifies dependence of \(r(p^k)\) on \(s\) as a question for further study. Hua-Chieh Li (2000) studies second-order recurrences modulo a **prime** and supplies the repeated-root and split/nonsplit constraints. Neither referenced result states the all-prime-power parameter distribution above. The present proof extends the cyclic-root analysis to two unit groups over prime-power rings, explicitly handles ramification, and counts trace parameters rather than only root orders. Published work on periods of fixed Lucas recurrences and on regularity of Lucas sequences concerns different invariants and does not imply the trace-parameter rank census.

## Limitations

The theorem is restricted to \(p\ge5\) and companion constant \(-1\); it does not classify arbitrary \(t\), ramified primes two or three, or ranks over arbitrary composite moduli. The limiting proportion \(2/p\) is a proportion of recurrence coefficients, not of indices or prime values. Historical priority remains qualified: an equivalent distribution could occur in a specialized trace/order-counting source not located in the literature comparison. Independent mathematical validation has not been performed.

## References

- Soohyun Park, *Arithmetic properties of generalized Fibonacci sequences*, arXiv:1407.8086v1 (first publicly posted 2014-07-30), especially Section 4, Theorems 19–21. https://arxiv.org/abs/1407.8086.
- Hua-Chieh Li, *Complete and Reduced Residue Systems of Second-Order Recurrences Modulo p*, Fibonacci Quarterly **38** (2000), 272–281. https://www.fq.math.ca/Scanned/38-3/li2.pdf.
- Miho Aoki and Yuho Sakai, *On Equivalence Classes of Generalized Fibonacci Sequences*, Journal of Integer Sequences **19** (2016), Article 16.2.6 (study of initial-condition equivalences rather than variable-coefficient prime-power ranks).
