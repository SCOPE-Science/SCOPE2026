# Exact two-transition packing law for three cylinders with prescribed conical axes

## Finding

Three congruent, infinite right circular cylinders are externally tangent to the Euclidean unit ball, have disjoint interiors, and have three prescribed, cyclically spaced **axis directions**. Their axis-line offsets are otherwise unrestricted. For every polar parameter \(0\le c<1\), the exact largest common radius has the closed formula below; the maximizing configuration need not inherit the cyclic symmetry of the directions.

Write the oriented representatives of the prescribed (unoriented) axis directions as
\[
v_j(c)=\left(\sqrt{1-c^2}\cos\frac{2\pi j}{3},\sqrt{1-c^2}\sin\frac{2\pi j}{3},c\right),\qquad j=0,1,2.
\]
Put
\[
k=\frac{1-3c^2}{1+3c^2},\quad q=\sqrt{2-2k},\quad k_*=\frac{7+\sqrt{17}}{16},
\]
and define
\[
g(k)=\begin{cases}
1+q/2,&k\ge k_*,\\
\displaystyle\frac{q(2-k)+\sqrt{2(1-k^2)(9-7k)}}{5-4k},&-1/2<k<k_*.
\end{cases}
\]
Then the sharp radius is
\[
\boxed{R(c)=\frac{T(c)}{2-T(c)},\quad T(c)=\max\{q,g(k)\}.}
\]
There are two exact transitions. At \(c=1/\sqrt3\) (three mutually perpendicular directions), the optimal separation-sign pattern switches from mixed to unanimous. At
\[
\boxed{c_*=\sqrt{\frac{1-k_*}{3(1+k_*)}}=0.2448168692\ldots,}
\]
the mixed-sign optimum changes from two pairwise cylinder contacts to three. Thus the optimal configurations explicitly constructed below have **exactly two** pairwise contacts for \(0\le c<c_*\), and all three pairs in contact for \(c_*\le c<1\). When \(0<c<1/\sqrt3\), the mixed pattern strictly beats any unanimous pattern; for \(1/\sqrt3<c<1\), the converse holds. At the switch both patterns are optimal.

The endpoints include \(R(0)=1\), \(R(1/\sqrt3)=1+\sqrt2\), and \(\lim_{c\uparrow1}R(c)=3+2\sqrt3\). The last is a limit only: the prescribed directions become parallel at \(c=1\), outside the stated domain. In particular, \(R(c)>R(1/\sqrt3)\) for \(c<1/\sqrt3\) sufficiently close to \(1/\sqrt3\); mutual orthogonality is not locally optimal when the common inclination is allowed to vary.

## Assumptions and scope

A radius-\(r\) solid cylinder with direction \(v_j\) has an axis line \(p_j+\mathbb R v_j\), where \(p_j\cdot v_j=0\). It is externally tangent to the unit ball precisely when \(\|p_j\|=1+r\). Cylinder interiors are disjoint when every two corresponding axis lines have distance at least \(2r\). The three axes are required only to have the stated *directions*; their points of tangency, azimuths, and offsets can all vary independently. No symmetry of the actual cylinders is assumed. Tangency between cylinders (equality of an axis separation with \(2r\)) is permitted.

The interval \(0\le c<1\) ensures each pair of axis directions is nonparallel. All assertions are for genuine nonnegative finite \(r\), with exact Euclidean distances.

## Proof

**1. Skew-line reduction.** Let \(s=1+r\), \(x_j=p_j/s\), and cyclically set
\[
w_j=\frac{v_j\times v_{j+1}}{\|v_j\times v_{j+1}\|},\qquad d_j=(x_j-x_{j+1})\cdot w_j.
\]
Here \(\|x_j\|=1\) and \(x_j\perp v_j\). The distance between axes \(j\) and \(j+1\) equals \(s|d_j|\). Direct cross-product calculation gives \(w_j\cdot w_{j+1}=k\). The largest attainable normalized minimum line distance is
\[
T=\max_{\substack{x_j\perp v_j\\\|x_j\|=1}}\min_j|d_j|.
\]
Since \(2r\le (1+r)T\), the optimal radius is \(T/(2-T)\), provided the computed \(T<2\), as it is for \(c<1\).

**2. Convex dual with all offset freedom retained.** For any choice of signs \(\sigma\in\{-1,1\}^3\), temporarily relax the unit circles to the three unit disks. Compact convex minimax gives the exact signed optimum
\[
t_\sigma=\min_{\substack{\lambda_j\ge0\\\sum_j\lambda_j=1}}
\sum_{j=0}^2\left\|\lambda_j\sigma_jw_j-\lambda_{j-1}\sigma_{j-1}w_{j-1}\right\|.
\]
Indeed, maximizing the signed minimum is the same as maximizing the minimum over the probability simplex of weighted signed gaps. Interchanging maximum and minimum of this bilinear form is valid on compact convex domains. Each \(w_j\) is perpendicular to the two adjacent axes, so the support function of the corresponding disk is exactly the displayed Euclidean norm, without omitted projections. The original unsigned maximum is the maximum of \(t_\sigma\) over eight sign choices, provided disk equality is attainable on the circles; explicit witnesses in step 4 establish this.

Up to cyclic relabelling and simultaneous reversal of all signs, there are only the unanimous pattern \((+,+,+)\) and the mixed pattern \((+,+,-)\).

**3. Exact dual minimization.** In the unanimous pattern, cyclic averaging of the convex dual objective forces a minimum at \(\lambda_j=1/3\), of value \(q=\sqrt{2-2k}\). In the mixed pattern, reflection averaging permits \(\lambda_0=\lambda_1=a\) and \(\lambda_2=b=1-2a\), with \(0\le a\le1/2\), reducing the dual to
\[
f(a)=a q+2\sqrt{a^2+(1-2a)^2+2ka(1-2a)}.
\]
The convex one-variable objective has its minimum at
\[
a=\begin{cases}1/2,&k\ge k_*,\\
\displaystyle\frac{2-k-(1-k)\sqrt{(1+k)/(9-7k)}}{5-4k},&k<k_*.
\end{cases}
\]
For the second branch, this follows by solving \(f'(a)=0\); the first branch follows from the derivative at the right endpoint and gives the exact breakpoint \(k_*\). Substitution yields \(g(k)\) as stated. For \(k<k_*\),
\[
\frac{g(k)}q=\frac{2-k+\sqrt{(1+k)(9-7k)}}{5-4k}.
\]
Subtracting one and using
\[
(1+k)(9-7k)-9(1-k)^2=4k(5-4k)
\]
shows that the sign of \(g-q\) equals the sign of \(k\). For \(k\ge k_*\), \(g=1+q/2>q\). Since \(k=0\) exactly at \(c=1/\sqrt3\), this proves the primary switch.

**4. Sharp primal witnesses and cylinder contacts.** With \(q>0\), define the unanimous witnesses
\[
x_j^{\mathrm{un}}=\frac{w_j-w_{j-1}}q.
\]
They are unit vectors perpendicular to the required \(v_j\), and all three signed gaps equal \(q\).

For the mixed pattern, take the minimizing \(a\), put \(b=1-2a\) and \(N=\sqrt{a^2+b^2+2kab}\), and set
\[
x_0^{\mathrm{mix}}=\frac{a w_0+b w_2}{N},\quad
x_1^{\mathrm{mix}}=\frac{w_1-w_0}{q},\quad
x_2^{\mathrm{mix}}=-\frac{a w_1+b w_2}{N}.
\]
All three are unit and perpendicular to their corresponding axes. The signed gaps are
\[
d_0=d_1=\frac q2+\frac{a+bk}{N},\qquad -d_2=\frac{2(ak+b)}{N}.
\]
For \(k<k_*\), the stationary equation \(q+2((5-4k)a+k-2)/N=0\) makes all three equal to \(g(k)\). For \(k\ge k_*\), \(a=1/2\), \(b=0\), and \(d_0=d_1=g(k)\) while \(-d_2=2k\ge g(k)\), with strict inequality for \(k>k_*\). This proves the secondary contact transition and sharpness of the disk relaxation. For \(c=0\), where \(q=0\), the normal vectors all coincide; the mixed optimum \(T=1\) is attained by \(x_0=w_0\), \(x_2=-w_0\), and any unit \(x_1\perp v_1,w_0\), producing absolute gaps \((1,1,2)\). Multiplication by \(s=1+R(c)\) gives actual tangent cylinders with the announced contacts, completing the proof.

## Verification

The standalone `verify.py` uses only the Python standard library. For 1001 distinct parameters in \((0,1)\), it reconstructs the three three-dimensional directions, their cross-product normals, the optimal signed dual value by an **independent golden-section minimization**, and both explicit primal witnesses. It checks the line-separation equalities, perpendicularity/unit constraints, strict active-set inequalities away from their thresholds, and exact distinguished parameter values. It prints `PASS 1001 cone values` on successful execution.

These finite computations corroborate, but do not replace, the analytic minimax and closed-form derivations.

## Relationship to prior work

Glazyrin (2026) studies the unrestricted number-versus-radius packing problem and quotes the known unrestricted three-cylinder optimum \(3+2\sqrt3\). That upper bound, attained by parallel cylinders, does not determine an exact optimum when three specified *nonparallel* axis directions are mandatory. Ogievetsky and Shlosman (2018/2019) analyze a threefold-symmetric six-cylinder family and certain three-line subconfigurations, obtaining general skew-line distance formulas and a different six-cylinder extremum. They do not establish a three-cylinder maximum over all offsets for the fixed cone-direction triple, or its two sharp contact transitions. The present theorem explicitly optimizes over **all** offsets at fixed directions.

## Limitations

The result assumes exactly three cylinders with the prescribed conical direction triple, not arbitrary triples of directions, arbitrary numbers of cylinders, or finite cylinders. The formula at \(c=1\) is only a limiting statement, not an assertion under the nonparallel-lines derivation. Two-contact and three-contact statements concern the explicit maximizing placements; no claim is made that there are no distinct maximizers beyond the exhibited symmetry-related ones. Priority against older literature using alternative cylinder-direction parametrizations is not exhaustively resolved.

## References

1. A. Glazyrin, *Upper bounds for packings of cylinders around the unit sphere*, arXiv:2611.00251v1, 30 October 2026, https://arxiv.org/html/2611.00251v1 .
2. O. Ogievetsky and S. Shlosman, *The Six Cylinders Problem: \(\mathbb D_3\)-symmetry Approach*, arXiv:1805.09833v2 (first released 24 May 2018), https://arxiv.org/html/1805.09833v2 .
3. E. W. Cheney, *Introduction to Approximation Theory*, Chelsea, 1982: standard finite-dimensional convex minimax principles; no special theorem from this reference is claimed beyond the stated compact convex minimax identity.
