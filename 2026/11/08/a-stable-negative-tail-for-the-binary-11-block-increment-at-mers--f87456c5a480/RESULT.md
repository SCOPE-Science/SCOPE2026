# A stable negative tail for the binary \(11\)-block increment at Mersenne shifts

## Finding

For every nonnegative integer \(n\), let \(r(n)\) be the number of overlapping occurrences of the word \(11\) in the ordinary binary expansion of \(n\): if \(n=\sum_{i\ge0}\varepsilon_i(n)2^i\), then
\[
r(n)=\sum_{i\ge0}\varepsilon_i(n)\varepsilon_{i+1}(n).
\]
For integers \(k\ge1\) and \(j\in\mathbb Z\), define the natural density
\[
\mu_k(j)=\lim_{N\to\infty}\frac1N\#\{0\le n<N:r(n+2^k-1)-r(n)=j\}.
\]
All these densities exist. For every \(k\ge4\) and every integer \(j\ge1\),
\[
\boxed{\mu_k(-j)=\frac{45}{128\,2^j},\qquad
\sum_{j\ge0}\mu_k(j)=\frac{83}{128}>\frac12.}
\]
The threshold \(k=4\) is sharp: the corresponding nonnegative-difference densities for \(k=1,2,3\) are, respectively, \(13/16,47/64,87/128\), none equal to \(83/128\).

In fact, for \(k\ge4\), the exact Laurent probability generating functions \(G_k(z)=\sum_{j\in\mathbb Z}\mu_k(j)z^j\), convergent for \(|z|>1/2\), satisfy
\[
\boxed{G_4(z)=\frac{(z+1)(4z^4+11z^2+10z+7)}{64(2z-1)}}
\]
and the polynomial-increment identity
\[
\boxed{G_{k+1}(z)-G_k(z)=
\frac{z^{k-4}(z-1)^2(z+1)(2z^2+z+2)}{2^{k+3}}.}
\]
Thus the entire negative tail is independent of the length of the run of ones, even though the nonnegative part of the distribution changes with \(k\).

## Assumptions and scope

All powers and binary digits are ordinary nonnegative-integer conventions. The density counts all \(n\ge0\) and concerns the unscaled difference of the *overlapping* adjacent-one count. The shift is exactly the one-block Mersenne number \(2^k-1\). The variable \(z\) is a nonzero complex number satisfying \(|z|>1/2\) when the Laurent expansion is interpreted as a probability generating series; all rational identities also hold formally.

## Proof

**Step 1: carry/adjacency automaton and limiting density.** Process the input bits of \(n\) from least to most significant. Maintain a state \(s=(c,p,q)\in\{0,1\}^3\), where \(c\) is the incoming carry for the addition, and \(p,q\) are the previous input and output bits. For a fixed bit \(b\) of the shift, a fresh input bit \(x\in\{0,1\}\) produces
\[
u=x+b+c,\qquad y=u\bmod2,\quad c'=\lfloor u/2\rfloor,
\qquad s'=(c',x,y).
\]
Its contribution to the difference in adjacent-one counts is \(qy-px\). Define an eight-by-eight matrix \(T_b(z)\), with rows and columns indexed by \((c,p,q)\) in lexicographic order, by adding \(z^{qy-px}/2\) to entry \((s,s')\) for each \(x=0,1\). The initial state is \(s_0=(0,0,0)\). The factor \(1/2\) represents independent, uniformly distributed low bits of \(n\).

After all nonzero shift bits have been processed, the remaining shift bits are zero. The carry can survive across \(h\) further steps only if the next \(h\) input bits are all ones, an event of probability \(2^{-h}\). Thus the contribution from the tail is almost surely finite. For any fixed cutoff, its evaluation depends on finitely many low bits, and these bits have exactly uniform asymptotic frequencies in natural-number intervals. The carry-tail probability bound, followed by increasing the cutoff, proves existence of the asserted natural densities and identifies them with the automaton distribution.

**Step 2: an explicit infinite zero-bit tail.** Let \(g_{c,p,q}(z)\) be the generating function of the remaining difference after the shift bits have become zero. Write
\[
P(z)=\frac{1+z}{2},\qquad H(z)=\frac{z(z+1)}{2(2z-1)}.
\]
A one-step recurrence on the next random input bit yields
\[
g_{0,p,q}=\begin{cases}1,&p=q,\\(1+z^{q-p})/2,&p\ne q,\end{cases}
\qquad
 g_{1,p,q}=\frac{z^q P(z)}2+\frac{z^{-p}H(z)}2.
\]
Indeed, with no incoming carry, the next output equals the input and the previous-bit mismatch disappears after one step. With carry one, input zero clears the carry, whereas input one preserves it; the latter case is a geometric series. In particular, the displayed formulas imply the exact vector identity \(T_0g=g\).

The binary expansion of \(2^k-1\) consists of \(k\) ones. Therefore
\[
G_k(z)=e_{s_0}^{\mathsf T}T_1(z)^k g(z).
\]

**Step 3: finite algebraic certificate.** Put \(w=(T_1-I)g\). Every entry of \(g\) and \(w\) is a Laurent polynomial divided by the common denominator \(2z-1\). Direct multiplication in the eight-state ring \(\mathbb Q[z,z^{-1},(2z-1)^{-1}]\) gives the three identities
\[
\begin{aligned}
(T_1^4-\tfrac z2 T_1^3)w&=0,\\
e_{s_0}^{\mathsf T}T_1^4w&=\frac{(z-1)^2(z+1)(2z^2+z+2)}{128},\\
e_{s_0}^{\mathsf T}T_1^4g&=\frac{(z+1)(4z^4+11z^2+10z+7)}{64(2z-1)}.
\end{aligned}
\]
These are *finite exact identities*, reproduced coefficient by coefficient, without floating-point operations, by the bundled `verify.py`. The program independently builds the transitions from the digit definitions and tests each identity over Laurent polynomials with rational coefficients. No unproved asymptotic or numerical extrapolation is used.

By the first identity, \(T_1^{k+1}w=(z/2)T_1^kw\) for every \(k\ge3\). Since \(G_{k+1}-G_k=e_{s_0}^{\mathsf T}T_1^k w\), the second identity gives the claimed increment for every \(k\ge4\). The third gives \(G_4\).

**Step 4: coefficient extraction and sharpness.** The difference \(G_{k+1}-G_k\) is a polynomial in nonnegative powers of \(z\); hence every coefficient of a negative power is independent of \(k\) once \(k\ge4\). For \(|z|>1/2\),
\[
\frac1{2z-1}=\sum_{h\ge1}2^{-h}z^{-h}.
\]
For \(j\ge1\), the coefficient of \(z^{-j}\) in \(G_4\) is the value of its numerator polynomial at \(z=1/2\), divided by \(64\cdot2^j\); the numerator evaluates to \(45/2\). This yields \(\mu_k(-j)=45/(128\cdot2^j)\). The total negative mass is \(45/128\), and normalization at \(z=1\) gives the complementary nonnegative mass \(83/128\). Exact extraction for \(k=1,2,3\), also checked by `verify.py`, gives \(13/16,47/64,87/128\) and proves sharpness.

## Verification

Run `python3 verify.py` (Python standard library only). The program independently constructs the eight-state matrices, represents each rational generating function by its Laurent-polynomial numerator over the denominator \(2z-1\), and checks every matrix and polynomial identity above exactly with `fractions.Fraction`. It also computes the sharp initial nonnegative probabilities and tests all \(524288\) integers in a dyadic interval for each of eight shifts as a separate, non-proving consistency check.

Expected success output:

`VERIFY_OK states=8 zero_suffix=invariant polynomial_identity=exact G4=exact recurrence=exact sharp_thresholds=1..4 negative_tail=45/(128*2^j) finite_integer_samples=8x524288`

The finite integer enumeration is not an infinite proof; the infinite parameter \(k\) is covered by the proved vector identity and induction, and the natural density exists by the carry-tail argument.

## Relationship to prior work

Sobolewski and Spiegelhofer, *Block occurrences in the binary expansion* (arXiv:2309.00142, first public 2023-08-31), define these exact difference distributions and ask whether their nonnegative masses exceed one half for every shift. Their Section 2 establishes a Gaussian approximation under a large *number of separate one-blocks*, and Proposition 3.2 gives general recurrences for fixed shifts; the present one-block Mersenne family has exactly one contiguous one-block and is not settled by that asymptotic theorem. The new statements are the stable full negative tail, sharp length threshold, and exact constant bias along an infinite family, proved from the structural rank-one transfer identity.

Sobolewski, *On monochromatic arithmetic progressions in binary words associated with block-counting functions* (arXiv:2204.05287), determines maximal constant-parity progression lengths for differences including \(2^k-1\); those statements concern \(r(nd)\bmod2\), not the probability law of \(r(n+d)-r(n)\). Sobolewski, *On the behavior of binary block-counting functions under addition* (arXiv:2412.15851), announces a general Gaussian approximation for shifts with many separate one-blocks, not this one-block exact law, although only its accessible abstract was inspected in this comparison. A previously recorded exact distribution for the distinct two-one-bit shifts \(2^a+1\) is likewise not a theorem for the present \(2^k-1\) family.

## Limitations

The exact law here is specific to overlapping `11` and to Mersenne shifts, not to arbitrary binary words or arbitrary shifts. While the negative half of the distribution stabilizes, the complete generating function does not. An unindexed equivalent result is a residual originality risk; the separate 2024 manuscript was assessed from its abstract rather than full text. Independent mathematical validation has not been carried out.

## References

1. B. Sobolewski and L. Spiegelhofer, *Block occurrences in the binary expansion*, arXiv:2309.00142 (public 2023-08-31), https://arxiv.org/abs/2309.00142.
2. B. Sobolewski, *On monochromatic arithmetic progressions in binary words associated with block-counting functions*, arXiv:2204.05287 (2022), https://arxiv.org/abs/2204.05287.
3. B. Sobolewski, *On the behavior of binary block-counting functions under addition*, arXiv:2412.15851 (public 2024-12-20), https://arxiv.org/abs/2412.15851.
