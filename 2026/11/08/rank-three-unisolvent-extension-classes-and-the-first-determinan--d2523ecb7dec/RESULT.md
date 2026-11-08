# Rank-three unisolvent extension classes and the first determinantal splitting wall

## Finding
Let \(m\ge 2\), and work in the category \(\mathcal U_m\) of \(m\)-unisolvent coherent systems on a fixed complex \(\mathbb P^1\), with morphisms over the identity of the base. Set \(L_m=(\mathcal O(m-1),H^0(\mathcal O(m-1)))\) and \(H_{m,2}=(J^1\mathcal O(2m-1),j^1H^0(\mathcal O(2m-1)))\). Write \(L=L_m\), \(H=H_{m,2}\).

The two oriented extension spaces have dimensions
\[
\dim\operatorname{Ext}^1_{\mathcal U_m}(L,H)=2m(m-2),\qquad
\dim\operatorname{Ext}^1_{\mathcal U_m}(H,L)=2(m-2).
\]
Every nonsimple rank-three object of diagonal exponent five is either \(H\oplus L\), the middle term of a nonzero extension \(0\to H\to M\to L\to0\), or the middle term of a nonzero extension \(0\to L\to M\to H\to0\). For \(m\ge3\), these give precisely one split isomorphism class and two disjoint collections of nonsplit isomorphism classes parametrized, as sets, by
\[
\mathbb P^{\,2m(m-2)-1}\quad\text{and}\quad\mathbb P^{\,2(m-2)-1}.
\]
Every nonsplit middle term is indecomposable and has endomorphism ring \(\mathbb C\). For \(m=2\), the two extension spaces vanish, recovering the sole split class.

For \(m=4\), the second projective family is \(\mathbb P^3=\mathbb P\operatorname{Ext}^1(H,L)\). Via \(\operatorname{Ext}^1(H,L)\cong H^1(\mathcal O(-3))^{\oplus2}\cong\operatorname{Mat}_{2\times2}(\mathbb C)\), write \(A\) for the associated nonzero matrix. The underlying rank-three bundle \(E_A\) obeys the exact dichotomy
\[
E_A\cong
\begin{cases}
\mathcal O(5)^{\oplus3},&\det A\ne0,\\
\mathcal O(6)\oplus\mathcal O(5)\oplus\mathcal O(4),&\det A=0.
\end{cases}
\]
The jumping locus is therefore exactly the smooth Segre quadric \(\{\det A=0\}\cong\mathbb P^1\times\mathbb P^1\subset\mathbb P^3\). By contrast, every class of the first oriented \(m=4\) family has underlying bundle \(\mathcal O(6)^{\oplus2}\oplus\mathcal O(3)\).

## Assumptions and scope
An \(m\)-unisolvent coherent system \((E,W)\) is a vector bundle on \(\mathbb P^1_{\mathbb C}\) with \(W\subset H^0(E)\) such that \(W\to H^0(E|_D)\) is an isomorphism for every reduced divisor \(D\) consisting of \(m\) distinct points. Its rank is \(\operatorname{rk}E\), and its diagonal exponent is the integer \(e\) for which \(\deg E=e(m-1)\). The category is the extension-closed finite-length abelian category of Li–Li–Russo, Theorem 5.4. Their simple rank-one and rank-two objects are respectively \(L_m\), of exponent one, and \(H_{m,2}\), of exponent four. All extension groups and isomorphisms below are in this category, over the fixed parameterized base \(\mathbb P^1\). The two projective spaces classify isomorphism classes as sets; no claim of a fine coarse moduli scheme or quotient by base reparametrizations is made.

## Proof
**Step 1: Explicit underlying Hermite bundle.** The first jet bundle of \(\mathcal O(2m-1)\) is \(\mathcal O(2m-2)^{\oplus2}\): after homogenizing a binary form of degree \(2m-1\), its two partial derivatives are a homogeneous pair of degree \(2m-2\); their values determine its first jet since the degree is nonzero. This is a bundle isomorphism. Under it \(W_H\) is the image of the injective gradient map from \(H^0(\mathcal O(2m-1))\). Hence \(\dim W_L=m\), \(\dim W_H=2m\), and \(\dim(H^0(E_H)/W_H)=2(2m-1)-2m=2m-2\).

**Step 2: Extension dimensions.** Apply the exact coherent-system extension sequence (Li–Li–Russo, Proposition 5.7) to \((L,H)\). The two simple objects are nonisomorphic, hence \(\operatorname{Hom}_{\mathcal U_m}(L,H)=0\). Also \(\operatorname{Hom}(E_L,E_H)\) has dimension \(2m\), \(\operatorname{Hom}(W_L,H^0(E_H)/W_H)\) has dimension \(m(2m-2)\), and \(\operatorname{Ext}^1(E_L,E_H)=H^1(\mathcal O(m-1))^{\oplus2}=0\). Exactness yields \(\dim\operatorname{Ext}^1(L,H)=m(2m-2)-2m=2m(m-2)\).

For the reverse direction, \(H^0(E_L)/W_L=0\), \(H^1(E_L)=0\), and \(\operatorname{Ext}^1(E_H,E_L)=H^1(\mathcal O(1-m))^{\oplus2}\). Thus \(\operatorname{Ext}^1_{\mathcal U_m}(H,L)\cong H^1(\mathcal O(1-m))^{\oplus2}\), of dimension \(2\max(m-2,0)\), giving the stated formula for \(m\ge2\).

**Step 3: Exhaustion and separation of isomorphism classes.** By finite length, a nonsimple rank-three exponent-five object has a proper nonzero subobject. Since the only rank-one simple object has exponent one and the only rank-two simple object has exponent four, additivity of exponent and the rank-two classification force exactly the two distinct Jordan–Hölder factors \(L,H\). It therefore has one of the two indicated exact sequences (Li–Li–Russo, Corollary 5.6 and Propositions 5.8–5.9). Extension closure ensures that every Yoneda extension between these objects is again \(m\)-unisolvent. Since \(\operatorname{Hom}(H,L)=\operatorname{Hom}(L,H)=0\), any nonzero extension \(0\to S\to M\to T\to0\) of these distinct simples has a unique simple subobject: a second simple subobject isomorphic to \(T\) would project isomorphically to \(T\), splitting the sequence, and any different copy of \(S\) maps trivially to the quotient and must equal the original kernel. Consequently, an isomorphism between two such nonsplit middle terms preserves the exact-sequence filtration and induces scalar automorphisms on its endpoints. Thus two nonzero classes give isomorphic middle terms exactly when their extension classes are proportional. The endomorphism of a nonsplit middle term similarly has equal scalar actions on the two endpoints (otherwise it would kill the nonzero extension class), and there is no off-diagonal homomorphism; hence its endomorphism ring is \(\mathbb C\), and it is indecomposable. The orientation is intrinsic because the unique simple subobject is either \(L\) or \(H\), so the two projective collections are disjoint.

**Step 4: The determinantal jumping wall.** At \(m=4\), in the orientation \(0\to L\to M_A\to H\to0\), the bundle extension is
\[
0\to\mathcal O(3)\to E_A\to\mathcal O(6)^{\oplus2}\to0.
\]
By Step 2 its Yoneda class is exactly the vector-bundle class \(A\in H^1(\mathcal O(-3))^{\oplus2}\), hence a \(2\times2\) matrix after bases are chosen. Twist the sequence by \(\mathcal O(-6)\). The long exact cohomology sequence gives \(H^0(E_A(-6))\cong\ker(A:\mathbb C^2\to H^1(\mathcal O(-3)))\). Twisting by \(\mathcal O(-7)\) gives \(H^0(E_A(-7))=0\), since both end bundles have no global sections. In the Birkhoff–Grothendieck decomposition \(E_A=\bigoplus_{i=1}^3\mathcal O(a_i)\), the latter vanishing forces \(a_i\le6\), while \(h^0(E_A(-6))\) counts the number of \(a_i=6\). The degree is \(3+6+6=15\). If \(\operatorname{rank}A=2\), there are no degree-six summands, so all \(a_i\le5\) and their sum fifteen forces \((5,5,5)\). If \(\operatorname{rank}A=1\), exactly one \(a_i=6\); the other two sum nine and are at most five, forcing \((5,4)\). Thus the two splitting types follow. The projectivized nonzero rank-one matrices form the smooth degree-two Segre surface, proving the wall is exactly one quadric. For the other orientation, \(\operatorname{Ext}^1(E_L,E_H)=0\), so the underlying bundle extension splits regardless of its coherent-system class.

## Verification
The accompanying `verify_extension_geometry.py` uses rational row reduction on the explicit polynomial-gradient comparison map to verify the two extension-dimension formulas for integers \(2\le m\le10\). It checks that the projective determinant-zero locus of \(2\times2\) matrices has exactly \((q+1)^2\) rational points over the prime fields of orders \(q=2,3,5,7\), as a check on the Segre-quadric identification. Output ends in `VERIFY_OK` and `QUADRIC_VERIFY_OK`. These computations are finite consistency checks; the proof for every integer \(m\ge2\), uniqueness of extensions, and the global splitting dichotomy are deductive arguments above.

## Relationship to prior work
Li, Li and Russo (arXiv:2610.38184v1, Sections 5.1–5.4) prove extension-closedness, identify the simple factors, supply the general extension sequence, and prove the exponent-five splitting statement for \(m=2\). These published ingredients are expressly **not** claimed as new. The present calculation supplies the extension dimensions for all \(m\), classifies the nonsplit middle terms up to isomorphism over the fixed base, and identifies a determinantal vector-bundle jumping divisor for \(m=4\). The inspected source section does not state those results. The coherent-systems literature offers general extension machinery and may contain further implicit consequences; historical priority is therefore provisional. Results about arbitrary unparameterized Grassmannian curves are not inferred from these fixed-base classes.

## Limitations
This describes the **nonsimple** rank-three exponent-five systems only, not simple rank-three systems or other exponents. The projective parameter spaces classify objects set-theoretically over a fixed \(\mathbb P^1\), not scheme structures of their full moduli stacks and not orbits under \(\operatorname{PGL}_2\) on the base. The bundle-splitting stratification is determined completely only for \(m=4\); for general \(m\) only extension dimensions and isomorphism classes are asserted. Source inspection cannot prove historical uniqueness. No independent mathematical audit has been performed.

## References
1. Duo Li, Yanjie Li, Francesco Russo, *Geometry of m-direct-sum morphisms*, arXiv:2610.38184v1 (first submitted 2026-10-28), Sections 3 and 5, especially Theorem 5.4 and Propositions 5.7–5.10; https://arxiv.org/html/2610.38184v1.
2. P. E. Newstead and M. Teixidor i Bigas, *Coherent systems on the projective line*, arXiv:2001.07114 (related general moduli context; abstract inspected).
3. J. Jelisiejew and A. Keneshlou, *On construction of k-regular maps to Grassmannians via algebras of socle dimension two*, arXiv:2112.14106 (related critical Grassmannian regularity context; abstract inspected).
