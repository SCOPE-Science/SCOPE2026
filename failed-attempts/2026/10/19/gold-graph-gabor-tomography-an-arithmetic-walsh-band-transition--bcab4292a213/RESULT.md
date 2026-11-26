# Gold-graph Gabor tomography: arithmetic Walsh bands and an APN spectral criterion

## Finding
For \(m\ge2\), \(q=2^m\), and \(1\le k<m\) satisfying \(\gcd(m,k)=1\), write \(F=\mathbb F_q\), \(G=F^2\), and
\[
C=\{(t,f(t)):t\in F\},\qquad f(t)=t^{2^k+1},\qquad g=q^{-1/2}\mathbf1_C.
\]
For the full Gabor family of rank-one operators associated with \(g\), the operator-analysis singular values, counted with multiplicity, are
\[
\begin{array}{c|c}
\text{value}&\text{multiplicity}\\\hline
2&(q-1)q^3/4\\
q&1\\
\sqrt{2q}&q(q-1)/2\quad(m\text{ odd})\\
\sqrt q&2q(q-1)/3\quad(m\text{ even})\\
2\sqrt q&q(q-1)/12\quad(m\text{ even}).
\end{array}
\]
Repeated numerical values in different rows have **additive** multiplicities. All remaining singular values among the \(q^4\) dimensions are zero. The rank is exactly
\[
\operatorname{rank}\mathcal L_g=
\begin{cases}
1+(q-1)q^3/4+q(q-1)/2,&m\text{ odd},\\
1+(q-1)q^3/4+3q(q-1)/4,&m\text{ even}.
\end{cases}
\]
Its positive-spectrum condition number is \(q/2\). Every zero singular direction has an explicit Weyl-basis description below. The full signature, including multiplicities, persists under every invertible affine reindexing of the ambient binary group, and therefore under CCZ equivalence whenever both affine images are function graphs.

The geometric part admits a converse for *every* function graph over \(F\): the horizontal-nonzero-translation part of its Gabor spectrum lies entirely in \(\{0,2\}\) if and only if its graph is almost perfect nonlinear (APN). For an APN graph this part has exactly \((q-1)q^3/4\) copies of \(2\), independently of the particular function.

## Assumptions and scope
All traces below are absolute traces \(\operatorname{Tr}_{F/\mathbb F_2}\). For \(h\in G\), translation is \((T_h\phi)(x)=\phi(x+h)\). For \(\omega=(u,v)\in G\), modulation is
\[
(M_\omega\phi)(x,y)=(-1)^{\operatorname{Tr}(ux+vy)}\phi(x,y).
\]
Let \(\pi_{h,\omega}=M_\omega T_h\), let \(P_{h,\omega}=|\pi_{h,\omega}g\rangle\langle\pi_{h,\omega}g|\), and define
\[
\mathcal L_g:\operatorname{Mat}_{q^2}(\mathbb C)\longrightarrow\mathbb C^{q^4},
\qquad (\mathcal L_g A)_{h,\omega}=\operatorname{Tr}(AP_{h,\omega}).
\]
The domain uses the Hilbert--Schmidt norm; the codomain uses unweighted Euclidean counting norm. Thus singular values here are **not** for a probability-normalized measurement system. We discuss complex-linear operator reconstruction; no nonlinear pure-state phase-retrieval statement is asserted. A Weyl direction means an operator in the basis \(\{M_\omega T_h\}\); a phase scalar does not change that direction.

## Proof
**1. Weyl diagonalization and normalization.** The \(N^2\) Weyl operators on a group of size \(N=q^2\) are an orthogonal Hilbert--Schmidt basis, each of squared norm \(N\). Averaging conjugates of \(|g\rangle\langle g|\) over the full time-frequency group diagonalizes the frame superoperator \(\mathcal L_g^*\mathcal L_g\) in that basis. At \((h,\omega)\) its eigenvalue is \(N|\langle g,M_\omega T_hg\rangle|^2\). Consequently its analysis singular value equals
\[
s(h,\omega)=\sqrt N|\langle g,M_\omega T_hg\rangle|=q|\langle g,M_\omega T_hg\rangle|.
\]
This is also the general Gabor Gram-spectrum mechanism of Goldberger--Kang--Okoudjou, Theorem 2; the remainder evaluates it exactly for this binary graph.

For \(h=(a,b)\), substitution gives the **integer character-sum formula**
\[
s((a,b),(u,v))=\left|\sum_{t\in F:\,f(t+a)+f(t)=b}(-1)^{\operatorname{Tr}(ut+vf(t))}\right|.
\]
(The sign convention in the translation only changes an irrelevant global character.)

**2. Every nonzero horizontal translation.** For \(a\ne0\), direct expansion gives
\[
f(t+a)+f(t)=a^{2^k}t+at^{2^k}+a^{2^k+1}.
\]
After \(t=ax\), its linear part is \(a^{2^k+1}(x^{2^k}+x)\). Because \(\gcd(k,m)=1\), its kernel is exactly \(\mathbb F_2\), so precisely \(q/2\) values of \(b\) give a two-element solution fiber, \(\{t,t+a\}\), and all other \(b\) give none. For such a fiber the character sum is
\[
(-1)^{\operatorname{Tr}(ut+vf(t))}
\left(1+(-1)^{\operatorname{Tr}(ua+vb)}\right).
\]
Exactly half of the \(q^2\) character pairs \((u,v)\) make this nonzero, with absolute value \(2\). Hence there are
\[
(q-1)(q/2)(q^2/2)=(q-1)q^3/4
\]
copies of \(2\) in this stratum. Translation \((0,b)\) for \(b\ne0\) never maps \(C\) to itself and contributes only zeros.

For any function \(F\to F\), the horizontal-nonzero translation with zero modulation has singular value precisely the derivative fiber size. Every derivative fiber has even cardinality, as it is stable under \(t\mapsto t+a\). Thus its nonzero-horizontal spectrum lies in \(\{0,2\}\) if and only if every fiber size is at most \(2\), the APN condition. If APN, the entire horizontal count above follows without the Gold formula.

**3. Zero translation and exact Walsh bands.** For \(a=b=0\), the character sum is the Walsh coefficient
\[
W(u,v)=\sum_{t\in F}(-1)^{\operatorname{Tr}(ut+vt^{2^k+1})}.
\]
For \(v=0\), exactly \(u=0\) yields \(W=q\); the other \(q-1\) coefficients vanish. Fix \(v\ne0\) and put \(Q_v(t)=\operatorname{Tr}(vt^{2^k+1})\). Its polar form is
\[
B_v(x,y)=\operatorname{Tr}\!\left(v(x^{2^k}y+xy^{2^k})\right).
\]
The radical \(R_v\) consists exactly of solutions of
\[
v^{2^k}r^{2^{2k}}+vr=0.
\]
Writing \(R_v\) additively, the standard quadratic-character autocorrelation identity follows directly by setting \(y=x+r\) in the squared Walsh sum:
\[
|W(u,v)|^2=q\sum_{r\in R_v}(-1)^{Q_v(r)+\operatorname{Tr}(ur)}.
\]
Since \(Q_v\) is additive when restricted to \(R_v\), the right-hand sum is either \(0\) or \(|R_v|\). Exactly \(q/|R_v|\) values of \(u\) give the latter case by character orthogonality. Their Walsh magnitude is \(\sqrt{q|R_v|}\).

For \(r\ne0\), the radical equation is equivalent to
\[
r^{2^{2k}-1}=v^{1-2^k}.
\]
Here \(\gcd(2^{2k}-1,q-1)=2^{\gcd(2k,m)}-1\). For odd \(m\) this gcd equals \(1\), so \(|R_v|=2\) for every \(v\ne0\). Each of the \(q-1\) such \(v\) gives exactly \(q/2\) values of \(u\) with magnitude \(\sqrt{2q}\). For even \(m\) the gcd is \(3\), and \(k\) is odd. The radical has cardinality \(4\) precisely when \(v\) is a cube in \(F^\times\), of which there are \((q-1)/3\); otherwise \(|R_v|=1\). The respective nonzero Walsh values are \(2\sqrt q\) at \(q/4\) values of \(u\), and \(\sqrt q\) at all \(q\) values of \(u\). Summing yields exactly the multiplicities in the finding.

**4. Weyl kernel, rank and conditioning.** The Weyl direction indexed by translation \((a,b)\) and modulation \((u,v)\) is in \(\ker\mathcal L_g\) precisely in one of these disjoint cases:

* \(a=0\), \(b\ne0\);
* \(a\ne0\) and either \(b\notin\{f(t+a)+f(t):t\in F\}\), or \(\operatorname{Tr}(ua+vb)=1\);
* \((a,b)=(0,0)\) and either \(v=0,u\ne0\), or \(v\ne0\) with some \(r\in R_v\) satisfying \(\operatorname{Tr}(ur)+Q_v(r)=1\).

All remaining Weyl directions survive, and their singular values are listed above. The counts add to the stated rank; the complementary nullity is \(q^4-\operatorname{rank}\mathcal L_g\). For \(q\ge4\), the smallest positive singular value is \(2\) and the largest is \(q\), yielding condition number \(q/2\).

**5. Affine/CCZ invariance.** For an invertible \(\mathbb F_2\)-affine automorphism \(x\mapsto Lx+c\) of \(G\), the associated permutation unitary sends \(T_h\) to \(T_{Lh}\) and \(M_\omega\) to \(M_{\omega\circ L^{-1}}\), up to unit scalars. It therefore unitarily conjugates and merely relabels the full family of Gabor projectors. All singular values, their multiplicities, and the Weyl kernel pattern under the induced index map are preserved. This includes CCZ-equivalent binary function graphs, without asserting invariance under arbitrary nonlinear permutations.

## Verification
The standalone standard-library program `verify.py` performs direct exact finite-field character sums for every ambiguity position for \(m=2,3,4,5\) and all coprime admissible exponents \(k\). For \(m=6\), it checks every zero-translation Walsh coefficient and every derivative-fiber size, using the proved two-point-fiber lemma to count the unenumerated character modulations. It also explicitly merges the coincident spectral values at small \(q\). The embedded `verification_output.txt` reports all checks as passing. These are finite consistency checks, not an enumeration proof for arbitrary \(m\); the general proof is the algebra above.

## Relationship to prior work
The universal Gabor-Gram eigenvalue identity and the informational-completeness criterion were proved by Goldberger, Kang and Okoudjou (2021, arXiv:2106.01509, Theorems 1--2). They do not evaluate the Gold-function graph. Alaifari and Wellershoff (2019, arXiv:1901.05296) analyze stability of discrete Gabor phase retrieval rather than these complete binary Gold-graph linear-lifting spectra. Chase and Lisoněk (2021, arXiv:2110.15582, Section 3) study Gold APN-function Walsh zero spaces, particularly in odd dimensions, without giving this Gabor projector spectrum, its operator-rank formulas or Weyl kernel classification. Later work on quadratic APN Walsh spectra provides related arithmetic background but not the operator-tomography statement. The published general mechanisms make portions of this calculation accessible; the contribution here is the **explicitly evaluated complete spectral signature, its operator-kernel classification, its APN converse, and its affine transfer** rather than a new universal Gabor diagonalization or a new classification of Gold Walsh spectra.

## Limitations
No independent mathematical audit has been performed. Related literature may contain an older equivalent Gold-specialized computation under a different title or normalization; the statement should not be treated as bibliographically exhaustive. The claim is for the full complex-linear operator analysis with the specified counting normalization; it neither gives a sharp theorem for nonlinear pure-state phase retrieval nor extends the Gold formula to \(\gcd(k,m)>1\). Finite computations do not establish the theorem beyond the tested field degrees.

## References
1. R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296, public version 2019-01-12, https://arxiv.org/abs/1901.05296.
2. A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509, public version 2021-06-02, Theorems 1--2 and Section 3, https://arxiv.org/abs/2106.01509.
3. B. Chase and P. Lisoněk, *Construction of APN permutations via Walsh zero spaces*, arXiv:2110.15582, public version 2021-10-29, Section 3, https://arxiv.org/abs/2110.15582.
4. *On the Walsh spectra of quadratic APN functions*, arXiv:2510.12008 (2025), contextual comparison outside the source-date cohort, https://arxiv.org/abs/2510.12008.
