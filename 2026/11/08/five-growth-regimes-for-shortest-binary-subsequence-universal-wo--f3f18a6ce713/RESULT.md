# Five growth regimes for shortest binary subsequence-universal words avoiding one four-letter factor

## Finding

Let the ambient alphabet be \(\Sigma=\{0,1\}\). For a positive integer \(k\), a finite word is \(k\)-subsequence universal if each word in \(\Sigma^k\) occurs as a scattered subsequence. For a forbidden contiguous word \(p\in\Sigma^4\), let \(a_p(k)\) be the number of length-\(2k\) binary words which are \(k\)-subsequence universal and avoid \(p\) as a contiguous factor, and let \(F_p(z)=\sum_{k\ge1}a_p(k)z^k\).

**Complete classification.** Under reversal and bit complementation, every four-letter forbidden word has one of the six representatives below. The generating functions shown are exact for every \(k\ge1\).

| Forbidden representative \(p\) | \(F_p(z)\) | Growth type |
|---|---|---|
| `0000` | \(\frac{2z}{1-2z}\) | \(2\) |
| `0001` | \(\frac{2z}{1-2z}\) | \(2\) |
| `0010` | \(\frac{z(2-z^2)}{1-2z+z^3}\) | \(\varphi=(1+\sqrt5)/2\) |
| `0011` | \(\frac{z(2+z^2)}{1-2z+z^2-z^3}\) | \(\alpha\approx1.7548776662\) |
| `0101` | \(\frac{z(2+3z+2z^2)}{1-z^2-z^3}\) | \(\rho\approx1.3247179572\) |
| `0110` | \(\frac{z(2-z)}{(1-z)^2}\) | polynomial, \(a_p(k)=k+1\) |

Here \(\alpha\) is the unique real root greater than one of \(t^3-2t^2+t-1=0\), and \(\rho\) is the unique real root greater than one of \(t^3-t-1=0\). The displayed growth types are precisely \(\lim_{k\to\infty}a_p(k)^{1/k}\). In particular, the sixteen possible single forbidden four-letter factors yield exactly **five distinct asymptotic growth rates**, including polynomial growth, three intermediate exponential rates, and unrestricted exponential growth.

In the `0010` orbit the formula simplifies to \(a_p(k)=\mathrm{Fib}_{k+3}-1\) (with \(\mathrm{Fib}_0=0\), \(\mathrm{Fib}_1=1\)). In the `0110` orbit there are exactly \(k+1\) shortest universal words. Every forbidden four-letter factor admits a \(k\)-subsequence-universal avoiding word of length exactly \(2k\) for every \(k\ge1\), so these counts concern the actual shortest length even after imposing avoidance.

## Assumptions and scope

All words are finite over the *fixed* binary alphabet \(\Sigma\), including when a particular word uses only one symbol. A forbidden factor means a **contiguous** substring; subsequence universality means **possibly noncontiguous** subsequences. Factors at the ends are counted in the usual manner. The parameter \(k\) ranges over all positive integers, and the pattern \(p\) ranges over every binary word of length four, with precisely one pattern forbidden. Generating functions are formal power series in \(z\).

## Proof

**1. Sharp length and block representation.** A \(k\)-universal binary word has at least \(k\) disjoint subwords each containing both alphabet symbols: greedily take the shortest prefix containing both symbols, then repeat on the remaining suffix. Conversely, such a concatenation is \(k\)-universal, since one can take the required symbol from each successive subword. Therefore the minimum length is at least \(2k\), and equality holds precisely for the words
\[
\mathcal U_k=\{01,10\}^{k}.
\]
Indeed every one of the \(k\) greedy arches then has length exactly two. This recovers the classical shortest-universality characterization, but is included to fix both directions and the boundary case \(k=1\).

**2. Symmetry classification.** Reversal preserves universality because it reverses every subsequence, and bit complementation permutes the target alphabet. Both operations transform avoidance of \(p\) to avoidance of the transformed pattern. Their orbits on the sixteen binary length-four patterns have representatives
\[
0000,\ 0001,\ 0010,\ 0011,\ 0101,\ 0110.
\]
They have respective orbit sizes \(2,4,4,2,2,2\), summing to sixteen. Thus it is enough to count these six representatives.

**3. Exact finite-state transfer.** Name the two length-two blocks \(A=01\) and \(B=10\), and order the four states \((A,A),(A,B),(B,A),(B,B)\). Define the row vector \(v_p\) by
\[
(v_p)_{(X,Y)}=\mathbf1_{\{p\not\subseteq XY\}},
\]
where containment here means occurrence as a contiguous factor, and define the zero-one matrix
\[
(M_p)_{(X,Y),(Y,Z)}=\mathbf1_{\{p\not\subseteq (XYZ)[2..6]\}},
\]
with all other entries zero. Here \((XYZ)[2..6]\) is the last five symbols of the six-symbol concatenation (indices starting at one). The first two blocks contribute \(v_p\). On appending a block, the only new four-symbol windows start at the second or third positions of the three most recent blocks; both are contained in the last five symbols. Thus \(M_p\) rejects exactly the newly introduced occurrences, with neither omissions nor double counting.

For \(k=1\), both blocks are allowed. For \(k\ge2\), the exact number of admissible block strings is \(v_pM_p^{k-2}\mathbf1\). Hence
\[
F_p(z)=2z+z^2v_p(I-zM_p)^{-1}\mathbf1.
\]
This identity is a finite algebraic proof of the complete infinite family of coefficients, not an inference from finite experiments. For example, for `0011`,
\[
v_{0011}=(1,1,1,1),\qquad
M_{0011}=\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
Evaluating the four-by-four rational inverse gives \(F_{0011}(z)=z(2+z^2)/(1-2z+z^2-z^3)\). Applying the same explicitly defined construction to the other five representatives yields the remaining five rational functions in the table. The accompanying standalone verifier implements this transfer independently and checks the formal rational identities exactly by integer-polynomial arithmetic (Cayley–Hamilton), then checks coefficients against unrestricted block enumeration.

**4. Distinct growth types.** The simplified denominators are \(1-2z\), \(1-2z+z^3=(1-z)(1-z-z^2)\), \(1-2z+z^2-z^3\), \(1-z^2-z^3\), and \((1-z)^2\). In the first four cases the unique dominant positive pole is simple, and the numerators are nonzero there; the Perron growth rates are respectively \(2\), \(\varphi\), \(\alpha\), and \(\rho\). For the last case, expansion yields \(a_{0110}(k)=k+1\). Since the five growth constants are distinct, the five regimes cannot merge. Their positivity and the exact rational expressions also show that each count is nonzero at every positive \(k\), so length \(2k\) remains optimal under each avoidance restriction.

## Verification

`verify.py` is a Python 3 standard-library checker. It constructs the transitions from their substring definition for every one of the sixteen forbidden patterns, checks the reversal-complement orbits, compares coefficient recurrences of the six rational functions with transfer-matrix counts through \(k=32\), and exhaustively enumerates all \(\{01,10\}^k\) through \(k=10\). A separate direct subsequence test for all binary words of lengths \(2,4,6,8,10\) checks the minimum-length characterization. The executed result was:

`VERIFY_OK patterns=16 orbits=6 rational_terms=32 symbolic_identities=16 direct_minimal_lengths=1..5 tested_words=1364 pattern_cases=32736`

These are finite diagnostics only. The transfer identity and algebraic calculation above establish the assertions for all \(k\), and the direct argument establishes the sharp minimum length.

## Relationship to prior work

The arch-factor characterization of shortest binary subsequence-universal words is established by Barker, Fleischmann, Harwardt, Manea and Nowotka (2020). Adamson (2023) gives algorithms for enumerating and ranking unconstrained subsequence-universal words. Adamson, Fleischmann, Huch, Koß, Manea and Nowotka (2023) give general algorithms for counting subsequence-universal words in regular languages; this ensures computational accessibility but does not state these six explicit rational functions or the five-way growth classification.

Counting words avoiding a single fixed factor is a standard finite-state technique, and the `0000`/`0001` cases are elementary. The nontrivial part of this particular classification is how forbidden four-symbol *contiguous* windows intersect the two-symbol arches realizing shortest *scattered* universality, yielding four distinct non-unrestricted rational laws. Some numerical sequences coincide with classical Fibonacci- or Padovan-type sequences; that coincidence alone does not identify the constrained-word counting interpretation.

## Limitations

The theorem treats one forbidden **length-four** pattern and only the **shortest length** \(2k\), not all lengths or multiple forbidden factors. It does not assert originality of the general transfer-matrix technique, of the arch factorization, or of the classical number sequences. Potential equivalent formulations in unindexed literature remain a bibliographic risk. The verification is not an independent external audit.

## References

- L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, first public version 2020-03-10, arXiv:2003.04629, https://arxiv.org/html/2003.04629v1.
- D. Adamson, *Ranking and Unranking k-Subsequence Universal Words*, first public version 2023-04-10, arXiv:2304.04583, https://arxiv.org/abs/2304.04583.
- D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea and D. Nowotka, *k-Universality of Regular Languages*, first public version 2023-11-17, arXiv:2311.10658, https://arxiv.org/abs/2311.10658.
- OEIS A000931, Padovan sequence, https://oeis.org/A000931; OEIS A207000, a distinct pattern-avoidance array containing some coincident initial numerical values, https://oeis.org/A207000.
