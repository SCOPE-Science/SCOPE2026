# Individual left-action cycle types and sharp fixed-point bounds in triangular radical braces

## Finding

Let \(q=p^e\) be a prime power, \(n\ge2\), \(D=\binom n2\), and \(A=\mathfrak n_n(\mathbb F_q)\) the algebra of strictly upper-triangular matrices. The radical-ring brace has circle law \(a\circ b=a+b+ab\); its canonical left action is \(\lambda_a(b)=b+ab\). For \(1\le r<n\) let \(a_r\) be the northwest \(r\times r\) corner and set
\[
F_s(a)=q^{\sum_{r=1}^{n-1}(r-\operatorname{rank}(a_r^{p^s}))}\quad(s\ge0).
\]
The permutation \(\lambda_a\) on the \(q^D\) elements of \(A\) has \(F_0(a)\) fixed points and \((F_s(a)-F_{s-1}(a))/p^s\) cycles of length \(p^s\) for each \(s\ge1\), with no other lengths.

The generated action group is canonically isomorphic to \(\mathrm{UT}_{n-1}(\mathbb F_q)\). Each \(F_s(a)\) is at least \(q^{\sum_{r=1}^{n-1}\min(r,p^s)}\), and the bounds are attained simultaneously. In particular, \(F_0(a)\ge q^{n-1}\), with equality precisely when \(a_{i,i+1}\ne0\) for \(1\le i\le n-2\). This locus comprises a proportion \((1-q^{-1})^{n-2}\) of all \(a\). On it the Jordan block sizes of \(\lambda_a\) over \(\mathbb F_q\) are \(1,2,\ldots,n-1\), one of each.

## Assumptions and scope

The cycle type is for one permutation \(\lambda_a\) of the additive set \(A\), not the orbit-size distribution of the full action group or of a Yang–Baxter solution. Although \(q\) determines the numbers of points, it is the characteristic prime \(p\) that determines the possible cycle lengths. The regularity condition is empty when \(n=2\).

## Proof

Column \(r+1\) of a strictly upper-triangular matrix carries \(r\) free coordinates and is preserved under left multiplication by \(a\). The restriction of the linear map \(L_a:b\mapsto ab\) to this column module is \(a_r\). Consequently \(\lambda_a=I+L_a\) is the direct sum of \(I_r+a_r\), and \(\lambda_a^{p^s}=I+L_a^{p^s}\) in characteristic \(p\). Its \(p^s\)-th power therefore has precisely \(F_s(a)\) fixed points. Its order is a power of \(p\), because any power \(p^s\ge n-1\) kills all the nilpotent blocks of \(L_a\). Hence the difference between two consecutive fixed-point counts consists exactly of the points on cycles of length \(p^s\); division by \(p^s\) gives their number.

The circle law identifies \(a\) with \(I+a\) under matrix multiplication. The column representation has kernel consisting of matrices supported on the last column, of cardinality \(q^{n-1}\). The circle projection \(a\mapsto I_{n-1}+a_{n-1}\) is surjective with that same kernel, and its natural action on column \(n\) is faithful. This yields the group isomorphism.

Each strictly upper-triangular \(r\times r\) matrix has nullity of its \(t\)-th power at least \(\min(r,t)\), since the first \(\min(r,t)\) standard basis vectors are killed. In particular \(F_0\) is minimal only if each corner has nullity one. The largest corner has nullity one exactly when it has a single nilpotent Jordan block, or, equivalently, its \((n-2)\)-th power is nonzero. The upper-right entry of that power is \(\prod_{i=1}^{n-2}a_{i,i+1}\), its only possible nonzero entry when \(n>2\); for \(n=2\) the power is the identity of the one-dimensional corner. When the product is nonzero all smaller corners are regular by the same test. This gives the asserted Jordan blocks and equality for every lower bound. The proportion follows by counting independent first-superdiagonal coordinates.

## Verification

The proof holds over every finite field. The finite checker `check.py` and recorded `check_output.txt` test direct permutation cycles over small prime fields. Some checks concern the group-order consequence below rather than the cycle theorem. The finite checks are not the proof.

## Relationship to prior work

The radical-ring brace construction and the canonical action are classical (Rump; Guarnieri–Vendramin, §1 and §5.3). Standard unipotent power identities are used as inputs. The specific result here is the formula in simultaneous principal-corner ranks and the sharp fixed-point bounds and equality locus for the individual permutations. Jordan-type counts of a single strictly upper-triangular matrix (Yip; Fuchs–Kirillov) do not give those simultaneous corner ranks. For example, at \(n=4\) the matrices \(E_{12}\) and \(E_{23}\) have the same Jordan type in the quotient corner of size three. But their corner ranks sum to two and one, respectively, giving \(q^4\) versus \(q^5\) fixed points. Related results on sizes of full-group \(\lambda\)-orbits describe a different invariant.

The first maximal-order jump is a **known group-level consequence, not an originality claim**. At \(n=p^s+2\) the action quotient is \(\mathrm{UT}_{p^s+1}\). With \(r=p^s\), the number \((q-1)^r q^{D-r}\) of brace elements of order \(p^{s+1}\) **in their left action** comes from the regular unipotent count in the quotient, times the \(q^{n-1}\) lifts. Indeed, exactly the elements with all first-superdiagonal coordinates nonzero in the quotient have nonzero \(r\)-th nilpotent power. The same quotient probability is stated in the unitriangular root-zero-strata result at its preceding dimension \(r+1\) for \(s\ge1\); \(s=0\) is the additive group \(\mathrm{UT}_2(\mathbb F_q)\) and gives the same formula. General triangular Jordan-type enumerations also determine this group-level count.

## Limitations

The cycle law computes the type for a specified element. It does not tabulate how many elements of each cycle type occur as \(a\) varies, nor does it classify all finite braces. Comparisons to existing literature are bounded and do not certify historical priority.

## References

- W. Rump, *Braces, radical rings, and the quantum Yang–Baxter equation*, J. Algebra 307 (2007), 153–170.
- L. Guarnieri and L. Vendramin, *Skew braces and the Yang–Baxter equation*, https://arxiv.org/abs/1511.03171.
- A. Smoktunowicz, *On Engel groups, nilpotent groups, rings, braces and the Yang–Baxter equation*, https://arxiv.org/abs/1509.00420.
- M. Yip, *Rook placements and Jordan forms of upper-triangular nilpotent matrices*, https://arxiv.org/abs/1703.00057, §3 and Corollary 3.9.
- D. Fuchs and A. Kirillov, *Jordan types of triangular matrices over a finite field*, https://arxiv.org/abs/2204.00066.
- *Borel-stable root-zero strata of maximal-order elements just beyond a unitriangular exponent threshold*, Resultary 1ec57ea01e67, Finding, preceding-dimension comparison.
- *Logarithmic defect of typical lambda-orbit sizes in unitriangular braces*, Resultary 10a296ae216c, Finding.
