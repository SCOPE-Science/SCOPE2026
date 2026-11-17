# Complete-monotonic trace-square law for arctangent commutators

## Finding
Let \(P=-i\,d/dx\) and \(Qf(x)=xf(x)\) be the canonical momentum and position operators on \(L^2(\mathbb R)\), and for every real \(s>0\) put
\[
C_s=i[\arctan(P/s),\arctan(Q/s)].
\]
The commutator is Hilbert--Schmidt for every \(s>0\). Define
\[
G(t)=t\arctan(t/2)-\log(1+t^2/4),\qquad t>0.
\]
Its exact squared Hilbert--Schmidt norm is
\[
T(s):=\operatorname{Tr}(C_s^2)=\|C_s\|_{\mathcal S_2}^2
=\pi\int_0^\infty e^{-2s^2t}\frac{G(t)}{t^2}\,dt.
\]
In particular the function \(x\mapsto T(\sqrt{x})\) is **strictly completely monotone** for \(x>0\): for every integer \(j\ge0\),
\[
(-1)^j\frac{d^j}{dx^j}T(\sqrt x)>0.
\]
The formula gives the sharp two-scale limits
\[
T(s)=\pi^2\log(1/s)+O(1)\quad(s\downarrow0),
\]
\[
T(s)=\frac{\pi}{8s^2}-\frac{\pi}{384s^6}
+\frac{\pi}{1280s^{10}}+O(s^{-14})\quad(s\to\infty).
\]
Moreover, at every \(s>0\), the following sharp-asymptotic global bounds hold:
\[
\frac{\pi}{8s^2}-\frac{\pi}{384s^6}
\le T(s)\le\frac{\pi}{8s^2}-\frac{\pi}{384s^6}
+\frac{\pi}{1280s^{10}}.
\]
On the positive trace-class range \(s\ge1\) already established in the motivating article, \(\operatorname{Tr} C_s=\pi/2\). Consequently its spectral effective rank
\[
R(s)=\frac{(\operatorname{Tr} C_s)^2}{\operatorname{Tr}(C_s^2)}
\]
is strictly increasing and obeys
\[
R(s)=2\pi s^2\left(1+\frac{1}{48s^4}+O(s^{-8})\right),
\qquad s\to\infty.
\]

## Assumptions and scope
The Hilbert space is complex \(L^2(\mathbb R,dx)\) and the Fourier transform is normalized by \(\widehat f(\xi)=(2\pi)^{-1/2}\int e^{-ix\xi}f(x)\,dx\). The bounded functional calculi of the self-adjoint operators \(P,Q\) define \(C_s\) for each \(s>0\). The trace-square claims and complete-monotonicity assertions are independent of any positivity assumption; the effective-rank statement uses positivity and trace class only for \(s\ge1\), a theorem of Frank--Ivanisvili. No claim is made about positivity for smaller \(s\).

## Proof
**1. Kernel and Hilbert--Schmidt reduction.** The Fourier transform of \(s/(s^2+\xi^2)\) is \(\sqrt{\pi/2}\,e^{-s|x|}\). The commutator calculation, also given in Frank--Ivanisvili, Lemma 6, yields the real symmetric integral kernel
\[
C_s(x,y)=\frac12e^{-s|x-y|}
\frac{\arctan(x/s)-\arctan(y/s)}{x-y},
\]
with the quotient on the diagonal interpreted as \(s/(s^2+x^2)\). Since this quotient is bounded by \(1/s\) and the difference of the two arctangents is bounded by \(\pi\), its square has integrable diagonal differences after the calculation below. Let \(u=x/s\), \(v=y/s\) and put \(t=|u-v|\). The Jacobian and the squared quotient cancel the factors of \(s\), giving
\[
\|C_s\|_{\mathcal S_2}^2
=\frac12\int_0^\infty e^{-2s^2t}\frac{J(t)}{t^2}\,dt,
\quad
J(t)=\int_{\mathbb R}[\arctan(u+t)-\arctan u]^2\,du.
\]
All exchanges of nonnegative integrands in the following steps are justified by Tonelli.

**2. Exact Cauchy autocorrelation.** Write \(p(u)=1/(1+u^2)\). Since \(\arctan(u+t)-\arctan u=\int_0^t p(u+v)\,dv\) and
\[
\int_{\mathbb R}p(u+v)p(u+w)\,du
=\frac{2\pi}{4+(v-w)^2},
\]
we obtain
\[
J(t)=4\pi\int_0^t\frac{t-r}{4+r^2}\,dr
=2\pi[t\arctan(t/2)-\log(1+t^2/4)]
=2\pi G(t).
\]
For example the autocorrelation identity follows by Fourier transforming the two Cauchy kernels, or by elementary residues. This proves the exact one-dimensional integral, and hence the Hilbert--Schmidt property, since \(G(t)/t^2\to1/4\) at zero and \(G(t)/t^2=O(1/t)\) at infinity.

**3. Complete monotonicity.** An elementary differentiation gives \(G'(t)=\arctan(t/2)>0\) and \(G(0)=0\). Differentiating the Laplace integral for \(x=s^2>0\) therefore gives, for every integer \(j\ge0\),
\[
(-1)^j\frac{d^j}{dx^j}T(\sqrt x)
=2^j\pi\int_0^\infty e^{-2xt}t^{j-2}G(t)\,dt>0.
\]
Differentiation is justified by exponential domination for each \(x>0\). Strictness also proves that \(T(s)\) is strictly decreasing in \(s\).

**4. Large-scale coefficients and valid global bounds.** For every real \(y\ge0\), finite geometric-series integration gives
\[
y-y^3/3\le\arctan y\le y-y^3/3+y^5/5,
\]
and the next alternating term bounds the remainder. Integrating with \(y=t/2\) gives
\[
\frac{t^2}{4}-\frac{t^4}{96}
\le G(t)\le\frac{t^2}{4}-\frac{t^4}{96}+\frac{t^6}{960}.
\]
Inserting these inequalities in the positive Laplace integral, and using \(\int_0^\infty e^{-at}t^k\,dt=k!/a^{k+1}\), proves the displayed global two-sided bounds. Keeping the next term in the alternating expansion and using its global remainder bound yields the three-term large-\(s\) expansion with remainder \(O(s^{-14})\).

**5. Small-scale logarithm.** As \(t\to\infty\),
\[
G(t)=\frac{\pi}{2}t+O(\log(2+t)),\qquad
\frac{G(t)}{t^2}=\frac{\pi}{2t}+O\left(\frac{\log(2+t)}{t^2}\right).
\]
The error term is integrable on \([1,\infty)\), uniformly after multiplication by \(e^{-2s^2t}\), while the contribution from \((0,1)\) is bounded. Thus
\[
T(s)=\frac{\pi^2}{2}\int_1^\infty\frac{e^{-2s^2t}}{t}\,dt+O(1)
=\pi^2\log(1/s)+O(1).
\]
The second equality is the elementary logarithmic asymptotic of the exponential integral.

**6. Effective rank.** For \(s\ge1\), the positivity and trace identity \(\operatorname{Tr}C_s=\pi/2\) are the established results of Frank--Ivanisvili, Theorem 1 and Proposition 4 (not re-proved here). Their trace formula and our strictly decreasing \(T(s)\) give strictly increasing \(R(s)\). Inverting the large-scale expansion yields the stated effective-rank formula. This measures spreading of a fixed total positive spectral mass across increasingly many effective eigenvalues.

## Verification
The included `checker.py` uses only Python 3 standard-library arithmetic. It verifies the first three expansion coefficients exactly using `fractions.Fraction`, and performs finite independent numerical diagnostics for eight scales, global bounds, monotonicity and the Cauchy autocorrelation. These diagnostics do not establish the infinite-dimensional theorem: Steps 1--6 above supply its analytical proof.

## Relationship to prior work
Frank and Ivanisvili, *A counterexample to the Kato conjecture for positive commutators* (arXiv:2608.07805v1, first submitted 2026-08-07), prove positivity and the trace \(\pi/2\) in the appropriate scaled family and derive the integral kernel used in Step 1 (their Lemma 6, equation (13)). Their primary MSC is 47B47. Those results are prior input, not new claims. Their stated contributions are positivity, Kato's converse counterexample, kernel factorization, trace and estimates of an auxiliary operator; the searched paper does not state an exact trace-square profile, complete monotonicity, its two scale asymptotics, or the effective-rank law. The older Howland--Kato literature concerns the positivity/analytic-strip classification rather than this spectral concentration profile. It remains possible that a general semiclassical or positive-commutator formula elsewhere implies a part of the result; the displayed exact Laplace density and global scale law are the differentiating statements.

## Limitations
The exact formula concerns \(\mathcal S_2\), not the full singular-value distribution or individual eigenvalues. The logarithmic divergence as \(s\downarrow0\) is a Hilbert--Schmidt statement, not a claim that \(C_s\) remains positive or has a trace formula there. The effective-rank formula uses the known positivity regime \(s\ge1\). The result does not characterize positivity thresholds, provide a full spectral decomposition, or assert originality beyond the accessible comparisons described above.

## References
1. R. L. Frank and P. Ivanisvili, *A counterexample to the Kato conjecture for positive commutators*, arXiv:2608.07805v1 (2026-08-07), https://arxiv.org/abs/2608.07805 (open text: https://pdfs.assets.alphaxiv.org/2608.07805v1.pdf).
2. R. Froese and I. Herbst, *The Howland--Kato commutator problem. II*, Journal of Operator Theory 93 (2025), 393--412, DOI:10.7900/jot.2023may20.2470.
3. I. Herbst and T. L. Kriete, *The Howland--Kato Commutator Problem*, arXiv:1804.05227v1 (2018).
