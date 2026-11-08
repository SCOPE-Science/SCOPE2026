# Quartic modular graphs: four-term progressions and the exceptional five-adic obstruction

## Finding

For every integer \(N\ge5\) with \(\gcd(N,6)=1\), consider the graph
\[
G_N=\{(u,u^4):u\in\mathbb Z/N\mathbb Z\}.
\]
An *ordered four-term affine progression* is a sequence of graph points
\[
P_j=(x+jh,(x+jh)^4),\qquad j=0,1,2,3,
\]
whose consecutive differences in \((\mathbb Z/N\mathbb Z)^2\) are equal. Repeated vertices are permitted. Write \(A_4(N)\) for the number of parameter pairs \((x,h)\) giving such a progression and \(A_5(N)\) for the number of those pairs for which the same affine progression also contains \(P_4\). Thus \(A_5(N)\) counts *extendible four-term progressions*, not arbitrary five-tuples with independently chosen steps.

For each \(p^k\parallel N\), set
\[
a_k=\left\lceil\frac{k}{4}\right\rceil,\quad
b_k=\left\lceil\frac{k}{2}\right\rceil,\quad
B_p(k)=p^{k+\lfloor k/2\rfloor}
 +(b_k-a_k)(p-1)p^{k+\lfloor k/2\rfloor-1},
\]
and
\[
E_p(k)=
\begin{cases}
4\,5^{3(k-1)/2},&p=5\text{ and }k\equiv1\pmod4,\\
0,&\text{otherwise}.
\end{cases}
\]
Then the complete exact formulas are
\[
\boxed{A_5(N)=\prod_{p^k\parallel N}B_p(k),\qquad
A_4(N)=\prod_{p^k\parallel N}(B_p(k)+E_p(k)).}
\]
In particular the number of nonextendible four-term progressions is
\(A_4(N)-A_5(N)\), and it is positive exactly when \(v_5(N)\equiv1\pmod4\) (with \(v_5(N)>0\)).

There is also a complete local classification. For \(p^k\parallel N\), let
\(y=x+3h/2\) modulo \(p^k\), with \(2^{-1}\) interpreted in that ring; put
\(s=\min\{k,v_p(h)\}\), \(t=\min\{k,v_p(y)\}\), where the truncated valuation of zero is \(k\). The local four-term condition holds precisely in one of two disjoint cases:

1. **Extendible branch:** \(s\ge a_k\) and \(t\ge\max\{0,b_k-s\}\). Every term \((x+jh,(x+jh)^4)\) then lies on the same affine line for all integers \(j\).
2. **Exceptional branch:** \(p=5\), \(k=4s+1\), and \(t\ge s+1\). This is a four-term progression which cannot be extended to five consecutive terms with the same step.

By the Chinese remainder theorem the global progression extends to five, and indeed to every integer index, if and only if the extendible branch holds at each prime-power factor.

Consequently **four graph points in an affine progression can be pairwise distinct if and only if \(5\mid N\) or \(N\) is not squarefree**. Five pairwise distinct consecutive points in an affine progression exist if and only if \(N\) is not squarefree. In either count, exactly \(N\) pairs have the zero step \(h=0\); thus the number of distinct-vertex four-term progressions is \(A_4(N)-N\) and the number of distinct-vertex extendible progressions is \(A_5(N)-N\).

For instance, \(A_4(5)=9\) and \(A_5(5)=5\), giving exactly four exceptional progressions; \(A_4(25)=A_5(25)=125\); and \(A_4(3125)=203125\), \(A_5(3125)=140625\), giving \(62500\) exceptional progressions.

## Assumptions and scope

All congruences are taken in \(\mathbb Z/N\mathbb Z\). We require \(N\ge5\) and \(\gcd(N,6)=1\), so each prime divisor is at least five and both \(2\) and \(12\) are units. The object is the *entire polynomial graph*, not the image set of fourth powers alone. Every ordered progression is counted once by its starting abscissa \(x\) and first-coordinate step \(h\). For such moduli, a nonzero step has additive order at least five, so its first four and first five abscissas are all distinct.

## Proof

**1. Exact differences.** For an arbitrary starting abscissa \(x\), let \(y=x+3h/2\). Direct expansion gives the two consecutive second differences
\[
\begin{aligned}
(x+2h)^4-2(x+h)^4+x^4
 &=h^2(12y^2-12yh+5h^2),\\
(x+3h)^4-2(x+2h)^4+(x+h)^4
 &=h^2(12y^2+12yh+5h^2).
\end{aligned}
\]
Because \(2\) is invertible, both vanish modulo \(N\) if and only if
\[
\boxed{N\mid h^2(12y^2+5h^2),\qquad N\mid 12h^3y.}\tag{1}
\]
This equivalence includes zero and nonunit steps.

**2. Exhaustive local valuation branches.** Fix a prime \(p\ge5\) and exponent \(k\ge1\). Use valuations truncated at \(k\), and write \(s=v_p(h)\), \(t=v_p(y)\) in this truncated sense. If \(4s\ge k\) and \(t\ge\lceil k/2\rceil-s\), then
\(2s+2t\ge k\). Also \(3s+t\ge k\): if \(t\ge s\) this follows from \(4s\ge k\), while if \(t<s\) it follows from \(3s+t>2s+2t\ge k\). Both divisibilities in (1) follow. Conversely, if \(4s\ge k\) but \(t<\max(0,\lceil k/2\rceil-s)\), then necessarily \(t<s\). The first expression in (1) has valuation exactly \(2s+2t<k\), since the two summands have different valuations. Hence for \(4s\ge k\), the first branch is necessary and sufficient.

Suppose instead that \(4s<k\). The second condition in (1), since \(12\) is a unit, forces \(3s+t\ge k\), hence \(t>s\). If \(p\ge7\), then \(5\) is a unit, so the two summands in \(h^2(12y^2+5h^2)\) have valuations \(2s+2t\) and \(4s\) with the latter strictly smaller. This makes (1) impossible. For \(p=5\) they have valuations \(2s+2t\) and \(4s+1\), with the latter strictly smaller because \(t>s\). The first condition is then equivalent to \(k\le4s+1\); combined with \(k>4s\), this gives \(k=4s+1\), and the second condition is equivalent to \(t\ge s+1\). Thus the exceptional branch is exhaustive, and its intersection with the first branch is empty.

**3. Extension criterion.** In the first branch, \(4s\ge k\), \(2s+2t\ge k\), and \(3s+t\ge k\). Expanding about \(y\), the coefficients of the quadratic, cubic, and quartic powers of the index in
\[
(y+jh)^4=y^4+4y^3hj+6y^2h^2j^2+4yh^3j^3+h^4j^4
\]
therefore all vanish modulo \(p^k\). The graph points form one affine progression for every integer \(j\). On the exceptional branch, the fourth finite difference is
\[
\Delta_h^4(u^4)=24h^4,
\]
whose valuation is exactly \(4s=k-1\), because \(p=5\) and \(24\) is a unit. Five consecutive graph points cannot lie in an affine progression, since the fourth finite difference of an affine function is zero. The same difference also shows that any four-term progression extending to five must have \(4s\ge k\); by step 2 it is then in the first branch. This proves the local and global extension statements.

**4. Exact counting.** Write \(a=\lceil k/4\rceil\) and \(b=\lceil k/2\rceil\). For \(s\ge b\), there are \(p^{k-b}\) possible steps and all \(p^k\) values of \(y\) are allowed, contributing \(p^{k+\lfloor k/2\rfloor}\) extendible pairs. For each \(a\le s<b\), exactly \((p-1)p^{k-s-1}\) steps have valuation \(s\); the allowed \(y\) values are the \(p^{k-b+s}\) multiples of \(p^{b-s}\). Each such valuation stratum contributes \((p-1)p^{k+\lfloor k/2\rfloor-1}\). Summing the \(b-a\) strata gives \(B_p(k)\).

The exceptional case occurs only when \(p=5\) and \(k=4s+1\). There are \(4\cdot5^{k-s-1}\) possible steps of valuation \(s\), and \(5^{k-s-1}\) values of \(y\) divisible by \(5^{s+1}\). Their product is \(4\cdot5^{2k-2s-2}=4\cdot5^{3(k-1)/2}=E_5(k)\). This yields both prime-power factors. The Chinese remainder theorem gives multiplicativity and all displayed formulas.

**5. Existence and distinctness.** For \(k=1\), \(B_p(1)=p\) and \(E_p(1)=4\) exactly at \(p=5\), so the sole extendible step is zero, with a nonzero exceptional step possible only at five. For every \(k\ge2\), \(B_p(k)>p^k\): choose a nonzero step divisible by \(p^{\lceil k/2\rceil}\). Consequently a nonzero four-term step exists globally precisely when \(5\mid N\) or a prime square divides \(N\), while a nonzero extendible step exists precisely when a prime square divides \(N\). If \(h\ne0\pmod N\), its additive order is divisible by some prime \(p\ge5\); hence the first five abscissas are distinct. This completes the proof.

## Verification

The file `verify.py` implements direct modular second-difference checks and independently evaluates the valuation classification and the prime-power product formulas. It exhaustively tests \(49\) coprime-to-six composite and prime moduli between \(5\) and \(150\), involving \(375049\) starting-abscissa/step pairs; it also exhaustively checks the prime powers \(125,625,343,121,169,289\), and makes targeted and randomized checks at \(3125\), including explicit nonextendible examples. Run with `python3 verify.py` from the directory containing that file. All tests use exact integers. Finite checks corroborate the algebraic proof, which is valid at every specified modulus.

## Relationship to prior work

Cook and Magyar (2010 preprint; 2012 publication) prove quantitative existence of progressions with polynomially constrained gaps in dense subsets of high-dimensional prime-field spaces; their paper also explains the importance of polynomial finite differences in related questions. Their conditions concern homogeneous polynomial maps and restricted differences, not exact four-term progressions *inside* a one-dimensional quartic graph over rings with prime-power nilpotents. Green and Tao (2005 preprint; later journal publication) study four-term progression avoidance and density in finite-field vector spaces, rather than the exact all-modulus classification here. Aggregate additive energy of quartic graphs is a distinct invariant; knowing its total does not determine the number or extendibility of equally spaced four-point configurations. The present statement does not assert absolute historical priority.

## Limitations

The formulas exclude moduli divisible by \(2\) or \(3\), where \(2\) or \(12\) is not invertible and new local cases arise. Counts include repeated-vertex progressions only through the zero-step contribution, which is explicitly removed in the distinct-vertex formulas. The theorem concerns consecutive points with a common affine step, not arbitrary collinear quadruples or arithmetic progressions among fourth-power *values* alone. An unlocated earlier specialized local-congruence treatment remains a bibliographic possibility.

## References

- Brian Cook and Ákos Magyar, *On restricted arithmetic progressions over finite fields*, arXiv:1011.5302, first posted 2010-11-24; *Online Journal of Analytic Combinatorics* 7 (2012). https://arxiv.org/abs/1011.5302 ; https://combinatorialpress.com/article/ojac/vol7/Cook_2012.pdf
- Ben Green and Terence Tao, *New bounds for Szemerédi's theorem, I: Progressions of length 4 in finite field geometries*, arXiv:math/0509560, first posted 2005-09-23; *Proceedings of the London Mathematical Society* 98 (2009), 365–392. https://arxiv.org/abs/math/0509560
