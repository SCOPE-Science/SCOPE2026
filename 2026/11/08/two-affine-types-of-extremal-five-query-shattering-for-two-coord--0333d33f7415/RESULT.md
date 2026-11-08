# Two affine types of extremal five-query shattering for two-coordinate parity

## Finding
Let \(\mathcal P_{11}=\{x\mapsto x_i\oplus x_j:1\le i<j\le11\}\) be the class of exactly-two-coordinate parity functions on \(\mathbb F_2^{11}\). A five-point query support is shattered when each of the 32 binary response patterns occurs among these functions. Associate to its five query points the eleven column profiles in \(\mathbb F_2^5\). Then every shattered support has **ten distinct profiles, one occurring twice**. Up to an affine automorphism of \(\mathbb F_2^5\) and a permutation of the eleven coordinate positions, there are exactly **two** such profile multisets:

\[
A_0\cup\{0\}\quad\text{or}\quad A_0\cup\{8\},\qquad
A_0=\{0,1,2,3,4,5,6,8,16,31\}.
\]

Here integers denote five-bit vectors, and all additions are bitwise XOR. The two types are inequivalent. Moreover every ten-element additive difference basis of \(\mathbb F_2^5\), i.e. every set \(A\) such that \(\{a\oplus b:a,b\in A,\ a\ne b\}=\mathbb F_2^5\setminus\{0\}\), is affinely equivalent to \(A_0\). There are precisely **317,440** labeled ten-element difference bases; their stabilizer in \(\operatorname{AGL}(5,2)\) has order **1,008**. Its action on the ten points has orbit sizes seven and three, explaining exactly the two duplicate-profile types.

These conclusions **classify extremal witnesses** at the first five-query threshold. The minimum difference-basis size ten, the associated shattering criterion, and the corresponding VC-dimension threshold were previously known or obtained and are **not** claimed as new here.

## Assumptions and scope
Work over the binary vector space \(\mathbb F_2^5\); an affine equivalence on profiles may include any invertible binary linear transformation and translation. Coordinate permutations are applied to the eleven input-coordinate positions, not to the profile vector's five labeled bit positions. This is a classification of five-query profile multisets under that specified group, **not** a classification up to mere permutation of the five queries, and not an assertion about larger supports or different sparse-parity classes. All 55 functions in \(\mathcal P_{11}\) are distinct.

## Proof
**1. Query supports and difference bases.** For five distinct input queries \(x^{(1)},\ldots,x^{(5)}\), write \(v_i=(x^{(1)}_i,\ldots,x^{(5)}_i)\in\mathbb F_2^5\) for coordinate \(i\). The response vector of the parity hypothesis indexed by \(i<j\) is \(v_i\oplus v_j\). Hence shattering is equivalent to obtaining every vector in \(\mathbb F_2^5\) as an XOR of two **distinct-coordinate** profiles. The zero vector requires a repeated profile; the 31 nonzero vectors require the distinct profile set to be a difference basis. Since no difference basis has fewer than ten points (also recorded in Banakh--Gavrylkiv's table for this group), with exactly eleven columns there must be ten distinct profiles and exactly one repetition.

**2. Exhaustive affine normalization.** Any difference basis has full affine span: otherwise all of its pairwise XOR differences lie in a proper linear subspace and cannot cover all 31 nonzero vectors. Thus any ten-point difference basis contains an ordered affine frame of six points. An affine map sends this frame to \((0,1,2,4,8,16)\), denoted \(F\). Consequently, after normalization, any difference basis is \(F\) together with four of the other 26 vectors in \(\mathbb F_2^5\). The standalone exact integer checker enumerates all \(\binom{26}{4}=14,950\) normalized candidates, tests their distinct-pair XOR unions against all 31 nonzero vectors, and finds exactly 80 covering ten-sets. It also checks all \(\binom{26}{3}=2,600\) nine-point normalized candidates, none covering (largest pair-XOR union size 28). Together with the full-span argument, this proves the required finite negative assertion, without a sampling assumption.

**3. One affine orbit.** Set \(A_0=\{0,1,2,3,4,5,6,8,16,31\}\). Its pair differences cover all 31 nonzero vectors directly. Enumerate every ordered affine-independent six-point frame inside \(A_0\); for each frame construct the inverse affine map sending it to \(F\), then record the image of all ten points. There are exactly 80,640 such ordered frames and their normalized ten-set images comprise **exactly the same 80 candidates** as in step 2. Thus any ten-element difference basis is affinely equivalent to \(A_0\). Among these ordered frames, exactly 1,008 generate affine maps stabilizing \(A_0\), giving a stabilizer order 1,008 in the whole affine group. Since \(|\operatorname{AGL}(5,2)|=32\cdot\prod_{i=0}^{4}(32-2^i)=319,979,520\), orbit--stabilizer yields \(319,979,520/1,008=317,440\) different ten-sets. The identity \(317,440\cdot80,640=319,979,520\cdot80\) independently double-counts normalized pairs.

**4. Exactly two inequivalent repetitions.** Directly accumulating the images of each point under the 1,008 stabilizing affine maps yields the two orbits
\[
\{0,1,2,3,4,5,6\}\quad\text{and}\quad\{8,16,31\}.
\]
Therefore, up to affine equivalence, a repeated profile has one representative in either orbit, and these exhaust all choices. For a directly checkable separating invariant, the set \(A_0\) contains exactly seven affine planes (four-element sets whose XOR is zero). Each of its seven first-orbit points belongs to four such planes, whereas none of the three second-orbit points belongs to any. The number of such affine planes through the repeated profile is invariant, so the two types cannot be equivalent. Both are shattered because each has a duplicated profile giving the zero response, while \(A_0\) supplies all 31 nonzero responses. This completes the classification.

## Verification
Run `python3 verify_sparse_parity.py` using Python's standard library. The program performs the complete finite searches of steps 2--4, constructs every normalized orbit image, checks both duplicate-profile types, and independently checks the affine-plane invariant. Expected terminal marker: `SPARSE_PARITY_FIVE_SHATTERING_PASS`; expected counts: 2,600 nine-sets, 14,950 ten-sets, 80 covering normalized candidates, 80,640 ordered frames, 1,008 stabilizer maps, 317,440 ten-bases, seven affine planes and two point orbits. The enumeration is exhaustive **because of the proved affine normalization**; the code alone would not prove general affine completeness without that reduction.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (2021) study VC and Littlestone dimensions of **full linear zero-set families**, rather than the 11-coordinate exactly-two-sparse parity restriction or orbit classification of its extremal query-profile witnesses. Banakh and Gavrylkiv (2017) already list the **minimum difference-basis cardinality ten** for \((\mathbb Z/2\mathbb Z)^5\); that minimum and the shattering threshold are not original claims here. The present claim is the affine uniqueness, exact enumeration of all minimizing ten-sets, and the two inequivalent choices of duplicated profile. Searches of related mathematical records under additive-basis, difference-basis, affine-orbit and sparse-parity terminology did not reveal the exact orbit classification, but negative searches do not establish priority.

## Limitations
The proof is an exact finite classification of a natural small extremal case; no pattern for higher ambient binary dimension is asserted. The affine-orbit count and repeated-profile classes require independent human priority review: an earlier difference-basis classification under another name could subsume them. Reproducibility requires Python 3 but no external libraries. No independent mathematical audit is claimed.

## References
- V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first posted 10 September 2021), https://arxiv.org/abs/2109.04805.
- T. Banakh, V. Gavrylkiv, *Difference bases in finite Abelian groups*, arXiv:1704.02471 (first posted 8 April 2017), https://arxiv.org/abs/1704.02471. In particular its table for elementary abelian groups records minimum ten in the binary five-space.
