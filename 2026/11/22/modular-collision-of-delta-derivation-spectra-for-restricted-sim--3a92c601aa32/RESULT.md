# Modular collision of \(\delta\)-derivation spectra for restricted simple \(\mathfrak{sl}_2\)-modules

## Finding

Let \(k\) be any field of odd prime characteristic \(p\) and \(\mathfrak g=\mathfrak{sl}_2(k)\). For \(0\le m\le p-1\) let \(V_m=\operatorname{Sym}^m(k^2)\) be its standard restricted simple module. A \(\delta\)-derivation is a linear map \(D:\mathfrak g\to V_m\) satisfying
\[
D([x,y])=\delta\bigl(x\cdot D(y)-y\cdot D(x)\bigr)
\]
for all \(x,y\in\mathfrak g\). Write \(d_p(m,\delta)\) for the dimension of this space.

The complete spectrum, for every \(\delta\in k\), is
\[
d_p(m,\delta)=
\begin{cases}
0,&m=0,\\
m+1,&1\le m\le p-3,\ \delta=1,\\
m+3,&1\le m\le p-3,\ \delta=-2/m,\\
m-1,&2\le m\le p-3,\ \delta=2/(m+2),\\
p+1,&m=p-2,\ \delta=1,\\
p,&m=p-1,\ \delta=1,\\
p+2,&m=p-1,\ \delta=2,\\
0,&\text{otherwise}.
\end{cases}
\]
All scalar conditions and fractions are interpreted in \(k\). The three exceptional parameters in the interior range are distinct. For a finite field \(k=\mathbb F_q\), the number of maps is precisely \(q^{d_p(m,\delta)}\).

The principal modular feature is the Steinberg boundary \(m=p-1\): the two generic eigenvalues \(-m/2\) and \((m+2)/2\) merge, leaving a \(\delta=2\) derivation space of dimension \(p+2\), while the \(\delta=1\) space has dimension \(p\). This is not obtained by naively adding the dimensions of the two characteristic-zero branches. The generic characteristic-zero branches themselves are established in earlier literature and are not claimed as new.

## Assumptions and scope

Use the basis \(e,f,h\) of \(\mathfrak g\) with \([h,e]=2e\), \([h,f]=-2f\) and \([e,f]=h\). On the basis \(v_0,\ldots,v_m\) of \(V_m\), with out-of-range vectors zero, the actions are
\[
hv_i=(m-2i)v_i,\qquad ev_i=(m-i+1)v_{i-1},\qquad fv_i=(i+1)v_{i+1}.
\]
The representation is simple throughout the indicated restricted range, and division by \(2\) is legitimate since \(p\) is odd. Nothing is claimed for characteristic two, nonrestricted highest weights, indecomposable nonsimple modules, or arbitrary Lie algebras.

## Proof

Set \(A=D(e)\), \(B=D(f)\), \(C=D(h)\). The three bracket relations show that \(D\) is a \(\delta\)-derivation exactly when \(D=\delta T(D)\) for the linear endomorphism of \(\operatorname{Hom}_k(\mathfrak g,V_m)\) defined by
\[
(TD)(e)=\tfrac12(hA-eC),\quad
(TD)(f)=\tfrac12(fC-hB),\quad
(TD)(h)=eB-fA.
\]
In particular \(\delta=0\) forces \(D=0\). For nonzero \(\delta\), its dimension is the geometric multiplicity of the eigenvalue \(\delta^{-1}\) of \(T\).

For \(m\ge1\), decompose the coefficient space into two singleton blocks, two edge blocks and \(m-1\) interior blocks. The singletons are the coefficient of \(v_0\) in \(B\), and of \(v_m\) in \(A\); each has eigenvalue \(-m/2\). The edge blocks on \((C_0,B_1)\) and \((A_{m-1},C_m)\) are respectively
\[
\begin{pmatrix}0&m\\\frac12&\frac{-m+2}{2}\end{pmatrix},\qquad
\begin{pmatrix}\frac{-m+2}{2}&-\frac12\\-m&0\end{pmatrix}.
\]
Each has characteristic polynomial \((t-1)(t+m/2)\).

For \(1\le j\le m-1\), the interior block on the coefficients \((A_{j-1},C_j,B_{j+1})\) is
\[
T_j=\begin{pmatrix}
\frac{m-2j+2}{2}&-\frac{m-j+1}{2}&0\\
-j&0&m-j\\
0&\frac{j+1}{2}&\frac{-m+2j+2}{2}
\end{pmatrix}.
\]
Direct determinant expansion gives the identity, valid as a polynomial over \(\mathbb Z[1/2,m,j,t]\),
\[
\det(tI-T_j)=(t-1)(t+m/2)(t-(m+2)/2).
\]
The dimensions add up to \(2+4+3(m-1)=3(m+1)\), so these blocks exhaust the full coefficient space.

When \(1\le m\le p-3\), the three displayed eigenvalues are pairwise different and nonzero. Each interior block contributes one eigenvector for each, each edge contributes one for \(1\) and \(-m/2\), and the two singleton blocks contribute two more for \(-m/2\). This yields geometric multiplicities \(m+1\), \(m+3\), \(m-1\), respectively; replacing eigenvalue \(\lambda\) with \(\delta=\lambda^{-1}\) proves the stable-range rows.

When \(m=p-2\), the three eigenvalues reduce to \(1,1,0\). On every interior block, the first and third rows of \(T_j-I\) have nonzero separate pivots \(-(j+1)\) and \(j+1\) in the first and third coordinates, respectively, for \(1\le j\le p-3\). Thus its \(1\)-eigenspace has dimension one, even though this eigenvalue is algebraically repeated. Each edge block has one-dimensional \(1\)-eigenspace because its off-diagonal entries are nonzero, and both singleton blocks contribute at \(1\). The total is \((m-1)+2+2=p+1\); the other eigenvalue is zero, which cannot equal \(\delta^{-1}\).

When \(m=p-1\), the eigenvalues reduce to \(1,1/2,1/2\). For each interior block, the first and third rows of \(T_j-\frac12 I\) have distinct nonzero pivots \(-j\) and \(j+1\) for \(1\le j\le p-2\), so the \(1/2\)-eigenspace is one-dimensional. The \(1\)-eigenspace is also one-dimensional by its simple characteristic root. Each edge block contributes one eigenvector to each eigenvalue, and the singletons add two at \(1/2\). The resulting geometric multiplicities are \(p\) at \(1\) and \(p+2\) at \(1/2\), corresponding to \(\delta=1\) and \(\delta=2\). Finally for \(m=0\), the module is trivial and \(\mathfrak g=[\mathfrak g,\mathfrak g]\), hence all such maps vanish. This proves every claimed case over every odd-characteristic field.

## Verification

Run `python3 verify_delta.py` with Python 3. The included checker constructs the original three bracket equations directly on \(3(m+1)\) unknown coefficients, computes their ranks over prime fields independently of the block decomposition, and compares all \(\delta\in\mathbb F_p\) and all \(0\le m\le p-1\) for \(p=3,5,7,11,13,17,19\). The observed output is `MODULAR_SL2_DELTA_SPECTRUM_OK 1023`. In particular, the \(p=3\) Steinberg boundary has dimension \(5\) at \(\delta=2\), and the \(p=5\) boundary has dimension \(7\). This finite test is supplemental: the symbolic block proof establishes the theorem for all odd-characteristic fields, including nonprime finite fields.

## Relationship to prior work

Zohrabi and Zusmanovich's *A \(\delta\)-first Whitehead Lemma* (2020 preprint; arXiv version 2022) already computes the stable-range exceptional \(\delta\)-derivation formulas for finite-dimensional irreducible characteristic-zero \(\mathfrak{sl}_2\)-modules. Those known formulas are repeated for comparison, not presented as a new discovery. Jiang, Liu, and Pei's November 13, 2026 paper treats complex simple Lie algebras and arbitrary modules, including a characteristic-zero \(\delta=2\) phenomenon; its hypotheses do not include characteristic \(p\). Wang and Li study ordinary cohomology for restricted simple \(\mathfrak{sl}_2\)-modules in prime characteristic, addressing the \(\delta=1\) branch. The distinct contribution assessed here is the complete modular parameter spectrum with the boundary eigenvalue-collision calculation, most sharply at the Steinberg \(\delta=2\) branch.

## Limitations

The priority comparison is provisional: an exhaustive search of all historical texts and independent specialist audit have not occurred. An earlier positive-characteristic generalization under alternate terminology could overlap. The unrestricted category of all simple modules in positive characteristic, including nonrestricted forms over nonclosed fields, is not considered. Direct numerical checks use prime fields of characteristics at most \(19\), not every field; correctness at general \(p\) rests on the explicit symbolic proof. Known characteristic-zero and ordinary-derivation statements are not novelty claims.

## References

1. A. Zohrabi and P. Zusmanovich, *A \(\delta\)-first Whitehead Lemma*, first public 2020 preprint, https://arxiv.org/abs/2211.06645 and https://www.researchgate.net/publication/342313556_A_DELTA-FIRST_WHITEHEAD_LEMMA.
2. L. Jiang, D. Liu and Y. Pei, *\(\delta\)-Derivations of Finite-Dimensional Simple Lie Algebras with Values in Arbitrary Modules*, arXiv:2611.17683v1, submitted November 13, 2026, https://arxiv.org/abs/2611.17683.
3. Wang and Li, *Cohomology of \(\mathfrak{sl}(2)\) and its applications in prime characteristic*, arXiv:2206.07943, https://arxiv.org/abs/2206.07943.
