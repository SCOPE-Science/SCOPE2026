# Six stable dyadic cycles of the first translated quadratic binomial map

## Finding
Let \(F:\mathbb Z\to\mathbb Z\) be the shifted second Pascal-column map
\[
F(x)=\binom{2x+4}{2}=(x+2)(2x+3)=2x^2+7x+6,
\]
extended by the same integer polynomial to \(\mathbb Z_2\). For each integer \(k\ge1\), the induced map on \(\mathbb Z/2^k\mathbb Z\) is a permutation. For any starting residue \(x\), its exact least orbit period is
\[
T_k(x)=\begin{cases}
1,&k=1,\\
2^{1+\max(k-3,0)},&k\ge2\ \text{and }x\text{ even},\\
2^{1+\max(k-4,0)},&k\ge2\ \text{and }x\text{ odd}.
\end{cases}
\]
In particular, **at every precision \(k\ge4\)** there are exactly **six cycles**: precisely two cycles of length \(2^{k-2}\), consisting entirely of even residues, and four cycles of length \(2^{k-3}\), consisting entirely of odd residues. At precisions \(k=1,2,3\), the counts of cycles are respectively \(2,2,4\).

## Assumptions and scope
The binomial expression is evaluated at nonnegative indices when \(x\ge0\), but the polynomial extension defines the same map on all integers and on \(\mathbb Z_2\). All cycle counts refer to the complete residue ring modulo \(2^k\), not a selected orbit or a finite sample. A cycle has its usual least positive period; the parity of an orbit is constant. The theorem concerns this specified *first translated* second-column map, not all integer shifts or all binomial columns.

## Proof
**1. Compatibility, bijectivity, and parity.** The polynomial has integer coefficients, so congruent arguments modulo \(2^k\) have congruent images. Its derivative is \(F'(x)=4x+7\), which is odd. For any \(x\ne y\) in \(\mathbb Z_2\), the divided difference is
\[
\frac{F(x)-F(y)}{x-y}=2(x+y)+7,
\]
an odd \(2\)-adic unit. Thus \(\nu_2(F(x)-F(y))=\nu_2(x-y)\): every reduction is a bijection, and \(F(x)\equiv x\pmod2\). The first displacement factors as
\[
F(x)-x=2(x^2+3x+3).
\]
Since \(x^2+3x+3\) is odd for every integer \(x\), \(\nu_2(F(x)-x)=1\), so no residue is fixed modulo \(2^k\) when \(k\ge2\).

**2. Exact two-step displacement.** Put \(G=F\circ F\). Direct polynomial expansion gives the exact identity
\[
G(x)-x=8(x^2+3x+3)(x^2+4x+5).
\]
The first factor is always odd. The second is odd for even \(x\); for odd \(x\), its residue modulo eight is \(1+4+5\equiv2\pmod8\). Consequently, without exceptions,
\[
\nu_2(G(x)-x)=\begin{cases}3,&x\text{ even},\\4,&x\text{ odd}.\end{cases}
\]
Moreover \(G'(x)=F'(F(x))F'(x)\equiv3\cdot3\equiv1\pmod4\) for every \(x\).

**3. An exact lifting lemma.** Suppose \(g\in\mathbb Z_2[x]\) satisfies \(g'(z)\equiv1\pmod4\) for every \(z\in\mathbb Z_2\), and at a given \(z\) has \(\nu_2(g(z)-z)=s\ge2\). Then
\[
\nu_2(g^{\circ2^j}(z)-z)=s+j\quad(j\ge0).
\]
Indeed, if \(H=g^{\circ2^j}\), the chain rule gives \(H'(z)\equiv1\pmod4\). Write \(H(z)=z+2^{s+j}u\) with odd \(u\). Taylor's polynomial identity, whose quadratic and higher remainder terms have valuation at least \(2(s+j)\ge s+j+2\), yields
\[
H(H(z))-z\equiv 2^{s+j}u(1+H'(z))\equiv2^{s+j+1}\pmod{2^{s+j+2}}.
\]
This proves the induction. As \(g^{\circ 2^{k-s}}(z)\equiv z\pmod{2^k}\) for \(k>s\) but the preceding half-iterate does not return, the least period modulo \(2^k\) is exactly \(2^{\max(k-s,0)}\). The same conclusion for \(k\le s\) follows because \(g(z)\equiv z\pmod{2^k}\).

**4. Exact periods and numbers of cycles.** Apply the lemma to \(g=G\). On even inputs its displacement valuation is \(s=3\), and on odd inputs \(s=4\). Thus the least period under \(G\) is respectively \(2^{\max(k-3,0)}\) and \(2^{\max(k-4,0)}\). For \(k\ge2\), no \(F\)-orbit has odd length: if an odd power of \(F\) were the identity at a residue, its induced parity-preserving orbit length would be odd, whereas \(F(x)-x\) has exact valuation one and \(F^{\circ 2^j}(x)\) can return only after an even number of steps (alternatively, \(F\pmod4\) is the swap on each parity class). Hence the \(F\)-period is twice the \(G\)-period. At \(k=1\), \(F\) is the identity.

Each parity class contains \(2^{k-1}\) residues, and the period is constant within that class. Dividing class cardinality by period yields the asserted number of cycles. For \(k\ge4\), these quotients are exactly two even cycles and four odd cycles. This proves the complete census.

## Verification
The standalone `verify.py` checks the integer polynomial identity, both exact displacement valuations, every least point period and the complete parity-resolved cycle decomposition for \(1\le k\le12\). The algebraic lifting argument above, not finite enumeration, proves the theorem for unbounded \(k\). Run `python3 verify.py` in a standard Python 3 environment.

## Relationship to prior work
Sun and Zhang, *Binomial coefficients and the ring of p-adic integers* (arXiv:0812.3089, Theorem 1.1), show congruence-image surjectivity on canonical prime-power index progressions. Their result does not address the periodic *iteration* of the shifted map above. Anashin, *Non-Archimedean Ergodic Theory and Pseudorandom Generators* (arXiv:0710.1418, Sections 3–4), gives general criteria for measure preservation and single-cycle ergodicity. The present map is isometric but **not ergodic**, and those criteria do not give the exact six-cycle, parity-dependent period census. The nearby published fifth-binomial-column fiber law concerns output multiplicities, not iteration cycle lengths. The first translated quadratic binomial polynomial is studied here because a one-step translation of the canonical binomial progression produces a sharp split from transitivity into two different parity clocks.

## Limitations
No assertion is made about all shifts of the second column or higher binomial columns. The finding concerns an exact but particular classical arithmetic map, and its mathematical value is the complete parity-resolved dynamical classification. A prior classification in general quadratic polynomial dynamics might imply this special case; accessible searches did not identify an explicit equivalent. The analysis is self-reviewed, not independently audited.

## References
- V. Anashin, *Non-Archimedean Ergodic Theory and Pseudorandom Generators*, arXiv:0710.1418, first public 2007-10-07, https://arxiv.org/abs/0710.1418 .
- Z.-W. Sun and W. Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089, first public 2008-12-16, https://arxiv.org/html/0812.3089v5 .
- *Exact three-level 2-adic fibers of the fifth binomial column*, published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-three-level-2-adic-fibers-of-the-fifth-binomial-column--68ab08bc975b/RESULT.md .
