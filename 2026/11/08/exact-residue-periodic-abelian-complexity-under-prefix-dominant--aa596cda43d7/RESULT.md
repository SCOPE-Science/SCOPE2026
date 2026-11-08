# Exact residue-periodic abelian complexity under prefix-dominant Parikh-constant binary substitutions

## Finding

Let \(\varphi:\{0,1\}^*\to\{0,1\}^*\) be a uniform morphism with image length \(b\ge2\), such that the two images \(u=\varphi(0)\) and \(v=\varphi(1)\) both have exactly \(c\) occurrences of \(1\), with \(1\le c<b\). Write \(P_z(t)\) for the number of ones in the prefix of length \(t\) of a finite word \(z\). Assume

\[
P_u(t)\le P_v(t)\qquad (0\le t\le b).
\]

Suppose \(\varphi\) has an **aperiodic** one-sided fixed point \(\mathbf x=x_0x_1\cdots\), and let \(\mathsf a_{\mathbf x}(n)\) denote its abelian complexity, namely the number of different Parikh vectors among all length-\(n\) factors. Define for \(0\le r<b\)

\[
\begin{split}
L_r&=\min_{0\le s<b}\left(c\left\lfloor\frac{s+r}{b}\right\rfloor+P_u((s+r)\bmod b)-P_v(s)\right),\\
U_r&=\max_{0\le s<b}\left(c\left\lfloor\frac{s+r}{b}\right\rfloor+P_v((s+r)\bmod b)-P_u(s)\right).
\end{split}
\]

**Theorem.** For every integer \(m\ge1\) and every \(0\le r<b\), the numbers of ones in length-\(bm+r\) factors of \(\mathbf x\) are **exactly** the integers from \(mc+L_r\) to \(mc+U_r\), inclusive. Consequently,

\[
\boxed{\mathsf a_{\mathbf x}(bm+r)=U_r-L_r+1\quad(m\ge1,\ 0\le r<b).}
\]

Thus the abelian complexity is periodic from length \(b\) onward, with period dividing \(b\), and its complete eventual period is computable by finitely many image-prefix counts. In particular, with \(\Delta=\max_{0\le s<b}(P_v(s)-P_u(s))\),

\[
\mathsf a_{\mathbf x}(bm)=2\Delta+1\qquad(m\ge1).
\]

A nontrivial explicit infinite family satisfying every assumption is

\[
\varphi_{p,q}(0)=0^p1^q,\qquad\varphi_{p,q}(1)=1^q0^p\qquad(p,q\ge1).
\]

For its fixed point beginning in \(0\), which is aperiodic for every such pair, the abelian complexity at multiples of \(p+q\) is \(2\min(p,q)+1\), and the full residue spectrum follows from the formula. For \((p,q)=(2,2)\), the values at lengths \(4m,4m+1,4m+2,4m+3\), for \(m\ge1\), are respectively \(5,4,3,4\).

## Assumptions and scope

A *factor* is any contiguous finite word appearing in the one-sided infinite sequence, at any position. Binary factors are abelian-equivalent exactly when they have the same number of ones. A morphism is *prolongable* on \(a\) when its image starts with \(a\) and its iterates grow without bound; this ensures the existence of the corresponding one-sided fixed point. *Aperiodic* means that no positive integer is a period of the entire infinite sequence (not merely that the sequence has infinitely many distinct letters). The theorem assumes a fixed point and aperiodicity explicitly; it does not assert that every prefix-dominant Parikh-constant substitution is aperiodic.

The relevant input data consist only of the two length-\(b\) image words and the prefix dominance inequalities. All quantifiers in the theorem range over arbitrary \(m\ge1\) and all residues \(r\in\{0,\ldots,b-1\}\). No conclusion is claimed about factor lengths below \(b\), nor about larger alphabets or nonuniform substitutions.

## Proof

**1. Uniform recurrence and ordered pairs at every distance.** Since both images contain both binary letters, each second iterate \(\varphi^2(a)\) contains both first-iterate images. More generally, if a finite factor \(F\) of the fixed point occurs in \(\varphi^k(a)\) for some letter \(a\), it occurs in each \(\varphi^{k+1}(0)\) and \(\varphi^{k+1}(1)\). The fixed-point decomposition into consecutive blocks of length \(b^{k+1}\) then gives a bounded gap between occurrences of \(F\). Thus every finite factor occurs with bounded gaps.

Fix \(d\ge1\). If \(x_i=x_{i+d}\) for all \(i\), the sequence is periodic, contrary to hypothesis. Hence at least one mismatch pair at distance \(d\) exists. Suppose only the pair \((0,1)\) occurs, but no \((1,0)\). The differences \(x_{i+d}-x_i\) are nonnegative and positive at a set of positions with bounded gaps, by uniform recurrence of the length-\(d+1\) factor realizing the mismatch. Their partial sums therefore tend to infinity. On the other hand,

\[
\sum_{i=0}^{N-1}(x_{i+d}-x_i)
=\sum_{i=N}^{N+d-1}x_i-\sum_{i=0}^{d-1}x_i
\]

is bounded in absolute value by \(d\), a contradiction. Reversing the symbols handles the case with only \((1,0)\). **Both ordered pairs \((0,1)\) and \((1,0)\) consequently occur at distance \(d\), for every positive \(d\).**

**2. Exact boundary decomposition.** Fix a length \(n=bm+r\) with \(m\ge1\), \(0\le r<b\), and any starting offset \(s\in\{0,\ldots,b-1\}\) inside an image block. Let \(e=\lfloor(s+r)/b\rfloor\) and \(t=(s+r)\bmod b\). A length-\(n\) factor beginning at offset \(s\) in \(\varphi(x_i)\) consists of the last \(b-s\) letters of that block, followed by \(m+e-1\) complete image blocks, and finally the first \(t\) letters of \(\varphi(x_{i+m+e})\). A zero-length initial or terminal piece is allowed. Each complete block contains exactly \(c\) ones. Hence its number of ones is precisely

\[
mc+ce-P_{\varphi(x_i)}(s)+P_{\varphi(x_{i+m+e})}(t).
\]

Because \(m+e\ge1\), the ordered-pair lemma from step 1 guarantees an occurrence of \((x_i,x_{i+m+e})=(0,1)\) and of \((1,0)\), for **every** fixed offset \(s\). Prefix dominance makes \((0,1)\) the pair attaining the largest possible boundary correction for that offset, and \((1,0)\) the pair attaining the smallest. Maximizing and minimizing across all \(s\) therefore yield exactly \(mc+U_r\) and \(mc+L_r\) as the global extremes. This proves **attainability**, not merely inequalities, of both endpoints.

**3. No gaps in the spectrum.** Let \(C_i(n)=\sum_{j=0}^{n-1}x_{i+j}\). Consecutive windows satisfy \(C_{i+1}(n)-C_i(n)=x_{i+n}-x_i\in\{-1,0,1\}\). Choose positions realizing the minimum and maximum from step 2 and slide between them. Every integer between the extreme values is assumed. Since a binary Parikh vector of length \(n\) is uniquely determined by its number of ones, the cardinality is \(U_r-L_r+1\).

For \(r=0\), one has \(e=0\), \(t=s\), and the definitions reduce to \(U_0=\max_s(P_v(s)-P_u(s))=\Delta\) and \(L_0=-\Delta\), proving the special formula.

**4. The explicit family really is aperiodic.** For \(\varphi_{p,q}\), the image of \(0\) begins in \(0\), so its fixed point exists. Both images contain both symbols and their common one-count is \(q\). The prefix inequalities are immediate: \(P_{0^p1^q}(t)=\max(0,t-p)\le\min(t,q)=P_{1^q0^p}(t)\). Thus \(\Delta=\min(p,q)\).

It remains to verify aperiodicity rather than assuming it. Let \(f_r(a)\) be the symbol in offset \(r\) of \(\varphi_{p,q}(a)\). For \(r<\min(p,q)\), \(f_r\) is the identity map on the letters; for \(\min(p,q)\le r<\max(p,q)\), it is a constant map; and for \(r\ge\max(p,q)\), it complements the letter. If the fixed point had least period \(d\ge1\), write \(d=(p+q)t+r\) with \(0\le r<p+q\). Since the first image symbol is always its input letter, \(x_{(p+q)i}=x_i\). Periodicity would give \(x_i=f_r(x_{i+t})\) for every \(i\). In the constant-map case the fixed point would be constant, impossible. In the complement case, \(t=0\) is impossible and \(t\ge1\) would give the strictly smaller period \(2t<d\). In the identity-map case, \(t\ge1\) gives the smaller period \(t<d\). If \(t=0\), then \(1\le d=r<\min(p,q)\); but the fixed point contains a run of at least \(d\) zeros and a run of at least \(d\) ones, impossible for a nonconstant period-\(d\) word. Every case contradicts the existence of a least positive period. This completes the proof.

## Verification

The file `verify.py` independently constructs each tested fixed-point prefix, enumerates length-specific sliding-window one-count spectra, and compares the observed minimum, maximum and number of attained counts with the closed formulas. It checks all \(49\) parameters \(1\le p,q\le7\), with eight multiples and every residue per parameter pair, as well as \(365\) additional sampled prefix-dominant image pairs of lengths two through six. The latter sample filters apparent low periods in finite prefixes but **does not certify the infinite aperiodicity hypothesis**. `verification_results.txt` records the successful counts. The proof above, not this finite test, establishes the theorem for all admissible parameters and lengths.

## Relationship to prior work

Rigo, Stipulanti and Whiteland (2024) prove that fixed points of arbitrary Parikh-collinear morphisms have *automatic* abelian-complexity functions and supply an automaton-construction procedure. Their conclusion explicitly asks whether all Parikh-constant fixed points have ultimately periodic abelian complexity. The present theorem supplies a positive answer for the explicitly specified aperiodic binary prefix-dominant class and determines its actual residue-periodic values. Automaticity by itself does not imply periodicity, nor does it supply these extrema.

Their 2023 paper proves automaticity under earlier hypotheses and exhibits an aperiodic complexity for a morphism whose two image Parikh vectors are not equal. That example does not meet the present assumptions. Guo, Lü and Wen (2022) study automatic boundary sequences and obtain automaticity of abelian complexity in a related class; the known abstract does not establish this exact residue formula. This literature comparison does not assert an exhaustive proof of global novelty.

## Limitations

The statement concerns ordinary abelian complexity of one-sided **binary** aperiodic fixed points of uniform **Parikh-constant** substitutions satisfying pointwise prefix dominance; removing any of these restrictions is not established. The minimal period of the complexity may be a proper divisor of \(b\). Nothing is asserted for \(1\le n<b\). Finite program output is only a consistency check and is not an independent mathematical proof. The literature comparison may miss an equivalent unindexed theorem, and independent external audit has not been performed.

## References

1. M. Rigo, M. Stipulanti and M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, arXiv:2405.18032, first public 2024-05-28; Theory of Computing Systems 68 (2024), 1622–1639, https://doi.org/10.1007/s00224-024-10197-5. Full open-access publisher text, especially Theorem 3 and §6.
2. M. Rigo, M. Stipulanti and M. A. Whiteland, *Automaticity and Parikh-collinear Morphisms*, Combinatorics on Words (2023), pp. 247–260, https://doi.org/10.1007/978-3-031-33180-0_19; lawful open manuscript https://orbi.uliege.be/handle/2268/302523.
3. Y. Guo, X.-T. Lü and Z.-X. Wen, *On the boundary sequence of an automatic sequence*, Discrete Mathematics 345 (2022), 112632, https://doi.org/10.1016/j.disc.2021.112632.
