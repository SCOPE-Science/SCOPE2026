# Minimum radial sampling layers for a tight quadratic Walsh frame

## Finding

For every integer \(n\ge4\), exactly two or three full Boolean Hamming shells suffice to sample the homogeneous degree-two Walsh Fourier space isometrically with positive weights constant on each shell. A single shell never suffices. There is an exact arithmetic criterion for when two suffice, a modular obstruction on three complete residue classes, and two infinite constructive families with two-shell tight sampling.

Write \(\mathcal X_n=\{-1,1\}^n\), and for an admissible imbalance \(s\in\{-n,-n+2,\ldots,n\}\), let \(\sigma_s\) denote uniform probability on \(H_s=\{x\in\mathcal X_n:\sum_jx_j=s\}\). A radial sampling measure on \(r\) shells is \(\mu=\sum_{j=1}^r w_j\sigma_{s_j}\), where the \(s_j\) are distinct, \(w_j>0\), and \(\sum_jw_j=1\). Define \(r_n\) as the smallest \(r\) for which

\[
\int_{\mathcal X_n}\left|\sum_{1\le i<j\le n}c_{ij}x_ix_j\right|^2\,d\mu(x)
=\sum_{1\le i<j\le n}|c_{ij}|^2
\]

holds for every complex coefficient vector \((c_{ij})\). The exact result is

\[
 r_n=\begin{cases}
 2,&\text{if there are integers }0\le a<b\le n,\quad a\equiv b\equiv n\pmod2,\quad
       (n-a^2)(b^2-n)=2n(n-1),\\
 3,&\text{otherwise.}
 \end{cases}
\]

Whenever the equation holds, necessarily \(a^2<n<b^2\), and the unique masses on those two squared-imbalance levels are

\[
 w_a=\frac{b^2-n}{b^2-a^2},\qquad
 w_b=\frac{n-a^2}{b^2-a^2}.
\]

The positive or negative signed shell with each absolute imbalance may be used independently: the frame identity depends only on its square. In particular,

\[
 n\equiv4,5,7\pmod8\quad\Longrightarrow\quad r_n=3.
\]

Conversely, both \(n=m^2+2\) for any integer \(m\ge2\) (choose \(a=m,b=n\)) and \(n=(b^2+2)/3\) for any even integer \(b\ge4\) not divisible by three (choose \(a=0\) and that \(b\)) yield \(r_n=2\). The formula is an exact decidable classification for every individual dimension; it does not assert that the three forbidden residue classes are the only dimensions requiring three shells.

## Assumptions and scope

The measure is a *probability* measure, uniform **within** each full shell, with arbitrary positive **shell masses**. The total point weights at different shells need not coincide. The measured family comprises precisely the distinct homogeneous quadratic Walsh characters \(x_ix_j\), not all Walsh polynomials of degree at most two. Tightness means an exact Parseval identity with the ambient uniform-cube Walsh coefficient normalization, not a cardinality-minimal relative design. The allowed shells may include the boundary \(s=\pm n\); no assumption of antipodal balancing between signed shells is imposed.

## Proof

**1. The Gram constraints.** For two different unordered pairs \(I,J\subset\{1,\ldots,n\}\) of size two, their symmetric difference has size two if the pairs share one coordinate, and size four if they are disjoint. Both occur for \(n\ge4\). Permutation symmetry of each shell shows that its quadratic-Walsh Gram matrix has identity diagonal and only two off-diagonal values: the common two-coordinate product moment and the common four-coordinate product moment. Thus the Gram matrix of \(\mu\) is the identity precisely when its order-two and order-four distinct-coordinate moments both vanish.

**2. Exact shell moments.** Put \(S=\sum_jx_j=s\) on a shell and \(U=s^2\). Expanding \(S^2\), using \(x_j^2=1\), gives the two-coordinate moment

\[
 m_2(s)=\frac{s^2-n}{n(n-1)}.
\]

Newton's identities for the elementary symmetric polynomial of degree four, or a direct expansion of \(S^4\) after separating index multiplicities, give

\[
 m_4(s)=\frac{s^4-(6n-8)s^2+3n(n-2)}{n(n-1)(n-2)(n-3)}.
\]

The denominators are nonzero for all \(n\ge4\). Consequently the two zero-moment equations are precisely

\[
 \mathbb E_\mu U=n,\qquad
 \mathbb E_\mu U^2=n(3n-2),\qquad
 \operatorname{Var}_\mu U=2n(n-1)>0.
\]

These are both necessary and sufficient for all quadratic-Walsh Gram entries. In particular, a single radial shell cannot be tight.

**3. Three shells always suffice.** Under the uniform probability distribution on the entire Boolean cube, the homogeneous Walsh characters are orthonormal, so the two moment equations above hold. Equivalently, its distribution over signed shells gives a convex combination of the finitely many points \((s^2,s^4)\) with barycenter \((n,n(3n-2))\). By the two-dimensional Carathéodory theorem, that barycenter is a convex combination of at most three of those points. A zero mass is discarded, and if a repeated squared imbalance occurs, its masses are consolidated onto one signed shell. These operations leave both required moments unchanged and preserve positivity of retained masses. Thus \(r_n\le3\) for all \(n\ge4\).

**4. Exact two-shell criterion and uniqueness.** Let the two distinct squared imbalances be \(u=a^2<v=b^2\). Since the variance is positive, their positive masses force \(u<n<v\), and the equation \(\mathbb E U=n\) uniquely fixes the masses to \((v-n)/(v-u)\) and \((n-u)/(v-u)\). Their variance is

\[
 \frac{v-n}{v-u}\frac{n-u}{v-u}(v-u)^2
 =(n-u)(v-n).
\]

Equating it to \(2n(n-1)\) yields precisely the displayed Diophantine condition. Conversely, any admissible pair satisfying it has the displayed strictly positive masses and meets both moments, proving tightness. Every valid two-shell choice is accounted for, including shell-sign freedom.

**5. Modular nonexistence.** If \(n\equiv4\pmod8\), then \(a,b\) are even and each of \(n-a^2\) and \(b^2-n\) is divisible by four. Their product is divisible by sixteen, while \(2n(n-1)\) is divisible by eight but not sixteen. If \(n\equiv5\pmod8\), then \(a,b\) are odd, so \(a^2\equiv b^2\equiv1\pmod8\); again the left product is divisible by sixteen and the right has exactly three factors of two. Finally, if \(n\equiv7\pmod8\), odd squares are \(1\) or \(9\) modulo sixteen, so for either \(n\equiv7\) or \(15\pmod{16}\),

\[
 (n-a^2)(b^2-n)\equiv12\pmod{16},
 \qquad 2n(n-1)\equiv4\pmod{16}.
\]

This contradiction rules out all two-shell frames in the three stated classes. Step 3 then forces exactly three shells there.

**6. Infinite constructions.** For any \(m\ge2\), put \(n=m^2+2\), \(a=m\), \(b=n\). The parities are admissible and

\[
 (n-a^2)(b^2-n)=2(n^2-n)=2n(n-1).
\]

For even \(b\ge4\) with \(3\nmid b\), the integer \(n=(b^2+2)/3\) is even and strictly greater than \(b\), and choosing \(a=0\) gives \(n(b^2-n)=2n(n-1)\). Both families have positive exact sampling weights from Step 4. This completes the proof.

## Verification

Run the standalone Python 3 file `check_two_shell.py` (standard library only). It enumerates exact shell moments for dimensions four through ten; computes the full quadratic-Walsh Gram matrices over all vertices for two explicitly weighted tight frames; checks several two-shell solutions with rational arithmetic; verifies the stated modular obstruction through dimension three thousand; and exercises both parametrized solution families. Expected terminal marker: `QUADRATIC_WALSH_TWO_SHELL_PASS`. These finite checks are corroboration. No finite enumeration is used to prove the all-dimension characterization or the modular obstruction.

## Relationship to prior work

The Boolean Hamming-sphere Fourier and Krawtchouk setting is classical. Kirshner and Samorodnitsky (2019) study Krawtchouk polynomial moment bounds and near-extremal properties of spheres; their moment-ratio inequalities do not state the minimum radial-shell count for exact quadratic-Walsh Parseval sampling. Bannai, Bannai, Tanaka and Zhu (2020) develop *relative* designs on two shells with a Fisher cardinality-based meaning of “tight”; the current Parseval frame problem has a different target measure, a different tightness definition, and a whole-shell positive-weight constraint. Rao (2021) analyzes the Fourier transform on a single Hamming slice using its Johnson-scheme harmonic structure, rather than globally matched quadratic-Walsh moments over several shells.

A previously available general Gram-spectrum analysis for a weighted pair of interior shells in the **entire degree-at-most-two** Walsh band is closely related and covers the input sampling measures. It does not assert the present exact **pure-degree-two** Parseval two-versus-three minimum, the arithmetic criterion for two shells, the three full congruence obstructions, or the all-dimension three-shell existence result. The common elementary shell-moment identities are not claimed as new. The novel focus is their simultaneous exact cubature feasibility and minimal-layer arithmetic; an implicit derivation from broader Walsh spectral work remains a residual bibliographic risk.

## Limitations

The two-shell criterion is a finite arithmetic test in each dimension, not a simple classification by residues: dimensions outside \(4,5,7\pmod8\) may also need three shells. This result does not determine optimal numbers of individual sample **points**, general nonuniform weights inside a shell, frames for the complete degree-at-most-two space, or higher homogeneous degrees. The proof is self-contained, but historical originality has not undergone independent specialist audit.

## References

1. N. Kirshner and A. Samorodnitsky, *A moment ratio bound for polynomials and some extremal properties of Krawchouk polynomials and Hamming spheres*, arXiv:1909.11929 (first public 2019-09-26), https://arxiv.org/abs/1909.11929.
2. E. Bannai, E. Bannai, H. Tanaka and Y. Zhu, *Tight relative t-designs on two shells in hypercubes, and Hahn and Hermite polynomials*, arXiv:2006.02054 (first public 2020-06-03), https://arxiv.org/abs/2006.02054.
3. S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, arXiv:2111.03213 (first public 2021-11-05), https://arxiv.org/abs/2111.03213.
