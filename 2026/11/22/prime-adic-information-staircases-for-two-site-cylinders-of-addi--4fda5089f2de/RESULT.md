# Prime-adic information staircases for two-site cylinders of additive cellular automata

## Finding

Fix a prime \(p\), integers \(r\ge 1\) and \(d\ge 1\), and the alphabet \(R=\mathbb Z/p^r\mathbb Z\). On the bilateral full shift \(X=R^{\mathbb Z}\), consider the additive cellular automaton
\[
(Fx)_i=x_i+x_{i+1}\pmod{p^r}.
\]
For \(u,v\in R\), let \(C_d(u,v)=\{x\in X:x_0=u,\ x_d=v\}\). Write \(a=\nu_p(d)\). For each integer \(t\ge1\), define
\[
e_{p,r,d}(t)=
\begin{cases}
r,&t=1,\\
\min\!\left(r,\max\!\left(0,a-\lfloor\log_p(t-1)\rfloor\right)\right),&t\ge2.
\end{cases}
\]
Then every \(F^t C_d(u,v)\) is an affine coset of a closed subgroup of \(X\) of **exact index** \(p^{e_{p,r,d}(t)}\). The cosets corresponding to pairs \((u,v)\) and \((u',v')\) coincide exactly when
\[
v-(-1)^d u\equiv v'-(-1)^d u'\pmod{p^{e_{p,r,d}(t)}};
\]
otherwise they are disjoint. In particular, **every two-site cylinder first has full image exactly at time \(p^{\nu_p(d)}+1\)**, independent of \(r\) and of the pinned values.

There is an explicit finite observation recovering the complete surviving congruence. Whenever \(e=e_{p,r,d}(t)>0\), necessarily \(t\le p^a\le d\). Divide \(z^d-(-1)^d\) by \((1+z)^t\) over \(\mathbb Z[z]\), and let \(Q_{d,t}(z)=\sum_{j=0}^{d-t}q_jz^j\) be the *integer quotient* (discarding the remainder). Then
\[
F^t C_d(u,v)=
\left\{y\in X:\sum_{j=0}^{d-t}q_j y_j\equiv v-(-1)^d u\pmod{p^e}\right\}.
\]
The last coefficient of \(Q_{d,t}\) is \(1\), so this equation really has index \(p^e\).

For independent uniform \(R\)-valued input coordinates \(X_i\), observe the whole output configuration \(Y=F^t X\). The exact Shannon mutual information (natural logarithms) is
\[
I\big((X_0,X_d);Y\big)=e_{p,r,d}(t)\log p.
\]
Thus a globally surjective and Haar-preserving cellular automaton has a **finite, prime-adically stratified memory** of each prescribed input pair. For example, if \(p=2\), \(r=3\), and \(d=8\), the image indices are \(8\) at times \(1,2\), \(4\) at times \(3,4\), \(2\) at times \(5,6,7,8\), and \(1\) from time \(9\) onward.

## Assumptions and scope

The space is the full *bilateral*, unrestricted shift, not a periodic spatial ring. All arithmetic in states and characters is modulo \(p^r\); valuations of positive integers are ordinary \(p\)-adic valuations. Time \(t\) is a positive integer. A cylinder specifies exactly two coordinates and leaves every other coordinate unrestricted. The Shannon statement assumes the product-uniform (Haar) input law and whole-configuration output observation, not a finite noisy observation. Index means cardinality of the compact-group quotient, not the number of individual output configurations.

## Proof

**1. Dual reduction to divisibility.** The map \(F\) is onto: for any target \(y\), choose \(x_0\) and extend the recurrence \(x_{i+1}=y_i-x_i\) in both directions. Every iterate is therefore onto. Finite-support characters of \(X\) are indexed by Laurent polynomials \(A(z)=\sum a_i z^i\in R[z,z^{-1}]\), via \(\chi_A(x)=\exp(2\pi i\sum a_ix_i/p^r)\). The dual action of \(F\) is multiplication by \(1+z\).

Let \(H_d=\{x:x_0=x_d=0\}\). A character \(\chi_Q\) annihilates \(F^tH_d\) exactly when \((1+z)^tQ\) has support contained in \(\{0,d\}\). Multiplication by \((1+z)^t\) is injective in \(R[z,z^{-1}]\), since both the lowest and highest nonzero coefficients of a product with the monic, constant-term-one polynomial cannot vanish. Any such supported polynomial is \(A(z)=b z^d+c\). Evaluation at \(z=-1\) gives \(c=-b(-1)^d\) whenever \(t\ge1\), so it is \(b(z^d-(-1)^d)\). Conversely this form lies in the dual range exactly when it is divisible by \((1+z)^t\) in \(R[z]\). Because \(1+z\) has a unit constant term and leading coefficient, passage to Laurent polynomials creates no additional such divisibilities: support endpoints force a quotient supported in \([0,d-t]\). Therefore the annihilator of \(F^tH_d\) is in bijection with the coefficients \(b\in R\) for which
\[
(1+z)^t\mid b(z^d-(-1)^d)\quad\text{in }R[z].
\]

**2. Exact prime-adic count.** Put \(w=z+1\). The identity
\[
z^d-(-1)^d=\sum_{j=1}^{d}(-1)^{d-j}\binom dj w^j
\]
shows that the divisibility in Step 1 holds exactly when \(p^r\mid b\binom dj\) for every \(1\le j<t\), with coefficients outside \(1\le j\le d\) understood as zero. If \(a=\nu_p(d)\), the following sharp valuation identity holds for every \(1\le j\le p^a\):
\[
\nu_p\!\binom dj=a-\nu_p(j).
\]
Indeed \(\binom dj=(d/j)\binom{d-1}{j-1}\), and Lucas' digit criterion shows that \(\binom{d-1}{j-1}\) is a \(p\)-adic unit: the lowest \(a\) base-\(p\) digits of \(d-1\) are all \(p-1\), while \(j-1<p^a\). In particular, the coefficient with \(j=p^a\) is a unit. Therefore the minimum valuation over \(1\le j<t\) is \(a-\lfloor\log_p(t-1)\rfloor\) when \(2\le t\le p^a\), and \(0\) when \(t>p^a\). At \(t=1\) there is no restriction on \(b\).

For any minimum valuation \(k\), the allowable coefficients \(b\) are precisely the multiples of \(p^{\max(0,r-k)}\) modulo \(p^r\), forming a cyclic group of order \(p^{\min(r,k)}\). This proves that the annihilator has order \(p^{e_{p,r,d}(t)}\). The compact-group character separation theorem identifies the same number with the index of \(F^tH_d\) in \(X\), proving the index and the sharp disappearance time.

**3. Explicit congruence and equality of cosets.** Let \(e>0\). Integer polynomial division gives
\[
z^d-(-1)^d=(1+z)^tQ_{d,t}(z)+R_{d,t}(z),\quad \deg R_{d,t}<t.
\]
In the \(w\)-basis the remainder contains only terms of degree below \(t\); by Step 2 all its coefficients are divisible by \(p^e\), and the same holds after changing back to \(z\). Pairing this identity with any input \(x\) therefore yields
\[
\sum_jq_j(F^t x)_j\equiv x_d-(-1)^d x_0\pmod{p^e}.
\]
The coefficient of \(z^{d-t}\) in \(Q_{d,t}\) is \(1\), so this observation map onto \(\mathbb Z/p^e\mathbb Z\) is surjective and each level set has index \(p^e\). The image \(F^t C_d(u,v)\) lies in the appropriate level set, and Step 2 says its index is exactly \(p^e\); hence the two sets coincide. This also gives the asserted equality/disjointness criterion. When \(e=0\), the annihilator is trivial, so the image is all of \(X\).

**4. Information identity.** The independent-uniform input law is Haar measure on \(X\). Since \(F^t\) is a surjective compact-group homomorphism, the output law is again Haar. Conditional on a given input pair, the output is Haar measure on the corresponding image coset, which has index \(p^e\). Its density relative to unconditional output Haar is exactly \(p^e\) on that coset and zero outside. Every conditional Kullback–Leibler divergence is therefore \(\log(p^e)\). Averaging over the pair gives \(I((X_0,X_d);Y)=e\log p\), as claimed.

## Verification

A standalone Python 3 program, `check.py`, uses integer polynomial long division (not the valuation formula) to enumerate the entire annihilator coefficient set in 2,457 parameter instances. It independently enumerates all finite-kernel initial conditions in 222 small cases and verifies 1,026 explicit decoder identities. It can be run with `python3 check.py` and requires only the standard library. The checks are finite diagnostics; the assertion for all primes, exponents, distances, and positive times follows from Steps 1–4.

## Relationship to prior work

Frobenius replication for prime-modulus linear lattice rules is a central theme of Nowak-Kępczyk, *Frobenius Revivals in Laplacian Cellular Automata* (arXiv:2511.17389, first public 2025-11-21), but there the emphasis is on finitely supported seeds, two-dimensional Laplacians, and prime-field dynamics, not prime-power pair-cylinder image indices. Castronuovo, Dennunzio, Kari and Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable* (arXiv:2611.16746, first public 2026-11-12), use group structure, Pontryagin duality and characteristic-polynomial methods for global entropy, rather than the two-pin prime-adic image and conditional-information profile computed here. Akın, Dikranjan, Giordano Bruno and Toller (arXiv:2306.10838, §§3–5) establish the Pontryagin-dual description of one-dimensional modular linear cellular automata and compute their global algebraic and topological entropy; their entropy formula depends on reduced support rather than the two-coordinate conditional-image index, and does not yield the time- and distance-resolved congruence or mutual-information staircase. General duality, Lucas' theorem and polynomial division are classical inputs, not claimed as novel. Binary finite-field mask-surjectivity laws cover the sharp loss time over characteristic two, but not the nonfield hierarchy of intermediate image indices nor its Shannon information interpretation.

## Limitations

The exact staircase uses the two-neighbor sum rule, two pinned input sites, and prime-power cyclic *ring* alphabets; it does not cover arbitrary linear rules, nonabelian alphabets, finite periodic rings, or noisy/finite-window decoding. It does not claim new global entropy computation, ergodicity, or a universal information law for other input distributions. Historical originality remains subject to comparison with additional older literature, especially general local-image results for modular linear cellular automata; full texts of all historical sources were not examined. Independent external mathematical validation has not been carried out.

## References

1. M. Nowak-Kępczyk, *Frobenius Revivals in Laplacian Cellular Automata: Replication, Entropy, and Information Recovery*, arXiv:2511.17389 (first posted 2025-11-21), https://arxiv.org/abs/2511.17389.
2. N. Castronuovo, A. Dennunzio, J. Kari and L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746 (first posted 2026-11-12), https://arxiv.org/abs/2611.16746.
3. T. B. Ward, *Additive cellular automata and volume growth*, Entropy 2 (2000), 142–167, https://doi.org/10.3390/e2030142.
4. E. Rowland and R. Yassawi, *A characterization of p-automatic sequences as columns of linear cellular automata*, Adv. Appl. Math. 63 (2015), 68–89, https://doi.org/10.1016/j.aam.2014.10.002.
5. H. Akın, D. Dikranjan, A. Giordano Bruno and D. Toller, *The algebraic entropy of one-dimensional finitary linear cellular automata*, Journal of Group Theory 27 (2024), 813–856, arXiv:2306.10838, https://arxiv.org/abs/2306.10838.
