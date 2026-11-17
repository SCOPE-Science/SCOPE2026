# Scattered path-tensor Schur spectra and isolation of algebraic thresholds

## Finding

For each integer \(k\ge2\), let \(B_k\) be the \(k\times k\) zero–one matrix retaining precisely the main diagonal and the first upper diagonal. Write \(\|B\|_{\bullet}\) for the Schur-multiplier norm acting on bounded Hilbert-space operators, not a Schatten norm, and set
\[
\sigma_k=\|B_k\|_{\bullet}=\frac{2}{k+1}\cot\!\left(\frac{\pi}{2(k+1)}\right),\qquad c=\frac4\pi.
\]
Let \(\mathcal P\) be the set of all finite products of the \(\sigma_k\), including the empty product \(1\). Let \(\mathcal S\) consist of the norms of all finite or countable block-diagonal direct sums of finite Kronecker products of the \(B_k\), allowing a one-by-one identity block, and retaining only bounded Schur multipliers.

**Theorem.** The precise norm spectrum and all its finite Cantor–Bendixson derivatives are
\[
\boxed{\mathcal S=\overline{\mathcal P}=\bigcup_{m=0}^{\infty}c^m\mathcal P},\qquad
\boxed{\mathcal S^{(m)}=c^m\mathcal S=\bigcup_{j=m}^{\infty}c^j\mathcal P\quad(m\ge0)}.
\]
Here \(\mathcal S^{(0)}=\mathcal S\), the successor derivative consists of all real accumulation points, and \(\mathcal S^{(\omega)}=\bigcap_{m\ge0}\mathcal S^{(m)}=\varnothing\). Every point \(c^m p\), \(p\in\mathcal P\), has **exact rank** \(m\): it belongs to \(\mathcal S^{(m)}\setminus\mathcal S^{(m+1)}\). Consequently \(\mathcal S\) is a closed countable scattered set, and all its accumulation points are transcendental. In particular each algebraic real is either absent from \(\mathcal S\) or isolated in it. Thus there exists \(\varepsilon>0\) such that
\[
\boxed{\mathcal S\cap(2-\varepsilon,2+\varepsilon)\subseteq\{2\}}.
\]
The bound is existential, not an explicit numerical certificate. It applies **only** to the stated path-tensor/block-sum family, not to all idempotent Schur multipliers.

## Assumptions and scope

All matrices and operators are complex and equipped with the operator norm. A rectangular or square zero–one mask defines the idempotent Schur multiplier \(X\mapsto B\bullet X\) by entrywise multiplication. A countable block sum acts between the corresponding Hilbertian direct sums of row and column spaces. Its Schur norm must be finite. The theorem permits any finite number of path factors per block and arbitrary finite or countable block collections. It does not permit arbitrary graph constructions beyond tensor products and block sums, nor arbitrary non-path factors.

The set \(\mathcal P\) is a multiplicative semigroup with unit. The constant \(c=4/\pi\) exceeds \(1\). The natural order-zero derivative convention is explicitly stated above; it makes the first derived set \(\mathcal S'=\mathcal S^{(1)}\).

## Proof

**1. Inputs from established Schur theory.** Levene's 2014 Theorem 4.2 gives the displayed formula for the diagonal/superdiagonal path masks; its Corollary 4.6 gives \(\sigma_k\nearrow c=4/\pi\). The 2026 Lemma 5.1, recalling an observation attributed to Davidson, gives the exact tensor identity
\[
\|B\otimes C\|_{\bullet}=\|B\|_{\bullet}\|C\|_{\bullet}.
\]
For direct sums one has \(\|\bigoplus_i B_i\|_{\bullet}=\sup_i\|B_i\|_{\bullet}\): the output is block diagonal, so the upper bound follows by restricting the input to each diagonal corner; inputs supported in a single block give the reverse bound. Thus the finite tensor blocks have exactly the norms in \(\mathcal P\), and the countable bounded sums have exactly the finite suprema of one or more such numbers or the suprema of countable sequences of them.

**2. The single accumulation generator.** Put \(t_k=\pi/(2(k+1))\). Then \(\sigma_k=c\,t_k\cot(t_k)\). Since
\[
\frac{d}{dt}(t\cot t)=\frac{\sin t\cos t-t}{\sin^2t}<0\qquad (0<t<\pi/2),
\]
and \(t_k\) decreases, \(\sigma_k\) increases strictly to \(c\). In particular \(\sigma_2=2/\sqrt3>1\). The compact subset of the real line
\[
F=\{\sigma_k:k\ge2\}\cup\{c\}
\]
has exactly one accumulation point, namely \(c\), and each individual \(\sigma_k\) is isolated in \(F\).

**3. Exact closure.** Every product of \(r\) factors from \(F\) is at least \((2/\sqrt3)^r\). Hence, in any bounded interval \([1,R]\), the number \(r\) of factors in a product is uniformly bounded by \(\log R/\log(2/\sqrt3)\). Given a convergent sequence of finite products of factors from \(F\), first take a subsequence of a fixed factor count, then use compactness of \(F\) successively in each coordinate. Its limit is a product of finitely many elements of \(F\). This proves that the set of all finite \(F\)-products is closed. Conversely, each such product with \(m\) factors equal to \(c\) is a limit of products in \(\mathcal P\) obtained by replacing those factors with \(\sigma_k\) as \(k\to\infty\). Therefore
\[
\overline{\mathcal P}=\left\{\prod_{i=1}^r x_i:r\ge0,\ x_i\in F\right\}=\bigcup_{m\ge0}c^m\mathcal P.
\]
A bounded countable block sum has norm a finite supremum of elements of \(\mathcal P\), or a limit of finite running maxima, and therefore belongs to \(\overline{\mathcal P}\). Conversely, for any \(c^m p\) choose block norms \(p\sigma_k^m\) as \(k\to\infty\) (for \(m=0\), one finite block suffices); their countable block sum has norm exactly \(c^m p\). Hence \(\mathcal S=\overline{\mathcal P}\).

**4. Every derived set.** Write \(\mathcal S\) as the set of all finite products of elements of \(F\). If \(x\) is the limit of a sequence of distinct points of \(\mathcal S\), the factor-count argument bounds the number of factors, after discarding finitely many terms. Take a fixed-count subsequence and coordinatewise limits. If every limit factor were an isolated member \(\sigma_k\) of \(F\), the individual factor sequences would eventually be constant, forcing the product sequence to be eventually constant—a contradiction. Thus at least one limiting factor is \(c\), and \(x\in c\mathcal S\). Conversely, every element \(cp\in c\mathcal S\) is a limit of **distinct** elements \(\sigma_k p\in\mathcal S\); the values strictly increase to \(cp\). Therefore
\[
\mathcal S'=c\mathcal S.
\]
Positive scalar multiplication is a homeomorphism and commutes with taking the derived set. Induction yields \(\mathcal S^{(m)}=c^m\mathcal S\). Since \(\mathcal S\subseteq[1,\infty)\), the intersection of all these derived sets is empty: an element of \(c^m\mathcal S\) is at least \(c^m\to\infty\).

**5. Exact ranks and arithmetic separation.** Put \(\zeta_k=e^{\pi i/(k+1)}\), a root of unity. The identity \(\cot(\pi/(2(k+1)))=i(\zeta_k+1)/(\zeta_k-1)\) shows each positive \(\sigma_k\) is algebraic, hence so is each \(p\in\mathcal P\). Since \(\pi\) is transcendental, so is \(c=4/\pi\). For every integer \(m\ge1\) and positive algebraic \(p\), \(c^m p\) is transcendental, for otherwise \(c\) would be algebraic as a root of \(X^m-(c^m p)/p\). More generally, \(c^m p=c^n q\) with \(m\ne n\) and positive algebraic \(p,q\) would make a positive integer power of \(c\) algebraic, which is impossible. Hence each \(c^m p\) belongs to the \(m\)-th derivative but not the next one, and all points in the first derivative are transcendental. If the algebraic number \(2\) were a limit point of \(\mathcal S\), it would belong to \(\mathcal S'=c\mathcal S\), contradiction. The asserted punctured neighborhood exists by the definition of a limit point, independently of whether \(2\in\mathcal S\).

## Verification

The proof is exact and uses no finite enumeration as a completeness argument. The critical premises can be checked independently in Levene (2014), Theorem 4.2 and Corollary 4.6, and Levene (2026), Lemma 5.1. The only external arithmetic fact in the new deductions is the classical transcendence of \(\pi\). Direct numerical evaluation gives \(\sigma_5\sigma_9\sigma_{122}=2.000001319114155648\ldots\), a near-threshold member of \(\mathcal P\) already highlighted by Levene (2026), Section 6; the isolatedness theorem is qualitative and does not compute the distance from \(2\) to other points of \(\mathcal S\).

## Relationship to prior work

Levene (2014) proves the individual path norms and their limit; Levene (2026) states tensor multiplicativity, closure of the **full** Schur norm spectrum under bounded suprema, and exhibits the near-\(2\) triple product while asking whether \(2\) is approached **from above** in the full spectrum. These antecedents are not claimed as new. The present theorem classifies the precise, much smaller spectrum obtained by repeatedly applying those natural operations **only to the finite path masks**. It establishes its entire derived-set hierarchy, precise point ranks, and the impossibility of approaching the algebraic threshold \(2\) in that restricted family. Neither of the inspected papers gives this restricted-spectrum classification or asserts isolation of \(2\) for the path-generated family. This does **not** settle the open question for arbitrary Schur idempotents; other graph constructions may yield sequences approaching \(2\).

## Limitations

The gap around \(2\) is proved to exist but no effective value is supplied. The theorem is limited to bounded direct sums of finite tensor products of the specified path masks. It does not classify all zero–one Schur multiplier norms, and neither the full-spectrum closure question nor the existence of full-spectrum norms decreasing to \(2\) is addressed. The proof of novelty is limited by the accessible literature; an older abstract general product-derived-set theorem could give a different formulation of the same structural argument. No independent mathematical review has been performed.

## References

1. R. H. Levene, *Norms of idempotent Schur multipliers*, New York Journal of Mathematics **20** (2014), 325–352, especially Theorem 4.2, Corollary 4.6 and Remark 4.7. https://nyjm.albany.edu/j/2014/20-19p.pdf ; first preprint arXiv:1302.4849.
2. R. H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (first posted 2026-11-05), especially Lemma 5.1 and Questions 6.2–6.3. https://arxiv.org/html/2611.08419v1.
3. The classical Lindemann theorem implying the transcendence of \(\pi\).
