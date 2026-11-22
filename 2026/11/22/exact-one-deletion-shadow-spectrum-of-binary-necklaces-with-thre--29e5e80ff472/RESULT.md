# Exact one-deletion shadow spectrum of binary necklaces with three ones

## Finding

For each integer \(n\ge3\), let \(\mathcal N_{n,3}\) denote binary words of length \(n\) with exactly three ones, identified under cyclic rotation, but **not** reflection or bit complementation. For each source necklace \(W\), let \(\mathcal D(W)\) be the set of distinct necklaces obtained by deleting exactly one position and then identifying the surviving length-\(n-1\) words under rotation. Put \(c_j(n)=|\{W\in\mathcal N_{n,3}:|\mathcal D(W)|=j\}|\), and \(F_j(z)=\sum_{n\ge3}c_j(n)z^n\).

The deletion-shadow sizes are precisely \(1,2,3,4,5,6\), and their full all-length distribution is:

\[
\begin{aligned}
F_1(z)&=z^3,\\
F_2(z)&=\frac{z^4}{1-z}+\frac{z^6}{1-z^3},\\
F_3(z)&=z^5,\\
F_4(z)&=\frac{z^5}{(1-z)^2}-z^5+\frac{z^8}{1-z^3},\\
F_5(z)&=\frac{z^6}{(1-z)(1-z^2)}-\frac{z^6}{1-z^3}-\frac{z^8}{1-z^3},\\
F_6(z)&=\frac{z^6}{3}\left(\frac{1}{(1-z)^3}-\frac{3}{(1-z)(1-z^2)}+\frac{2}{1-z^3}\right).
\end{aligned}
\]

All other \(F_j\) vanish identically. Exactly one source necklace has three deletion outputs (at \(n=5\)); six outputs first occur at \(n=9\). For a uniformly sampled weight-three necklace, \(\Pr\{|\mathcal D(W)|=6\}=1-O(1/n)\), because the number with six outputs is \(n^2/6+O(n)\), while all other classes together have \(O(n)\) members.

## Assumptions and scope

A source is a binary *oriented* necklace: cyclic rotation is quotiented, while reflection and complementation are not. Deletion removes exactly one bit, preserves the clockwise order of survivors, and forgets the output's starting point. Multiple deletion positions producing the same output are counted once. The input has exactly three ones. A necklace is represented canonically by its cyclic ordered three-zero-gap tuple \((a,b,c)\) with \(a,b,c\ge0\) and \(a+b+c=n-3\), corresponding to \(1\,0^a1\,0^b1\,0^c\). Rotating this triple but not reversing it leaves the same source. When \(n=3\), the all-one word is included.

## Proof

Put \(N=a+b+c\). Deleting a one yields a necklace with two ones and \(N\) zeros. Its cyclic gap pair is \((g,N-g)\) for some \(g\in\{a,b,c\}\); its rotation class is determined by the unordered pair \(\{g,N-g\}\). Two values \(g,h\) give the same unordered pair exactly when \(g=h\) or \(g+h=N\). For different gap positions, the second possibility requires their remaining gap to be zero. The number \(O(a,b,c)\) of distinct one-deletion outputs is therefore the number of distinct values among \(\min(a,N-a),\min(b,N-b),\min(c,N-c)\). This formula also holds for zero gaps and \(N=0\).

Deleting a zero from a positive gap replaces \((a,b,c)\) by the triple obtained by decrementing that coordinate once, with nonnegative entries and total \(N-1\). The resulting weight-three necklaces are equal exactly when these new triples agree up to rotation. Let \(Z(a,b,c)\) be the number of distinct outputs from such operations. There are \(p=|\{g\in\{a,b,c\}:g>0\}|\) candidate positive-gap operations. For two different positive gap positions, after a cyclic relabeling it suffices to compare \((a-1,b,c)\) and \((a,b-1,c)\). Direct equality is impossible. Equality with the first nontrivial rotation, \((b-1,c,a)\), forces \(a=b=c\). Equality with the other rotation, \((c,a,b-1)\), forces \(a=b=c+1\). These are all alternatives. Consequently

\[
Z(a,b,c)=p-2\mathbf 1_{\{a=b=c>0\}}-\mathbf 1_{\{(a,b,c)\sim(t,t,t-1),\ t\ge1\}},
\]

where \(\sim\) means a cyclic rotation. The two exceptional events are disjoint. The boundary instance \(t=1\) is the triple \((1,1,0)\), and its two positive-gap deletions do collide. A zero-deletion output has three ones while a one-deletion output has two, so the two output families are disjoint, and
\[
|\mathcal D(W)|=Z(a,b,c)+O(a,b,c).
\]

This yields a complete structural partition (up to rotation):

| Cyclic zero-gap type | Shadow size |
|---|---:|
| \((0,0,0)\) | 1 |
| \((N,0,0)\), \(N>0\), or \((t,t,t)\), \(t>0\) | 2 |
| \((1,1,0)\) | 3 |
| \((a,b,0)\), \(a,b>0\), other than \((1,1,0)\), or \((t,t,t-1)\), \(t\ge2\) | 4 |
| \((t,t,s)\), \(t,s>0\), \(s\ne t\), \(s\ne t-1\) | 5 |
| \((a,b,c)\), all positive and pairwise distinct | 6 |

The table follows from the two formulas: for all-positive pairwise-distinct gaps, each of the three zero and three one deletions is different; for exactly two equal positive gaps, there are two distinct one-deletion outputs and either three or two zero-deletion outputs; when exactly one gap is zero there are two one-deletion outputs and normally two zero-deletion outputs, with a collision only for \((1,1,0)\). The remaining types are immediate, including \(N=0\).

We now count these mutually disjoint cyclic-gap classes. Let \(\delta_{3\mid N}\) indicate divisibility by three. The singleton class occurs only for \(N=0\); the size-two classes contribute one for each \(N\ge1\) plus one all-equal positive triple at every positive multiple of three. The size-three class contributes only at \(N=2\). For \(N\ge2\), the one-zero-gap classes contribute \(N-1\) rotation classes, except the \((1,1,0)\) member at \(N=2\); the exceptional all-positive \((t,t,t-1)\) contributes one at each \(N=3t-1\), \(t\ge2\).

The all-positive two-equal triples have one rotation class for each choice of integers \(t,s\ge1\), \(s\ne t\), and total zeros \(N=2t+s\). Their generating series by \(N\) is \(x^3/((1-x)(1-x^2))-x^3/(1-x^3)\). Remove the exceptional \((t,t,t-1)\) series \(x^5/(1-x^3)\) to obtain the size-five class. Finally, count all-positive pairwise-distinct ordered triples by removing the all-equal and exactly-two-equal triples from all positive compositions of \(N\), and divide by three since each such cyclic orbit has size three. Their generating series by \(N\) equals
\[
\frac{x^3}{3}\left(\frac{1}{(1-x)^3}-\frac{3}{(1-x)(1-x^2)}+\frac{2}{1-x^3}\right).
\]

Multiplying every series in \(x\) by \(z^3\) and replacing \(x\) with \(z\) gives exactly the six displayed \(F_j(z)\). This is an all-length derivation, with no unproved extrapolation. Summing all six yields the independent Burnside count \(\bigl(\binom{N+2}{2}+2\delta_{3\mid N}\bigr)/3\). All non-six cases number only \(O(N)\), whereas the last generating function has coefficient \(N^2/6+O(N)\). The limiting assertion follows. \(\square\)

## Verification

The included standalone Python 3 file `verify.py` has no external dependencies. Run `python verify.py`. It independently deletes every literal bit and canonicalizes all output rotations for each of 981 cyclic-gap triples with at most 24 zeros, compares a separate gap-prediction function, independently builds all fixed-three-one binary necklace deletion shadows at lengths \(3\) through \(18\), and checks integer coefficients of all six generating functions through length \(57\). Its expected output is `VERIFY_OK gap_orbits=981 direct_length=3..18 rational_coefficients=3..57`. These finite tests support the proof but do not replace the universal algebraic argument.

## Relationship to prior work

Sloane (2002), Section 5, studies linear binary deletion descendants and identifies their count with the linear run number. Liron and Langberg (2012) analyze the number of linear subsequences after deletions and their extremizers. Narayanan and Ren (2020) study circular trace reconstruction under a stochastic deletion channel, with a sample-complexity goal rather than this exact fixed-content output-shadow histogram. Chee, Ge and Ling (2010) discuss perfect deletion-code size spectra in the linear model; their Theorem-level claims do not determine this circular-source distribution.

The published *Sharp one-deletion outdegree of binary necklaces* gives the **maximum** shadow size among all binary necklaces at each length, explicitly not the full per-source count or a fixed-composition distribution. *First fractional-shadow packing gap for binary necklace deletion codes* gives finite integer/fractional code optima through length nine, not an all-length three-one sphere histogram. *Three-marker border correlation: a local gap law and its exact distribution* enumerates gap-equality types for **unbordered conjugates**, and in particular its all-distinct gap column numerically equals the present six-output column. The latter numerical column is not claimed as new on its own: the contribution is the full six-bucket one-deletion shadow distribution, including the adjacency-of-equal-gaps collision \((t,t,t-1)\), its small exceptional type \((1,1,0)\), and the different coding observable. Neither a shared gap parameterization nor that one known column implies the entire claimed shadow classification without the new deletion-collision analysis.

## Limitations

The theorem treats only binary necklaces of Hamming weight exactly three, exactly one deletion, and equivalence under rotation (not reversal). It does not establish any optimal deletion-correcting code size, decoding under unknown orientation, or general fixed-weight formula for weight four and higher. The finite checker is bounded. An earlier equivalent classification under different terminology may exist; neither literature search nor computational experiments certify universal historical priority. Independent mathematical audit has not been performed.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, first public 2002-07-22, https://arxiv.org/html/math/0207197v1, Section 5.
2. Y. M. Chee, G. Ge and A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, first published online 2010-02-05, https://doi.org/10.1137/090751311; public preprint https://arxiv.org/abs/1008.1343.
3. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, first public 2012-02-08, https://arxiv.org/html/1202.1644v1.
4. S. Narayanan and M. Ren, *Circular Trace Reconstruction*, first public 2020-09-02, https://arxiv.org/html/2009.01346v2.
5. *Sharp one-deletion outdegree of binary necklaces* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-one-deletion-outdegree-of-binary-necklaces--2341722fce11.
6. *First fractional-shadow packing gap for binary necklace deletion codes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-first-fractional-shadow-packing-gap-for-binary-necklace-deletion--b2d604e329da.
7. *Three-marker border correlation: a local gap law and its exact distribution* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-three-marker-border-correlation-a-local-gap-law-and-its-exact-di--8c6645349a80.
