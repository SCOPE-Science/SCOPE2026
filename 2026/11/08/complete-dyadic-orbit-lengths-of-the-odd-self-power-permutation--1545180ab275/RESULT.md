# Complete dyadic orbit lengths of the odd self-power permutation

## Finding
For every integer \(k\ge 1\), the self-power function \(F_k(x)=x^x\pmod{2^k}\) is a permutation of the odd residue classes modulo \(2^k\). Its *least positive orbit period* \(L_k(x)\) is determined exactly as follows. For \(k=1\), the unique odd residue is fixed. For \(k\ge2\), the residues \(x\equiv1\) and \(x\equiv-1\pmod{2^k}\) are fixed; for every other odd residue, take the uniquely determined integer \(2\le r<k\) with the indicated valuation.

If \(x\equiv1\pmod4\) and \(r=\nu_2(x-1)\), then
\[
L_k(x)=2^{\max(0,k-2r)}.
\]
If \(x\equiv-1\pmod4\) and \(r=\nu_2(x+1)\), then
\[
L_k(x)=\begin{cases}
1,&k\le r+1,\\
2^{\max(1,k-3r+1)},&k>r+1.
\end{cases}
\]
All valuations are taken of any integer representative and are unambiguous when \(r<k\). These formulas give a complete cycle census. Specifically, for \(k\ge2\) put
\[
A_{k,r}=2^{k-r-1},\quad P_{k,r}=2^{\max(0,k-2r)},\quad
Q_{k,r}=\begin{cases}1,&k\le r+1,\\2^{\max(1,k-3r+1)},&k>r+1.\end{cases}
\]
The number \(C_k(\ell)\) of distinct cycles of length \(\ell\) is
\[
C_k(\ell)=2\mathbf1_{\ell=1}
+\sum_{r=2}^{k-1}A_{k,r}\left(
\frac{\mathbf1_{\ell=P_{k,r}}}{P_{k,r}}+
\frac{\mathbf1_{\ell=Q_{k,r}}}{Q_{k,r}}\right).
\]
Here \(C_1(1)=1\) and all other \(C_1(\ell)=0\). In particular, for \(k\ge3\), the number of fixed points is \(2^{\lfloor k/2\rfloor}+2\). For every \(k\ge6\), the maximum period is \(2^{k-4}\), attained by exactly **two cycles**.

## Assumptions and scope
The domain is the multiplicative unit set \((\mathbb Z/2^k\mathbb Z)^\times\), equivalently all odd classes. The exponent is the same odd integer representative as the base, interpreted by ordinary modular exponentiation; the proof establishes that the resulting residue depends only on the class. This is not a statement about even inputs, about other prime powers, or about general functions \(x\mapsto x^{x^n}\). We use \(\nu_2(0)=+\infty\) and the standard 2-adic logarithm and exponential on \(1+4\mathbb Z_2\) and \(4\mathbb Z_2\), respectively.

## Proof
**1. Interpolation and a sharp isometry.** For odd \(z\in\mathbb Z_2\), let \(\sigma\in\{1,-1\}\) be the unique sign such that \(z\equiv\sigma\pmod4\), and write \(u=\sigma z\in1+4\mathbb Z_2\). Define
\[
F(z)=\sigma\exp\bigl(z\log(\sigma z)\bigr)=\sigma u^z.
\]
For a positive odd integer \(z\), this equals its ordinary self-power \(z^z\). Now fix \(x\equiv\sigma\pmod4\), and let \(h\in4\mathbb Z_2\setminus\{0\}\), \(y=x+h\). The binomial expansion for integral 2-adic exponents gives
\[
\frac{F(y)}{F(x)}
=(\sigma x)^h(1+h/x)^{x+h}
\equiv1+h\pmod{4h\mathbb Z_2}.
\]
Indeed \((\sigma x)^h\equiv1\pmod{4h}\) because its logarithm is a multiple of \(4h\), while \((1+h/x)^{x+h}\equiv1+(x+h)h/x\equiv1+h\pmod{h^2}\), and \(h^2\in4h\mathbb Z_2\). Consequently,
\[
F(x+h)-F(x)\equiv\sigma h\pmod{4h\mathbb Z_2}.\tag{1}
\]
Thus \(\nu_2(F(y)-F(x))=\nu_2(y-x)\) within each mod-four branch. Across different mod-four branches both sides have valuation one, because \(F(z)\equiv z\pmod4\). Hence \(F\) is a 2-adic isometry on the units. It induces an injective, therefore bijective, map on the finite odd classes modulo every \(2^k\). Equation (1) also shows that on the positive branch \(F\) has slope \(1\pmod4\), while on the negative branch its square \(F^2\) has slope \(1\pmod4\).

**2. Initial displacements.** Suppose \(x\equiv1\pmod4\), \(x\ne1\), and write \(r=\nu_2(x-1)\ge2\). Since \(F(x)/x=x^{x-1}\), and \(\nu_2(\log x)=r\), the logarithmic/exponential isometry yields
\[
\nu_2(F(x)-x)=2r.\tag{2}
\]
Now suppose \(x\equiv-1\pmod4\), \(x\ne-1\). Set \(u=-x\in1+4\mathbb Z_2\) and \(r=\nu_2(x+1)=\nu_2(\log u)\ge2\). Because \(\nu_2(x-1)=1\) and \(F(x)/x=u^{x-1}\),
\[
\nu_2(F(x)-x)=r+1.\tag{3}
\]
There is a second exact identity for this branch. Let \(y=F(x)=-u^x\). Then \(-y=u^x\), \(xy=u^{x+1}\), and
\[
\frac{F^2(x)}x=u^{xy-1}.
\]
The 2-adic valuation of \(xy-1=u^{x+1}-1\) is \(2r\), so
\[
\nu_2(F^2(x)-x)=3r.\tag{4}
\]
The two exceptional points \(x=\pm1\) are fixed exactly in \(\mathbb Z_2\).

**3. Exact period doubling.** We use an elementary strong-isometry lemma: if an isometry \(H\) preserves a mod-four ball and satisfies
\[
H(z+h)-H(z)\equiv h\pmod{4h\mathbb Z_2}
\quad(h\in4\mathbb Z_2\setminus\{0\}),
\]
then for \(d=H(z)-z\ne0\) with \(d\in4\mathbb Z_2\),
\[
\nu_2(H^{2^j}(z)-z)=\nu_2(d)+j\quad(j\ge0).\tag{5}
\]
To prove this, note that the congruence is preserved by composition. Writing \(d=H(z)-z\), we have
\[
H^2(z)-z=d+\bigl(H(z+d)-H(z)\bigr)
\equiv2d\pmod{4d\mathbb Z_2},
\]
whose valuation is exactly \(\nu_2(d)+1\). Replace \(H\) by \(H^2\) and repeat. This proves (5) by induction.

By (1), lemma (5) applies to \(H=F\) on \(1+4\mathbb Z_2\), using (2), and to \(H=F^2\) on \(-1+4\mathbb Z_2\), using (4). Hence for all \(j\ge0\),
\[
\nu_2(F^{2^j}(x)-x)=2r+j\quad(x\equiv1\pmod4),\tag{6}
\]
and for all \(j\ge1\),
\[
\nu_2(F^{2^j}(x)-x)=3r+j-1\quad(x\equiv-1\pmod4).\tag{7}
\]
For the negative branch the first iterate instead obeys (3). Equations (6) and (7) show that some power of two returns every point modulo \(2^k\), so all least periods are powers of two. The first such power whose displacement is divisible by \(2^k\) gives the displayed period formulas. In the negative branch, if (3) fails the fixed-point test, the first possible period is two, and (7) gives all subsequent doublings.

**4. Cycle counts and extremal lengths.** For each \(2\le r<k\), each of the sets \(\{x\bmod 2^k:\nu_2(x-1)=r\}\) and \(\{x\bmod2^k:\nu_2(x+1)=r\}\) has precisely \(2^{k-r-1}\) members. The two exceptional residues \(\pm1\) are fixed. Dividing the number of points of each period by that period proves the exact formula for \(C_k(\ell)\). Summing the fixed-point terms gives \(2^{\lfloor k/2\rfloor}+2\) for \(k\ge3\). For \(k\ge6\), the largest possible period is \(2^{k-4}\), arising only in the positive branch with \(r=2\). That branch has \(2^{k-3}\) points, hence precisely two such maximal cycles.

## Verification
The accompanying standard-library script `verify_selfpower.py` enumerates the independent modular functional graphs on all odd residues for every \(1\le k\le16\), compares the observed cycle decompositions with the closed formulas, and independently checks sample iterate-displacement valuations to forty-bit precision. The successful replay reported `VERIFY_OK k=1..16 complete_odd_cycles=PASS total_cycles=3626 valuation_tests=1016 max_cycles=PASS prior_two_walk_counts=PASS`. At \(k=10\), for example, the cycle-length counts are \(C_{10}(1)=34\), \(C_{10}(2)=31\), \(C_{10}(4)=24\), \(C_{10}(16)=4\), \(C_{10}(32)=4\), \(C_{10}(64)=2\), and zero otherwise. These finite tests are not the proof of the all-\(k\) result.

## Relationship to prior work
Holden, Richardson and Robinson, arXiv:1609.06696 (first public September 21, 2016), study the generalized self-power maps and count fixed points and two-step rooted closed walks modulo prime powers. In the binary special case their Corollary 11 gives the fixed-point count, and Corollary 19 counts all points of period dividing two. Both are recovered by the formulas above, but neither determines the period of arbitrary points or the full cycle census at all lengths. Their Section 6 expressly discusses cycles beyond length two as future work. Holden and Robinson (2012), Section 6, count inverse fibers of the self-power map for odd primes; their Section 7 treats self-power collisions, not full binary orbit lengths. Friedrichsen, Larson and McDowell (2010) focus on the prime-modulus setting, a distinct scope. The contribution here is the valuation law for **every iterate of dyadic length**, its branch-dependent initial displacement, and the resulting complete cycle census.

## Limitations
The theorem concerns only the unit permutation at powers of two; even inputs, odd prime powers, and generalized exponents are not classified. The mathematical proof is self-contained, but historical priority cannot be certified by finite literature searches, and earlier or inaccessible equivalent statements remain possible. The code checks finite moduli only; all infinite assertions depend on the written proof. No independent mathematical audit has been performed.

## References
1. J. Holden, P. A. Richardson, M. M. Robinson, *Counting fixed points and rooted closed walks of the singular map \(x\mapsto x^{x^n}\) modulo powers of a prime*, arXiv:1609.06696, original submission 2016-09-21; particularly Theorem 10, Corollaries 11 and 19, and Section 6. https://arxiv.org/abs/1609.06696 ; full HTML https://ar5iv.labs.arxiv.org/html/1609.06696
2. J. Holden and M. M. Robinson, *Counting fixed points, two-cycles, and collisions of the discrete exponential function using \(p\)-adic methods*, Journal of the Australian Mathematical Society 92 (2012), 163–178. DOI:10.1017/S1446788712000262; particularly Sections 6–7.
3. M. Friedrichsen, B. Larson, E. McDowell, *Structure and Statistics of the Self-Power Map*, Rose-Hulman Undergraduate Mathematics Journal 11 (2010), issue 2, article 6. https://scholar.rose-hulman.edu/rhumj/vol11/iss2/6/
