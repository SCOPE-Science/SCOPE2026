# Exceptional characteristics and the first adjoint cohomology of an eight-dimensional Leibniz algebra

## Finding
For any field \(K\), let \(L_K\) be the right Leibniz algebra obtained by interpreting the integer multiplication table below over \(K\). Let \(\operatorname{Inn}(L_K)\) mean the Lie algebra spanned by **right multiplications** \(R_a(x)=xa\), and put \(H^1_\mathrm{ad}(L_K)=\operatorname{Der}(L_K)/\operatorname{Inn}(L_K)\). Then the complete characteristic-dependent dimensions are
\[
\begin{array}{c|c|c|c}
\operatorname{char}K & \dim\operatorname{Der}(L_K)&\dim\operatorname{Inn}(L_K)&\dim H^1_\mathrm{ad}(L_K)\\\hline
0\text{ or }p\notin\{2,3,11\}&6&6&0\\
2&9&6&3\\
3&7&6&1\\
11&7&5&2
\end{array}
\]
The exceptional prime \(11\) is qualitatively distinct: the right-annihilator dimension rises from \(2\) to \(3\), while a derivation newly appears that acts nonnilpotently on \(L_K/L_K^2\). In particular \(L_K\) is **not characteristically nilpotent** in characteristic \(11\). In characteristic zero and in every positive characteristic outside \(\{2,3,11\}\), all derivations are inner and hence nilpotent.

## Assumptions and scope
The eight-dimensional vector space has basis \(e_1,\ldots,e_8\), with multiplication specified by the following complete list of nonzero basis products; all unlisted products vanish. Every integer is interpreted through the canonical map \(\mathbb Z\to K\), with no restrictions on \(K\).

\[
\begin{aligned}
e_1e_1&=4e_8,&e_1e_2&=e_3,&e_1e_3&=e_4,&e_1e_4&=e_6,\\
e_1e_5&=6e_8,&e_1e_6&=e_8,\\
e_2e_1&=-e_3-9e_7+e_8,&e_2e_2&=-6e_7-e_8,\\
e_2e_3&=e_5,&e_2e_4&=3e_7,&e_2e_5&=e_8,&e_2e_6&=2e_8,\\
e_3e_1&=-e_4,&e_3e_2&=-e_5-6e_8,&e_3e_3&=-e_7+2e_8,&e_3e_4&=e_8,\\
e_4e_1&=-e_6,&e_4e_2&=-e_7-4e_8,&e_4e_3&=-2e_8,\\
e_5e_1&=-2e_7-2e_8,&e_5e_2&=-e_8,\\
e_6e_1&=-e_8,&e_6e_2&=e_8,&e_7e_1&=-e_8.
\end{aligned}
\]

The right Leibniz identity is \((xy)z=x(yz)+(xz)y\). All assertions concern this **fixed integral multiplication table** and its reductions, not arbitrary eight-dimensional Leibniz algebras, and use the right-multiplication convention for inner derivations.

## Proof
**1. Validity over every field.** The right Leibniz identity is an integral polynomial identity in the structure constants. Expanding it for all \(8^3=512\) triples of basis vectors, and all eight output coordinates, gives zero identically in \(\mathbb Z\), as checked without modular reduction by `verify.py`. Hence the table defines a right Leibniz algebra over any field. The filtration with degrees \((1,1,2,3,3,4,4,5)\) has products of nondecreasing total degree. It is therefore nilpotent, and its fifth lower-central term is nonzero because \((e_1e_2)e_1=-e_4\), \(((e_1e_2)e_1)e_1=e_6\), and \((((e_1e_2)e_1)e_1)e_1=-e_8\). In particular it is nilpotent of class five over every characteristic.

**2. The derivation matrix.** For each \(D\in\operatorname{End}(L_K)\), write \(D(e_u)=\sum_v d_{v,u}e_v\), and set \(e_i e_j=\sum_k c_{ij}^ke_k\). The derivation equations for \((i,j,k)\) have coefficients
\[
\sum_r c_{ij}^r d_{k,r}-\sum_r c_{rj}^k d_{r,i}-\sum_r c_{ir}^k d_{r,j}=0.
\]
This defines an explicit integral \(512\times64\) matrix \(M\); deleting its \(215\) zero rows leaves a \(297\times64\) matrix. Its **integer Smith invariant factors**, computed by exact integer operations on this fully specified finite matrix, are
\[
\underbrace{1,\ldots,1}_{55},\quad 2,2,66,\quad \underbrace{0,\ldots,0}_{6}.
\]
The standalone `verify.py` constructs \(M\) from the displayed multiplication table and computes these invariants exactly (and separately performs modular Gaussian elimination for the exceptional and sample ordinary primes). Smith transformations are unimodular over \(\mathbb Z\), so remain invertible over every field. Therefore the rank is \(58\) outside characteristics \(2,3,11\), \(55\) in characteristic \(2\), and \(57\) in characteristic \(3\) or \(11\). The nullity is exactly the stated derivation dimension.

**3. Inner derivations and cohomology.** The right Leibniz identity makes every map \(R_a(x)=xa\) a derivation. Stack the eight columns \(R_{e_j}\) (flattened as \(8\times8\) matrices) to obtain a \(64\times8\) integral matrix \(N\). Its Smith factors, computed independently and exactly by the same checker, are
\[
1,1,1,1,1,11,0,0.
\]
Thus \(\dim\operatorname{Inn}(L_K)=6\) except in characteristic \(11\), when it is \(5\). In characteristic \(11\) one directly checks \(R_{e_5}=6R_{e_6}\), while the maps corresponding to \(e_1,e_2,e_3,e_4,e_6\) remain independent. Since \(\operatorname{Inn}\subseteq\operatorname{Der}\), subtraction of their dimensions yields every cohomology entry in the table. No finite-field size restrictions are used, so the formulas hold over all fields.

**4. A genuine nonnilpotent derivation in characteristic eleven.** The following eight columns list the coefficients of \(D(e_1),\ldots,D(e_8)\), in order, over \(\mathbb F_{11}\):
\[
\begin{aligned}
D(e_1)&=8e_1+4e_2+3e_3+3e_4+4e_5+5e_6+3e_7,\\
D(e_2)&=5e_2+6e_3+7e_4+10e_5+6e_6+7e_7,\\
D(e_3)&=2e_3+6e_4+8e_5+7e_6+6e_7,\\
D(e_4)&=10e_4+4e_5+6e_6+8e_7,\\
D(e_5)&=7e_5+e_7+9e_8,\\
D(e_6)&=7e_6+e_7,\\
D(e_7)&=4e_7,\qquad D(e_8)=e_8.
\end{aligned}
\]
Substitution verifies all \(512\) derivation identities modulo \(11\); the checker tests each. On the quotient \(L_K/L_K^2\) spanned by the images of \(e_1,e_2\), this induces \(\begin{pmatrix}8&0\\4&5\end{pmatrix}\), which is not nilpotent (its determinant is \(40\equiv7\ne0\)). The same derivation exists by base extension over every field of characteristic eleven. This proves the final assertion.

## Verification
Run `python verify.py` with Python 3 and SymPy. The code constructs all structure constants from the complete stated table; checks the integral right Leibniz equations; forms the derivation and inner-multiplication matrices; obtains the exact Smith factors over \(\mathbb Z\); separately verifies modular ranks for primes \(2,3,5,7,11,13,17\); and checks the displayed characteristic-eleven derivation. `verification_output.txt` records a successful execution. The universal field classification follows from the integral Smith forms, **not** from testing finitely many primes. The certificate is an exact finite integer-matrix computation, not a formal proof assistant or independent mathematical audit.

## Relationship to prior work
Abdurasulov and Adashev, *An eight-dimensional nilpotent Leibniz algebra without outer derivations* (first submitted 2026-10-26, arXiv:2610.35015v1), introduce the multiplication table and prove \(\dim\operatorname{Der}=\dim\operatorname{Inn}=6\) **over the complex numbers**, plus automorphism and deformation results. That characteristic-zero fact and the algebra itself are prior work. Their Theorem 3.6 contains an equation with coefficient \(11\), but does not establish the complete positive-characteristic Smith factors, exact three-prime exceptional set, or the new cohomology dimensions. The new theorem identifies exactly how and where the characteristic-zero vanishing of \(H^1_\mathrm{ad}\) fails.

Atajonov, Khudoyberdiyev and Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras* (arXiv:2610.40348v1, 2026-10-29), study a **different** eight-dimensional Leibniz algebra \(A_8\), with fourteen nonzero basis products and seven-dimensional complex derivation space; they do not cover the present integral table or its modular cohomology. Generic papers on inner derivations of Leibniz algebras also do not supply these explicit invariant factors.

## Limitations
The classification is for the stated integral model, not all integral forms of the same complex algebra, which may have different bad primes. The characteristic-eleven derivation proves failure of characteristic nilpotency in that characteristic, but the corresponding property in characteristics two and three is not classified here. The exact Smith computations require replaying the included script with SymPy; the positive-characteristic originality comparison cannot rule out an earlier result under unsearched terminology. No independent audit has been performed.

## References
1. K. Abdurasulov and J. Adashev, *An eight-dimensional nilpotent Leibniz algebra without outer derivations*, arXiv:2610.35015v1 (2026-10-26), https://arxiv.org/abs/2610.35015 ; multiplication Table (3), Theorem 2.1, Theorems 3.5–3.7.
2. K. Atajonov, A. Khudoyberdiyev and B. Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras*, arXiv:2610.40348v1 (2026-10-29), https://arxiv.org/abs/2610.40348 ; §5.5.
3. M. Newman, *Integral Matrices*, Academic Press (1972), standard Smith-normal-form theory.
