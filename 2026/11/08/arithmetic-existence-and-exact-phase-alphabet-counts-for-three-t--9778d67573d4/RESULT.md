# Arithmetic existence and exact phase-alphabet counts for three-translate cyclic Gabor tight frames

## Finding

Fix any even integer \(N=2p\ge4\), and any step \(s\in\mathbb Z_N\) of order \(\ell=N/\gcd(N,s)\ge3\). Define the three distinct translations \(K=\{0,s,2s\}\) and the even-modulation subgroup \(L=\{0,2,4,\ldots,2(p-1)\}\). Let \(g\in\mathbb C^N\) have \(|g_j|=N^{-1/2}\) for every \(j\). Set
\[
 z_j=N g_j\overline{g_{j+p}},\qquad
 \sigma_j=z_j+z_{j-s}+z_{j-2s},
\]
with all subscripts modulo \(N\). The \(3p\) vectors \(\{M_aT_kg:a\in L,\ k\in K\}\) have **exactly** the following frame-operator eigenvalues, with multiplicities:
\[
 \boxed{\frac32-\frac{|\sigma_j|}{2},\quad
 \frac32+\frac{|\sigma_j|}{2}\qquad(0\le j<p).}
\]
In particular, the system is a tight frame if and only if \(\sigma_j=0\) for all \(j\); its tight frame bound is then \(3/2\). **Such a flat complex-phase window exists if and only if**
\[
 \boxed{\ell\equiv3\pmod{6}.}
\]
Whenever that condition holds, every successful \(z\)-sequence is obtained as follows. The subgroup \(H=\langle s\rangle\) has odd order \(\ell\), its \(d=N/\ell\) cosets come in \(d/2\) pairs exchanged by addition of \(p\), and on one coset \(a+H\) of each pair,
\[
 z_{a+ts}=u\,e^{\varepsilon 2\pi i t/3}
 \quad(t\in\mathbb Z_\ell),\qquad
 u\in\mathbb T,\quad\varepsilon\in\{1,-1\};
\]
on the partner coset, \(z_{a+p+ts}=\overline{z_{a+ts}}\). Every such \(z\) is realized by flat windows \(g\), with arbitrary phases chosen independently on \(p\) antipodal coordinate pairs.

For an integer phase-alphabet size \(q\ge2\), restrict further to \(g_j\in N^{-1/2}\mu_q\), where \(\mu_q\) is the set of \(q\)-th complex roots of unity. **Such a tight frame exists if and only if** \(\ell\equiv3\pmod{6}\) **and** \(3\mid q\). In that case the exact number of indexed phase windows is
\[
 \boxed{q^p(2q)^{d/2},\qquad d=\gcd(N,s).}
\]
The count is before quotienting by global phase, translations, modulations, or any other symmetry.

## Assumptions and scope

The complex Hilbert space is \(\mathbb C^{\mathbb Z_N}\) with its standard counting inner product. Translation and modulation are \((T_kg)_j=g_{j-k}\) and \((M_ag)_j=e^{2\pi iaj/N}g_j\). Each indexed pair \((a,k)\in L\times K\) contributes one measurement vector; distinct pairs are retained with their multiplicity even if projectively coincident. There are \(3p\) such vectors and each has Euclidean norm one. By assumption \(\ell\ge3\), the three translations are distinct. No primeness restriction is made on \(p\), and no restriction is placed on the individual phases unless the \(q\)-alphabet conclusion is invoked.

## Proof

**Step 1: exact frame-spectrum reduction.** Let \(S\) be the frame operator. By summing the \(p\) even modulations,
\[
 S_{j,k}=p\,\mathbf 1_{j\equiv k\pmod{p}}
       \sum_{h\in\{0,s,2s\}}g_{j-h}\overline{g_{k-h}}.
\]
The diagonal entries are \(3p/N=3/2\). The only potentially nonzero off-diagonal entry in row \(j\) occurs at \(k=j+p\), and is \(\sigma_j/2\). Moreover \(|z_j|=1\) and \(z_{j+p}=\overline{z_j}\), whence \(\sigma_{j+p}=\overline{\sigma_j}\). Permuting coordinates into antipodal pairs gives \(p\) independent Hermitian blocks
\[
 \begin{pmatrix}3/2&\sigma_j/2\\\overline{\sigma_j}/2&3/2\end{pmatrix}
 \quad (0\le j<p).
\]
Their elementary eigenvalues give the stated spectrum. Thus tightness is equivalent to the cyclic equations \(z_j+z_{j-s}+z_{j-2s}=0\) at every site. (The equations for \(j+p\) follow by conjugation.)

**Step 2: rigidity along translation cycles.** Fix an \(s\)-orbit, writing \(w_t=z_{a+ts}\) for \(t\in\mathbb Z_\ell\). The equations read \(w_t+w_{t-1}+w_{t-2}=0\). Subtracting the equation one time step earlier gives \(w_t=w_{t-3}\). Since all \(|w_t|=1\), if \(3\nmid\ell\), then \(w\) would be constant and the original equation would force \(w=0\), impossible. Thus \(3\mid\ell\). In this case the first three values have unit modulus and sum to zero. The elementary geometry of three unit vectors shows they are \(u,u\zeta,u\zeta^2\), in either cyclic order, where \(\zeta=e^{2\pi i/3}\). Therefore \(w_t=u\zeta^{\varepsilon t}\) with \(\varepsilon=\pm1\). Conversely every such orbit sequence solves the equations.

**Step 3: the half-period obstruction.** If \(\ell\) is even, then \(p\), the unique nonzero element of order two in \(\mathbb Z_N\), lies in \(H=\langle s\rangle\) and equals \((\ell/2)s\). But \(3\mid\ell\) and \(2\mid\ell\) imply \(3\mid\ell/2\); the three-periodicity then gives \(z_{j+p}=z_j\). The necessary identity \(z_{j+p}=\overline{z_j}\) forces every \(z_j\) to be real, so each is \(+1\) or \(-1\); three such numbers cannot sum to zero. Hence \(\ell\) must be odd, proving the necessity of \(\ell\equiv3\pmod{6}\).

If \(\ell\) is odd and divisible by three, \(p\notin H\) because \(p\) has order two. Addition of \(p\) therefore pairs the \(d\) cosets of \(H\) without fixed cosets. Choose a three-periodic equilateral pattern independently on one coset from each pair and define the other by antipodal complex conjugation. The resulting \(z\) obeys every equation. Conversely Steps 1–2 force this form, so the classification is complete. To lift it to \(g\), choose any unit complex numbers \(\xi_j\) for \(0\le j<p\), and set
\[
 g_j=N^{-1/2}\xi_j,\qquad
 g_{j+p}=N^{-1/2}\xi_j\overline{z_j}.
\]
The required identities follow immediately; this proves complex-phase existence and completeness.

**Step 4: finite-alphabet rigidity and count.** Three complex numbers of modulus one sum to zero precisely when, up to a common rotation, they are the three cubic roots of unity. If all \(z_j\in\mu_q\), a rotation of this triple exists within \(\mu_q\) if and only if \(3\mid q\). For \(3\mid q\), each of the \(d/2\) independent coset pairs has exactly \(q\) choices of initial phase and two distinct orientations; the other coset is forced. There are consequently \((2q)^{d/2}\) admissible \(z\). For every such \(z\), the \(p\) values \(\xi_j\in\mu_q\) can be chosen independently, yielding exactly \(q^p\) indexed \(g\)'s. The reconstruction of \(z\) from \(g\) is unique, so no windows are double counted. This proves the formula and all quantifiers.

## Verification

`python3 CHECK.py` uses only Python's standard library. It reconstructs the complete \(N\times N\) Gabor frame operators from their \(3p\) shifted columns and independently compares all their entries to the antipodal block formula for many steps and randomly chosen phases. It also checks explicit tight constructions in several dimensions, and performs exact modular enumeration for small \(q\)-phase systems, including \((N,s,q)=(6,2,3)\), which has precisely \(162\) tight indexed windows, and \((6,2,6)\), which has precisely \(2592\). Its finite tests supplement but do not replace the proof for all \(N,s,q\).

## Relationship to prior work

Asipchuk, De Carli and Rodriguez (arXiv:2605.16139, first public version 15 May 2026) prove a general block-equivalence theorem for finite Gabor systems with subgroup modulations; their Lemma 3.1 supplies a general matrix factorization. Specializing that identity motivates Step 1 here, but their Theorems 1.1 and 1.3, Corollary 1.2, and Sections 3–5 do not give the arithmetic existence criterion for three arithmetic-progression translations, its complete phase classification, or the exact quantized-phase count. Magsino (arXiv:1611.00818, first version in 2016) gives general tightness tests involving ambiguity functions and constructs CAZAC examples; its accessible full mathematical text does not identify the present order-of-step dichotomy or enumerate these phase windows. Generic frame criteria are not being claimed as new.

## Limitations

The theorem concerns even ambient dimension, the full **even-modulation subgroup**, exactly **three translations in arithmetic progression**, and **flat-amplitude** windows. Neither a general classification for nonflat windows nor tightness for other modulation sets follows. The frame spectrum here describes linear coefficient reconstruction; it says nothing directly about nonlinear phase retrieval. The originality comparisons are based on inspected publications and available research records; specialized equivalent results under different terminology may remain undiscovered. No independent mathematical audit has been performed.

## References

1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (15 May 2026), revised v2 24 October 2026. https://arxiv.org/html/2605.16139v2
2. M. Magsino, *Constructing Tight Gabor Frames Using CAZAC Sequences*, arXiv:1611.00818 (2016). https://arxiv.org/abs/1611.00818
3. A. J. E. M. Janssen, *Duality and biorthogonality for Weyl–Heisenberg frames*, J. Fourier Anal. Appl. **1** (1994), 403–436.
