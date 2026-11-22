# Exact parity-split maximum nilpotency law for random brackets of triangular radicals

## Finding

Let \(q\ge2\) be a prime power, let \(\mathfrak n_n(\mathbb F_q)\) be the associative algebra of strictly upper-triangular \(n\times n\) matrices, and choose \(X,Y\) independently and uniformly from it. Write \(C=XY-YX\), and define the nilpotency index \(\nu(C)=\min\{k\ge1:C^k=0\}\). Since \(C\in\mathfrak n_n^2\), one always has \(\nu(C)\le\lceil n/2\rceil\). For \(n\ge3\), this is the exact attainable maximum.

Put \(a=(1-q^{-2})(1-q^{-1})\). For every integer \(h\ge1\), the odd-dimensional maximum-index probability is
\[
\Pr\bigl(\nu([X,Y])=h+1\mid n=2h+1\bigr)=a^h.
\]
For every \(h\ge2\), the even-dimensional probability is, with \(b_h=(1-q^{-2})(1-q^{-1})^{2h-2}\),
\[
\Pr\bigl(\nu([X,Y])=h\mid n=2h\bigr)
=(1-q^{-1})a^{h-2}\left[a+(h-1)(1-a-q^{-4})\right]
+q^{-1}\left(2a^{h-1}-b_h\right).
\]
Both formulas hold in every field characteristic, including characteristic two.

In particular, for each fixed \(q\), comparing consecutive odd and even dimensions with *the same* maximal index gives
\[
\frac{\Pr\bigl(\nu([X,Y])=h\mid n=2h\bigr)}{\Pr\bigl(\nu([X,Y])=h\mid n=2h-1\bigr)}
\sim \frac{(1-q^{-1})(1-a-q^{-4})}{a}\,h
\qquad(h\to\infty).
\]
The positive linear factor is a parity asymmetry in the image of a Lie bracket, distinct from the analogous phenomenon for unconstrained products of two matrices.

## Assumptions and scope

The variables \(X,Y\) have each strictly-upper entry independent uniform in \(\mathbb F_q\), and are mutually independent. Matrix multiplication and the additive bracket use the actual field operations; for characteristic two subtraction equals addition. The probability space has \(q^{n(n-1)}\) ordered pairs. The theorem concerns only attainment of the largest possible *associative-matrix* nilpotency index of their bracket, not the Lie nilpotence class of the whole algebra, the Jordan partition distribution, or a group commutator. For \(n=2\) the bracket is identically zero and has index one; the even formula begins at \(n=4\).

## Proof

Let \(v_i=(X_{i,i+1},Y_{i,i+1})\in\mathbb F_q^2\) be the independent uniform pairs on the first superdiagonal. Define \(\Delta_i=\det(v_i,v_{i+1})\) for \(1\le i\le n-2\). The first potentially nonzero superdiagonal of \(C\) has entries \(C_{i,i+2}=\Delta_i\). Two independent uniform vectors have nonzero determinant with probability \(a\), by first requiring the first vector nonzero, then requiring the second outside its one-dimensional span.

For \(n=2h+1\), the only potentially nonzero entry of \(C^h\) is \((C^h)_{1,2h+1}=\prod_{j=1}^h\Delta_{2j-1}\). The factors use disjoint pairs of independent \(v_i\)'s. Hence their simultaneous nonvanishing has probability \(a^h\).

For \(n=2h\) with \(h\ge2\), put \(m=h-1\). The only potentially nonzero entries of \(C^m\) are \((1,2h-1)\), \((2,2h)\), and \((1,2h)\). The first two equal
\[
U=\prod_{j=1}^{m}\Delta_{2j-1},\qquad V=\prod_{j=1}^{m}\Delta_{2j}.
\]
Thus \(\Pr(U\ne0)=\Pr(V\ne0)=a^m\). The event \(U\ne0,V\ne0\) requires all adjacent determinants along \(v_1,\ldots,v_{2h-1}\) to be nonzero and has probability \(b_h=(1-q^{-2})(1-q^{-1})^{2h-2}\). Set \(E=\{U\ne0\}\cup\{V\ne0\}\); then \(\Pr(E)=2a^m-b_h\).

For the one-long-step paths contributing to \((C^m)_{1,2h}\), let \(u_i=(X_{i,i+2},Y_{i,i+2})\) be the independent uniform second-superdiagonal pairs, independent of all \(v_i\). Put
\[
 d_i=C_{i,i+3}=\det(v_i,u_{i+1})+\det(u_i,v_{i+2}).
\]
The path expansion gives
\[
(C^m)_{1,2h}=\sum_{j=1}^{m}\left(\prod_{r<j}\Delta_{2r-1}\right)
 d_{2j-1}\left(\prod_{r>j}\Delta_{2r}\right).\tag{1}
\]
For different \(j\), these \(d_{2j-1}\) involve disjoint pairs \((u_{2j-1},u_{2j})\). Conditioned on all \(v_i\), each one is uniformly distributed on the field unless both \(v_{2j-1}\) and \(v_{2j+1}\) vanish, in which case it is zero. Therefore (1) is either deterministically zero or exactly uniform, and no independence assertion about overlapping \(\Delta_i\)'s is needed.

Call an index \(j\) active when all preceding odd determinants \(\Delta_{2r-1}\) with \(r<j\) and all succeeding even determinants \(\Delta_{2r}\) with \(r>j\) are nonzero. If every odd determinant is nonzero, an active index exists (the last). Otherwise let \(j\) be the first failed odd determinant. It is the last candidate for an active index, and an active index exists precisely when all even determinants strictly after \(j\) are nonzero. The disjoint-pair determinants in these two tests are independent. Summing over \(j\) gives
\[
\Pr(\text{some active index})=a^m+m(1-a)a^{m-1}.
\]
An active index contributes a nontrivial uniform \(d\) except on the following exceptional event: there is a unique active index \(j\) and \(v_{2j-1}=v_{2j+1}=0\). Such an event forces \(\Delta_{2j-1}=\Delta_{2j}=0\), all earlier odd determinants nonzero, and all later even determinants nonzero. Conversely those conditions with these two zero vectors characterize precisely this exceptional case. For each \(j\) its probability is \(q^{-4}a^{m-1}\), and different \(j\)'s are disjoint. Thus the event \(W\) that at least one nontrivial uniform term occurs has
\[
\Pr(W)=a^m+m(1-a-q^{-4})a^{m-1}.
\]
Since \(E\subseteq W\), on \(E\) the matrix power is certainly nonzero; on \(W\setminus E\) its sole possible nonzero entry is uniformly distributed, hence nonzero with probability \(1-q^{-1}\). Outside \(W\) the whole power is zero. Consequently
\[
\Pr(C^m\ne0)=\Pr(E)+(1-q^{-1})\bigl(\Pr(W)-\Pr(E)\bigr)
=(1-q^{-1})\Pr(W)+q^{-1}\Pr(E),
\]
which is the claimed even formula.

Both parities admit positive maximum probabilities for all admissible dimensions. For fixed \(q\), \(1-a-q^{-4}>0\), and \(b_h/a^{h-1}=(1-q^{-2})[(1-q^{-1})/(1-q^{-2})]^{h-1}\to0\). Comparing the dominant linear-in-\(h\) even term to the previous odd probability \(a^{h-1}\) proves the stated asymptotic ratio.

## Verification

The bundled `checker.py` independently enumerates the necessary first- and second-superdiagonal coefficient pairs for six prime-field configurations, then evaluates the derived probabilities as exact rational numbers. It additionally enumerates **all** pairs of full strictly-upper-triangular matrices for \(n=4\) over \(\mathbb F_2\) (4096 pairs) and \(\mathbb F_3\) (531441 pairs), constructing full commutator matrices and their powers directly rather than using the reduction. All eight tests returned PASS. These finite computations check the formulas only on the stated test cases; the proof, not enumeration, establishes the claim for all prime powers and dimensions. Run `python checker.py` with Python 3 standard library.

## Relationship to prior work

Boyko, Patera and Popovych study the strictly upper triangular Lie algebra as a nilradical, but their coadjoint-invariant classifications do not count powers of brackets of independent random elements. Fuchs and Kirillov count Jordan types under the **uniform single-matrix measure** on the entire triangular radical; the bracket pushforward measure is not this measure, so those formulas do not imply the present probabilities. Published exact bracket-fiber studies in small dimensions and an existing maximal-index theorem for **products** address different claims. The proof uses only elementary finite-field linear algebra and path expansions; neither general nilpotent-matrix Jordan counts nor product distributions are presented as original here.

## Limitations

This result does not supply the complete Jordan distribution of \([X,Y]\), nor is it a claim about group commutators or multibrackets. Finite-field checks were exhaustive only for the listed small prime-field cases. Publicly indexed comparisons do not establish historical uniqueness; closely relevant published records for low-dimensional brackets could not all be inspected in full. Publication priority should be independently checked.

## References

- V. Boyko, J. Patera, R. O. Popovych, *Invariants of solvable Lie algebras with triangular nilradicals and diagonal nilindependent elements*, arXiv:0706.2465, first public 17 June 2007; https://arxiv.org/abs/0706.2465 .
- D. Fuchs and A. Kirillov Sr., *Jordan Types of Triangular Matrices over a Finite Field*, Arnold Mathematical Journal 8 (2022), 543–559; https://doi.org/10.1007/s40598-022-00214-1 .
- *Three-stratum Lie-bracket fibers and adjoint ranks of strictly upper triangular four-by-four matrices*, published research record; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-stratum-lie-bracket-fibers-and-adjoint-ranks-of-strictly-u--b92d2e107407 .
- *Maximal nilpotency index in products of random upper triangular matrices*, published research record; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-maximal-nilpotency-index-in-products-of-random-upper-triangular--3038b4056c47 .
