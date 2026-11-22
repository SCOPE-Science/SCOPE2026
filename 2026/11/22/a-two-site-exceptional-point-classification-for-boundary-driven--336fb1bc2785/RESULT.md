# A two-site exceptional-point classification for boundary-driven symmetric exclusion

## Finding
For the two-site symmetric simple exclusion process with exchange rate \(h>0\), reservoir refresh rates \(a,b>0\), and reservoir occupation probabilities \(0<p,q<1\), the four-state Markov generator is **not diagonalizable over \(\mathbb C\)** if and only if
\[
h=\frac{ab}{a+b}\quad\text{and}\quad p\ne q.
\]
At these and only these nonequilibrium parameter values the generator has exactly one Jordan block of size two, with eigenvalue \(-(a+b)\). In contrast, each single-site occupation mean evolves as a sum of ordinary real exponentials, without a polynomial-in-time prefactor. A two-site joint occupation can reveal the defective mode through a nonzero multiple of \(t e^{-(a+b)t}\).

For the explicit resonance \(a=b=2,\ h=1\), starting from the empty configuration, put \(s=p+q\), \(d=p-q\), and \(C_\infty=s^2/4-d^2/8\). Then for all \(t\ge0\),
\[
\Pr(\eta_1(t)=\eta_2(t)=1)=C_\infty(1-e^{-4t})-\frac{s^2}{2}(e^{-2t}-e^{-4t})+\frac{d^2}{2}t e^{-4t}.
\]
The polynomial-exponential term is present precisely for unequal reservoir densities. In this family, the first two sites and the first two independent boundary reservoirs are already sufficient for this nonequilibrium defect: a single-site continuous-time two-state chain always has a complete eigenbasis, and a two-site model with only one active bath has no eigenvalue collision for positive exchange rate.

## Assumptions and scope
There are exactly two lattice sites and configurations \(\eta=(\eta_1,\eta_2)\in\{0,1\}^2\). At rate \(h\), the occupations at the two sites are swapped, with swaps of equal bits having no effect. Independently, at rate \(a\) site one is overwritten by a new Bernoulli\((p)\) bit, and at rate \(b\) site two is overwritten by a new Bernoulli\((q)\) bit. Equivalently, the injection/removal rates are \((ap,a(1-p))\) at site one and \((bq,b(1-q))\) at site two. All five parameters satisfy the strict inequalities above. The finite-state chain is irreducible and has a unique stationary distribution.

The Markov generator \(L\) acts on observables; the row transition-rate generator and its transpose have the same spectrum and Jordan structure. A defective eigenvalue means algebraic multiplicity exceeds geometric multiplicity. The fixed-time probability formula uses the deterministic empty initial condition, while the general classification is independent of the initial law.

## Proof
In the ordered observable basis \((1,\eta_1,\eta_2,\eta_1\eta_2)\), a direct enumeration of swaps and reservoir overwrites gives
\[
L1=0,\qquad L\eta_1=ap-(a+h)\eta_1+h\eta_2,\qquad L\eta_2=bq+h\eta_1-(b+h)\eta_2,
\]
\[
L(\eta_1\eta_2)=bq\eta_1+ap\eta_2-(a+b)\eta_1\eta_2.
\]
The middle two-dimensional diagonal block is the real symmetric matrix
\[
M=\begin{pmatrix}-a-h&h\\h&-b-h\end{pmatrix}.
\]
Consequently the exact characteristic polynomial of the full generator is
\[
\chi_L(z)=z(z+a+b)\left[z^2+(a+b+2h)z+ab+h(a+b)\right].
\]
Its four real eigenvalues are \(0\), \(-(a+b)\), and
\[
-\frac{a+b+2h}{2}\pm\sqrt{h^2+\frac{(a-b)^2}{4}}.
\]
The two eigenvalues of \(M\) are distinct since \(h>0\), and they are both negative. The only possible repeated eigenvalue of the four-dimensional generator is a collision between \(-(a+b)\) and one eigenvalue of \(M\). Its criterion is
\[
\det(M+(a+b)I)=ab-h(a+b)=0.
\]
Thus the collision occurs exactly at \(h=ab/(a+b)\). Then \(M(a,-b)^T=-(a+b)(a,-b)^T\), while the other middle-block eigenvalue is \(-2h\), distinct from \(-(a+b)\) because \(a+b>2ab/(a+b)\). The coupling of the pair-occupation equation to the colliding eigenvector is
\[
(bq,ap)\begin{pmatrix}a\\-b\end{pmatrix}=ab(q-p).
\]
If \(p\ne q\), this is nonzero, so the repeated eigenvalue has a one-dimensional eigenspace and forms a size-two Jordan block. If \(p=q\), the coupling vanishes and the eigenspace has dimension two; all blocks are diagonalizable. Away from the collision all four eigenvalues are simple. This proves the necessary-and-sufficient classification and the Jordan multiplicity statement.

Let \(m_i(t)=\mathbb E[\eta_i(t)]\) and \(C(t)=\mathbb E[\eta_1(t)\eta_2(t)]\). Their exact evolution is
\[
\begin{pmatrix}m_1'\\m_2'\end{pmatrix}=M\begin{pmatrix}m_1\\m_2\end{pmatrix}+\begin{pmatrix}ap\\bq\end{pmatrix},\qquad
C'=-(a+b)C+bq m_1+ap m_2.
\]
Since \(M\) is symmetric, both means are pure sums of two decaying exponentials about their stationary values, even at resonance. Set \(S=a+b\) and write \(\mathbf m_\infty=-M^{-1}(ap,bq)^T\). At resonance, projection of the initial mean deviation onto the fast eigenvector \((a,-b)\) shows that the coefficient of \(t e^{-St}\) in \(C(t)\) is exactly
\[
J=\frac{ab(q-p)}{a^2+b^2}\left[a(m_1(0)-m_{1,\infty})-b(m_2(0)-m_{2,\infty})\right].
\]
For \(a=b=2,\ h=1\), the stationary means are \((3p+q)/4\) and \((p+3q)/4\). For the all-empty initial law, substitution in the preceding linear equations gives \(J=(p-q)^2/2\), the displayed exact formula, and \(C_\infty=s^2/4-d^2/8\). The positive quadratic coefficient proves visibility of the Jordan mode in that joint observable for every \(p\ne q\).

For minimality, a one-site ergodic two-state generator has eigenvalues zero and minus its positive total flip rate, so cannot be defective. With two sites but only one active bath (say \(b=0\)), the four eigenvalues \(0,-a\) and the two distinct roots of \(z^2+(a+2h)z+ah\) are all distinct for \(a,h>0\): substituting \(z=-a\) gives \(-ah\ne0\), and the quadratic discriminant is \(a^2+4h^2>0\). The other one-bath case is symmetric.

## Verification
A standalone `verify.py` builds the physical four-state row generator independently from the moment equations, checks the symbolic characteristic polynomial and resonance, checks Jordan eigenspace dimensions using exact rational arithmetic in five cases, tests off-resonance eigenvalues, and compares the exact two-site occupation formula against matrix exponentials for five reservoir choices at six observation times each (30 comparisons). Its successful execution produced:

```
PASS symbolic 4-state characteristic polynomial
PASS exact collision and nonzero off-diagonal Jordan coupling
PASS five exact algebraic/geometric multiplicity checks
PASS off-resonance distinct-spectrum checks
PASS 30 independent numerical matrix exponential versus closed form cases
PASS visibility criterion for the double occupancy signal
ALL CHECKS PASSED
```

Run with `python verify.py` after installing NumPy, SymPy, and SciPy. The infinite continuum of allowed parameters is covered by the symbolic proof, not inferred from finite tests.

## Relationship to prior work
Schulman and Sinclair (2026, arXiv:2607.22991) prove that the spectrum of nonequilibrium symmetric exclusion is independent of reservoir densities and provide a **three-site**, endpoint-driven nondiagonalizable example (Remark 10). Their general spectral-invariance theorem includes the density-independence of the eigenvalues here; that fact is *not* claimed as new. The finding here instead supplies a sharp necessary-and-sufficient resonance surface and nonequilibrium condition for **two sites**, establishes the smallest-system boundary, and identifies an exact observable that detects the resulting defective relaxation while all one-point means do not.

Frassek (2019, arXiv:1910.13163) constructs eigenstates of boundary-driven SSEP using integrable spin chains and supplies stationary correlations, but expressly assumes nondegenerate eigenvalues in the eigenvector construction (Section 2.1, item (iii), and Section 2.2); hence the singular resonant Jordan case is not established by that construction. Floreani and González Casanova (2023, arXiv:2307.02481) describe nonequilibrium stationary measures through a mixture representation, not a complete transient Jordan classification. The general matrix and exclusion literature remains a possible source of equivalent special-case formulas.

## Limitations
The classification concerns only two sites, strictly positive exchange and both reservoir refresh rates, and interior reservoir probabilities. The explicit pair-occupation formula assumes a specified empty initial condition and the symmetric-rate example. The general Jordan coefficient may vanish for specially selected initial states or observables, despite generator defectiveness. A finite collection of literature searches cannot establish publication priority; integrability-derived exceptional cases or equivalent elementary two-site transient calculations may already exist. No result is asserted for larger graphs, interacting multispecies variants, or singular endpoint reservoirs.

## References
1. Leonard J. Schulman and Alistair Sinclair, *Mixing times and spectra of non-equilibrium symmetric exclusion processes on general graphs*, arXiv:2607.22991, first publicly submitted 25 July 2026. https://arxiv.org/abs/2607.22991
2. Rouven Frassek, *Eigenstates of triangularisable open XXX spin chains and closed-form solutions for the steady state of the open SSEP*, arXiv:1910.13163 (2019). https://arxiv.org/abs/1910.13163
3. Simone Floreani and Adrian González Casanova, *Non-equilibrium steady state of the symmetric exclusion process with reservoirs*, arXiv:2307.02481 (2023). https://arxiv.org/abs/2307.02481
4. Hong-Quan Tran, *Cutoff for the non reversible SSEP with reservoirs*, arXiv:2211.14687 (2022). https://arxiv.org/abs/2211.14687
