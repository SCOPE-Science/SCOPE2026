# The sharp quadratic power bound for positive absolutely Cesàro operators on unital AM-spaces

## Finding

Let \(X\) be a real or complex unital AM-space whose distinguished positive order unit \(e\) satisfies \(\|e\|=1\) and \(\|x\|=\inf\{c\geq0:|x|\leq ce\}\), and let \(T:X\to X\) be a bounded positive linear operator. Its optimal absolute Cesàro constant is
\[
K_{\mathrm{ac}}(T)=\sup_{N\geq1}\sup_{\|x\|\leq1}\frac1N\sum_{j=0}^{N-1}\|T^jx\|.
\]
If \(K_{\mathrm{ac}}(T)<\infty\), then
\[
\boxed{\sup_{n\geq0}\|T^n\|\leq K_{\mathrm{ac}}(T)^2.}
\]
The coefficient and exponent are simultaneously optimal: **for every real \(K>1\)**,
\[
\boxed{\sup\{\sup_{n\geq0}\|T^n\|:T\geq0\text{ on a finite-dimensional }\ell_\infty^d,\ K_{\mathrm{ac}}(T)=K\}=K^2.}
\]
The supremum over finite-dimensional examples is approached by explicit nilpotent positive weighted backward shifts. Thus positivity turns absolute Cesàro boundedness into power boundedness on every unital AM-space, with a best possible universal quantitative law. The reverse implication holds for arbitrary bounded operators, by averaging their uniformly bounded powers.

## Assumptions and scope

The space may be identified isometrically as \(C(\Omega)\) for a compact Hausdorff \(\Omega\); this includes finite \(\ell_\infty^d\) and suitable \(L^\infty\)-spaces. No reflexivity, compactness of \(T\), invertibility, or spectral hypothesis is imposed. Positivity means \(x\geq0\Rightarrow Tx\geq0\). The bound applies to the **optimal absolute Cesàro constant** with sums from time zero; it is not a statement about ordinary Cesàro boundedness of \(\frac1N\sum T^j\) without absolute values. Here \(K_{\mathrm{ac}}(T)\geq1\), and \(K_{\mathrm{ac}}(T)=1\) forces \(\|T\|\leq1\).

## Proof

**Step 1 (order-unit reduction).** For every \(n\geq0\), positivity gives \(|T^nx|\leq T^n|x|\leq\|x\|T^ne\). Hence
\[
a_n:=\|T^n\|=\|T^ne\|\geq0,\qquad a_0=1.
\]
Because the same vector \(e\) attains every power norm, the optimal Cesàro constant obeys the exact scalar identity
\[
K_{\mathrm{ac}}(T)=\sup_{N\geq1}\frac1N\sum_{j=0}^{N-1}a_j.
\]
The power-norm sequence is submultiplicative: \(a_{j+k}\leq a_ja_k\).

**Step 2 (sharp universal upper bound).** For every integer \(n\geq1\) and \(0\leq j\leq n\), submultiplicativity yields \(a_ja_{n-j}\geq a_n\). Pair the terms with reverse indices and apply arithmetic-geometric mean:
\[
\sum_{j=0}^n a_j=\frac12\sum_{j=0}^n(a_j+a_{n-j})
\geq\sum_{j=0}^n\sqrt{a_ja_{n-j}}
\geq(n+1)\sqrt{a_n}.
\]
The defining bound \(\sum_{j=0}^na_j\leq(n+1)K_{\mathrm{ac}}(T)\) gives \(a_n\leq K_{\mathrm{ac}}(T)^2\). At \(n=0\), \(a_0=1\leq K_{\mathrm{ac}}(T)^2\). No limiting or spectral argument is used.

**Step 3 (exact finite-dimensional witnesses).** Fix \(N\geq2\) and \(c>1\). On \(\ell_\infty^{N+1}\) put
\[
(T_{N,c}x)_i=w_ix_{i+1}\quad(0\leq i<N),\qquad (T_{N,c}x)_N=0,
\]
where \(w_0=w_{N-1}=c\) and \(w_i=1\) for \(1\leq i\leq N-2\). These are two positive spikes separated by \(N-2\) unit weights. For every \(1\leq j<N\), a product of \(j\) consecutive weights contains at most one spike, and some such product contains one spike; for \(j=N\) the unique product contains both. Thus
\[
\|T_{N,c}^0\|=1,\quad \|T_{N,c}^j\|=c\ (1\leq j<N),\quad \|T_{N,c}^N\|=c^2,\quad \|T_{N,c}^j\|=0\ (j>N).
\]
The averages of these scalar norms increase strictly until the first \(N+1\) terms have been included, then decrease. Consequently the **exact** optimal absolute Cesàro constant is
\[
K_{\mathrm{ac}}(T_{N,c})=\frac{1+(N-1)c+c^2}{N+1}=c+\frac{(c-1)^2}{N+1},
\qquad \sup_{j\geq0}\|T_{N,c}^j\|=c^2.
\]
For any prescribed \(K>1\), the equation \(c+(c-1)^2/(N+1)=K\) has a unique solution \(c_N>1\) and \(c_N\to K\) as \(N\to\infty\). Every \(T_{N,c_N}\) therefore has **exactly** the same optimal absolute Cesàro constant \(K\), while its maximum power norm tends to \(K^2\). This proves sharpness on finite-dimensional \(C(\Omega)\)-spaces. For \(K=1\), the identity operator realizes equality \(1\).

## Verification

All inequalities are algebraic consequences of positivity, the defining order-unit norm, scalar submultiplicativity, and AM–GM. The finite-dimensional construction is verified by direct products of the displayed weights, with the actual all-vector absolute Cesàro constant reduced to the order-unit vector. The accompanying exact-arithmetic Python check verifies the entire power-norm list and each prefix average over representative dimensions and rational spike sizes. This finite check supplements, and does not replace, the proof for all spaces, all \(K\) and all dimensions.

## Relationship to prior work

Abbar, Arnold and Coine (2026) prove positive absolute Cesàro self-improvement on \(L^p\) for \(1<p<\infty\), using different lattice estimates; their investigated text does not state this finite-dimensional sharp quadratic endpoint. Arnold (2026) develops sharp self-improvement thresholds for general \(p\)-absolute Cesàro bounds; its accessible abstract does not assert an AM-space endpoint, but the entire manuscript was not inspected. Cohen, Cuny, Eisner and Lin (2020) already show that simultaneous absolute Cesàro boundedness of an operator and its adjoint implies power boundedness. Their standard two-sided argument can itself yield a quadratic upper estimate after positivity and the order-unit property are used. **The upper estimate in isolation is not claimed as new.** The distinct contribution assessed here is the **proof of optimality of the exact function \(K\mapsto K^2\)** under the single positive AM-space assumption, proved with a universal argument and a matching two-spike family. A published finite-horizon absolute-Cesàro extremal result concerns \(\ell^p\) with finite \(p\) and does not directly imply this AM-space endpoint. No claim is made that the qualitative power-boundedness implication is new.

## Limitations

The theorem requires positivity and a norming order unit. It makes no assertion for general Banach spaces, for \(L^p\) with \(1\leq p<\infty\), or for nonpositive operators on \(C(\Omega)\). The constant \(K^2\) is a supremum over dimensions and can be approached without necessarily being attained at a finite power for \(K>1\). An older implicit sharp AM-space endpoint result or an inaccessible full manuscript could weaken the originality assessment. Independent external verification has not been performed.

## References

- A. Abbar, L. Arnold and C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1 (first submitted 21 September 2026), especially Theorem 2.1 and Section 3. https://arxiv.org/abs/2609.24601
- L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1 (first submitted 24 September 2026). https://arxiv.org/abs/2610.00271
- G. Cohen, C. Cuny, T. Eisner and M. Lin, *Resolvent conditions and growth of powers of operators*, J. Math. Anal. Appl. (2020), particularly Proposition 2.1. https://doi.org/10.1016/j.jmaa.2020.124035
- *Sharp finite-horizon power amplification under absolute Cesàro bounds*, published mathematical finding, October 2026, record `2026/10/11/SCOPE-sharp-finite-horizon-power-amplification-under-absolute-ces-ro-b--1b6cb9a310fc`; comparison is confined to its accessible summary.
