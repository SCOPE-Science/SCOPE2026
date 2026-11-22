# Retraction-rank spectra and class-dependent concentration in free nilpotent Lie algebras

## Finding
Let \(c\ge3\) and \(d\ge2\). For every field \(K\), let \(L_{d,c}(K)\) denote the free nilpotent Lie algebra of class at most \(c\) on \(d\) generators. Define the Witt dimensions and their sums by
\[
w_j(t)=\frac1j\sum_{a\mid j}\mu(a)t^{j/a},\qquad D_c(t)=\sum_{j=1}^{c}w_j(t),\qquad S_c(t)=D_c(t)-t.
\]
Every idempotent Lie-algebra endomorphism \(F\) of \(L_{d,c}(K)\) has image isomorphic to \(L_{r,c}(K)\) for one and only one integer \(0\le r\le d\). Two such endomorphisms are conjugate by an algebra automorphism exactly when their induced maps on the abelianization have the same rank \(r\). Their full linear rank is \(D_c(r)\).

Over each finite field \(\mathbb F_q\), the **complete labeled retraction-rank enumerator**, including nonlinear generator images, is
\[
\boxed{\mathcal R_{d,c,q}(T)=\sum_{r=0}^{d}{d\brack r}_q\,q^{r(d-r)+r[S_c(d)-S_c(r)]+(d-r)S_c(r)}T^{D_c(r)}.}
\]
Here \({d\brack r}_q\) is the Gaussian binomial coefficient; each coefficient counts exactly the endomorphisms of the specified ordinary linear rank. The endpoint coefficients equal one. More finely, exactly
\[
\boxed{I_{d,c,r}(q)={d\brack r}_q q^{r[S_c(d)-S_c(r)]}}
\]
distinct embedded image subalgebras of this type occur, and **each particular embedded image** supports exactly
\[
\boxed{M_{d,c,r}(q)=q^{(d-r)D_c(r)}}
\]
idempotent retractions onto it. Thus the formula resolves both the image embedding and map multiplicity, not just the marginal rank count. In particular, for two generators the class-three and class-four polynomials are, respectively,
\[
1+(q+1)q^4T+T^5,\qquad 1+(q+1)q^7T+T^8.
\]

For fixed \(c\ge3\) and fixed prime power \(q\), let \(r_d\) be the induced abelianization rank of an idempotent chosen uniformly from all such endomorphisms on \(L_{d,c}(\mathbb F_q)\). Write
\[
f_c(a)=a+(1-2a)a^c,\qquad \alpha_c\in(1/2,1):\quad 1+c\alpha_c^{c-1}-2(c+1)\alpha_c^c=0.
\]
There is exactly one indicated root. For every fixed \(\varepsilon>0\), a positive constant \(\kappa_{c,q,\varepsilon}\) exists such that, for all sufficiently large \(d\),
\[
\Pr\bigl(|r_d/d-\alpha_c|>\varepsilon\bigr)\le q^{-\kappa_{c,q,\varepsilon}d^{c+1}}.
\]
Consequently \(r_d/d\) converges in probability to \(\alpha_c\), the full image-rank fraction \(D_c(r_d)/D_c(d)\) converges in probability to \(\alpha_c^c\), and
\[
\lim_{d\to\infty}\frac{\log_q\mathcal R_{d,c,q}(1)}{d^{c+1}}=\frac{f_c(\alpha_c)}c.
\]
For \(c=3\), \(\alpha_3\simeq0.6610498029006991\); the same numerical root has also arisen in a distinct anti-associative-algebra retraction problem and is not claimed as a newly discovered constant.

## Assumptions and scope
Lie brackets are alternating, including in characteristic two. The object is the free \(c\)-step nilpotent Lie algebra, a quotient of the integral free Lie algebra by bracket lengths exceeding \(c\). Hall bases show that its degree-\(j\) dimension equals the Witt number \(w_j(d)\) over every field, independently of characteristic. Its abelianization is the span \(V\) of the specified \(d\) generators. The word *retraction* means a \(K\)-linear Lie endomorphism satisfying \(F\circ F=F\), not a derivation or an idempotent element.

The formula concerns **labeled** endomorphism maps, not just isomorphism types. The exact census applies to every prime power, while the probability statements fix both \(c\) and \(q\) as \(d\to\infty\). The theorem does not cover quotients of free nilpotent Lie algebras with extra relations, pro-nilpotent completions, or classification of arbitrary nonidempotent endomorphisms. The polynomial notation has the usual empty-subspace conventions at \(r=0\).

## Proof
**1. The free graded filtration and automorphisms.** Put \(J=[L_{d,c},L_{d,c}]\), the sum of bracket-length pieces from degree two through \(c\). By the free universal property, arbitrary images of the \(d\) generators determine a unique endomorphism. Any assignment of generators that is invertible modulo \(J\) determines an automorphism: its induced maps on the degree-\(j\) associated-graded pieces are those of the corresponding invertible degree-one linear map, and hence are invertible. A filtration-preserving linear map that is invertible on all finite graded quotients is invertible. In particular, the kernel \(G\) of the action of automorphisms on \(V=L_{d,c}/J\) consists of the independent assignments \(v_i\mapsto v_i+h_i\), with each \(h_i\in J\), and
\[
|G|=q^{dS_c(d)}
\]
over \(\mathbb F_q\). The extension and invertibility statements do not divide by any field characteristic.

**2. Normal form for every idempotent.** For \(F^2=F\), the induced linear map \(A\) on \(V\) is an idempotent of rank \(r\). Conjugate by the degreewise extension of a suitable \(\operatorname{GL}(V)\) change of generators so that \(A=P\), the projection for a direct sum \(V=U\oplus W\), with \(\dim U=r\). Let \(\widetilde P\) be the Lie endomorphism fixing the generators in \(U\) and killing those in \(W\). Define a new generator assignment
\[
H(u)=F(u)\quad(u\text{ in a basis of }U),\qquad H(w)=w-F(w)\quad(w\text{ in a basis of }W).
\]
Because these assignments are the identity modulo \(J\), they extend to an automorphism \(H\in G\). Idempotence immediately gives \(F(H(u))=H(u)\) and \(F(H(w))=0\); hence \(FH=H\widetilde P\) on generators, and therefore on the whole algebra. Thus \(F=H\widetilde PH^{-1}\). The image is the free \(c\)-step algebra on \(r\) generators and has dimension \(D_c(r)\). Distinct values of \(r\) cannot be conjugate because the abelianization rank is invariant. This proves the classification in all characteristics.

**3. Exact conjugation-stabilizer count.** Fix the degree-one projection \(P\). The group \(G\) acts transitively by conjugation on idempotent lifts of \(P\), by Step 2. For \(H\in G\), the condition \(H\widetilde P=\widetilde PH\) is equivalent to these independent conditions on its generator corrections: \(h_u\) for each of the \(r\) basis elements of \(U\) lies in the degree-at-least-two free Lie subalgebra on \(U\), a space of dimension \(S_c(r)\); and \(h_w\) for each of the \(d-r\) basis elements of \(W\) lies in the kernel of \(\widetilde P|_J\), a space of dimension \(S_c(d)-S_c(r)\). Consequently
\[
|C_G(\widetilde P)|=q^{rS_c(r)+(d-r)[S_c(d)-S_c(r)]},
\]
so the number of lifts of this fixed \(P\) is
\[
\frac{|G|}{|C_G(\widetilde P)|}=q^{r[S_c(d)-S_c(r)]+(d-r)S_c(r)}.
\]
There are \({d\brack r}_q\) choices for the image of a rank-\(r\) projection on \(V\), with \(q^{r(d-r)}\) complementary kernels for each. Multiplying proves the exact polynomial. For the refined image count, an image with fixed degree-one span \(U\) is conjugate under \(G\) to the standard free subalgebra \(L_{r,c}(U)\). Its stabilizer permits \(S_c(r)\) higher-degree parameters for each generator in \(U\) and all \(S_c(d)\) parameters for each generator in \(W\). Dividing \(q^{dS_c(d)}\) by the stabilizer size and choosing the leading \(r\)-plane gives \(I_{d,c,r}(q)\). The ratio of the total map count to this image count is \(q^{(d-r)[r+S_c(r)]}=q^{(d-r)D_c(r)}\), independent of the image, because \(G\) acts transitively on images with a fixed \(r\)-plane and \(\operatorname{GL}(V)\) acts transitively on all planes. All powers are nonnegative integers. For \(r=0,d\) the orbit has one map.

**4. Asymptotic exponent.** For fixed \(c\ge3\), the Witt formula gives \(S_c(t)=t^c/c+O_c(t^{c-1})\) as \(t\to\infty\). Uniformly for integer \(0\le r\le d\), the rank-stratum coefficient \(N_{d,c,r}(q)\) from Step 3 satisfies
\[
\log_q N_{d,c,r}(q)=\frac{d^{c+1}}c f_c(r/d)+O_{c,q}(d^c).
\]
Indeed \(\log_q {d\brack r}_q=O_q(d^2)\) uniformly, as does the projection-complement exponent; the two terms involving \(S_c\) have leading value \(d^{c+1}[a+(1-2a)a^c]/c\), where \(a=r/d\). The stated error is valid because \(c\ge3\).

**5. Unique saddle and concentration.** The derivative of \(f_c\) is
\[
f_c'(a)=1+c a^{c-1}-2(c+1)a^c,
\]
and its second derivative is \(c a^{c-2}[(c-1)-2(c+1)a]\). Thus \(f_c'\) first increases and then strictly decreases, is positive at \(a=1/2\) and negative at \(a=1\). It has exactly one zero \(\alpha_c\in(1/2,1)\), the unique global maximizer. For each fixed \(\varepsilon>0\), compactness supplies a positive gap \(\delta\) between this maximum and every \(f_c(a)\) with \(|a-\alpha_c|\ge\varepsilon\) in \([0,1]\). A rank closest to \(\alpha_c d\) has exponent \(d^{c+1}f_c(\alpha_c)/c+O(d^c)\). The bad ranks contribute at most \(d+1\) terms of exponent lower by \(\delta d^{c+1}/c+O(d^c)\). Dividing by the total census yields the asserted exponentially small probability, for a suitable positive constant. The Witt leading term also gives \(D_c(r_d)/D_c(d)\to\alpha_c^c\) in probability. Comparing the total count with its maximum summand proves the logarithmic growth limit.

## Verification
Run `python3 verify.py` (Python standard library only) to exhaustively enumerate **all generator assignments** to the class-three free Lie algebra on two generators over \(\mathbb F_2\) and \(\mathbb F_3\), and the class-four counterpart over \(\mathbb F_2\). The checker constructs induced maps on the full Hall bases using explicit structure constants, tests composition-idempotence on both generators without relying on the claimed census, computes the induced abelianization rank, and compares the observed histogram with the formula. It confirms respectively \((1,48,1)\), \((1,324,1)\), and \((1,384,1)\) for generator ranks \(0,1,2\), checking \(1{,}024\), \(59{,}049\), and \(65{,}536\) assignments. The sample computations are checks, not substitutes for the all-parameter proof and asymptotic argument.

## Relationship to prior work
Published class-two results already classify retractions of \(V\oplus\bigwedge^2 V\), enumerate their ranks, and prove a sharp two-neighbor concentration law. Their scope explicitly excludes free nilpotent Lie algebras of class three and higher. The present statement covers **every fixed class \(c\ge3\)** in all finite characteristics and determines their entire graded-Witt-dependent rank spectra and distinct class-dependent entropy functions. It does not reclaim the known class-two result or claim novelty for the free mapping property.

The general free-nilpotent automorphism parameterization of Benito and Roldán-López is a structural precursor, not a finite-field idempotent census. Del Barco and Ovando study the automorphism structure of free nilpotent Lie algebras in the context of ad-invariant metrics, not these retraction fibers. Classical work of Mikhalev and Yu characterizes retracts of unrestricted free Lie algebras, but the accessible abstract does not supply the exact finite-field class-\(c\) quotient census; the unread full text remains a priority risk.

A published result for **free anti-associative algebras** gives an analogous generator-conjugation count and cubic rank condensation, including the same numerical root \(\alpha_3\). Those algebras do not satisfy the Lie relations and the result does not imply the Lie-algebra census; the shared method and constant are acknowledged. This result is assessed as a complete invariant for a different classical family, rather than as a new general orbit-stabilizer technique.

## Limitations
The theorem is about free nilpotent Lie algebras and their composition-idempotent endomorphisms only. It does not yield a two-adjacent-rank concentration bound for each finite \(d\), a count of arbitrary endomorphisms, or a global publication-priority guarantee. The 1997 retract characterization was available only in abstract, and a more general free-object enumeration could subsume some of the counting arguments. Independent scientific review has not been performed. All exhaustive verification is in small explicit cases.

## References
1. G. Ovando and V. del Barco, *Free Nilpotent Lie Algebras Admitting Ad-Invariant Metrics*, arXiv:1104.4773, first public 2011-04-25, https://arxiv.org/abs/1104.4773.
2. P. Benito and D. de-la-Concepción, *An overview of free nilpotent Lie algebras*, 2014, https://dml.cz/handle/10338.dmlcz/143811.
3. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897, 2019-11-05, https://arxiv.org/abs/1911.01897.
4. *Retraction orbits and finite-field rank spectra of free two-step nilpotent Lie algebras*, published 2026-10-13, https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-retraction-orbits-and-finite-field-rank-spectra-of-free-two-step--7573f7956962/RESULT.md.
5. *Exact retraction-rank spectrum and two-point concentration in free class-two Lie algebras*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-retraction-rank-spectrum-and-two-point-concentration-in-fr--8cb566c6da84/RESULT.md.
6. *Cubic-rank condensation for retractions of free anti-associative algebras*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-cubic-rank-condensation-for-retractions-of-free-anti-associative--1b2c8029e3a6/RESULT.md.
7. A. A. Mikhalev and J.-T. Yu, *Test elements and retracts of free Lie algebras*, Communications in Algebra 25 (1997), 3283–3289, https://doi.org/10.1080/00927879708826054 (abstract inspected; full text inaccessible).
