# Exact Lie classes and logarithmic Abelian divergence in geometric-marker automatic words

## Finding
For an integer base \(B\ge2\), let the binary right-infinite word \(w_B\) be indexed from zero and satisfy \(w_B(i)=1\) if and only if \(i=B^j\) for an integer \(j\ge0\). Let \(\operatorname{Fac}_B(n)\) be its distinct contiguous length-\(n\) factors. Write \([v]_{\mathrm{cyc}}\) for all cyclic rotations of a finite word \(v\). Define the Lie complexity \(L_B(n)\) as the number of distinct classes \([v]_{\mathrm{cyc}}\subseteq\operatorname{Fac}_B(n)\), and the Abelian complexity \(A_B(n)\) as the number of distinct weights \(|v|_1\) among \(v\in\operatorname{Fac}_B(n)\).

**Theorem.** For all integers \(B\ge2\) and \(n\ge1\), the rotation-complete conjugacy classes are exactly those of \(0^n\) and \(10^{n-1}\), together with one additional two-marker class precisely for \((B,n)=(2,2),(2,3),(3,4)\). These additional classes are represented, respectively, by \(11\), \(011\), and \(0101\). Hence
\[
L_B(n)=2+\mathbf{1}_{(B,n)\in\{(2,2),(2,3),(3,4)\}},\qquad
A_B(n)=2+\lfloor\log_B n\rfloor.
\]
In particular \(L_B(n)=2\) for all \(n\ge5\), although \(A_B(n)\) is unbounded.

## Assumptions and scope
All factors are taken in the one-sided infinite word indexed by \(\mathbb N_0\). All cyclic rotations are treated as words, including repetitions of a nonprimitive word, so each rotation class is counted once. Lie complexity uses the convention of Bell and Shallit (2021); Abelian complexity counts distinct Parikh vectors, equivalently Hamming weights for a binary alphabet. Lengths start at \(n=1\). Base \(B\) is any integer, including composite bases.

## Proof
The ordered positions of the marked symbols are \(1,B,B^2,\ldots\). Their consecutive positive gaps are
\[
g_j=B^{j+1}-B^j=(B-1)B^j,\qquad j\ge0.
\]
These gaps are strictly increasing and each possible gap occurs for exactly one pair of consecutive marked positions.

**At most two marked symbols.** Consider a cyclic class containing a word with \(r\ge3\) marked symbols, and suppose every rotation is a factor. Let \(d_0,\ldots,d_{r-1}\) denote the positive distances between consecutive marks around this cyclic word. For every \(i\), rotate the word to begin with its \(i\)-th marked symbol. The resulting factor contains \(r\) consecutive marked positions of \(w_B\). Therefore its first two internal mark gaps satisfy \(d_{i+1}=B d_i\), with indices modulo \(r\). These equations hold for all \(i\), because \(r-1\ge2\). Their product gives \(1=B^r\), impossible. Thus any rotation-complete class has at most two marked symbols.

**Exactly two marked symbols.** Write the two positive cyclic distances between its marks as \(d,e\), so the length is \(n=d+e\). Two rotations must appear: a factor with marks at positions \(0,d\), and another with marks at positions \(e-1,e-1+d\). Since the internal distance \(d\) uniquely identifies a consecutive-power pair, both are occurrences of the pair \(B^a,B^{a+1}\) for some integer \(a\ge0\), and \(d=g_a\). For the second rotation to be an actual factor, the \(e-1\) zeros before \(B^a\) must not include the preceding marked position. If \(a=0\), the one-sided boundary at the initial index \(0\) forces \(e\le2\). If \(a\ge1\), the preceding mark is at \(B^{a-1}\), forcing
\[
e\le B^a-B^{a-1}=g_{a-1}.
\]
Swapping the roles of the two marks shows that \(e=g_c\) for some \(c\ge0\) and, symmetrically, \(d\le2\) for \(c=0\), or \(d\le g_{c-1}\) for \(c\ge1\).

If \(a,c\ge1\), these inequalities imply \(c\le a-1\) and \(a\le c-1\), a contradiction. If \(a=c=0\), they require \(g_0=B-1\le2\), giving \(B=2\) with \(n=2\), or \(B=3\) with \(n=4\). If exactly one of \(a,c\) is zero, the other gap must be at most \(2\). Since it is at least \(g_1=B(B-1)\), the only possibility is \(B=2\) with the other index \(1\), giving \(n=3\). All exceptions really occur: for base \(2\), the factors \(11\) and \(011,110,101\) appear, and for base \(3\), both \(0101\) and \(1010\) appear. Thus this case contributes precisely the stated exceptional classes.

**Zero or one marked symbol.** Arbitrarily long gaps between powers yield \(0^n\) for every \(n\). For every fixed \(n\), choose a sufficiently high power whose distances from both neighboring powers exceed \(n\). Moving the window through this isolated power realizes all \(n\) words with exactly one marked symbol. They form a single cyclic class. Combining this with the preceding cases establishes the exact formula for \(L_B(n)\).

**Abelian complexity.** If a factor contains \(r\ge1\) marks, these include \(r\) consecutive powers. Their span is at least \(B^{r-1}-1\), so the factor length satisfies \(n\ge B^{r-1}\). Conversely the length-\(n\) factor starting at position \(1\) contains \(1+\lfloor\log_B n\rfloor\) marks: exactly the powers not exceeding \(n\). This proves that its maximal weight is
\[
M=1+\lfloor\log_B n\rfloor.
\]
Sliding a length-\(n\) window from this factor into an arbitrarily long marker-free gap changes the weight by at most one at every step, so all weights \(0,1,\ldots,M\) occur. There are therefore \(M+1=2+\lfloor\log_B n\rfloor\) Abelian classes. \(\square\)

## Verification
The attached `verify.py` independently enumerates the entire length-\(n\) factor language for each tested base–length pair. Its finite cutoff is justified by choosing a high marked position whose preceding gap is at least \(n\); beyond it, every new factor has at most one marker, and all one-marker rotations already appear. It then computes cyclic-rotation classes and Hamming weights directly and compares them with both formulas. It returned `VERIFY_OK base_length_pairs=1600 bases=2..11 lengths=1..160`. These finite tests are diagnostics, not a replacement for the proof for all integers \(B,n\).

To reproduce: run `python3 verify.py` using a standard Python 3 interpreter. No external packages or data files are required.

## Relationship to prior work
Bell and Shallit introduced Lie complexity and proved general boundedness and automaticity for automatic words [1]. Their examples include the ternary Cantor fixed point, whose marked-position set is not the single-power support considered here. De Luca and Fici studied an exact Lie-complexity classification for Sturmian languages [2]; the present word is not Sturmian, since it contains arbitrarily long zero blocks. Fici, Postic and Silva investigated Abelian antipowers and an Abelian-complexity estimate for the Cantor/Sierpiński word [3], which again has a different marked-position set. The new statement here is the *exact complete rotation-class classification* of the geometric-power support family. The logarithmic Abelian formula is included as an elementary comparison, not claimed as a standalone general novelty.

## Limitations
The result concerns contiguous factors in the one-sided geometric-power support word, not arbitrary sparse automatic sequences, nor occurrences at prescribed positions. It gives no full ordinary factor-complexity or cyclic-complexity formula. Prior-art searches and comparisons cannot rule out unindexed equivalent statements. Verification is finite; the all-base result relies on the proof.

## References
[1] J. P. Bell and J. Shallit, *Lie complexity of words*, first public preprint 2021-02-07, https://arxiv.org/abs/2102.03821 (primary MSC 68R15).

[2] A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, first public preprint 2022-06-02, https://arxiv.org/abs/2206.00995.

[3] G. Fici, M. Postic and M. Silva, *Abelian antipowers in infinite words*, author preprint dated 2019-03-21, https://run.unl.pt/bitstream/10362/75564/1/Abelian_AntiPowers_in_Infinite_Words.pdf.
