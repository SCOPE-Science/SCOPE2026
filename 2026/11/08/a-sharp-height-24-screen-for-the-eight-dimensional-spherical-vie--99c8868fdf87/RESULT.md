# Which height-24 directions attain the eight-dimensional spherical obstruction constant?

## Finding

For a positive integer vector \(v=(v_1,\ldots,v_8)\), put
\[
d(v)=\min_{t\in\mathbb R}\sum_{i=1}^8\operatorname{dist}(tv_i-\tfrac12,\mathbb Z)^2.
\]
Let \(w=(1,2,3,4,5,7,9,11)\). Among all positive integer vectors with \(\max_i v_i\le24\), the only ones attaining the **known** eight-dimensional constant \(8/17\) are coordinate permutations of \(w\) and \(2w\). In particular, there is exactly one primitive attaining orbit in this box. The classification includes repeated coordinates; it does not assert unrestricted uniqueness.

## Assumptions and scope

The distance is squared Euclidean distance to the half-integral lattice, not the radius or the diameter-one scaling of the obstruction parameter. The height is the maximum coordinate of the vector itself. A direction may be scaled without changing its distance, but the height constraint need not survive scaling. When the speed cap of 24 used in Kahlon's six-dimensional direct screen is applied in dimension eight, the question here is which admissible directions can realize the now-known global value.

## Proof

For positive integer coordinates the function of \(t\) is periodic with period one and invariant under \(t\mapsto 1-t\). It therefore suffices to minimize on \([0,1/2]\). Sort the vectors, which preserves the distance. Assign each sorted vector to its final coordinate \(h\), so there are \(\binom{h+6}{7}\) vectors in that part: the first seven are a multiset drawn from \(\{1,\ldots,h\}\). This partitions the \(\binom{31}{8}=7{,}888{,}725\) sorted vectors without excluding multiples or repetitions.

Take the common refinement of the time intervals for all speeds \(1\) through \(24\): order the distinct fractions \(0,1/2\) and \(k/a\) with \(1\le a\le24\) and \(0<2k<a\). There are 90 resulting intervals. For an interval with midpoint \(m\), write \(c_a=2\lfloor am\rfloor+1\); then \(c_a/2\) is a nearest half-integer to \(at\) for every \(t\) in its interior. The same formula for the distance holds by continuity at both endpoints, even with ties or simultaneous crossings. Thus for a fixed vector the squared distance function on a closed interval is
\[
Q t^2-Bt+C/4,\qquad Q=\sum_i v_i^2,\quad B=\sum_i v_i c_{v_i},\quad C=\sum_i c_{v_i}^2.
\]
The minimizer on that interval is \(B/(2Q)\) clipped to its endpoints. At an interior minimizer the exact value is \((QC-B^2)/(4Q)\); at a selected endpoint \(n/d\) it is \((4Qn^2-4Bnd+Cd^2)/(4d^2)\).

The accompanying `verify_equality.py` rejects a vector only once a clipped interval minimum has been shown to be strictly less than \(8/17\). For every vector not rejected it checks all intervals and reports the exact minimum. All comparisons use integers: a fraction \(p/q\) is rejected exactly when \(17p<8q\). Since \(0<c_a\le a\) on the interior of this half-period, \(Q,B,C\le4608\); endpoint fractions have denominator at most 24 and numerator at most 12. Each squared coordinate fits the input integer type, and the stored sums, products and threshold comparisons are safely inside signed 64-bit range. The minimum calculation itself uses no rounding.

The complete census leaves exactly one survivor at height 11 (\(w\)), one at height 22 (\(2w\)), and none at any other height at most 24. Both exact minima are \(8/17\). For a direct check of the first direction, \(Q=306\) and the minimum is \(576/(4\cdot306)\), attained at \(t=8/51\) and \(25/51\) in \([0,1/2]\). The equality for the second follows also by rescaling time. This proves both directions of the boxed-height equality classification.

## Verification

Run `python3 verify_equality.py 1 24` with NumPy. The same check may be partitioned into disjoint ranges of final coordinates, using inclusive endpoints. It verifies the combinatorial size of each part and the exact list and scores of all threshold survivors. See `VERIFICATION.md` for the expected output and limits.

## Relationship to prior work and limitations

Hu Tan and Ying Zhang, *Euclidean View-Obstruction in Dimensions Eight to Ten and the Asymptotic Deficit*, [arXiv:2611.10782v1](https://arxiv.org/html/2611.10782v1), dated 7 November 2026, give \(\Delta_8=8/17\) and exhibit \(w\) in Theorem 1.1. The primitivity reduction and multiplication invariance are background. Their Section 4 and Appendix C certify the upper bound by excluding strict counterexamples, including a much larger finite norm-bounded census that contains the whole height-24 box. Equation (14) certifies a non-strict upper bound, not an exhaustive equality list in this box. Neither the bounded optimum value nor the unrestricted bound or attaining example is claimed here as a new result. The claim is the exact equality set for a specified speed budget; nothing is concluded about equality types above that budget. A separate equality census or material in supplementary data could affect priority.

V. Kahlon, *The View-Obstruction Problem for Spheres in Dimensions Six and Seven*, [arXiv:2610.37711v2](https://arxiv.org/html/2610.37711v2), uses the same squared-distance normalization; Section 6.4 describes a height-24 direct screen in dimension six, and Remark 7.3 identifies dimension eight as a next computational target.
