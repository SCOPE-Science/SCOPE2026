# Sharp bounded-variation stability of the four-point subdivision limit

## Finding

For real bi-infinite data \(f=(f_i)_{i\in\mathbb Z}\) of finite discrete total variation, let \(\mathcal S_\omega f\) be the continuous limit of the classical interpolatory four-point dyadic subdivision scheme
\[
 f^{k+1}_{2i}=f^k_i,\qquad
 f^{k+1}_{2i+1}=\left(\frac12+\omega\right)(f_i^k+f_{i+1}^k)-\omega(f_{i-1}^k+f_{i+2}^k).
\]
For every \(0\le\omega<1/8\), the limit exists uniformly and has a **sharp finite discrete-to-continuous total-variation norm** \(L(\omega)\). Define a finitely supported jump-difference sequence by \(d^{(0)}_i=\mathbf1_{\{i=0\}}\) and iterate
\[
 d^{(k+1)}_{2i}=\frac12d^{(k)}_i+\omega(d^{(k)}_{i-1}-d^{(k)}_{i+1}),\qquad
 d^{(k+1)}_{2i+1}=\frac12d^{(k)}_i-\omega(d^{(k)}_{i-1}-d^{(k)}_{i+1}).
\]
Set \(V_k=\sum_i|d_i^{(k)}|\) and \(W_k=\sum_i|d_i^{(k)}-d_{i-1}^{(k)}|\). Then, for every integer \(k\ge0\),
\[
 \boxed{L(\omega)=\lim_{k\to\infty}V_k},\qquad
 \boxed{V_k\le L(\omega)\le V_k+\frac{4\omega}{\frac12-4\omega}W_k}.
\]
Every \(L(\omega)\) is attained by a single-jump input. At the cubic-reproducing tension \(\omega=1/16\), this gives the rigorous numerical enclosure
\[
 \boxed{\frac{402935131604148261256695280}{309485009821345068724781056}
 \le L(1/16)\le
 \frac{402935354667284728311119600}{309485009821345068724781056}},
\]
so \(1.30195362<L(1/16)<1.30195436\). The full limiting scheme has strictly larger sharp variation gain than its first two refinements, whose gains are \(5/4\) and \(41/32\), respectively.

## Assumptions and scope

The input is a real sequence indexed by \(\mathbb Z\) satisfying \(V_{\mathbb Z}(f)=\sum_i|f_{i+1}-f_i|<\infty\). Constant sequences form the kernel of this seminorm. Each subdivision level is regarded as a piecewise-linear curve through its nodes at locations \(i/2^k\). The limiting output has continuous total variation \(\operatorname{Var}_{\mathbb R}\). The operator norm is \(\sup_{V_{\mathbb Z}(f)>0}\operatorname{Var}_{\mathbb R}(\mathcal S_\omega f)/V_{\mathbb Z}(f)\). The theorem covers the real scalar, uniform dyadic, bi-infinite interpolatory rule for \(0\le\omega<1/8\); it does not claim optimality of the chosen tension or a closed algebraic expression for the limiting constant.

## Proof

**1. First-difference refinement.** Put \(d_i=f_{i+1}-f_i\). Direct subtraction from the four-point rule gives the displayed recursion for \(d^{(k)}\). For arbitrary finite-variation input, the same linear recursion holds. Integer translation of an input jump corresponds after \(k\) refinements to a translation by \(2^k\) output edges. Hence any initial \(d^{(0)}\in\ell^1\) has \(d^{(k)}\) equal to the absolutely convergent superposition of shifted unit-jump responses, with
\[
 \|d^{(k)}\|_1\le V_k\|d^{(0)}\|_1.
\]
The single-jump input gives equality. The interpolatory property makes \(\|d^{(k)}\|_1\) nondecreasing in \(k\) for every input, by the triangle inequality on split edges.

**2. Contracting second differences.** Define \(e_i=d_i-d_{i-1}\). Exact subtraction yields
\[
 e^{(k+1)}_{2i}=\left(\frac12-2\omega\right)e_i^{(k)}-\omega(e_{i-1}^{(k)}+e_{i+1}^{(k)}),\quad
 e^{(k+1)}_{2i+1}=2\omega(e_i^{(k)}+e_{i+1}^{(k)}).
\]
For \(0\le\omega<1/8\), the sum of absolute output coefficients in each column is at most \(q=1/2+4\omega<1\). Therefore \(\|e^{(k)}\|_1\le q^k\|e^{(0)}\|_1\), and for the jump input \(W_{k+1}\le qW_k\).

**3. Existence of the limiting continuous curve.** Relative to linear interpolation of level \(k\), each new midpoint is displaced by \(\omega(d^{(k)}_{i-1}-d^{(k)}_{i+1})=-\omega(e_i^{(k)}+e_{i+1}^{(k)})\). The difference between the piecewise-linear curves of levels \(k+1\) and \(k\) has maximum magnitude at the inserted midpoints and is bounded by \(\omega\|e^{(k)}\|_1\). This is summable. Thus the curves converge uniformly to a continuous \(\mathcal S_\omega f\) for all finite-variation inputs.

**4. Limit variation and sharpness.** At each level, polygonal variation is exactly \(\|d^{(k)}\|_1\). Lower semicontinuity under uniform convergence gives \(\operatorname{Var}(\mathcal S_\omega f)\le\liminf_k\|d^{(k)}\|_1\). Conversely, the limiting curve agrees at every level's retained nodes, so \(\operatorname{Var}(\mathcal S_\omega f)\ge\|d^{(k)}\|_1\) for every \(k\). Therefore the variation equals \(\lim_k\|d^{(k)}\|_1\). Superposition from Step 1 bounds it by \(L(\omega)V_{\mathbb Z}(f)\), and one jump attains equality. Thus the limit of the jump-response norms is precisely the sharp operator norm, not merely a sampled lower bound.

**5. Explicit infinite-tail certificate.** For real \(a,b\), \(|a+b|+|a-b|=2\max\{|a|,|b|\}\). Applying this with \(a=d_i/2\) and \(b=\omega(d_{i-1}-d_{i+1})\) shows
\[
 V_{k+1}-V_k\le 2\omega\sum_i|d_{i-1}^{(k)}-d_{i+1}^{(k)}|\le4\omega W_k.
\]
Summing the geometric second-difference bound yields the claimed exact remainder inequality. At \(\omega=1/16\), \(q=3/4\), and the prefactor reduces to one, so \(V_k\le L(1/16)\le V_k+W_k\). Direct symbolic evaluation at the cubic-reproducing tension \(\omega=1/16\) gives \(V_1=5/4\) and \(V_2=41/32\). No formula for all tensions is inferred from these two values.

**6. Exact large-level instance.** At \(\omega=1/16\), write \(d_i^{(k)}=A_i^{(k)}/16^k\), where the \(A_i^{(k)}\) are integers. The recurrence becomes
\[
 A^{(k+1)}_{2i}=8A_i^{(k)}+A_{i-1}^{(k)}-A_{i+1}^{(k)},\quad
 A^{(k+1)}_{2i+1}=8A_i^{(k)}-A_{i-1}^{(k)}+A_{i+1}^{(k)}.
\]
After 22 levels, exact integer accumulation gives \(16^{22}=309485009821345068724781056\), \(\sum_i|A_i^{(22)}|=402935131604148261256695280\), and \(\sum_i|A_i^{(22)}-A_{i-1}^{(22)}|=223063136467054424320\). Substitution into Step 5 gives both rational bounds with no floating-point dependence.

## Verification

Compile `verify_fourpoint.cpp` with `g++ -O3 -std=c++17 verify_fourpoint.cpp -o verify_fourpoint`, then run `./verify_fourpoint 22`. It outputs the integer denominator, variation numerator, second-difference numerator and upper numerator stated above. Independent small-level rational calculations using Python `fractions.Fraction` agreed with the C++ recurrence for levels zero through eight. The numerical certificate is finite; the analytically proved tail inequality is what turns it into a valid infinite-level bound. The source code uses signed 128-bit integers at level 22 and has a hard level cap of 22 to avoid integer overflow.

## Relationship to prior work

The original four-point interpolatory scheme is due to Dyn, Gregory and Levin (1987). Their October 1988 report explicitly presents the same rule and analyzes continuity and differentiability through difference schemes. Amat, Dadourian and Liandrat (arXiv:0810.1146v1, October 7, 2008) analyze convergence and stability of nonlinear multiresolution schemes based on perturbations of linear subdivision, in supremum norm. Neither inspected text supplies the sharp infinite-refinement discrete-to-continuous total-variation norm of this fixed linear four-point rule, its jump-attainment formula, or the certified cubic-tension interval. These comparisons do not prove absolute historical novelty; the 1987 original article was not available in full text.

## Limitations

The theorem establishes a convergent recursive characterization and a certified narrow rational interval, not a closed elementary expression for \(L(1/16)\). The value outside the stated tension range, vector-valued data, other boundaries, finite-data endpoint conventions, and other subdivision masks remain unproved. The original 1987 paper's online record gives month/year, and the 1988 author's report gives month/year; no exact public day is inferred from those records. The day-verified archival lead in the metadata is the 2008 arXiv version, not a claim that the four-point scheme originated then.

## References

- N. Dyn, J. A. Gregory, D. Levin, *A 4-point interpolatory subdivision scheme for curve design*, Computer Aided Geometric Design 4 (1987), 257–268, DOI: https://doi.org/10.1016/0167-8396(87)90001-X.
- N. Dyn, J. A. Gregory, D. Levin, *Uniform subdivision algorithms for curves and surfaces*, Brunel University technical report TR/09/88 (October 1988), https://bura.brunel.ac.uk/bitstream/2438/2208/1/TR_09_88.pdf.
- S. Amat, K. Dadourian, J. Liandrat, *Analysis of a class of non linear subdivision schemes and associated multi-resolution transforms*, arXiv:0810.1146v1 (October 7, 2008), https://arxiv.org/pdf/0810.1146.
