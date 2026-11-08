# Exact cyclic avoidance and necklace spectrum for nondecreasing triples

## Finding

Let \(q\ge1\), let \([q]=\{1,\ldots,q\}\) with its usual order, and let \(C_q(m)\) count indexed circular words \((a_0,\ldots,a_{m-1})\in[q]^m\) such that no cyclic triple \((a_i,a_{i+1},a_{i+2})\), with indices modulo \(m\), is weakly increasing. Define the six-periodic integer sequence \(c_0,c_1,\ldots=(1,1,0,-1,-1,0,1,1,\ldots)\), and the polynomial

\[
\Delta_q(z)=1-\sum_{j=2}^{q}c_{j-2}\binom qj z^j.
\]

Then, for every positive integer \(m\),

\[
\boxed{\sum_{m\ge1}C_q(m)z^m=-\frac{z\Delta_q'(z)}{\Delta_q(z)}}.
\]

Consequently, the number of rotation classes (necklaces) of length \(m\) satisfying the same cyclic avoidance condition is

\[
N_q(m)=\frac1m\sum_{d\mid m}\varphi(d)C_q(m/d),
\]

and the number of primitive necklaces is

\[
P_q(m)=\frac1m\sum_{d\mid m}\mu(d)C_q(m/d).
\]

These identities provide complete exact enumerations for every alphabet size and cycle length without a transfer matrix of dimension depending on the length. For \(q=2\), exactly two indexed cyclic words exist at each positive even length, and none at odd length. For \(q\ge3\), an admissible indexed circular word exists for every length at least two; length one is impossible for every \(q\). For example, \(\Delta_3(z)=1-3z^2-z^3\) and \((C_3(1),\ldots,C_3(6))=(0,6,3,18,15,57)\).

## Assumptions and scope

A circular word is represented by an indexed tuple, so rotations are counted separately in \(C_q(m)\); the two necklace counts quotient by rotations. The avoidance condition is checked at **all** cyclic starting positions. When \(m=1\) or \(m=2\), the length-three cyclic test repeats positions, as happens when the word is extended periodically. The alphabet is the fixed totally ordered set \([q]\). The formal power series are over the rational numbers; no numerical convergence is required.

## Proof

Define \(q\times q\) matrices \(D,U\) by \(D_{ij}=1\) if \(i>j\), otherwise zero, and \(U_{ij}=1\) if \(i\le j\), otherwise zero. Thus \(U=J-D\), where \(J=\mathbf 1\mathbf 1^\top\). At each letter, remember whether the preceding comparison was weakly increasing. A weak increase after another weak increase creates a forbidden triple. The resulting two-layer transfer matrix is

\[
A=\begin{pmatrix}D&U\\D&0\end{pmatrix}.
\]

Each admissible cyclic indexed word determines exactly one closed length-\(m\) walk in these states, and conversely: the stored comparison is fixed by the adjacent letters, even when the cycle has length one or two. Therefore \(C_q(m)=\operatorname{tr}(A^m)\).

Taking the Schur complement of the bottom-right identity block in \(I_{2q}-zA\) gives

\[
\det(I_{2q}-zA)=\det(I_q-zD-z^2UD).
\]

Because \(D\) is strictly lower triangular, it is nilpotent. Put \(H=I_q-zD+z^2D^2\). Then \(\det H=1\), and the matrix determinant lemma yields

\[
\det(I_q-zD-z^2UD)
=\det(H-z^2\mathbf1(\mathbf1^\top D))
=1-z^2\mathbf1^\top D H^{-1}\mathbf1.
\]

From \((1-t+t^2)^{-1}=(1+t)/(1+t^3)\),

\[
H^{-1}=\sum_{r=0}^{q-1}c_rz^rD^r.
\]

The entries of \(D^{r+1}\) count strictly decreasing index chains of \(r+2\) letters; summing all entries gives \(\mathbf1^\top D^{r+1}\mathbf1=\binom q{r+2}\). Consequently \(\det(I_{2q}-zA)=\Delta_q(z)\), including the stated six-periodic coefficient pattern. The formal logarithmic determinant identity gives

\[
-\log\det(I_{2q}-zA)=\sum_{m\ge1}\frac{\operatorname{tr}(A^m)}m z^m.
\]

Differentiating and multiplying by \(z\) proves the main generating function. A length-\(m\) indexed periodic word fixed by a rotation with a cycle decomposition into \(d\) repeats corresponds exactly to an admissible cyclic word of length \(m/d\). Burnside's lemma produces \(N_q(m)\); Möbius inversion on minimal periods produces \(P_q(m)\).

For the existence assertions, when \(q=2\) strict descents and weak ascents must alternate, so precisely the two alternating words of each even length qualify. For \(q\ge3\), consider the state with current letter \(1\) and a preceding strict descent. The successive letters \(2,1\) return to this state in two steps, while \(3,2,1\) return to it in three steps. Concatenating these two loops yields every length representable as \(2a+3b\) with nonnegative \(a,b\), namely every length at least two. A one-letter periodic word contains a weakly increasing cyclic triple and is forbidden.

## Verification

The accompanying standard-library Python program `verify.py` calculates \(\Delta_q\) and \(C_q(m)\) using the coefficient recurrence induced by the logarithmic derivative, independently calculates \(\operatorname{tr}(A^m)\) by exact integer matrix multiplication, and directly enumerates cyclic words over small alphabets. It checks every \(1\le q\le8\) and \(1\le m\le12\) against the matrix method, and all corresponding direct enumeration cases with at most \(450000\) candidate words. This finite check tests the implementation and small cases; the determinant argument above proves the infinite theorem.

## Relationship to prior work

Senan Sekhon, *Counting words without non-decreasing subwords of fixed length* (first publicly posted July 12, 2026), Theorem 3.9, gives the ordinary generating function for **linear** words avoiding nondecreasing contiguous patterns. The present result treats cyclic closure, including windows wrapping around the endpoint, and determines rooted periodic counts and primitive rotation orbits. A linear avoidance sequence is not itself a cyclic enumeration. General finite-state transfer and Burnside methods are standard, but the explicit six-periodic binomial determinant and its combined all-alphabet necklace formulas are additional evaluations. Sekhon's 2025 paper concerns strictly rather than weakly increasing patterns, also in linear words.

## Limitations

The closed polynomial evaluation is proved for forbidden nondecreasing triples, not arbitrary forbidden lengths or patterns. It counts order-labeled words, not words modulo arbitrary alphabet permutations. No algorithmic asymptotic improvement over all general finite-automaton methods is claimed. The novelty comparison cannot exclude unindexed equivalent cyclic enumeration formulas.

## References

1. S. Sekhon, *Counting words without non-decreasing subwords of fixed length*, arXiv:2607.19410, first posted 2026-07-12, https://arxiv.org/abs/2607.19410. See Definition 3.1 and Theorem 3.9 (linear enumeration).
2. S. Sekhon, *Counting words without strictly increasing subwords of fixed length*, arXiv:2511.13287, first posted 2025-11-17, https://arxiv.org/abs/2511.13287 (different strict-pattern linear problem).
