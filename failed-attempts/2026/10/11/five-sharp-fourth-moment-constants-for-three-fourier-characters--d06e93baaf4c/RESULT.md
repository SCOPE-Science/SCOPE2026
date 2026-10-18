# Five sharp fourth-moment constants for three Fourier characters on finite abelian groups

## Finding
Let \(G\) be any finite abelian group, let \(\Gamma=\widehat G\) be its character group, written additively, and let \(S=\{\gamma_0,\gamma_1,\gamma_2\}\subset\Gamma\) consist of three distinct characters. Define the sharp three-frequency fourth-moment constant
\[
C_4(S)=\max_{(c_0,c_1,c_2)\ne0}\frac{|G|^{-1}\sum_{x\in G}|\sum_{j=0}^2 c_j\gamma_j(x)|^4}{(\sum_{j=0}^2|c_j|^2)^2}.
\]
There are exactly six mutually exclusive additive types of \(S\), with only five possible sharp constants:

| Additive type of the three characters | \(C_4(S)\) |
| --- | --- |
| All six unordered two-term sums are distinct (Sidon triple) | \(5/3\) |
| Exactly one equality \(2\gamma_i=2\gamma_j\), with no midpoint equality | \(2\) |
| Exactly one equality \(2\gamma_m=\gamma_i+\gamma_j\), with no equality of two doubles | \(15/7\) |
| A midpoint equality and an equality of endpoint doubles; necessarily a coset of \(\{0,u,2u\}\) with \(\operatorname{ord}(u)=4\) | \(7/3\) |
| All three doubles coincide; necessarily a three-point subset of a four-element Klein subgroup coset | \(7/3\) |
| All three points form a coset of a subgroup of order \(3\) | \(3\) |

Every maximizing coefficient vector is characterized below. Put \(M=\sum_j|c_j|^2\). In the Sidon case, equality holds exactly when all three coefficient squared moduli are \(M/3\), with unrestricted phases. In the single double-coincidence case, the pair involved has squared moduli \(M/2\), the third coefficient is zero, and the two nonzero coefficient squares have the same phase. In the single-midpoint case, the midpoint coefficient has squared modulus \(3M/7\), the endpoints each have squared modulus \(2M/7\), and the midpoint's square has the phase of the endpoints' product. In the order-four case all three squared moduli are \(M/3\), the endpoint squares have the same phase, and the midpoint square has the phase of the endpoints' product. In the Klein case all three squared moduli are \(M/3\) and their squares have the same phase. In the order-three case equality holds exactly for
\[
c_j=\lambda\overline{\gamma_j(x_0)}\quad(0\le j\le2),\qquad \lambda\in\mathbb C\setminus\{0\},\quad x_0\in G.
\]
Here “same phase” means that the quotient of the two nonzero complex quantities is a positive real number. These are necessary and sufficient conditions, including the possibility that one coefficient is zero only in the single double-coincidence type.

## Assumptions and scope
The group is finite and abelian; no restriction on its order, exponent, or invariant-factor decomposition is needed beyond the existence of three distinct characters. All averages use normalized counting measure on \(G\), and all characters have modulus one. The coefficient vector may have zeros even though the available character set \(S\) has three members. No claim is made for supports of four or more characters, other moment exponents, or nonabelian representations.

## Proof
Write \(F(x)=\sum_j c_j\gamma_j(x)\). Since characters are orthonormal under normalized counting measure, Fourier orthogonality applied to \(F^2\) gives the **exact** identity
\[
|G|^{-1}\sum_{x\in G}|F(x)|^4=\sum_{\sigma\in\Gamma}\left|\sum_{i,j:\,\gamma_i+\gamma_j=\sigma}c_ic_j\right|^2.\tag{1}
\]
The only potentially colliding monomials come from the six unordered pairs, with diagonal weights \(c_i^2\) and off-diagonal weights \(2c_ic_j\). If two distinct unordered pair sums agree, cancellation of a shared character shows that either \(2\gamma_i=2\gamma_j\) for distinct \(i,j\), or \(2\gamma_m=\gamma_i+\gamma_j\) for all distinct indices. There are no other possible collision types.

Two distinct midpoint equalities imply three midpoint equalities and make \(S\) an order-three coset. Two distinct equalities between doubles imply all three doubles coincide, so their differences are order-two elements and \(S\) lies in an affine Klein four-subgroup. When precisely one midpoint equality and one double equality occur, the double equality must involve the two endpoints; otherwise distinctness is contradicted. Writing the triple as \(\{a-u,a,a+u\}\), the endpoints differ by \(2u\), which is nonzero of order two. Hence \(u\) has order four. These exhaust the six types.

Let \(x_j=|c_j|^2\ge0\) with \(x_0+x_1+x_2=1\); homogeneity justifies this normalization. If there are no collisions, (1) becomes \(2-\sum_j x_j^2\le5/3\), with equality precisely for \(x_j=1/3\). If there is one equality \(2\gamma_i=2\gamma_j\), (1), together with the triangle inequality, gives
\[
C\le 2-(x_i-x_j)^2-x_k^2\le2.
\]
Equality forces \(x_i=x_j=1/2\), \(x_k=0\), and equal phases of \(c_i^2,c_j^2\).

If the only collision is \(2\gamma_m=\gamma_i+\gamma_j\), the triangle inequality bounds (1) by
\[
x_i^2+x_j^2+4x_m(x_i+x_j)+(x_m+2\sqrt{x_ix_j})^2.
\]
For fixed \(x_m=t\), this is strictly increasing in \(\sqrt{x_ix_j}\), so \(x_i=x_j=(1-t)/2\) at equality. Substitution gives
\[
\frac32+3t-\frac72t^2=\frac{15}{7}-\frac72\left(t-\frac37\right)^2\le\frac{15}{7}.
\]
Equality also requires aligned phases of \(c_m^2\) and \(c_ic_j\), giving the claimed midpoint condition.

For an order-four triple, label the endpoints \(i,j\) and midpoint \(m\). The four convolution fibers in (1) have coefficients \(c_i^2+c_j^2\), \(c_m^2+2c_ic_j\), \(2c_ic_m\), and \(2c_jc_m\). Writing \(t=x_m\) and \(u=x_i+x_j=1-t\), the triangle inequality and \(2\sqrt{x_ix_j}\le u\) give
\[
C\le u^2+(t+u)^2+4tu=1+4u-3u^2\le\frac73.
\]
Equality is equivalent to \(u=2/3\), \(x_i=x_j=1/3\), and both indicated fiberwise phase alignments.

For the Klein triple the convolution fibers have coefficients \(c_0^2+c_1^2+c_2^2\) and the three products \(2c_ic_j\). Consequently
\[
C\le1+4\sum_{i<j}x_ix_j=3-2\sum_jx_j^2\le\frac73.
\]
Equality forces \(x_0=x_1=x_2=1/3\) and all three squares to align.

Finally, for an order-three coset, multiplying by a fixed character reduces to a function constant on cosets of the annihilator of the order-three subgroup. The resulting function is an arbitrary function on a quotient of size three, with \(\|F\|_2^2=M\). Pointwise concentration gives \(\|F\|_4^4\le3M^2\), with equality if and only if the induced function is supported at one quotient point. Fourier inversion on that quotient gives exactly the three displayed coefficient phases. Thus all six sharp constants and their complete equality conditions follow.

## Verification
Run `python checker.py` with standard Python 3. The checker generates all translated triples with a fixed zero character in cyclic groups of orders \(3\) through \(33\) and nine noncyclic products. It checks that every collision structure belongs to precisely one of the six types, that the stated attaining coefficients achieve the asserted ratio, and that 23,160 integer-Gaussian coefficient choices satisfy the exact rational upper bound by integer arithmetic. It also compares the character-side and convolution-side fourth moments on 167 representative small-group inputs. Its observed output was `VERIFY_OK triples= 5790 gaussian_integer_tests= 23160 direct_Fourier= 167 max_fourier_error= 9.95e-14 cases= {'sidon': 4494, 'single_involution': 450, 'single_progression': 744, 'cyclic_four': 51, 'klein_four': 33, 'cyclic_three': 18}`. The finite checks corroborate (1); the general classification follows from the exhaustive symbolic collision analysis above, not computational enumeration.

## Relationship to prior work
Shkredov's work on higher energies and Sidon sets (2021) motivates the connection between repeated sums and fourth moments but studies Sidon-type substructures and higher-energy estimates rather than sharp weighted three-character \(L^2\)-to-\(L^4\) norms and equality cases. Schmidt's 2013 work analyzes small fourth moments of long unimodular polynomials and records an autocorrelation identity, but fixes coefficient magnitudes and treats asymptotic families rather than this maximum with freely varying coefficients. Neuwirth's analysis of trigonometric trinomials concerns the maximum-modulus norm and Sidon constants, not the sharp fourth moment.

Recent work on three-frequency phase resonance gives formulas for even moments of **unimodular** trinomials on the continuous circle; it does not classify optimizers over nonuniform magnitudes or torsion-sensitive finite abelian groups. Work on four-point supports in prime cyclic groups studies the **minimum** fourth moment with equal-magnitude coefficients, likewise not the present maximum on three-point supports. Their concrete statements therefore do not imply the theorem here.

## Limitations
This is an elementary but complete three-character classification; the general convolution identity and familiar Sidon principle are prior facts, not claimed as new. The contribution is the universal exact five-value list, the order-two and order-four transition, and the six equality classifications. Equivalent small-support computations in older \(\Lambda(4)\), Littlewood-polynomial, coding, or sequence-design literature cannot be ruled out by available searches, so originality remains subject to independent literature review. No quantitative claim beyond three characters is made.

## References
1. I. D. Shkredov, *On an application of higher energies to Sidon sets*, arXiv:2103.14670v1 (first public 2021-03-26), https://arxiv.org/abs/2103.14670.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1 (first public 2013-02-12), https://arxiv.org/html/1302.2766v1.
3. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1 (first public 2007-03-08), https://arxiv.org/abs/math/0703236.
4. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79.
5. *Four-point support geometry quantizes the phase-only fourth Fourier moment*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-point-support-geometry-quantizes-the-phase-only-fourth-four--2b7f859e0b5c.
