# Exact singleton-predecessor spectrum of cyclic binary majority Rule 232

## Finding

For every integer \(n\ge1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the simultaneous majority update on an **indexed cyclic** binary ring:
\[
(F_n(x))_i=\mathbf1\{x_{i-1}+x_i+x_{i+1}\ge2\},\qquad i\in\mathbb Z/n\mathbb Z.
\]
The cyclic subscripts are used literally, including repeated neighboring positions when \(n=1,2\). Put
\[
U_n=\#\{y\in\{0,1\}^n:|F_n^{-1}(\{y\})|=1\}.
\]
Let \(P(z)=\sum_{j=0}^{20}p_jz^j\) and \(D(z)=\sum_{j=0}^{18}d_jz^j\), with coefficient vectors in increasing degree order
\[
\begin{aligned}
(p_0,\ldots,p_{20})={}&(0,2,4,-2,2,18,8,-14,-6,36,12,-78,-76,0,-10,-52,-4,44,16,-6,-2),\\
(d_0,\ldots,d_{18})={}&(1,0,-1,0,-1,-4,-3,0,0,-4,-2,6,7,2,2,4,1,-2,-1).
\end{aligned}
\]
Then the **exact all-length singleton-predecessor generating function** is
\[
\boxed{\sum_{n\ge1}U_nz^n=\frac{P(z)}{D(z)}.}
\]
The denominator also has a factorization into two degree-nine polynomials:
\[
\begin{split}
D(z)={}&(1-z-z^2+z^3-2z^5-z^6-z^8-z^9)\\
&\cdot(1+z+z^2+z^3-2z^5-3z^6-2z^7+z^8+z^9).
\end{split}
\]
For lengths one through sixteen the exact counts are
\[
(U_1,\ldots,U_{16})=(2,4,0,6,20,26,28,38,108,182,242,330,572,1108,1910,2934).
\]
In particular, the polynomial \(D\) gives an integer linear recurrence valid for every \(n\ge21\): \(\sum_{j=0}^{18}d_jU_{n-j}=0\), with \(U_0=0\) as a formal-series convention. The theorem counts observation words with **one**, rather than zero or merely at least one, periodic predecessor.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), all sites and outputs are indexed, and cyclic rotations are *not* identified. The local update uses the three slots \(i-1,i,i+1\); they may refer to the same site when the ring is very short. Each distinct cyclic predecessor is counted once. Formal power series are expanded at zero. No symmetry quotient, probabilistic source assumption, infinite-lattice boundary convention, or multistep evolution is involved.

## Proof

**1. Pair-state matrices and the exact inverse-fiber count.** Index the four ordered binary pairs as \(00,01,10,11\). For each \(b\in\{0,1\}\), define the nonnegative integer \(4\times4\) matrix \(M_b\) by
\[
(M_b)_{(a,c),(c',d)}=\mathbf1\{c=c'\}\,\mathbf1\{a+c+d\ge2\text{ iff }b=1\}.
\]
For a cyclic output \(y=y_0\cdots y_{n-1}\), compatible closed paths of length \(n\) in the pair graph are in bijection with indexed cyclic input predecessors. Consequently,
\[
|F_n^{-1}(\{y\})|=\operatorname{tr}(M_{y_0}M_{y_1}\cdots M_{y_{n-1}}),
\]
where multiplication on the right is ordinary integer matrix multiplication. In particular this closed-path argument handles the small rings \(n=1,2\) with repeated neighbors correctly.

**2. Exact finite saturated monoid.** Saturate nonnegative counts at two, using \(a\oplus b=\min(2,a+b)\) and \(a\odot b=\min(2,ab)\). For \(4\times4\) matrices let the product be computed in this saturated semiring, and let \(I\) be the identity. The finite set \(\mathcal S\) of all saturated products of \(M_0,M_1\), including the empty product \(I\), is closed under right multiplication by the two generators. Since saturation retains exactly the distinctions zero, one, and at least two, a word is counted by \(U_n\) exactly when the sum of the four diagonal entries of its saturated product is one.

A complete exact breadth-first construction of this monoid (reproduced by `verify_transfer.py`) has **476 states**, of which **136** have saturated trace exactly one. This is a finite computation over explicit integer arrays, not a sampling of large lengths. Enumerate the states from the identity by breadth-first discovery, scanning generator zero before one. Define the integer transition-count matrix \(T\) of size \(476\times476\) by assigning one transition for each generator, counting coincident destinations twice. Let \(e\) be the column vector indicating states with saturated trace exactly one and let \(u\) be the row vector selecting the identity state. Then
\[
U_n=uT^ne,\qquad n\ge1.
\]

**3. An exact vector certificate for the infinite recurrence.** Write \(D(z)=\sum_{j=0}^{18}d_jz^j\) with the coefficient vector displayed in the finding. The standalone verifier reconstructs all 476 states and transitions, forms \(T^ke\) for \(0\le k\le21\) by integer arithmetic, and checks **every coordinate** of the identity
\[
\boxed{\sum_{j=0}^{18}d_jT^{21-j}e=0.}
\]
Since this is a vector equality, multiplying by \(uT^{n-21}\) proves \(\sum_{j=0}^{18}d_jU_{n-j}=0\) for every \(n\ge21\), without a finite-to-infinite extrapolation. Direct multiplication of the first 21 values \(uT^ke\) by \(D(z)\) returns precisely the coefficient vector of \(P(z)\). Thus \(D(z)\sum_{n\ge1}U_nz^n=P(z)\) holds as a formal power-series identity. The displayed factorization of \(D\) is confirmed by exact polynomial multiplication.

## Verification

The included `verify_transfer.py` independently constructs both letter matrices from the majority truth table, exhaustively discovers the 476-element saturated transition monoid, checks all 476 coordinates of the recurrence certificate, verifies the numerator and denominator through degree 20, and compares 120 exact output counts with the recurrence. `verify_bruteforce.py` enumerates every input configuration for each \(1\le n\le16\), computes its majority-rule output directly, and counts outputs with exactly one preimage. Both scripts use Python's standard library only and were executed successfully from the packaged file contents. Finite direct enumeration is a cross-check; the vector identity is the all-length proof.

## Relationship to prior work

Jen's 1989 article derives arbitrary-block predecessor recurrences for the majority rule (especially Section 4, Case e, pp. 441–442), establishing the underlying classical preimage-counting method; that free-boundary block treatment does not state the cyclic, all-length **number of target words of predecessor multiplicity one** or the displayed rational function. Powley and Stepney (2010) treat predecessor counts of **homogeneous** periodic targets, which do not determine the number of arbitrary singleton targets. Turau's preprint (publicly posted 2023-12-21) studies fixed and two-periodic configurations in majority dynamics; these are temporal orbit counts, not counts of one-step inverse-fiber singletons.

The related published record *Exact cyclic image counts and spectral growth for elementary majority cellular automaton Rule 232* derives the number of outputs with **at least one** predecessor but expressly leaves inverse-fiber distributions outside its scope. Another published record gives singleton-predecessor counts for **Rule 54**, a different local rule, and does not cover Rule 232. A separate published majority-dynamics result gives transient entry times, not one-step inverse-fiber multiplicities. Standard finite-state and de Bruijn counting techniques are not claimed as new here; the new invariant is the explicit complete periodic singleton spectrum for majority Rule 232.

## Limitations

The formula does not give the complete distribution of all inverse-fiber sizes or multistep predecessor counts. The finite exact certificate is reproducible but is not independent human validation. The accessible literature and research-record searches do not exclude every unindexed or differently formulated predecessor-census result. A closely related classical preimage treatment could conceivably yield an equivalent enumeration after further nontrivial specialization, although no equivalent all-length cyclic singleton statement was found in the inspected primary results. The finding does not assert an independently certified first discovery.

## References

1. V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769, first posted 2023-12-21, https://arxiv.org/abs/2312.13769 .
2. E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems **3** (1989), 421–456, esp. pp. 441–442, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf .
3. E. J. Powley and S. Stepney, *Counting Preimages of Homogeneous Configurations in 1-Dimensional Cellular Automata*, Journal of Cellular Automata **5** (2010), 353–381, https://www.oldcitypublishing.com/journals/jca-home/jca-issue-contents/jca-volume-5-number-4-5-2010/jca-5-4-5-p-353-381/ .
4. *Exact cyclic image counts and spectral growth for elementary majority cellular automaton Rule 232*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-image-counts-and-spectral-growth-for-elementary-maj--da4a182e6a5a .
5. *Exact singleton-predecessor generating function for cyclic elementary Rule 54*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-singleton-predecessor-generating-function-for-cyclic-eleme--c2f1f9b3c735 .
6. *Exact entrance-time census and logarithmic settling for cyclic majority dynamics*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-entrance-time-census-and-logarithmic-settling-for-cyclic-m--380fba13c913 .
