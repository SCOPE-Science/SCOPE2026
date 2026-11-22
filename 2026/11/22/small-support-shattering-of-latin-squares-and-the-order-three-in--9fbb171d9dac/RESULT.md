# Small-support shattering of Latin squares and the order-three incidence complex

## Finding

Identify a Latin square of order \(n\) with its \(n^2\) positive triples \((r,c,s)\) in \([n]^3\). Let \(\mathcal L_n\) be the family of **all** such labelled squares, considered as Boolean concepts on the universe \([n]^3\). A query support \(S\) is shattered when every binary assignment to its triples is induced by some member of \(\mathcal L_n\).

**Uniform sharp small-support theorem.** For every integer \(n\ge2\) and every \(S\subseteq[n]^3\) with \(|S|\le n-1\), \(S\) is shattered if and only if no two distinct triples of \(S\) agree in two coordinates. Thus up to size \(n-1\), the shattering complex is the partial-Latin-square compatibility complex. The cutoff is best possible for every \(n\ge2\): a full row of \(n\) positive triples from any Latin square is compatible but is not shattered.

**Exact order-three boundary.** The 12 labelled order-three squares have complete support-shattering polynomial
\[
\Phi_3(z)=1+27z+270z^2+216z^3.
\]
A compatible triple is shattered exactly when each of its three pairs agrees in exactly one coordinate and the three coordinates so shared are different. Call such a configuration a *Latin triangle*. There are 216 Latin triangles, all maximal shattered three-faces. There are also exactly 108 maximal shattered pairs: the compatible pairs whose endpoints differ in all three coordinates. No shattered support has four elements, and \(\operatorname{VCdim}(\mathcal L_3)=3\).

The resulting two-dimensional simplicial shattering complex \(K_3\) is nonpure. Its reduced homology over \(\mathbb F_2\) is concentrated in degrees one and two, with
\[
\dim_{\mathbb F_2}\widetilde H_1(K_3;\mathbb F_2)=111,
\qquad
\dim_{\mathbb F_2}\widetilde H_2(K_3;\mathbb F_2)=83.
\]
In particular, its 216 triangular faces have boundary-map rank 133 over \(\mathbb F_2\).

## Assumptions and scope

All squares, coordinates, and supports are *labelled*. For arbitrary \(n\), only the degree-\(\le n-1\) characterization and the failure at size \(n\) are asserted; the full polynomial is computed only for order three. The claimed homology is over \(\mathbb F_2\), not integral homology or homotopy type. A pair of triples is *compatible* precisely when it does not prescribe two different entries in a cell or repeat the same symbol within a row or column; equivalently, it shares at most one coordinate.

## Proof

1. **Necessity.** If two queries agree in two coordinates, they are forbidden from being simultaneously positive in any Latin square. Therefore every shattered support is pairwise compatible.

2. **Uniform sufficiency for \(|S|=k\le n-1\).** Fix any prescribed zero–one labelling of a pairwise compatible support. Fill all cells corresponding to positive queries with their prescribed symbols. These entries form a partial Latin square. Next process each negative query \((r,c,s)\), choosing a symbol different from \(s\), from any previously used symbol in row \(r\), and from any previously used symbol in column \(c\). At most \(k-1\) other previously inserted symbols, together with the forbidden \(s\), exclude at most \(k\le n-1\) symbols, so there is an available choice. All selected cells are distinct and the resulting partial Latin square has exactly \(k\) entries. Smetaniuk's proof of Evans' conjecture says that any partial Latin square of order \(n\) with at most \(n-1\) entries extends to a Latin square. The completion realizes the desired trace. This applies separately to every binary assignment.

3. **Sharpness.** Select all \(n\) entries of one row of a Latin square. They form a compatible support. Their first \(n-1\) positive answers force the remaining symbol in that row, so a trace with those answers positive and the final answer negative cannot occur.

4. **Order-three pair and triple counts.** Every order-three Latin square is a coordinate relabelling of the cyclic table \(L(r,c)=r+c\pmod3\), and exactly 12 distinct labelled squares result. By the natural coordinate symmetries, each of the 27 possible entries occurs in four squares. Two compatible entries occur together in two squares if they agree in exactly one coordinate and in one square if they agree in none; incompatible pairs occur together in none. Thus all \(\binom{27}{2}-81=270\) compatible pairs are shattered, by step 2.

   If a triple \(S\) is shattered, the seven nonzero Boolean traces must each occur at least once. The total number of positive incidences between the twelve squares and the three selected entries is exactly \(3\cdot4=12\), which is already the sum of the Hamming weights of the seven nonzero patterns. Consequently every nonzero trace occurs exactly once. In particular, each pair of selected entries appears jointly in exactly two squares and the three jointly occur in exactly one square. Each pair must therefore agree in precisely one coordinate. If two pairs shared the same coordinate, all three entries would occupy one row, column, or symbol fibre and would jointly occur in two squares, a contradiction. Thus the three coordinate equalities are different.

   Conversely, any triple having these three different pair-equality coordinates is equivalent by row, column, and symbol relabelling (and permutation of the three coordinate roles) to
   \[
   \{(0,0,0),(0,1,1),(1,0,1)\}.
   \]
   Exactly one of the twelve squares contains all three. Each pair belongs to two, each singleton to four, so inclusion–exclusion gives one occurrence of each nonzero trace and five occurrences of the empty trace. Therefore it is shattered. Fixing one entry gives 24 Latin triangles through it; division by three yields \(27\cdot24/3=216\) triangles. Every compatible pair sharing exactly one coordinate is in a Latin triangle; the pairs with no common coordinate are not. The latter number \(27\cdot 2^3/2=108\). Since \(12<2^4\), no four-point support is shattered.

5. **Mod-two boundary ranks.** The complex has \(f_0=27\), \(f_1=270\), \(f_2=216\). Its one-skeleton is connected, since every compatible pair is an edge and any incompatible pair has a compatible intermediary. Thus the vertex-to-edge boundary has rank 26. Construct the 270-by-216 edge–triangle incidence matrix over \(\mathbb F_2\) and reduce by exact XOR elimination. Its rank is 133, independently reproduced by the two attached standalone programs. Hence \(\widetilde\beta_1=270-26-133=111\) and \(\widetilde\beta_2=216-133=83\). There are no higher-dimensional faces and reduced degree-zero homology vanishes.

## Verification

Run `python3 verify_latin.py` with Python 3, then `g++ -std=c++17 -O2 verify_latin.cpp -o verify_latin && ./verify_latin` with a C++17 compiler. Both programs reconstruct the twelve order-three squares by distinct methods; both enumerate all supports through size four and compute the binary boundary rank. The Python program additionally reconstructs all 576 order-four Latin squares and checks that all 25,920 pairwise compatible three-point supports are shattered, as the uniform theorem predicts. Expected output markers are `LATIN_TRACES_PASS`, `LATIN_MOD2_PASS`, `LATIN_ORDER4_TRIPLE_PASS`, and `LATIN_ISOTOPE_PASS`. No approximation, random sampling, or external data file is used.

## Relationship to prior work

Hatami and Qian [1] introduced exactly this Latin-square concept class, representing each Latin square as a subset of \([n]^3\), and proved asymptotic lower bounds for its VC and recursive teaching dimensions. Their stated results do not give the exact order-three shattering complex, the pair/triple obstruction, or its homology. The representation of Latin squares as three-dimensional Latin boxes in Luria and Simkin [2] supplies a complementary completion/avoidance viewpoint; their theorems concern random support thresholds rather than Boolean traces. The sharp small-support argument uses Smetaniuk's classical partial-Latin-square completion theorem, as stated in [3]; that theorem itself and the bound of \(n-1\) are **not** claimed as new. Benediktsson, Macpherson, and Adler [4] study VC dimensions of a different incidence family, neighborhoods of Hamming and Johnson graphs, and do not imply the present classification.

A distinct published classification of the *complex of all partial Latin squares of order three* has a different ground concept and a different face set; it is not the Boolean shattered-support complex of the 12 completed squares. Searches of indexed prior research and the cited texts did not identify an exact equivalent to the stated combined order-three face/homology result. This is an originality assessment within accessible evidence, not a proof of historical novelty.

## Limitations

The exact homology ranks are supported by reproducible finite field elimination, not an intrinsic closed-form topological proof; integral torsion and homotopy type are not determined. Beyond the sharply classified first \(n-1\) support sizes and the obstruction at \(n\), no all-order shattering polynomial is asserted. Earlier or unindexed finite Latin-square computations may contain the same finite data, and independent priority review is still necessary.

## References

[1] H. Hatami and Y. Qian, *Teaching dimension, VC dimension, and critical sets in Latin squares*, arXiv:1606.00032 (first posted 2016-05-31), https://arxiv.org/html/1606.00032v2 .

[2] Z. Luria and M. Simkin, *On the Threshold Problem for Latin Boxes*, arXiv:1711.09741 (first posted 2017-11-27), https://arxiv.org/abs/1711.09741 .

[3] B. Smetaniuk, proof of Evans' conjecture (1981), as stated in *On avoiding odd partial Latin squares and \(r\)-multi Latin squares*, *Discrete Mathematics* (2007), https://doi.org/10.1016/j.disc.2006.05.028 .

[4] B. G. Benediktsson, D. Macpherson, and I. Adler, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, arXiv:2007.16042 (first posted 2020-07-31), https://arxiv.org/abs/2007.16042 .
