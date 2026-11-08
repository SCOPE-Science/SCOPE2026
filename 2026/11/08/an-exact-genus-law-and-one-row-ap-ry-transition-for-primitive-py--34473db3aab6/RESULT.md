# An exact genus law and one-row Apéry transition for primitive Pythagorean quadruple semigroups

## Finding
Let \(n,p,m\) be positive integers with
\[\gcd(n,p)=1,\qquad Q=n^2+p^2<m,\qquad \gcd(m,Q)=1,\qquad m+n+p\equiv1\pmod2.\]
Consider the numerical semigroup
\[S=\langle A,D,B,C\rangle,\quad A=2mn,\quad D=2mp,\quad B=m^2-Q,\quad C=m^2+Q.\]
Write \(g(S)=|\mathbb Z_{\ge0}\setminus S|\) for its **genus** (not its Frobenius number). Define \(t\in\{0,\ldots,n-1\}\) uniquely by \(pt\equiv Q-m\pmod n\); when \(n=1\), take \(t=0\). Put \(\ell=Q+p(n-t)-m\). Then
\[
\boxed{g(S)=\frac{m^3-Q+1}{2}+m(np-n-p)-\frac{t}{n}\max(0,\ell).}
\]
In particular, the departure from the cubic baseline is **exactly** the arithmetic condition \(t>0\) and \(Q<m<Q+p(n-t)\); the correction is a nonnegative integer. Every admissible \(m\ge Q+p(n-1)\) has no correction, which sharpens the uniform earlier regime \(m\ge2Q\) in which the base representatives are known.

More precisely, define \(W(v,z)=2mpv+m^2|z|+Qz\). The complete Apéry set \(\operatorname{Ap}(S,A)\) is given by all \(W(v,z)\) with \(0\le v<n\), \(-m\le z<m\), with the sole exception that, if \(t>0\) and \(\ell>0\), each of the \(t\) entries \(W(v,m-1)\) with \(n-t\le v<n\) is replaced by \(W(v+t-n,-m-1)\). Each replacement decreases its entry by \(2m\ell\). When the exception is inactive, no entry is replaced.

## Assumptions and scope
The hypotheses ensure positive generators and \(\gcd(B,2m)=1\) because \(B\) is odd and \(\gcd(m,Q)=1\); also \(\gcd(A,D)=2m\), so \(S\) is cofinite. No assumption that \(n<p\) or that \(m\ge2Q\) is imposed. The theorem concerns coprime \(n,p\) and the entire range \(m>Q\), including the subthreshold band \(Q<m<2Q\). It does not assert any formula for noncoprime \(n,p\), for \(m\le Q\), or for other geometric invariants of associated semigroup curves.

## Proof
**1. Normalization to a finite residue family.** Since \(nD=pA\), any semigroup element has a presentation
\[uA+vD+xB+yC,\qquad u,v,x,y\ge0,\]
with \(0\le v<n\). Let \(s=\min(x,y)\), \(z=y-x\). Then
\[xB+yC=2sm^2+m^2|z|+Qz.\]
Choose the unique \(v_0\in\{0,\ldots,n-1\}\) with \(pv_0\equiv pv+ms\pmod n\). The element is
\[W(v_0,z)+uA+2m[p(v-v_0)+ms].\]
The final bracket is divisible by \(n\). If \(s=0\), then \(v_0=v\) and the bracket vanishes. If \(s\ge1\), it is at least \(m-p(n-1)>0\) because \(Q=n^2+p^2>p(n-1)\). Thus every element in each residue class is obtained by adding a *nonnegative multiple of* \(A\) to some \(W(v,z)\), with \(0\le v<n\) and arbitrary integral \(z\). Conversely every such \(W(v,z)\) is in \(S\), by choosing either \(|z|\) copies of \(B\) or \(z\) copies of \(C\).

**2. Distinct baseline residues.** The \(2mn=A\) values \(W(v,z)\) for \(0\le v<n\), \(-m\le z<m\) occupy distinct residues modulo \(A\). Indeed, reducing an equality modulo \(m\) and using \(\gcd(m,Q)=1\) shows that \(z-z'\) is a multiple of \(m\). Since \(|z-z'|<2m\), a nonzero option would be \(\pm m\). Modulo \(2m\), this is impossible: \(|z|-|z'|\equiv z-z'\pmod2\), and \(m^2-Q=B\) is odd, so the difference of the \(W\) values is odd in units of \(m\), not divisible by \(2m\). Therefore \(z=z'\), and \(n\mid p(v-v')\) forces \(v=v'\). Hence the baseline values form a complete residue system.

**3. All possible competitors.** Fix a baseline index \((v_0,z_0)\). Any competing \(W(v,z)\) with the same residue has \(z=z_0+2mk\) for some integer \(k\) (the preceding parity argument still excludes odd multiples of \(m\) for unrestricted \(z\)). Its difference is
\[\Delta=2mp(v-v_0)+m^2(|z_0+2mk|-|z_0|)+2mQk.\]
For \(k\ge1\), the bound \(|z_0+2mk|-|z_0|\ge2m(k-1)\) gives
\[\frac{\Delta}{2m}\ge (k-1)m^2+kQ-p(n-1)>0.\]
For \(k=-j\) with \(j\ge2\), \(|z_0-2mj|-|z_0|\ge2m(j-1)+2\), so
\[\frac{\Delta}{2m}\ge (j-1)m^2+m-jQ-p(n-1)>0.\]
The last inequality follows because the right-hand side increases with \(j\), and at \(j=2\) it exceeds \(m^2+m-3Q>0\) for integral \(m>Q\ge2\). For \(k=-1\) and \(z_0\le m-2\), similarly
\[\frac{\Delta}{2m}\ge2m-Q-p(n-1)>0.\]
Thus an improvement is possible *only* at \(k=-1\) and \(z_0=m-1\).

**4. The unique boundary transition.** At this exceptional boundary, the alternative has index \(z=-m-1\), and
\[\frac{\Delta}{2m}=m-Q+p(v-v_0).\]
For the residue to agree modulo \(A\), one must have \(p(v-v_0)\equiv Q-m\pmod n\). Therefore \(v\equiv v_0+t\pmod n\). If \(t=0\), then \(v=v_0\) and \(\Delta>0\). If \(t>0\) and \(v_0<n-t\), then \(v=v_0+t\) and again \(\Delta>0\). For precisely the remaining \(t\) values \(n-t\le v_0<n\), one has \(v=v_0+t-n\), giving
\[\frac{\Delta}{2m}=m-Q-p(n-t)=-\ell.\]
When \(\ell>0\) this is a strict improvement by \(2m\ell\), and otherwise the baseline is minimal (with possible ties when \(\ell=0\)). Consequently the stated set is exactly \(\operatorname{Ap}(S,A)\). Notice \(\ell\equiv0\pmod n\) when \(t>0\), guaranteeing integrality of the correction.

**5. Sum the representatives.** The baseline sum is
\[\sum_{v=0}^{n-1}\sum_{z=-m}^{m-1}W(v,z)=n(m^4-Qm)+2m^2pn(n-1),\]
using \(\sum_{z=-m}^{m-1}|z|=m^2\) and \(\sum_{z=-m}^{m-1}z=-m\). Each of the \(t\) possible replacements, when active, reduces this sum by \(2m\ell\). The standard Apéry gap-count identity
\[g(S)=\frac1A\sum_{w\in\operatorname{Ap}(S,A)}w-\frac{A-1}{2}\]
then yields the boxed cubic formula and the exact correction. Finally, since \(p(n-1)<Q\), any \(m\ge Q+p(n-1)\) makes \(\ell\le0\), as claimed.

## Verification
An independent integer-only program, `verify.py`, constructs the semigroup's Apéry representatives using Dijkstra shortest paths on residues modulo \(A\) with generators \(B,C,D\); it neither presumes the theorem nor uses its proof to compute the shortest paths. It separately constructs the asserted replaced baseline array, checks every residue and value, and verifies both genus expressions. On coprime \(1\le n,p\le7\) and admissible \(m\) drawn from a subthreshold neighborhood and the transition beyond \(2Q\), it checked 512 parameter triples, including 76 with nonzero genus correction. The largest directly checked modulus was 2,086. Run `python verify.py`; exact expected output is in `verification_output.txt`. Finite checks do not prove the universal claim; the proof above handles all admissible integers.

## Relationship to prior work
Hwang and Song [1] consider exactly these four generators and prove a Frobenius-*number* formula under the stronger \(m\ge2Q\) condition in the coprime case, using a complete residue system. The present result concerns the distinct invariant **genus** and determines its exact formula and full Apéry representatives throughout \(m>Q\), including the subthreshold band not treated by their explicit formula. The earlier 2026 research result [2] derives a sharp Frobenius-number correction for \(Q<m<2Q\) and supplies a general congruence-class membership decomposition. That decomposition gives computational access to the semigroup, so the new finding does not claim first knowledge of semigroup membership. It does not, however, state the genus, the all-parameter cubic formula, or the single-boundary-row Apéry transition and its exact count. Extracting this explicit classification requires comparing all infinitely many lifted representatives and calculating their total correction; this is supplied above. Older results [3] concern three-generator Pythagorean triple semigroups and do not directly give this four-generator genus formula. Standard Apéry identities are used as known background, not claimed as new.

## Limitations
The proof requires \(\gcd(n,p)=1\) and \(m>n^2+p^2\), and says nothing about the noncoprime branch or smaller \(m\). The baseline becomes valid by the stated bound, but no claim is made that this bound is always individually sharp for every fixed \((n,p)\); exact activity is governed by \(t\) and \(\ell\). An explicit membership description was previously available, making historical priority of intermediate representations qualified. Search and full-text comparisons do not prove global novelty, and independent mathematical audit has not been performed.

## References
1. WonTae Hwang and Kyunghwan Song, “Frobenius Numbers Associated with Primitive Pythagorean Quadruples,” arXiv:2609.21397v1, first posted 18 September 2026, https://arxiv.org/abs/2609.21397.
2. “Exact subthreshold Frobenius correction for primitive Pythagorean quadruples,” published-finding corpus 2026/10/4/SCOPE-exact-subthreshold-frobenius-correction-for-primitive-pythagorea--3f9d1229d594, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-subthreshold-frobenius-correction-for-primitive-pythagorea--3f9d1229d594.
3. Edgar Federico Elizeche and Amitabha Tripathi, “On numerical semigroups generated by primitive Pythagorean triplets,” Integers 20 (2020), A75.
4. E. S. Selmer, classical Apéry-set genus formula (standard numerical-semigroup identity).
