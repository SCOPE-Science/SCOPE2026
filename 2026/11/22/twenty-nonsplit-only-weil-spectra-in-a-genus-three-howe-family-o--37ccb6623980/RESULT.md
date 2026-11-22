# Twenty nonsplit-only Weil spectra in a genus-three Howe family over \(\mathbb F_{11}\)

## Finding
Let \(k=\mathbb F_{11}\). For every ordered pair \((M,N)\in k^2\) with
\[
\Delta(M,N)=(N+2M+2)(N-2M+2)(M^2-4N+8)\ne0,
\]
consider the smooth projective curve
\[
C_{M,N}:\quad y^2=x^8+Mx^6+Nx^4+Mx^2+1.
\]
There are exactly **91** smooth coefficient-marked curves in this family. Their Jacobians realize exactly **28 distinct Weil polynomials** over \(k\). Writing \(\delta=M^2-4N+8\), exactly **36** of the smooth coefficients have square \(\delta\), corresponding to two distinct quartic factors defined separately over \(k\); the remaining **55** have nonsquare \(\delta\), corresponding to conjugate quartic factors over \(\mathbb F_{121}\). The split locus exhibits **8** distinct Weil polynomials, the nonsplit locus **23**; exactly **3** occur on both loci. Consequently, **20 of the 28 Weil polynomials occur exclusively on the nonsplit quartic-factor locus**.

For each smooth coefficient pair there are three explicitly defined elliptic-quotient traces \(t_0,t_+,t_-\in\mathbb Z\); the complete zeta numerator is
\[
L_{C_{M,N}}(T)=\prod_{j\in\{0,+,-\}}(1-t_jT+11T^2).
\]
The following exhaustive spectrum gives sorted triples \((t_1,t_2,t_3)\), and numbers of marked coefficients with square or nonsquare \(\delta\) (not isomorphism classes):

| Elliptic trace triple | Split \(\Delta\) | Nonsplit \(\Delta\) | Total |
|---|---:|---:|---:|
| \((-6,-6,0)\) | 0 | 1 | 1 |
| \((-6,-4,-2)\) | 0 | 2 | 2 |
| \((-6,-4,2)\) | 0 | 2 | 2 |
| \((-6,-2,0)\) | 0 | 4 | 4 |
| \((-6,-2,4)\) | 0 | 2 | 2 |
| \((-6,0,2)\) | 0 | 2 | 2 |
| \((-6,0,6)\) | 0 | 2 | 2 |
| \((-6,2,4)\) | 0 | 2 | 2 |
| \((-4,-4,-4)\) | 2 | 0 | 2 |
| \((-4,-4,0)\) | 5 | 0 | 5 |
| \((-4,-4,4)\) | 4 | 0 | 4 |
| \((-4,-2,-2)\) | 0 | 1 | 1 |
| \((-4,-2,2)\) | 0 | 2 | 2 |
| \((-4,-2,6)\) | 0 | 2 | 2 |
| \((-4,0,0)\) | 5 | 6 | 11 |
| \((-4,0,4)\) | 10 | 0 | 10 |
| \((-4,2,2)\) | 0 | 1 | 1 |
| \((-4,4,4)\) | 3 | 1 | 4 |
| \((-2,-2,0)\) | 0 | 2 | 2 |
| \((-2,-2,4)\) | 0 | 1 | 1 |
| \((-2,0,2)\) | 0 | 8 | 8 |
| \((-2,0,6)\) | 0 | 2 | 2 |
| \((-2,4,6)\) | 0 | 2 | 2 |
| \((0,0,4)\) | 4 | 3 | 7 |
| \((0,2,2)\) | 0 | 2 | 2 |
| \((0,2,6)\) | 0 | 4 | 4 |
| \((0,4,4)\) | 3 | 0 | 3 |
| \((2,2,4)\) | 0 | 1 | 1 |

In particular, the respective frequencies of \(4,8,12,16,20,24\) rational points on \(C_{M,N}\) over \(\mathbb F_{11}\) are \(10,15,26,23,12,5\). The maximum **24** is attained precisely for
\[
(M,N)=(1,10),(2,10),(5,4),(6,2),(8,5),
\]
three of which lie on the nonsplit quartic-factor locus. The \(11\)-rank frequency distribution for ranks \(1,2,3\) is \(18,45,28\); there is no rank-zero smooth coefficient pair in this marked family.

## Assumptions and scope
All coefficients and Frobenius traces are over the prime field \(k=\mathbb F_{11}\). The split or nonsplit distinction refers **only** to the two reciprocal monic quartic factors of the octic branch polynomial, not to splitting of the Jacobian into elliptic isogeny factors. In both cases the Jacobian is isogenous over \(k\) to a product of three elliptic curves. No claim is made about abstract curve isomorphism classes, all field forms, all genus-three Howe curves, or any universal maximum among genus-three curves.

Put \(s=x^2\). Over an algebraic closure the branch octic factors as
\[
(x^4-a x^2+1)(x^4-b x^2+1),\qquad a+b=-M,\quad ab=N-2.
\]
For \(a\ne b\) and \(a,b\ne\pm2\), its eight branch roots are pairwise distinct, giving a smooth genus-three double cover. The three factors of \(\Delta\) are precisely the equations for \(a=\pm2\), \(b=\pm2\), and \(a=b\); thus the stated discriminant condition is necessary and sufficient for geometric smoothness. Every smooth fiber has two rational points at infinity, since the branch octic is monic of even degree.

## Proof
**Elliptic decomposition.** The three involutions \(x\mapsto-x\), \(x\mapsto1/x\), \(x\mapsto-1/x\), with \(y\mapsto y/x^4\) for the last two, generate a Klein four action on the smooth genus-three curve. Their three elliptic quotients have affine models
\[
\begin{aligned}
E_0 &: v^2=u^4+Mu^3+Nu^2+Mu+1,\\
E_+ &: v^2=u^4+(M-4)u^2+N-2M+2,\\
E_- &: v^2=u^4+(M+4)u^2+N+2M+2.
\end{aligned}
\]
The quotient maps are respectively \((u,v)=(x^2,y)\), \((x+x^{-1},y/x^2)\), and \((x-x^{-1},y/x^2)\). These three degree-two genus-one quotients are smooth on the stated discriminant-open locus, and each has two rational points at infinity. On holomorphic differentials, the three nontrivial characters occur exactly once: the spans of \(x\,dx/y\), \((1+x^2)dx/y\), and \((1-x^2)dx/y\). The trivial character is absent; the full Klein-four quotient has genus zero. Since \(2\ne11\), the character projectors decompose rational \(\ell\)-adic first cohomology into the three two-dimensional elliptic quotient summands for any auxiliary \(\ell\ne2,11\). Hence the displayed zeta numerator factorization is valid over \(k\), not merely geometrically.

**Exact quotient counts.** For each of the three quartic right-hand sides \(Q_j(u)\), define the quadratic character \(\chi(0)=0\), \(\chi(v)=1\) for nonzero squares, and \(-1\) for nonsquares in \(k\). Since each quartic model has two rational points at infinity,
\[
\#E_j(k)=13+\sum_{u\in k}\chi(Q_j(u)),\qquad
 t_j=12-\#E_j(k)=-1-\sum_{u\in k}\chi(Q_j(u)).
\]
The nonzero squares modulo \(11\) are \(\{1,3,4,5,9\}\). Evaluating these three **eleven-term** character sums for each smooth \((M,N)\) produces the 28-row spectrum and the full 91-row parameter table in `spectrum_28.csv` and `parameters_91.csv`. For each row, the direct curve point count independently satisfies
\[
\#C_{M,N}(k)=13+\sum_{x\in k}\chi(x^8+Mx^6+Nx^4+Mx^2+1)=12-(t_0+t_++t_-).
\]
All 91 rows were enumerated, not sampled; the attached verifier recomputes every sum from first principles.

**Completeness and Galois descent.** A nonsmooth pair lies on one of the two distinct lines \(N=\pm2M-2\) or the parabola \(N=(M^2+8)/4\). Over \(k\), the three eleven-point loci have three pairwise intersection points, no triple intersection; therefore they exclude \(33-3=30\) pairs, leaving \(121-30=91\) smooth pairs. Writing \(\delta=(a-b)^2\), square nonzero \(\delta\) is equivalent to two distinct coefficients \(a,b\in k\setminus\{\pm2\}\). They give \(\binom{9}{2}=36\) unordered pairs, each determining a unique \((M,N)\). For nonsquare \(\delta\), \(a,b\) are a conjugate pair in \(\mathbb F_{121}\setminus k\), providing \((121-11)/2=55\) unordered pairs. The lists therefore exhaust the entire smooth marked base, and their 28 distinct trace multisets determine all isogeny types. Direct inspection of the exact finite arrays yields eight split types, 23 nonsplit types and a three-type intersection. Unique factorization of rational polynomials \(\prod(1-t_jT+11T^2)\) identifies precisely the sorted elliptic trace multisets, since the discriminants \(t_j^2-44\) are negative, and these monic-in-constant quadratic Weil factors are irreducible over \(\mathbb Q\).

For a genus-one curve over \(\mathbb F_{11}\), its \(11\)-rank is one if its trace is nonzero modulo \(11\), and zero otherwise. The displayed isogeny decomposition therefore also yields the indicated genus-three \(11\)-rank distribution; the quotient isogeny is of degree prime to \(11\).

## Verification
Run `python3 verify_howe11.py` with Python 3 and the two adjacent CSV files. The verifier exhausts the \(11^2\) coefficient pairs, checks geometric smoothness through the exact discriminant, recomputes all three elliptic traces and the full two-way partition, checks all 28 spectrum frequencies and all 91 parameter records, and independently counts rational points on the original octic model. It also counts all 91 curves directly over \(\mathbb F_{121}\) using two independently constructed representations \(\mathbb F_{11}[w]/(w^2-2)\) and \(\mathbb F_{11}[w]/(w^2-6)\); both point-count sequences equal \(122-\sum_j(t_j^2-22)\), the independent quadratic-extension prediction of elliptic factors. This verifies the first two extension degrees but does not replace the character-decomposition proof for all extensions. The expected identifier is `HOWE_F11_SPLIT_NONSPLIT_WEIL_VERIFIED`; the script additionally prints the exact 28-row spectrum and maximizers.

## Relationship to prior work
Ohashi (2021), Section 3 and Theorem 1.1, gives the genus-three hyperelliptic Howe model, Klein-four quotients and results on the superspecial/maximal subfamily; their existence and splitting are not new claims here. Moriya–Kudo (2022) give general genus-three arithmetic and superspecial enumeration algorithms, but not this complete rational-coefficient Weil census. Borówka–Shatsila (2023) study genus-three curves with involutions and Prym geometry; their moduli results do not determine this characteristic-eleven arithmetic table.

The closest recorded arithmetic census is the five-spectrum classification of 42 **ordered split-factor** Howe coefficient pairs over \(\mathbb F_9\), a different base field and a restricted parameter presentation. Its generic quotient method is the same but does not imply the current \(\mathbb F_{11}\) 28-spectrum, especially the 20 isogeny types not realized by separately rational quartic factors. A separate characteristic-eleven dihedral Hasse-divisor computation treats only the one-parameter subfamily \(M=0\) and its \(p\)-rank stratification, not Weil polynomials across the two-parameter rational base. Neither an unaltered change of notation nor these known structural theorems supplies the 91-entry arithmetic table. A literature and mathematical-record search located no published table with these complete quantities; this is not a proof of global priority.

## Limitations
The tables count coefficient-marked **smooth** equations, not distinct \(\mathbb F_{11}\)-isomorphism classes, geometric isomorphism classes or field twists. The split/nonsplit distinction belongs to one chosen reciprocal-factor presentation and need not be an invariant of unmarked curves. While the zeta numerators determine extension-field point counts, they do not determine canonical isomorphism classes, Newton polygons beyond the \(p\)-ranks given, or explicit endomorphism rings. A separately indexed older computation may have tabulated equivalent arithmetic spectra. The complete finite computations are reproducible, but independent mathematical audit has not been performed.

## References
1. R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152, first publicly submitted 2021-12-21, https://arxiv.org/abs/2112.11152 (model and elliptic quotients, Section 3).
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926, first posted 2022-09-07, https://arxiv.org/abs/2209.02926 (arithmetic and superspecial algorithms).
3. P. Borówka and A. Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map*, arXiv:2308.07038, first posted 2023-08-14, https://arxiv.org/abs/2308.07038 (moduli and involutions).
4. *Five Hasse–Weil spectra for marked genus-three Howe curves over \(\mathbb F_9\)*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-five-hasse-weil-spectra-for-marked-genus-three-howe-curves-over--1630154b90d2.
5. *The characteristic-eleven Hasse divisor on the dihedral genus-three hyperelliptic pencil*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-characteristic-eleven-hasse-divisor-on-the-dihedral-genus-th--0d59fdaeb507.
