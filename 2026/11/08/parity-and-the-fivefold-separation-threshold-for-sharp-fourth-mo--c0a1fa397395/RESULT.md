# Parity and the fivefold separation threshold for sharp fourth moments of two monomials

## Finding

Let \(0\le \ell<h\) be integers and let \(\mu=dx/2\) be normalized Lebesgue measure on \([-1,1]\). Set
\[
M_{\ell,h}=\operatorname{span}_{\mathbb R}\{x^\ell,x^h\},\qquad
K_{\ell,h}=\sup_{0\ne f\in M_{\ell,h}}\frac{\|f\|_{L^4(\mu)}^4}{\|f\|_{L^2(\mu)}^4}.
\]
The sharp \(L^2\)-to-\(L^4\) embedding norm is \(K_{\ell,h}^{1/4}\). Define the rational parameters
\[
A=\frac{(2\ell+1)^2}{4\ell+1},\quad
B=\frac{(2h+1)^2}{4h+1},\quad
C=\frac{3(2\ell+1)(2h+1)}{2\ell+2h+1}.
\]
For opposite parity, that is, \(\ell+h\) odd, there is a **sharp, exact lacunarity transition**:
\[
\boxed{K_{\ell,h}=\begin{cases}
\dfrac{C^2-AB}{2C-A-B},&h\le 5\ell+1,\\[5pt]
B,&h\ge5\ell+3.
\end{cases}}
\]
In the first regime *every* maximizer has nonzero coefficients of both powers, and its squared \(L^2\)-energy in the higher-degree monomial is exactly
\[
s_* = \frac{C-A}{2C-A-B}\in(0,1).
\]
Equivalently, for \(f(x)=a x^\ell+b x^h\), its maximizing coefficient magnitudes obey
\[
\boxed{\frac{b^2}{a^2}=\frac{2h+1}{2\ell+1}\,\frac{C-A}{C-B}}.
\]
Either choice of the two coefficient signs is possible, as is any common nonzero scalar. In the second regime precisely the nonzero multiples of \(x^h\) maximize. No boundary equality case is omitted: opposite parity forbids \(h=5\ell+2\).

For same parity, \(\ell+h\) even, neither monomial alone can maximize \(K_{\ell,h}\); every maximizer necessarily uses both monomials. This is a separate exact structural obstruction, not a claim of a closed formula for the same-parity norm.

There is also a uniform large-degree interpretation. For opposite-parity pairs with \(\ell\to\infty\) and \(h/\ell\to\tau>1\),
\[
\frac{K_{\ell,h}}{\ell}\longrightarrow
\begin{cases}
\dfrac{\tau(\tau^2-34\tau+1)}{(\tau+1)(\tau^2-10\tau+1)},&1<\tau\le5,\\[5pt]
\tau,&\tau\ge5.
\end{cases}
\]
The branches agree at \(\tau=5\). Thus the integer fivefold separation is the exact discrete version of a limiting sharp transition at degree ratio five.

## Assumptions and scope

All exponents are nonnegative integers with \(0\le\ell<h\). Coefficients are real, the domain is the symmetric interval \([-1,1]\), and the underlying measure is \(dx/2\). The supremum is over all nonzero functions in the specified two-dimensional space. The choice of symmetric measure is essential: opposite-parity powers are \(L^2\)-orthogonal and have vanishing odd mixed fourth moments. The result makes no claim for complex coefficients or other moment exponents.

## Proof

**1. Exact moment reduction.** For every nonnegative integer \(j\),
\[
\int_{-1}^1 x^j\,\frac{dx}{2}=
\begin{cases}0,&j\text{ odd},\\(j+1)^{-1},&j\text{ even}.\end{cases}
\]
When \(\ell+h\) is odd, all mixed terms of odd coefficient multiplicity vanish in both the second and fourth moments. If \(f(x)=a x^\ell+b x^h\), write
\[
L=\frac{a^2}{2\ell+1},\quad H=\frac{b^2}{2h+1},\quad s=\frac H{L+H}.
\]
The second moment equals \(L+H\) and the fourth moment equals \(AL^2+BH^2+2CLH\). Consequently
\[
\frac{\|f\|_4^4}{\|f\|_2^4}=Q(s):=A(1-s)^2+Bs^2+2Cs(1-s),\qquad 0\le s\le1.
\]
Conversely, each \(s\in[0,1]\) is realized by a real polynomial in the space. One also has \(A<B\), since \((2z+1)^2/(4z+1)\) is strictly increasing for nonnegative \(z\).

**2. The exact integer barrier.** A direct rational identity gives
\[
C-B=-\frac{2(2h+1)[2h^2-(10\ell+4)h-(2\ell+1)]}
{(4h+1)(2h+2\ell+1)}.
\]
The quadratic expression \(P_\ell(h)=2h^2-(10\ell+4)h-(2\ell+1)\) has exactly one positive root. It satisfies
\[
P_\ell(5\ell+2)=-(2\ell+1)<0,
\qquad P_\ell(5\ell+3)=8\ell+5>0.
\]
Because \(\ell+h\) odd, \(h=5\ell+2\) is inadmissible. It follows that \(C>B\) exactly when \(h\le5\ell+1\), and \(C<B\) exactly when \(h\ge5\ell+3\). These inequalities are strict for every admissible pair.

**3. Sharp optimization and all equality cases.** If \(C>B>A\), then \(D=2C-A-B>0\) and
\[
Q(s)=\frac{C^2-AB}{D}-D\left(s-\frac{C-A}{D}\right)^2.
\]
Its unique maximizing energy share is \(s_*=(C-A)/D\in(0,1)\), with the stated value and coefficient ratio. In particular, the *exact improvement over the pure higher monomial* is
\[
K_{\ell,h}-B=\frac{(C-B)^2}{D}>0.
\]
If \(C<B\), then for every \(0\le s<1\),
\[
Q(s)-B=(A-B)(1-s)^2+2(C-B)s(1-s)<0,
\]
so the unique energy maximizer is \(s=1\), corresponding exactly to nonzero multiples of the higher monomial. The fourth-moment expression depends only on \(a^2,b^2\), so both independent sign choices are allowed in the mixed branch.

**4. Same-parity obstruction.** If \(\ell+h\) is even, the two monomials have the same parity. Consider the fourth-to-second moment quotient of \(f_t(x)=x^h+t x^\ell\). Differentiating its logarithm at \(t=0\) gives
\[
\left.\frac{d}{dt}\log\frac{\|f_t\|_4^4}{\|f_t\|_2^4}\right|_{t=0}
=4\left(\frac{4h+1}{3h+\ell+1}-\frac{2h+1}{h+\ell+1}\right)
=\frac{-8h(h-\ell)}{(3h+\ell+1)(h+\ell+1)}<0.
\]
Thus the higher monomial is not even stationary. If \(\ell\ge1\), the analogous logarithmic derivative for \(x^\ell+t x^h\) at zero is strictly positive, as the same numerator becomes \(8\ell(h-\ell)\). If \(\ell=0\), the lower monomial is constant and has moment ratio \(1\), strictly below the higher monomial's ratio \(B>1\). Therefore no pure monomial maximizes in the same-parity case. Compactness of the projective unit circle ensures existence of a maximizer, which must be mixed.

**5. Large-degree limit.** Divide \(A,B,C\) by \(\ell\) along \(h/\ell\to\tau>1\). Their limits are respectively \(1\), \(\tau\), and \(6\tau/(1+\tau)\). Substitute in the sharp finite formulas and simplify. The two limit branches meet at \(\tau=5\), so sequences approaching the transition from either side yield the same limit.

## Verification

The accompanying standalone Python program evaluates the moments by an independent binomial expansion with exact rational integration; it tests every opposite-parity pair in the stated finite grid against the sharp branch and energy-share identities. It also checks the same-parity local obstruction. To reproduce, run `python check_muntz.py` using Python 3 without third-party packages. A successful run prints `ALL_MUNTZ_TWO_POWER_CHECKS_PASSED`. The finite tests are cross-checks only; the universally quantified conclusions follow from the proof above.

Examples: the pair \((\ell,h)=(0,1)\) has \(K_{0,1}=9/4\), with mixed extremizers. The pair \((\ell,h)=(0,3)\) has \(K_{0,3}=49/13\), with only the cubic monomial extremal. In general, the sharp transition occurs between the last opposite-parity degree not exceeding \(5\ell+1\) and the first one at least \(5\ell+3\).

## Relationship to prior work

Borwein and Erdélyi's *Müntz spaces and Remez inequalities* (public arXiv version dated 1995-01-01) establishes density and Remez-type properties of Müntz spaces. Borwein, Erdélyi, and Zhang's *Müntz systems and orthogonal Müntz–Legendre polynomials* develops \(L^2\) orthogonality, reproducing kernels, derivative bounds, and other Nikolskii-type estimates, rather than the exact \(L^2\)-to-\(L^4\) constant on parity-split two-monomial spaces. The elementary two-vector quadratic-moment reduction is not itself claimed as new: the proposed contribution is the exact, all-integer fivefold threshold, complete equality cases, and same-parity obstruction. Targeted comparison did not identify a published stronger statement implying this particular sharp exponent-gap law. Unindexed or implicit treatments remain a priority risk.

## Limitations

The exact norm formula requires opposite parity and real coefficients. For same parity only the no-pure-extremizer conclusion is proved; the exact norm there is not determined. No assertion is made for more than two degrees, arbitrary measures, complex coefficient fields, or other \(L^p\) targets. The priority assessment is a best-effort literature comparison and is not an independent mathematical validation.

## References

1. P. Borwein and T. Erdélyi, *Müntz spaces and Remez inequalities*, Bull. Amer. Math. Soc. 32 (1995), 38–42; arXiv:math/9501225 (first indexed public version 1995-01-01), https://arxiv.org/abs/math/9501225.
2. P. Borwein, T. Erdélyi and J. Zhang, *Müntz systems and orthogonal Müntz–Legendre polynomials*, Trans. Amer. Math. Soc. 342 (1994), 523–542, doi:10.1090/S0002-9947-1994-1227091-4. An accessible full-text rendering is https://citeseerx.ist.psu.edu/document?doi=ce01bb0e4711c4738f03ccf1563ccb2f11364c1f&repid=rep1&type=pdf.
