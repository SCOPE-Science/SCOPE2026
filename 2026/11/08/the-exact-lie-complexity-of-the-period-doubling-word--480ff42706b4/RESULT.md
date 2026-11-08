# The exact Lie complexity of the period-doubling word

## Finding
Let \(\mathbf p\) be the infinite fixed point beginning with \(0\) of the binary morphism \(\mu(0)=01\) and \(\mu(1)=00\). Write \(\operatorname{Fac}_n(\mathbf p)\) for its distinct length-\(n\) contiguous factors. The *Lie complexity* \(L_{\mathbf p}(n)\) is the number of cyclic-rotation classes \(\mathcal C\) of binary words of length \(n\) with \(\mathcal C\subseteq\operatorname{Fac}_n(\mathbf p)\).

**Theorem.** For all integers \(n\ge1\),
\[
L_{\mathbf p}(n)=\begin{cases}
2,&n=2^a\text{ or }n=3\cdot2^a\text{ for an integer }a\ge0,\\
0,&\text{otherwise}.
\end{cases}
\]
Consequently, the support of this complexity function is exactly the union of two geometric progressions; every nonzero value is two.

## Assumptions and scope
Indices start at zero. Cyclic conjugacy includes every rotation, including rotations of a nonprimitive word; one class is counted once irrespective of orbit size. A rotation-complete class requires *all* its members as factors of the same infinite fixed point, not simply one member. The fixed point satisfies \(p(i)=\nu_2(i+1)\bmod2\), where \(\nu_2\) is the exponent of two in a positive integer. Let \(\mathbf q\) denote its bitwise complement, \(q(i)=1-p(i)\).

## Proof
**1. Parity structure and short forbidden factors.** The valuation formula immediately gives
\[
p(2i)=0,\qquad p(2i+1)=1-p(i)=q(i)\quad(i\ge0).
\]
All occurrences of \(1\) therefore lie at odd positions; in particular \(11\) is not a factor. The factor \(0000\) is also impossible. Indeed, a window of four consecutive positions contains two consecutive odd positions \(2j+1\) and \(2j+3\). If both letters were \(0\), then \(p(j)=p(j+1)=1\), contradicting the absence of \(11\). The prefix \(010001\) exhibits the factor \(000\), as well as \(001,010,100\), the three rotations of \(001\) (here \(010\) is at positions zero through two, \(100\) at one through three, and \(001\) at three through five).

**2. Odd lengths.** At length one the rotation-complete classes are \(\{0\}\) and \(\{1\}\), giving \(L_{\mathbf p}(1)=2\). At length three the rotation-complete classes are \(\{000\}\) and \(\{001,010,100\}\), giving \(L_{\mathbf p}(3)=2\); a binary three-letter word with at least two ones contains a circular adjacent \(11\) and cannot have all rotations as factors.

Fix an odd length \(n\ge5\), and suppose a circular binary word of length \(n\) has all rotations among factors of \(\mathbf p\). If it contains two or more ones, each positive circular distance between successive ones must be even: rotate the circular word so that the first of those two successive ones occurs at its initial position; the second one then lies at another position within the same factor. The two corresponding one-positions in \(\mathbf p\) are both odd, so their difference is even. Summing these even circular distances over all successive ones would yield the odd circumference \(n\), a contradiction. If there are no ones, the circular word is \(0^n\), forbidden since \(0000\) is absent. If there is just one one, some rotation contains \(0^{n-1}\), likewise forbidden. Hence \(L_{\mathbf p}(n)=0\) for all odd \(n\ge5\).

**3. Exact halving identity.** For any \(m\ge1\), put \(I(v)=0v_0 0v_1\cdots0v_{m-1}\) and \(J(v)=v_0 0v_1 0\cdots v_{m-1}0\) for a binary word \(v=v_0\cdots v_{m-1}\). The parity identities in Step 1 show that \(\operatorname{Fac}_{2m}(\mathbf p)\) is precisely
\[
\{I(v),J(v):v\in\operatorname{Fac}_m(\mathbf q)\}.
\]
Indeed, these are respectively all windows starting at an even or an odd position of \(\mathbf p\), and every factor of \(\mathbf q\) appears at both phases. Rotating \(I(v)\) by one position yields \(J(v)\); rotating by two positions yields \(I(\operatorname{rot}(v))\), up to the chosen rotation direction. The same holds for the \(J\) phase. Thus a class formed from \(I(v)\) and \(J(v)\) is rotation-complete in \(\mathbf p\) if and only if the class of \(v\) is rotation-complete in \(\mathbf q\).

This correspondence is one-to-one on cyclic classes. For a circular word with at least one \(1\), the phase with all even-position letters zero is determined uniquely among the two parities, except when both parities are zero, which is the all-zero word and corresponds uniquely to the all-zero source class. Equivalently, the circular word is the subdivision of a source circle by one zero between successive source letters; its inverse source circle is uniquely defined up to cyclic rotation. Therefore
\[
L_{\mathbf p}(2m)=L_{\mathbf q}(m).
\]
Bitwise complementation bijects factor languages and commutes with rotation, so \(L_{\mathbf q}(m)=L_{\mathbf p}(m)\). Consequently \(L_{\mathbf p}(2m)=L_{\mathbf p}(m)\) for all \(m\ge1\).

**4. Solve the recurrence.** Repeatedly remove factors of two from \(n\). The remaining positive odd integer is one or three precisely when \(n=2^a\) or \(n=3\cdot2^a\). The odd base cases proved in Step 2 give exactly the displayed formula. This completes the proof.

## Verification
The standalone `verify.py` is a finite, reproducible check, not the infinite proof. It constructs the complete length-\(n\) factor set by substituting every occurring length-two source factor \(00,01,10\) through \(k\) stages, where \(2^k\ge n\), and extracting every length-\(n\) window. Any actual length-\(n\) factor crosses at most two adjacent \(k\)-supertiles, and all three source pairs occur; thus this finite set is exactly the full factor set for the chosen \(n\). The script computes every cyclic orbit and compares the resulting Lie count with the theorem for each \(1\le n\le160\). It also compares explicit classes at lengths one, three, and four. The executed check printed `VERIFY_OK lengths=1..160 exact-factor-cover=adjacent-substitution-blocks factor_instances= 20267 lie_formula=PASS`.

## Relationship to prior work
Bell and Shallit introduced Lie complexity, showed general boundedness under linear factor complexity and automaticity for automatic words, and computed examples for several classical sequences [1]. Their inspected examples do not give this period-doubling exact support law. De Luca and Fici obtained an exact formula for the different class of Sturmian words [2], which excludes the period-doubling fixed point. Cassaigne and collaborators investigated *cyclic complexity*, which counts all partially represented rotation classes rather than only fully represented classes [3]; their period-doubling cyclic results do not yield the exact Lie formula. The present result is a direct, elementary classification specialized to the period-doubling word, with a two-step parity desubstitution.

## Limitations
The theorem addresses one fixed point and its binary complement, not every Toeplitz or period-doubling-like morphism. The absence of an equivalent formula in the literature inspected is not a proof of worldwide novelty; unindexed or differently formulated results may exist. The finite verifier does not certify any unbounded quantifier without the separate proof.

## References
[1] J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821, first posted 2021-02-07. https://arxiv.org/abs/2102.03821

[2] A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, arXiv:2206.00995, first posted 2022-06-02. https://arxiv.org/abs/2206.00995

[3] J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, *Cyclic complexity of words*, arXiv:1402.5843. https://arxiv.org/abs/1402.5843
