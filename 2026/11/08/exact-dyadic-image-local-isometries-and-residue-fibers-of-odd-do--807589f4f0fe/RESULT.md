# Exact dyadic image, local isometries and residue fibers of odd double factorials

## Finding

Let \(q_n=(2n-1)!!=\prod_{j=0}^{n-1}(2j+1)\), with \(q_0=1\). For every integer \(t\ge2\) and \(n\ge0\), the exact block-product valuation is
\[
\nu_2\!\left(\prod_{j=0}^{2^t-1}(2n+2j+1)-1\right)=t+1+(n\bmod2).
\]
Consequently, whenever \(m>n\ge0\) and \(m\equiv n\pmod4\),
\[
\nu_2(q_m-q_n)=\nu_2(m-n)+1+(n\bmod2).
\]
The four maps on indices \(n=4u+r\), \(r\in\{0,1,2,3\}\), extend to \(2\)-adic bijections from \(\mathbb Z_2\) onto the respective balls
\[
1+8\mathbb Z_2,\quad1+16\mathbb Z_2,\quad3+8\mathbb Z_2,\quad15+16\mathbb Z_2.
\]
Each map becomes an isometry after subtracting its starting value and dividing by the corresponding power of two. In particular,
\[
\overline{\{q_n:n\ge0\}}=(1+8\mathbb Z_2)\,\cup\,(3+8\mathbb Z_2)\,\cup\,(15+16\mathbb Z_2),
\]
where the three displayed balls are disjoint, and the normalized additive Haar measure of this image is \(5/16\). The number of attained residues modulo \(2^k\) is \(1,2,3\) for \(k=1,2,3\), respectively, and \(5\cdot2^{k-4}\) for every \(k\ge4\). For \(k\ge4\), among indices \(0\le n<2^k\), the multiplicity of a residue \(y\) modulo \(2^k\) is exactly
\[
\begin{cases}
6,&y\equiv1\pmod{16},\\
4,&y\equiv15\pmod{16},\\
2,&y\equiv9\pmod{16}\text{ or }y\equiv3\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]
The least index period of \(q_n\bmod 2^k\) equals \(1\) for \(k=1\), \(4\) for \(k=2\), and \(2^{k-1}\) for every \(k\ge3\). As a consequence, the Morita dyadic gamma function maps \(\mathbb Z_2\) onto \(\mathbb Z_2^\times\); the exact even-argument image is the proper set of measure \(5/16\) above.

## Assumptions and scope

All indices are nonnegative ordinary integers; the product over the empty set is one. The symbol \(\nu_2(a)\) means the exponent of two in a nonzero integer \(a\); \(\mathbb Z_2\) is the ring of dyadic integers. The residue fibers count **indices** in one full block \(0\le n<2^k\), not distinct dyadic lifts. Every asserted infinite-level image is the closure of the nonnegative-index values. The normalized measure on \(\mathbb Z_2\) assigns measure \(2^{-h}\) to each coset modulo \(2^h\).

## Proof

**Block lemma.** Put \(B_t(n)=\prod_{j=0}^{2^t-1}(2n+2j+1)\). For \(t=2\), direct expansion in the four residue classes of \(n\pmod4\) yields
\[
B_2(n)\equiv\begin{cases}9\pmod{32},&n\equiv0\pmod2,\\17\pmod{32},&n\equiv1\pmod2.\end{cases}
\]
Thus \(\nu_2(B_2(n)-1)=3+(n\bmod2)\). For every \(t\ge2\), division by odd factors is valid modulo any power of two, so
\[
\frac{B_t(n+2^t)}{B_t(n)}=\prod_{j=0}^{2^t-1}\left(1+\frac{2^{t+1}}{2n+2j+1}\right).
\]
The coefficient of \(2^{t+1}\) is a sum of \(2^t\) odd-unit inverses. Modulo eight, those denominators run equally often through \(1,3,5,7\), whose inverses are the same residue classes and whose sum is zero modulo eight. All terms involving at least two correction factors are divisible by \(2^{2t+2}\), hence by \(2^{t+4}\). Therefore
\[
B_t(n+2^t)\equiv B_t(n)\pmod{2^{t+4}}.
\]
Using \(B_{t+1}(n)=B_t(n)B_t(n+2^t)\), we have \(B_{t+1}(n)\equiv B_t(n)^2\pmod{2^{t+4}}\). The block product is always \(1\pmod8\) by induction; thus
\[
\nu_2(B_t(n)^2-1)=\nu_2(B_t(n)-1)+1=t+2+(n\bmod2)<t+4.
\]
Induction establishes the block lemma for every \(t\ge2\).

**Distance law.** If \(m-n=2^t a\) with \(t\ge2\) and \(a\) odd, then \(q_m/q_n\) is the product of \(a\) consecutive blocks \(B_t(n+j2^t)\). All these blocks are congruent to \(1+2^{t+1+(n\bmod2)}\) modulo \(2^{t+2+(n\bmod2)}\). Multiplying an odd number of these factors gives the same exact valuation. Because \(q_n\) is odd, the quotient valuation equals \(\nu_2(q_m-q_n)\). This proves the distance law for \(m>n\) in the same class modulo four; symmetry handles reversed indices.

**Four isometries.** Let \(c_r=q_r\) and \(e_r=3\) when \(r\) is even, \(e_r=4\) when \(r\) is odd. The distance law applied to \(m=4v+r\), \(n=4u+r\) says
\[
\nu_2\left(\frac{q_{4v+r}-c_r}{2^{e_r}}-\frac{q_{4u+r}-c_r}{2^{e_r}}\right)=\nu_2(v-u).
\]
Since \(c_0=c_1=1\), \(c_2=3\), and \(c_3=15\), each normalized map on \(u\ge0\) extends uniquely by density and the isometry property to an isometry \(F_r:\mathbb Z_2\to\mathbb Z_2\). Every isometry of \(\mathbb Z_2\) into itself maps distinct classes modulo \(2^h\) to distinct classes; because there are exactly \(2^h\) such classes, the induced map is bijective for every \(h\), and compactness makes \(F_r\) onto. The four images are precisely the stated balls.

**Image and fibers.** The image of all nonnegative indices is the union of these four balls, reducing to three disjoint balls because \(1+16\mathbb Z_2\subset1+8\mathbb Z_2\). Their measures sum to \(1/8+1/8+1/16=5/16\). For \(k\ge4\), the four residue classes of indices each contribute \(2^{k-2}\) arguments. By the bijective isometries, a residue in a ball of modulus \(2^{e_r}\) is attained exactly \(2^{e_r-2}\) times from the corresponding index class; hence even classes each contribute two, odd classes each contribute four. Adding their contributions gives the stated exact fiber table and residue count. Reduction modulo two, four and eight yields the three smaller counts.

**Least period.** The block lemma shows \(q_{n+2^{k-1}}\equiv q_n\pmod{2^k}\) for every \(k\ge3\), and the first four residues verify period four for \(k=2\). For \(k\ge4\), the same block lemma shows \(q_{2^{k-2}}\not\equiv q_0\pmod{2^k}\), excluding half the candidate period. Every period of a sequence with period a power of two has a least period dividing that power, so the proposed period is least. For \(k=3\), compare \(q_2=3\) with \(q_0=1\); for \(k=2\) the analogous comparison excludes period two.

**Dyadic gamma corollary.** By the standard continuous Morita definition, \(\Gamma_2(2n)=q_n\) and \(\Gamma_2(2n+1)=-q_n\). Continuity and density therefore give \(\Gamma_2(2\mathbb Z_2)=S\) and \(\Gamma_2(1+2\mathbb Z_2)=-S\), with \(S\) the three-ball image above. The union \(S\cup(-S)\) meets all eight odd classes modulo sixteen as full balls; it equals \(\mathbb Z_2^\times\). This corollary does not assert historical novelty of general gamma-function surjectivity.

## Verification

Run the included standard-library script using `python3 verify.py`. It enumerates all index fibers modulo \(2^k\), for \(1\le k\le15\), and verifies the sharp block-product valuation in 720 instances. The script is finite corroboration, not a proof of the infinite statements; the block lemma and isometry argument establish those statements.

## Relationship to prior work

Morita introduced the continuous \(p\)-adic gamma function, whose even dyadic integer values coincide with odd double factorials. The integer sequence itself is classical and appears in OEIS A055634; those definitions and identities are not claimed as new. Relevant background includes Barsky's study of Morita's function, Menken and Körükçü's dyadic q-extension identity, and Adamus's study of differential transcendence. The assessed contribution is the exact four-branch isometry law, three-ball even-input value image, exact all-level fiber census, and least index periods. The original Morita and Barsky full texts were not materially inspected; it remains possible that relevant historical results or implications appear there.

## Limitations

The theorem is confined to the prime two and the classical odd double factorial sequence, not the odd-prime Morita functions. It gives exact fibers for full dyadic index blocks rather than a formula for the smallest positive index attaining every residue. Literature priority requires specialist review; no independent mathematical audit has been performed.

## References

1. Y. Morita, “A p-adic analogue of the Gamma-function,” 1975. Bibliographic record: https://cir.nii.ac.jp/crid/1390853649532240000.
2. D. Barsky, “On Morita’s p-adic Γ-function,” seminar contribution, 1977–1978. https://numdam.org/item/GAU_1977-1978__5__A1_0/.
3. OEIS A055634, “2-adic factorial function.” https://oeis.org/A055634.
4. OEIS Wiki, “Double factorial.” https://oeis.org/wiki/Double_factorial.
5. E. Adamus, “On the differential transcendentality of the Morita p-adic gamma function,” European Journal of Mathematics 9 (2023), article 7. https://doi.org/10.1007/s40879-023-00602-7.
6. “Hypergeometric L-functions in average polynomial time, II,” Research in Number Theory (2025), Section 3, standard gamma definition. https://doi.org/10.1007/s40993-024-00593-8.
7. H. Menken and A. Körükçü, “Some Properties of the q-Extension of the p-Adic Gamma Function,” Abstract and Applied Analysis (2013). https://doi.org/10.1155/2013/176470.
