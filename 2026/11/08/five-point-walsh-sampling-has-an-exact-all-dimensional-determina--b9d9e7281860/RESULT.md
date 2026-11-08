# Five-point Walsh sampling has an exact all-dimensional determinant distribution
## Finding
For every integer \(d\ge4\), write \(Q=2^d\), \(G=\mathbb F_2^d\), and consider the unnormalized Walsh--Fourier matrix
\[
W_{a,b}=(-1)^{a\cdot b},\qquad a,b\in G.
\]
For each \(\delta\ge0\), let \(N_\delta(Q)\) count **ordered pairs of unordered five-element subsets** \((A,B)\) of \(G\) such that \(|\det W[A,B]|=\delta\). Define
\[
R_4(Q)=\frac{Q(Q-1)(Q-2)(Q-4)(Q-8)}{120},\qquad
R_3(Q)=\binom Q5-R_4(Q).
\]
Then \(N_\delta(Q)=0\) unless \(\delta\in\{0,16,32,48\}\), and **every** multiplicity is
\[
\begin{aligned}
N_{16}(Q)&=2672R_4(Q)(Q/16)^5,\\
N_{32}(Q)&=320R_4(Q)(Q/16)^5+32R_3(Q)(Q/8)^5,\\
N_{48}(Q)&=16R_4(Q)(Q/16)^5,\\
N_0(Q)&=\binom Q5^2-N_{16}(Q)-N_{32}(Q)-N_{48}(Q).
\end{aligned}
\]
In particular the **maximum five-point sampling determinant is exactly \(48\)**, attained by precisely \(16R_4(Q)(Q/16)^5\) pairs. For fixed affine-independent \(A\), the 16 optimal projected column sets are the 16 translates in \(\mathbb F_2^4\) of \(\{0,3,5,9,14\}\), with each projected point admitting \(Q/16\) lifts. No affinely dependent \(A\) attains \(48\).

For \(Q=16\), the counts corresponding to \(\delta=0,16,32,48\) are respectively
\[
(9{,}273{,}600,\ 7{,}182{,}336,\ 2{,}580{,}480,\ 43{,}008).
\]
As \(d\to\infty\), the corresponding probabilities among the \(\binom Q5^2\) row-column pairs converge to
\[
\frac1{8192}(5372,2505,300,15).
\]
The known order-16 numerical determinant distribution is not asserted to be new; the scope of the classification is every dimension and the explicit affine-orbit lift.

## Assumptions and scope
Row and column sets have cardinality five; their internal order changes only the determinant sign. The field is \(\mathbb F_2\), the transform is unnormalized, and determinants are taken over the integers (equivalently over \(\mathbb C\)). The result applies to the Sylvester Walsh character table for all \(d\ge4\), not to arbitrary Hadamard matrices. With the unitary Fourier normalization \(Q^{-1/2}W\), each determinant magnitude is multiplied by \(Q^{-5/2}\).

## Proof
**1. Affine row types.** A five-element set cannot have affine dimension below three because an affine plane over \(\mathbb F_2\) has only four points. Dimension four means an affine-independent five-tuple. Dimension three means there is a unique nonzero affine dependence: over \(\mathbb F_2\) any dependence of distinct points is an even-cardinality subset, hence a four-point affine circuit, and the fifth point lies outside its affine plane. All five-point row sets thus fall in precisely two affine orbits with representatives
\[
A_3=\{0,1,2,4,7\}\subset\mathbb F_2^3,
\qquad A_4=\{0,1,2,4,8\}\subset\mathbb F_2^4.
\]
Here integers denote binary coordinate vectors. The number of ordered affine-independent five-tuples is \(Q(Q-1)(Q-2)(Q-4)(Q-8)\), since after the first point each successive difference must avoid the span of the previous differences. Dividing by \(5!\) proves \(R_4(Q)\); subtraction yields \(R_3(Q)\).

**2. Exact finite local determinants.** After translating the row set and applying an invertible linear change of coordinates, a row set is one of the two representatives. These operations permute projected character labels or change column signs, so do not alter absolute determinants. The exact local tables for five-element projected column subsets are:
\[
\begin{array}{c|rrrr|r}
\text{row type}&0&16&32&48&\text{total}\\\hline
A_3\;(8\text{ columns})&24&0&32&0&56\\
A_4\;(16\text{ columns})&1360&2672&320&16&4368.
\end{array}
\]
A second, smaller enumeration derives the local tables transparently. Translate a selected projected column to \(0\), subtract the all-ones Walsh row from the four remaining rows, and expand along that first row. The absolute \(5\times5\) Walsh determinant becomes \(16\) times the absolute determinant of a \(4\times4\) zero-one matrix whose entries are the incidences \(a\cdot b\bmod2\), for the four nonzero rows and the four nonzero columns. Over all anchored four-element column sets, this gives binary-determinant counts \((0:15,2:20)\) for \(A_3\), and \((0:425,1:835,2:100,3:5)\) for \(A_4\). There are respectively \(\binom74=35\) and \(\binom{15}4=1365\) such configurations. Translating all five-element projected column sets and designating one of five anchors shows that each anchored count is multiplied by \(2^r/5\), recovering the local tables exactly.

The same tables follow directly by enumerating every strictly increasing five-tuple of columns and calculating its integer determinant by the alternating-permutation formula. The accompanying standalone program `verify_walsh_five.py` independently rechecks every entry via exact fraction-free elimination and the permutation formula; these are the entire \(\binom85=56\) and \(\binom{16}5=4368\) local domains, not random samples. It also checks that the 16 local \(48\)-determinant sets are precisely all translations of \(\{0,3,5,9,14\}\), which are distinct.

**3. Exact lifting.** For a fixed five-point row set \(A\) of affine dimension \(r\in\{3,4\}\), the Walsh values on its rows depend, up to signs, only on the image of a column index in the \(r\)-dimensional dual quotient. Every image has exactly \(Q/2^r\) preimages. A five-column choice having two equal images gives two proportional sampled columns and determinant zero. For each fixed five-element set of *distinct* quotient images, each point has \(Q/2^r\) independent possible lifts, giving exactly \((Q/2^r)^5\) five-element column sets. Combining this with the exact local tables and the numbers \(R_3,R_4\) proves the four displayed multiplicities for every \(d\ge4\).

**4. Maximality, limiting law, consistency.** The local tables show \(48\) is the largest possible absolute determinant, and it occurs for every affine-independent row set, giving the precise number of maximizers. The proportion of affine-independent five-point row sets tends to one. For such a row set, five independently uniform columns have limiting distinct-projection determinant probabilities \(2672\cdot5!/16^5\), \(320\cdot5!/16^5\), and \(16\cdot5!/16^5\) for magnitudes \(16,32,48\), respectively. The remaining probability is zero; simplification gives the four fractions above. Independently, orthogonality \(WW^*=QI\) and Cauchy--Binet imply
\[
256N_{16}(Q)+1024N_{32}(Q)+2304N_{48}(Q)=\binom Q5 Q^5,
\]
which agrees identically with the formulas and serves as a separate arithmetic check.

## Verification
Use Python 3 standard library to run `python3 verify_walsh_five.py`. Its local exhaustive stage evaluates all \(4424\) distinct 5-column subsets across the two row representatives, using exact Bareiss and exact alternating-permutation determinants (two algorithmically different integer computations). It separately enumerates \(35+1365\) anchored four-by-four binary incidence determinants, checks the resulting multiplicities, and then verifies all four global count formulas and the independent Cauchy--Binet identity for dimensions \(4\) through \(9\), and prints `WALSH_FIVE_DETERMINANT_HISTOGRAM_PASS`. The all-dimension assertion rests on the structural affine-orbit and projection-lifting proof, not on tests restricted to these dimensions.

## Relationship to prior work
Krahmer, Pfander and Rashkov develop support-rank criteria for finite-group Fourier uncertainty and include numerical data for groups of order \(16\), but no all-dimensional five-by-five determinant histogram. Brent and Osborn establish mean-square identities and exact singular-minor counts for sizes two and three, while their *On minors of maximal determinant matrices* reports **numerical multiplicities for all submatrix sizes of maximal-determinant matrices through order \(21\)**, including the Sylvester-equivalent order-\(16\) class: their supplementary `0_mod_4.pdf` table, order `16(a)`, records precisely \(9{,}273{,}600,7{,}182{,}336,2{,}580{,}480,43{,}008\) for determinant magnitudes \(0,16,32,48\). The \(d=4\) numerical counts therefore have prior coverage and are retained here as a check, not a novelty claim. Their finite tables and general Cauchy--Binet identity alone do not establish the stated formulas for all \(d\ge4\), the dimension-independent two-affine-orbit lifting, or the translated optimizer classification for all dimensions. Kravvaritis and Mitrouli investigate possible minors and algorithms for binary (zero-one) Hadamard cores and give the known maximum determinant \(48\) at order five; that maximum is not new. A previously published characterization of the small-minor incidence distribution under alternate design-theoretic terminology would still threaten historical priority.

## Limitations
This is an exact theorem for the Sylvester family and five-by-five minors; it does not classify other Hadamard equivalence classes or larger minor orders. The two local tables are established by a fully specified finite exhaustive exact-arithmetic certificate, not a symbolic reduction to a closed combinatorial classification of arbitrary five-by-five sign matrices. The order-16 histogram and the general maximum \(48\) were known. The originality claim pertains only to the all-dimensional distribution, affine lifting, and optimizer classification. Independent mathematical validation has not been performed; historical-priority searches are bounded.

## References
1. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493 (first public 2006-11-16), https://arxiv.org/abs/math/0611493.
2. R. P. Brent, J.-a. H. Osborn, *Bounds on minors of binary matrices*, arXiv:1208.3330 (2012), https://arxiv.org/abs/1208.3330.
3. R. P. Brent, J.-a. H. Osborn, *On minors of maximal determinant matrices*, arXiv:1208.3819 (2012), https://arxiv.org/abs/1208.3819. Supplementary table: https://maths-people.anu.edu.au/~brent/maxdet/minors/0_mod_4.pdf (order 16(a), five-minor distribution).
4. C. Kravvaritis, M. Mitrouli, *A technique for computing minors of binary Hadamard matrices and application to the growth problem*, Electron. Trans. Numer. Anal. 31 (2008), 49--67, https://etna.ricam.oeaw.ac.at/vol.31.2008/pp49-67.dir/pp49-67.pdf.
5. J. Seberry, M. Mitrouli, *Some remarks on Hadamard matrices*, Cryptography and Communications 2 (2010), 293--306, DOI 10.1007/s12095-010-0036-9.
