# Exact sub-160-bit census of third–fourth order reciprocal prime pairs

## Finding
Let \(p,q\) be distinct primes and let \(\operatorname{ord}_m(t)\) denote the multiplicative order of \(t\) modulo \(m\). Among all ordered pairs with \(\max\{p,q\}\le 2^{160}\), exactly six satisfy
\[
\operatorname{ord}_q(p)=3,\qquad \operatorname{ord}_p(q)=4.
\]
They are, in the indicated order,
\[
\begin{gathered}
(137,37),\ (4817,1291),\ (4817,17977),\\
(934441,3487381),\ (998988257,3728274931),\\
(35166746297,131244083917).
\end{gathered}
\]
The cutoff is the 160-bit prime-size threshold discussed by Costello and Korpal. It is a finite classification, not a claim that no larger pairs exist.

## Assumptions and scope
All integers are ordinary positive integers; the two primes are ordered because the respective orders are different. A prime \(p\) in such a pair must be at least \(5\), and so must \(q\). For primes \(p,q\ge5\), the order conditions are equivalent to
\[
q\mid(p^2+p+1),\qquad p\mid(q^2+1).
\]
Indeed, the first congruence gives order precisely \(3\) (order \(1\) would imply \(q\mid3\)); the second gives order precisely \(4\) because \(q^2\equiv-1\pmod p\).

## Proof
**Algebraic reduction.** Consider arbitrary positive integers \(a,b\) satisfying
\[
b\mid a^2+a+1,\qquad a\mid b^2+1.\tag{1}
\]
They are coprime, because any common divisor divides \(b^2+1\) and \(b\), hence is \(1\). Therefore
\[
K=\frac{a^2+a+b^2+1}{ab}
\]
is a positive integer. If \(a>b\), replace \(a\) by \(a'=(b^2+1)/a\). This is a positive integer; if \(b\ge2\), then \(a'\le (b^2+1)/(b+1)<b\), while \(b=1\) forces \((a,b)=(2,1)\), giving \(a'=1\). If \(b>a\), the case \(b=a+1\) is impossible because \(a^2+a+1\equiv1\pmod{a+1}\). Thus when \(a\ge2\), \(b\ge a+2\) and \(b'=(a^2+a+1)/b<a\); when \(a=1\), \(b=3\), giving \(b'=1\). Equal coordinates imply \(a=b=1\) by coprimality.

Both replacements preserve the same integer \(K\): they interchange the two roots of one of the quadratic equations obtained from \(a^2+a+b^2+1=Kab\). Each nontrivial replacement strictly lowers the maximum coordinate. Repeated descent therefore reaches \((1,1)\), where \(K=4\). Conversely, the conic equation
\[
a^2+a+b^2+1=4ab\tag{2}
\]
implies both divisibilities by reduction modulo \(a\) and modulo \(b\). Consequently (1) is equivalent to (2).

**Exhaustive parametrization.** On the positive solutions of (2), define two involutions
\[
T_a(a,b)=(4b-a-1,b),\qquad T_b(a,b)=(a,4a-b).
\]
Every nonroot solution has a unique involution lowering its largest coordinate; the other involution increases that coordinate. Thus the entire positive solution set consists of the common root \((1,1)\) and the two nonintersecting rays obtained by alternating \(T_a,T_b\) and \(T_b,T_a\), respectively, starting at the root. Beyond their first steps, the maximum coordinate grows by at least a factor \(3\) at each step. Therefore, as soon as a ray first exceeds a fixed cutoff, every later node also exceeds it.

**Exact finite certification.** For the cutoff \(2^{160}\), both rays have together exactly \(169\) distinct nodes including the root. Exactly five nodes have a coordinate less than \(5\), leaving \(164\) candidates for the prime condition. Of these, \(81\) have an even coordinate greater than \(2\), and a further \(77\) have odd coordinates but at least one coordinate \(t\) satisfying
\[
2^{t-1}\not\equiv1\pmod t.
\]
Each such Fermat failure proves \(t\) composite. The remaining six nodes are precisely the listed pairs. All twelve coordinates are smaller than \(2^{64}\); their primality is proved by complete trial division up to the integer square root. Direct modular exponentiation establishes the required orders. Thus the list is complete and every listed pair is valid.

## Verification
The bundled Python 3 standard-library program `verify.py` reconstructs both rays using unbounded exact integers and stops only after exceeding \(2^{160}\). It checks the conic and divisibilities at every node; certifies the \(81+77\) exclusions; tests all remaining integers for primality by complete trial division; and verifies the two multiplicative orders directly. As an independent bounded algebraic cross-check it enumerates all solutions with both coordinates at most \(100000\) using the quadratic discriminant \(3a^2-a-1\), then compares the exact sets. Run `python3 verify.py` from the extracted package. The reported successful counts are \(169\) total nodes, \(164\) eligible nodes, \(81\) parity exclusions, \(77\) Fermat exclusions, and six prime pairs. The program needs no external packages.

## Relationship to prior work
Costello and Korpal (2025) define order reciprocity, implement a sieve through the first \(200\) million primes, and discuss \(160\)-bit prime-size thresholds. Their reported search bound is far smaller than \(2^{160}\). The new contribution is the **exact finite prime census at that literature-motivated cutoff**, not the general idea of a quadratic descent. Mills (1953, 1956) developed much broader methods for quadratic Diophantine equations, including those leading to linear recurrences, so the conic reduction and two-ray mechanism are used here as established-style tools rather than claimed as a new general method. Bibby, Vyncke and Zelinsky (2021 revision) classify related equal-degree cyclotomic divisibilities, but their results do not supply this finite mixed-order prime census. The older public questions on order reciprocity describe general order relations rather than this six-pair classification.

## Limitations
The finding has a natural but finite cutoff. It does not prove finiteness of all reciprocal-order prime pairs, nor any result for orders other than \((3,4)\). It does not produce secure pairing-friendly curves: small embedding degrees can be unsuitable for the cryptographic applications motivating the reference. Historical priority beyond the inspected literature, including unindexed numerical tables, is not certified. The primality verification is ordinary exact integer trial division, not an external formal proof or an independent mathematical audit.

## References
Costello, C., and Korpal, G., *On pairs of primes with small order reciprocity*, Cryptology ePrint Archive 2025/150 (first received 2025-01-31), https://eprint.iacr.org/2025/150 ; arXiv:2608.03268.

Mills, W. H., *A system of quadratic Diophantine equations*, Pacific Journal of Mathematics **3** (1953), 209–220, https://msp.org/pjm/1953/3-1/pjm-v3-n1-p15-p.pdf .

Mills, W. H., *Certain Diophantine equations linear in one unknown*, Canadian Journal of Mathematics **8** (1956), 5–12, https://doi.org/10.4153/CJM-1956-003-2 .

Bibby, S., Vyncke, P., and Zelinsky, J., *On the third largest prime divisor of an odd perfect number*, arXiv:1908.09420 (revised 2021), especially discussion of related quadratic divisor pairs.
