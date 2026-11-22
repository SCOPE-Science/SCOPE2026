# Exact inverse-list spectrum of the cyclic mod-five adjacent-sum sensor on proper colorings

## Finding

For every integer \(n\ge2\), let \(X_n\) be the set of indexed cyclic words \(x=(x_0,\ldots,x_{n-1})\in\mathbb F_5^n\) satisfying \(x_i\ne x_{i+1}\) for all indices modulo \(n\). Observe the ordered cyclic adjacent-sum vector \(F_n(x)=y\), where \(y_i=x_i+x_{i+1}\) in \(\mathbb F_5\). Let \(A_{n,j}=|\{y\in\mathbb F_5^n:|F_n^{-1}(y)\cap X_n|=j\}|\).

**Exact all-length inverse-list distribution.** If \(n\) is odd, \(A_{n,1}=4^n-4\), all \(A_{n,j}\) for \(j\ge2\) vanish, and the remaining \(5^n-4^n+4\) output words are unreachable. If \(n=2m\) is even, for \(m\ge1\) let \(L_r\) be the Lucas sequence \(L_0=2\), \(L_1=1\), \(L_{r+2}=L_{r+1}+L_r\). Then

\[
\begin{aligned}
A_{2m,4}&=5,\\
A_{2m,3}&=2\cdot4^m+4L_{2m}-20,\\
A_{2m,2}&=2\cdot9^m-6\cdot4^m-8L_{2m}+30,\\
A_{2m,1}&=16^m-4\cdot9^m+6\cdot4^m+4L_{2m}-16.
\end{aligned}
\]

No output has five or more admissible predecessors. Consequently the image size is

\[
|F_{2m}(X_{2m})|=16^m-2\cdot9^m+2\cdot4^m-1.
\]

The five degree-four outputs are exactly the five constant output words. The full unrestricted linear map has image of size \(5^{2m-1}\) at even length; its constrained image is the whole linear image at \(n=2,4\) but first misses outputs at \(n=6\), where precisely \(360\) otherwise linearly feasible outputs are missing. For \(m\to\infty\),

\[
\frac{A_{2m,1}}{|F_{2m}(X_{2m})|}=1-2(9/16)^m+o((9/16)^m),\qquad
\frac{|F_{2m}(X_{2m})|}{5^{2m-1}}\sim5(16/25)^m.
\]

This is an inverse-list theorem for *position-indexed* words, without identifying rotations, and not a theorem about unordered adjacent-pair histograms.

## Assumptions and scope

The alphabet is the field \(\mathbb F_5\). Both the input and output coordinates are indexed and cyclic, with edges \((n-1,0)\) included. There is no probabilistic assumption and no allowance for errors or erasures. Input words must be proper colorings of the cyclic adjacency relation; observed words need not be proper. The length bound \(n\ge2\) includes the two-position cyclic case (the single distinct adjacency is tested twice). The observation is a residue sum modulo five, not an integer sum or full histogram.

## Proof

**1. Linear kernels.** Write \(P\) for the cyclic shift. The determinant of \(I+P\) is \(1-(-1)^n\). If \(n\) is odd, this is \(2\ne0\) in \(\mathbb F_5\), so the map is injective on the full space; the number of proper cycle colorings is \(4^n-4\). If \(n=2m\) is even, the linear kernel consists exactly of \((t,-t,t,-t,\ldots)\) with \(t\in\mathbb F_5\), and the full image is the hyperplane \(\sum_{i=0}^{n-1}(-1)^i y_i=0\).

**2. Exact fiber degree from signed differences.** For proper \(x\) define

\[
z_i=\frac{(-1)^i}{2}(x_{i+1}-x_i)\in\mathbb F_5^\times.
\]

A kernel shift by \((t,-t,\ldots)\) changes the signed differences to \(z_i-t\). This shifted preimage is proper precisely when \(t\notin\{z_0,\ldots,z_{n-1}\}\). Every output with a proper predecessor therefore has inverse-list size \(5-r\), where \(r\) is the number of distinct nonzero signed differences. Every allowable shift preserves \(r\), since translation preserves the size of the value-set. Hence inverse-list sizes are exactly among \(1,2,3,4\).

**3. A constrained additive-word count.** Cyclic closure gives \(\sum_{i=0}^{n-1}(-1)^iz_i=0\). Conversely, every vector \(z\in(\mathbb F_5^\times)^{2m}\) with that alternating-sum property, together with an arbitrary choice of \(x_0\in\mathbb F_5\), reconstructs exactly one proper source. Let \(T_r(m)\) count such vectors with exactly \(r\) distinct coordinate values. Because a fiber of degree \(5-r\) accounts for \(5-r\) proper sources,

\[
(5-r)A_{2m,5-r}=5T_r(m),\qquad r=1,2,3,4.
\]

For a fixed nonempty subset \(S\subseteq\mathbb F_5^\times\), let \(E_m(S)\) count two ordered length-\(m\) words with letters in \(S\) and equal coordinate sums modulo five. With \(\zeta=e^{2\pi i/5}\), the character orthogonality identity gives

\[
E_m(S)=\frac15\sum_{a=0}^{4}\left|\sum_{s\in S}\zeta^{as}\right|^{2m}.
\]

This count depends only on \(h=|S|\), for \(1\le h\le4\). Indeed, the multiplicative group of \(\mathbb F_5\) is transitive on singleton sets and on unordered two-point sets up to the common difference; the nontrivial character magnitudes for every two-point set are the two values \(\frac{3+\sqrt5}{2}\) and \(\frac{3-\sqrt5}{2}\), each occurring twice in squared modulus. Every three-point set is \(\mathbb F_5^\times\setminus\{a\}\), so its nontrivial Fourier sums are \(-(1+\zeta^{ka})\). The entire four-point set has all nontrivial character sums \(-1\). Therefore, using \(L_{2m}=((1+\sqrt5)/2)^{2m}+((1-\sqrt5)/2)^{2m}\),

\[
E_1=1,\quad E_2=\frac{4^m+2L_{2m}}5,\quad
E_3=\frac{9^m+2L_{2m}}5,\quad E_4=\frac{16^m+4}5.
\]

**4. Exact support via inclusion-exclusion.** Summing the previous counts over all \(h\)-subsets of the four nonzero field elements and inverting the subset-incidence relation yields

\[
\begin{aligned}
T_1&=4,\\
T_2&=6E_2-12,\\
T_3&=4E_3-12E_2+12,\\
T_4&=E_4-4E_3+6E_2-4.
\end{aligned}
\]

Substitution into \((5-r)A_{2m,5-r}=5T_r\) proves all four formulas. Adding the four formulas gives the stated image size. The case \(r=1\) means every signed difference is equal; hence \(x\) alternates between two distinct symbols, and its output is constant. Conversely every constant output has exactly four such proper predecessors. The asymptotics follow by comparing the leading exponential terms. The absent outputs inside the full linear-image hyperplane at length six equal \(5^5-(16^3-2\cdot9^3+2\cdot4^3-1)=360\).

## Verification

A standalone exact-integer Python program, `verify.py`, independently enumerates all \(5^n\) indexed input words at lengths \(2\le n\le8\), restricts to proper colorings, records every image and its inverse-list degree, and compares the resulting entire zero-to-five histogram against the displayed formulas. It additionally checks nonnegativity, the complete ambient histogram sum, and the proper-coloring source-incidence identity at all lengths \(2\le n\le201\). Reproduce with `python3 verify.py` in an ordinary Python 3 environment. Exhaustive small-length checks are evidence for, not replacements for, the algebraic proof above.

## Relationship to prior work

Sporring and Darkner (2022) count ambiguities arising from ordered overlapping local histograms of *binary* finite signals, and Ye and Elishco (2022) study reconstruction from *unordered* prefix/suffix and substring composition multisets. These are related reconstruction models but neither observation is this cyclic modulo-five local-sum channel with a proper-coloring input restriction. Yehezkeally and collaborators (2022) study unordered partially overlapping substrings and achievable code rates, not exact inverse-list multiplicities for additive reads. Mariot and Leporati (2015) characterize periods of preimages for linear bipermutive cellular automata without this input-language restriction; the unrestricted linear kernel is only the starting step of the present count. Takemoto and Nozaki (2020) construct constrained insertion/deletion-correcting codes under a different channel. No assertion is made that these broader mathematical areas have been exhaustively indexed or that independent priority verification has occurred.

## Limitations

The result is specific to the prime-five residue alphabet and the two-tap unit-weight cyclic sum with no equal adjacent source symbols. It does not extend unchanged to integer-valued pair sums, unordered read multisets, non-prime alphabets or arbitrary forbidden-factor constraints. The exact value of individual fibers is determined through a valid source and its signed-difference support; a general efficient image-membership algorithm for arbitrary observations is not provided. An implicit equivalent under a different constrained-additive or Potts-model formulation remains a priority risk. The findings have not undergone independent mathematical validation.

## References

- J. Sporring and S. Darkner, "Reconstructing Binary Signals from Local Histograms," *Entropy* 24(3):433 (2022), https://doi.org/10.3390/e24030433 (public 2022-03-21).
- Z. Ye and O. Elishco, "Reconstruction of a Single String from a Part of its Composition Multiset," arXiv:2208.14963 (first public 2022-08-31), https://arxiv.org/abs/2208.14963.
- Y. Yehezkeally, D. Bar-Lev, S. Marcovich and E. Yaakobi, "Reconstruction from Substrings with Partial Overlap," arXiv:2205.03933 (first public 2022-05-08), https://arxiv.org/html/2205.03933v1.
- L. Mariot and A. Leporati, "On the Periods of Spatially Periodic Preimages in Linear Bipermutive Cellular Automata," AUTOMATA 2015, https://doi.org/10.1007/978-3-662-47221-7_14.
- R. Takemoto and T. Nozaki, "Construction and Encoding Algorithm for Maximum Run-Length Limited Single Insertion/Deletion Correcting Code," arXiv:2012.13536 (2020), https://arxiv.org/html/2012.13536v1.
