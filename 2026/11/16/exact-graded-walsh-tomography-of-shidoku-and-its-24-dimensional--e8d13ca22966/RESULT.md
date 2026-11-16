# Exact graded Walsh tomography of Shidoku and its 24-dimensional cubic blind space

## Finding
Let \(\mathcal S\) be the set of all completed \(4\times4\) Shidoku (Sudoku) grids, with symbols \(0,1,2,3\), and let \(x_{c,a}\) indicate that cell \(c\) contains symbol \(a\). Regard these 64 indicators as Boolean coordinates. For \(0\le d\le4\), let \(E_d\) be the real evaluation matrix whose rows are the 288 grids and whose columns are all products of at most \(d\) distinct coordinates \(x_{c,a}\), including the empty product.

The **exact degree-filtered ranks** are
\[
\bigl(\operatorname{rank}_{\mathbb R}E_0,\operatorname{rank}_{\mathbb R}E_1,\operatorname{rank}_{\mathbb R}E_2,\operatorname{rank}_{\mathbb R}E_3,\operatorname{rank}_{\mathbb R}E_4\bigr)=(1,25,151,264,288).
\]
Equivalently, the associated graded dimensions are \((1,24,126,113,24)\). These are also the ranks of the restrictions of *all* Walsh characters of Boolean degree at most \(d\), because \((-1)^{x_{c,a}}=1-2x_{c,a}\) and the two degree filtrations coincide over \(\mathbb R\).

Consequently, all up-to-three-clue joint placement marginals leave a **24-dimensional linear ambiguity** among signed measures on \(\mathcal S\); in particular, distinct strictly positive probability distributions can have identical marginals of this order. All up-to-four-clue joint placement marginals determine any probability distribution on \(\mathcal S\) uniquely. Thus degree four, and not degree three, is the exact universal tomography threshold.

## Assumptions and scope
A Shidoku grid has exactly one of four symbols in each of its 16 cells, and each row, each column and each of its four designated \(2\times2\) blocks contains all four symbols exactly once. The 64 coordinates have fixed labels \((c,a)\), with cells ordered row-major and symbols \(0,1,2,3\). All matrices are over \(\mathbb R\) unless a finite field is explicitly identified. There are 288 such labelled grids; no quotient by a symmetry group is taken. The evaluation rank counts distinct functions on this finite set, not the number of formally different Boolean monomials.

A marginal of order at most \(d\) means the expected value of any conjunction of at most \(d\) cell-symbol assertions. Such conjunctions are the columns of \(E_d\); those asserting incompatible placements are identically zero. Other fixed-coordinate indicator marginals are linear combinations of these. The claim concerns all probability laws, not merely deterministic puzzle completion.

## Proof
**Reduction to an exact integer Gram matrix.** Every completed grid has exactly 16 positive indicator coordinates. For grids \(u,v\in\mathcal S\), set
\[
a(u,v)=\#\{c:u(c)=v(c)\}.
\]
The monomial Gram matrix \(K_d=E_dE_d^{\mathsf T}\) therefore obeys the exact identity
\[
K_d(u,v)=\sum_{j=0}^{d}\binom{a(u,v)}{j},\qquad 0\le d\le4.
\]
Indeed a monomial of degree \(j\) evaluates to one at both grids exactly when its \(j\) chosen positive coordinates belong to their \(a(u,v)\) common placements. Since \(K_d\) is a real Gram matrix, its rational and real ranks agree with that of \(E_d\).

**Finite exhaustive domain.** The program `verify.py` independently enumerates all four-row choices from the 24 permutations of four symbols and rejects exactly those violating a column or a designated block. It obtains 288 distinct labelled grids. The second program `crosscheck.py` instead starts with the normalized first row \((0,1,2,3)\), obtains 12 normalized boards, and applies the 24 symbol permutations to recover precisely 288 distinct boards.

**Exact rank certificate.** The file `projector_data.zlib` consists of three consecutive signed 16-bit, little-endian \(288\times288\) matrices \(X_d\), for \(d=1,2,3\), compressed using zlib. Their respective positive integer scales are \(s_1=288\) and \(s_2=s_3=2880\). The verifier checks, entry by entry in integer arithmetic,
\[
X_d^{\mathsf T}=X_d,\qquad X_d^2=s_dX_d,\qquad K_dX_d=0,\qquad
\operatorname{tr}(X_d)=s_d(288-r_d),
\]
where \((r_1,r_2,r_3)=(25,151,264)\). Since \(X_d/s_d\) is a rational idempotent, its rank equals its trace, so these identities prove \(\operatorname{rank}_{\mathbb Q}K_d\le r_d\).

Ordinary modular Gaussian elimination modulo the prime 1009, also performed from the generated integer Gram entries, gives ranks \((1,25,151,264,288)\) for degrees zero through four. Any nonzero modular minor proves the same lower bound over \(\mathbb Q\). Combining these bounds with the exact projectors proves equality at degrees one to three. At degree zero the constant column has rank one; at degree four the modular rank is already the full row count 288. This completes the real-rank determination. No numerical eigenvalue approximations or probabilistic assumptions enter the verification of the final certificate.

**Tomography.** For each signed distribution vector \(p\in\mathbb R^{288}\), its degree-\(d\) marginal data equal \(E_d^{\mathsf T}p\). The kernel therefore has dimension \(288-\operatorname{rank}E_d\). At degree three it has dimension 24 and every kernel vector has coordinate sum zero because the constant feature occurs at degree zero. For any nonzero real kernel vector \(h\), the two vectors \(p_\pm=(1/288)\mathbf1\pm\varepsilon h\) are distinct positive probability laws with identical degree-three data for sufficiently small \(\varepsilon>0\). Degree four has zero kernel and thus determines all laws uniquely.

## Verification
Run `python3 verify.py` and `python3 crosscheck.py` in a directory containing those files and `projector_data.zlib`. Both require only the Python standard library. The first re-enumerates grids, rebuilds all five integer Gram matrices, verifies every exact projector identity and the finite-field rank lower bounds, and separately calculates feature-column ranks over \(\mathbb F_2\). The second uses a structurally different normalized-grid enumeration and bitset elimination for the degree-filtered Boolean monomial ranks in characteristic two.

Both reproduce the independent characteristic-two incidence-rank sequence \((1,25,150,264,288)\). The one-dimensional characteristic-two drop at degree two is not a contradiction: the theorem concerns the real ranks, certified by the rational integer projectors and the odd-prime lower bounds. Each verifier also confirms that no placement conjunction of size at most three isolates an individual completed board and that exactly 25,728 four-placement conjunctions isolate a single board; that four-clue count is background, not claimed as new.

## Relationship to prior work
Arnold, Lucas and Taalman (2010) give a Boolean 64-variable polynomial description and Gröbner-basis tools for Shidoku, including its 288-solution count. They do not state the degree-filtered real evaluation ranks or the exact dimension of probability-law ambiguity. Arnold, Field, Lucas and Taalman (2013) determine small Shidoku symmetry groups and the two solution orbits (96 and 192), without these Walsh sampling ranks. Previously published Shidoku clue censuses include the 25,728 uniquely determining four-clue patterns; this supports the degree-four endpoint but does not imply the exact quadratic rank 151 or the 24-dimensional cubic deficiency. The present assertion is a quantitative low-order-distribution recovery statement, not a new count of grids or an improved ordinary clue minimum.

The statistical-design literature of Fontana and Rogantin (2009) studies Sudoku indicator functions and solves a four-by-four polynomial-system instance. Only publicly available abstract and extract material could be checked here; a complete comparison with that chapter is a priority risk. This is not a claim that the chapter lacks these ranks.

## Limitations
This is an exact finite result only for ordinary \(4\times4\) Shidoku and all its 288 labelled grids. No analogous rank values, condition numbers, or bounds are claimed for larger Sudoku boards, nonstandard variants, or other characteristic fields. These rank data do not specify optimal restricted measurement subsets or an algorithm robust to measurement noise. The distinct probability laws in the proof are existential, while the embedded null projectors give an exact reproducible construction of suitable kernel vectors. A complete independent literature and mathematical audit has not been performed.

## References
1. E. Arnold, R. Field, S. Lucas, and L. Taalman, *Minimal complete Shidoku symmetry groups*, arXiv:1302.5949, first submitted 24 February 2013. https://arxiv.org/abs/1302.5949
2. E. Arnold, S. Lucas, and L. Taalman, *Gröbner Basis Representations of Sudoku*, College Mathematics Journal **41** (2010), 101–112. DOI:10.4169/074683410X480203. Lawful author-hosted full text: https://educ.jmu.edu/~arnoldea/cmjarnoldlucastaalman.pdf
3. R. Fontana and M. P. Rogantin, *Indicator function and sudoku designs*, in *Algebraic and Geometric Methods in Statistics* (2009), 203–224. DOI:10.1017/CBO9780511642401.013.
4. S. Gupta, *Shi Doku: Exploring the Mathematics of Su Doku*, including a published four-clue Shidoku census. https://theory.tifr.res.in/~sgupta/sudoku/shidoku.html
5. E. Soedarmadji and R. J. McEliece, *Iterative Decoding for Sudoku and Latin Square Codes*, 45th Allerton Conference (2007), 488–494.
