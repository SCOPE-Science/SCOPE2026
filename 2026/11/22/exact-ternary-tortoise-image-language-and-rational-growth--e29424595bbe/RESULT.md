# Exact ternary tortoise-image language and rational growth

## Finding

Let \(\mathsf T\) be the Defant–Kravitz tortoise stack-sorting map, acting on words over the ordered alphabet \(\{0,1,2\}\), and let \(\mathcal I=\{\mathsf T(w):w\in\{0,1,2\}^*\}\). Put
\[
\mathcal B=0^*\ \cup\ \{0,1\}^*1.
\]
Then the image language has the exact *unambiguous-by-maximal-letter* description
\[
\boxed{\mathcal I=\mathcal B\ \cup\ \{0,1\}^*2(\mathcal B2)^*.}
\]
Here a star denotes Kleene closure, not arithmetic multiplication. In particular, with \(a_n=|\mathcal I\cap\{0,1,2\}^n|\),
\[
\boxed{\sum_{n\ge0}a_nz^n
=\frac{1-4z+2z^2+7z^3-6z^4-z^5}
{(1-z)(1-2z)(1-4z+3z^2+z^3)}.}
\]
The initial values \(a_0,\ldots,a_{10}\) are \(1,3,6,14,35,91,242,653,1780,4888,13496\). Its exponential growth rate is the largest real root \(\lambda\approx2.8019377358\) of \(\lambda^3-4\lambda^2+3\lambda+1=0\).

## Assumptions and scope

Words are finite, including the empty word. Alphabet order is fixed as \(0<1<2\). The map pops the stack whenever the current input symbol is at least the stack top, then pushes the current symbol; when the input ends it pops the remaining stack. No reversal, relabeling, or alternative equal-symbol convention is used. The claim concerns one pass and **every** word length, not only bounded lengths or selected Parikh vectors. Counts concern distinct output words, not the number of inputs or their multiplicities.

## Proof

For any maximum letter \(m\) occurring \(r\ge1\) times, the Defant–Kravitz recursion writes an input uniquely as \(A_0mA_1m\cdots mA_r\), with every \(A_i\) over smaller letters, and gives
\[
\mathsf T(A_0m\cdots mA_r)
=\mathsf T(A_0)\mathsf T(A_1)m\mathsf T(A_2)m\cdots\mathsf T(A_r)m.
\]
This identity follows directly by inspecting the stack: each new maximum forces any previous copy of that maximum from the stack, and the intervening strictly smaller blocks are processed recursively. It includes empty blocks and \(r=1\).

First take the binary alphabet \(\{0,1\}\). If an input contains no one, its image is a block of zeros. Otherwise the displayed recursion has at least one maximum, so its image ends in one. Conversely, any binary word ending in one can be produced: write it \(u1\), split \(u\) at the last one (or into an empty prefix and a zeros-only suffix if there is none), and use the recursion. More directly, with \(r\) ones the input zero-gap vector \((g_0,\ldots,g_r)\) transforms to \((g_0+g_1,g_2,\ldots,g_r,0)\). Thus the binary image language is exactly \(\mathcal B\). It includes the empty word. Crucially,
\[
\mathcal B\mathcal B=\{0,1\}^*:
\]
for any binary word, split after its last one, leaving a prefix ending in one and a suffix of zeros; the all-zero case has an empty prefix.

Now take a ternary input containing at least one two. The maximum-letter recursion shows that its image is \(\mathsf T(A_0)\mathsf T(A_1)2\) followed by zero or more blocks \(\mathsf T(A_i)2\). Every \(\mathsf T(A_i)\) lies in \(\mathcal B\). The first two factors range over all binary words because \(\mathcal B^2=\{0,1\}^*\); conversely every choice of the displayed factors has a preimage, by choosing independent binary preimages for its blocks and inserting twos. Words with no two have exactly the binary image language \(\mathcal B\). This proves the exact language identity.

The two cases (no two / at least one two) are disjoint. In the second case the locations of the two symbols fix the decomposition uniquely, so ordinary generating functions may be multiplied without counting a word twice. The generating function for \(\mathcal B\) is
\[
B(z)=\frac{1}{1-z}+\frac{z}{1-2z}.
\]
An arbitrary binary prefix contributes \((1-2z)^{-1}\); the first two contributes \(z\); subsequent \(\mathcal B2\) blocks give \((1-zB(z))^{-1}\). Therefore
\[
F(z)=B(z)+\frac{z}{(1-2z)(1-zB(z))},
\]
which simplifies by exact rational arithmetic to the boxed formula. The denominator has simple zeros at \(1\), \(1/2\), and the three reciprocals of the roots of \(x^3-4x^2+3x+1\). Its unique smallest-modulus zero is the positive reciprocal of the largest real root, approximately \(0.3568958679\); the numerator is nonzero there. Standard rational-function coefficient extraction gives the stated dominant exponential rate.

## Verification

The self-contained standard-library programs `verification/exhaustive.py` and `verification/series.py` provide separate checks. The first implements the stack and the maximum-letter recursive definition independently, proves their agreement by exhaustive comparison at every ternary input through length nine, and checks language membership of every ternary word through that length against the computed image sets. The second independently uses integer coefficient recurrences for \(B(z)\) and \((1-zB(z))^{-1}\), verifies the first eleven counts, and checks the exact rational polynomial identity through degree forty. These computations support, but are not substitutes for, the unrestricted proof above. Run with `python3 verification/exhaustive.py` and `python3 verification/series.py` from the package root.

## Relationship to prior work

Defant and Kravitz (2018) introduced the tortoise recursion and a general valid-hook-configuration method for per-word fertility. Campbell and Rampersad (first public version April 28, 2026) introduced \(k\)-tortoise complexity and explicitly analyzed the binary operation on automatic sequences. Their published source establishes the binary first-one movement used as context, but it does not state the ternary full-image language or its length enumerator. The present result isolates a complete nonbinary output language and its rational cardinality series. This is an explicit language-level and aggregate-count claim, not a claim to have invented tortoise sorting or general per-target fertility computations.

## Limitations

The explicit rational coefficient formula is proved for the fixed three-letter ordered alphabet and one tortoise pass. The maximum-letter recursion gives regularity recursively over any fixed finite alphabet, but no closed counting formula for alphabets of size four or greater is claimed. Equivalent results in unindexed literature remain possible. No independent mathematical audit has been performed.

## References

1. C. Defant and N. Kravitz, *Stack-sorting for Words*, arXiv:1809.09158, first public September 24, 2018, https://arxiv.org/abs/1809.09158.
2. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first public April 28, 2026, https://arxiv.org/abs/2604.25811.
