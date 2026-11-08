# Three-line Heisenberg tomography: a complete Gauss-phase spectrum and a characteristic-three rank jump

## Finding
For every **odd prime** \(p\), the sum of the normalized averages over any three noncentral order-\(p\) cyclic subgroups of the finite Heisenberg group whose projected directions are pairwise distinct has an explicit, complete spectral decomposition. The spectrum is given by three scalar values and a cubic governed by a single quadratic Gauss sum. In particular, its rank equals
\[
\operatorname{rank}T=3p^2-2\quad(p\ge5),
\]
whereas in characteristic three it equals \(19\) or \(25\), distinguished exactly by an additive central-lift relation. Among the \(108\) unordered triples of such cyclic subgroups when \(p=3\), exactly \(36\) have rank \(19\) and \(72\) have rank \(25\).

These ranks are also the dimensions recoverable from **three separately recorded families of cyclic-coset averages**, since the associated measurement operator has normal operator \(T\).

## Assumptions and scope
Let \(\mathbb F_p\) be the prime field, and define \(H_p=\mathbb F_p^2\times\mathbb F_p\) with multiplication
\[
(u,w)(v,z)=(u+v,w+z+\tfrac12\omega(u,v)),
\qquad\omega((x,y),(a,b))=xb-ya,
\]
where \(\tfrac12\) is the multiplicative inverse of \(2\) in \(\mathbb F_p\). Thus \(|H_p|=p^3\). Choose \(g_i=(u_i,w_i)\), for \(i=1,2,3\), such that the \(u_i\ne0\) span three *distinct projective directions*. In particular \(u_1,u_2\) are independent, and uniquely
\[
u_3=\alpha u_1+\beta u_2,\qquad \alpha,\beta\in\mathbb F_p^\times.
\]
Define \(\Delta=\omega(u_1,u_2)\ne0\), \(A=\alpha\beta\Delta/2\ne0\), and \(B=w_3-\alpha w_1-\beta w_2\). Put \(L_i=\{g_i^t:t\in\mathbb F_p\}\), and let
\[
(P_if)(h)=\frac1p\sum_{t\in\mathbb F_p}f(hg_i^t),\qquad
T=P_1+P_2+P_3
\]
on \(\ell^2(H_p)\) with counting measure. Each \(P_i\) is an orthogonal projection. Equivalently the three-view operator \(\mathcal R:f\mapsto(P_1f,P_2f,P_3f)\) satisfies \(\mathcal R^*\mathcal R=T\). The spectral statements below use this precise **normalized** operator.

For every \(\tau\in\mathbb F_p^\times\), define
\[
q_\tau=\frac1{p^2}\sum_{t\in\mathbb F_p}
\exp\!\left(\frac{2\pi i\tau}{p}(At^2+Bt)\right),
\]
with field elements represented by residues before exponentiation. Let \(\lambda_{\tau,1},\lambda_{\tau,2},\lambda_{\tau,3}\) be the three real roots, including any zero, of
\[
(\lambda-1)^3-\frac3p(\lambda-1)-2\operatorname{Re}q_\tau=0.
\]
The **complete eigenvalue multiset** of \(T\) consists of: eigenvalue \(3\) once; eigenvalue \(1\) with multiplicity \(3(p-1)\); eigenvalue \(0\) with multiplicity \((p-1)(p-2)+p(p-1)(p-3)\); and, for each nonzero \(\tau\), all three \(\lambda_{\tau,j}\), each repeated \(p\) times. If a cubic root is zero or coincides with any separately listed eigenvalue, multiplicities are **added**. In particular, the total multiset has exactly \(p^3\) entries.

For \(p\ge5\), each cubic root is positive. For \(p=3\), the two possible cubic families are
\[
B=0:\quad \{\lambda_{\tau,j}\}_{j=1}^3=\{0,1,2\};
\qquad
B\ne0:\quad(\lambda-1)^3-(\lambda-1)-\frac13=0,
\]
and all three roots in the latter case are positive. Hence for \(p=3\), \(\dim\ker T=8\) if \(B=0\), and \(\dim\ker T=2\) otherwise. The condition \(B=0\) is intrinsic: it says that the three central lifts are restrictions of one \(\mathbb F_p\)-linear functional on \(\mathbb F_p^2\), independently of the chosen generators.

## Proof
**1. Scalar Fourier blocks.** The Heisenberg group has \(p^2\) one-dimensional characters, all trivial on the center, and \(p-1\) irreducible characters of degree \(p\), parametrized by their nontrivial central character \(\tau\). Each degree-\(p\) representation occurs \(p\) times in the regular representation. The dimension-sum identity \(p^2+(p-1)p^2=p^3\) verifies completeness. A scalar character is indexed by \(\xi\in\mathbb F_p^2\) and equals \(\exp(2\pi i\langle\xi,u\rangle/p)\) on \((u,w)\). Its \(P_i\)-eigenvalue is \(1\) exactly when \(\langle\xi,u_i\rangle=0\), and otherwise is \(0\). The trivial character therefore yields \(3\). Of the nonzero characters, precisely \(3(p-1)\) vanish on exactly one selected direction; the remaining \((p-1)(p-2)\) vanish on none, yielding the stated scalar multiplicities.

**2. The degree-\(p\) projections.** An explicit Schrödinger realization is
\[
(\pi_\tau(x,y,w)\varphi)(s)=
\exp\!\left(\frac{2\pi i\tau}{p}(w+xy/2+ys)\right)\varphi(s+x).
\]
Its trace is \(p\exp(2\pi i\tau w/p)\) when \(u=0\), and zero when \(u\ne0\). Thus
\[
Q_i=\frac1p\sum_{t\in\mathbb F_p}\pi_\tau(g_i^t)
\]
is an orthogonal rank-one projection. For distinct projected directions, trace orthogonality gives \(\operatorname{tr}(Q_iQ_j)=1/p\). Indeed the sum \(ru_i+su_j=0\) forces \(r=s=0\). Consequently their three unit spanning vectors have pairwise inner-product modulus \(p^{-1/2}\).

**3. The triple phase.** Expanding the product of the three projection averages, a nonzero matrix trace occurs only when
\(r u_1+s u_2+t u_3=0\), namely \(r=-\alpha t\), \(s=-\beta t\). The group multiplication law then gives exactly the central coordinate
\[
(-\alpha t)w_1+(-\beta t)w_2+t w_3+
\frac12\bigl(\alpha\beta\Delta-\alpha\beta\Delta+\alpha\beta\Delta\bigr)t^2
=Bt+At^2.
\]
As \(\operatorname{tr}\pi_\tau(0,z)=p\exp(2\pi i\tau z/p)\), this proves
\[
\operatorname{tr}(Q_1Q_2Q_3)=q_\tau.
\]
The nonzero eigenvalues of \(Q_1+Q_2+Q_3\) agree, including multiplicities, with those of the Gram matrix of the three unit spanning vectors. Expanding that Gram determinant, using the three cross-modulus squares \(1/p\) and the cyclic triple product \(q_\tau\), gives the claimed cubic. Its other \(p-3\) eigenvalues are zero when \(p\ge3\).

**4. The rank boundary.** By the elementary Gershgorin bound, each Gram eigenvalue is at least \(1-2/\sqrt p\), which is strictly positive for every prime \(p\ge5\). In \(\mathbb F_3\), \(A\ne0\); direct enumeration of the three quadratic phases gives \(\operatorname{Re}q_\tau=0\) for \(B=0\), and \(\operatorname{Re}q_\tau=1/6\) for \(B\ne0\), independent of \(\tau\ne0\). The cubic is accordingly \((\lambda-1)((\lambda-1)^2-1)\) in the first case, with roots \(0,1,2\), while in the second case the determinant is \(1/3\), so all three roots are positive (the Gram matrix is positive semidefinite). Regular-representation multiplicities now yield total ranks \(3p^2-2\) for \(p\ge5\), and \(19\) or \(25\) for \(p=3\).

**5. Exhaustive characteristic-three census.** There are four projective directions in \(\mathbb F_3^2\), so there are \(\binom43=4\) choices of three. Fixing a normalized nonzero vector in each selected direction, its central lift \(w\in\mathbb F_3\) uniquely determines a cyclic subgroup, giving \(3^3=27\) triples per direction choice. Since \(B=w_3-\alpha w_1-\beta w_2\) is a nontrivial linear functional, exactly \(3^2=9\) of those have \(B=0\). The rank-\(19\) and rank-\(25\) counts are therefore \(4\cdot9=36\) and \(4\cdot18=72\), respectively.

## Verification
The supplied standalone `check_heisenberg.py` builds the normalized right-regular convolution matrices and the Schrödinger projection matrices directly from the group law; it does not read or assume the asserted spectral formula when diagonalizing the full regular matrices. For all six canonical cases with \(p\in\{3,5,7\}\) and central lifts \(B\in\{0,1\}\), it compared complete eigenvalue multisets, with maximum absolute discrepancy below \(5\times10^{-15}\). It also checks the quadratic-Gauss triple-product identity in \(24\) nontrivial irreducible blocks. For characteristic three it enumerates all \(108\) distinct-direction three-subgroup configurations, obtains the exact \(36/72\) rank census, and verifies representative regular-matrix ranks over the rationals using exact integer arithmetic. Invoke `python check_heisenberg.py` with NumPy and SymPy installed. These are finite tests, not a proof of the universal-prime statement.

## Relationship to prior work
Finite Heisenberg representations and mutually unbiased eigenbases are classical; the distinct-direction pairwise overlap \(p^{-1/2}\) follows from the established construction of Šulc and Tolar. Ilmavirta studies the complete finite-group Radon transform over all cyclic geodesics and gives the underlying general Fourier-block method. Blanchfield studies dependencies among canonical and Alltop mutually unbiased bases; her discussion of dependent vectors and characteristic-three geometry is particularly relevant to the small-prime exception. None of these facts is claimed as new. The present result is a three-direction, noncentral **subgroup-average operator classification**, including its full regular spectrum and the exact characteristic-three subgroup-triple rank census. The comparison is bounded rather than a guarantee of historical priority.

## Limitations
The theorem assumes odd prime field order, **exactly three** distinct projected directions, unit positive line-average weights, and the finite three-dimensional Heisenberg group. It does not prove sharp condition numbers, any composite-modulus analogue, or a spectrum for four or more selected directions. The characteristic-three dependence phenomenon has connections to existing Hesse and mutually unbiased basis theory. An older general theorem on finite stabilizer-state Gram matrices may imply some or all spectral consequences; historical priority remains a residual risk. No independent mathematical audit has occurred.

## References
1. P. Šulc and J. Tolar, *Group theoretical construction of mutually unbiased bases in Hilbert spaces of prime dimensions*, arXiv:0708.4114 (first posted 30 August 2007), Sections 3–6. https://arxiv.org/abs/0708.4114
2. K. Blanchfield, *Orbits of Mutually Unbiased Bases*, arXiv:1310.4684 (2013), especially Sections 2, 6 and the characteristic-three appendix. https://arxiv.org/abs/1310.4684
3. J. Ilmavirta, *On Radon transforms on finite groups*, arXiv:1411.3829 (2014), especially Sections 2 and 6. https://arxiv.org/abs/1411.3829
