# Asymptotic rigid-simple orbit law for finite-field evolution algebras

## Finding

Fix a prime power \(q\ge3\). Let \(N_{n,q}\) be the number of isomorphism classes of **simple** \(n\)-dimensional evolution algebras over \(\mathbb F_q\). Put
\[
C_q=\prod_{j=1}^{\infty}(1-q^{-j})>0.
\]
Then, as \(n\to\infty\) with \(q\) fixed,
\[
\boxed{N_{n,q}\sim C_q\,\frac{q^{n^2}}{(q-1)^n n!}.}
\]
Moreover, among uniformly sampled *labeled* matrices defining simple evolution algebras, the proportion whose automorphism group is trivial tends to \(1\). Both assertions have explicit finite-dimensional error bounds given below. The conclusions concern simple algebras, not the entire collection of non-perfect evolution algebras.

## Assumptions and scope

For any \(n\ge2\), an evolution algebra \(E_M\) associated to a matrix \(M=(m_{ij})\in M_n(\mathbb F_q)\) has natural basis \(e_1,\ldots,e_n\), products \(e_i e_j=0\) for \(i\ne j\), and \(e_i^2=\sum_jm_{ij}e_j\). Its support digraph has an edge \(i\to j\) precisely when \(m_{ij}\ne0\), including loops. An algebra is simple precisely when \(M\) is invertible and its support digraph is strongly connected (established evolution-algebra structure theory).

Let \(\mathcal S_{n,q}\subset M_n(\mathbb F_q)\) be the set of simple defining matrices and \(H_{n,q}=(\mathbb F_q^\times)^n\rtimes S_n\) the monomial change-of-natural-basis group of order \(h_{n,q}=(q-1)^n n!\). The symbol \(N_{n,q}\) counts orbits of this group on \(\mathcal S_{n,q}\), not the labeled matrices themselves. The asymptotics fix \(q\), with no claim of uniformity when \(q\) grows with \(n\).

Here is an explicit estimate. Define
\[
 c_{n,q}=\prod_{j=1}^n(1-q^{-j}),\quad
 x=nq^{-n/2},\quad z=nq^{-3n/4},
\]
\[
 B_{n,q}=\frac{2x}{1-x},\qquad
 R_{n,q}=\left(\frac{q-1}{q}\right)^n+(q-1)^n\left(\frac{z^2}{1-z}+n^{n+1}q^{-n^2/4}\right).
\]
For every \(n\ge2\) with \(x<1\) and \(z<1\),
\[
 \left|\frac{N_{n,q}h_{n,q}}{q^{n^2}}-C_q\right|
 \le B_{n,q}+R_{n,q}+\frac{q^{-n}}{q-1}.
\]
Also, if \(c_{n,q}>B_{n,q}\),
\[
 \Pr\bigl(\operatorname{Aut}(E_M)\ne1\mid M\in\mathcal S_{n,q}\bigr)
 \le \frac{R_{n,q}}{c_{n,q}-B_{n,q}}.
\]
For each fixed \(q\), \(B_{n,q}\to0\), \(R_{n,q}\to0\), and \(c_{n,q}\to C_q\).

## Proof

**1. Labeled simple matrices.** Choose each entry independently and uniformly from \(\mathbb F_q\). The fraction of invertible matrices is exactly \(c_{n,q}\). If the support digraph is not strongly connected, some nonempty proper vertex set \(S\) has no outgoing edge to its complement. For \(|S|=s\), that event has probability \(q^{-s(n-s)}\). A union bound therefore gives
\[
 0\le c_{n,q}-\frac{|\mathcal S_{n,q}|}{q^{n^2}}
 \le\sum_{s=1}^{n-1}\binom ns q^{-s(n-s)}
 \le 2\sum_{s=1}^{\lfloor n/2\rfloor}(nq^{-n/2})^s
 \le B_{n,q}.
\]
The first inequality makes no assumption that matrix invertibility and graph connectivity are independent. The second uses \(\binom ns\le n^s\) and \(s(n-s)\ge sn/2\) for \(s\le n/2\).

**2. Monomial stabilizers are all automorphisms on the simple locus.** For \(\sigma\in S_n\) and \(t=(t_1,\ldots,t_n)\in(\mathbb F_q^\times)^n\), the natural-basis replacement \(f_i=t_i e_{\sigma(i)}\) changes the matrix to
\[
 m'_{ij}=\frac{t_i^2}{t_j}m_{\sigma(i),\sigma(j)}.
\]
Since a simple algebra is perfect, every one of its natural bases differs from another by such a monomial replacement. Hence two simple matrices describe isomorphic algebras if and only if they lie in one \(H_{n,q}\)-orbit, and the stabilizer of a simple matrix is its full algebra automorphism group.

**3. Diagonal stabilizers.** Suppose \(\sigma=1\), the graph is strongly connected, and a nonidentity vector \(t\) stabilizes \(M\). For every edge \(i\to j\), the fixed equation gives \(t_j=t_i^2\). A loop at any vertex forces its scalar to equal \(1\). Strong connectivity then propagates this equality along directed paths to every vertex, contradicting \(t\ne(1,\ldots,1)\). Thus a simple matrix with a nonidentity diagonal stabilizer must have **all** \(n\) diagonal entries zero. For each of the fewer than \((q-1)^n\) nonidentity diagonal elements, the fixed-simple probability in the full matrix space is at most \(q^{-n}\). Their total contribution to the normalized Burnside sum, and to the probability of a nontrivial stabilizer, is at most \(((q-1)/q)^n\).

**4. Stabilizers moving vertices.** Fix \(\sigma\ne1\) moving exactly \(s\ge2\) vertices, and arbitrary \(t\). Invariance under its action imposes linear equations in the \(n^2\) entries of \(M\). Each orbit of the permutation \((i,j)\mapsto(\sigma(i),\sigma(j))\) can carry at most one freely chosen entry: the monomial weights may force the whole orbit to zero, but cannot add degrees of freedom. There are \((n-s)^2\) fixed ordered pairs; all other coordinate orbits have size at least two. Consequently the fixed linear space has dimension at most
\[
 (n-s)^2+\frac{n^2-(n-s)^2}{2}
 =n^2-ns+\frac{s^2}{2}.
\]
In particular, the probability that uniform \(M\) is fixed by this specific monomial transformation is at most \(q^{-ns+s^2/2}\), without assuming \(M\) invertible.

There are at most \(n^s\) permutations moving exactly \(s\) vertices, and at most \((q-1)^n\) monomial weight vectors per permutation. For \(2\le s\le n/2\), \(ns-s^2/2\ge3ns/4\), so the normalized total fixed-point contribution is at most
\[
 (q-1)^n\sum_{s=2}^{\lfloor n/2\rfloor}(nq^{-3n/4})^s
 \le (q-1)^n\frac{z^2}{1-z}.
\]
For \(s>n/2\), the codimension is at least \(n^2/4\), yielding at most \((q-1)^n n^{n+1}q^{-n^2/4}\). Adding the diagonal bound from step 3 proves that the normalized sum of fixed-simple matrices over all nonidentity \(H_{n,q}\)-elements is at most \(R_{n,q}\).

**5. Burnside and generic rigidity.** Burnside's lemma gives
\[
 N_{n,q}=\frac{1}{h_{n,q}}\sum_{g\in H_{n,q}}
 |\{M\in\mathcal S_{n,q}:gM=M\}|.
\]
The identity term is \(|\mathcal S_{n,q}|/h_{n,q}\); steps 3–4 bound the other terms by \(q^{n^2}R_{n,q}/h_{n,q}\). Also
\[
 0\le c_{n,q}-C_q\le\sum_{j=n+1}^{\infty}q^{-j}=\frac{q^{-n}}{q-1}.
\]
Combining the bounds proves the finite-\(n\) estimate. A union bound over nonidentity stabilizers proves the conditional rigidity estimate. Finally, \((q-1)/q<1\), \((q-1)/q^{3/2}<1\), and for fixed \(q\) the factor \(q^{-n^2/4}\) dominates \(n^{n+1}(q-1)^n\). Therefore \(R_{n,q}\to0\), proving the asymptotic law.

## Verification

The self-contained checker `verify_random_simple.py` exhausts the full finite matrix spaces for the prime-field pairs \((p,n)=(2,2),(2,3),(3,2),(3,3),(5,2)\). For each simple matrix it independently performs modular Gaussian elimination, directed reachability, monomial transformations, orbit-stabilizer calculations, and the Burnside sum. It checks that every orbit remains simple, that disjoint orbits partition the simple matrices, and that both ways of counting classes coincide. Its recorded output appears in `verification_output.txt` and ends with `VERIFY_OK exact_orbit_and_burnside_agreement=yes`.

These finite calculations do not establish the infinite asymptotic. The proof above supplies the unrestricted argument for every fixed prime power \(q\ge3\); the small characteristic-two tests are additional consistency checks only.

## Relationship to prior work

The monomial natural-basis theorem, simple/perfect/strong-connectivity criterion, and finite-field Burnside enumeration framework are established results, not new. Wei and Zou (2023) give a general exact Burnside formula for *perfect* evolution algebras and low-dimensional explicit formulas; their paper does not state the present fixed-field asymptotic for **simple** isomorphism classes. Kaygorodov, Martín González, and Viruel (2026) explicitly raise the random-algebra and isomorphism-class asymptotic questions, including the fixed-field setting. Prior finite-binary-field research already gives sharper symmetry asymptotics for perfect algebras when \(q=2\), and prior work establishes the labeled simplicity probability limit for all finite fields. This theorem's new contribution is therefore **the all-fixed-field \(q\ge3\) simple-isomorphism-class asymptotic and accompanying generic monomial rigidity**, not the underlying Burnside formula or labeled simplicity limit.

## Limitations

No assertion is made about the asymptotic number of isomorphism classes of *all* non-perfect evolution algebras. The conditional automorphism statement concerns simple labeled algebras, not an unconditional uniformly random algebra and not uniformly chosen isomorphism classes. The bounds apply as \(n\to\infty\) with \(q\) fixed; no optimized rate or sparse-graph threshold is claimed. The research-priority assessment remains conditional on accessible literature; independent mathematical audit has not been performed.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first submitted 2026-10-15), especially Questions 21–22 and Theorems 4 and 6. https://arxiv.org/abs/2610.22248
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023), especially Theorem 1.1 and Sections 2–3. https://arxiv.org/abs/2310.12368
3. C. Costoya, P. Mayorga, A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean Journal of Mathematics 22, article 149 (2025), Section 2. https://doi.org/10.1007/s00009-025-02924-0
4. I. Alshatnawi, C. Costoya, A. Viruel, *On the Grothendieck Ring of Finite-Dimensional Non-Degenerate Evolution Algebras*, arXiv:2607.15154 (2026), for the distinct decomposability and tensor-product context. https://arxiv.org/abs/2607.15154
