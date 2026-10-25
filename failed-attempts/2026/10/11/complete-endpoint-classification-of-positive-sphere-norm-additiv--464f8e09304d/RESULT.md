# Complete endpoint classification of positive-sphere norm-additive maps on \(C^1([0,1])\)
## Finding
Let \(I=[0,1]\) and \(S\) be the positive unit sphere of real \(C^1(I)\) under the norm \(\|f\|_{(1)}=|f(0)|+\|f'\|_{\infty}\). Set
\[
P=\{h\in C(I):h\ge0,\ \|h\|_{\infty}=1\},\qquad m(h)=\min_{s\in I}h(s).
\]
For each \(h\in P\) and \(a\in[0,m(h)]\), write
\[
f_{h,a}(t)=a+\int_0^t(h(s)-a)\,ds.
\]
**Complete classification.** A map \(T:S\to S\) is onto and satisfies
\[
\|Tf+Tg\|_{(1)}=\|f+g\|_{(1)}\qquad(f,g\in S)
\]
if and only if there are a homeomorphism \(\tau:I\to I\) and, independently for each \(h\in P\), a surjection \(\psi_h:[0,m(h)]\to[0,m(h)]\) for which
\[
(Tf_{h,a})(t)=\psi_h(a)+\int_0^t\bigl(h(\tau(s))-\psi_h(a)\bigr)\,ds,
\qquad h\in P,\quad a\in[0,m(h)],\quad t\in I.
\]
Both the homeomorphism and the complete indexed family of fiber maps are uniquely determined by \(T\). No continuity or injectivity is assumed for the fiber maps. In particular, \(T\) is injective, hence bijective, precisely when all \(\psi_h\) are injective.

## Assumptions and scope
The scalar field is real; derivatives are continuous on the closed interval and are nonnegative pointwise. The norm is exactly \(\|f\|_{(1)}=|f(0)|+\|f'\|_\infty\), not the maximum norm or any exponent above one. The unit sphere is restricted by \(f(0)\ge0\) and \(f'\ge0\). The condition is a two-variable preservation of the norm of sums, together with surjectivity of \(T\); no metric isometry, measurability, continuity, or linear extension is assumed for \(T\). Singleton fibers with \(m(h)=0\) are included.

## Proof
**Step 1: exact quotient and fibers.** Define \(H:S\to P\) by \(Hf=f(0)+f'\), where the initial value is viewed as a constant function. Since \(f(0)\ge0\), \(f'\ge0\) and \(f(0)+\|f'\|_\infty=1\), one has \(Hf\ge0\) and \(\|Hf\|_\infty=1\). Conversely, any \(h\in P\) is \(Hf_{h,0}\), so \(H\) is onto. If \(Hf=h\), the scalar \(a=f(0)\) must satisfy \(0\le a\le\min_I h\); then \(f'=h-a\) and integration forces \(f=f_{h,a}\). Conversely, every such \(f_{h,a}\) belongs to \(S\), because its initial value plus the maximum of its nonnegative derivative equals \(a+(1-a)=1\). Hence the displayed parametrization exhausts every fiber and contains no duplicates.

**Step 2: norm of positive sums.** For all \(f,g\in S\), nonnegativity gives the exact identity
\[
\|f+g\|_{(1)}=f(0)+g(0)+\|f'+g'\|_\infty=\|Hf+Hg\|_\infty.
\]
The equality is valid for all fibers, not only for affine functions.

**Step 3: positive-sum profiles separate the quotient.** If \(u,v\in P\) have equal values \(\|u+w\|_\infty=\|v+w\|_\infty\) for every \(w\in P\), then \(u=v\). Indeed, if \(u(s_0)<v(s_0)\), choose \(0<\varepsilon<v(s_0)-u(s_0)\), and a continuous bump \(w\in P\) with \(w(s_0)=1\), supported where \(u(s)<u(s_0)+\varepsilon\). Off that support, \(u\le1\); consequently \(\|u+w\|_\infty<u(s_0)+\varepsilon+1<v(s_0)+1\le\|v+w\|_\infty\), a contradiction. Compactness and continuity ensure strictness of the first inequality. This is the point-separation mechanism of Ezumi–Miura, Lemmas 2.3–2.4.

**Step 4: induced rigid homeomorphism.** Suppose \(T:S\to S\) is an onto norm-additive map. If \(Hf=Hg\), then Step 2 gives equal values \(\|f+k\|_{(1)}=\|g+k\|_{(1)}\) for every \(k\in S\). Their \(T\)-images therefore have equal positive-sum profiles against every \(H(Tk)\). Both \(T\) and \(H\) are surjective, so these tests exhaust \(P\). Step 3 forces \(H(Tf)=H(Tg)\). Thus a well-defined map \(\Phi:P\to P\) satisfies \(\Phi(Hf)=H(Tf)\); it is onto and, by Step 2, obeys
\[
\|\Phi(h)+\Phi(k)\|_\infty=\|h+k\|_\infty\qquad(h,k\in P).
\]
The published positive-sphere Banach–Stone theorem of Ezumi–Miura (Theorem 2.1), whose proof uses maximal-value sets and continuous peak functions and allows zeros of \(h\), therefore applies to \(\Phi\): there is a homeomorphism \(\tau:I\to I\) such that \(\Phi(h)=h\circ\tau\). Uniqueness of \(\tau\) follows because the functions in \(P\) separate points of \(I\).

**Step 5: free and surjective fiber actions.** For each \(h\in P\), \(T\) maps the fiber \(\{f_{h,a}:0\le a\le m(h)\}\) into that of \(h\circ\tau\). These fibers have the same endpoint since \(\min_I(h\circ\tau)=m(h)\). Define \(\psi_h(a)=(Tf_{h,a})(0)\). The fiber parametrization from Step 1 yields the claimed integral formula. Because \(T\) is onto and \(\Phi(h)=h\circ\tau\) is a bijection of \(P\), every target point in the fiber over \(h\circ\tau\) has a preimage *in the fiber over \(h\)*; hence \(\psi_h\) is onto. The formula determines both \(\tau\) and \(\psi_h\) uniquely.

**Step 6: converse.** Given any such \(\tau\) and onto family \(\psi_h\), the formula defines elements of \(S\): the new derivative \(h\circ\tau-\psi_h(a)\) is nonnegative and has supremum \(1-\psi_h(a)\). It also gives \(H(Tf_{h,a})=h\circ\tau\); Step 2 and the sup-norm invariance under homeomorphism imply the norm-additive identity. Given an arbitrary target \(f_{k,b}\), choose \(h=k\circ\tau^{-1}\), and choose \(a\in[0,m(h)]\) with \(\psi_h(a)=b\); then \(Tf_{h,a}=f_{k,b}\). Thus \(T\) is onto. Within each fiber \(T\) is injective exactly when \(\psi_h\) is injective, and distinct quotient fibers stay distinct because \(h\mapsto h\circ\tau\) is injective. The bijectivity criterion follows.

## Verification
All calculations are exact. The full fiber interval is verified using both nonnegativity of the derivative and the equality \(\max_I h=1\). The kernel separation uses an actual continuous peak bump and tests against the whole surjective quotient. The external nonstandard ingredient is Ezumi–Miura's Theorem 2.1; its statement and full primary proof (star sets, maximal-value set preservation, compactness, and point representation) were inspected. The converse checks the range and surjectivity explicitly. Boundary cases \(m(h)=0\) and \(h\equiv1\) are included: the former has one-element fibers and the latter has an entire unit interval fiber, on which noninjective surjections may be chosen. No numerical experiment, unproved density assertion, or unattained extremum is used.

## Relationship to prior work
Ezumi–Miura prove the rigid homeomorphism formula for \(1<p\le\infty\), prove the positive-sphere Banach–Stone theorem for \(C(K)\) as an auxiliary result, and exhibit one nonrigid affine-fiber counterexample at \(p=1\). Their paper does not formulate the unrestricted complete endpoint classification. The present result combines a specifically endpoint quotient/fiber identification with the auxiliary theorem, proving that arbitrary surjective endpoint maps have **only** composition-homeomorphism freedom on the quotient and independently unrestricted surjective interval maps within each fiber. Enami–Hirota–Koshimizu–Lin study surjective **isometries** on related positive spheres; isometry is a different, stronger property and their rigidity statement does not cover arbitrary norm-additive surjections. The earlier Chen–Dong–Zheng representation concerns positive continuous functions, not the complete endpoint \(C^1\)-sphere fiber structure.

## Limitations
The theorem classifies surjective norm-additive self-maps on this particular real positive sphere. It makes no assertion about nonsurjective norm-additive maps, general \(C^1\) Banach norms, higher-dimensional domains, arbitrary target spaces, or continuity of the fiber maps. The Banach–Stone theorem for the quotient is a previously proved ingredient, not a new independent theorem. The classification does not assert linear extension of all maps; in fact arbitrary fiber choices generally prevent it.

## References
1. K. Ezumi and T. Miura, *Norm-Additive Maps on the Positive Unit Sphere of \(C^1([0,1])\)*, arXiv:2610.02862v1 (2026), especially Theorems 1.1, 2.1, and Counterexample 6.1.
2. Y. Enami, D. Hirota, H. Koshimizu, and M.-R. Lin, *Surjective isometries on the positive parts of the unit spheres of some function spaces*, arXiv:2606.30952v1 (2026).
3. L. Chen, Y. Dong, and B. Zheng, *On norm-additive maps between the maximal groups of positive continuous functions*, Results in Mathematics 74 (2019), Article 152 (used only through the comparison described by Ezumi–Miura).
