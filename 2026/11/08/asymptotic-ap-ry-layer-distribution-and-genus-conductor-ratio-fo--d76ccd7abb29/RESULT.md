# Asymptotic Apéry-layer distribution and genus–conductor ratio for shifted-square semigroups

## Finding
For each integer \(a\ge3\), consider the numerical semigroup
\[
 S_a=\langle a,\,a+1^2,\,a+2^2,\,a+3^2,\ldots\rangle.
\]
For \(1\le r<a\), let \(w_{a,r}\) be the least nonnegative element of \(S_a\) congruent to \(r\pmod a\), and set \(h_{a,r}=(w_{a,r}-r)/a\). Define \(H_j(a)=\#\{1\le r<a:h_{a,r}=j\}\). Uniformly as \(a\to\infty\),
\[
\begin{aligned}
 H_4(a)&=\frac a6+O\!\left(\frac a{\sqrt{\log a}}\right),\\
 H_3(a)&=\frac{5a}6+O\!\left(\frac a{\sqrt{\log a}}\right),\\
 H_1(a)+H_2(a)&=O\!\left(\frac a{\sqrt{\log a}}\right).
\end{aligned}
\]
No other positive Apéry layers occur. In particular the number \(g(S_a)\) of nonnegative integers outside \(S_a\) (the genus) and the conductor \(c(S_a)=1+\max(\mathbb N_0\setminus S_a)\) satisfy
\[
\boxed{g(S_a)=\frac{19}{6}a+O\!\left(\frac a{\sqrt{\log a}}\right),\qquad
c(S_a)=4a+O\!\left(\frac a{\sqrt{\log a}}\right).}
\]
Thus
\[
 \boxed{\frac{g(S_a)}{c(S_a)}=\frac{19}{24}+O\!\left(\frac1{\sqrt{\log a}}\right).}
\]
All constants implicit in the error terms are absolute.

## Assumptions and scope
The generators have coefficient \(1\) on each positive square and include \(a\) itself. Since \(a\) and \(a+1\) are coprime, the complement of \(S_a\) in \(\mathbb N_0\) is finite. Let \(\iota(n)\) denote the least number of **positive** integer squares with sum \(n\), for each integer \(n\ge1\). Let \(\mathcal E=\{4^v(8u+7):u,v\in\mathbb N_0\}\), and let \(\mathcal Q\) denote positive integers representable as the sum of two nonnegative squares. The latter includes ordinary squares. The theorem concerns the limit through every positive integer \(a\), not only a congruence class; no statement about exact finite-\(a\) layer frequencies is implied by the asymptotics.

## Proof
**1. Exact Apéry heights.** Liu and Xin's Lemma 2.7 (reference [1]) yields
\[
 w_{a,r}=r+a\min_{m\ge0}\bigl(m+\iota(ma+r)\bigr).
\]
Lagrange's four-square theorem ensures \(\iota(r)\le4\). For \(m\ge3\), positivity of \(\iota(ma+r)\) implies \(m+\iota(ma+r)\ge4\). It follows, for *every* \(a\ge3\) and \(1\le r<a\), that
\[
 h_{a,r}=\min\{\iota(r),\;1+\iota(a+r),\;2+\iota(2a+r)\}.
 \tag{1}
\]
In particular, \(1\le h_{a,r}\le4\).

**2. A density-one structural description.** Legendre's three-square theorem and Lagrange's theorem imply \(\iota(n)=4\) precisely for \(n\in\mathcal E\); for \(n\notin\mathcal E\cup\mathcal Q\) one has \(\iota(n)=3\). The Landau–Ramanujan theorem gives, for all real \(x\ge3\),
\[
 \#(\mathcal Q\cap[1,x])\ll\frac{x}{\sqrt{\log x}}.
 \tag{2}
\]
Define the exceptional set
\[
 \mathcal B_a=\{1\le r<a:r\in\mathcal Q\text{ or }a+r\in\mathcal Q\text{ or }2a+r\text{ is a square}\}.
\]
By (2), applied at \(x=a\) and \(x=2a\), and by the elementary bound on the number of squares below \(3a\),
\[
 |\mathcal B_a|\ll a/\sqrt{\log a}. \tag{3}
\]
For any \(r\notin\mathcal B_a\), \(\iota(a+r)\ge3\), \(\iota(2a+r)\ge2\), and \(\iota(r)\) equals either \(3\) or \(4\) according as \(r\notin\mathcal E\) or \(r\in\mathcal E\). Equation (1) therefore gives the **exact** identity outside \(\mathcal B_a\):
\[
 h_{a,r}=3+\mathbf1_{\mathcal E}(r). \tag{4}
\]

**3. Frequency and genus.** Every positive integer in \(\mathcal E\) has a unique representation \(4^v(8u+7)\), because the factor \(8u+7\) is odd. For any \(x\ge2\), summing the counts in the residue class \(7\pmod8\) over \(v\le\log_4 x\) yields
\[
 \#(\mathcal E\cap[1,x])=\sum_{v\ge0}\left(\frac{x}{8\cdot4^v}+O(1)\right)
 =\frac x6+O(\log(2+x)). \tag{5}
\]
The same count in any interval \([u,v)\subset[1,x]\) equals \((v-u)/6+O(\log(2+x))\), by subtraction. Equations (3)–(5) give the three claimed layer-count estimates. For each \(r\), the missing integers in residue \(r\pmod a\) are exactly \(r,r+a,\ldots,r+(h_{a,r}-1)a\). Hence
\[
 g(S_a)=\sum_{r=1}^{a-1}h_{a,r}=
3(a-1)+\#(\mathcal E\cap[1,a))+O(|\mathcal B_a|)
=\frac{19}{6}a+O\!\left(\frac a{\sqrt{\log a}}\right).
\]

**4. Conductor, with a quantitative error.** The Apéry characterization gives
\[
 F(S_a)=\max_{1\le r<a} w_{a,r}-a
 =\max_{1\le r<a}\bigl((h_{a,r}-1)a+r\bigr)\le4a-1,
\]
where \(F(S_a)=c(S_a)-1\). The absolute implied constant in (3) allows a fixed \(K>0\) such that, for all sufficiently large \(a\),
\[
 |\mathcal B_a|\le K a/\sqrt{\log a}.
\]
Choose a fixed \(L>6K\), and consider the final interval of residue classes of length \(L a/\sqrt{\log a}\) immediately below \(a\). By (5) this interval contains
\[
 \frac{L a}{6\sqrt{\log a}}+O(\log a)>|\mathcal B_a|
\]
points of \(\mathcal E\) for all sufficiently large \(a\). At least one of them, say \(r\), therefore lies outside \(\mathcal B_a\), where (4) forces \(h_{a,r}=4\). Consequently
\[
 4a-O\!\left(\frac a{\sqrt{\log a}}\right)
 \le c(S_a)\le4a.
\]
Combining with the genus estimate and dividing by \(c(S_a)\asymp a\) proves the stated ratio estimate. \(\square\)

## Verification
A standard-library Python program `artifacts/verify.py` independently obtains the Apéry representatives by Dijkstra shortest paths modulo \(a\) and the least square counts by dynamic programming. It exhaustively compares (1), the structural rule (4) outside the explicitly defined exceptional set, and the exact genus formula for \(111\) values \(3\le a\le2000\), checking \(12{,}875\) nonzero residue classes in total. It does **not** verify the infinite asymptotic estimates; those depend on the full proof and the classical Landau–Ramanujan theorem.

## Relationship to prior work
Liu and Xin [1], Section 2, introduced the least-square-summand function and obtained the exact Apéry minimization formula as part of their Frobenius-number work. Equation (1) is explicitly credited as a reduction of their result and the four-square theorem, not claimed as new. Their inspected article does not establish the limiting distribution of the Apéry layers, the resulting genus asymptotic, or the genus-to-conductor constant \(19/24\). The density analysis here combines Legendre's exceptional class, the Landau–Ramanujan upper bound [2,3], and a uniform translated exceptional-set estimate. Song [4] studies Frobenius numbers of the same shifted-square family; the accessible abstract alone does not establish or refute the genus-layer assertion. The complete later full text could not be inspected, and potentially equivalent results remain a priority risk. Finite shifted-square triples such as \(\langle a,a+1,a+4\rangle\) are different semigroups from the infinite-generator family here.

## Limitations
This is a first-order distribution law with an error of order \(a/\sqrt{\log a}\), not an exact genus formula for any given \(a\), and no sharp second-order constant or effective numerical threshold is asserted. The proof imports established four-square, three-square, and Landau–Ramanujan results; the independent mathematical validation status is not established. The full text of the later related 2026 Frobenius paper was inaccessible, so the bibliographic comparison cannot rule out an unpublished or unindexed equivalent analysis. A complete Apéry formula in prior work gives exact finite computational information, whereas the new assertion addresses uniform asymptotic counts; this distinction is central to the originality assessment.

## References
[1] F. Liu and G. Xin, *On Frobenius Formulas of Power Sequences*, arXiv:2210.02722 (first posted 6 October 2022), Section 2, especially Lemma 2.7 and Theorem 2.6. Full text: https://arxiv.org/html/2210.02722v3.

[2] E. Landau, *Über die Einteilung der positiven ganzen Zahlen in vier Klassen nach der Mindestzahl der zu ihrer additiven Zusammensetzung erforderlichen Quadrate*, Archiv der Mathematik und Physik **13** (1908), 305–312.

[3] E. Bank, L. Bary-Soroker, and A. Fehm, *Sums of two squares in short intervals in polynomial rings over finite fields*, arXiv:1509.02013 (2015), introduction recalling Landau's classical integer density theorem.

[4] K. Song, *The Frobenius problem for shifted square sequences*, arXiv:2605.25542 (first posted 25 May 2026; later version dated July 2026). The accessible abstract addresses Frobenius numbers; complete later full text not inspected.
