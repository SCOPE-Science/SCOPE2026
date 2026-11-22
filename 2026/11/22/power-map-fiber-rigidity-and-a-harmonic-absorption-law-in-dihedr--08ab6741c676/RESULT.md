# Power-map fiber rigidity and a harmonic absorption law in dihedral \(0\)-Hecke monoids

## Finding

For every integer \(m\ge3\), write \(H_m=H_0(I_2(m))\), the \(0\)-Hecke monoid of the finite dihedral Coxeter system with braid length \(m\). Let \(z\) be its absorbing longest element, and let \(\Phi_r:H_m\to H_m\) be the set map \(\Phi_r(x)=x^r\) for an integer \(r\ge1\). Put
\[
A_r=\left\lfloor\frac{m-1}{2r}\right\rfloor,\qquad
B_r=\left\lfloor\frac{m-2}{2r}\right\rfloor.
\]
Then the exact image and longest-element fiber sizes are
\[
|\Phi_r(H_m)|=4+2(A_r+B_r),\qquad
|\Phi_r^{-1}(z)|=2m-3-2(A_r+B_r).
\]
All other fibers of \(\Phi_r\) contain at most one element. At \(r=2\), the exact number of roots of the absorbing element exhibits an arithmetic mod-four split:
\[
|\{x\in H_m:x^2=z\}|=
\begin{cases}
m,&m\text{ odd},\\
m+1,&m\equiv0\pmod4,\\
m-1,&m\equiv2\pmod4.
\end{cases}
\]
These are consequences of the full explicit power normal form proved below, not isolated numerical coincidences.

Uniformly sample \(x\) among the \(2(m-2)\) nonidempotent elements and let \(T_m=\min\{r\ge1:x^r=z\}\). Then for every integer \(r\ge1\),
\[
\Pr(T_m\le r)=1-\frac{A_r+B_r}{m-2}.
\]
Consequently, for every fixed integer \(k\ge2\),
\[
\lim_{m\to\infty}\Pr(T_m=k)=\frac1{k(k-1)},\qquad
\mathbb E[T_m]=\log m+O(1).
\]
The limiting distribution has infinite mean, although every finite monoid has a finite maximum absorption time \(\lceil m/2\rceil\). The exact finite distribution, mod-four root count and power-fiber rigidity form one classification of the same family of power maps.

## Assumptions and scope

The Coxeter generators are named \(s,t\). The monoid has presentation \(\pi_s^2=\pi_s\), \(\pi_t^2=\pi_t\), and equality of the two alternating products of length \(m\). It has \(2m\) distinct elements: the identity \(1\); two alternating words \(a_\ell\) and \(b_\ell\) of each length \(1\le\ell<m\), starting respectively with \(\pi_s\) and \(\pi_t\); and the common longest element \(z=a_m=b_m\). Here \(z\) is an absorbing monoid element, not an additive zero. All assertions hold over the abstract monoid: there is no coefficient field and no restriction on characteristic. The set power map is not asserted to be a monoid homomorphism.

The only idempotents are \(1,a_1,b_1,z\). Nonidempotents are exactly the alternating elements of lengths \(2,\ldots,m-1\).

## Proof

**Normal-form power calculation.** In the dihedral Coxeter system, an alternating word shorter than \(m\) has a unique reduced expression. Right multiplying by a simple \(0\)-Hecke generator increases Coxeter length precisely when that generator is different from the last letter of the current alternating word; otherwise idempotence discards it. The first time length reaches \(m\), the element is \(z\) and remains there. Thus, before absorption, concatenation of an alternating word of length \(\ell\) with itself gains \(\ell\) letters when \(\ell\) is even, because the boundary letters differ, and gains \(\ell-1\) when \(\ell\) is odd, because the boundary letters coincide. The output retains its first letter, and its parity is respectively even or odd. Induction gives for all \(r\ge1\), with \(c\) denoting either initial generator,
\[
(c_\ell)^r=\begin{cases}
c_{r\ell},&\ell\text{ even and }r\ell<m,\\
c_{r(\ell-1)+1},&\ell\text{ odd and }r(\ell-1)+1<m,\\
z,&\text{otherwise},
\end{cases}
\]
where the first two lines are interpreted only at lengths strictly less than \(m\). The identity and \(z\) are fixed. In particular, the two length-one elements are fixed and all other alternating elements eventually reach \(z\).

**All power fibers.** Each nonabsorbed even-length output has length \(2rh\) for a unique source length \(2h\). This occurs for exactly \(1\le h\le A_r\). Each nonabsorbed odd-length output of length greater than one has length \(2rh+1\) for a unique source length \(2h+1\), with exactly \(1\le h\le B_r\). The initial generator is preserved, and outputs of opposite parity cannot collide. Together with the fixed elements \(1,a_1,b_1,z\), this gives \(4+2(A_r+B_r)\) distinct images; each image other than \(z\) has exactly one preimage. Since \(|H_m|=2m\), the remaining fiber has \(2m-3-2(A_r+B_r)\) points. Substituting \(r=2\) and evaluating the two floors separately for odd \(m\), multiples of four and integers congruent to two modulo four establishes the stated square-root trichotomy.

**Absorption times and limiting law.** For the two elements of length \(\ell\) with \(2\le\ell<m\), the first exponent reaching \(z\) is
\[
\tau_m(\ell)=\begin{cases}
\lceil m/\ell\rceil,&\ell\text{ even},\\
\lceil(m-1)/(\ell-1)\rceil,&\ell\text{ odd}.
\end{cases}
\]
Exactly \(A_r+B_r\) of the \(m-2\) possible lengths have not absorbed by time \(r\), proving the exact cumulative distribution. Since \(A_r+B_r=m/r+O_r(1)\) for fixed \(r\), the limit satisfies \(\Pr(T_m\le r)\to1-1/r\). Taking consecutive differences gives the probability mass \(1/[k(k-1)]\) for \(k\ge2\), which sums to one but has divergent mean. Finally, uniformly for \(2\le\ell<m\), the displayed formula implies \(\tau_m(\ell)=m/\ell+O(1+m/\ell^2)\). Hence
\[
\mathbb E[T_m]=\frac1{m-2}\sum_{\ell=2}^{m-1}\tau_m(\ell)
=\frac m{m-2}\sum_{\ell=2}^{m-1}\frac1\ell+O(1)
=\log m+O(1).
\]
No interchange of the diverging limiting expectation with a finite-\(m\) mean is used.

## Verification

The standalone `verify_power_maps.py` tests the Demazure right-generator multiplication independently of the closed power formulas. It compares every element power for \(3\le m\le80\), \(1\le r\le m+5\); checks complete fiber counts, uniqueness of all nonabsorbing fibers, every individual absorption time, square-root counts, and associativity in small monoids. It also checks finite-size frequency approximations at \(m=1000,10000,100000\). Run `python verify_power_maps.py` using Python 3; the recorded stdout is `checker_output.txt`. Enumeration corroborates finitely many instances; the proof above is the basis for all-parameter claims.

## Relationship to prior work

Denton, Hivert, Schilling and Thiéry (2010), Section 2.4, establish the standard \(0\)-Hecke presentation, canonical indexing by Coxeter elements, and monoid structure in a representation-theoretic investigation. Denton's 2011 dissertation, Section 2.1, explicitly records the known eventual-power identity \(x^\omega=w^+_{J(x)}\); this qualitatively implies that every dihedral element supported on both generators eventually reaches the longest parabolic element. Neither inspected treatment states the first hitting exponent for each dihedral element, the complete power-image/fiber formulas, the mod-four square-root trichotomy, or the limiting absorption-depth distribution. The dissertation's Section 2.5 concerns powers of *diagram demipotents in the monoid algebra*, not powers of individual monoid elements. Thus the known eventual idempotence is foundational prior work, not claimed as a new result.

A separate exact heavy-tailed law with probability mass \(1/[k(k-1)]\) is recorded for nilpotent consecutive-diagonal rook inverse monoids, a different semigroup with different multiplication and zero. The probability law itself is therefore not claimed to be unprecedented among finite semigroups; what is asserted here is its precise occurrence and complete finite power-map fiber structure in the dihedral \(0\)-Hecke family. The full formulas may follow quickly from classical dihedral normal forms, and undiscovered prior quantitative treatments remain a priority risk.

## Limitations

The work concerns only finite rank-two dihedral \(0\)-Hecke monoids, not general higher-rank Coxeter types or algebra-valued demipotents. The power-map formulas are elementary consequences of the special alternating normal form; no broad classification of aperiodic semigroups is implied. Independent historical-priority review has not been performed. Finite checker examples are not proofs of the infinite family or limit law.

## References

1. T. Denton, F. Hivert, A. Schilling and N. M. Thiéry, *On the representation theory of finite \(\mathcal J\)-trivial monoids*, arXiv:1010.3455, originally made public 2010-10-17; Section 2.4. https://arxiv.org/abs/1010.3455
2. T. Denton, *Excursions into Algebra and Combinatorics at \(q=0\)*, arXiv:1108.4379, originally made public 2011-08-22; Sections 2.1 and 2.5. https://arxiv.org/abs/1108.4379
3. SageMath, *Hecke Monoids*, online documentation for the standard monoid presentation. https://doc.sagemath.org/html/en/reference/monoids/sage/monoids/hecke_monoid.html
