# A lossless golden-mean restriction of elementary Rule 28 with an exact forbidden-block image

## Finding

Write \(X\) for the two-sided binary shift avoiding the adjacent block `11`, and \(Y\) for the two-sided binary shift avoiding both `111` and `0100`. Let \(F\) be synchronous elementary cellular automaton Rule 28, with \(F(x)_i=1\) exactly when \((x_{i-1},x_i,x_{i+1})\) is `010`, `011`, or `100`. Then the restriction \(F|_X:X\to Y\) is a shift-commuting homeomorphism onto \(Y\), with a two-site local inverse

\[
(F|_X)^{-1}(y)_i=y_i(1-y_{i-1}).
\]

For every indexed cyclic binary ring of length \(n\ge1\), including rings where neighborhood indices coincide, let \(X_n\) be the ring words avoiding cyclic `11` and let \(Y_n\) be the ring words avoiding cyclic `111` and `0100` (the factors are tested with wraparound, even when their length exceeds \(n\)). Then \(F_n:X_n\to Y_n\) is a bijection with the same inverse. In particular, each allowed output has exactly one hard-core predecessor and each other output has none. The exact attainable-output count is

\[
|Y_n|=|X_n|=L_n,
\]

where \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\) are Lucas numbers. The image shift has periodic-point zeta function

\[
\zeta_Y(z)=\exp\left(\sum_{n\ge1}\frac{|Y_n|z^n}{n}\right)=\frac1{1-z-z^2}.
\]

The pair of forbidden blocks is irredundant as a presentation: both `111` and `0100` are minimal forbidden factors of \(Y\).

## Assumptions and scope

Input and output are binary, indexed, and updated synchronously. Neighborhood entries follow the standard Rule 28 truth table (Wolfram convention). In finite rings all index arithmetic is modulo \(n\), including length-one and length-two rings. `11`, `111`, and `0100` denote *contiguous* factors, never scattered subsequences. For the two-sided shift, indices range over all integers and the product topology is used. The map need not send \(X\) into \(X\); it is a conjugacy between \(X\) and the distinct shift \(Y\), not a claim that unrestricted Rule 28 is invertible.

## Proof

**1. Exact local rule on admissible inputs.** Since `11` cannot occur in \(X\), its only three-site neighborhoods are `000`, `001`, `010`, `100`, and `101`. Rule 28 maps exactly `010` and `100` to one in this list. Thus for every \(x\in X\),

\[
F(x)_i=x_i\ \lor\ [x_{i-1}=1\text{ and }x_{i+1}=0].
\]

An output one can therefore come only from a source one at its own site (the `010` case) or from a source one immediately to its left (the `100` case). In the first case the preceding output is zero: the preceding neighborhood is either `001` or `101`, both mapped to zero. In the second case the preceding output is one, because the preceding neighborhood is `010`. Consequently, with \(y=F(x)\),

\[
x_i=y_i(1-y_{i-1})\quad\text{for every index }i.
\]

This proves injectivity and the claimed local left inverse. The argument is valid on every cyclic ring, including lengths one and two, because it uses only the allowed neighborhoods and their values.

**2. The two image obstructions.** If an output has three consecutive ones, the first and third (or the first and second) would require inconsistent placements of the isolated source ones under the two cases in Step 1. More explicitly, the inverse formula selects the beginnings of maximal one-runs of \(y\); a source one creates at most two consecutive output ones, and there is always an output zero between successive such groups. Hence `111` is forbidden. Also, if \(y_{i-2}y_{i-1}y_iy_{i+1}=0100\), then \(y_{i-1}=1,y_{i-2}=0\) forces \(x_{i-1}=1\). Since both \(y_i=0\) and \(y_{i+1}=0\), the inverse formula yields \(x_{i+1}=0\), so the source neighborhood at site \(i\) must be `100` and \(F(x)_i=1\), a contradiction. Thus \(F(X)\subseteq Y\).

**3. Every avoiding word has a preimage.** Conversely, take any \(y\in Y\) and define \(x_i=y_i(1-y_{i-1})\). If \(x_i=1\), then \(y_i=1\) and \(y_{i-1}=0\), which makes \(x_{i+1}=0\). Thus \(x\in X\).

If \(y_i=1\) and \(y_{i-1}=0\), then \(x_i=1\), and its source neighborhood is `010`, so \(F(x)_i=1\). If \(y_i=y_{i-1}=1\), avoidance of `111` gives \(y_{i-2}=0\), hence \(x_{i-1}=1\), while \(x_{i+1}=0\); the source neighborhood is `100` and the output is again one. If \(y_i=0\), then \(x_i=0\). A source neighborhood could produce a spurious one only if \(x_{i-1}=1\) and \(x_{i+1}=0\). But \(x_{i-1}=1\) says \(y_{i-2}y_{i-1}=01\); the forbidden `0100` then forces \(y_{i+1}=1\), so \(x_{i+1}=1\), contradiction. Therefore \(F(x)_i=y_i\) in all cases. The inverse is a sliding-block map, and \(F\) is a sliding-block map, so their restrictions are inverse homeomorphisms commuting with the shift. All arguments are coordinate-local and also apply to cyclic words at every \(n\ge1\).

**4. Periodic-point counts and irredundancy.** The golden-mean shift is represented by the adjacency matrix \(A=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\). Its number of indexed length-\(n\) periodic points is \(\operatorname{tr}(A^n)=L_n\). The bijection transfers the count to \(Y_n\). Using \(\exp(\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n)=1/\det(I-zA)\) gives the displayed zeta function. Finally, `11` occurs in \(Y\) (for instance in \((1100)^\mathbb Z\)), and both `010` (in \((01)^\mathbb Z\)) and `100` (in \((1100)^\mathbb Z\)) occur. These cover all proper contiguous subfactors of `111` and `0100`, so neither forbidden block is redundant or contains a shorter absent subfactor.

## Verification

The self-contained `verify_rule28.py` evaluates Rule 28 from its original eight-neighborhood truth table. It exhaustively compares the actual image of all cyclic `11`-avoiding inputs with the proposed cyclic `111`/`0100` avoidance condition for every \(1\le n\le15\), verifies injectivity and the two-site decoding identity, and independently checks the Lucas counts. It also enumerates all five-bit local contexts respecting the two output obstructions and verifies the inverse reconstruction at the central site. Invoke `python3 verify_rule28.py`; the success message begins `VERIFY_OK`. These experiments corroborate the local proof, which alone establishes the statements for all lengths.

## Relationship to prior work

Salo's work on von Neumann regularity of cellular automata (arXiv:1804.03913; extended arXiv:2209.13373) establishes that unrestricted Rule 28 is non-regular, determines its full-shift image by avoiding `111`, and treats same-period preimages. In particular, the expanded paper discusses a *flipped* golden-mean shift as a tool for a periodic-preimage section. That is not the source-restricted map \(F|_X\) proved bijective here, nor does it characterize its image by also forbidding `0100`.

The published published-finding corpus result “Sharp Lucas inverse-fiber law and output classification for cyclic Rule 28” (2026/11/8, item 8fa574301e73) gives unrestricted indexed cyclic predecessor multiplicities via a two-matrix trace product and classifies worst-case fibers. Its unrestricted fibers are not the hard-core restricted fibers considered here; in particular, the present theorem gives a two-site inverse and an image SFT rather than an unrestricted maximum. Neither source, in the portions actually inspected, states the source-restricted conjugacy or its two-pattern forbidden presentation. Standard recoding and transfer-matrix principles are used; a prior equivalent recoding could exist under different notation.

## Limitations

There is no claim that Rule 28 is bijective on all binary configurations, or that it acts as a cellular automaton from the golden-mean shift to itself. The image has a different local constraint, and unique reconstruction holds only for inputs with cyclic or bi-infinite `11` avoidance. The Lucas counts are classical for the source shift; the asserted new object is the explicit constrained Rule-28 image identification and local conjugacy, not a new Lucas enumeration. Literature comparisons are non-exhaustive; an earlier equivalent symbolic-dynamics recoding remains a possibility. No independent mathematical audit has been performed.

## References

1. V. Salo, “Von Neumann regularity, split epicness and elementary cellular automata,” arXiv:1804.03913 (first public 2018-04-11). https://arxiv.org/abs/1804.03913
2. V. Salo, “On von Neumann regularity of cellular automata,” arXiv:2209.13373 (2022-09-27); *Natural Computing* **22** (2023), 527–538. https://doi.org/10.1007/s11047-022-09935-w
3. “Sharp Lucas inverse-fiber law and output classification for cyclic Rule 28,” published-finding corpus, record 2026/11/8/SCOPE-sharp-lucas-inverse-fiber-law-and-output-classification-for-cycl--8fa574301e73. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-lucas-inverse-fiber-law-and-output-classification-for-cycl--8fa574301e73
