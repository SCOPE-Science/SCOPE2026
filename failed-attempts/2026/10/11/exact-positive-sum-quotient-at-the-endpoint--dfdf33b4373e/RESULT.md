# Exact positive-sum quotient at the endpoint
## Finding
Let \(I=[0,1]\) and let
\[
S_1^+=\{f\in C^1(I): f(0)\ge0,\ f'\ge0,\ f(0)+\|f'\|_\infty=1\}.
\]
For \(f\in S_1^+\), define
\[
m_f=\|f'\|_\infty,\qquad \delta_f(t)=f'(t)-m_f.
\]
Then \(\delta_f\in C(I)\), \(-1\le\delta_f\le0\), and \(\max_I\delta_f=0\). For every \(f,g\in S_1^+\),
\[
\boxed{\ \|f+g\|_{(1)}=2+\max_{t\in I}(\delta_f(t)+\delta_g(t))\ }.
\]
Thus the complete pairwise positive-sum data of \(f\) depends only on the normalized derivative deficit \(\delta_f\).

More precisely, for \(f,h\in S_1^+\), the following are equivalent:

1. \(\|f+g\|_{(1)}=\|h+g\|_{(1)}\) for every \(g\in S_1^+\);
2. \(\delta_f=\delta_h\);
3. \(h'-f'\) is a constant function.

For every continuous \(\delta:I\to[-1,0]\) with \(\max_I\delta=0\), set \(a_\delta=-\min_I\delta\). The whole equivalence class associated with \(\delta\) is exactly
\[
f_{\delta,M}(t)=1-M+\int_0^t(\delta(s)+M)\,ds,
\qquad a_\delta\le M\le1.
\]
Therefore, if for each such \(\delta\) one chooses any surjection
\[
\theta_\delta:[a_\delta,1]\to[a_\delta,1],
\]
then
\[
T(f_{\delta,M})=f_{\delta,\theta_\delta(M)}
\]
defines a surjective norm-additive self-map of \(S_1^+\). The affine functions \(f_r(t)=r+(1-r)t\) form exactly the fiber \(\delta=0\); the affine-fiber permutations used in the motivating endpoint counterexample are therefore one special case of a fiberwise non-rigidity that occurs for every non-singleton fiber.

## Assumptions and scope
The scalar field is real. The space is \(C^1([0,1])\) with the endpoint norm \(\|f\|_{(1)}=|f(0)|+\|f'\|_\infty\), and only its positive unit sphere \(S_1^+\) is considered. Here positivity means \(f(0)\ge0\) and \(f'\ge0\), exactly as in the motivating source.

The statement classifies indistinguishability for the two-point datum \(g\mapsto\|f+g\|_{(1)}\) and constructs a large family of norm-additive self-maps. It does not classify all surjective norm-additive self-maps, because a map may also act nontrivially on the quotient variable \(\delta\) while preserving the kernel \(\max_I(\delta+\eta)\).

## Proof
Fix \(f,g\in S_1^+\), and write \(m=m_f\) and \(n=m_g\). Since \(f(0)=1-m\) and \(g(0)=1-n\), while \(f'=m+\delta_f\) and \(g'=n+\delta_g\), positivity gives
\[
\begin{aligned}
\|f+g\|_{(1)}
&=f(0)+g(0)+\|f'+g'\|_\infty\\
&=2-m-n+\max_{t\in I}\bigl(m+n+\delta_f(t)+\delta_g(t)\bigr)\\
&=2+\max_{t\in I}\bigl(\delta_f(t)+\delta_g(t)\bigr).
\end{aligned}
\]
This proves the boxed identity and the forward direction of the indistinguishability criterion.

For the converse, suppose \(f,h\in S_1^+\) satisfy
\[
\|f+g\|_{(1)}=\|h+g\|_{(1)}
\quad\text{for every }g\in S_1^+.
\]
The derivative map sends \(S_1^+\) bijectively onto
\[
B^+=\{u\in C(I):0\le u\le1\}.
\]
Indeed, from \(u\in B^+\) one recovers a sphere point by taking initial value \(1-\|u\|_\infty\) and derivative \(u\). Applying the boxed identity to all such test derivatives shows
\[
\max_I(\delta_f+u)=\max_I(\delta_h+u)
\quad\text{for every }u\in B^+.
\]
For a continuous \(\delta:I\to[-1,0]\) with \(\max_I\delta=0\), define
\[
R_\delta(x)=\inf\left\{\max_I(\delta+u):u\in B^+,\ u(x)=1\right\}.
\]
For every admissible \(u\), evaluation at \(x\) gives \(\max_I(\delta+u)\ge1+\delta(x)\). Conversely, for every \(\varepsilon>0\), continuity provides a neighborhood \(O\) of \(x\) on which \(\delta(t)<\delta(x)+\varepsilon\). Choose a continuous \(u:I\to[0,1]\) with \(u(x)=1\) and support contained in \(O\). On \(O\), \(\delta+u\le\delta(x)+1+\varepsilon\); outside \(O\), \(\delta+u=\delta\le0\le\delta(x)+1+\varepsilon\). Hence
\[
R_\delta(x)=1+\delta(x).
\]
Equality of the test functionals for \(\delta_f\) and \(\delta_h\) therefore gives \(\delta_f(x)=\delta_h(x)\) for every \(x\in I\). Thus \(\delta_f=\delta_h\). By definition this is equivalent to
\[
h'-f'=m_h-m_f,
\]
a constant function.

Now fix \(\delta\) as above. If \(f\) has \(\delta_f=\delta\) and \(M=\|f'\|_\infty\), then \(f'=\delta+M\). Nonnegativity is equivalent to \(M\ge-\min_I\delta\), and the unit-sphere condition gives \(f(0)=1-M\), so necessarily \(M\le1\). This yields exactly the displayed fiber \(f_{\delta,M}\). Conversely every \(M\) in that interval produces a member of \(S_1^+\) with deficit \(\delta\).

Finally, the boxed identity is unchanged when \(M\) is replaced by any other allowed parameter in the same fiber. Therefore any family of surjections \(\theta_\delta\) defines a surjective self-map preserving every positive-sum norm, hence a surjective norm-additive map.

## Verification
The proof uses only the defining norm, compactness of \(I\), continuity, and elementary bump functions. No finite experiment, numerical approximation, or external computation is used.

Boundary cases are included. If \(\delta=0\), then \(a_\delta=0\) and the fiber is the full affine interval \(f_r(t)=r+(1-r)t\). If \(-\min_I\delta=1\), the fiber is a singleton, so its only surjection is the identity. If \(f'\equiv0\), then \(m_f=0\) and the same formulas remain valid.

A direct reverse check of the fiber parametrization gives \(f_{\delta,M}(0)=1-M\ge0\), \(f_{\delta,M}'=\delta+M\ge0\), \(\|f_{\delta,M}'\|_\infty=M\), and therefore \(\|f_{\delta,M}\|_{(1)}=1\).

## Relationship to prior work
Ezumi and Miura introduce the endpoint norm and positive sphere, and their Counterexample 6.1 uses the affine family \(f_r(t)=r+(1-r)t\). They observe that whenever at least one member of a pair is affine, the positive-sum norm equals \(2\), and they use an arbitrary bijection of that affine family to obtain a surjective norm-additive map that need not have the rigid representation valid for \(p>1\). They do not state the quotient formula above, the converse characterization of pairwise indistinguishability, or the full constant-shift fiber decomposition.

Their general star-set lemma for positive unit spheres of \(C(K)\) explains why maximal-sum relations are natural invariants, but it is a sup-norm result on \(C(K)\) and does not identify the endpoint \(C^1\) fibers. The present formula shows that the affine counterexample is the \(\delta=0\) fiber of a larger exact quotient structure.

Enami, Hirota, Koshimizu, and Lin study surjective isometries on the same positive unit spheres for all \(p\); their accessible abstract states extension rigidity for isometries, a strictly stronger mapping hypothesis than norm-additivity. Chen, Dong, and Zheng study norm-additive maps on maximal groups of strictly positive continuous functions with the supremum norm, a different domain and geometry. Sun and Sun study positive unit spheres of sequence spaces. None of these inspected statements gives the endpoint constant-shift quotient above.

## Limitations
The theorem identifies exactly what the two-point positive-sum data cannot see, but it does not classify automorphisms of the quotient kernel
\[
(\delta,\eta)\longmapsto\max_I(\delta+\eta).
\]
Accordingly it is not a classification of all surjective norm-additive self-maps of \(S_1^+\).

The closest same-space comparator by Enami, Hirota, Koshimizu, and Lin was available through its public abstract, while a full-text extraction attempt failed; no whole-document noncoverage claim is made for that paper. Its stated subject is surjective isometries rather than norm-additive maps, so this access limitation leaves a residual but non-decisive originality risk. A second residual risk is an older equivalent observation formulated in terms of max-plus kernels, normalized positive cones, or quotienting by constant functions.

## References
1. Kazuki Ezumi and Takeshi Miura, *Norm-Additive Maps on the Positive Unit Sphere of \(C^1([0,1])\)*, arXiv:2610.02862v1, 2026.
2. Yuta Enami, Daisuke Hirota, Hironao Koshimizu, and Min-Ruei Lin, *Surjective isometries on the positive parts of the unit spheres of some function spaces*, arXiv:2606.30952v1, 2026.
3. Lihong Chen, Yunbai Dong, and Bentuo Zheng, *On Norm-Additive Maps Between the Maximal Groups of Positive Continuous Functions*, Results in Mathematics 74 (2019), article 152, DOI 10.1007/s00025-019-1076-x.
4. Longfa Sun and Yinghua Sun, *On Extension of Norm-Additive Maps Between the Positive Unit Spheres of \(\ell_q(\ell_p)\)*, Results in Mathematics 79 (2024), DOI 10.1007/s00025-024-02154-y.
