# Exact antisquare factors, occurrence sets and densities in generalized period-doubling words

## Finding

For every integer \(b\ge2\), the one-sided generalized period-doubling word \(x_b\) has the **complete antisquare factor language**
\[
\mathcal A_b=\begin{cases}
\{01,10,010101,101010\},&b=2,\\
\{01,10,1001\},&b=3,\\
\{01,10\},&b\ge4.
\end{cases}
\]
An antisquare is a binary word \(u\overline u\) with nonempty \(u\), and \(\overline u\) changes every bit. All factors in the displayed sets occur infinitely often, and no others occur. The following **exact zero-based starting-position sets** hold:

- \(\operatorname{Occ}_b(10)=\{i\ge0:\nu_b(i+1)\text{ is odd}\}\).
- \(\operatorname{Occ}_b(01)=\{i\ge0:\nu_b(i+2)\text{ is odd}\}\).
- \(\operatorname{Occ}_3(1001)=\{3q+2:q\ge0,\ \nu_3(q+1),\nu_3(q+2)\text{ are even}\}\).
- \(\operatorname{Occ}_2(010101)=\{2q:q\ge0,\ \nu_2(q+2)\text{ is positive and even}\}\).
- \(\operatorname{Occ}_2(101010)=\{2q+1:q\ge0,\ \nu_2(q+2)\text{ is positive and even}\}\).

Every listed antisquare has a natural starting-position density, explicitly
\[
\delta_b(01)=\delta_b(10)=\frac{1}{b+1},\quad
\delta_3(1001)=\frac16,\quad
\delta_2(010101)=\delta_2(101010)=\frac1{12}.
\]
Every absent antisquare has zero occurrence density.

**Exact finite-cutoff law.** For \(N\ge0\), let \(C_b(w,N)=|\{0\le i<N:x_b[i..i+|w|-1]=w\}|\). Introduce the finite integer sums
\[
H_b(T)=\sum_{j\ge0}\left(\left\lfloor\frac{T}{b^{2j+1}}\right\rfloor-\left\lfloor\frac{T}{b^{2j+2}}\right\rfloor\right),\quad
E(T)=\sum_{j\ge1}\left(\left\lfloor\frac{T}{2^{2j}}\right\rfloor-\left\lfloor\frac{T}{2^{2j+1}}\right\rfloor\right),
\]
with \(H_b(0)=E(0)=0\) and terms zero once powers exceed \(T\). Then
\[
\begin{aligned}
C_b(10,N)&=H_b(N),& C_b(01,N)&=H_b(N+1),\\
C_2(010101,N)&=E\left(\left\lfloor\tfrac{N-1}{2}\right\rfloor+2\right),&
C_2(101010,N)&=E\left(\left\lfloor\tfrac{N-2}{2}\right\rfloor+2\right).
\end{aligned}
\]
For \(b=3\), set \(Q=\lfloor(N-3)/3\rfloor\). Then \(C_3(1001,N)=0\) if \(Q<0\), and otherwise
\[
C_3(1001,N)=Q+1-H_3(Q+1)-H_3(Q+2).
\]
Here every occurrence is counted by its starting index, even when its right endpoint lies beyond the first \(N\) symbols.

## Assumptions and scope

The base \(b\) is any integer at least two, not necessarily prime. For any positive integer \(m\), \(\nu_b(m)=\max\{e\ge0:b^e\mid m\}\) is the exponent of divisibility by powers of the entire base, and \(x_b(i)=\nu_b(i+1)\bmod2\) for integer \(i\ge0\). No valuation of zero is used. All positions and factor starts are zero-based. A density is a limit of \(C_b(w,N)/N\) as integer \(N\to\infty\). The standard binary complement is bitwise exchange of zero and one.

## Proof

**1. Spacing and the general obstruction.** For every base \(b\), \(x_b(i)=1\) implies \(b\mid(i+1)\), so every one occurs at index congruent to \(b-1\) modulo \(b\); in particular, ones are separated by at least \(b\) positions. Every order-\(k\) antisquare \(u\overline u\) of length \(2k\) contains exactly \(k\) ones, independently of \(u\). A window of \(2k\) positions with ones spaced at least \(b\) contains at most \(1+\lfloor(2k-1)/b\rfloor\) ones. For \(b\ge4\) and \(k\ge2\), this is smaller than \(k\). For \(b=3\) and \(k\ge3\), this is smaller than \(k\). Hence the only possible nontrivial antisquare occurs at \(b=3,k=2\), and none occur at \(b\ge4,k\ge2\).

**2. Base three.** At \(b=3,k=2\), two ones in four positions spaced at least three units apart force the factor \(1001\), which is \(10\overline{10}\). Its first one must occur at \(i=3q+2\), \(q\ge0\). The endpoint values are \(x_3(3q+2)=(1+\nu_3(q+1))\bmod2\) and \(x_3(3q+5)=(1+\nu_3(q+2))\bmod2\). Both equal one precisely when those two valuations are even; all positions between them are automatically zero. This gives the factor and its full occurrence test.

**3. Base two.** Every even index of \(x_2\) is zero. Therefore an antisquare of length \(2k\), having exactly \(k\) ones, must have ones at every odd index in its window, hence must alternate. Its first half and second half are complementary precisely if \(k\) is odd. For any four consecutive odd indices \(2t+1\), one has \(t+1\equiv2\pmod4\), and its value is \((1+\nu_2(t+1))\bmod2=0\). Thus four consecutive odd positions cannot all be ones, giving \(k\le3\). For \(k=1\), transitions \(01,10\) occur; for \(k=3\), only \(010101,101010\) are possible. The three odd indices in either alternating length-six factor are associated with three consecutive positive integers \(q+1,q+2,q+3\) via \(x_2(2t+1)=(1+\nu_2(t+1))\bmod2\). The outer integers are odd exactly when the center integer \(q+2\) is even, and then the three values all equal one iff \(\nu_2(q+2)\) is positive and even. Distinguishing even and odd starting indices gives the two exact occurrence sets.

**4. Order one in every base.** A one in \(x_b\) is isolated by at least \(b-1\ge1\) zeros. Consequently the factor \(10\) begins exactly at a one-index \(i\), and \(01\) begins exactly one position before that one-index; there is no one at position zero. Replacing the one-index condition by valuation parity proves both occurrence sets.

**5. All exact counts and densities.** The number of positive integers \(m\le T\) with odd \(\nu_b(m)\) is \(H_b(T)\): the summand indexed by \(j\) counts integers divisible by \(b^{2j+1}\) but not \(b^{2j+2}\). Similarly, \(E(T)\) counts positive integers \(m\le T\) with strictly positive even \(\nu_2(m)\). Translating the occurrence tests gives the finite-cutoff equations above. For the base-three test, note that \(q+1\) and \(q+2\) cannot both be divisible by three, so the events of *odd* valuation are disjoint and can be subtracted from \(Q+1\) possible starting indices. This yields its exact count.

The geometric series give \(H_b(T)/T\to\sum_{j\ge0}(b^{-(2j+1)}-b^{-(2j+2)})=1/(b+1)\), and \(E(T)/T\to\sum_{j\ge1}(2^{-2j}-2^{-(2j+1)})=1/6\). Integer floor errors are at most logarithmic in \(T\), hence vanish after division by \(T\). The base-two exceptional factors each draw one parity class of starting positions, so each density is \((1/2)(1/6)=1/12\). The base-three exceptional factor draws one residue class mod three and excludes two disjoint odd-valuation conditions, each of conditional density \(1/4\), so its density is \((1/3)(1-1/4-1/4)=1/6\). Each density is positive, proving all displayed factors actually occur infinitely often. This completes the proof.

## Verification

The accompanying standalone \(\texttt{verify.py}\) implements the valuation definition independently, tests all bases \(2\) through \(14\), inspects \(16{,}000\) starts per base and antisquare orders \(1\) through \(32\), and checks exact finite-cutoff formulas at 18 selected cutoffs for each base. The observed result was \(\texttt{VERIFY\_OK}\). The infinite exclusion and exact density statements follow from the proof above, not from the finite test horizon.

## Relationship to prior work

Baranwal, Currie, Mol, Ochem, Rampersad and Shallit defined the antisquare-avoidance setting and characterized minimal antisquares in their 2022 preprint [1]. Their results include the base patterns needed for general obstruction tests but do not present the all-base occurrence and density equations here. Currie's 2023 analysis [2] of ordinary period-doubling words already supplies avoidance constraints that cover the base-two *factor-support* portion in conjunction with elementary observations. That support is not claimed as independently new. The contribution assessed here is the **combined exact all-base support, occurrence positions, rational densities, and exact finite-prefix counting formulas**. Known general automatic-sequence counting methods could in principle compute individual frequencies; no checked primary source was found stating these explicit formulas. An unindexed or differently formulated equivalent remains possible.

## Limitations

The theorem concerns standard bitwise binary antisquares and the specified one-sided valuation-parity family only; it makes no claim about other binary morphisms, longer alphabets, or uniformly random words. It does not establish a novel general algorithm for all automatic words. The base-two antisquare support is partly covered by previous avoidance work; novelty is qualified accordingly. The finite verifier is diagnostic evidence, not an infinite proof. No independent scientific validation has been performed.

## References

[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223 (first public 2022-09-19), https://arxiv.org/abs/2209.09223 ; published in *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023), DOI:10.46298/dmtcs.10063.

[2] J. D. Currie, *The Analog of Overlap-Freeness for the Period-Doubling Sequence*, arXiv:2303.14539 (first public 2023-03-25); *Journal of Integer Sequences* 26 (2023), Article 23.8.2, https://arxiv.org/abs/2303.14539 and https://cs.uwaterloo.ca/journals/JIS/VOL26/Currie/currie16.html.
