# A universal determinant-valuation zeta law for cubic Hankel matrices over finite chain rings

## Finding

Let \(R\) be any finite commutative chain ring with radical \((\pi)\), length \(m\ge 1\), and residue field \(\mathbb F_q\), where \(q\) is an arbitrary prime power. Choose \(a,b,c,d,e\) independently and uniformly in \(R\), and form the three-by-three Hankel matrix

\[
H=\begin{pmatrix}a&b&c\\b&c&d\\c&d&e\end{pmatrix},\qquad
f(H)=ace+2bcd-ad^2-b^2e-c^3.
\]

For \(x\in R\), put \(\nu_\pi(x)=\max\{j\in\{0,\ldots,m\}:x\in(\pi^j)\}\), with \(\nu_\pi(0)=m\). Let \(V=\nu_\pi(f(H))\) and \(u=q^{-1}\). Define the rational formal power series

\[
\boxed{\mathcal Z_q(t)=\frac{(1-u)(1-u^3t)(1-u^5t^2)}{(1-ut)(1-u^3t^2)(1-u^5t^3)}=\sum_{r\ge 0}p_r(q)t^r.}
\]

**Theorem.** For every \(m\ge1\), the complete determinant-valuation distribution is

\[
\Pr(V=r)=p_r(q)\quad(0\le r<m),\qquad
\Pr(V=m)=1-\sum_{r=0}^{m-1}p_r(q).
\]

In particular, the numbers of input quintuples in these strata are the displayed probabilities multiplied by \(q^{5m}\). These counts depend only on \((q,m)\), not on the characteristic or ramification type of \(R\). For example,

\[
\Pr(V\ge1)=q^{-1},\quad
\Pr(V\ge2)=q^{-2}+q^{-3}-q^{-4},\quad
\Pr(V\ge3)=q^{-3}+q^{-4}-q^{-6}
\]

whenever the relevant lengths exist. At a fixed \(q\), the untruncated valuation tail satisfies

\[
\sum_{j\ge r}p_j(q)=(1+q^{-1}+q^{-2})q^{-r}+O_q(q^{-3r/2}).
\]

Thus the singular determinant locus has an exact, characteristic-uniform tower of thickened congruence counts, including the contributions near its rank-one singular locus.

## Assumptions and scope

A finite commutative chain ring has a unique descending chain of ideals \(R\supsetneq(\pi)\supsetneq\cdots\supsetneq(\pi^m)=0\), with \(|R|=q^m\). All formulas apply to every such ring; no assumption that \(R\) is a polynomial quotient or an unramified extension is needed. The formal generating function \(\mathcal Z_q\) specifies a compatible sequence of exact finite-length counts; it does not assert the existence of an infinite complete discrete valuation ring extending an arbitrary \(R\). The notation \(O_q\) allows an implicit constant depending on \(q\) alone.

## Proof

**Step 1: a valuation recurrence for the hyperbolic quadratic determinant.** Consider \(Q(U,V,W)=UW-V^2\) for three independent uniform entries, and let \(\mathcal Q_q(t)\) be its stable valuation generating function. Over \(\mathbb F_q\), the cone \(Q=0\) has exactly \(q^2\) solutions: for \(U\ne0\) choose \(U,V\) and solve for \(W\), giving \((q-1)q\), while for \(U=0\), \(V=0\) and \(W\) is arbitrary, giving \(q\). Its only singular point is the origin, in every characteristic, because \(\nabla Q=(W,-2V,U)\). Consequently the reductions consist of nonsingular values with probability \(1-u\), smooth zero values with probability \(u-u^3\), and the origin with probability \(u^3\).

At a smooth zero, varying a suitable coordinate provides a local bijection with a uniformly random residue parameter, so the subsequent valuation has generating function \(t\mathcal G(t)\), where \(\mathcal G(t)=(1-u)/(1-ut)\) is the valuation series of one uniform coordinate. At the origin, all three entries are in \((\pi)\), so \(Q=\pi^2Q'\), with the reduced coefficient triple independent and uniform in the shorter quotient. Therefore finite-length truncations satisfy

\[
\mathcal Q_q(t)=(1-u)+(u-u^3)t\mathcal G(t)+u^3t^2\mathcal Q_q(t),
\]

and solving in formal power series gives

\[
\mathcal Q_q(t)=\frac{(1-u)(1-u^3t)}{(1-ut)(1-u^3t^2)}.
\]

**Step 2: exact field-level rank stratification of the cubic.** Over \(\mathbb F_q\), the equation \(f(H)=0\) has \(q^4\) solutions. If \(a\ne0\), the invertible triangular change of variables

\[
U=c-b^2/a,\qquad V=d-bc/a,\qquad W=e-c^2/a
\]

satisfies \(f(H)=a(UW-V^2)\), so this case contributes \((q-1)q^3\) zeros. If \(a=0,b\ne0\), \(f=-b^2e+2bcd-c^3\) has exactly one solution in \(e\) for each \((b,c,d)\), contributing \((q-1)q^2\). Finally, if \(a=b=0\), the equation is \(-c^3=0\), so \(c=0\) and there are \(q^2\) choices for \((d,e)\). The total is \(q^4\).

The field-level zero matrices of rank at most one number \(q^2\). For \(a\ne0\), rank one forces \((a,b,c,d,e)=(a,b,b^2/a,b^3/a^2,b^4/a^3)\), giving \((q-1)q\) nonzero matrices. For \(a=0\), rank at most one forces \(b=c=d=0\) and permits arbitrary \(e\), giving \(q-1\) further nonzero rank-one matrices and the zero matrix. Thus the four residue strata have probabilities

\[
\begin{array}{c|c}
\text{residue type}&\text{probability}\\\hline
\det H\ne0&1-u\\
\operatorname{rank}H=2&u-u^3\\
\operatorname{rank}H=1&u^3-u^5\\
H=0&u^5.
\end{array}
\]

**Step 3: normal forms in each singular stratum.** Every rank-two zero is a smooth point of \(f=0\) over every characteristic. Indeed, with \(a\ne0\), it reduces to a nonzero zero of \(Q\); with \(a=0,b\ne0\), \(\partial f/\partial e=-b^2\) is nonzero; with \(a=b=0\), the zero condition implies \(c=0\), and rank two entails \(d\ne0\), so \(\partial f/\partial a=ce-d^2=-d^2\ne0\). Therefore smooth-zero lifts have valuation series \(t\mathcal G(t)\).

At a nonzero rank-one residue, at least one of the end entries \(a,e\) is a unit. Reversing rows and columns if necessary makes \(a\) a unit. The displayed Schur-complement coordinates are then an invertible triangular coordinate transformation over \(R\); the residue rank-one condition forces \(U,V,W\in(\pi)\), and the determinant is the unit \(a\) times \(\pi^2\) times a uniformly distributed quadratic \(Q'\). Its conditional valuation series is \(t^2\mathcal Q_q(t)\). At the all-zero residue, the degree-three homogeneity of \(f\) gives \(f=\pi^3f'\), with uniform shorter-ring coefficients, contributing \(t^3\mathcal Z_q(t)\). This produces the exact truncated recurrence

\[
\mathcal Z_q(t)=(1-u)+(u-u^3)t\mathcal G(t)+(u^3-u^5)t^2\mathcal Q_q(t)+u^5t^3\mathcal Z_q(t).
\]

Substitution of the formula for \(\mathcal Q_q\) and simplification gives the boxed rational expression. All recurrence arguments hold modulo each finite power of \(\pi\); equality of coefficients below the truncation level proves the asserted finite-ring counts. The final stratum is the remaining probability mass, because \(V=m\) precisely when \(f(H)=0\) in \(R\). This proves universality.

**Step 4: tail.** For fixed \(q\), the unique nearest pole of \(\mathcal Z_q(t)\) to the origin is the simple pole at \(t=u^{-1}\), with principal-part coefficient \(1-u^3\). The other poles have modulus at least \(u^{-3/2}\). Therefore \(p_r(q)=(1-u^3)u^r+O_q(u^{3r/2})\), and summing gives the tail formula above.

## Verification

The standalone standard-library program `checks/check_hankel.py` evaluates the rational generating series by exact rational coefficient division and independently enumerates every five-entry Hankel matrix over the following ten rings: \(\mathbb Z/2\), \(\mathbb Z/4\), \(\mathbb Z/8\), \(\mathbb Z/16\), \(\mathbb Z/3\), \(\mathbb Z/9\), \(\mathbb Z/5\), \(\mathbb F_2[t]/(t^2)\), \(\mathbb F_3[t]/(t^2)\), and \(\mathbb F_4[t]/(t^2)\). For the last ring, the field is represented as \(\mathbb F_2[z]/(z^2+z+1)\). Each complete histogram agrees, including the exhaustive \(16^5=1{,}048{,}576\)-tuple enumeration in the final case. See `checks/verification_output.txt` for the observed fractions. These finite checks test the proof and are not offered as an infinite-family certificate.

## Relationship to prior work

Comer and Kaltofen's work on the Berlekamp–Massey algorithm determines the classical finite-field singularity count for arbitrary-size Hankel matrices and related rank profiles, hence covers the reduction modulo \(\pi\) but not the complete valuation spectrum over longer chain rings. Ballico and Elia study finite-field determinantal varieties of a structured Hankel family; their 28 April 2014 public article establishes an archival connection to rank geometry without asserting the present congruence tower. Doan's 2026 treatment gives local **topological** zeta functions of generic catalecticant determinantal varieties and a general local-rank reduction, substantially overlapping the geometry used above. In the square \(3\)-by-\(3\) case, replacing \(t\) by \(q^{-s}\) in the boxed formula and formally letting \(q\to1\) gives the established topological expression

\[
\frac{(s+3)(2s+5)}{(s+1)(2s+3)(3s+5)}.
\]

This consistency is not an identification of the full arithmetic series with a result of that article: a topological specialization does not recover the finite-field-size-dependent coefficients or the mixed-characteristic finite-ring universality. Related published determinations of four-by-four Hankel determinant fibers over fields concern a different matrix size and no higher congruence length.

## Limitations

The theorem addresses determinant valuations only, not individual nonzero determinant fibers or full Smith forms. It does not extend the displayed formula to arbitrary non-chain local rings. Literature precedence remains qualified because an unindexed arithmetic-zeta derivation or an application of a more general p-adic integration theorem may imply the same formula. The same-author scientific review is not an independent audit.

## References

1. M. T. Comer and E. L. Kaltofen, *On the Berlekamp/Massey Algorithm and Counting Singular Hankel Matrices over a Finite Field*, preprint dated 14 June 2011, https://users.cs.duke.edu/~elk27/bibliography/10/CoKa10.pdf (Sections 1–3 on field singularity and rank-profile counts).
2. E. Ballico and M. Elia, *On Determinantal Varieties of Hankel Matrices*, **Algebra** (2014), Article 970157, first published 28 April 2014, https://doi.org/10.1155/2014/970157 (Introduction, Section 3).
3. A. K. Doan, *Local topological zeta functions of generic symmetric and catalecticant determinantal varieties*, arXiv:2610.23689 (16 October 2026), https://arxiv.org/abs/2610.23689 (Theorem 1.3, Lemma 7.3, Section 7).
4. Published record *Arithmetic determinant fibers of four-by-four Hankel matrices over finite fields* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-arithmetic-determinant-fibers-of-four-by-four-hankel-matrices-ov--ef46cabffa4c (four-by-four field comparison only).
