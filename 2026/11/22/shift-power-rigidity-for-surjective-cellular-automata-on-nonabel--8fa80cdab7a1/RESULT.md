# Shift-power rigidity for surjective cellular automata on nonabelian groups of order \(p^3\)

## Finding

**Theorem.** Let \(p\) be a prime and let \(G\) be any nonabelian group of order \(p^3\). Put \(X=G^{\mathbb Z}\), with pointwise multiplication and the left shift \((\sigma x)_i=x_{i+1}\). Let \(F:X\to X\) be continuous, commute with \(\sigma\), and be a homomorphism of groups. Then the following three conditions are equivalent:

1. \(F\) is surjective;
2. \(F\) is bijective;
3. For a finite set of distinct offsets \(S\subset\mathbb Z\), its local homomorphism can be written, with a **unique** offset \(k\in S\), as
   \[
   F(x)_i=\alpha(x_{i+k})\prod_{j\in S\setminus\{k\}}c_j(x_{i+j}),
   \]
   where \(\alpha\in\operatorname{Aut}(G)\) and each \(c_j:G\to Z(G)\) is a group homomorphism. The central factors commute, so their order is immaterial.

Here an unused offset can be assigned the trivial homomorphism; the unique offset \(k\) does not depend on that choice. Write \(t=\operatorname{ord}(\alpha)\). **Every such surjective map obeys the exact map identity**
\[
\boxed{F^{pt}=\sigma^{kpt}.}
\]
It follows that
\[
\boxed{h_{\mathrm{top}}(F)=|k|\log|G|=3|k|\log p.}
\]
If \(k=0\), all points have period dividing \(pt\) and \(F\) is equicontinuous. If \(k\ne0\), the homeomorphism \(F\) is topologically mixing. For any prescribed \(r\ge1\) distinct input offsets, the number of surjective group-homomorphism local rules is exactly
\[
\boxed{r\,|\operatorname{Aut}(G)|\,p^{2(r-1)}.}
\]
The exponent factor \(p\) in the shift-power bound is necessary even when \(\alpha\) is the identity: there are central shears of exact order \(p\).

## Assumptions and scope

The alphabet is a finite **nonabelian** group of order \(p^3\). The global map is simultaneously a shift-commuting cellular automaton and a homomorphism for coordinatewise group multiplication. No assumption of a finite spatial ring, particular generating set, or predetermined neighborhood is made. The shift exponent \(k\) may be positive, negative or zero. The theorem does not address arbitrary nonlinear cellular automata or abelian alphabet groups of order \(p^3\).

Every such \(G\) has center \(Z=Z(G)\) and commutator subgroup \([G,G]\) both of order \(p\), and these subgroups coincide. Indeed, a finite \(p\)-group has nontrivial center. If \(|Z|\ge p^2\), then \(G/Z\) is cyclic, which forces \(G\) to be abelian, contrary to assumption. Thus \(|Z|=p\), the quotient \(G/Z\) has order \(p^2\) and cannot be cyclic, so is \((C_p)^2\). The quotient is abelian, hence \([G,G]\subseteq Z\); noncommutativity makes the commutator nontrivial, proving \([G,G]=Z\). Every proper subgroup has order at most \(p^2\) and is therefore abelian.

## Proof

**1. Decomposition of the local rule.** By the cellular-automaton characterization, there is a finite neighborhood \(S\) and a map \(f:G^S\to G\) with \(F(x)_i=f((x_{i+j})_{j\in S})\). Since the global \(F\) is a group homomorphism, so is \(f\). Restricting \(f\) to the individual direct-product factors gives group endomorphisms \(h_j:G\to G\). Distinct factors of \(G^S\) commute, so their images \(h_j(G)\) commute elementwise. Moreover
\[
f((g_j)_{j\in S})=\prod_{j\in S}h_j(g_j).
\]
If \(F\) is surjective, its local map \(f\) is surjective: every constant output configuration must have a preimage, and evaluation at any site attains every group element.

Suppose none of the \(h_j\) is surjective. Every image \(h_j(G)\) is then a proper, hence abelian, subgroup. Because different images commute elementwise, the group \(\prod_j h_j(G)=f(G^S)\) is abelian and cannot equal the nonabelian group \(G\). Therefore, some \(h_k\) is surjective and hence, by finiteness, an automorphism \(\alpha\). For each other \(j\), the image \(h_j(G)\) centralizes \(h_k(G)=G\), so lies in \(Z\). Put \(c_j=h_j\). Two distinct surjective coordinate homomorphisms would have mutually commuting images \(G\), which is impossible; hence \(k\) is unique. Conversely, a local rule of the displayed form is indeed a homomorphism because the additional factors are central. Since \([G,G]=Z\), every central-valued homomorphism kills \(Z\), and factors through \(G/Z\).

**2. An explicit inverse.** Put \(\bar G=G/Z\), with projection \(\pi:G\to\bar G\). Modulo \(Z\), the formula reads
\[
\pi(F(x)_i)=\bar\alpha(\pi(x_{i+k})),
\]
where \(\bar\alpha\) is an automorphism of \(\bar G\). Given an output \(y\), the quotient coordinates of its unique possible preimage are thus known:
\[
\pi(x_i)=\bar\alpha^{-1}(\pi(y_{i-k})).
\]
Each \(c_j(x_{i+j})\) depends only on this already-recovered quotient coordinate. Consequently
\[
x_{i+k}=\alpha^{-1}\!\left(y_i\left(\prod_{j\ne k}c_j(x_{i+j})\right)^{-1}\right)
\]
defines a unique preimage coordinate. Its quotient is precisely the recovered quotient, so the expressions are consistent at all sites. The inverse is a finite-radius continuous map. Thus the local normal form is sufficient for bijectivity. Conversely, bijectivity implies surjectivity.

**3. Uniform finite shift-power.** Shift \(F\) back by its unique dominant offset and write \(H=\sigma^{-k}F\). Since shifts commute with group cellular automata, \(F=\sigma^kH\) and \(F^n=\sigma^{kn}H^n\). The centered map \(H\) has the form
\[
H(x)_i=\alpha(x_i)d_i(\pi x),
\]
where each \(d_i\) is a \(Z\)-valued function of finitely many quotient coordinates; write \(\pi x\) for the full quotient configuration. Therefore
\[
\pi(H(x)_i)=\bar\alpha(\pi x_i),\qquad
H(xz)_i=H(x)_i\alpha(z_i)
\]
for any central configuration \(z\in Z^{\mathbb Z}\). Iterating the second identity gives
\[
H^n(xz)_i=H^n(x)_i\alpha^n(z_i).
\]
Set \(t=\operatorname{ord}(\alpha)\). The first identity implies \(\pi(H^t x)=\pi x\), while the second implies \(H^t(xz)=H^t(x)z\). Hence there is a well-defined function \(D_i:\bar G^{\mathbb Z}\to Z\), depending only on the quotient configuration, such that
\[
H^t(x)_i=x_iD_i(\pi x).
\]
Because applying \(H^t\) does not change \(\pi x\), induction yields \(H^{tm}(x)_i=x_i D_i(\pi x)^m\) for every positive integer \(m\). The group \(Z\) has order \(p\), so \(D_i^p=e\) for every \(i\). Consequently \(H^{pt}=\operatorname{id}_X\) and thus \(F^{pt}=\sigma^{kpt}\) as asserted. This is an identity for all bi-infinite configurations, not only periodic points or finite samples.

**4. Entropy and dynamics.** Entropy satisfies \(h_{\mathrm{top}}(F^n)=nh_{\mathrm{top}}(F)\) for continuous maps on a compact metric space; a shift by \(q\) sites on \(G^{\mathbb Z}\) has entropy \(|q|\log|G|\). Comparing the two sides of the shift-power identity gives \(h_{\mathrm{top}}(F)=|k|\log|G|\). For \(k=0\), \(F^{pt}=\operatorname{id}\) makes every point periodic with period dividing \(pt\), and the finite family of iterates makes the system equicontinuous. For \(k\ne0\), the positive power \(F^{pt}=\sigma^{kpt}\) is a nonzero shift and is mixing. Since \(F\) is onto, mixing of a positive power implies mixing of \(F\): for each of the finitely many exponent residues, pull back the second open set along that residue iterate and use mixing of the power.

**5. Exact local-rule census and sharpness of the central factor.** The abelianization \(G/[G,G]\cong(C_p)^2\) and \(Z\cong C_p\) give exactly \(p^2\) homomorphisms \(c:G\to Z\). For \(r\) named offsets choose \(k\) in \(r\) ways, \(\alpha\) in \(|\operatorname{Aut}(G)|\) ways, and one of \(p^2\) central maps at each remaining site. Uniqueness of \(k\) ensures no double counting. For sharpness take any nontrivial homomorphism \(c:G\to Z\), and define \(H(x)_i=x_i c(x_{i+1})\). It is a group cellular automaton, and \(\pi(Hx)=\pi x\). Thus \(H^n(x)_i=x_i c(x_{i+1})^n\). Its order is precisely \(p\), since some \(c(g)\) is a nonidentity element of \(Z\). This construction works for every permitted prime and group.

## Verification

The proof is self-contained except for standard finite-group facts (subgroups of order \(p^2\) are abelian; finite \(p\)-groups have nontrivial center) and the standard entropy-of-iterates identity. The supplied `verify.py` independently constructs the groups \(D_4\), \(Q_8\), the order-27 Heisenberg group and an order-27 modular group. It enumerates their endomorphisms by generator assignments, checks the center and commutator identities, tests the necessary abelianity of proper images and the central-factor property, independently counts surjective two-site homomorphism rules (respectively 64, 192, 7776 and 972), and evaluates \(F^{p\operatorname{ord}(\alpha)}=\sigma^{kp\operatorname{ord}(\alpha)}\) on randomized cyclic configurations. The finite checks corroborate but do **not** replace the general proof above. Reproduce with `python verify.py` using Python 3 without third-party dependencies.

## Relationship to prior work

Dennunzio, Formenti and Margara (2024) characterize several dynamical properties for specific nonabelian alphabets, including \(Q_8\), and establish that a local automorphism coordinate gives a bijective group cellular automaton. Existing analyses of \(Q_8\) give finer finite-order information for that one alphabet. The result here is **not** a new quaternion-only classification: it applies simultaneously to both nonabelian groups of order eight and, for every odd prime, to both nonabelian groups of order \(p^3\); its uniform identity \(F^{p\operatorname{ord}(\alpha)}=\sigma^{kp\operatorname{ord}(\alpha)}\) and all-prime rule census are its central assertions. Castronuovo, Dennunzio and Margara (2025) decompose general group cellular automata into simpler algebraic factors and derive a pure-shift power for appropriate products of nonabelian *simple* groups. Castronuovo, Dennunzio, Kari and Margara (2026) prove effective entropy computation for every finite-group alphabet and include the simple-group result, but their general algorithm does not state the above class-two \(p\)-group finite-power classification. The present explicit entropy formula is consistent with that broader computability theorem. Béaur and Kari (2024) establish general decision-theoretic properties of group cellular automata, not this uniform identity for all nonabelian groups of order \(p^3\).

## Limitations

The theorem is restricted to pointwise group-endomorphism cellular automata and nonabelian groups of exact order \(p^3\); it does not classify non-surjective maps, larger nonabelian \(p\)-groups or arbitrary cellular automata. The exponent \(p\operatorname{ord}(\alpha)\) is a valid uniform bound, not a minimal power for every map, though the factor \(p\) can be necessary when \(\alpha\) is the identity. This proof and its checks do not constitute independent external certification or exhaustive historical-priority determination.

## References

1. N. Castronuovo, A. Dennunzio, J. Kari and L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746v1 (first public 2026-11-12). https://arxiv.org/abs/2611.16746
2. N. Castronuovo, A. Dennunzio and L. Margara, *A Divide and Conquer Algorithm for Deciding Group Cellular Automata Dynamics*, arXiv:2507.09761v1 (2025-07-13). https://arxiv.org/abs/2507.09761
3. A. Dennunzio, E. Formenti and L. Margara, *On the Dynamical Behavior of Cellular Automata on Finite Groups*, IEEE Access 12 (2024), 122061–122077, DOI:10.1109/ACCESS.2024.3452199. https://doi.org/10.1109/ACCESS.2024.3452199
4. P. Béaur and J. Kari, *Effective Projections on Group Shifts to Decide Properties of Group Cellular Automata*, International Journal of Foundations of Computer Science 35 (2024), 77–100. https://arxiv.org/abs/2301.11133
