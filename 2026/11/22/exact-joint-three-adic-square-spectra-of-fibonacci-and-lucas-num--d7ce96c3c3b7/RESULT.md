# Exact joint three-adic square spectra of Fibonacci and Lucas numbers

## Finding

Let \(F_0=0\), \(F_1=1\), \(L_0=2\), \(L_1=1\), and let both sequences satisfy \(X_{n+2}=X_{n+1}+X_n\). For \(k\ge1\) put \(q_k=3^k\) and \(P_k=8\cdot3^{k-1}\). A residue is called a square modulo \(q_k\) if it is congruent to the square of an integer, including zero. Define \(N_k(a,b)\) for \(a,b\in\{0,1\}\) as the number of indices \(0\le n<P_k\) for which the indicators of \(F_n\) and \(L_n\) being squares modulo \(q_k\) are \(a\) and \(b\), respectively.

Set \(T_k=3^{k-1}\), \(B_1=1\), and for \(k\ge2\) put
\[
B_k=S_{k-2},\qquad S_0=1,\qquad
S_m=1+\sum_{j=0}^{\lfloor(m-1)/2\rfloor}3^{m-2j-1}\quad(m\ge1).
\]
Then **all four counts at every precision** are
\[
\boxed{N_k(1,1)=T_k+2B_k,\quad N_k(1,0)=N_k(0,1)=2T_k,\quad N_k(0,0)=3T_k-2B_k.}
\]
In particular, the corresponding limiting densities for simultaneous square membership in \(\mathbb Z_3\) are
\[
\boxed{(d_{11},d_{10},d_{01},d_{00})=(5/32,1/4,1/4,11/32).}
\]
Each marginal square probability equals \(13/32\); the two square indicators have covariance \(-9/1024\), so they are not independent. For each pair \((a,b)\) the number of indices below an arbitrary cutoff \(N\) having the indicated **three-adic** square membership is
\[
\boxed{d_{ab}N+O(\log(2N))}\qquad(N\ge1),
\]
where the implied constant is absolute. This claim concerns local squares, not simultaneous integer squares.

## Assumptions and scope

The prime is exactly \(3\). A three-adic square means an element of \((\mathbb Z_3)^2\), not merely a square at one finite precision. Every nonzero unit of \(\mathbb Z_3\) is a square if and only if it is \(1\pmod3\), and every nonzero three-adic integer is a square exactly when its valuation is even and its unit part is \(1\pmod3\). Finite square status at precision \(k\) includes the residue zero; its indicator need not coincide with infinite three-adic square status at an individual index.

The common pair period modulo \(3^k\) is \(P_k\). All finite formulas are for full half-open periods \(0\le n<P_k\); the density and discrepancy statement concerns all nonnegative integers. The sequences and the square condition are not shifted or renormalized.

## Proof

**1. Period and base-three branches.** Put
\[
M=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
M^8=I+3A,\quad A=\begin{pmatrix}11&7\\7&4\end{pmatrix}.
\]
Here \(F_n\) is the upper-right entry of \(M^n\), and \(L_n=\operatorname{tr}(M^n)\). Since \(M^4\equiv-I\pmod3\), the order modulo \(3\) is eight. Moreover, \(A\not\equiv0\pmod3\), and the binomial expansion gives \(v_3((I+3A)^{3^r}-I)=r+1\), where matrix valuation is the minimum valuation of its entries. Thus the exact common period is \(P_k=8\cdot3^{k-1}\).

For \(j=0,1,\ldots,7\), the ordered pairs \((F_j,L_j)\pmod3\) are
\[
(0,2),(1,1),(1,0),(2,1),(0,1),(2,2),(2,0),(1,2).
\]
These pairs persist for every index \(n=j+8t\). Only \(j=1\) has both entries congruent to \(1\), and hence both permanently square. Precisely \(j=2,4\) can contribute additional simultaneous squares, through a single coordinate divisible by three. For marginal squares, the nonsingular branches are \(j=1,2,7\) for Fibonacci and \(j=1,3,4\) for Lucas; the singular branches are \(j=0,4\) for Fibonacci and \(j=2,6\) for Lucas.

**2. Four exact isometries.** For \(j\in\{0,4\}\) define \(f_j(t)=F_{j+8t}/3\); for \(j\in\{2,6\}\) define \(\ell_j(t)=L_{j+8t}/3\). Each is integer-valued for \(t\ge0\). For \(d\ge1\), the binomial theorem and the inequality \(v_3\binom dm\ge v_3(d)-v_3(m)\) yield
\[
(I+3A)^d-I=3dA+R_d,
\quad v_3(R_d)\ge v_3(d)+2,
\]
because \(m-v_3(m)\ge2\) for all \(m\ge2\). The relevant entries of \(M^jA\) are units modulo three:
\[
(M^0A)_{12}\equiv1,\quad (M^4A)_{12}\equiv2,\quad
\operatorname{tr}(M^2A)\equiv1,\quad \operatorname{tr}(M^6A)\equiv2\pmod3.
\]
Since \((I+3A)^u\equiv I\pmod3\), subtraction at \(t>u\ge0\) gives, for each of the four normalized functions \(g\),
\[
v_3(g(t)-g(u))=v_3(t-u).
\]
Therefore each \(g\) induces a bijection modulo \(3^h\) for every \(h\ge1\) and extends to an isometric bijection \(\mathbb Z_3\to\mathbb Z_3\). No assertion about other branches is needed.

**3. Counting finite-precision square classes.** The count \(S_m\) is the number of distinct squares modulo \(3^m\): besides zero, a square of valuation \(2j<m\) is \(3^{2j}\) times a unit square modulo \(3^{m-2j}\), of which there are \(3^{m-2j-1}\). For \(k\ge2\), if a coordinate is \(3g(t)\), its being a square modulo \(3^k\) is equivalent to
\[
g(t)\equiv3s\pmod{3^{k-1}}\qquad(s\in (\mathbb Z/3^{k-2}\mathbb Z)^2).
\]
The normalized isometry makes the number of such \(t\pmod{3^{k-1}}\) exactly \(S_{k-2}=B_k\). At \(k=1\), zero is a square residue and each singular branch contributes \(B_1=1\). Every one of the eight branches has \(T_k\) indices in a period. From the branch list, the joint square count is \(T_k+2B_k\); each marginal count is \(3T_k+2B_k\). Subtraction gives the four displayed entries. The four counts add to \(8T_k\), providing a separate normalization check.

**4. Three-adic densities and arbitrary cutoffs.** For an isometric \(g:\mathbb Z_3\to\mathbb Z_3\), the event \(3g(t)\in(\mathbb Z_3)^2\) is the disjoint union, apart from the zero point, of the single residue cylinders
\[
g(t)\equiv3^{2h+1}\pmod{3^{2h+2}},\qquad h=0,1,2,\ldots.
\]
Its measure is \(\sum_{h\ge0}3^{-2h-2}=1/8\). In a prefix of length \(X\), cylinders with modulus at most \(X\) contribute total discrepancy \(O(\log(2X))\) from their measures. All deeper cylinders lie in one ball around the unique zero of \(g\), whose modulus can be chosen greater than \(X\); thus they contain at most one index in the prefix. The zero itself contributes at most one. This gives the same logarithmic error for every singular branch. The nonsingular branches are complete arithmetic progressions modulo eight, with \(O(1)\) discrepancy.

Consequently the simultaneous density is \((1+2/8)/8=5/32\), and each marginal density is \((3+2/8)/8=13/32\). The other two joint frequencies are obtained by subtraction, and the covariance is
\[
5/32-(13/32)^2=-9/1024.
\]
The logarithmic error follows simultaneously for all four patterns.

## Verification

The standalone program `verify.py` independently generates Fibonacci and Lucas terms modulo \(3^k\) and enumerates all four square-status patterns for every \(1\le k\le9\), including a complete period check. It verifies the square-residue counting formula for \(0\le m\le8\), and it directly compares the valuation of differences on the four singular normalized branches in 4,644 tests. The observed counts for simultaneous finite-precision squares at \(k=1,2,3,4,5,6,7,8,9\) are respectively \(3,5,13,35,103,305,913,2735,8203\), agreeing with the theorem. Run `python3 verify.py` in the package directory. This is independent finite diagnostic verification; it is not a computer proof of the infinite density, which is established in the preceding argument.

## Relationship to prior work

Bundschuh and Bundschuh (2011) give complete **single-sequence** residue-frequency functions for Fibonacci and Lucas numbers modulo powers of three (Theorems 1.1 and 1.2, pages 202 and 209), including their marginal exceptional fibers and a shift/scaling relationship. Those functions do not determine the aligned, two-coordinate square-status table because they discard the common index. Southwick (2014, arXiv first version February 4) establishes residue completeness of Gibonacci sequences modulo powers of three, a weaker kind of information than the present joint index distribution. Bragman and Rowland (2022 preprint, 2025 journal) analyze the proportion of **output residues** attained by Fibonacci numbers, a distinct statistic from proportions of input indices with two simultaneous local-square properties. Bugeaud, Mignotte and Siksek (2006) classify **integer** perfect powers, a global Diophantine question that does not imply the local-square density.

The novelty claimed here is only the evaluated full aligned joint square spectrum at every three-power precision, with its limiting three-adic correlation and counting error, not the underlying recurrence, period, or marginal residue-frequency theorems.

## Limitations

The result is specialized to the prime three and the classical Fibonacci/Lucas pair. It does not classify integer square indices, nor establish a comparable joint law at other primes. Previously known single-sequence congruences and the period are prerequisites, not new discoveries. A logically equivalent theorem in an older, unindexed treatment of simultaneous local quadratic characters remains a residual historical-priority risk; a negative database search alone does not establish priority. The numerical verification covers finite levels and cannot replace the general argument. Independent mathematical audit has not been performed.

## References

1. Jeremiah T. Southwick, *The Lucas Numbers and Other Gibonacci Sequences Mod \(m\)*, arXiv:1402.0598, version 1 first publicly posted February 4, 2014. https://arxiv.org/abs/1402.0598
2. Ralf Bundschuh and Peter Bundschuh, *Distribution of Fibonacci and Lucas Numbers Modulo \(3^k\)*, Fibonacci Quarterly 49(3) (August 2011), 201–210. https://fq.math.ca/Papers1/49-3/Bundschuh2.pdf
3. Yann Bugeaud, Maurice Mignotte and Samir Siksek, *Classical and modular approaches to exponential Diophantine equations I. Fibonacci and Lucas perfect powers*, Annals of Mathematics 163 (2006), 969–1018. https://annals.math.princeton.edu/2006/163-3/p05
4. Nicholas Bragman and Eric Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, arXiv:2202.00704 (2022), Research in Number Theory 11 (2025), article 88. https://arxiv.org/abs/2202.00704
