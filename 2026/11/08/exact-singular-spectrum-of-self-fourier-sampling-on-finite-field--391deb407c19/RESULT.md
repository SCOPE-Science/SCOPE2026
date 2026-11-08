# Exact singular spectrum of self-Fourier sampling on finite-field rank-one matrix cones

## Finding

Let \(q\) be any prime power and \(m,n\ge2\). Write
\[
S=\{X\in M_{m\times n}(\mathbb F_q):\operatorname{rank}(X)=1\},
\quad P_k=\frac{q^k-1}{q-1},\quad |S|=(q-1)P_mP_n.
\]
For a fixed nontrivial additive character \(\psi\) of \(\mathbb F_q\), form the square matrix indexed on *both* axes by \(S\):
\[
 H_{X,Y}=\psi\!\left(\sum_{i=1}^m\sum_{j=1}^n X_{ij}Y_{ij}\right).
\]
**Theorem.** The complete singular-value multiset of \(H\) is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
\displaystyle L=\frac{q^{m+n-1}-q^m-q^n+1}{q-1}&1\\[3pt]
q^{m+(n-2)/2}&P_n-1\\
q^{n+(m-2)/2}&P_m-1\\
q^{(m+n-2)/2}&(P_m-1)(P_n-1)\\
q^{(m+n-1)/2}&(q-2)P_mP_n.
\end{array}
\]
Repeated numerical levels have their multiplicities added. At \(q=2\) the last multiplicity is zero. All listed levels of positive multiplicity are strictly positive. Hence \(H\) is invertible over \(\mathbb C\) for every such \(q,m,n\); a complex signal supported on \(S\) is uniquely determined by its Fourier transform observed on \(S\). Its sharp Euclidean condition number is precisely the largest displayed level divided by the smallest displayed level with positive multiplicity. This gives all optimal two-sided sampling inequalities by squaring those endpoints.

## Assumptions and scope

The domain is *rank exactly one*, excludes the zero matrix, and uses the standard coordinatewise bilinear pairing (not the trace matrix-product pairing). \(q\) may have any characteristic and need not be prime. The character \(\psi\) is nontrivial and has complex modulus one. The matrix is unnormalized: multiplying all entries by the same scalar rescales every singular value but not the condition number. Signals and samples are both indexed by the same \(S\); the result is not a statement about ambient convolution by the indicator of \(S\), nor about a small subfamily of Fourier frequencies. For projective lines a representative vector is chosen arbitrarily; none of the final singular values depend on that choice.

## Proof

**1. Projective scalar coordinates.** Choose a nonzero representative \(u_L\) for each line \(L\in\mathbb P^{m-1}(\mathbb F_q)\), and \(v_M\) for each \(M\in\mathbb P^{n-1}(\mathbb F_q)\). Each \(X\in S\) has a *unique* expression \(X=c\,u_Lv_M^{\mathsf T}\), where \(c\in\mathbb F_q^\times\) and \(L,M\) are projective lines. Its pairing with \(Y=d\,u_{L'}v_{M'}^{\mathsf T}\) is
\[
 \langle X,Y\rangle=cd\,(u_L\cdot u_{L'})(v_M\cdot v_{M'}).
\]
There are \(P_mP_n\) pairs of lines and exactly \(q-1\) scalars per pair, giving the claimed matrix size.

**2. The multiplicative-character decomposition.** Decompose scalar functions on \(\mathbb F_q^\times\) into orthogonal character lines \(\mathbb C\chi\). If a column vector is \(f(d,L',M')=\chi(d)g(L',M')\), then its image under \(H\) is computed from
\[
\sum_{d\ne0}\chi(d)\psi(cdz).
\]
For a nontrivial multiplicative character \(\chi\), this is zero when \(z=0\), and equals \(\tau(\chi)\overline{\chi(cz)}\) otherwise, with Gauss sum \(|\tau(\chi)|=\sqrt q\). Thus the \(\chi\)-sector maps into the \(\overline\chi\)-sector by a modulus-\(\sqrt q\) scalar times
\[
 A_{\overline\chi}^{(m)}\otimes A_{\overline\chi}^{(n)},\qquad
 A_{\eta}^{(k)}(L,L')=\begin{cases}\eta(u_L\cdot u_{L'}),&u_L\cdot u_{L'}\ne0,\\0,&u_L\cdot u_{L'}=0.\end{cases}
\]
The character-sector bases are orthogonal even when \(\chi\) and \(\overline\chi\) coincide. Each projective twisted incidence satisfies the *exact* orthogonality identity
\[
 A_\eta^{(k)}(A_\eta^{(k)})^*=q^{k-1}I\quad(\eta\ne1).
\]
To verify it, the diagonal entry counts \(q^{k-1}\) projective lines with nonzero dot product. For independent projective vectors \(u,w\), replace the projective sum by \(1/(q-1)\) times the sum over nonzero vectors \(z\). The two independent linear forms \(u\cdot z,w\cdot z\) range uniformly over \(\mathbb F_q^2\), and the off-diagonal sum factors through \(\sum_{a\ne0}\eta(a)=0\). Hence every nontrivial multiplicative sector has singular value
\[
\sqrt q\,q^{(m-1)/2}q^{(n-1)/2}=q^{(m+n-1)/2}
\]
with multiplicity \(P_mP_n\) per character. There are \(q-2\) such characters, including none at \(q=2\).

**3. The trivial scalar-character sector.** For \(\chi=1\), the scalar sum is \(q-1\) if \(z=0\) and \(-1\) otherwise. Let \(A_1^{(k)}\) be the symmetric zero-one projective nonorthogonality matrix. The restriction of \(H\) to scalar-constant vectors is therefore
\[
 T=(q-1)J_{P_mP_n}-q A_1^{(m)}\otimes A_1^{(n)}.
\]
The matrix \(A_1^{(k)}\) has constant row sum \(q^{k-1}\). A direct count of common nonorthogonal projective lines gives diagonal entries \(q^{k-1}\) and distinct-row entries \(q^{k-2}(q-1)\) for its square. Therefore
\[
 (A_1^{(k)})^2=q^{k-2}I+q^{k-2}(q-1)J.
\]
Thus its singular modulus on the constant line is \(q^{k-1}\), while on its orthogonal complement of dimension \(P_k-1\) it is \(q^{(k-2)/2}\). This remains valid in even characteristic, and for \(k=2\).

The tensor of the two projective line spaces splits into four orthogonal subspaces: constant–constant, constant–mean-zero, mean-zero–constant, and mean-zero–mean-zero. The first is an eigenspace of \(T\), with eigenvalue
\[
 (q-1)P_mP_n-q^{m+n-1}
 =\frac{q^{m+n-1}-q^m-q^n+1}{q-1}=L.
\]
On the other three tensor subspaces the all-ones term vanishes. The three corresponding singular moduli are, in order,
\[
 q^{m+(n-2)/2},\qquad q^{n+(m-2)/2},\qquad q^{(m+n-2)/2},
\]
with the corresponding product multiplicities listed in the theorem.

**4. Completeness and strict positivity.** The multiplicities add to
\[
 P_mP_n+(q-2)P_mP_n=(q-1)P_mP_n=|S|.
\]
No singular values remain uncounted. To show \(L>0\), note \(L=|S|-q^{m+n-1}\) and, for \(m,n\ge2\), \((q^m-1)(q^n-1)>(q-1)q^{m+n-1}\); the inequality follows directly by expanding each side, with its minimum case \(q=2,m=n=2\) giving \(L=1\). All other levels are powers of positive \(q\). The singular values therefore give invertibility and the exact condition number. The linear-algebra inequalities are sharp because every displayed singular value has an actual singular subspace.

## Verification

The standalone `check_rankone_self.py` constructs the rank-one matrices by independent enumeration of all nonzero vector pairs, deduplicates them by matrix entries, computes the *full* Fourier submatrix and its numerical singular values, and compares the multiset with the theorem. The tested tuples \((q,m,n)\) are \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), \((3,2,2)\), \((3,2,3)\), \((4,2,2)\), and \((5,2,2)\). The size \(q=4\) test implements \(\mathbb F_4\) as a quadratic extension of \(\mathbb F_2\). The terminal success token is `RANK_ONE_SELF_FOURIER_PASS`. Run `python check_rankone_self.py` with Python 3 and NumPy. These finite examples are cross-checks, not the proof for arbitrary \(q,m,n\).

## Relationship to prior work

Delsarte's bilinear-forms association scheme contains the classical Fourier transform of a rank-one shell, which in particular supplies the constant-mode character sum \(L\). That Fourier coefficient does not itself provide the complete singular spectrum of the **square submatrix restricted to rank-one inputs and rank-one output frequencies**. General abelian-symmetry frame diagonalization, such as Eldar–Bölcskei, provides a methodological backdrop but not the present projective tensor decomposition. Li–Hu compute additive Fourier sums over invertible matrix groups instead of this rank-one submatrix; Gurevich–Howe study Fourier coefficients of rank strata, not this principal sampling operator. A complete first-coordinate character restriction result for rank-one matrices (2026) studies a much smaller frequency band \(\{0\}\cup\{aE_{ij}\}\), so does not imply this full self-restriction spectrum. These are comparisons of **operators and implications**, not assertions that different titles ensure originality.

## Limitations

The theorem does not treat rank-at-most-one with the origin adjoined, arbitrary rank strata, arbitrary bilinear pairings, complex spectral phases, or full spark of all smaller minors. Numerical tests do not establish the universal theorem. Classical association-scheme literature or projective-incidence diagonalization could contain a broader theorem implying this exact spectrum; that historical-priority risk is not eliminated. The Delsarte 1978 original full text was not available for a line-by-line comparison; available abstract and rank-one transform references were considered, with this limitation recorded rather than inferring noncoverage from snippets. No independent validation has been conducted.

## References

1. Ph. Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory, Series A 25 (1978), 226–241, DOI: 10.1016/0097-3165(78)90015-8 (classical rank-shell Fourier sums; original full text not inspected).
2. Y. C. Eldar and H. Bölcskei, *Geometrically Uniform Frames*, arXiv:math/0108096v1, first publicly submitted 2001-08-13 (frame diagonalization background).
3. Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1, first submitted 2011-05-23 (different matrix group transform).
4. S. Gurevich and R. Howe, *Ranks for Representations of GL(n) Over Finite Fields, their Agreement, and Positivity of Fourier Transform*, arXiv:2107.02240v1, first submitted 2021-07-05 (rank-shell character coefficients).
5. *Complete first-coordinate Fourier spectrum on finite-field rank-one matrices*, publicly available 2026 (first-coordinate frequency restriction, distinct operator).
