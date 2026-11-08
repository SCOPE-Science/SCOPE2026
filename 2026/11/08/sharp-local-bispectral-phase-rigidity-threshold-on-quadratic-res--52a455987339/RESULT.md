# Sharp local bispectral phase-rigidity threshold on quadratic-residue Fourier supports

## Finding

For every odd prime \(p\), put \(H=(\mathbb F_p^\times)^2\) and \(m=(p-1)/2\). Construct the integer matrix \(R_p\) with one column for each \(h\in H\) and one row for each ordered triple \((a,b,a+b)\in H^3\). The triple contributes the row \(e_a+e_b-e_{a+b}\), allowing repeated indices. Then its **exact rational rank** is
\[
\boxed{\operatorname{rank}_{\mathbb Q}R_p=
\begin{cases}
0,&p=3,5,\\
4,&p=13,\\
(p-1)/2,&\text{for every other odd prime }p.
\end{cases}}
\]
These are all exceptions; in particular, every prime \(p\ge17\) has full rank.

For a complex signal on \(\mathbb Z/p\mathbb Z\) whose Fourier transform is nonzero exactly on \(H\), fix its nonzero Fourier magnitudes and observe the complete complex bispectrum \(B(a,b)=\widehat f(a)\widehat f(b)\overline{\widehat f(a+b)}\). The phase-ratio fiber is the compact subgroup
\[
\mathcal K_p=\{(u_h)_{h\in H}\in\mathbb T^H:\ u_au_b=u_{a+b}\text{ whenever }a,b,a+b\in H\}.
\]
Its identity component has dimension \(m-\operatorname{rank}R_p\). Thus there are positive-dimensional phase ambiguities precisely at \(p=3,5,13\), with dimensions \(1,2,2\), respectively. For every other odd prime the phase fiber is finite (local rigidity); **its exact finite cardinality and global uniqueness modulo translation are not asserted**.

At \(p=13\), the fiber is in fact exactly a two-torus: \(H=\langle4\rangle\), and all phases are
\[
(u_{4^j})_{j=0}^{5}=(A,B,B/A,1/A,1/B,A/B),\qquad A,B\in\mathbb T.
\]

## Assumptions and scope

Here \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). All Fourier coefficients on \(H\) are assumed nonzero, with arbitrary fixed positive magnitudes; coefficients off \(H\) vanish. The bispectrum is measured as a complex number, not only its magnitude. The setting is the prime cyclic group with no real-valuedness assumption on the signal. The rank is over \(\mathbb Q\) (equivalently \(\mathbb R\) or \(\mathbb C\)); the theorem does **not** determine the integer Smith normal form for arbitrary primes, and does not promote local injectivity to global injectivity.

## Proof

**1. Phase relations.** If two signals have the same fixed nonzero Fourier magnitudes, define \(u_h=\widehat g(h)/\widehat f(h)\in\mathbb T\). Equality of their complex bispectra is equivalent to \(u_au_b=u_{a+b}\) at precisely the triples in the statement; every other bispectral entry vanishes for both. The identity-component dimension of this torus homomorphism kernel is the real nullity of the displayed integer relation matrix.

**2. Multiplicative translation and diagonalization.** Let \(D=\{x\in H:1-x\in H\}\). Each supported triple has the unique normalized form \((tx,t(1-x),t)\) with \(t\in H,x\in D\). Hence the row constraints, on functions \(v:H\to\mathbb C\), are
\[
v(tx)+v(t(1-x))-v(t)=0\qquad(t\in H,x\in D).
\]
The multiplicative characters \(\chi\in\widehat H\) are a basis for \(\mathbb C^H\). Substitution of \(v(t)=\chi(t)\) gives the scalar condition
\[
\chi(x)+\chi(1-x)=1\quad\text{for every }x\in D.
\]
Therefore the nullity is exactly the number of multiplicative characters satisfying all these scalar equalities.

**3. Unit-circle rigidity.** If complex numbers \(u,v\) have \(|u|=|v|=1\) and \(u+v=1\), then \(u,v\) are the two primitive sixth roots \(e^{\pm i\pi/3}\), in either order: the two unit circles centered at \(0\) and \(1\) meet at precisely these points. Consequently an exceptional multiplicative character \(\chi\) must have order divisible by six, and every \(x\in D\) must lie in one of just two fibers of \(\chi\). If \(d=\operatorname{ord}\chi\), each fiber has size \(m/d\), so necessarily
\[
|D|\le 2m/d\le m/3.
\]
The trivial character is never exceptional when \(D\ne\varnothing\), since its scalar sum is \(2\), not \(1\).

**4. Exact quadratic-residue count.** Extend the Legendre symbol by \(\eta(0)=0\). Expanding the product of quadratic-residue indicators and using
\[
\sum_x\eta(x)=0,\qquad\sum_x\eta(x)\eta(1-x)=-\eta(-1),
\]
then removing the exceptional terms \(x=0,1\), yields
\[
|D|=\frac{p-4-\eta(-1)}4=
\begin{cases}(p-5)/4,&p\equiv1\pmod4,\\(p-3)/4,&p\equiv3\pmod4.\end{cases}
\]
For \(p\equiv3\pmod4\), \(m\) is odd and cannot support a multiplicative character of order divisible by six. In this residue class \(D\ne\varnothing\) for all \(p\ge7\). For \(p\equiv1\pmod4\), one has \(|D|=(p-5)/4>m/3=(p-1)/6\) as soon as \(p>13\). Step 3 then excludes every exceptional character. The only remaining primes are \(3,5,13\).

**5. Sharp exceptions.** At \(p=3,5\), the set \(D\) is empty, so there are no rows and ranks are zero. At \(p=13\), \(H=\langle4\rangle\) has size six and \(D=\{4,10\}=\{4,4^{-1}\}\). Exactly the two characters with \(\chi(4)=e^{\pm i\pi/3}\) satisfy \(\chi(4)+\chi(10)=1\). Hence the nullity is two and the rank is four. Writing \(A=u_1,B=u_4\), the six multiplicative translates of the relation \(u_4u_{10}=u_1\) successively give the two-torus parametrization in the finding. This closes the proof for every odd prime.

## Verification

Run \(\texttt{python3 check_paley_bispectrum.py}\) from the directory containing the embedded checker. The script constructs every normalized triple, checks the exact quadratic-residue counts, and computes relation-matrix ranks modulo two different large coefficient primes for all 25 odd primes through \(101\). It additionally computes rational ranks directly for all primes through \(31\) and verifies the entire two-parameter family for \(p=13\) at several phase choices. Result: \(\texttt{PALEY_BISPECTRAL_LOCAL_RIGIDITY_CHECK_PASS}\). Modular rank tests are finite corroboration, not an all-prime or integral Smith-form certificate; the all-prime theorem follows from steps 2–5.

## Relationship to prior work

Kondor's 2007 preprint develops the skew spectrum of finite groups and relates bispectral completeness to full Fourier support. Kakarala's 2009 preprint develops bispectral completeness for compact groups. Their full-support hypotheses do not cover the Fourier transforms vanishing outside the quadratic-residue set. Existing sharp fourth-moment results for Paley frequency supports concern extremizers of a different inequality, not the rank of the Schur-triple bispectral phase relation matrix, and are limited in the compared statement to primes \(p\equiv3\pmod4\). Known sharp phase-recovery results on asymmetric contiguous frequency supports use interval geometry rather than this multiplicative subgroup. The new distinction is the uniform rank classification and the isolated two-torus at \(p=13\); no discovery priority beyond the inspected literature is certified.

## Limitations

Only prime cyclic groups and the nonzero quadratic-residue Fourier support are treated. Real or conjugate-symmetric signals, finite field extensions, noisy or incomplete bispectral measurements, and global enumeration of discrete phase ambiguities are outside scope. Full rational rank implies only local rigidity, not that translations exhaust the global fiber. A more general prior partial-character theorem could imply the result.

## References

- R. Kondor, *The skew spectrum of functions on finite groups and their homogeneous spaces*, arXiv:0712.4259, first publicly posted 2007-12-27, https://arxiv.org/abs/0712.4259.
- R. Kakarala, *The bispectrum as a source of phase-sensitive invariants for Fourier descriptors: a group-theoretic approach*, arXiv:0902.0196, first posted 2009-02-02, https://arxiv.org/abs/0902.0196.
- Related literature on finite Fourier fourth moments, Paley spectra, and bispectral recovery from interval supports was compared at the level of the theorem statements and inspected arguments; no global-priority assertion is made.
