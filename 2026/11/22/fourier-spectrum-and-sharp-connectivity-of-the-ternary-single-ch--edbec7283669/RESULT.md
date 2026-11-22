# Fourier spectrum and sharp connectivity of the ternary single-check codeword polytope

## Finding
For every integer \(n\ge 2\), let
\[
C_n=\{x\in\mathbb F_3^n:\textstyle\sum_{i=1}^n x_i=0\},\qquad
P_n=\operatorname{conv}\{(e_{x_1},\ldots,e_{x_n}):x\in C_n\}\subset\mathbb R^{3n},
\]
where \(e_0,e_1,e_2\) are the three standard coordinate vectors. The vertices of \(P_n\) are exactly these \(3^{n-1}\) embedded words.

Two different vertices are adjacent precisely when their words differ on **two** positions with opposing nonzero differences in \(\mathbb F_3\), or on **three** positions with equal nonzero differences. In the inherited Euclidean metric, its edges therefore have only squared lengths \(4\) and \(6\), with exact respective multiplicities
\[
E_2=3^{n-1}\binom n2,\qquad E_3=3^{n-1}\binom n3.
\]
Here \(E_3=0\) when \(n=2\). Its graph is a regular Cayley graph of \(C_n\), with degree \(d_n=(n^3-n)/3\).

The **entire combinatorial graph Laplacian spectrum including multiplicities** is as follows. For every nonnegative integer triple \(c=(c_0,c_1,c_2)\) summing to \(n\), define
\[
F(c)=\sum_{0\le i<j\le2}c_i c_j(c_i+c_j).
\]
The spectrum, as a multiset, has eigenvalues \(\mu(c)=3F(c)/2\), with the compact multiplicity generating formula
\[
\boxed{\quad
\sum_{\mu}\operatorname{mult}(\mu)t^\mu
=\frac13\sum_{c_0+c_1+c_2=n}\frac{n!}{c_0!c_1!c_2!}\,t^{\frac32 F(c)}.\quad}
\]
The expression has nonnegative integer coefficients. In particular, the exact algebraic connectivity is
\[
\boxed{\mu_2(P_n)=\frac32 n(n-1),\qquad
\frac{\mu_2(P_n)}{d_n}=\frac9{2(n+1)}.}
\]
Its multiplicity is \(2\) when \(n=2\), \(8\) when \(n=3\), and \(2n\) when \(n\ge4\). The graph is complete for \(n=2,3\), and noncomplete for every \(n\ge4\).

## Assumptions and scope
All claims use the full constant-weight (three-coordinate, one-hot) embedding and the **unweighted combinatorial** graph Laplacian \(L=d_nI-A\) of the polytope's one-skeleton. This graph Laplacian is distinct from a Euclidean matrix or a length-weighted graph Laplacian. The Euclidean edge lengths refer only to the inherited Euclidean metric on \(\mathbb R^{3n}\). The code is the **single all-ones ternary parity-check code**; no claims are made for arbitrary parity-check matrices, other primes, or binary cyclic transversal polytopes. All statements are exact, with no asymptotic hypotheses.

## Proof
**Step 1: Characterize actual polytope edges.** Each one-hot word is a vertex of the Cartesian product \((\Delta_2)^n\), hence of its subpolytope \(P_n\). Fix distinct codewords \(x,y\). Let \(D=\{i:x_i\ne y_i\}\) and \(\delta_i=y_i-x_i\in\{1,2\}\subset\mathbb F_3\) for \(i\in D\). The smallest coordinate face of \((\Delta_2)^n\) containing their two images allows coordinate \(i\) to select exactly \(x_i\) or \(y_i\) at each differing position (and fixes every equal position). Its intersection with \(P_n\) is the convex hull of all such selections satisfying the parity check. A selection switching precisely a subset \(T\subseteq D\) is a codeword iff \(\sum_{i\in T}\delta_i=0\) in \(\mathbb F_3\).

If no proper nonempty \(T\) has zero sum, the intersection is precisely the segment joining \(x,y\), so it is an edge. Conversely, if such a subset exists, switching \(T\) and switching its complement produce two distinct other codewords \(z,w\), and their embedded vectors satisfy \(v(x)+v(y)=v(z)+v(w)\). The original segment is therefore not an exposed edge. Thus adjacency is **equivalent** to the nonzero difference multiset being a minimal zero-sum sequence of \(\mathbb F_3\).

The only minimal nonempty zero-sum sequences over \(\mathbb F_3\) with nonzero terms are \((1,2)\), \((1,1,1)\), and \((2,2,2)\), up to order. Indeed, a mixed-sign sequence of length at least two has a zero-sum pair, whereas a same-sign sequence has zero sum first at length three. This proves the adjacency description.

**Step 2: Edge counts and metric.** Every difference from a fixed codeword is itself a codeword; the generating steps are all vectors with one \(1\) and one \(2\) (\(2\binom n2\) steps) and all vectors with three equal nonzero coordinates (\(2\binom n3\) steps). These steps are distinct, and the codeword translation group acts transitively on vertices. Double-counting edge endpoints gives \(E_2,E_3\) above. A changed one-hot coordinate contributes squared distance \(\|e_i-e_j\|^2=2\), so squared edge length is twice its Hamming support size. The degree simplifies to \(2\binom n2+2\binom n3=(n^3-n)/3\). Pair steps generate the entire parity-check subgroup \(C_n\), so the graph is connected.

**Step 3: Fourier diagonalization.** Every complex character of \(C_n\) has the form
\[
\chi_a(x)=\omega^{\sum_i a_ix_i},\quad \omega=e^{2\pi i/3},\quad
[a]\in\mathbb F_3^n/\langle(1,\ldots,1)\rangle.
\]
The quotient has exactly \(3^{n-1}\) characters. Put \(z_i=\omega^{a_i}\), \(S=\sum_i z_i\), and \(e_3=\sum_{i<j<k}z_i z_j z_k\). The pair generators have total character sum \(\sum_{i\ne j}z_i\overline{z_j}=|S|^2-n\). The triple generators have sum \(2\operatorname{Re}e_3\). Since \(\sum_i z_i^2=\overline S\) and \(\sum_i z_i^3=n\), Newton's identity gives
\[
6e_3=S^3-3S\overline S+2n.
\]
Therefore the adjacency eigenvalue is \(\lambda(a)=(\operatorname{Re}(S^3)-n)/3\). If \(c_j=|\{i:a_i=j\}|\), expansion of the cube using \(1+\omega+\omega^2=0\) yields
\[
\operatorname{Re}(S^3)=n^3-\frac92\sum_{i<j}c_i c_j(c_i+c_j).
\]
It follows that \(d_n-\lambda(a)=3F(c)/2\). Adding a constant to all \(a_i\) cyclically relabels the three counts, without changing \(F\). The action of the three constant shifts on \(\mathbb F_3^n\) is free, so summing multinomial character counts and dividing by three gives the spectrum with its exact multiplicities.

**Step 4: Exact spectral gap and equality.** A character is trivial iff only one of the three counts is positive. For nontrivial characters, reorder counts so that \(c_0\) is largest and put \(t=c_1+c_2\), so \(1\le t\le2n/3\). One has
\[
F=nt(n-t)+(3t-2n)c_1c_2.
\]
If \(t=1\), then \(F=n(n-1)\). If \(t\ge2\), the coefficient \(3t-2n\) is nonpositive and \(c_1c_2\le t^2/4\), hence
\[
F\ge h(t):=n^2t-\frac32nt^2+\frac34t^3,
\qquad h'(t)=(n-3t/2)^2\ge0.
\]
Consequently \(F\ge h(2)=2n^2-6n+6=n(n-1)+(n-2)(n-3)\). For \(n\ge4\) this is strictly larger than \(n(n-1)\), so all minimizing count triples are permutations of \((n-1,1,0)\). There are \(6n\) corresponding labelled exponent vectors and thus \(2n\) characters after quotienting by constant shifts. For \(n=3\), also \((1,1,1)\) minimizes, contributing another \(6/3=2\) characters to the \(6\) one-defect characters; for \(n=2\), the only two nontrivial characters minimize. This proves the gap and its multiplicity. Comparing degree with \(3^{n-1}-1\) proves the complete-graph assertions.

## Verification
The included `check_exact.py` performs exhaustive comparisons of the minimal-zero-sum adjacency rule with an independent classification of the two allowed difference patterns for every pair at \(2\le n\le6\). It also computes the complete spectrum twice: from count triples, and independently as exact integer Fourier character sums over the generating set. It checks the edge counts, the spectral gap, and the gap multiplicity in every tested dimension. A separate linear-programming test of whether a midpoint lies in the convex hull of the remaining vertices verified all \(36\) pairs at \(n=3\) and all \(351\) pairs at \(n=4\) (SciPy HiGHS, run separately). These finite tests corroborate, but do **not** replace, the proof for all \(n\).

## Relationship to prior work
Rosnes and Helmling's study of prime-field single-parity-check codeword polytopes supplies the constant-weight embedding and a complete, irredundant facet description in the ternary case, not the explicit graph Fourier spectrum or sharp algebraic-connectivity and multiplicity formulas here. Earlier work of the same authors (2015) also describes ternary facet inequalities; this is not claimed as new. Frede, Kaibel, and Merkert define binary cyclic transversal polytopes over \(\mathbb F_2\); their binary setup does not contain the ternary one-hot codeword polytope. Graph spectra of binary cyclic transversal polytopes, other finite-field Fourier problems, and generic parity-check sampling operators do not imply the precise ternary edge-generating set and its cubic character formula. The claims here are restricted to the special ternary one-check family and do not constitute a complete facet classification.

## Limitations
No independently commissioned mathematical audit has been performed. The priority assessment is based on inspected published material and targeted searches, not an exhaustive bibliographic proof of novelty. In particular, older or unindexed literature on ternary codeword-polytope graphs may contain equivalent results. The graph Laplacian is unweighted; weighted-edge or random-walk-mixing-time theorems beyond the normalized spectral gap are not claimed.

## References
- E. Rosnes and M. Helmling, *Adaptive Linear Programming Decoding of Nonbinary Linear Codes Over Prime Fields*, arXiv:1708.06959 (first public version 2017-08-23; inspected 2019 revision), especially Definition 1, Corollary 1, and Theorem 3. https://arxiv.org/abs/1708.06959
- E. Rosnes and M. Helmling, *On Adaptive Linear Programming Decoding of Ternary Linear Codes*, IEEE Information Theory Workshop (2015), DOI:10.1109/ITW.2015.7133150. https://doi.org/10.1109/ITW.2015.7133150
- J. Frede, V. Kaibel, and M. Merkert, *Binary Cyclic Transversal Polytopes*, arXiv:2404.06088v1 (2024-04-09). https://arxiv.org/abs/2404.06088
