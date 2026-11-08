# The complete dyadic value image and seven-twelfths density of Tribonacci numbers

## Finding
For the Tribonacci sequence \(T_0=0\), \(T_1=T_2=1\), \(T_{n+3}=T_{n+2}+T_{n+1}+T_n\), the closure of its values at nonnegative indices in the ring \(\mathbb Z_2\) is precisely
\[
\mathcal I=4\mathbb Z_2\;\sqcup\;(1+4\mathbb Z_2)\;\sqcup\;(2+16\mathbb Z_2)\;\sqcup\;(8\kappa-1+8\mathbb Z_2^2),
\]
where the symbol \(\sqcup\) denotes disjoint union. Define \(H(u)=(T_{8u+5}+1)/8\) initially for nonnegative integers \(u\), extend it as in the proof to all \(u\in\mathbb Z_2\), let \(\alpha\in\mathbb Z_2\) be its unique critical point, and set \(\kappa=H(\alpha)\). In particular \(\kappa\equiv1264\pmod{2048}\). The normalized additive Haar measure is
\[
\mu(\mathcal I)=\frac14+\frac14+\frac1{16}+\frac18\frac16=\boxed{\frac7{12}}.
\]
For every \(k\ge4\), the exact cardinality of the residue image is
\[
R(k)=\#\{T_n\bmod2^k:n\ge0\}=2^{k-1}+2^{k-4}+S(k-3),
\]
where \(S(m)=1+\sum_{j=0}^{\lfloor(m-1)/2\rfloor}s(m-2j)\), \(s(1)=s(2)=1\), and \(s(t)=2^{t-3}\) for \(t\ge3\). Equivalently, \(S(m)\) counts all squares modulo \(2^m\). For \(k=1,2,3\), the counts are respectively \(2,4,6\). The exact index period is \(2^{k+1}\) for every \(k\ge1\).

## Assumptions and scope
All indices are nonnegative integers, and the limiting ring is the standard \(2\)-adic ring with additive Haar measure normalized by \(\mu(\mathbb Z_2)=1\). The notation \(\mathbb Z_2^2\) means the **set of squares** \(\{u^2:u\in\mathbb Z_2\}\), not a Cartesian square. The closure, rather than the countable set of integer-index values itself, is classified. The number \(\kappa\) is an exact, uniquely specified \(2\)-adic constant and can be computed to arbitrary precision from the convergent series below.

## Proof
Let
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix},\quad
v=(0,1,1)^\mathsf T,\quad e=(1,0,0).
\]
Then \(T_n=eM^n v\). Direct integer matrix multiplication gives \(M^8=I+4D_3\), with
\[
D_3=\begin{pmatrix}3&5&6\\6&9&11\\11&17&20\end{pmatrix},
\]
and \(M^{32}=I+16D_5\) with
\[
D_5\equiv\begin{pmatrix}1&1&0\\0&1&1\\1&1&2\end{pmatrix}\pmod4.
\]
For \(s\ge3\), put \(D_s=(M^{2^s}-I)/2^{s-1}\). Squaring proves \(D_{s+1}=D_s+2^{s-2}D_s^2\). Thus \(D_s\equiv D_3\pmod2\) for \(s\ge3\), and \(D_s\equiv D_5\pmod4\) for \(s\ge5\). Evaluation of \(eM^n D_3v\) for \(0\le n<8\) gives residue \(1\pmod2\) for every even \(n\); evaluation of \(eM^nD_5v\) for \(n\equiv3,11\pmod{16}\) gives residue \(2\pmod4\). These residue calculations extend to every such index because \(M^4\equiv I\pmod2\) and \(M^{16}\equiv I\pmod4\).

For positive integers \(h\) with \(\nu_2(h)=s\ge3\), the factorization of \(M^h-I\) through \(M^{2^s}-I\) shows that the same leading congruence holds with its coefficient multiplied by an odd number. Hence, for every even \(n\),
\[
\nu_2(T_{n+h}-T_n)=s-1\quad(s\ge3),
\]
and for \(n\equiv3\pmod8\),
\[
\nu_2(T_{n+h}-T_n)=s\quad(s\ge5).
\]
The identities persist under \(2\)-adic interpolation of the index because \((M^8)^u=\sum_{j\ge0}\binom uj(M^8-I)^j\) converges uniformly for \(u\in\mathbb Z_2\). The first identity makes each of \(u\mapsto T_{8u}/4\) and \(u\mapsto(T_{8u+2}-1)/4\) an isometry of \(\mathbb Z_2\) onto itself. Their images supply precisely \(4\mathbb Z_2\) and \(1+4\mathbb Z_2\). The remaining even index classes have images inside these two balls.

Write \(J(u)=(T_{8u+3}-2)/16\). The binomial expansion and the displayed matrices give \(T_{8u+3}\equiv2\pmod{16}\). The second difference-valuation formula says that for \(u\equiv a\pmod4\), the map \(w\mapsto(J(a+4w)-J(a))/2\) is a \(2\)-adic isometry of \(\mathbb Z_2\) onto itself. Since \(J(0)=0\) and \(J(1)=17\), the two classes \(a=0,1\) yield respectively all even and all odd values of \(J\). Thus the class \(n\equiv3\pmod8\) has exact image \(2+16\mathbb Z_2\).

The class \(n\equiv1\pmod8\) is contained in \(1+4\mathbb Z_2\), and \(n\equiv7\pmod8\) is contained in \(4\mathbb Z_2\), by the recurrence modulo four. The only remaining branch is \(n\equiv5\pmod8\). Define the analytic \(2\)-adic function
\[
H(u)=\frac{T_{8u+5}+1}{8}=\sum_{j\ge0}c_j\binom uj,
\qquad c_j=\frac{eM^5(M^8-I)^jv}{8}\quad(j\ge1),\quad c_0=1.
\]
Direct computations give \(c_1=115\), \(c_2=14946\), \(\nu_2(c_3)=4\), and \(\nu_2(c_4)=7\). For \(j\ge5\), \(\nu_2(c_j)\ge2j-3\). Since \(\nu_2(j!)\le j-1\), every term with \(j\ge3\) has power-series coefficients divisible by eight, tending to zero \(2\)-adically. Consequently
\[
H(u)=7473u^2-7358u+1+8E(u),\qquad E\in\mathbb Z_2\langle u\rangle.
\]
Here \(\mathbb Z_2\langle u\rangle\) is the ring of restricted power series with integral coefficients. The derivative equation
\[
H'(u)/2=7473u-3679+4E'(u)=0
\]
has exactly one solution \(\alpha\in\mathbb Z_2\), since the equivalent fixed-point map is a strict contraction (Lipschitz factor at most \(1/4\)). Taylor expansion at this root gives
\[
H(u)-H(\alpha)=(u-\alpha)^2\bigl(7473+8Q(u)\bigr),\qquad Q\in\mathbb Z_2\langle u\rangle.
\]
The parenthetical unit is \(1\pmod8\) and therefore has a square root \(b(u)\equiv1\pmod4\). Its variation satisfies \(\nu_2(b(u)-b(w))\ge2+\nu_2(u-w)\). It follows that \(u\mapsto(u-\alpha)b(u)\) is a \(2\)-adic isometry onto \(\mathbb Z_2\), proving the exact branch identity \(H(\mathbb Z_2)=\kappa+\mathbb Z_2^2\), with \(\kappa=H(\alpha)\). Therefore the final branch is precisely \(8\kappa-1+8\mathbb Z_2^2\). All four components are pairwise disjoint by their residues modulo four.

The unit squares in \(\mathbb Z_2\) are exactly \(1+8\mathbb Z_2\). Separating even valuations shows that squares have Haar measure \(\sum_{j\ge0}2^{-2j}/8=1/6\) and gives the stated formula for \(S(m)\). Disjointness yields the measure \(7/12\) and exact finite image counts. Finally, \(\det[v,Mv,M^2v]=-1\), so the index period equals the matrix order. The matrices \(D_s\) show that this order modulo \(2^k\) is exactly \(2^{k+1}\) (including \(k=1\) by direct check).

## Verification
The accompanying standalone `verify_tribonacci_dyadic.py` independently constructs the recurrence, performs integral matrix calculations for the critical congruences, derives the polynomial form of \(H\), computes \(\kappa\pmod{2^{11}}\) by derivative-root lifting, and compares the complete predicted image with direct enumeration for all exponents \(1\le k\le14\). It reports 32,766 checked target residue fibers. These finite computations support the proof but do not constitute the infinite proof.

## Relationship to prior work
Marques and Lengyel (2014) prove the exact \(2\)-adic **valuation** formula for Tribonacci numbers; their Theorem 1 is not an image or target-residue classification. Bilu, Luca, Nieuwveld, Ouaknine and Worrell (2022 preprint) study \(p\)-adic **zeros** and related valuation formulas; their primary analytic interpolation treatment explicitly excludes the prime two. The present statement concerns all **values**, including odd targets, their complete image and its measure. OEIS A248174 records the valuation sequence, not the target-image cardinalities. General existence of analytic interpolation is not sufficient to imply this four-component image without the critical-point and matrix analysis above.

## Limitations
Only the classical third-order recurrence and the prime two are covered. The theorem does not give a formula for the multiplicity of every individual residue within the period, nor does it settle any analogous question for general odd primes or arbitrary third-order recurrences. Historical-priority comparison is limited to the listed accessible sources and the checked research index; an unlocated exact image theorem remains possible. No independent mathematical audit has been performed.

## References
1. D. Marques and T. Lengyel, *The 2-adic Order of the Tribonacci Numbers and the Equation \(T_n=m!\)*, Journal of Integer Sequences 17 (2014), Article 14.10.1, first online publication 2014-10-03, https://cs.uwaterloo.ca/journals/JIS/VOL17/Lengyel/lengyel21.html (full text PDF linked there).
2. Y. Bilu, F. Luca, J. Nieuwveld, J. Ouaknine and J. Worrell, *On the p-adic zeros of the Tribonacci sequence*, arXiv:2210.16959 (first posted 2022-10-30), https://arxiv.org/abs/2210.16959.
3. OEIS A248174, *2-adic order of the tribonacci sequence*, https://oeis.org/A248174.
