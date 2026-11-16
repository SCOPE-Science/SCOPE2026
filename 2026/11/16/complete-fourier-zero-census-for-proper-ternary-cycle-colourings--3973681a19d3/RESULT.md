# Complete Fourier zero census for proper ternary cycle colourings

## Finding

For each integer \(n\ge 3\), let \(G_n=(\mathbb Z/3\mathbb Z)^n\) with coordinates indexed \(0,\ldots,n-1\), and let
\[
P_n=\{x\in G_n:x_i\ne x_{i+1\pmod n}\text{ for every }i\}.
\]
For \(b\in G_n\), write \(\omega=\exp(2\pi i/3)\) and define the **unnormalized** additive Fourier coefficient
\[
W_n(b)=\sum_{x\in P_n}\omega^{\sum_{i=0}^{n-1}b_i x_i}.
\]
Set \(c_n=0\) and \(c_j=\sum_{i=j}^{n-1}b_i\pmod3\) for \(1\le j<n\). For each \(t\in\{0,1,2\}\), let \(z_t=|\{1\le j\le n:c_j=t\}|\). Then the entire Fourier transform is given exactly by
\[
W_n(b)=\begin{cases}
0,&\sum_i b_i\not\equiv0\pmod3,\\
(-1)^n\bigl((-2)^{z_0}+(-2)^{z_1}+(-2)^{z_2}\bigr),&\sum_i b_i\equiv0\pmod3.
\end{cases}
\]
In the zero-total-frequency hyperplane, a coefficient vanishes if and only if the three occupancies are a permutation of \((a,a,a+1)\) for some integer \(a\ge1\). In particular **additional Fourier zeros exist if and only if \(n\equiv1\pmod3\)**. Their exact number is
\[
E_n=\begin{cases}
\displaystyle\frac{n!}{a!^2(a+1)!},&n=3a+1\ (a\ge1),\\
0,&n\not\equiv1\pmod3.
\end{cases}
\]
Therefore the rank of unnormalized convolution by \(\mathbf1_{P_n}\) on \(\mathbb C^{G_n}\) is
\[
\boxed{\operatorname{rank}C_n=3^{n-1}-E_n.}
\]
All nonzero multipliers are nonzero integers divisible by \(3\). Consequently the Moore--Penrose pseudoinverse satisfies \(\|C_n^\dagger\|_{\ell^2\to\ell^2}\le1/3\). The bound is attained at \(n=3\) and \(n=5\); a sharp inverse norm for every \(n\) is not asserted.

## Assumptions and scope

A proper colouring is a map from the \(n\) distinct vertices of the ordinary simple cycle \(C_n\) into the additive group of three colours; the constraint is inequality, not a prescribed difference. The group Fourier transform and convolution carry no probability or unitary normalization. Convolution acts by \((C_nf)(y)=\sum_{x\in P_n}f(y-x)\). Changing the sign convention for additive characters permutes frequencies and leaves the rank formula unchanged. The theorem concerns all \(3^n\) frequencies, not only first-coordinate characters.

## Proof

**1. Translation constraint.** Adding a common \(u\in\mathbb Z/3\mathbb Z\) to every colour preserves \(P_n\). In the defining sum, this multiplies \(W_n(b)\) by \(\omega^{u\sum_i b_i}\). Hence \(W_n(b)=0\) unless the total frequency is zero modulo three.

**2. Edge increments and character orthogonality.** Assume henceforth that \(\sum_i b_i\equiv0\pmod3\). Write \(d_j=x_j-x_{j-1}\in\{1,-1\}\) for \(1\le j<n\), and \(d_n=x_0-x_{n-1}\in\{1,-1\}\). A proper cycle colouring corresponds bijectively to a starting colour \(x_0\in\mathbb Z/3\mathbb Z\) and \(n\) increments \(d_j\in\{1,-1\}\) satisfying \(\sum_{j=1}^n d_j\equiv0\pmod3\). Since \(x_i=x_0+\sum_{j\le i}d_j\), summation by parts gives
\[
\sum_i b_i x_i=\sum_{j=1}^{n}c_jd_j\pmod3,
\]
where \(c_n=0\). Insert the exact root-of-unity filter
\[
\mathbf1_{\sum d_j=0}=\frac13\sum_{u=0}^2\omega^{u\sum d_j}.
\]
The three choices of \(x_0\) cancel its prefactor. Thus
\[
W_n(b)=\sum_{u=0}^{2}\prod_{j=1}^{n}
\bigl(\omega^{c_j+u}+\omega^{-(c_j+u)}\bigr).
\]
The parenthesized factor equals \(2\) for a zero residue and \(-1\) otherwise. Every \(u\) simply selects one of the three occupancy numbers \(z_t\), proving the displayed formula. In particular all coefficients in the allowed hyperplane are real integers.

**3. Complete classification of cancellations.** Let \(r_1\le r_2\le r_3\) be nonnegative integers. If
\[
(-2)^{r_1}+(-2)^{r_2}+(-2)^{r_3}=0,
\]
then necessarily \(r_1=r_2\): otherwise division by \((-2)^{r_1}\) makes the left side odd. If \(r_1=r_2=r_3\), the sum is three times a nonzero integer. Otherwise, division by \((-2)^{r_1}\) gives \(2+(-2)^{r_3-r_1}=0\); this holds precisely when \(r_3=r_1+1\). Conversely, the exponent multiset \((a,a,a+1)\) gives exact cancellation. Its sum is \(3a+1=n\). As \(n\ge3\), any such \(a\) is at least one. Every occupancy triple is attainable by some \(c_1,\ldots,c_{n-1}\) with \(c_n=0\), and hence by a unique total-zero \(b\), provided its zeroth occupancy is positive. The required triples have this property for \(a\ge1\).

**4. Multiplicities and rank.** The map from the total-zero frequency hyperplane to \((c_1,\ldots,c_{n-1})\in(\mathbb Z/3\mathbb Z)^{n-1}\) is bijective: its inverse is \(b_0=-c_1\), \(b_j=c_j-c_{j+1}\) for \(1\le j<n-1\), and \(b_{n-1}=c_{n-1}\). For \(n=3a+1\), the number of length-\(n\) ternary strings whose occupancy multiset is \((a,a,a+1)\) is
\[
3\frac{n!}{a!^2(a+1)!}.
\]
By symmetry of the three alphabet symbols, exactly one third have final entry zero. This gives \(E_n\) and proves there are no other zeros inside the total-zero hyperplane. The Fourier diagonalization of group convolution gives rank \(3^{n-1}-E_n\).

**5. Nonzero spectral bound.** Since \(-2\equiv1\pmod3\), every allowed-hyperplane multiplier is congruent to \((-1)^n(1+1+1)=0\pmod3\). A nonzero multiplier therefore has absolute value at least three. For \(n=3\) and \(n=5\), the exponent triples \((0,1,2)\) and \((0,2,3)\) respectively give absolute multiplier three; the residues may be permuted to ensure \(z_0\ge1\), so these values occur at genuine frequencies. This proves the norm statement and its two specified sharp cases.

## Verification

Run `python3 checker.py` with Python 3.10 or later. Its integer-pair implementation of \(\mathbb Z[\omega]\) constructs the indicator independently and performs all \(3^n\) cyclotomic Fourier coefficients by successive three-point transforms for each \(3\le n\le10\). Only after that computation does it compare against the theorem and the rank formula. It checks 88,560 coefficient values in total and prints `TERNARY_CYCLE_FULL_FOURIER_PASS total_coefficients=88560`. These finite checks corroborate the proof but do not substitute for its arbitrary-length arguments.

## Relationship to prior work

The chromatic polynomial and zero-temperature antiferromagnetic Potts partition function are classical; in particular the total number of colourings of a cycle is \(2^n+2(-1)^n\). The cited magnetic-field and weighted-chromatic papers develop transfer matrices and partition functions, including uniform external fields for cyclic graphs. Their fields do not encode independently chosen additive character weights at each vertex, and the inspected statements do not determine the vanishing of all Fourier frequencies or the exact additional-nullity formula above. A separate published study of degree-one Fourier sampling on proper cycle colourings computes a restricted Gram spectrum, not the full Fourier transform and convolution rank. General integer-point generating functions for arbitrary vertex-weighted chromatic sums also encode the individual weighted counts after suitable specialization, but do not state the cycle-specific root-of-unity cancellation criterion or its closed nullity census. The present claim is the all-frequency cyclotomic cancellation and exact nullity census, not a new general partition-function construction.

## Limitations

The formula is specialized to three colours and simple cycles with at least three vertices. It does not classify all nonzero multiplier magnitudes or their multiplicities, nor give sharp inverse norms for all lengths. Bounded literature comparison does not exclude an equivalent earlier character-weighted chromatic or Potts identity under different terminology. The checker is finite; no independent mathematical validation has been conducted.

## References

1. S.-C. Chang and R. Shrock, *Structure of the Partition Function and Transfer Matrices for the Potts Model in a Magnetic Field on Lattice Strips*, arXiv:0907.0925v1, first public 2009-07-06; https://arxiv.org/html/0907.0925v2. Section VIII.1 treats the cyclic one-row case.
2. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182v1, first public 2010-09-07; https://arxiv.org/abs/1009.1182. Sections I, II, X and XII describe uniform subset-weighted fields and cycle calculations.
3. *Sharp universal Fourier sampling stability on proper colourings of cycles*, published research record 8dc8f90856db, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-universal-fourier-sampling-stability-on-proper-colourings--8dc8f90856db. Its stated scope is the constant and first-coordinate Fourier characters.
4. M. Beck, B. Braun and A. Cornejo, *Generating functions of q-chromatic polynomials*, arXiv:2509.22946v1, first public 2025-09-26; https://arxiv.org/abs/2509.22946. Sections 1 and 3 give general weighted-colouring generating functions, without an all-frequency cycle nullity formula.
