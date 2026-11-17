# Exact finite-summand moduli for logarithmic Lorentz gauges

## Finding

Fix a real number \(k>0\). On finitely supported real or complex sequences let \(x^*\) be the decreasing rearrangement of absolute coordinate values, and define the logarithmic Lorentz gauge
\[Q_k(x)=\sum_{j\ge1}(1+(\log j)^k)x_j^*.\]
For every integer \(n\ge2\), its sharp finite-summand constant is
\[C_{n,k}=\sup_{x_1,\dots,x_n\ne0}\frac{Q_k(x_1+\cdots+x_n)}{\sum_{i=1}^n Q_k(x_i)}.\]
Put \(\Phi_k(0)=0\) and \(\Phi_k(m)=\sum_{j=1}^m(1+(\log j)^k)\) for positive integers \(m\). **The precise all-\(n\) formula is**
\[\boxed{C_{n,k}=\max_{S\ge1}\frac{\Phi_k(S)}{(n-r)\Phi_k(m)+r\Phi_k(m+1)},\qquad S=nm+r,\quad 0\le r<n.}\]
In particular this is an attained *finite maximum*, not merely a supremum, and at least one sharp family consists of \(n\) equal-height indicators of pairwise-disjoint coordinate blocks whose sizes are \(m\) and \(m+1\), with exactly \(r\) larger blocks. The formula also holds with supremum (possibly infinite) for an arbitrary positive nondecreasing rank-weight sequence in place of the logarithmic weights.

This reduction is not the assertion that singleton vectors always extremize: for \(n=k=2\), the two disjoint five-coordinate indicators give the rigorously attained lower bound
\[C_{2,2}\ge\frac{\Phi_2(10)}{2\Phi_2(5)}\approx1.6808888313>\frac{\Phi_2(2)}2\approx1.2402265070.\]
These displayed decimals are illustrations, not a claimed globally maximizing block size.

## Assumptions and scope

The gauge \(Q_k\) is the specific rearrangement gauge of Corollary 4.2 of Cabello Sánchez–Castillo–Martínez-Bohórquez–Navarro Garmendia (2026), an equivalent quasi-norm on their logarithmic Orlicz model; the theorem concerns **this exact gauge**, not the different equivalent Luxemburg or coordinate-entropy gauges. Finite-support sequences are used to exhibit equality. The bounds extend by truncation to the completion. Take natural logarithms and the convention \((\log1)^k=0\).

## Proof

Let \(w_1\le w_2\le\cdots\) be arbitrary positive increasing rank weights; write \(\Phi(m)=\sum_{j=1}^m w_j\) and \(Q_w(x)=\sum_j w_j x_j^*\). First, **merging coordinates never increases the increasing-weight rearrangement gauge**: when two nonnegative coordinates of a finite vector are replaced by their sum and zero, the resulting vector majorizes the original; if \(a\) majorizes \(b\) with equal total sum, summation by parts gives
\[\sum_{j=1}^N w_j a_j^*-\sum_{j=1}^N w_j b_j^*=-\sum_{j=1}^{N-1}(w_{j+1}-w_j)\left(\sum_{s=1}^j a_s^*-\sum_{s=1}^j b_s^*\right)\le0.\]
Since \(|\sum_i x_i|\le\sum_i|x_i|\) coordinatewise, padding with zeroes and repeatedly merging the coordinate lists therefore yields
\[Q_w(x_1+\cdots+x_n)\le Q_w(|x_1|\oplus\cdots\oplus|x_n|).\]
Here \(\oplus\) denotes disjoint concatenation of coordinate lists.

Second, for a nonnegative finitely supported vector \(z\) the layer-cake identity, by Tonelli's theorem, is
\[Q_w(z)=\int_0^\infty\Phi(\#\{j:z_j>t\})\,dt.\]
Let \(m_i(t)=\#\{j:|x_{ij}|>t\}\). The previous inequality and layer cake imply that the sharp \(n\)-summand constant is at most
\[\sup_{m_1,\ldots,m_n\in\mathbb N_0,\,\sum m_i>0}\frac{\Phi(m_1+\cdots+m_n)}{\Phi(m_1)+\cdots+\Phi(m_n)}.\]
Conversely, disjoint indicator blocks of respective cardinalities \(m_i\) attain the ratio inside this supremum. This proves equality for arbitrary increasing positive weights, even when the result is infinite.

Third, \(\Phi\) is discretely convex because its forward differences \(w_{m+1}\) are nondecreasing. Given \(S=\sum_i m_i=nm+r\), transferring one unit from a block of size at least two greater than another block cannot increase the denominator, since
\[\Phi(a-1)+\Phi(b+1)-\Phi(a)-\Phi(b)=w_{b+1}-w_a\le0\quad(a\ge b+2).\]
Iterating leaves \(n-r\) blocks of size \(m\) and \(r\) blocks of size \(m+1\). This proves the boxed exact formula.

Finally take \(w_j=1+(\log j)^k\) for fixed \(k>0\). The standard integral comparison gives \(\Phi_k(M)/M\sim(\log M)^k\) as \(M\to\infty\). For fixed \(n\), if \(S=nm+r\to\infty\), then \(m\to\infty\) and
\[\frac{\Phi_k(S)}{(n-r)\Phi_k(m)+r\Phi_k(m+1)}\longrightarrow1.\]
At \(S=n\), the ratio \(\Phi_k(n)/n\) exceeds \(1\), since \(w_1=1\) and \(w_j>1\) for \(j\ge2\). Thus the global supremum is attained among finitely many positive integers \(S\). The \(n=k=2\) lower bound is substitution of \(S=10,m=5,r=0\); its strict comparison with \(S=2\) follows, for example, from explicit high-precision interval evaluation of the finite logarithmic sums, or from standard elementary logarithm bounds. No infinite search is invoked to prove this comparison.

## Verification

The accompanying stand-alone script checks the finite formula against independently generated small integer compositions and evaluates the displayed finite-block example. These tests diagnose implementations; the proof above establishes the full arbitrary-length statement. Run \(`python3 check.py`\) in the directory containing the extracted files. No external scientific package is required.

## Relationship to prior work

The 2026 Serre-closure paper defines \(c(n;X)\), identifies the equivalent Lorentz rearrangement gauge, and proves logarithmic-order bounds, not the exact finite-summand extremal formula for this gauge. The same paper uses a **different equivalent gauge** for its explicit lower bound, so those constants must not be conflated. Earlier general research on \(q\)-convexity and triangle inequalities in Lorentz spaces (Kamińska–Parrish, 2008; Barza–Kolyada–Soria, 2009) concerns related sharp norms but does not, on the material inspected, resolve these *finite-\(n\), growing-weight, nonuniform* constants. A published 2026 logarithmic-summand asymptotic for a different concave Orlicz gauge does not provide isometric exact values here.

## Limitations

The formula is a discrete one-parameter maximum; it does not give a closed-form maximizing integer for every \(n,k\), nor the complete set of all equality vectors. The finite-block numerical example does not claim global optimality of block size five. Isometric constants are specific to \(Q_k\), and equivalent quasi-norms can have different sharp constants. Exact earlier finite-\(n\) weighted-Lorentz results under different notation remain a publication-priority risk; the referenced older papers were not exhaustively available as full text.

## References

1. F. Cabello Sánchez, J. M. F. Castillo, R. Martínez-Bohórquez, J. Navarro Garmendia, *The Serre closure of Banach spaces*, arXiv:2610.35259 (first publicly available 2026-10-26), especially Corollary 4.2 and Lemma 4.3. https://arxiv.org/abs/2610.35259
2. A. Kamińska, A. M. Parrish, *Convexity and concavity constants in Lorentz and Marcinkiewicz spaces*, Journal of Mathematical Analysis and Applications 343 (2008), 337–351. https://doi.org/10.1016/j.jmaa.2008.01.034
3. S. Barza, V. Kolyada, J. Soria, *Sharp constants related to the triangle inequality in Lorentz spaces*, Transactions of the American Mathematical Society 361 (2009), 5555–5574. https://arxiv.org/abs/0709.0647
