# Primitive spatial extinction under two-scale finite differences

## Finding

Let \(q=p^h\) be a prime power and \(n\ge2\) an integer with \(p\nmid n\). On the cyclic lattice \(\mathbb Z/n\mathbb Z\) consider the shift \((Sx)_i=x_{i+1}\) and the two-scale finite-difference cellular automaton
\[
F_{a,b}=(I-S^a)(I-S^b),\qquad a,b\ge1.
\]
A configuration is *primitive* if its least positive spatial shift period is \(n\). Write \(C_q(n;a,b)\) for the number of primitive configurations annihilated in **one** update by \(F_{a,b}\). Then, with \(\mu\) denoting arithmetic Möbius,
\[
\boxed{C_q(n;a,b)=\sum_{d\mid n}\mu(n/d)\,q^{\gcd(d,a)+\gcd(d,b)-\gcd(d,a,b)}.}
\]
Set \(A=\gcd(n,a)\), \(B=\gcd(n,b)\). The precise existence boundary is
\[
\boxed{C_q(n;a,b)>0\ \Longleftrightarrow\ \operatorname{lcm}(A,B)=n.}
\]
If \(a,b\) are each nonzero modulo \(n\), the automaton itself is nonzero. Thus **a nonzero two-scale difference automaton can annihilate a primitive spatial configuration in one update if and only if \(n\) has at least two distinct prime divisors**; the statement concerns the existence of suitable strides \(a,b\), not every pair.

For coprime integers \(a,b\ge2\) with \(n=ab\) and \(p\nmid n\), let \(P_q(k)=\sum_{e\mid k}\mu(k/e)q^e\) be the number of primitive \(k\)-words. Then the count factors sharply:
\[
\boxed{C_q(ab;a,b)=\frac{P_q(a)P_q(b)}q.}
\]
For uniformly sampled primitive \(ab\)-words, the exact extinction probability is \(P_q(a)P_q(b)/(qP_q(ab))\). For instance, over \(\mathbb F_5\) on a six-cell ring with strides two and three, the nonzero update annihilates exactly \(480\) of the \(15480\) primitive inputs.

## Assumptions and scope

Configurations are *indexed* elements of \(\mathbb F_q^n\), not rotation orbits. The update is simultaneous, with periodic boundary conditions. The coprimality \(p\nmid n\) is essential for the simple semisimple formula and the stated criterion; the theorem does not cover lengths divisible by the field characteristic. Strides may exceed \(n\) and are interpreted modulo \(n\). Every count includes zero outputs only, not all outputs with newly created symmetry.

## Proof

**Kernel on a prescribed period space.** Let \(V_d=\{x:S^dx=x\}\) for each divisor \(d\mid n\); this is canonically the \(d\)-cell configuration space and is invariant under \(F_{a,b}\). Identifying it with \(R_d=\mathbb F_q[z]/(z^d-1)\), the update acts by multiplication by \(g(z)=(1-z^a)(1-z^b)\). Since \(p\nmid d\), the polynomial \(z^d-1\) has distinct roots. The rank-nullity identity for multiplication in \(R_d\) gives
\[
\dim_{\mathbb F_q}(V_d\cap\ker F_{a,b})
=\deg\gcd(z^d-1,g(z))
=\gcd(d,a)+\gcd(d,b)-\gcd(d,a,b).
\]
The last equality counts roots whose orders divide \(a\) or \(b\), using inclusion-exclusion. Thus the number of configurations of period *dividing* \(d\) which vanish after one update is exactly the corresponding power of \(q\).

**Primitive count.** The sets of configurations of period dividing each \(d\mid n\) form the standard divisor lattice: every configuration has a unique least spatial period. Applying Möbius inversion to the preceding exact kernel sizes proves the displayed formula for \(C_q\).

**Existence boundary.** Write \(A=\gcd(n,a)\), \(B=\gcd(n,b)\), and \(L=\operatorname{lcm}(A,B)\). Because \(p\nmid n\), the shift module has the cyclotomic direct-sum decomposition
\[
\mathbb F_q^n=\bigoplus_{d\mid n} W_d,\qquad W_d=\ker\Phi_d(S).
\]
Here \(\Phi_d\) is the ordinary cyclotomic polynomial reduced modulo characteristic \(p\); the factors remain pairwise coprime and \(\dim W_d=\varphi(d)>0\). Every nonzero vector of \(W_d\) has *exact* shift period \(d\). Moreover \(F_{a,b}\) vanishes on \(W_d\) precisely when \(d\mid A\) or \(d\mid B\), and is invertible on the other summands. Consequently
\[
\ker F_{a,b}=V_A+V_B\subseteq V_L.
\]
If \(L<n\), no vector in the kernel has primitive period \(n\). If \(L=n\) and \(A\ne B\), take nonzero vectors \(u\in W_A\) and \(v\in W_B\); their sum lies in the kernel and has shift period \(\operatorname{lcm}(A,B)=n\), because distinct cyclotomic summands cannot cancel. If \(A=B=n\), any nonzero \(u\in W_n\) works. This establishes both directions.

**Nontriviality and the arithmetic boundary.** If neither \(a\) nor \(b\) is divisible by \(n\), evaluation of \(g\) at a primitive \(n\)-th root of unity is nonzero, hence \(F_{a,b}\ne0\). If \(n\) is a prime power, \(A\) and \(B\) are ordered by divisibility; having \(\operatorname{lcm}(A,B)=n\) forces one of them to equal \(n\), making the corresponding factor zero. Conversely, if \(n\) has at least two distinct prime divisors, split its prime-power factors into two nonempty groups with products \(a,b\), so \(ab=n\), \(\gcd(a,b)=1\), and \(1<a,b<n\). Their least common multiple equals \(n\), and both factors of the automaton are nonzero. This proves the existence dichotomy.

**Factorization at coprime strides.** For \(n=ab\), \(\gcd(a,b)=1\), one has \(\ker F_{a,b}=V_a+V_b\) and \(V_a\cap V_b=V_1\), the space of constants with \(q\) elements. Therefore \((u,v)\mapsto u+v\) is exactly \(q\)-to-one from \(V_a\times V_b\) onto the kernel. As \(\gcd(a,b)=1\), the sum is primitive of period \(ab\) exactly when \(u\) has period \(a\) and \(v\) has period \(b\): any potential cancellation is confined to the constant component, which cannot change either nonconstant exact period. There are \(P_q(a)P_q(b)\) such pairs. Dividing by \(q\) proves the last boxed formula and the probability assertion.

## Verification

The standalone `check_two_scale.py` uses only the Python 3 standard library. It enumerates all configurations at selected semisimple ring lengths for characteristics \(2,3,5\), applies the two-stride local update explicitly, checks the primitive-period restriction and extinction, and compares every tested count against the divisor formula and its positive-count criterion. It also checks the coprime-stride factorization. Actual execution reported 58,939 explicitly inspected configurations, 110 full comparison instances, and no disagreements. The infinite theorem is the preceding algebraic proof; finite checking is only a reproducibility aid.

## Relationship to prior work

Banda, Caughman and Lehman (2026, §§4, 8) enumerate shift-symmetric configurations and prove that an equivariant update cannot *destroy* translation symmetry. Their general inclusion theorem does not count primitive configurations annihilated by this specified two-scale update, or determine exactly when it happens for a nonzero map. Ninagawa (2013) studies spatial period halving in binary single-scale Rule 60, principally on power-of-two rings. The present prime-to-characteristic, two-scale mechanism is different: the new symmetries may involve distinct primes dividing the spatial length. Barbè and von Haeseler (2001) study **temporal periods of fixed-site vertical orbits** for linear cellular automata, a different observable. Classical cyclic-module polynomial gcd methods, finite-field Fourier splitting and Möbius inversion are explicitly treated here as established tools, not new results.

## Limitations

This theorem does not describe the full distribution of nonzero outputs, repeated updates, nonlinear rules, or spatial lengths divisible by the characteristic. Its novelty is the combined sharp primitive-extinction census and arithmetic existence dichotomy, not the underlying standard polynomial-algebra lemmas. Historical priority is uncertain because a sufficiently general existing enumeration of spatial periods in linear cellular automata may imply this specialization; independent mathematical validation has not been performed.

## References

1. P. Banda, J. Caughman, T. Lehman, *Shift-Symmetric Configurations in d-Dimensional Cellular Automata: Enumeration, Bounds, Irreversibility, and Detection*, arXiv:2611.15751v1, first public 2026-11-11. https://arxiv.org/html/2611.15751v1
2. S. Ninagawa, *Solving the Parity Problem with Rule 60 in Array Size of the Power of Two*, arXiv:1307.3888, 2013. https://arxiv.org/abs/1307.3888
3. A. Barbè, F. von Haeseler, *Periodic Patterns in Orbits of Certain Linear Cellular Automata*, Discrete Mathematics and Theoretical Computer Science Proceedings AA, 79–94, 2001. https://www2.math.ethz.ch/EMIS/journals/DMTCS/pdfpapers/dmAA0105.pdf
4. R. Cordovil, R. Dilão, A. Noronha da Costa, *Periodic Orbits for Additive Cellular Automata*, Discrete & Computational Geometry 1 (1986), 277–288. https://doi.org/10.1007/BF02187700
