# Three moments suffice for dyadic two-point Fourier geometry

## Finding
For every integer \(k\ge2\), put \(N=2^k\), \(R=\mathbb Z/N\mathbb Z\), and define the cubic moment curve
\[
C_k=\{(u,u^2,u^3):u\in R\}\subset R^3.
\]
For a target \((s,t_2,t_3)\in R^3\), let \(r_k(s,t_2,t_3)\) count ordered pairs \((u,v)\in R^2\) for which
\[
u+v=s,\qquad u^2+v^2=t_2,\qquad u^3+v^3=t_3.
\]
**Complete pointwise convolution law.** Set \(Q=N/2\). For odd \(s\), define the uniquely determined residue \(w=(s^3-t_3)(3s)^{-1}\in R\). Then
\[
r_k(s,t_2,t_3)=\begin{cases}2,&w\equiv0\pmod2\text{ and }t_2=s^2-2w\text{ in }R,\\0,&\text{otherwise}.\end{cases}
\]
For even \(s\), if \(s^2-t_2\) is odd then the count is zero. Otherwise take the unique residue \(w\in\mathbb Z/Q\mathbb Z\) satisfying \(2w=s^2-t_2\) in \(R\). If \(t_3\ne s^3-3sw\) in \(R\), the count is zero. If the equality holds, choose either half \(h\in R\) with \(2h=s\), and put \(z=h^2-w\in\mathbb Z/Q\mathbb Z\). Then
\[
\boxed{r_k(s,t_2,t_3)=2\#\{a\pmod Q:a^2=z\pmod Q\}.}
\]
This is independent of the chosen half and representative of \(w\).

**Explicit fiber histogram.** Write \(m=k-1\). There are exactly \(N^2/4\) positive targets with odd first coordinate, all of multiplicity \(2\). Each even first coordinate has one target associated to the zero square modulo \(2^m\), with multiplicity \(2^{1+\lfloor m/2\rfloor}\). For each integer \(0\le j\le\lfloor(m-1)/2\rfloor\), set \(\ell=m-2j\) and
\[
U_\ell=\begin{cases}1,&\ell=1,2,\\2^{\ell-3},&\ell\ge3,\end{cases}\qquad
R_\ell=\begin{cases}1,&\ell=1,\\2,&\ell=2,\\4,&\ell\ge3.\end{cases}
\]
For each even first coordinate there are \(U_\ell\) additional targets of multiplicity \(2^{j+1}R_\ell\). When different strata give the same multiplicity, their target counts are added. All other targets have zero representations. Hence the exact twofold sumset size and additive energy are
\[
\boxed{|C_k+C_k|=\begin{cases}(7N^2+20N)/24,&k\text{ even},\\(7N^2+16N)/24,&k\text{ odd},\end{cases}\qquad E(C_k)=kN^2.}
\]
In particular \(|C_k+C_k|/N^2\to7/24\), while \(E(C_k)/|C_k|^2=k\).

**Sharp moment stabilization.** For every integer \(d\ge3\), the ordered pairs with identical first \(d\) power sums have exactly the same equivalence classes as those with identical first three power sums. Thus their complete two-sum representation multiset is unchanged by adjoining any number of coordinates \(u^4,u^5,\ldots\). Degree three is minimal for every \(k\ge2\): the degree-two moment map has strictly larger collision classes.

With the unweighted Fourier sum
\[
F_k(a,b,c)=\sum_{u\pmod N}\exp\!\left(\frac{2\pi i(au+bu^2+cu^3)}N\right),
\]
finite-group orthogonality gives the exact constant-input fourth moment
\[
\boxed{\frac1{N^3}\sum_{a,b,c\pmod N}|F_k(a,b,c)|^4=kN^2.}
\]
This is **not** a sharp extension norm for arbitrary coefficients.

## Assumptions and scope
All arithmetic on targets and moments is modulo \(N=2^k\). The theorem is for every integer \(k\ge2\) and ordered input pairs, with counting measure on \(C_k\), the unnormalized exponential sum \(F_k\), and normalized averaging \(N^{-3}\) over its three Fourier variables. Congruences modulo \(Q=N/2\) have the ordinary integer-residue interpretation. There are no omitted assumptions on either first-coordinate parity class. The modulus \(N=2\) is separately checked by the program but excluded from the displayed two-branch sumset formula.

## Proof
Write \(s=u+v\), \(w=uv\), and \(p_j=u^j+v^j\). The identities
\[
p_1=s,\qquad p_2=s^2-2w,\qquad p_3=s^3-3sw,
\]
and the recurrence \(p_0=2\), \(p_1=s\), \(p_j=sp_{j-1}-wp_{j-2}\) for \(j\ge2\), hold over every commutative ring.

If \(s\) is odd, \(3s\) is a unit in \(R\); therefore \(p_3\) fixes \(w\) modulo \(N\). The quadratic \(u(s-u)=w\) has two roots modulo \(2\) precisely when \(w\) is even, namely the residues \(0,1\), and the derivative \(s-2u\) is odd at either root. Each root lifts uniquely to \(R\). This proves the odd-\(s\) pointwise formula, including its zero conditions.

If \(s\) is even, \(p_2\) fixes \(w\) modulo \(Q\), and \(3s\) is even, so changing \(w\) by \(Q\) does not affect \(p_3\). The entire three-moment data are therefore fixed by \(s\) and \(w\pmod Q\). For \(s=2h\), complete the square:
\[
u(s-u)=h^2-(u-h)^2\pmod Q.
\]
Every solution \(u\pmod Q\) lifts to exactly two values \(u\pmod N\), giving the even-\(s\) formula. Changing \(h\) by \(Q\) does not change \(h^2\pmod Q\).

For completeness, the square-fiber facts used in the histogram are proved as follows. A nonzero square modulo \(2^m\) has even valuation \(2j<m\), and its odd unit factor must be a unit square modulo \(2^\ell\) with \(\ell=m-2j\). The number of distinct odd unit squares is \(U_\ell\) in the theorem: one for \(\ell=1,2\), and \(2^{\ell-3}\) for \(\ell\ge3\). The squaring homomorphism on odd units has kernel size \(R_\ell\), namely one, two, and four in these three regimes. Lifting the odd factor from modulus \(2^\ell\) to modulus \(2^{m-j}\) introduces \(2^j\) root choices. The zero square has exactly \(2^{\lfloor m/2\rfloor}\) roots. These identities include the low-modulus boundary cases \(m=1,2\), and prove the complete histogram.

There are \(N/2\) odd values of \(s\), each yielding \(N/2\) target values. For each even \(s\), the attainable target set is in bijection with square residues modulo \(Q\). The number of such residues is
\[
S_m=\begin{cases}(4^{(m-1)/2}+5)/3,&m\text{ odd},\\(2\cdot4^{m/2-1}+4)/3,&m\text{ even}.\end{cases}
\]
Indeed this is one for zero, plus the geometric sum of the \(U_\ell\) over the possible even valuations. Thus \(|C_k+C_k|=N^2/4+(N/2)S_{k-1}\), which simplifies to the stated parity-dependent formulas.

For the energy, fix \(s\) and compare two ordered decompositions \((u,s-u)\) and \((v,s-v)\). Equality of their three moment sums is equivalent to
\[
(u-v)(s-u-v)\equiv0\pmod N\quad(s\text{ odd}),
\]
or to the same congruence modulo \(Q\) when \(s\) is even. For odd \(s\), exactly one factor is odd, giving precisely \(2N\) ordered choices of \((u,v)\): either \(u=v\) or \(u+v=s\), and the alternatives are disjoint.

For even \(s\) and \(k\ge3\), put \(a=u-v\), \(b=s-u-v\). These have the same parity, and each compatible ordered pair \((a,b)\pmod N\) comes from exactly two pairs \((u,v)\pmod N\). Divisibility of \(ab\) by \(Q\ge4\) forces both to be even. Writing \(a=2A\), \(b=2B\), the requirement is \(AB=0\pmod{2^{k-3}}\). Denote by \(Z_r\) the count of such zero-product pairs modulo \(2^r\). One has \(Z_0=1\) and, for \(r\ge1\),
\[
Z_r=2^r+\sum_{j=0}^{r-1}2^{r-j-1}2^j=(r+2)2^{r-1}.
\]
There are \(16\) lifts from each pair modulo \(2^{k-3}\) to \((A,B)\pmod{2^{k-1}}\), and two original \((u,v)\) per lift. Thus for fixed even \(s\) there are \(32Z_{k-3}=2(k-1)N\) colliding choices. At \(k=2\), the modulus \(Q=2\) simply forces both \(a,b\) to be even and yields \(2N\) choices, consistent with the formula \(2(k-1)N\). Summing over \(N/2\) odd and \(N/2\) even values of \(s\) gives \(E(C_k)=kN^2\).

For stabilization, if \(s\) is odd equality through degree three forces equality of \(w\pmod N\); the recurrence then forces equality of every \(p_j\). If \(s\) is even, the two elements of each ordered pair have the same parity, hence every \(p_j\) (including \(p_0=2\)) is even. Equality through degree three forces their \(w\)'s to agree modulo \(Q\). Inducting in the recurrence, the difference in each higher \(p_j\) is a sum of multiples of \(N\) and a multiple of \(Q\) times an even earlier \(p_{j-2}\), so it vanishes modulo \(N\). Conversely equality through higher degrees obviously implies equality through the first three. To prove minimality, for every \(k\ge2\) the pairs \((0,1)\) and \((Q,1-Q)\) have identical first and second power sums modulo \(N\), but their third sums differ by \(Q\ne0\pmod N\).

Finally, orthogonality of additive characters on \(R^3\) expands the normalized fourth power of \(F_k\) into precisely the number of ordered additive quadruples counted by \(E(C_k)\).

## Verification
A standalone, standard-library-only integer checker is included as `check_moment_curve.py`. It enumerates all ordered pairs and compares **each positive convolution fiber** with a separate formula using square-root counts modulo \(N/2\). It exhaustively checks every target, including zero fibers, for \(2\le k\le5\), and verifies sampled zero and positive targets for larger exponents. It independently confirms exact energy and image-size formulas for \(1\le k\le10\), and verifies agreement of power sums through degree nine on all equal-three-moment fibers for \(1\le k\le8\). For \(k\ge2\) it also verifies a degree-two collision split by the third moment. Its success marker is `DYADIC_THREE_MOMENT_STABILIZATION_AND_FULL_FIBERS_PASS`. These finite computations are supporting evidence, not a proof for unbounded \(k\).

## Relationship to prior work
Mockenhaupt and Tao (2002) initiate finite-field restriction and consider characteristic greater than two. Hickman's 2015 thesis, Chapter 4, §4.6, treats Fourier restriction to moment curves over prime-power rings under \(p>n\), and uses Newton–Girard identities under non-zero-divisor hypotheses; the three-dimensional dyadic case falls outside those hypotheses. Hickman and Wright (2018), §7, develops moment-curve restriction and general congruence-solution estimates, but its relevant theorem assumes \(p>n\) and does not state the present complete two-point dyadic convolution, higher-moment stabilization, or explicit sumset law. Known square-root congruence formulas are used as ingredients and are not claimed as discoveries. The new claim concerns their exact aggregate behavior on a fixed natural Fourier surface. Broader local moment-counting or representation-density results could potentially imply the conclusion; exhaustive historical priority has not been established.

## Limitations
Only the prime-power sequence \(N=2^k\) and the twofold additive convolution of this particular moment curve are classified. Nothing here establishes a general sharp Fourier extension bound for arbitrary complex coefficients, higher-fold convolutions, stability estimates, or the extension to arbitrary composite moduli. An independent mathematical audit has not been performed; the proof and exact checker are supplied for scrutiny.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, first arXiv submission 2002-04-18, arXiv:math/0204234, https://arxiv.org/abs/math/0204234.
2. J. Hickman, *Topics in affine and discrete harmonic analysis*, University of Edinburgh PhD thesis, 2015-07-01, Chapter 4 §4.6, https://era.ed.ac.uk/items/29ea5d40-6678-4834-8ac0-2f2278ae7ffd.
3. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176 (first submitted 2018-01-09), Discrete Analysis 2018:11, especially §7, https://arxiv.org/abs/1801.03176.
