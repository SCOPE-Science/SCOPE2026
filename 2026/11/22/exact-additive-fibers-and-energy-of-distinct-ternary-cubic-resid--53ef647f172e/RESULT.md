# Exact additive fibers and energy of distinct ternary cubic residues

## Finding

For every integer \(k\ge0\), let \(C_k=\{x^3\bmod 3^k:x\in\mathbb Z/3^k\mathbb Z\}\), a **set of distinct cube values**, not a multiset of input cubes. For the one-element ring, \(C_0=\{0\}\). Write \(s_k=|C_k|\), and for each residue \(y\bmod3^k\) count ordered value pairs by
\[
r_k(y)=\#\{(a,b)\in C_k^2:a+b\equiv y\pmod{3^k}\}.
\]
The initial fibers are \(r_0(0)=1\); \(r_1(y)=3\) for every residue modulo three; and modulo nine \(r_2(0)=3\), \(r_2(\pm1)=2\), \(r_2(\pm2)=1\), with all other fibers zero.

For every \(k\ge3\), put \(h_k=3^{k-2}\) and \(s=s_{k-3}\). Then **every target fiber** obeys the exact recursion
\[
\boxed{r_k(y)=\begin{cases}
h_k,&y\equiv 2,-2\pmod9,\\
2s,&y\equiv1,-1\pmod9,\\
2h_k+\mathbf1_{27\mid y}\,r_{k-3}(y/27),&y\equiv0\pmod9,\\
0,&y\equiv3,4,5,6\pmod9.
\end{cases}}
\]
In the third line, the quotient \(y/27\) is evaluated modulo \(3^{k-3}\) only when \(27\mid y\), and the indicator is zero otherwise. The cube-value cardinality, previously studied in its own right, is
\[
s_k=\frac{3^{k+1}+c_{k\bmod3}}{13},\qquad(c_0,c_1,c_2)=(10,30,12).
\]

The principal exact additive invariant is the ordered **distinct-value additive energy**
\[
E_k=\#\{(a,b,c,d)\in C_k^4:a+b\equiv c+d\pmod{3^k}\}=\sum_{y\bmod3^k}r_k(y)^2.
\]
It has initial values \((E_0,E_1,E_2)=(1,27,19)\) and the all-depth three-step recurrence
\[
\boxed{E_k=E_{k-3}+6\cdot 3^{3k-6}+12\cdot3^{k-2}s_{k-3}^{2}\quad(k\ge3).}
\]
In particular, the exact limiting collision concentration is
\[
\boxed{\lim_{k\to\infty}\frac{E_k}{3^{3k}}=\frac{13851}{1663129},\qquad
\lim_{k\to\infty}\frac{3^kE_k}{s_k^4}=\frac{2223}{757}.}
\]
The second constant is the limiting additive-energy amplification relative to the minimum \(s_k^4/3^k\) allowed by Cauchy--Schwarz for the same set size. The sumset-support criterion modulo nine is elementary and already follows from known cube-congruence work; it is not claimed separately as new.

## Assumptions and scope

For each modulus, a residue occurring as the cube of multiple inputs is included **once** in \(C_k\). The ordered pair \((a,b)\) is distinguished from \((b,a)\) unless the values coincide. There are no positivity, primitiveness, or nonzero-unit restrictions. All claims are exact for every integer \(k\ge0\); the limits are taken through all integer depths. The energy is a property of the cube **image set**. In contrast, counting the input solutions \((x,y)\) to \(x^3+y^3\equiv z\) gives different weighted fibers and different energy values.

## Proof

**1. Exact cube-value decomposition.** For \(k\ge3\), the unit group modulo \(3^k\) is cyclic of order \(2\cdot3^{k-1}\). Its cubing homomorphism has kernel of size three; its image consists exactly of the \(2\cdot3^{k-2}\) residues congruent to \(1\) or \(-1\) modulo nine, with \(h_k=3^{k-2}\) values of each sign. Every nonunit input is \(3z\), whose cube is \(27z^3\); as a **distinct value**, this ranges exactly over the embedded set \(27C_{k-3}\). Since the three parts have different classes modulo nine,
\[
C_k=(1+9\mathbb Z/3^k\mathbb Z)\ \dot\cup\ (-1+9\mathbb Z/3^k\mathbb Z)\ \dot\cup\ 27C_{k-3},
\quad s_k=2h_k+s_{k-3}.
\]
From \(s_0=1\), \(s_1=3\), \(s_2=3\), the last recurrence yields the displayed three-periodic closed formula for \(s_k\). This cardinality law is cited as prior knowledge.

**2. The complete pair-sum fibers.** Distinguish the types of both value summands. Two unit values of the same sign sum to a target congruent to \(2\) or \(-2\) modulo nine, and every such target has exactly \(h_k\) ordered representations: any value of the first unit coset uniquely fixes the second. Opposite-sign unit values sum to a target congruent to zero modulo nine and contribute exactly \(2h_k\) ordered representations, independent of the higher digits. If one summand is a cube value from \(27C_{k-3}\) and the other a unit value, the target is congruent to \(1\) or \(-1\) modulo nine. For each of the \(s_{k-3}\) nonunit values, the other summand is uniquely prescribed in the appropriate unit coset; the two orientations contribute \(2s_{k-3}\). Finally, two summands from \(27C_{k-3}\) have sum divisible by \(27\), and dividing by \(27\) gives exactly \(r_{k-3}(y/27)\) ordered value pairs. Every possible type is included, so their disjoint contributions give the displayed complete fiber recurrence.

**3. Energy identity.** The target classes \(\pm2,\pm1,0\pmod9\) each contain \(h_k\) residues modulo \(3^k\). The two \(\pm2\)-classes contribute \(2h_k^3\) to \(E_k\). The two \(\pm1\)-classes contribute \(8h_ks_{k-3}^2\). For the zero class, square the expression \(2h_k+\mathbf1_{27\mid y}r_{k-3}(y/27)\) and sum. Its constant term is \(4h_k^3\), its cross term is \(4h_k\sum_z r_{k-3}(z)=4h_ks_{k-3}^2\), and its final term is \(E_{k-3}\). Summing the three disjoint strata proves
\[
E_k=E_{k-3}+6h_k^3+12h_ks_{k-3}^2.
\]
Direct enumeration of the one-element ring, the full set modulo three, and \(\{0,1,-1\}\) modulo nine gives respectively \(E_0=1\), \(E_1=27\), and \(E_2=19\).

**4. Exact asymptotic constants.** Write \(c=c_{k\bmod3}\). Since \(s_{k-3}=(3^{k-2}+c)/13\), expansion of the recurrence gives
\[
E_k-E_{k-3}=\frac{38}{4563}27^k+\frac{8c}{4563}9^k+\frac{4c^2}{507}3^k.
\]
The bounded periodic parameter \(c\) makes the last two terms negligible after division by \(27^k\). Since the recurrence advances by three, each of its three subsequences has the **same** limiting quotient
\[
\frac{38/4563}{1-27^{-3}}=\frac{13851}{1663129}.
\]
Also \(s_k/3^k\to3/13\). Dividing the energy quotient by the fourth power of that cardinality ratio gives
\[
\frac{13851}{1663129}\left(\frac{13}{3}\right)^4=\frac{2223}{757}.
\]
This establishes the two limits and completes the proof.

## Verification

The standalone `verify.py` uses only Python's standard library. Independently of the displayed fiber recursion, it constructs cube **sets** by enumerating input cubes, then explicitly enumerates all ordered pairs of distinct cube values and tabulates every sum target modulo \(3^k\) for \(0\le k\le8\). It checks all 9828 target fibers at levels three through eight, all corresponding energy and cardinality identities, and exact rational values of both limiting constants. It additionally checks the integer recurrence through depth fifteen. Run `python3 verify.py` and expect `CUBIC_VALUE_FIBERS_PASS`. A finite enumeration alone does not establish any all-depth assertion; the infinite proof is in Steps 1--4.

## Relationship to prior work

Finch and Sebah study the set of cubes modulo general integers and give the prime-power **cardinality** formula quoted above (in particular, their Section 1.9 treats the case of powers of three). That formula does not encode the additive pair-sum fibers or the additive energy.

Schipani and Elia determine additive decompositions of multiplicative-character cosets over **finite fields**, which is a different ring and does not encompass the nested nonunit cube-value strata of \(\mathbb Z/3^k\mathbb Z\) for \(k\ge3\).

Published results entitled *Exact ternary fibre law and collision moments for two cubes* and *Exact representation counts for two cubes modulo powers of three* determine the number of **input pairs** satisfying \(x^3+y^3\equiv y_0\pmod{3^k}\), hence weight each distinct cube value according to its number of cube roots. That is not the unweighted \(r_k\) above: root multiplicities depend on valuation. Their exact formulas do not directly state the distinct-value energy recurrence or its limiting concentration constant. The related published *Complete pair-sum fibers of the cubic graph over odd residue rings* works with graph points \(x,x^3\) in a two-dimensional additive ring. Its summing over the first coordinate recovers **input-weighted**, not distinct-value, cubic-sum fibers; its two-dimensional energy counts a different equality relation. Root-weighted congruence support is an earlier result, not an original contribution here. The known count formula and weighted fiber machinery might allow a longer derivation of the present results; an unindexed equivalent or general theorem is a priority risk, not ruled out by searches.

## Limitations

The results concern cube-image sets over powers of three, not primitive cube values alone, other primes, input-weighted cube sums, or integer solutions to equations over the positive integers. The limit measures normalized additive energy, not independent randomness or a theorem about global Waring representations. The main new components are the precise **distinct-value** fibers, their all-depth energy recurrence, and the evaluated rational concentration constant; mere cube-set cardinalities and support modulo nine are prior elementary knowledge. Searches and comparison of accessible material do not establish exhaustive historical priority. No independent mathematical review has been conducted.

## References

1. Steven R. Finch and Pascal Sebah, *Squares and Cubes Modulo n*, arXiv:math/0604465, first posted 21 April 2006; Section 1.9, https://arxiv.org/html/math/0604465v3 .
2. Davide Schipani and Michele Elia, *Additive decompositions induced by multiplicative characters over finite fields*, arXiv:1107.1364, first posted 7 July 2011, https://arxiv.org/abs/1107.1364 .
3. *Exact ternary fibre law and collision moments for two cubes*, publicly available mathematical result dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-ternary-fibre-law-and-collision-moments-for-two-cubes--876b3ebf3861 .
4. *Exact representation counts for two cubes modulo powers of three*, publicly available mathematical result dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-representation-counts-for-two-cubes-modulo-powers-of-three--dd802b0bb880 .
5. *Complete pair-sum fibers of the cubic graph over odd residue rings*, publicly available mathematical result dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-pair-sum-fibers-of-the-cubic-graph-over-odd-residue-rin--1bbc7ea862f6 .
