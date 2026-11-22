# A sharp asymmetric Hardy–Copson composition error and its unique jump extremizers

## Finding

Write \(Hf(x)=x^{-1}\int_0^x f(u)\,du\) and \(Rf(x)=(1-x)^{-1}\int_x^1 f(u)\,du\) for \(0<x<1\). These are constant-preserving one-sided averages. Set \(T=HR\), with the rightmost operator applied first, and \(T^{\mathrm{rev}}=RH\). For every real \(f\in BV(0,1)\), with distributional total variation \(V(f)=|Df|(0,1)\),

\[
\|f-Tf\|_{L^1(0,1)}\le C_*V(f),\qquad
\|f-T^{\mathrm{rev}}f\|_{L^1(0,1)}\le C_*V(f),
\]

and both constants are best possible. Define, for \(0<s<1\),

\[
A(s)=s+(1-s)\log(1-s),\quad
F(s)=(1-s)\operatorname{Li}_2(s)-A(s)\log s,
\]

where \(\operatorname{Li}_2(s)=\sum_{k\ge1}s^k/k^2\). There is a **unique** \(s_*\in(0,1)\) satisfying

\[
F'(s_*)=-1-\operatorname{Li}_2(s_*)+\log s_*\log(1-s_*)
-\frac{2(1-s_*)}{s_*}\log(1-s_*)=0.
\]

Precisely,

\[
s_*=0.589195414987420\ldots,\qquad
C_*=F(s_*)=0.410507498717943\ldots.
\]

Up to equality almost everywhere, the **only nonconstant equality inputs** for \(T\) are \(f(x)=a+b\mathbf1_{(s_*,1)}(x)\), for real \(a\) and nonzero real \(b\). For \(T^{\mathrm{rev}}\) replace \(s_*\) with \(1-s_*\). In particular, \(C_*>1/e\), the sharp constant for one application of \(H\) or \(R\). Thus two successive, oppositely directed averages yield a strictly larger worst-case integrated approximation error than one application, when error is normalized by original total variation.

## Assumptions and scope

The domain consists of real functions of bounded variation on the open interval \((0,1)\), identified up to Lebesgue-almost-everywhere equality. Here \(Df\) is their distributional derivative as a finite signed Radon measure on \((0,1)\); no endpoint jumps are counted. Averages use Lebesgue measure and are defined almost everywhere. The inequalities concern the \(L^1(0,1)\) distance from the identity, not the variation of the output and not the operator norms on \(L^1\). Constants have zero variation and zero error. Both orders of composition are considered for every finite-variation input; the proof is exact, without a discretization or smoothness assumption.

## Proof

**1. Exact response to a jump.** Let \(h_s(x)=\mathbf1_{(s,1)}(x)\) for \(0<s<1\). Direct integration gives

\[
Rh_s(u)=\begin{cases}(1-s)/(1-u),&0<u<s,\\1,&s\le u<1,\end{cases}
\]

and hence

\[
HRh_s(x)=\begin{cases}
-(1-s)\log(1-x)/x,&0<x\le s,\\
1-A(s)/x,&s<x<1.
\end{cases}
\]

Since \(A(s)>0\), the defect \(h_s-HRh_s\) is negative to the left of \(s\) and positive to its right. Its integrated absolute value is

\[
\begin{aligned}
\|(I-HR)h_s\|_1
&=(1-s)\int_0^s\frac{-\log(1-x)}x\,dx
+A(s)\int_s^1\frac{dx}{x}\\
&=(1-s)\operatorname{Li}_2(s)-A(s)\log s=F(s).
\end{aligned}
\]

These expressions also show that \(F\) extends continuously to \([0,1]\) with \(F(0)=F(1)=0\), and \(F(s)>0\) for interior \(s\).

**2. Uniqueness of the optimizing jump.** Differentiation produces the displayed formula for \(F'\) and

\[
F''(s)=\frac{2(1+s)}{s^2}\log(1-s)+\frac2s-\frac{\log s}{1-s}.
\]

We prove \(F'(s)>0\) for \(0<s\le1/5\). Put \(q=1-s\) and use the dilogarithm reflection identity \(\operatorname{Li}_2(s)+\operatorname{Li}_2(q)=\pi^2/6-\log s\log q\). Because \(\operatorname{Li}_2(q)\ge q+q^2/4\), \(-\log q\ge s+s^2/2\), and \(\log s\log q\ge0\),

\[
F'(s)\ge4q-\frac34q^2-1-\frac{\pi^2}6
\ge\frac{68}{25}-1-\frac{\pi^2}6>\frac4{75}>0.
\]

(The middle bound holds for \(4/5\le q<1\) since \(4q-3q^2/4\) is increasing; the final strict inequality uses \(\pi^2<10\).) For \(s\ge1/5\), use \(\log(1-s)\le-s-s^2/2\) to obtain

\[
F''(s)\le-3-s+\frac{-\log s}{1-s}<0.
\]

Indeed \((-\log s)/(1-s)\) is strictly decreasing on \((0,1)\), and its value at \(1/5\) is \(5\log5/4<5/2<3\). Finally, \(\lim_{s\uparrow1}F'(s)=-1-\pi^2/6<0\). Thus \(F'\) is positive up to \(1/5\), then strictly decreasing through exactly one zero, proving a unique strict global maximizer \(s_*\).

**3. From jumps to all BV functions.** Every real \(f\in BV(0,1)\) admits the almost-everywhere step-measure representation

\[
f(x)=c+\int_{(0,1)}h_s(x)\,Df(ds).
\]

Because \(HR\) preserves constants and is positive and bounded on \(L^\infty\), applying the defect operator and using Tonelli for the total-variation measure yields

\[
\|(I-HR)f\|_1\le\int_{(0,1)}F(s)\,|Df|(ds)
\le C_*|Df|(0,1).
\]

If equality holds with \(V(f)>0\), uniqueness of the maximizer in the second bound forces \(|Df|\) to be supported at \(\{s_*\}\); consequently \(f\) is a single nonzero jump there, plus a constant. Conversely each such input attains equality by step 1. This also establishes sharpness.

**4. Reverse order and strict comparison.** Reflection \(Jf(x)=f(1-x)\) preserves both \(V\) and \(L^1\) and satisfies \(JHJ=R\). Therefore \(J(HR)J=RH\), giving the same sharp constant and the reflected unique-jump location. For a single Hardy average, the jump error is \(-s\log s\), whose maximum over \((0,1)\) is \(1/e\). The strict comparison follows already at \(s=1/2\), since

\[
F(1/2)=\frac{\pi^2}{24}+\frac{\log2}{2}
-\frac{3(\log2)^2}{4}>1/e.
\]

For instance elementary rational bounds \(\pi>3.14\), \(0.69<\log2<0.70\), \(e>2.718\) suffice for the final strict inequality. This proves every assertion.

## Verification

The accompanying `check_hardy_copson.py` uses only the Python standard library. It computes the stationary point by bisection of the exact derivative; independently compares the dilogarithm formula with numerical quadrature of the step response and nested averaging; verifies multiple signed multi-jump BV inputs; and compares against \(1/e\). The checked run reports 59 direct step/composition comparisons and 65 signed-BV cases, all passing. These finite numerical checks are diagnostics, **not** substitutes for the global analytic proof above. Numerical decimals are nonessential approximate values; the exact result is the unique zero and its closed dilogarithm expression.

## Relationship to prior work

Gogatishvili and Mustafayev, *Weighted iterated Hardy-type inequalities* (arXiv:1503.04079v1, publicly posted 2015-03-13), analyze reduction and equivalence of weighted inequalities for positive iterated Hardy/Copson operators on monotone cones. Their theorems do not state this signed \(BV\)-to-\(L^1\) identity-defect norm or equality classification. Gogatishvili and coauthors, *Weighted inequalities for a superposition of the Copson operator and the Hardy operator* (arXiv:2109.03095v1, 2021), address weighted positive-function inequalities for superpositions; these do not directly imply the present sharp approximation error of \(I-HR\). Nekvinda and Pick's *Duals of Optimal Spaces for the Hardy Averaging Operator* concerns duals and optimal Banach function spaces, not this approximation problem. Previously computed variation-of-output bounds for compositions and error bounds for powers or mixtures of one-sided averages concern different seminorms/operators and cannot by themselves yield the present constant. The novelty assessment is relative to the literature inspected; no claim of exhaustive historical priority or independent certification is made.

## Limitations

The exact theorem is for unweighted Lebesgue averages on \((0,1)\), real BV inputs, and one application of each oppositely directed average in either order. It does not determine optimal constants for arbitrary weights, higher alternating products, multidimensional Hardy-type operators, or complex-valued equality cases. Source searches cannot exclude an unindexed equivalent older result, so historical priority remains provisional. The supplied numerical checks do not establish the infinite-dimensional statement without the proof.

## References

1. A. Gogatishvili and R. Mustafayev, *Weighted iterated Hardy-type inequalities*, arXiv:1503.04079v1 (2015-03-13), https://arxiv.org/abs/1503.04079 .
2. A. Gogatishvili, Z. Mihula, L. Pick, H. Turčinová, and T. Ünver, *Weighted inequalities for a superposition of the Copson operator and the Hardy operator*, arXiv:2109.03095v1 (2021-09-07), https://arxiv.org/abs/2109.03095 .
3. A. Nekvinda and L. Pick, *Duals of Optimal Spaces for the Hardy Averaging Operator*, accessible preprint, https://www.karlin.mff.cuni.cz/kma-preprints/2010-pap/2010-345.pdf .
