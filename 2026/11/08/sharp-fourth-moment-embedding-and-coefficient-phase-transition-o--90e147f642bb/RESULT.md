# Sharp fourth-moment embedding and coefficient phase transition on Johnson slices

## Finding
For every integer \(n\ge4\) and \(2\le k\le n-2\), the exact real \(L^2\)-to-\(L^4\) embedding norm of the first nonconstant harmonic subspace of the uniform Johnson slice has a closed formula, with a sharp change in the full optimizer class. Define
\[
 c=\frac{k(n-k)}{n(n-1)},\qquad
 A=\frac{3k(k-1)(n-k)(n-k-1)}{n(n-1)(n-2)(n-3)},
\]
\[
 B=\frac{k(n-k)[n(n+1)-6k(n-k)]}{n(n-1)(n-2)(n-3)},\qquad
 T_+=\frac{n^2-3n+3}{n(n-1)},\quad
 T_-=\frac{n}{\lfloor n/2\rfloor\lceil n/2\rceil}-\frac3n.
\]
Then, with \(\mathcal H_1=\{f_a(S)=\sum_{i\in S}a_i:\sum_i a_i=0\}\),
\[
 \boxed{\sup_{0\ne f\in\mathcal H_1}\frac{\|f\|_4^4}{\|f\|_2^4}=\frac{A+B\,T}{c^2}},\quad
 T=\begin{cases}T_+,&6k(n-k)<n(n+1),\\T_-,&6k(n-k)>n(n+1),\\T_+,&6k(n-k)=n(n+1).\end{cases}
\]
The convention in the zero branch is only a convenient choice because \(B=0\); it does **not** assert \(T_+=T_-\).

For \(B>0\), equality holds exactly for coefficient vectors with a single exceptional coordinate, up to permutation and nonzero real scale: \((n-1,-1,\ldots,-1)\). For \(B<0\), equality holds exactly for two-level vectors whose two multiplicities are \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\), with values determined (up to common nonzero scale) by zero sum. For \(B=0\), every nonzero zero-sum coefficient vector attains equality. This last case gives a genuine full-sphere norm resonance, for example at \((n,k)=(8,2)\) or \((8,6)\).

## Assumptions and scope
The probability space is \(X_{n,k}=\{S\subseteq[n]:|S|=k\}\) with uniform measure. Functions and coefficients are real. The first harmonic space \(\mathcal H_1\) consists of \(f_a(S)=\sum_{i\in S}a_i\) with \(\sum_i a_i=0\), and has dimension \(n-1\). Norms \(\|\cdot\|_r\) use uniform probability, not counting measure. The coefficient map is injective in the stated interior range. The phase boundary and equality cases are stated for all such \(n,k\), with no limiting assumptions.

## Proof
**1. Exact moment identity.** Put \(s_j=\sum_{i=1}^n a_i^j\) and \(p_j=(k)_j/(n)_j\) for \(j\le k\), with \(p_j=0\) if \(j>k\). Because \(s_1=0\), simple expansion of the sum of inclusion indicators gives
\[
 \mathbb E f_a^2=(p_1-p_2)s_2=c\,s_2,\qquad
 \mathbb E f_a^4=3(p_2-2p_3+p_4)s_2^2+(p_1-7p_2+12p_3-6p_4)s_4.
\]
The symmetric identities needed for the fourth expansion are
\[
 \sum_{i\ne j}a_i^3a_j=-s_4,\quad
 \sum_{i<j}a_i^2a_j^2=(s_2^2-s_4)/2,\quad
 \sum_i\sum_{\substack{j<\ell\\ j,\ell\ne i}}a_i^2a_ja_\ell=s_4-s_2^2/2,
\]
\[
 \sum_{i<j<\ell<m}a_i a_j a_\ell a_m=(3s_2^2-6s_4)/24.
\]
Substitution and simplification give the displayed \(A,B,c\). Thus the norm problem reduces exactly to maximizing or minimizing \(s_4/s_2^2\) over real zero-sum vectors.

**2. Exact extremal coefficient kurtoses.** On the compact smooth manifold \(\{a\in\mathbb R^n:\sum_i a_i=0,\ \sum_i a_i^2=1\}\), any extremizer of \(s_4\) satisfies \(4a_i^3-2\lambda a_i-\mu=0\). There are at most three distinct coordinate values.

If there are two values, with respective multiplicities \(h,n-h\), the constraints give
\[
 s_4=\frac{n}{h(n-h)}-\frac3n.
\]
This is largest at \(h=1\) or \(n-1\), and smallest at the two most balanced multiplicities. Write these two values as \(T_+\) and \(T_-\).

To exclude an unaccounted three-value extremum, let its distinct coordinates be \(u<v<w\), of multiplicities \(p,r,q\). Since they are roots of the cubic with no quadratic term, \(u+v+w=0\). The constrained Hessian has diagonal entries \(F'(a_i)\) for \(F(x)=4(x-u)(x-v)(x-w)\). Its signs on \(u,v,w\) are respectively positive, negative, positive. At a local maximum, swapping two equal copies of either outside value is an admissible tangent variation with strictly positive Hessian, hence each outside value appears once: \(p=q=1\). The zero-sum constraint then gives \((n-3)v=0\); since \(n\ge4\), \(v=0\) and \(u=-w\). This configuration has \(s_4=1/2<T_+\), so cannot be globally maximal.

At a local minimum, two equal copies of \(v\) would give a tangent direction with strictly negative Hessian, so \(r=1\). Put \(\alpha=v-u>0\), \(\beta=w-v>0\), with \(p+q=n-1\ge3\). Set the tangent perturbation to \(-\beta/p\) on the \(u\)-coordinates, \(\alpha+\beta\) on the unique \(v\)-coordinate, and \(-\alpha/q\) on the \(w\)-coordinates. Both linearized constraints vanish. Its constrained Hessian quadratic form is
\[
 4\alpha\beta(\alpha+\beta)\left(\frac\beta p-(\alpha+\beta)+\frac\alpha q\right)<0,
\]
because \(p,q\ge1\) and at least one is at least two. This contradicts local minimality. Thus every global maximum and minimum is two-valued, with all equality cases as stated.

**3. Phase sign and sharpness.** Since \(s_2>0\), the exact ratio is \((A+B(s_4/s_2^2))/c^2\). The coefficient \(B\) has the sign of \(n(n+1)-6k(n-k)\), and substitution of \(T_+\) or \(T_-\) gives the formula. The stated vectors belong to \(\mathcal H_1\) and attain the value, proving both sharpness and exhaustiveness. When \(B=0\), the fourth-to-second ratio is independent of all coefficient directions, so equality holds throughout the subspace.

## Verification
The included standalone script `check_johnson4.py` uses only Python standard-library exact fractions. It enumerates all \(k\)-subsets for \(4\le n\le14\), \(2\le k\le n-2\), verifies the second/fourth moment identities for all \(n-1\) two-level coefficient patterns, checks every pattern against the proposed sharp bound, and confirms attaining configurations in both odd and even dimensions. The aggregate checks cover 638 exact moment profiles and sample all three sign regimes. Run: `python check_johnson4.py`. These finite computations are checks of formulas, not a replacement for the global constrained-Hessian proof.

## Relationship to prior work
Filmus's basis paper (2014) gives the slice harmonic decomposition and degree-one setting. Filmus and Mossel (2015), especially their Proposition 5.1 and Lemma 5.2 on hypercontractivity, give nonsharp \(L^r\)-to-\(L^2\) comparisons for low-degree slice functions. Ai, Kuželka, and Pelekis (2025) consider the same zero-sum sample sums but prove tail-probability bounds using majorization rather than this exact fourth-moment embedding norm and its phase-specific optimizer classification. Classical finite-population sampling formulas can imply the coefficient form of the fourth moment; the new assertion is the globally sharp optimization with complete equality cases and the integer phase boundary.

## Limitations
The conclusion is for real coefficients, degree one, uniform Johnson slices, and the fourth moment only. It does not give optimal constants for higher harmonic degrees, other exponents, or nonuniform sampling measures. The originality judgment is bounded by the inspected literature, not a proof of historical uniqueness; a general finite-population moment or extremal-kurtosis result could provide an alternative derivation. Independent mathematical verification has not been performed.

## References
- Yuval Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first publicly submitted 2014-06-01), https://arxiv.org/abs/1406.0142 .
- Yuval Filmus and Elchanan Mossel, *Harmonicity and invariance on slices of the Boolean cube*, arXiv:1507.02713 (first publicly submitted 2015-07-09), https://arxiv.org/abs/1507.02713 .
- Jianhang Ai, Ondřej Kuželka, and Christos Pelekis, *Concentration inequalities for the sum in sampling without replacement: an approach via majorization*, arXiv:2503.20473 (2025), https://arxiv.org/abs/2503.20473 .
