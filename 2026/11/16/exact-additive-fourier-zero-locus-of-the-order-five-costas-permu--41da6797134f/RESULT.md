# Exact additive Fourier zero locus of the order-five Costas permutation codebook

## Finding
Let \(G=(\mathbb Z/5\mathbb Z)^5\). A Costas permutation \(\pi=(\pi_0,\ldots,\pi_4)\) is a permutation of \(\{0,1,2,3,4\}\) for which, for each distance \(d\in\{1,2,3,4\}\), the \(5-d\) integers \(\pi_{i+d}-\pi_i\), \(0\le i<5-d\), are pairwise distinct. Let \(C\subset G\) be the set of all such permutations and let \(T_Cf=1_C*f\) be unnormalized convolution. Put \(\zeta=e^{2\pi i/5}\) and
\[
W_C(k)=\sum_{\pi\in C}\zeta^{\sum_{j=0}^4 k_j\pi_j},\qquad k\in G.
\]
There are exactly \(40\) elements of \(C\). The zero set \(\{k:W_C(k)=0\}\) consists of exactly \(16\) orbits of size \(20\) under the transformations \(k\mapsto ak+c\mathbf1\), where \(a\in\mathbb F_5^\times\), \(c\in\mathbb F_5\), and \(\mathbf1=(1,1,1,1,1)\). In the canonical representative convention \(k_0=0\) and the first nonzero coordinate equal to \(1\), the complete list of vanishing classes is:

| Classes already zero for all permutations | Extra classes zero only for the Costas codebook |
|---|---|
| `00100`, `00132`, `01010` | `01031` |
| `01014`, `01143`, `01201` | `01103` |
| `01313`, `01320`, `01332` | `01202` |
| `01401`, `01430`, `01433` | `01441` |

The constant-frequency orbit has no zero. Therefore
\[
\boxed{\dim\ker T_C=320,\qquad \operatorname{rank}T_C=2805.}
\]
In contrast, for the indicator \(1_P\) of all \(120\) permutations \(P\subset G\), convolution has rank \(625\) and nullity \(2500\). Exactly \(240\) Fourier frequencies vanish for both codebooks; exactly \(80\) vanish only for \(C\). The weight distribution of the \(320\) Costas zeros (number of nonzero frequency coordinates) is \(4,4,92,108,112\) in degrees \(1,2,3,4,5\), respectively.

## Assumptions and scope
Coordinates are indexed from \(0\) through \(4\); differences in the defining Costas property are computed as **ordinary integers**, not modulo \(5\). Once the forty permutations have been selected, their five entries are embedded into the additive group \(G\) and Fourier pairings are computed modulo \(5\). Convolution uses the counting measure, with no factor of \(1/|G|\). The word *rank* means the complex rank of the full translation-invariant convolution operator on functions \(G\to\mathbb C\); it is not the rank of a permutation matrix or the standard radar ambiguity function.

## Proof
**Costas enumeration.** For each of the \(5!=120\) permutations, test the four sets of differences described above. Exhaustiveness is immediate because every order-five permutation occurs once. The test accepts exactly forty permutations. This is also the classical order-five Costas count, but it is rederived here to avoid reliance on external tables.

**Cyclotomic zero criterion.** For \(k\in G\), let \(N_r(k)\) count those \(\pi\in C\) for which \(\sum_j k_j\pi_j\equiv r\pmod5\), for \(0\le r\le4\). Then \(W_C(k)=\sum_r N_r(k)\zeta^r\). Since the minimal polynomial of a primitive fifth root of unity is \(1+X+X^2+X^3+X^4\), a polynomial of degree at most four with integer coefficients vanishes at \(\zeta\) if and only if all five coefficients coincide. Consequently,
\[
W_C(k)=0\quad\Longleftrightarrow\quad N_0(k)=\cdots=N_4(k)=8.
\]
The same argument with \(P\) uses common count \(24\).

**Frequency reduction.** Every permutation satisfies \(\sum_j\pi_j=10\equiv0\pmod5\), so \(W_C(k+c\mathbf1)=W_C(k)\). For \(a\in\mathbb F_5^\times\), \(W_C(ak)\) is the Galois conjugate of \(W_C(k)\) under \(\zeta\mapsto\zeta^a\), hence vanishes exactly when \(W_C(k)\) does. The five constant frequencies form one orbit, each with multiplier \(40\); the other \(3120\) frequencies split into \(156\) orbits of size \(20\). Every nonconstant orbit has a unique representative with initial coordinate \(0\) and first nonzero subsequent coordinate \(1\). Thus there are exactly \(157\) representatives to test, counting the constant class.

**Complete finite certificate.** The supplied `certificate.json` contains, for *all 157* canonical representatives, the five integer residue counts both for \(C\) and for \(P\). Direct comparison with the cyclotomic criterion yields the sixteen Costas zero representatives in the table, twelve also zero for \(P\) and four not zero for \(P\). For these four extra representatives, the full-permutation residue vector is \((40,20,20,20,20)\), while the Costas vector is \((8,8,8,8,8)\). The other \(140\) nonconstant canonical representatives have nonconstant Costas vectors; the constant class has multiplier forty. Hence \(16\cdot20=320\) zeros and \(3125-320=2805\) nonzero multipliers. The complete direct character loop also gives the stated Hamming-weight distribution.

For \(P\), cyclically shifting all five values of each permutation by the same residue permutes \(P\), forcing all multipliers with \(\sum_j k_j\not\equiv0\pmod5\) to vanish. These account for exactly \(2500\) frequencies. The same finite certificate confirms that every one of the remaining \(625\) multipliers is nonzero. Thus \(\operatorname{rank}T_P=625\). Exactly twelve of the sixteen Costas zero orbits fall in the sum-nonzero region and the other four fall in the sum-zero region, proving the overlap numbers.

Finally, finite Fourier diagonalization on \(G\) sends the convolution operators to diagonal multipliers \(W_C\) and \(W_P\), so their ranks equal the counts of nonzero multipliers.

## Verification
The entire census is an exact finite computation with no floating-point zero tests. Run `python3 check_integer.py`; it enumerates all \(120\) permutations, checks the Costas differences, constructs all \(157\) canonical classes, tests all \(3125\) frequencies and checks the class reductions, overlap and degree counts. Independently, run `c++ -std=c++17 -O2 check_independent.cpp -o check_independent && ./check_independent`: this second program constructs all forty Costas arrays by incremental backtracking and computes all frequency residue counts directly. Both programs include assertions for the headline numbers. `certificate.json` is a complete small witness table rather than a digest or an uninspectable log.

## Relationship to prior work
Drakakis, Gow and Rickard's 2007 work establishes the Costas property and studies parity populations in finite-field Costas constructions. The 2009 paper by Drakakis, Gow, Healy and Rickard studies cross-correlations of individual arrays and their flips. Drakakis's 2010 study examines nonlinearities of individual Costas permutations, including phase sums taken *within a permutation*. Soltanalian and Stoica's 2014 paper studies efficient enumeration of Costas arrays. These are distinct from the present group Fourier transform obtained by summing *over all forty permutations*, its full zero locus, and comparison of the corresponding translation-convolution ranges. The classical Costas counts, symmetry properties and definitions are acknowledged; none is claimed as new.

## Limitations
This is an exact classification for the order-five Costas ensemble only. It does not provide a general formula for larger orders, prove radar performance gains, or assess Fourier transforms on the \(25\)-coordinate binary permutation-matrix cube. Historical searches cannot exclude an unindexed equivalent computation; the complete finite arithmetic establishes the numerical statements, not worldwide historical priority.

## References
1. K. Drakakis, R. Gow and S. Rickard, *Parity properties of Costas arrays defined via finite fields*, arXiv:0706.3313, first arXiv version 2007-06-22. https://arxiv.org/abs/0706.3313
2. K. Drakakis, R. Gow, J. Healy and S. Rickard, *Cross-Correlation Properties of Costas Arrays and Their Images under Horizontal and Vertical Flips*, *Mathematical Problems in Engineering* (2009), https://doi.org/10.1155/2008/369321 (first online 2009-02-03).
3. K. Drakakis, *On the Measurement of the (Non)linearity of Costas Permutations*, *Journal of Applied Mathematics* (2010), https://doi.org/10.1155/2010/149658 (first online 2010-06-21).
4. M. Soltanalian and P. Stoica, *A Recursive Method for Enumeration of Costas Arrays*, arXiv:1404.0173, first version 2014-04-01. https://arxiv.org/abs/1404.0173
