# Complete two-sum multiplicity spectrum of the finite-field quartic graph

## Finding
Let \(F=\mathbb F_q\) have characteristic greater than \(3\), let
\[C_4=\{(t,t^4):t\in F\},\qquad r(s,y)=\#\{(t,u)\in F^2:t+u=s,\ t^4+u^4=y\},\]
where ordered pairs are counted. Let \(\chi\) be the quadratic character of \(F\), with \(\chi(0)=0\), and write
\[\epsilon=\chi(-1),\qquad\delta=\chi(-3),\qquad\eta=\chi(-6),\qquad g=\gcd(4,q-1).\]
For every fixed \(s\in F^\times\), the numbers \(k_j=\#\{y\in F:r(s,y)=j\}\) are independent of \(s\), vanish for \(j>4\), and satisfy the **complete** formula
\[
\boxed{\begin{aligned}
k_0&=\frac{5q-4+2\eta-\epsilon-2\delta}{8},&
k_1&=\frac{1-\eta}{2},\\
k_2&=\frac{q+\epsilon+2\delta}{4},&
k_3&=\frac{1+\eta}{2},\\
k_4&=\frac{q-4-2\eta-\epsilon-2\delta}{8}.
\end{aligned}}
\]
At \(s=0\), exactly one target has multiplicity \(1\), exactly \((q-1)/g\) targets have multiplicity \(g\), and all other targets have multiplicity \(0\). In particular, writing \(N_j=\#\{(s,y)\in F^2:r(s,y)=j\}\),
\[
\boxed{\begin{aligned}
N_0&=(q-1)k_0+(q-1)-(q-1)/g,\\
N_1&=(q-1)k_1+1,\\
N_2&=(q-1)k_2+\mathbf{1}_{g=2}(q-1)/g,\\
N_3&=(q-1)k_3,\\
N_4&=(q-1)k_4+\mathbf{1}_{g=4}(q-1)/g.
\end{aligned}}
\]
The exact twofold sumset size is therefore
\[
\boxed{|C_4+C_4|=1+\frac{(q-1)(3q+7+2\delta-2\eta)}8.}
\]
The appearance of \(\chi(-6)\) in the full spectrum and sumset distinguishes information not determined by the known total additive energy, which depends on \(\chi(-3)\) alone.

## Assumptions and scope
The field can have prime or nonprime order. Characteristic \(2\) and \(3\) are excluded; characteristic \(5\) and \(7\) are included. We count *ordered* representations, so \(r(s,y)\) need not be the number of unordered pairs. All values of \(y\), including those of zero multiplicity, are counted in \(k_0\). Every formula is an exact finite-field equality, not an asymptotic. With \(q\) odd, \(g=2\) if \(q\equiv3\pmod4\) and \(g=4\) if \(q\equiv1\pmod4\).

## Proof
**1. Scaling and the quadratic involution.** Fix \(s\ne0\) and write \(t=s(1+w)/2\), \(u=s(1-w)/2\). Direct expansion gives
\[\frac{t^4+u^4}{s^4}=\frac{w^4+6w^2+1}{8}.\]
Set \(v=w^2\). For each target \(\lambda=y/s^4\), solving for \(v\) gives \(v^2+6v+1=8\lambda\), with \(1+\chi(v)\) lifts \(w\in F\). The two solutions for \(v\), if distinct, are exchanged by the affine involution \(T(v)=-6-v\). This involution has the sole fixed point \(v=-3\); its only nonfixed orbit containing zero is \(\{0,-6\}\). The images of these two special orbits are distinct because the first maps to \(\lambda=-1\) and the second to \(\lambda=1/8\), which are unequal in characteristic greater than \(3\).

**2. Special targets.** At the fixed point \(v=-3\), there are precisely \(1+\chi(-3)=1+\delta\) lifts; hence its target has multiplicity \(0\) if \(\delta=-1\) and \(2\) if \(\delta=1\). At \(\{0,-6\}\), the contributions are \(1\) and \(1+\chi(-6)\), giving multiplicity \(2+\eta\): precisely \(1\) if \(\eta=-1\), and \(3\) if \(\eta=1\).

**3. The remaining nonfixed orbits.** Remove the points \(0,-6,-3\) from \(F\). All remaining orbits of \(T\) have two nonzero elements. Write \(A\), \(B\), \(C\) for the numbers of these orbits on which the quadratic characters of the two elements are respectively \((+1,+1)\), \((-1,-1)\), or opposite. These give target multiplicities \(4,0,2\), respectively.

The standard quadratic Jacobi identity, valid because \(-6\ne0\), is
\[\sum_{v\in F}\chi(v)\chi(-6-v)=-\chi(-1)=-\epsilon.\]
Also \(\sum_{v\in F}\chi(v)=0\), \(\chi(-3)=\delta\), and \(\chi(-6)=\eta\). Excluding \(0,-6,-3\) and pairing the remaining points under \(T\) gives three relations
\[
A+B+C=\frac{q-3}{2},\qquad
A-B=-\frac{\eta+\delta}{2},\qquad
A+B-C=\frac{-\epsilon-\delta^2}{2}.
\]
As \(\delta^2=1\), solving gives
\[
\boxed{A=\frac{q-4-2\eta-\epsilon-2\delta}{8},\quad
B=\frac{q-4+2\eta-\epsilon+2\delta}{8},\quad
C=\frac{q-2+\epsilon}{4}.}
\]
(Equivalently, the character-product relation is \(2(A+B-C)+1=-\epsilon\); the last singleton term is the fixed point contribution.)

**4. Targets without any quadratic root.** The discriminant of \(v^2+6v+1-8\lambda\) is \(32(1+\lambda)\). Since \(\lambda\mapsto32(1+\lambda)\) is a bijection of \(F\), exactly \((q-1)/2\) targets yield nonsquare discriminant and no \(v\). The nonfixed orbits of nonsquares contribute another \(B\) zero-multiplicity targets, and the fixed point contributes one more precisely when \(\delta=-1\). Hence
\[k_0=(q-1)/2+B+(1-\delta)/2.\]
The positive multiplicities are \(k_1=(1-\eta)/2\), \(k_2=C+(1+\delta)/2\), \(k_3=(1+\eta)/2\), and \(k_4=A\). Substitution of \(A,B,C\) proves the five displayed expressions. Nonnegative integrality follows directly from their interpretation as counts of orbits and targets; no divisibility assumption is being imported.

**5. The zero-sum slice and the global spectrum.** If \(s=0\), then \(u=-t\) and \(y=2t^4\). The map \(F^\times\to F^\times\), \(t\mapsto t^4\), is a homomorphism with kernel of size \(g\). Thus \(y=0\) has one preimage, \((q-1)/g\) distinct nonzero values of \(y\) have exactly \(g\) preimages, and all others have none. Adding this slice to the \(q-1\) identical nonzero slices gives every \(N_j\) above. Counting positive-multiplicity targets gives
\[
|C_4+C_4|=1+\frac{q-1}{g}+(q-1)(q-k_0)
=1+\frac{(q-1)(3q+7+2\delta-2\eta)}8,
\]
where the second equality uses the dependence of \(g\) on \(\epsilon\). This completes the classification.

As a consistency identity, the spectrum yields
\[
\sum_{s,y}r(s,y)^2=3q^2-3q-2(q-1)\chi(-3)+1,
\]
which agrees with the previously known total quartic-graph additive energy. This energy identity is **not** asserted to be new.

## Verification
Run `python verify_quartic.py` after extracting the files. The self-contained integer-arithmetic program directly constructs all \(q^2\) ordered pairs, their sums and fourth powers, and their multiplicity distribution. It compares the exact five-level histogram, weighted first and second moments, and the sumset size to the formulas. Thirteen prime fields of orders \(5,7,11,13,17,19,23,29,31,37,41,43,47\) and three quadratic extension fields of orders \(25,49,121\) passed; see `verification_output.txt` for the actual run. Enumeration is corroborative; the algebraic argument above proves the infinite family.

## Relationship to prior work
The public result *Exact additive energy of the finite-field quartic graph* obtains the total collision count via the product involution \(u\mapsto2s^2-u\) and shows its dependence on \(\chi(-3)\); its full mathematical statement and proof do **not** give target-by-target fiber frequencies or the twofold sumset size. The public result *An arithmetic phase transition in the invariant quartic-curve Fourier norm* computes a different local collision statistic and a sharp norm on a two-orbit coefficient subspace; its local coefficient-incidence statistic involving \(\chi(-7)\) does not give the present image-fiber multiplicities. The public result *Complete two-sum spectrum of the finite-field fifth-power graph* determines the analogous problem for odd power \(5\); its zero-sum fiber is an additive collapse and its nonzero-sum quadratic orbit is different, so those formulas do not specialize to even power \(4\). The published quartic-image phase theorems *Sidon quartic-power images and the complete phase-only fourth-moment equality groups* and *Quartic-image Singer geometry and all unimodular Fourier fourth-moment maximizers over thirteen elements* **already report the quartic pair-sum fiber histograms in the exceptional fields of orders \(5\) and \(13\)**. Those two special cases are not new; their phase classifications and finite tables do not establish the present general-character formula for all finite fields.

The relevant finite-field Fourier-extension framework and convolution fourth-moment method appear in Mockenhaupt--Tao; González-Riquelme--Oliveira e Silva establish sharp inequalities for parabolas, paraboloids and cones, not this quartic graph. In contrast with the earlier quartic energy, the current sumset size detects \(\chi(-6)\), an arithmetic parameter absent from the total energy.

## Limitations
The special field-order-five and field-order-thirteen histograms were previously computed; originality applies to the uniform all-field classification, the character-resolved formulas, and the general sumset theorem, not those finite cases. The classification applies to twofold sums of the unweighted quartic graph over fields of characteristic at least five. It does not prove sharp weighted Fourier-extension norms or classifications of weighted extremizers, nor address characteristics two and three. Exhaustive checks over sixteen finite fields do not prove the universal result. An equivalent but unindexed finite-field fiber-count or sumset formula may exist; the comparison provides best-knowledge originality rather than a priority certification. Independent validation has not been performed.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (2002).
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first public 26 May 2024), especially the finite-field fourth-moment convolution formulation.
3. *Exact additive energy of the finite-field quartic graph*, published mathematical result, 2026, public full text: https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f/RESULT.md.
4. *An arithmetic phase transition in the invariant quartic-curve Fourier norm*, published mathematical result, 2026, public full text: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-an-arithmetic-phase-transition-in-the-invariant-quartic-curve-fo--ba1c8156001a/RESULT.md.
5. *Complete two-sum spectrum of the finite-field fifth-power graph*, published mathematical result, 2026, public full text: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-two-sum-spectrum-of-the-finite-field-fifth-power-graph--f9410cde2e91/RESULT.md.
6. *Sidon quartic-power images and the complete phase-only fourth-moment equality groups*, published mathematical result, 2026, full text: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sidon-quartic-power-images-and-the-complete-phase-only-fourth-mo--bccd0021eeec/RESULT.md.
7. *Quartic-image Singer geometry and all unimodular Fourier fourth-moment maximizers over thirteen elements*, published mathematical result, 2026, full text: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-quartic-image-singer-geometry-and-all-unimodular-fourier-fourth--3cf25572a021/RESULT.md.
