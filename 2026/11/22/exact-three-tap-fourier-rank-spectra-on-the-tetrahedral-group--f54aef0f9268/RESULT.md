# Exact three-tap Fourier-rank spectra on the tetrahedral group

## Finding
Let \(G=A_4\), let \(f:G\to\mathbb C\) have **exactly three** nonzero values, and let
\[
(T_fh)(z)=\sum_{g\in G}f(g)h(g^{-1}z),\qquad R(f)=\operatorname{rank}_{\mathbb C}T_f.
\]
Write \(V=\{e,(12)(34),(13)(24),(14)(23)\}\), the normal Klein four subgroup of \(A_4\). There are exactly four geometric kinds of three-element supports, with the following complete attainable-rank sets:

| Support geometry | Number of supports | \(\{R(f):\operatorname{supp}(f)=S\}\) for every fixed \(S\) |
| --- | ---: | --- |
| A coset of an order-three subgroup | 16 | \(\{4,8,12\}\) |
| Two points in one \(V\)-coset, one in another | 144 | \(\{9,11,12\}\) |
| One point in each \(V\)-coset, but not an order-three coset | 48 | \(\{9,10,11,12\}\) |
| Three points in one \(V\)-coset | 12 | \(\{9,12\}\) |

The four classes partition all \(\binom{12}{3}=220\) supports. All listed values occur with nonzero **rational** coefficients on every fixed support; every omitted value is impossible even for arbitrary nonzero complex coefficients. In particular rank \(10\) distinguishes the noncyclic transversals from the other three geometries, while rank \(4\) is possible only on cosets of order-three subgroups.

## Assumptions and scope
Permutation products are compositions (the right factor acts first); \(A_4\) is the even permutation group of four points. A three-tap coefficient function has values \(a,b,c\in\mathbb C^*\) at three distinct group elements and zero elsewhere. Scaling all coefficients by a nonzero scalar does not change rank, so after left translation and scaling it is legitimate to write
\[
f=\delta_e+x\delta_u+y\delta_v,\qquad x,y\in\mathbb C^*.
\]
Left translating the support, and simultaneously conjugating its elements by a permutation in \(S_4\), preserve convolution rank. Rank is the dimension of the image over \(\mathbb C\), not the number of nonzero distinct irreducible Fourier blocks. The irreducible dimensions of \(A_4\) are \(1,1,1,3\), giving
\[
R(f)=\sum_{\rho\in\widehat G}(\dim\rho)\operatorname{rank}\!\left(\sum_{g\in G}f(g)\rho(g)\right).
\]
Using inverse Fourier transforms, or choosing right instead of left regular multiplication, does not change this rank.

## Proof
**1. Exhaustion of support geometries.** Each of the three \(V\)-cosets has four elements. All triples in one coset contribute \(3\binom43=12\) supports. Choosing the doubled coset, its two points, the other coset and its one point gives \(3\binom42\cdot2\cdot4=144\) supports. The transversals number \(4^3=64\); among these, the four order-three subgroups have four left cosets each, yielding \(16\) cyclic triples and \(48\) noncyclic transversals. Under left translations by \(A_4\) and conjugations by \(S_4\), each of these four types is one orbit (the precise 220-support orbit partition is checked by `verify_regular.py`). Suitable normalized representatives \((e,u,v)\) are
\[
\begin{array}{c|cc}
\text{type}&u&v\\\hline
\text{cyclic}&(234)&(243)\\
\text{mixed}&(234)&(12)(34)\\
\text{noncyclic transversal}&(234)&(123)\\
\text{Klein}&(12)(34)&(13)(24)
\end{array}
\]
Each rank set on its representative therefore transports to every fixed support of the same type.

**2. The two subgroup classes.** A convolution supported on one coset of a subgroup \(H\leq G\) has the same rank as a convolution in \(\mathbb C[H]\), multiplied by \([G:H]\). For the cyclic triple \(H=C_3\), put \(\omega=e^{2\pi i/3}\). The three scalar eigenvalues on \(H\) are \(1+x\omega^k+y\omega^{2k}\), \(k=0,1,2\). They cannot all vanish, by invertibility of the three-point Fourier matrix; with \(xy\ne0\), zero, one or two can vanish, realized respectively by \((x,y)=(1,2),(-1/2,-1/2),(1,1)\). The ranks in the twelve-dimensional regular representation are exactly \(12,8,4\). For a three-point support in \(V\), the four scalar Fourier values are \(1\pm x\pm y\), using the four character sign patterns. Two cannot vanish simultaneously with \(xy\ne0\): subtracting two equations forces a coefficient to vanish or forces \(2=0\). Thus the \(V\)-regular rank is three or four, and the \(G\)-regular rank is \(9\) or \(12\), realized by \((x,y)=(1/2,1/2)\) and \((1,1)\).

**3. The remaining three-dimensional Fourier block.** Realize the three-dimensional irreducible \(\rho\) as the action of even permutations on the zero-sum subspace of \(\mathbb C^4\), with basis \(e_1-e_4,e_2-e_4,e_3-e_4\). For the mixed representative, the block \(I+x\rho(u)+y\rho(v)\) and its determinant are
\[
M_{\mathrm m}=\begin{pmatrix}1+x&y&0\\-x+y&1-x&-x\\-y&x-y&1-y\end{pmatrix},\quad
P_{\mathrm m}=1+x^3+y^3-y^2-y.
\]
A two-by-two minor is \(-xy\), so \(\operatorname{rank}M_{\mathrm m}\ge2\). For the noncyclic transversal representative,
\[
M_{\mathrm t}=\begin{pmatrix}1+x&0&y\\-x+y&1-x&-x\\0&x+y&1\end{pmatrix},\quad
P_{\mathrm t}=1+x^3+xy+y^3.
\]
Three of its two-by-two minors are \(1+x\), \(y-x\) and \(y(x-1)\). They cannot simultaneously vanish: the first two would imply \(x=y=-1\), making the third equal to \(2\). Therefore this block also has rank two or three, never zero or one. In either case its only possible regular-representation contribution is \(6\) or \(9\).

**4. No simultaneous scalar and three-dimensional losses.** The three one-dimensional characters of \(A_4\) factor through \(G/V\cong C_3\). For the mixed representative they yield \(L_k=1+\omega^kx+y\); for the noncyclic transversal they yield \(L_k=1+\omega^kx+\omega^{2k}y\). In the mixed case at most one \(L_k\) vanishes because \(x\ne0\). For the transversal case at most two vanish by invertibility of the \(C_3\) Fourier matrix. Their simultaneous vanishing in pairs occurs at \((x,y)=(1,1),(\omega,\omega^2),(\omega^2,\omega)\), and \(P_{\mathrm t}=4\) there.

More generally, for any vanishing \(L_k\) put \(X=\omega^kx\) and either \(Y=y\) (mixed case) or \(Y=\omega^{2k}y\) (transversal case). Both determinant polynomials are unchanged under this substitution and the scalar equation is \(X=-1-Y\). Direct expansion gives in each case
\[
P=-4Y(Y+1).
\]
For \(P=0\), the possibilities \(Y=0\) or \(Y=-1\) would force \(y=0\) or \(X=0\), contradicting \(xy\ne0\). Hence no three-dimensional rank loss coincides with any scalar rank loss. The mixed ranks can only be \(12,11,9\); the transversal ranks can only be \(12,11,10,9\).

**5. Attainment on both non-subgroup classes.** Integer coefficient triples \((a,b,c)\), respectively at the representative's \((e,u,v)\), give every remaining rank:

| Type | Rank | \((a,b,c)\) |
| --- | ---: | --- |
| Mixed | 9 | \((9,-8,-7)\) |
| Mixed | 11 | \((2,-1,-1)\) |
| Mixed | 12 | \((1,1,1)\) |
| Noncyclic transversal | 9 | \((1,1,-1)\) |
| Noncyclic transversal | 10 | \((1,1,1)\) |
| Noncyclic transversal | 11 | \((2,-1,-1)\) |
| Noncyclic transversal | 12 | \((1,1,2)\) |

These values follow by substituting the corresponding normalized \((x,y)=(b/a,c/a)\) into the preceding determinant and scalar formulas. The separate exact regular-matrix computation checks all listed witnesses on every support in each class. This establishes both impossibility and complete attainment.

## Verification
`verify_symbolic.py` uses only the Python standard library and expands the four representative three-dimensional determinant polynomials exactly in \(\mathbb Z[x,y]\); it verifies the stated rank-two minors and the scalar/three-dimensional determinant disjointness identity. `verify_regular.py` independently builds all 12-by-12 left-regular matrices, generates all 220 supports through the action of \(A_4\times S_4\), verifies the orbit sizes \((16,144,48,12)\), and runs exact rational Gaussian elimination for every listed attainable-rank witness transported onto every support. All \(696\) witness tests pass. Run `python3 verify_symbolic.py` and `python3 verify_regular.py` using Python 3 with no external dependencies. `verification_output.txt` contains the exact recorded console results. The symbolic proof is all-coefficient; the finite exact checks of witnesses alone would not rule out unlisted complex ranks.

## Relationship to prior work
Alagic and Russell (2006) establish the rank-weighted finite-group Fourier uncertainty inequality \(|\operatorname{supp}f|R(f)\ge|G|\), which gives only the lower bound \(R(f)\ge4\) for three taps on \(A_4\). Arezoomand and Taeri (2013) give a representation-theoretic characteristic-polynomial factorization for Cayley digraphs; the block decomposition is already known but the four coefficient-sensitive rank spectra, mutual singularity exclusions and exact support geometry are not stated there. The previously published tetrahedral Fourier-support result treats functions with **Fourier rank exactly three** and asks which **time support sizes** occur, the reverse question from this theorem. Prior three-tap rank classifications on dihedral groups cover a different group family; the binary tetrahedral result covers unweighted coefficients on a different 24-element group. None of these inspected results directly implies the four fixed-support rank spectra after a simple normalization. An unindexed weighted Cayley calculation may nevertheless be equivalent.

## Limitations
The theorem is specific to exactly three nonzero **complex** coefficients on \(A_4\). It does not classify supports with two or four points, condition numbers of nonsingular operators, or higher alternating groups. The finite checks establish attainment and corroborate finite orbit classification; the impossibility for arbitrary complex coefficients comes from the displayed algebraic identities, not from sampling or experiments. Historical literature coverage is bounded and independent mathematical review has not been performed.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702 (publicly submitted 2006-08-28), Theorem 2 and Sections 2–3. https://arxiv.org/abs/math/0608702
2. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, Electronic Journal of Combinatorics 20(3), P57 (2013), Lemma 1 and Section 2. https://doi.org/10.37236/3105
3. *Exact time-support spectrum at rank-weighted Fourier size three on the tetrahedral group*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-time-support-spectrum-at-rank-weighted-fourier-size-three--43499b938eaa
4. *Complete three-tap Fourier-rank spectrum on odd-prime dihedral groups*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-three-tap-fourier-rank-spectrum-on-odd-prime-dihedral-g--eb09d9b17153
5. *Exact three-tap convolution nullities on the binary tetrahedral group*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-three-tap-convolution-nullities-on-the-binary-tetrahedral--180fb72fc4da
