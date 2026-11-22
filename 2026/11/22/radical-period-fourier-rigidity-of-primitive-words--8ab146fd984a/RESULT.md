# Radical-period Fourier rigidity of primitive words

## Finding
Let \(A\) be any finite abelian group of order \(q\ge 2\), and let \(n\ge 2\). A *primitive word* is a word \(x=(x_0,\ldots,x_{n-1})\in A^n\) with least cyclic rotation period exactly \(n\). Write \(f_{A,n}\) for its indicator and \(T_{A,n}g=f_{A,n}*g\) for **unnormalized** convolution on the additive group \(A^n\). Put
\[
r=\operatorname{rad}(n)=\prod_{p\mid n}p,\qquad b=n/r.
\]
Define the subgroup \(V_b\subseteq A^n\) of words obtained by repeating a block of length \(b\), and its character annihilator \(V_b^\perp\). Then:

1. Every nonzero Fourier multiplier of \(T_{A,n}\) occurs **precisely** at a character in \(V_b^\perp\). Thus
   \[
   \operatorname{rank}T_{A,n}=q^{n-b},\qquad
   \operatorname{nullity}T_{A,n}=q^n-q^{n-b}.
   \]
2. Its smallest nonzero singular value is **exactly** \(q^b\); the largest is the number of primitive words
   \[
   P_n(q)=\sum_{d\mid n}\mu(n/d)q^d.
   \]
   Its exact nonzero-range Hilbert-space condition number is \(P_n(q)/q^b\).
3. The **full additive translation stabilizer** of \(f_{A,n}\) is exactly \(V_b\). The recoverable image of convolution consists exactly of functions constant on cosets of \(V_b\); its orthogonal projection is averaging over \(V_b\). In particular the projection has norm one on every \(\ell^p(A^n)\), \(1\le p\le\infty\).
4. Every multiplier is the following explicit integer, independent of the isomorphism type of \(A\) apart from its order and the character's annihilator conditions:
   \[
   \widehat f_{A,n}(\chi)
   =\sum_{\substack{d\mid n\\\chi\in V_d^\perp}}
   \mu(n/d)q^d.
   \]
   Here \(V_d\) denotes the block-period-\(d\) subgroup for \(d\mid n\).

The squarefree kernel \(b=n/\operatorname{rad}(n)\) therefore controls *all* zero frequencies and the exact recovery dimension. For example, with binary symbols, the ranks at lengths \(6,8,9,12\) are respectively \(32,16,64,1024\), despite ambient dimensions \(64,256,512,4096\).

## Assumptions and scope
All additions are coordinatewise in the finite abelian group \(A\). The word is primitive in the **rotation / proper-power** sense; it need not be unbordered in the usual linear-string sense. Its least rotation period divides \(n\). No quotient by rotation is taken: all labelled rooted words are present. Each frequency \(\chi=(\chi_0,\ldots,\chi_{n-1})\in\widehat A^n\) is a product character. Fourier transforms are unnormalized:
\[
\widehat f(\chi)=\sum_{x\in A^n}f(x)\overline{\chi(x)}.
\]
For each \(d\mid n\), membership \(\chi\in V_d^\perp\) means that for every \(0\le j<d\) the product character \(\chi_j\chi_{j+d}\cdots\chi_{j+(n/d-1)d}\) is trivial on \(A\). Singular values are Euclidean singular values of the counting-convolution matrix; characters form an orthogonal diagonalizing basis.

## Proof
**Step 1: Period sieve.** Every word has a unique least block period dividing \(n\), and a word has period dividing \(d\) exactly when it belongs to \(V_d\). The subgroup \(V_d\) has order \(q^d\). Divisor-lattice Möbius inversion, applied pointwise to the least period, gives
\[
f_{A,n}=\sum_{d\mid n}\mu(n/d)\mathbf 1_{V_d}.
\]
Character orthogonality on a subgroup gives
\[
\sum_{x\in V_d}\overline{\chi(x)}=
\begin{cases}q^d,&\chi\in V_d^\perp,\\0,&\text{otherwise}.\end{cases}
\]
Taking transforms proves assertion 4 and the formula for \(P_n(q)=\widehat f(1)\).

**Step 2: Determine the exact nonzero locus.** A Möbius coefficient \(\mu(n/d)\) is nonzero only if \(n/d\) is squarefree. This forces \(b\mid d\). Thus \(V_b\subseteq V_d\) for every potentially contributing divisor. A character not annihilating \(V_b\) annihilates none of those subgroups, so its multiplier is zero.

Conversely, if \(\chi\in V_b^\perp\), the term at \(d=b\) is present and equals \(\mu(r)q^b\), which is nonzero. Let \(D\) be the **largest** divisor with a nonzero contributing term. All smaller contributing exponents are distinct positive integers. Consequently,
\[
\left|\sum_{\substack{d<D\\d\mid n\\\chi\in V_d^\perp}}
\mu(n/d)q^d\right|
\le\sum_{j=1}^{D-1}q^j<q^D
\quad(q\ge2).
\]
The leading term cannot cancel. Hence \(\widehat f(\chi)\ne0\) at *every* character of \(V_b^\perp\). Since \(|V_b|=q^b\), dual orthogonality gives \(|V_b^\perp|=q^{n-b}\), proving the rank and nullity.

**Step 3: Sharp smallest and largest multipliers.** Every contributing exponent \(d\) is divisible by \(b\). Hence every Fourier coefficient is a multiple of \(q^b\), so a nonzero multiplier has magnitude at least \(q^b\). Choose a nontrivial character \(\psi\in\widehat A\), and let \(\chi_0=\psi\), \(\chi_b=\psi^{-1}\), and all other component characters be trivial. Because \(b<n\) for \(n\ge2\), these are distinct positions. This character annihilates \(V_b\) but no \(V_d\) with \(d>b\) and \(d\mid n\), since positions \(0\) and \(b\) belong to distinct residue classes modulo such a \(d\). Therefore
\[
\widehat f(\chi)=\mu(r)q^b,
\]
attaining the lower bound. The triangle inequality gives \(|\widehat f(\chi)|\le P_n(q)\), with equality at the trivial character. Normality of convolution and Fourier diagonalization give the singular values and condition number.

**Step 4: Exact additive stabilizer and recovered range.** Translation by \(v\in A^n\) fixes \(f\) if and only if every \(\chi\) with \(\widehat f(\chi)\ne0\) is trivial on \(v\). The nonzero locus is *all* of \(V_b^\perp\), whose common annihilator is \(V_b\). Thus the stabilizer equals \(V_b\). The range of \(T_{A,n}\) is the span of the same characters, equivalently the coset-constant functions. Orthogonal projection onto this range is
\[
(\Pi_b g)(x)=q^{-b}\sum_{v\in V_b}g(x+v).
\]
Averaging is a contraction on every \(\ell^p\) and fixes nonzero constant functions, giving its exact operator norm one.

## Verification
The included `verify.py` uses four independent, exact finite test mechanisms: (i) an in-place integer Walsh–Hadamard transform of primitive binary words at all lengths \(2\le n\le12\); (ii) direct enumeration of each cyclic ternary word-frequency pair at lengths \(2\le n\le6\), reducing cyclotomic sums in the basis \(1,\omega\); (iii) direct cyclic order-four sums in the basis \(1,i\) at lengths \(2\le n\le4\); and (iv) direct order-four Klein-group character sums at lengths \(2\le n\le4\). It compares every coefficient to the divisor formula and every rank, minimum and maximum to the theorem.

Run `python3 verify.py` from the directory of this file. Expected exact output:

```text
PASS binary_frequency_tests=8188 ternary=1089 cyclic4=336 klein=336
```

The proof of all parameter ranges is the preceding algebra, not extrapolation from these finite tests.

## Relationship to prior work
The classical formula for the number of primitive necklaces, and the Möbius formula for primitive rooted words, are not claimed as new. Moree's 2003 paper studies the necklace/Witt transform, fixed-content enumeration and a sign-twisted variation; its Sections 1–4 were examined. Its sign twist depends on symbol counts, not arbitrary **position-dependent** dual characters, and it does not state the present exact Fourier support, rank, smallest multiplier, or translation stabilizer.

The previous study of *first-band Fourier sampling on surjective words* (2026) addresses sampled degree-one Gram eigenvalues on an onto-word ensemble, not full counting-convolution for primitive words. The previously published *sharp root-ratio thresholds for primitive-necklace counts* (2026) treats growth of \(P_n(q)/n\), not Fourier zeros. These objects, operators, and implications were differentiated rather than treating titles alone as novelty evidence.

## Limitations
No claim is made for arbitrary nonabelian alphabets, words primitive under a different period notion, rotation-quotient necklaces as an additive group, or weighted indicators. The formula determines each multiplier but does not present a closed table of *multiplicities for every distinct nonzero multiplier*. The originality search was bounded; an unindexed equivalent treatment using period-group algebras may exist. This work has not undergone independent mathematical validation.

## References
- P. Moree, *The formal series Witt transform*, arXiv:math/0311194v1, first public version 2003-11-12, https://arxiv.org/abs/math/0311194 . Sections 1–4; established necklace and Möbius formulas.
- *Exact first-band Fourier sampling spectra on surjective words*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-first-band-fourier-sampling-spectra-on-surjective-words--38dfe55b7163 . Different ensemble and operator.
- *Sharp root-ratio thresholds for primitive-necklace counts*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-root-ratio-thresholds-for-primitive-necklace-counts--776f6cf4f46c . Same counting polynomial but different invariant.
