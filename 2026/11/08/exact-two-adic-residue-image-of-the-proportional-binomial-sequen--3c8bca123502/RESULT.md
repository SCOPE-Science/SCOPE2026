# Exact two-adic residue image of the proportional binomial sequence \(\binom{3n}{n}\)

## Finding
For each integer \(n\ge0\) put \(B_n=\binom{3n}{n}\). For every integer \(k\ge2\),
\[
\{ B_n\bmod 2^k:n\ge0\}=\{r\bmod 2^k:0\le r<2^k,\ r\not\equiv 2\pmod4\}.
\]
Modulo \(2\), both residue classes occur. Thus for every exponent the image consists of the odd classes and the classes represented by multiples of four. Each permitted residue occurs at infinitely many distinct positive indices. Therefore the exact image cardinality is \(2\) for \(k=1\) and \(3\cdot2^{k-2}\) for \(k\ge2\); the closure in the two-adic integers is \(\mathbb Z_2^\times\cup4\mathbb Z_2\), of normalized Haar measure \(3/4\).

## Assumptions and scope
All binomial coefficients are ordinary integer binomial coefficients. The valuation \(\nu_2\) satisfies \(\nu_2(0)=+\infty\). Congruences and limits refer to \(\mathbb Z_2\). No claims are made about other proportional binomial sequences, their index distributions, or frequencies within finite index windows.

## Proof
**1. Exclusion of valuation one and valuation seeds.** By Kummer's theorem, \(\nu_2(B_n)\) is the number of carries in base-two addition of \(n+2n\). If a first carry occurs at position \(i\), the input bits at that position must be \(n_i=n_{i-1}=1\). At position \(i+1\), the shifted summand has bit \(n_i=1\), and the incoming carry is one, so a second carry is forced. Hence \(\nu_2(B_n)\ne1\). For each \(s\ge2\), direct examination of doubling the \(s\)-bit string of ones shows exactly \(s\) carries for \(n=2^s-1\). Shifting the binary string left does not change the carry count, so \(\nu_2(B_{2^t(2^s-1)})=s\) for all \(t\ge0\).

**2. Limits under doubling.** For a positive integer \(m\) let \(O(m)=\prod_{1\le j\le m,\;j\text{ odd}}j\). Separating even from odd factors in factorials gives
\[
\frac{B_{2N}}{B_N}=\frac{O(6N)}{O(2N)O(4N)}.
\]
For fixed \(k\ge1\) and \(N=2^t a\) with \(a\ge1\) fixed, all three products on the right are congruent to one modulo \(2^k\) for sufficiently large \(t\). Indeed, each is a union of complete blocks of odd residues modulo \(2^k\); the product of the units in a complete block equals one when \(k\ge3\), and for \(k=1,2\) each block product also becomes one after the even number of repetitions supplied by increasing \(t\). The ratio therefore tends to one modulo every \(2^k\); thus \(U_a=\lim_{t\to\infty}B_{2^t a}\in\mathbb Z_2\) exists. The carry count proves \(\nu_2(U_a)=\nu_2(B_a)\).

**3. Multiplication from separated binary blocks.** Fix \(k\ge1\) and positive integers \(a,b\). Put \(A=2^t a\) and \(H=2^{t+r}b\). The exact factorial identity is
\[
\frac{B_{A+H}}{B_H}=\frac{\prod_{j=1}^{3A}(3H+j)}{\left(\prod_{j=1}^{A}(H+j)\right)\left(\prod_{j=1}^{2A}(2H+j)\right)}.
\]
Comparing factor-by-factor with the factorial formula for \(B_A\), note that \(\nu_2(j)\le t+\lfloor\log_2(3a)\rfloor\) for all appearing \(j\). Whenever \(r\ge k+\lfloor\log_2(3a)\rfloor+1\), each factor \(1+3H/j\), \(1+H/j\), and \(1+2H/j\) is congruent to one modulo \(2^k\) in \(\mathbb Z_2\). It follows that
\[
B_{2^t(a+2^r b)}\equiv B_{2^t a}B_{2^{t+r}b}\pmod{2^k}.
\]
Taking \(t\to\infty\) gives \(U_{a+2^r b}\equiv U_aU_b\pmod{2^k}\). The lower bound on \(r\) is independent of \(b\). Inductively, any finite product \(\prod_i U_{a_i}\) can be represented modulo \(2^k\) by some \(U_N\), by separating finitely many prescribed blocks by sufficiently many zeros.

**4. Unit generation.** The congruence in step 2 gives \(U_1\equiv B_8\equiv7\pmod8\) and \(U_9\equiv B_{72}\equiv5\pmod8\). For every \(k\ge3\), the elementary lifting identity \(\nu_2(u^{2^j}-1)=j+2\) for \(u\equiv5\pmod8\) and \(j\ge0\) shows that \(U_9\) has order \(2^{k-2}\) modulo \(2^k\), and therefore generates all units congruent to one modulo four. Since \(U_1\equiv3\pmod4\), the pair generates every odd unit modulo \(2^k\). The assertions for \(k=1,2\) follow directly.

**5. All permitted valuations.** To obtain an arbitrary odd residue \(u\bmod2^k\), realize a suitable nonempty finite product of \(U_1,U_9\) as \(U_N\) (for the identity residue, use a positive power of \(U_9\) equal to one modulo \(2^k\)). Given \(2\le s<k\), use \(a=2^s-1\); step 1 gives \(U_a=2^s v\) for some odd two-adic unit \(v\). Choose a finite product of \(U_1,U_9\) reducing modulo \(2^{k-s}\) to \(v^{-1}u\). The block lemma realizes its product with \(U_a\), giving \(U_N\equiv2^su\pmod{2^k}\). To obtain zero, take \(a=2^s-1\) with \(s\ge\max\{2,k\}\). Finally, for each constructed \(N>0\), the sequence \(B_{2^t N}\) stabilizes to \(U_N\) modulo \(2^k\), yielding infinitely many distinct witnesses. The missing valuation-one classes were excluded in step 1, completing the proof.

## Verification
A standalone Python verifier checks \(B_n\) against exact integer binomial coefficients, scaled-limit congruences, separated-block congruences, unit generators, and the predicted spectrum through \(2^8\). Run `python3 verify.py`. Finite checks support but do not replace the five unlimited steps of the proof.

## Relationship to prior work
Barat and Grabner studied distributions and unit parts among broadly varying binomial coefficients in Pascal's triangle (2001), not this fixed proportional family. Sun and Zhang established density results for coefficients with fixed lower index (arXiv:0812.3089), which does not fix the ratio of upper and lower indices. Davis developed limits of binomial coefficients involving growing prime powers (arXiv:1301.6285). Theorem 1.3 assumes the difference between the fixed top and bottom multipliers is a prime-adic unit; for multipliers \(3\) and \(1\) at the prime \(2\), that difference is \(2\), so the stated theorem is inapplicable. The paper does not classify the present full residue image. Guo (arXiv:1312.7548) studied divisibility of closely related \(\binom{3n}{n}\) expressions, not their complete fixed-power residue spectrum. The image formula, forced valuation gap, and generation of every remaining valuation shell constitute the claimed contribution.

## Limitations
The assertion applies only to the ratio \(\binom{3n}{n}\) and the prime two. It gives no quantitative bounds on the smallest witnessing index and no asymptotic frequencies of residues among initial segments. Novelty is a best-knowledge assessment, not proof of global historical uniqueness; a previously unlocated stronger result could imply this theorem. Independent mathematical verification remains outstanding.

## References
1. G. Barat and P. J. Grabner, “Distribution of Binomial Coefficients and Digital Functions”, *Journal of the London Mathematical Society* 64 (2001), 523–547. Accessible preprint: `https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf` (consulted in full).
2. Z.-W. Sun and W. Zhang, “Binomial coefficients and the ring of \(p\)-adic integers”, arXiv:0812.3089 (December 16, 2008), `https://arxiv.org/abs/0812.3089` (consulted in full).
3. D. M. Davis, “Binomial Coefficients Involving Infinite Powers of Primes”, arXiv:1301.6285 (January 26, 2013), `https://arxiv.org/pdf/1301.6285` (consulted in full).
4. V. J. W. Guo, “Proof of two divisibility properties of binomial coefficients conjectured by Z.-W. Sun”, arXiv:1312.7548 (December 29, 2013), `https://arxiv.org/abs/1312.7548` (consulted in full).
