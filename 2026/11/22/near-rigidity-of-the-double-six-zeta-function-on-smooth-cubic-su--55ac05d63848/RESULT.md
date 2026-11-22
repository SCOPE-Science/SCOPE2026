# Near-rigidity of the double-six zeta function on smooth cubic surfaces

## Finding
For every smooth cubic surface \(S\) over any finite field \(\mathbb F_q\), let \(\mathcal D(S)\) be the finite étale scheme corresponding to its \(36\) geometric **unordered Schläfli double-sixes**, and let \(\mathcal L(S)\) denote its \(27\) geometric lines. The zeta function \(Z(\mathcal D(S),T)\) determines the Frobenius conjugacy class in \(W(E_6)\) **up to exactly one two-class ambiguity** among the \(25\) possible classes. It assumes exactly \(24\) distinct forms as the Frobenius class varies.

The single ambiguity occurs for the two order-four classes denoted \((1^2,4)\) and \((2,4)\) in the virtual-cycle notation of Das. Both yield
\[
Z(\mathcal D(S),T)=\frac{1}{(1-T)^2(1-T^2)^3(1-T^4)^7},
\]
but their line-scheme zeta functions are respectively
\[
\frac{1}{(1-T)^5(1-T^2)(1-T^4)^5}
\qquad\text{and}\qquad
\frac{1}{(1-T)(1-T^2)^3(1-T^4)^5}.
\]
In the same order they have \(5\) and \(1\) rational lines, arithmetic Picard ranks \(4\) and \(3\), and Frobenius traces on the geometric Picard group \(3\) and \(1\). In particular their surface point counts are respectively \(q^2+3q+1\) and \(q^2+q+1\). Both types occur as smooth cubic surfaces over every finite field with \(q\ge7\) by the known inverse-Galois realization theorem.

Consequently the pair
\[
\bigl(Z(\mathcal D(S),T),\,\#\mathcal L(S)(\mathbb F_q)\bigr)
\]
**uniquely recovers the Frobenius conjugacy class** and hence the zeta functions of all finite étale geometric configurations functorially defined by the \(27\) lines. This theorem does not assert that a zeta function distinguishes isomorphism classes of surfaces.

## Assumptions and scope
A sixer is an unordered six-element collection of mutually skew geometric lines. A double-six is an unordered pair of complementary sixers, each line in one half meeting exactly five lines in the other half, with six different missing partners. No ordering of halves or constituent lines is retained. The associated finite étale scheme is the Galois set of these geometric configurations. A rational double-six therefore need not have two individually rational sixer halves.

Write the geometric surface as the blow-up of \(\mathbb P^2\) in six general-position points. In the basis \((H,E_1,\ldots,E_6)\), the intersection form is \(\mathrm{diag}(1,-1,-1,-1,-1,-1,-1)\), and its \(27\) lines have divisor classes
\[
E_i,\quad H-E_i-E_j\ (i<j),\quad 2H-\sum_{j\ne i}E_j.
\]
This description and the Weyl action apply to smooth cubic surfaces in every characteristic. The theorem concerns conjugacy in the **full** Weyl group \(W(E_6)\), not a particular embedding of a cyclic group or an explicit choice of a geometric blow-down over \(\mathbb F_q\).

## Proof
**1. Geometry and the Weyl group.** Represent a divisor \(dH-\sum_i m_iE_i\) by the integer vector \((d,m_1,\ldots,m_6)\), with pairing \((d,m)\cdot(e,n)=de-\sum_i m_in_i\). Use the six simple roots
\[
E_1-E_2,\ E_2-E_3,\ E_3-E_4,\ E_4-E_5,\ E_5-E_6,\ H-E_1-E_2-E_3.
\]
Each root has square \(-2\), and its reflection is \(s_r(v)=v+(v\cdot r)r\). Acting on the above \(27\) line classes, these reflections generate \(W(E_6)\) as an explicitly faithful permutation group. Exhaustive closure produces \(51\,840\) permutations, the known order of \(W(E_6)\).

**2. Complete double-six construction.** Among all \(\binom{27}{6}=296\,010\) six-element subsets of lines, retain exactly those whose \(15\) pairs have intersection number zero. There are exactly \(72\) sixers. For a sixer \(A\), define \(B(A)\) to be the set of lines meeting exactly five members of \(A\). In each of the \(72\) cases this set contains six mutually skew lines; the map \(A\mapsto B(A)\) is a fixed-point-free involution. Thus the \(36\) distinct unordered pairs \(\{A,B(A)\}\) are all the double-sixes. Independently, the orbit under \(W(E_6)\) of the standard pair \(\{\{E_i\},\{2H-\sum_{j\ne i}E_j\}\)\) gives the identical \(36\) pairs. This establishes the complete finite universe without assuming a table of configurations.

**3. Exhaustive conjugacy and splitting.** Starting from the identity and multiplying by all six simple reflections gives all \(51\,840\) group elements. For each previously unseen element, repeatedly conjugate by the six generators to obtain its entire conjugacy class. The procedure partitions the group into exactly \(25\) classes, with class sizes totaling \(51\,840\). On each class representative compute the permutations of the \(27\) lines and the \(36\) unordered double-sixes, then their cycle decompositions. The full, independently reproducible \(25\)-row certificate is `certificate.csv`, generated and checked by `verify.py` using integer operations only.

The \(25\) line permutation spectra have \(20\) distinct values; the double-six spectra have exactly \(24\). Comparing complete double-six cycle multisets gives one and only one duplicate, with cycle type \(1^2 2^3 4^7\). Its two line spectra are \(1^5 2^1 4^5\) and \(1^1 2^3 4^5\), so their numbers of rational lines are \(5\) and \(1\). The ordered pairs consisting of the double-six cycle type and rational-line count are therefore pairwise distinct for all \(25\) classes. As a finite étale scheme with \(a_d\) orbits of length \(d\) has zeta function \(\prod_d(1-T^d)^{-a_d}\), these finite computations imply the asserted classification for **every** finite-field cubic surface.

**4. The geometric arithmetic distinction is genuine.** For either ambiguous class, the action on \(H\) is recovered from invariance of \(-K_S=3H-\sum_iE_i\) and its action on the six \(E_i\). Exact integer matrix calculations give \((\mathrm{tr},\mathrm{rank}\,\mathrm{Pic}^{F})=(3,4)\) and \((1,3)\). The standard cohomological point-count formula for a smooth cubic surface is \(\#S(\mathbb F_q)=1+q\,\mathrm{tr}(F\mid\mathrm{Pic}\,\overline S)+q^2\). The inverse-Galois classification of Loughran–Trepalin, Theorem 1.1, supplies actual smooth cubic surfaces of both Frobenius types over every field with \(q\ge7\), proving that the ambiguity is not merely formal group theory.

## Verification
Run `python3 verify.py certificate.csv` in a directory containing the two files, using the Python standard library only. The program derives the \(27\) line classes, checks all simple reflections, enumerates every group element and conjugacy class, independently reconstructs the double-six set by complementary sixers and by a Weyl orbit, checks the full \(25\)-row CSV, checks the unique spectral collision and its two Picard invariants, and prints `VERIFIED_E6_51840_CLASSES_25_DOUBLE_SIX_SPECTRA_24_UNIQUE_COLLISION_1_BASE_LINE_SPLITS` on success. The same certificate was reproduced under multiple Python hash seeds. This is an **exhaustive finite verification of the full geometric action**, not an extrapolation from finitely many sampled finite fields.

## Relationship to prior work
Das, *Arithmetic statistics on cubic surfaces* (2020), gives the \(25\) Frobenius conjugacy classes, the general marked-line arithmetic framework, and class-distribution tables; his paper does not list the \(36\)-double-six orbit spectra or assert the almost-injective inverse above. Loughran–Trepalin, *Inverse Galois problem for del Pezzo surfaces over finite fields* (2018), proves finite-field realization of the Weyl classes, but does not determine which classes share a double-six zeta function. Elsenhans–Jahnel, *Cubic surfaces with a Galois invariant double-six* (2010), study descent of individual double-sixes over number fields rather than the complete finite-field class-separation problem. A published study of sixers and double-sixes on the **Fermat cubic** computes only that special surface's Frobenius action; a published integral-incidence study computes the Smith form of double-six sums, not their class-separating permutation spectra.

This theorem therefore makes the new, exact near-rigidity comparison on the full \(25\)-class Weyl universe. It does not claim novelty for the geometric numbers \(27\), \(36\), \(72\), for the Weyl classification itself, or for the existence of the two Frobenius types.

## Limitations
The result reconstructs the Frobenius **Weyl conjugacy class**, not the cubic surface's isomorphism class or equations. The sharp examples are guaranteed by a published realization theorem; explicit surface equations for each type are not supplied. Group calculations are finite and exhaustive once the standard geometric identification is made. An older unpublished or unindexed permutation-character table could implicitly give the same class-separation result; independent mathematical audit has not been performed.

## References
1. Ronno Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183, first publicly posted 2020-02-25, https://arxiv.org/abs/2002.11183.
2. Daniel Loughran and Andrey Trepalin, *Inverse Galois problem for del Pezzo surfaces over finite fields*, arXiv:1811.06785, first posted 2018-11-16, https://arxiv.org/abs/1811.06785, Theorem 1.1.
3. Andreas-Stephan Elsenhans and Jörg Jahnel, *Cubic surfaces with a Galois invariant double-six*, *Central European Journal of Mathematics* 8 (2010), 646–661, https://doi.org/10.2478/s11533-010-0036-1.
4. *Frobenius descent of sixers and double-sixes on the Fermat cubic surface*, published mathematical finding, 2026-11-08, complete result inspected.
5. *The order-four integral reconstruction obstruction for Schläfli double-sixes*, published mathematical finding, 2026-11-02, complete result inspected.
