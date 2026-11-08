# An \(83.2878\%\) lower-density certificate for Zumkeller-plus-square sums

## Finding
A positive integer \(z\) is **Zumkeller** when its positive divisors can be partitioned into two subsets of equal sum. Let
\[
\mathcal R=\{N\in\mathbb Z_{>0}:N=z+x^2,\ z\text{ is Zumkeller},\ x\in\mathbb Z_{>0}\}.
\]
Then
\[
\boxed{\liminf_{X\to\infty}\frac{\#(\mathcal R\cap[1,X])}{X}\ge
\frac{2768772438842683346}{3324339686048415489}
=0.8328789174170931\ldots.}
\]
More precisely, there is an explicitly described periodic set \(\mathcal C_*\), of exactly the displayed rational density, such that **every** \(N\in\mathcal C_*\) with \(N>236421376\) is in \(\mathcal R\). The improvement over the ten-prime single-support square-residue certificate is exactly \(12/175\) (more than 6.85 percentage points), supplied by the mixed-prime Zumkeller integer \(70=2\cdot5\cdot7\). The displayed bound is **not** asserted to be the exact density of all representable integers.

## Assumptions and scope
All integers, primes, summands and square bases are positive unless a residue variable explicitly ranges from zero. Define \(\sigma(z)=\sum_{d\mid z}d\). For any odd prime \(p\), let
\[
G_p=\{r\bmod p^2:\exists x\in\mathbb Z,\ p\mid r-x^2,\ p^2\nmid r-x^2\}.
\]
Let \(P=\{3,5,7,11,13,17,19,23,29,31\}\), \(a(p)=\min\{a\ge1:p\le2^{a+1}-1\}\), and let \(E_a\subset\mathbb Z/2^a\mathbb Z\) be the square residues. Define the first certificate set
\[
\mathcal C=\bigcup_{p\in P}\{N:N\bmod2^{a(p)}\in E_{a(p)},\ N\bmod p^2\in G_p\}.
\]
Define a second, mixed-prime certificate set
\[
\mathcal T=\{N:N\bmod4\in\{2,3\},\ N\bmod25\in G_5,\ N\bmod49\in G_7\}.
\]
The set in the theorem is \(\mathcal C_*=\mathcal C\cup\mathcal T\), which is periodic by the Chinese remainder theorem. No claim of optimality among possible certificates or of density one is made.

## Proof
**1. Zumkeller building blocks.** For an odd prime \(p\) with \(p\le2^{a+1}-1\), the divisors of \(2^ap\) sum to \((2^{a+1}-1)(p+1)\). The difference between half this sum and the divisor \(2^ap\) is
\[
R=(2^{a+1}-1-p)/2\in\{0,\ldots,2^a-1\}.
\]
A subset of the distinct divisors \(\{2^j:0\le j<a\}\) sums to \(R\) by binary expansion; with \(2^ap\) it has exactly half of the divisor sum. Therefore \(2^ap\) is Zumkeller. Separately, \(\sigma(70)=144\), and the divisor subset \(\{70,2\}\) sums to \(72\), proving that \(70\) is Zumkeller.

If \(q\) is Zumkeller and \(\gcd(t,q)=1\), then \(qt\) is Zumkeller: the divisors of \(qt\) correspond bijectively to pairs of divisors of \(q\) and \(t\), and multiplying each half-partition of divisors of \(q\) by every divisor of \(t\) multiplies both sums by \(\sigma(t)\).

**2. The ten-prime certificate really produces representations.** If \(N\) belongs to the \(p\)-event in \(\mathcal C\), choose an integer \(x\) satisfying \(x^2\equiv N\pmod{2^{a(p)}}\) and \(v_p(N-x^2)=1\). The two conditions can be imposed together using CRT and a positive \(x\le 2^{a(p)}p^2\). Put \(z=N-x^2\). For \(N>(2^{a(p)}p^2)^2\), we have \(z>0\) and \(2^{a(p)}\mid z\), \(v_p(z)=1\). Write \(z=2^bp t\) with \(b\ge a(p)\) and \(\gcd(t,2p)=1\). Step 1 implies \(z\) is Zumkeller. Since \(2^{a(p)}p^2\le16\cdot31^2=15376\), the uniform bound \(N>15376^2\) suffices.

**3. Density of the ten-prime certificate.** A residue \(r\bmod p^2\) belongs to \(G_p\) exactly when either (i) its reduction modulo \(p\) is a nonzero quadratic residue, or (ii) \(p\mid r\) but \(p^2\nmid r\). In case (i), among the \(p\) lifts of a nonzero square root modulo \(p\), exactly one solves the congruence modulo \(p^2\); a different lift gives valuation exactly one. In case (ii), the root \(x=0\) works. The other cases fail. Thus
\[
|G_p|=p(p-1)/2+(p-1)=\frac{(p-1)(p+2)}2.
\]
The binary square-residue probabilities for \(E_1,E_2,E_3,E_4\) are \(1,1/2,3/8,1/4\). The prime groups indexed by \(a(p)=1,2,3,4\) are respectively \(\{3\}\), \(\{5,7\}\), \(\{11,13\}\), and \(\{17,19,23,29,31\}\). Put
\[
B_a=\prod_{p\in P:\ a(p)\le a}\left(1-\frac{(p-1)(p+2)}{2p^2}\right).
\]
Explicitly,
\[
B_1=\frac49,\quad B_2=B_1\frac{11}{25}\frac{22}{49},\quad
B_3=B_2\frac{56}{121}\frac{79}{169},
\]
\[
B_4=B_3\frac{137}{289}\frac{172}{361}\frac{254}{529}\frac{407}{841}\frac{466}{961}.
\]
The four disjoint binary strata \(E_1\setminus E_2\), \(E_2\setminus E_3\), \(E_3\setminus E_4\), \(E_4\), taken as nested congruence properties modulo \(16\), have proportions \(1/2,1/8,1/8,1/4\). CRT makes the conditions at distinct odd prime squares independent. Consequently,
\[
\operatorname{dens}(\mathcal C)
=1-\frac{B_1}{2}-\frac{B_2}{8}-\frac{B_3}{8}-\frac{B_4}{4}
=\frac{63520442937841228526}{83108492151210387225}.
\]
This ten-prime intermediate bound is included to make the stronger mixed-prime result self-contained.

**4. The extra mixed-prime classes.** A residue \(N\pmod4\) admits a square \(x^2\) with \(v_2(N-x^2)=1\) if and only if \(N\equiv2\) or \(3\pmod4\). By the CRT, the defining conditions of \(\mathcal T\) give a positive \(x\le4\cdot25\cdot49=4900\) with \(v_2(N-x^2)=v_5(N-x^2)=v_7(N-x^2)=1\). Therefore \(N-x^2=70t\) with \(t>0\), \(\gcd(t,70)=1\) whenever \(N>4900^2\); Step 1 proves it is Zumkeller.

Every \(p\)-event in \(\mathcal C\) with \(p\ge5\) requires \(N\) to be a square modulo \(4\), so it is disjoint from \(\mathcal T\). The remaining \(p=3\) event is just \(N\bmod9\in G_3\), which is CRT-independent of the moduli \(4,25,49\). Hence the **new** residue classes have exact density
\[
\operatorname{dens}(\mathcal T\setminus\mathcal C)
=\frac12\frac{14}{25}\frac{27}{49}\left(1-\frac59\right)
=\frac{12}{175}.
\]
Combining this with Step 3 gives
\[
\operatorname{dens}(\mathcal C_*)
=\frac{63520442937841228526}{83108492151210387225}+\frac{12}{175}
=\frac{2768772438842683346}{3324339686048415489}.
\]
By Steps 2 and 4, every \(N\in\mathcal C_*\) with \(N>15376^2=236421376\) is representable. Deleting finitely many integers does not affect natural density, proving the theorem.

## Verification
Run the standalone exact-arithmetic checker using `python3 verify.py`. It independently enumerates the defining root residues modulo every \(p^2\) for the ten primes, checks the prime-power Zumkeller building blocks by their divisor partitions, evaluates all rational probabilities, and counts the new classes directly on the period \(4\cdot9\cdot25\cdot49=44100\). On this period it finds \(6804\) classes of \(\mathcal T\), \(3780\) classes of \(\mathcal T\cap\mathcal C\), and exactly \(3024\) genuinely additional classes, or \(12/175\). All computations are exact. The proof of representability and the asymptotic conclusion come from the arguments above, not from sampling.

## Relationship to prior work
Somu, Kukla, and Tran (2023), Proposition 4.11, prove eventual representability in ten residue classes modulo \(18\), giving lower density \(5/9\); their Theorem 4.17 proves infinitely many failures, and Conjecture 4.21 predicts those failures have density zero. A ten-prime single-support congruence sieve already yields the stronger quantitative bound \(0.7643074888\ldots\). Its conditions require a square residue modulo \(4\) except for the lone \(p=3\) event. The additional \(70\)-support construction exploits the complementary **nonsquare** residues \(2,3\pmod4\) and therefore adds the exact disjoint density \(12/175\). Mahanta, Saikia, and Yaqubi (2020) give the foundational \(2^ap\) Zumkeller characterization, but do not establish the mixed-prime additive density improvement.

## Limitations
The result does not establish the natural density of \(\mathcal R\), prove the conjectural density-one assertion, or classify all exceptional integers. The rational number is **exact only for the constructed periodic certificate set**. The proof uses standard CRT and elementary lifting at fixed prime squares. Published and indexed source searches cannot exclude independently obtained or unindexed equivalent statements. No independent validation has been performed.

## References
1. S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (first posted 2023-10-22), revised as v2 on 2023-11-27, Proposition 4.11, Theorem 4.17, Conjecture 4.21, Lemma 2.1. https://arxiv.org/abs/2310.14149
2. P. J. Mahanta, M. P. Saikia, D. Yaqubi, *Some Properties of Zumkeller Numbers and \(k\)-Layered Numbers*, arXiv:2008.11096 (2020-08-07), Theorem 2.2; *Journal of Number Theory* 217 (2020), 218–236. https://arxiv.org/abs/2008.11096
3. Y. Peng, K. P. S. Bhaskara Rao, *On Zumkeller Numbers*, *Journal of Number Theory* 133 (2013), 1135–1155 (coprime multiplication principle as reproduced and independently proved here).
