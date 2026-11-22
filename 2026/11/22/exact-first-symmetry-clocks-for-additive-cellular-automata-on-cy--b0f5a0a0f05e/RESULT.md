# Exact first-symmetry clocks for additive cellular automata on cyclic rings

## Finding

A finite cyclic cellular automaton cannot destroy a spatial translation symmetry. The exact time at which a **new** spatial symmetry first arises, however, is a different observable. For the difference update, this first-passage law is both explicit at every ring length and universal after reversing the time to its sharp cutoff.

Let \(q=p^h\) be a prime power and \(n\ge2\). On \(\mathbb F_q^n\) with cyclic indices, let \(S\) be the shift \((Sx)_i=x_{i+1}\) and \(F=I-S\), so \((Fx)_i=x_i-x_{i+1}\). Let \(T(x)\) be the least \(t\ge0\) for which \(F^t x\) is fixed by some nonidentity power of \(S\); put \(T(x)=\infty\) if there is none. Write \(N_t=|\{x:T(x)=t\}|\).

Set
\[
B_q(n)=\sum_{d\mid n}\mu(n/d)q^d.
\]
This counts configurations with exact spatial period \(n\). Always \(N_0=q^n-B_q(n)\). If \(p\nmid n\), then \(N_\infty=B_q(n)\) and \(N_t=0\) for all finite \(t>0\).

If \(n=p^a m\), where \(a\ge1\) and \(p\nmid m\), define
\[
L=(p-1)p^{a-1},\qquad H_q(n,p)=\sum_{r\mid\operatorname{rad}(m)}\mu(r)q^{n/(pr)}.
\]
Then the entire first-symmetry time distribution is
\[
\boxed{N_t=(q-1)q^{t-1}H_q(n,p)\quad(1\le t\le L),}
\]
\[
\boxed{N_\infty=B_q(n)-(q^L-1)H_q(n,p),\quad N_t=0\ (t>L).}
\]
Every newly acquired nontrivial translation symmetry contains one of order \(p\); no prime-order translation of order \(\ell\ne p\) can first appear at positive time. Conditional on \(0<T<\infty\), the reversed onset lag has law
\[
\boxed{\Pr(L-T=j\mid 0<T<\infty)=\frac{(q-1)q^{-j-1}}{1-q^{-L}}\quad(0\le j<L).}
\]
It is independent of the prime-to-\(p\) factor \(m\). In particular, on rings with \(n=p^a\) every trajectory is eventually spatially symmetric, and the sharp last possible first-symmetry time is \(L\). The formulas remain valid with \(F=(I-S)u(S)\) for any shift-polynomial \(u(S)\) invertible on \(\mathbb F_q^n\).

## Assumptions and scope

The sample space is all \(q^n\) **indexed**, uniformly counted configurations, not rotation orbits. The coefficient field is any finite field of characteristic \(p\). The Möbius function is the arithmetic \(\mu\); \(\operatorname{rad}(m)\) is the product of distinct prime divisors of \(m\), with \(\operatorname{rad}(1)=1\). Symmetry means fixed by at least one translation \(S^d\) with \(1\le d<n\); thus aperiodic means minimal spatial period \(n\). An invertible shift-polynomial factor means that its representative is a unit modulo \(z^n-1\), or equivalently \(\gcd(u(z),z^n-1)=1\) after clearing any negative exponent.

## Proof

**1. Reduction to prime-order symmetries.** A nontrivial subgroup of the finite cyclic translation group has a prime-order subgroup. Thus a word is shift-symmetric iff it belongs to at least one space \(V_\ell=\operatorname{Fix}(S^{n/\ell})\), where \(\ell\) runs through prime divisors of \(n\). The number of initially asymmetric (exact-period-\(n\)) words is the Möbius inversion \(B_q(n)\), proving the expression for \(N_0\).

**2. Only the characteristic prime can create symmetry.** Identify the configuration module with \(R=\mathbb F_q[z]/(z^n-1)\), on which \(S\) acts as multiplication by \(z\). Write \(n=p^a m\), \(p\nmid m\). In characteristic \(p\),
\[
z^n-1=(z^m-1)^{p^a}=(z-1)^{p^a}Q(z),\qquad \gcd(z-1,Q)=1.
\]
Chinese remaindering splits \(R\) as the direct sum of the \((z-1)\)-primary factor and the \(Q\)-primary factor. The multiplier \(1-z\) is nilpotent on the first and invertible on the second. For any prime \(\ell\mid n\), \(\ell\ne p\), the polynomial \(z^{n/\ell}-1\) is divisible by \((z-1)^{p^a}\). Hence the whole nilpotent summand lies in \(V_\ell\). On the complementary summand \(F\) is an automorphism commuting with \(S\), so preimages and images under \(F\) preserve membership in the restricted fixed subspace. Therefore \(F^t x\in V_\ell\) iff \(x\in V_\ell\) for all \(t\ge0\). If \(p\nmid n\), this holds for every prime dividing \(n\), and no new symmetry is possible.

**3. Exact first appearance of order-\(p\) symmetry.** Suppose \(a\ge1\) and put \(U_t=\{x:F^t x\in V_p\}\). For a polynomial \(g\), the kernel of multiplication by \(g\) on \(R\) has \(\mathbb F_q\)-dimension \(\deg\gcd(g,z^n-1)\), by cancellation in the principal ideal \((z^n-1)\). Since \(V_p=\ker(z^{n/p}-1)(S)\),
\[
\dim U_t=\deg\gcd((1-z)^t(z^{n/p}-1),z^n-1)=\frac np+\min(t,L).
\]
Indeed \(z^{n/p}-1=(z^m-1)^{p^{a-1}}\), and adding \((1-z)^t\) increases only the multiplicity of root \(1\), by at most \(p^a-p^{a-1}=L\). Thus \(|U_t|=q^{n/p+\min(t,L)}\). For \(1\le t\le L\), the first-order-\(p\) shell \(U_t\setminus U_{t-1}\) has cardinality \((q-1)q^{n/p+t-1}\).

**4. Remove previously existing other-prime symmetries.** A point in this shell has overall \(T(x)=t\) precisely when it has no initial \(\ell\)-symmetry for any prime \(\ell\mid m\). Step 2 shows such other-prime symmetry cannot be created during the evolution. For each squarefree divisor \(r\mid m\), simultaneous invariance under all prime-order translations indexed by primes dividing \(r\) means that the initial word has spatial period dividing \(n/r\). Restricted to this invariant subspace, the update is exactly the same difference rule on a ring of length \(n/r=p^a(m/r)\); therefore its first order-\(p\) shell at time \(t\) has \((q-1)q^{n/(pr)+t-1}\) elements. Inclusion-exclusion over \(r\mid\operatorname{rad}(m)\) yields
\[
N_t=(q-1)q^{t-1}\sum_{r\mid\operatorname{rad}(m)}\mu(r)q^{n/(pr)}
\]
for \(1\le t\le L\). No first appearance occurs later. Subtracting the initial symmetric class and the positive finite shells from \(q^n\) gives the claimed \(N_\infty\). For \(m=1\), \(H=q^{n/p}\), \(q^L H=q^n\), and so \(N_\infty=0\).

**5. Universality and unit multipliers.** Summing finite positive shells gives \((q^L-1)H\). Dividing the shell at time \(L-j\) by this total produces the displayed reversed-geometric law. For an invertible shift-polynomial \(u(S)\), every \(V_\ell\) is invariant under \(u(S)\) and its inverse; hence \((I-S)^t u(S)^t x\in V_\ell\) exactly when \((I-S)^t x\in V_\ell\). All entry times, not merely their distribution, are unchanged. This completes the proof.

## Verification

The bundled `check_symmetry.py` is a self-contained Python 3 standard-library program. It independently enumerates all \(q^n\) indexed words, simulates the recurrence until a symmetry occurs or a state repeats, and compares complete first-passage histograms to an independently coded Möbius formula. It passed 26 exhaustive finite-field/ring cases with \(q\in\{2,3,4,9\}\), inspecting 30,852 configurations in total, including \(q=2,n=12\) and \(q=3,n=8\). For example \(q=2,n=6\) gives \(N_0=10\), \(N_1=6\), and \(N_\infty=48\), while \(q=2,n=8\) gives \(N_0=16\) and \((N_1,N_2,N_3,N_4)=(16,32,64,128)\). The finite census is not a substitute for the preceding all-length polynomial proof.

## Relationship to prior work

Banda, Caughman, and Lehman (2026, arXiv:2611.15751v1, sections 4 and 8) enumerate shift-symmetric configurations and prove that equivariant dynamics cannot destroy symmetry, with nondecreasing prime-symmetry ranks. They do not supply this first-passage distribution for a specified rule. Cordovil, Dilão, and Noronha da Costa (1986, Proposition 2.4 and Theorem 2.5) analyze spatial periods and the census of **temporally periodic** configurations of additive automata; their statements do not determine the first time of newly developing spatial symmetry. The present formula concerns that different first-passage observable, including its infinite-time mass and its universal reversed-clock statistics. Standard cyclic-module and Möbius tools are used, not claimed as new.

## Limitations

The classification is for \(F=(I-S)u(S)\) with \(u(S)\) invertible, over a finite field, on a single cyclic ring, under uniform initial counting. It does not address nonunit perturbations, two-dimensional grids, arbitrary linear rules, or nonuniform initial ensembles. The first-passage formula has a complete proof but not an independent expert audit. A mathematically equivalent theorem might exist in specialized historical additive-cellular-automata literature that was not indexed in the searches performed.

## References

1. P. Banda, J. Caughman, T. Lehman, *Shift-Symmetric Configurations in d-Dimensional Cellular Automata: Enumeration, Bounds, Irreversibility, and Detection*, arXiv:2611.15751v1, first posted 2026-11-11. https://arxiv.org/html/2611.15751v1
2. R. Cordovil, R. Dilão, A. Noronha da Costa, *Periodic Orbits for Additive Cellular Automata*, Discrete & Computational Geometry **1** (1986), 277–288. https://doi.org/10.1007/BF02187700
3. A. Castronuovo, A. Dennunzio, J. Kari, E. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746v1 (2026), contextual comparison. https://arxiv.org/html/2611.16746v1
